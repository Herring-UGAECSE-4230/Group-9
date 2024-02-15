import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)

#global variables 
global state #state of each number being pressed; 0-14\

#initialized variables
state = -1 


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
# def toggleClock():
#     GPIO.output(clk1, GPIO.HIGH)
#     sleep(0.0001)

#     GPIO.output(clk1, GPIO.LOW)
#     sleep(0.0001)

def toggleClock():
    # Read the current state of the pin
    current_state = GPIO.input(clk1)
    # Toggle the pin state
    new_state = GPIO.LOW if current_state == GPIO.HIGH else GPIO.HIGH
    GPIO.output(clk1, new_state)

#     
# #funtion to call specfic segments and make GPIO HIGH
# def readGPIO(pins):
#     GPIO.setmode(GPIO.BCM)
#     
#     GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) #B
#     GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) #C
#         
#     GPIO.output(22, GPIO.HIGH)
#     GPIO.output(13, GPIO.HIGH)

# function that turns all GPIO off 
def reset():
    GPIO.output(22, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)



#function to interpret which button was pressed
def readKeypad(rowNum,char):
    global state
    def hashtag():
        print("#")
        # checks if all GPIO segments are OFF 
        if GPIO.output(27, GPIO.LOW) and GPIO.output(22, GPIO.LOW) and GPIO.output(13, GPIO.LOW) and GPIO.output(2, GPIO.LOW) and GPIO.output(5, GPIO.LOW) and GPIO.output(6, GPIO.LOW) and GPIO.output(26, GPIO.LOW) and GPIO.output(3, GPIO.LOW):
            print("dog")
            if state==1: # if state == (0-14) then it will call each numbers function to turn the GPIO segments ON 
                one() 
            if state==2:
                two()
            if state==3:
                three()
            if state==4:
                four()
            if state==5:
                five()
            if state==6:
                six()
            if state==7:
                seven()
            if state==8:
                eight()
            if state==9:
                nine()
            if state==10:
                star()
#             if hashtag==False: #if hashtage equals False, then it will be True 
#                 hashtag=True
#             else:
#                 hashtag=False
        else:
            reset()
            
    def zero():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        state=0
        
    def one():
        global state 
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=1
    
    def two():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=2
    
    def three():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=3
    
    def four():
        global state
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=4
    
    def five():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=5
        
    def six():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=6
        
    def seven():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=7
        
    def eight():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=8
    
    def nine():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=9
    
    def star():
        global state
        GPIO.output(26, GPIO.HIGH)
        state=10
        
    def a():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=11
        check="a"
    
    def b():
        global state
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=12
        check="b"
    def c():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=13
        check="*"
    def d():
        global state
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        
        state=14
        check="*"

    display=-1
    GPIO.setmode(GPIO.BCM)
    GPIO.output(rowNum, GPIO.HIGH)
##################################################
    if GPIO.input(COL_1)==1:
        #col_1 is 12
        if rowNum==18: 
            print("1")
            reset()
            one()
        if rowNum==23:
            print("4")
            reset()
            four()
        if rowNum==24:
            print("7")
            reset()
            seven()
        if rowNum==25:
            print("*")
            reset()
            star()
            
    if GPIO.input(COL_2)==1:
         #col_1 is 16
        if rowNum==18:
            print("2")
            reset()
            two()
        if rowNum==23:
            print("5")
            reset()
            five()
        if rowNum==24:
            print("8")
            reset()
            eight()
        if rowNum==25:
            print("0")
            reset()
            zero()
        
    if GPIO.input(COL_3)==1:
         #col_1 is 20
        if rowNum==18:
            print("3")
            reset()
            three()
        if rowNum==23:
            print("6")
            reset()
            six()
        if rowNum==24:
            print("9")
            reset()
            nine()
        if rowNum==25:
            print("#")
            while(True):
                toggleClock()
                reset()
                sleep(0.2)
                if GPIO.input(COL_3)==1:
                    if rowNum==25:
                        print(state)
                        if state==1:
                            one()
                        if state==2:
                            two()
                        if state==3:
                            three()
                        if state==4:
                            four()
                        if state==5:
                            five()
                        if state==6:
                            six()
                        if state==7:
                            seven()
                        if state==8:
                            eight()
                        if state==9:
                            nine()
                        if state==10:
                            star()
                        if state==11:
                            a()
                        if state==12:
                            b()
                        if state==13:
                            c()
                        if state==14:
                            d()
                        break
                                    
            
        
    if GPIO.input(COL_4)==1:
         #col_1 is 21
        if rowNum==18:
            print("A")
            reset()
            a()
            state = 11
        if rowNum==23:
            print("B")
            reset()
            b()
            state = 12
        if rowNum==24:
            print("C")
            reset()
            c()
            state = 13
        if rowNum==25:
            print("D")
            reset()
            d()
            state = 14
       
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
        readKeypad(ROW_1,['1','4','7','*'])
        readKeypad(ROW_2,['2','5','8','0'])
        readKeypad(ROW_3,['3','6','9','#'])
        readKeypad(ROW_4,['A','B','C','D'])
        time.sleep(.2)
        
        toggleClock()
        
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       
