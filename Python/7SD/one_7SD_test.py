import RPi.GPIO as GPIO
import time
from time import sleep



GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)

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

# clock pins
clk1 = 10 #left most DFF
GPIO.setup(clk1, GPIO.OUT, initial=GPIO.LOW)

# Define the pin numbers for the segments of the 7-segment display
segments = [2, 3, 27, 22, 5, 6, 13, 26] #data pins from DFF

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


GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW) #A
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) #B
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) #C
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) #D
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)#E
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)#F
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)#G
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)#Dp

#function to toggle on and off clock
def clock():
    GPIO.output(clk1, GPIO.HIGH)
    sleep(0.0001)

    GPIO.output(clk1, GPIO.LOW)
    sleep(0.0001)

#     if toggle == 1:
#         for n in range(1):
#             GPIO.output(clk1, GPIO.HIGH)
#         toggle = 0
#     
#     elif toggle == 0:
#         for i in range(8):
#             GPIO.output(segments[i], GPIO.LOW)  
#         toggle = 1 

    
        

    
# #funtion to call specfic segments and make GPIO HIGH
# def readGPIO(pins):
#     GPIO.setmode(GPIO.BCM)
#     
#     GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) #B
#     GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) #C
#         
#     GPIO.output(22, GPIO.HIGH)
#     GPIO.output(13, GPIO.HIGH)

def reset():
    GPIO.output(22, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)

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


#function to interpret which button was pressed
def readKeypad(rowNum,char):
    GPIO.setmode(GPIO.BCM)
    GPIO.output(rowNum, GPIO.HIGH)

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
            toggleClock()
                
       
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
