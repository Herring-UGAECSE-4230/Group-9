import RPi.GPIO as GPIO
from time import sleep
import time


# setting gpio pins to telegraph, led, speaker 
KEY_PIN = 21
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

# Lists for Morse code processing
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
    '-.-': 'over', '.-.-.': 'out'
}
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
    'over': '-.-', 'out': '.-.-.'
}

# function that accepts the length of a key press as the input and returns its corresponding unit (dot or dash) 
def translateToSymbol(length):
    global cutoffLength
    if length > cutoffLength:
        return '-'
    else:
        return '.'

# function designed to convert a list of time durations into Morse code symbols
def convertTimeToSymbol():
    global keypressTimes, morseSymbols
    if not keypressTimes:
        return
    for times in keypressTimes:
        morseSymbols.append(translateToSymbol(times))
    keypressTimes.clear()

# function that changes morse code to letter and store this in decodedCharacters list
def convertSymbolsToLetter():
    global morseSymbols, decodedCharacters
    letter = ''
    if not morseSymbols:
        return
    for v in morseSymbols:
        letter += v
    if letter in mc_to_letters:
        letter = mc_to_letters[letter]
    else:
        letter = '?'
    print(letter)
    decodedCharacters.append(letter)
    morseSymbols.clear()

#This function is for rising edge - starts timer immediately, turns on led, once falling edge is triggered, global time variable 
#is updated
#Also, if rising edge is called during 'letter' space period, call two methods converting times to symbols and symbols to a letter
def risingEdge(channel):
    global lastFallingEdgeTime, keypressTimes, start, keypressComplete, speaker
    keypressComplete = 0
    temp = time.time()
    #debounce case
    if (temp - lastFallingEdgeTime) < 0.1:
        keypressComplete = 1
        return
    GPIO.output(LED_PIN, GPIO.LOW)
    #Turn tone on here:
    speaker.stop()
    #Morse Letter case
    if (time.time() - lastFallingEdgeTime) >= spaceLength and not start:
        convertTimeToSymbol()
        convertSymbolsToLetter()
    while GPIO.input(TELEGRAPH_PIN):
        i = 0
    lastFallingEdgeTime = time.time()
    GPIO.output(LED_PIN, GPIO.HIGH)
    #Turn tone off here:
    speaker.start(50)
    #Case for glitch press occurs on device
    if (lastFallingEdgeTime - temp) < 0.01:
        keypressComplete = 1
        return
    keypressTimes.append(lastFallingEdgeTime - temp)
    keypressComplete = 1

GPIO.add_event_detect(TELEGRAPH_PIN, GPIO.RISING, callback=risingEdge, bouncetime=100)

#This loop is the starting calibration loop that determines the time variables
print('Enter Attention')
while True:
    if len(keypressTimes) == 5:
        avgDotDuration = (keypressTimes[1] + keypressTimes[3]) / 2
        cutoffLength = avgDotDuration * 2
        keypressTimes.clear()
        decodedCharacters.clear()
        print('\n*')
        break

print('cutoffLength: ', cutoffLength, '  s')

fileName = str(time.strftime('%H:%M:%S')) + ' Test'
while GPIO.input(TELEGRAPH_PIN):
    i = 0
start = 0
#This is main loop that calls the different methods to convert times to letters and also writes to the file
with open(fileName, 'a') as file:
    file.write('*')
    print("Hereeeeeeeeeeeeeee")
    while True:
        if (time.time() - lastFallingEdgeTime) > spaceLength and keypressComplete:
            print("hmmmmmmmmmmmmmmmm")
            if keypressTimes:
                convertTimeToSymbol()
                convertSymbolsToLetter()
            if not file.closed and decodedCharacters:
                if decodedCharacters[0] != '!':
                    file.write(decodedCharacters[0])
                else:
                    file.write('!')
                    file.close()
                decodedCharacters.clear() 
