import RPi.GPIO as GPIO
import time
from time import sleep

#initial setup 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


 #setting row pins
rows = [18, 23, 24, 25] # X1 - X4

 #setting column pins
cols = [12, 16, 20, 21] # Y1 - Y4

# setting clock pins
clk_pins = [10, 9, 11, 8] # left to right DFF

# Define the pin numbers for the segments of the 7-segment display
segments = [2, 3, 27, 22, 5, 6, 13, 26] #data pins from DFF

#from instructions: GPIO pins connected to the 'X' lines will be setup as inputs to the pad/output from the PI
for i in range(len(rows)):
    GPIO.setup(rows[i], GPIO.OUT, initial=GPIO.LOW)

#from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
#if needed set low by default: pull_up_down=GPIO.PUD_DOWN
for i in range(len(cols)):
    GPIO.setup(cols[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# setup for 7SD GPIO Pins
for i in range(len(segments)): 
    GPIO.setup(segments[i], GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(segments[i], GPIO.LOW)

# setup for Clock GPIO Pins 
for i in range(len(clk_pins)): 
    GPIO.setup(clk_pins[i], GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(clk_pins[i], GPIO.HIGH)

#global variables 
global toggle
global state
global prev_state
global zero

#initialize variables 
toggle = 0 
state = "-1"
prev_state = state
zero = 0 
clock_state = [-1, -1, -1, -1] 
# useDot = False         #using the Dot for AM/PM

# keypad layout 
row_layout = [['1','4','7','*'],
        ['2','5','8','0'],
        ['3','6','9','#'],
        ['A','B','C','D']]

char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "*"]

# Define the segments required to display each number
number_1 = [
    [1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1] #dp
]
number_2 = [
    [1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1] #dp
]

# function will display number on 7SD 
def display_num(number):
    for i in range(8):
        GPIO.output(segments[i], number_2[number][i]) 
            
# function to go between DFF clock pins 
def seven_seg(pin):
    for i in clk_pins:
        if i != pin:
            GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    GPIO.output(pin, GPIO.LOW)

def start():
    for i in range(4):
        display_num(0)
        seven_seg(clk_pins[i])

def toggle(): 
    global toggle, zero
    if toggle == 1:
        for i in range(len(clk_pins)):
            if clock_state[i] != -1: 
                display_num(clock_state[i])
                seven_seg(clk_pins[i])   
            else:
                pass
        toggle = 0 
    elif toggle == 0:
        for i in range(len(clk_pins)):
            for i in range(8):
                GPIO.output(segments[i], GPIO.LOW)
            seven_seg(clk_pins[i])
        toggle = 1 
                        

# #function to toggle on and off clock
# def clock():
#     GPIO.output(clk1, GPIO.HIGH)
#     sleep(0.0001)

#     GPIO.output(clk1, GPIO.LOW)
#     sleep(0.0001)



    
def reset():
    GPIO.output(22, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)


# display_state = 1  # 1 for ON, 0 for OFF
# hash_count = 0
# #function to interpret which button was pressed
def readKeypad(rowNum,char):
    GPIO.output(rowNum, GPIO.HIGH)
    if GPIO.input(cols[0])==1:
        state = char[0]

    if GPIO.input(cols[1])==1:
        state = char[1]

    if GPIO.input(cols[2])==1:
        state = char[2]

    if GPIO.input(cols[3])==1:
        state = char[3]

    GPIO.output(rowNum, GPIO.LOW)

   

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


curr_state = 1
try:
    while True:
        start()
        # clock()

        readKeypad(rows[0], row_layout[0])
        readKeypad(rows[1], row_layout[1])
        readKeypad(rows[2], row_layout[2])
        readKeypad(rows[3], row_layout[3])

        if str(state) == "#":
            toggle()


        time.sleep(.2)
        
    
        
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       
