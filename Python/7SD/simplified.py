import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define pin numbers
ROW_PINS = [18, 23, 24, 25]
COL_PINS = [12, 16, 20, 21]
CLK_PINS = [10, 9, 11, 8]
SEGMENT_PINS = [2, 3, 27, 22, 5, 6, 13, 26]

# Initialize GPIO pins
for pin in CLK_PINS:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
for pin in ROW_PINS:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
for pin in COL_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for pin in SEGMENT_PINS:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# Function to toggle clock
def toggleClock(clk_pin):
    current_state = GPIO.input(clk_pin)
    new_state = GPIO.LOW if current_state == GPIO.HIGH else GPIO.HIGH
    GPIO.output(clk_pin, new_state)

# Function to reset all GPIO pins
def reset():
    for pin in SEGMENT_PINS:
        GPIO.output(pin, GPIO.LOW)

# Function to interpret button presses
def readKeypad(rowNum, char):
    def hashtag():
        print("#")
        if all(GPIO.input(pin) == GPIO.LOW for pin in SEGMENT_PINS):
            print("dog")
            if state == 1:
                one()
            if state == 2:
                two()
            if state == 3:
                three()
            if state == 4:
                four()
            if state == 5:
                five()
            if state == 6:
                six()
            if state == 7:
                seven()
            if state == 8:
                eight()
            if state == 9:
                nine()
            if state == 10:
                star()
        else:
            reset()

    # Define the mappings for each character to its GPIO configuration
CHARACTER_MAP = {
    '0': [27, 22, 13, 2, 5, 6, 26],
    '1': [22, 13],
    '2': [27, 22, 3, 5, 6],
    '3': [27, 22, 3, 13, 6],
    '4': [2, 3, 22, 13],
    '5': [27, 2, 3, 13, 6],
    '6': [27, 2, 5, 6, 13, 3],
    '7': [27, 22, 13],
    '8': [27, 22, 13, 2, 5, 6, 3],
    '9': [27, 2, 22, 3, 13],
    '*': [26],
    'A': [27, 2, 22, 5, 13, 3],
    'B': [2, 3, 5, 13, 6],
    'C': [27, 2, 5, 6],
    'D': [22, 3, 5, 13, 6]
}

# Function to set GPIO outputs based on the character input
def setGPIO(character):
    global state
    reset()
    if character in CHARACTER_MAP:
        GPIO.output(CHARACTER_MAP[character], GPIO.HIGH)
        state = list(CHARACTER_MAP.keys()).index(character)

    # Other functions omitted for brevity...

    GPIO.output(rowNum, GPIO.HIGH)

    if GPIO.input(COL_1) == 1:
        if rowNum == 18:
            print("1")
            reset()
            one()
        # Other conditions omitted for brevity...
    elif GPIO.input(COL_2) == 1:
        # Implementation for column 2...
    elif GPIO.input(COL_3) == 1:
        # Implementation for column 3...
    elif GPIO.input(COL_4) == 1:
        # Implementation for column 4...

    GPIO.output(rowNum, GPIO.LOW)

# Function to display a number on 7-segment display
def display_number(number):
    numbers = {
        0: [1, 1, 1, 1, 1, 1, 0, 0],
        1: [0, 1, 1, 0, 0, 0, 0, 0],
        # Other number segments omitted for brevity...
    }

    for i, segment_pin in enumerate(SEGMENT_PINS):
        GPIO.output(segment_pin, numbers[number][i])

try:
    while True:
        readKeypad(ROW_1, ['1', '4', '7', '*'])
        readKeypad(ROW_2, ['2', '5', '8', '0'])
        readKeypad(ROW_3, ['3', '6', '9', '#'])
        readKeypad(ROW_4, ['A', 'B', 'C', 'D'])
        time.sleep(.2)
        
        for clk_pin in CLK_PINS:
            toggleClock(clk_pin)

except KeyboardInterrupt:
    print("\nKeypad Application Interrupted") 
    GPIO.cleanup()
