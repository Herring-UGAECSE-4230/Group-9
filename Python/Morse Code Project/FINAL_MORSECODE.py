import RPi.GPIO as GPIO
from time import sleep
import time

# setting gpio pins to telegraph, led, speaker 
TELEGRAPH_PIN = 21
LED_PIN = 16
SPEAKER_PIN = 27

# gpio setups 
GPIO.setmode(GPIO.BCM)
GPIO.setup(TELEGRAPH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(SPEAKER_PIN,GPIO.OUT)
speaker = GPIO.PWM(SPEAKER_PIN,50) # (pin, 50% Duty Cycle)


# time values for Morse code processing
avgDotDuration = 0.05 
cutoffLength = avgDotDuration * 2
spaceLength = cutoffLength * 3
spaceLength = .5

lastFallingEdgeTime = 0

wordComplete = 0
start = 1
keypressComplete = 0

# empty lists for morse code processing
keypressTimes = []
morseSymbols = []
decodedCharacters = []

## dictionary converting morse code to into its corresponding letter
mc_to_letters = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
    '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
    '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
    '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
    '..-': 'u', '..--': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
    '--..': 'z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9', '-.-.-': 'attention',
    '-.-': 'over', '.-.-.': 'out' }
## dictionary converting letters into their corresponding morse code
letters_to_mc = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '..--', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', 'attention': '-.-.-',
    'over': '-.-', 'out': '.-.-.' }

# function that accepts the length of a key press as the input and returns its corresponding unit (dot or dash) 
def translateToSymbol(length):
    global cutoffLength
    if length > cutoffLength: # if the time is longer than the cutoff time, it will be a dash 
        return '-'
    else:
        return '.'      

# function designed to convert a list of time durations into morse code symbols
def convertTimeToSymbol():
    global keypressTimes, morseSymbols
    if not keypressTimes: # checks if the 'keypressTimes' list is empty. if it is, exit the function
        return
    for times in keypressTimes:
        # this converts the time duration to a Morse symbol using the 'translateToSymbol' function
        # this appends the resulting Morse symbol to the 'morseSymbols' list
        morseSymbols.append(translateToSymbol(times))
    keypressTimes.clear() 

# function that changes morse code to letter and store this in decodedCharacters list
def convertSymbolsToLetter():
    global morseSymbols, decodedCharacters
    letter = ''
    if not morseSymbols: 
        return
    for v in morseSymbols:                  # iterates through each symbol in 'morseSymbols'
        letter += v             
    if letter in mc_to_letters:             # checks if the concatenated morse code string matches anything in 'mc_to_letters'
        letter = mc_to_letters[letter]
    else:
        letter = '?'                        # if its not in 'mc_to_letters' then will give '?' as unknown
    print(letter)
    decodedCharacters.append(letter)
    morseSymbols.clear()

# function starts a timer and turns on an LED on a rising edge. on the fall edge it updates the global time
def risingEdge(channel):
    global lastFallingEdgeTime, keypressTimes, start, keypressComplete, speaker
    keypressComplete = 0
    temp = time.time()

    #debounce case
    if (temp - lastFallingEdgeTime) < 0.1:
        keypressComplete = 1
        return

    # turns on the LED and speaker
    GPIO.output(LED_PIN, GPIO.HIGH) 
    speaker.start(50)

    # converts times to morse code to a letter during a 'letter' space period
    if (time.time() - lastFallingEdgeTime) >= spaceLength and not start:
        convertTimeToSymbol()
        convertSymbolsToLetter()
    while GPIO.input(TELEGRAPH_PIN):
        i = 0

    lastFallingEdgeTime = time.time()

    # turns off the LED and speaker
    GPIO.output(LED_PIN, GPIO.LOW)
    speaker.stop()

    # debouncing for very short presses
    if (lastFallingEdgeTime - temp) < 0.01:
        keypressComplete = 1
        return
    keypressTimes.append(lastFallingEdgeTime - temp)
    keypressComplete = 1

# event detecting case for a rising edge 
GPIO.add_event_detect(TELEGRAPH_PIN, GPIO.RISING, callback=risingEdge, bouncetime=100)

# loop that initally runs to calibrate the dots and dashes
print('Enter Attention "-.-.-":')
while True:
    # calculates the average dot press after recording the 5 key presses from 'attention' 
    if len(keypressTimes) == 5:
        avgDotDuration = (keypressTimes[1] + keypressTimes[3]) / 2 # the average duration of a dot from the recorded times
        cutoffLength = avgDotDuration * 2   # this sets the cutoff length for differentiating between dots and dashes
        sevenDotDuration = cutoffLength * 7 # the duration representing seven dots, used for the morse code spacing
        # clears the lists for the next set of inputs
        keypressTimes.clear()
        decodedCharacters.clear()
        print('\n*')
        break
print('cutoffLength: ', cutoffLength, ' s')

fileName = "try.txt" # output file that stores the decoded & morse code characters 

start = 0
#  main loop that calls the functions to convert and writes in the file 
with open(fileName, 'a') as file: # opens the file and appends to it 
    file.write('-.-.- | attention \n') # writes attention in the beginning of file 
    file.flush()  # clears the internal buffer of the file
    morseCodeWords= "" # empty string that stores the morse code
    decodedCharsWords= "" # empty string that stores the letters that corresponds to the morse code 

    ## main loop starts here ## 
    while True:
        if (time.time() - lastFallingEdgeTime) > spaceLength and keypressComplete:
             if keypressTimes:
                # converts recorded keypress times to Morse symbols and then to a letter if any are recorded
                convertTimeToSymbol()
                morseCodeString = ''.join(morseSymbols)
                convertSymbolsToLetter()
               # this records the decoded characters 
                if decodedCharacters:
                    decodedChar = decodedCharacters.pop(0)
                    morseCodeWords += morseCodeString + " "
                    decodedCharsWords += decodedChar
                    # special case: if the user sends the "out" symbol, we close the file and exit
                    if morseCodeString == '.-.-.': 
                        file.write(".-.-. -.- | over")
                        file.flush()
                        file.close()
                        print("File is closed!")
                        break

             # if we waited long enough for a word to end - 7  dots, then it will write the Morse code and decoded words to the file
             if (time.time() - lastFallingEdgeTime) >= sevenDotDuration:
                if morseCodeWords and decodedCharsWords:
                    completedLine = morseCodeWords.strip() + " | " + decodedCharsWords + '\n'
                    file.write(completedLine)
                    file.flush()
                    # resets words to decode the next word
                    morseCodeWords = ""
                    decodedCharsWords = ""  
