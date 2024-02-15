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
for i in range(3):
    GPIO.setup(rows[i], GPIO.OUT, initial=GPIO.LOW)

#from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
#if needed set low by default: pull_up_down=GPIO.PUD_DOWN
for i in range(3):
    GPIO.setup(cols[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# setup for 7SD GPIO Pins
for i in range(7): 
    GPIO.setup(segments[i], GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(segments[i], GPIO.LOW)

# setup for Clock GPIO Pins 
for i in range(3): 
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
rows = [['1','4','7','*']),
        ['2','5','8','0']),
        ['3','6','9','#']),
        ['A','B','C','D'])]

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
                display_num(clock_state[i]
                seven_seg(clk_pins[i])   
                        

#function to toggle on and off clock
def clock():
    GPIO.output(clk1, GPIO.HIGH)
    sleep(0.0001)

    GPIO.output(clk1, GPIO.LOW)
    sleep(0.0001)


     

    
def reset():
    GPIO.output(22, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)


display_state = 1  # 1 for ON, 0 for OFF
hash_count = 0
#function to interpret which button was pressed
def readKeypad(rowNum,char):
   
    GPIO.setmode(GPIO.BCM)
    GPIO.output(rowNum, GPIO.HIGH)

    global display_state
    global hash_count
    
    def hashtag():
        global display_state
        global hash_count
        
        if display_state == 0:  # If display is off
            print("Display ON")
            display_state = 1
            hash_count = 0

        else:  # If display is on
            hash_count += 1
            if hash_count >= 4:  # Toggle display off after four consecutive "#" key presses
                print("Display OFF")
                display_state = 0
                hash_count = 0
                reset()

    def zero():        
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        state=0
        check=0
    
    def one():
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=1
        check=1
    
    def two():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=2
        check=2
    
    def three():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=3
        check="3"
    
    def four():
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=4
        check="4"
    
    def five():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=5
        check="5"
            
    def six():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=6
        check="6"
        
    def seven():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=7
        check="7"
        
    def eight():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=8
    check="8"
    
    def nine():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=9
        check="9"
    
    def star():
        GPIO.output(26, GPIO.HIGH)
        state=10
        check="*"
    def a():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=11
        check="a"
    def b():
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=12
        check="b"
    def c():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=13
        check="*"
    def d():
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        
        state=14
        check="*"

    if GPIO.input(COL_1)==1:
        #col_1 is 12
        if rowNum==18: 
            print("1")
            reset()
            off = 1
            state = 1
            
        if rowNum==23:
            print("4")
            reset()
            four()
            state = 4
        if rowNum==24:
            print("7")
            reset()
            seven()
            state = 7
        if rowNum==25:
            print("*")
            reset()
            star()
            state = 10
            
    if GPIO.input(COL_2)==1:
         #col_1 is 16
        if rowNum==18:
            print("2")
            reset()
            two()
            state = 2
        if rowNum==23:
            print("5")
            reset()
            five()
            state = 5
        if rowNum==24:
            print("8")
            reset()
            eight()
            state = 8
        if rowNum==25:
            print("0")
            reset()
            zero()
            state = 0
        
    if GPIO.input(COL_3)==1:
         #col_1 is 20
        if rowNum==18:
            print("3")
            reset()
            three()
            state = 3
        if rowNum==23:
            print("6")
            reset()
            six()
            state = 6
        if rowNum==24:
            print("9")
            reset()
            nine()
            state = 9
        if rowNum==25:
            print("#")
                
       
    if GPIO.input(COL_4)==1:
             #col_1 is 21
        if rowNum==18:
            print("A")
            a()
            state = 11
        if rowNum==23:
            print("B")
            b()
            state = 12
        if rowNum==24:
            print("C")
            c()
            state = 13
        if rowNum==25:
            print("D")
            d()
            state = 14

    if char == '#':
        hashtag()
       
    GPIO.output(rowNum, GPIO.LOW)
    # return curVal #check this SIMLINE

off=1
# def toggleClock():
#     global off
#      # Read the current state of the pin
# #     current_state = GPIO.input(clk1)
#     # Toggle the pin state
#     if off==1:
#         for i in range(8):
#             GPIO.output(segments[i], GPIO.LOW)
#         off= 0
#     elif off==0:
#         if state==0:
#             zero()
#         if state==1:
#             one()
#         if state==2:
#             two()
#         if state==3:
#             three()
#         if state==4:
#             four()
#         if state==5:
#             five()
#         off=1
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

curr_state = 1
try:
    while True:
        
        state=1
#         toggleClock()
#         zero()
#         one()
#         two()
#         three()
#         four()
#         five()
#         six()
#         seven()
#         eight()
#         nine()
#         a()
#         b()
#         c()
#         d()
#         star()
        clock()
        #initial state
        readKeypad(ROW_1,['1','4','7','*'])
        readKeypad(ROW_2,['2','5','8','0'])
        readKeypad(ROW_3,['3','6','9','#'])
        readKeypad(ROW_4,['A','B','C','D'])
        curr_state=0
        #other states
        time.sleep(.2)
        
    
        
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       
