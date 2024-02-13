import RPi.GPIO as GPIO
import time
#setting row pins
ROW_1 = 18
ROW_2 = 23
ROW_3 = 24
ROW_4 = 25
#setting column pins
COL_1 = 12
COL_2 = 16
COL_3 = 20
COL_4 = 21
# Define the pin numbers for the segments of the 7-segment display
segments = [2, 3, 27, 22, 5, 6, 13, 26] #data pins from DFF

GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)
#from instructions: GPIO pins connected to the 'X' lines will be setup as inputs to the pad/output from the PI
GPIO.setup(ROW_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_4, GPIO.OUT, initial=GPIO.LOW)
#from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
#if needed set low by default: pull_up_down=GPIO.PUD_DOWN
GPIO.setup(COL_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

keypad_value= 2
def readKeypad(rowNum, char):
    GPIO.output(rowNum, GPIO.HIGH)
    global keypad_value
    if GPIO.input(COL_1)==1:
#         print(char[0])
#         return char[0]
        keypad_value= char[0]
        return keypad_value
    if GPIO.input(COL_2)==1:
#         print(char[1])
#         return char[1]
        keypad_value= char[1]
        return keypad_value
    if GPIO.input(COL_3)==1:
#         print(char[2])
#         return char[2]
        keypad_value= char[2]
        return keypad_value
    if GPIO.input(COL_4)==1:
#         print(char[3])
#         return char[3]
        keypad_value= char[3]
        return keypad_value
    GPIO.output(rowNum, GPIO.LOW)
    # return curVal #check this SIMLINE
#physical keyboard layout
#loop checking each row
print("Press buttons on keypad. Ctrl+C to exit.")


# Function to light up segments for a given number
def display_number(number):
    # Define the segments required to display each number
    numbers = {
        0: [1, 1, 1, 1, 1, 1, 0, 0],
        1: [0, 1, 1, 0, 0, 0, 0, 0],
        2: [1, 1, 0, 1, 1, 0, 1, 0],
        3: [1, 1, 1, 1, 0, 0, 1, 0],
        4: [0, 1, 1, 0, 0, 1, 1, 0],
        5: [1, 0, 1, 1, 0, 1, 1, 0],
        6: [1, 0, 1, 1, 1, 1, 1, 0],
        7: [1, 1, 1, 0, 0, 0, 0, 0],
        8: [1, 1, 1, 1, 1, 1, 1, 0],
        9: [1, 1, 1, 1, 0, 1, 1, 0],
        10: [0, 0, 0, 0, 0, 0, 0, 1] #dp
    }
    i=number
    print(numbers[i])
#     
#     # Turn on/off the segments based on the number
#     for i, segment_pin in enumerate(segments):
#         GPIO.output(segment_pin, numbers[number][i])


try:
    while True:
        readKeypad(ROW_1,['1','2','3','A'])
        readKeypad(ROW_2,['4','5','6','B'])
        readKeypad(ROW_3,['7','8','9','C'])
        readKeypad(ROW_4,['*','0','#','D'])
        time.sleep(0.2)
        
        print(display_number(keypad_value))
#         print(keypad_value)
        
    while True:
        #getting user input from keypad
        GPIO.output(rowNum, GPIO.HIGH)
        global keypad_value
        if GPIO.input(COL_1)==1:
            keypad_value= char[0]
        if GPIO.input(COL_2)==1:
            keypad_value= char[1]
        if GPIO.input(COL_3)==1:
            keypad_value= char[2]
        if GPIO.input(COL_4)==1:
            keypad_value= char[3]
        return keypad_value
        GPIO.output(rowNum, GPIO.LOW)
        
        #comparing user input to segment keypad_mapping
        if rowNum and 
        display_number(keypad_value)
        
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       

