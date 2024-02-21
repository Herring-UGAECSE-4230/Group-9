import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)

#global variables 
global state #state of each number being pressed; 0-14\
global pressed

#initialized variables
state = -1 
pressed = -1

#setting row pins
ROW_PINS = [18,23,24,25]

#setting column pins
COL_PINS = [12,16,20,21]

# clock pins
clk1 = 10 #left most DFF
clk2 = 9 
clk3 = 11                                                         
clk4 = 8 #right most DFF

#GPIO setup for clk pins 
GPIO.setup(clk1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(clk2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(clk3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(clk4, GPIO.OUT, initial=GPIO.LOW)


# Define the pin numbers for the segments of the 7-segment display
segments = [2, 3, 27, 22, 5, 6, 13, 26] #data pins from DFF

#from instructions: GPIO pins connected to the 'X' lines will be setup as inputs to the pad/output from the PI
GPIO.setup(ROW_PINS[0], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_PINS[1], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_PINS[2], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_PINS[3], GPIO.OUT, initial=GPIO.LOW)

#from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
#if needed set low by default: pull_up_down=GPIO.PUD_DOWN
GPIO.setup(COL_PINS[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_PINS[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_PINS[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_PINS[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#initialize all pins to low
#A is 27, B is 22, C is 13, D is 6, E is 5, F is 2, G is 3, DO is 26
for pin in segments:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# LED GPIO Setup
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

#toggle function
def toggleClock(clk_pin):
    current_state = GPIO.input(clk_pin)
    new_state = GPIO.LOW if current_state == GPIO.HIGH else GPIO.HIGH
    GPIO.output(clk_pin, new_state)


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
    global pressed
    def hashtag():
        print("#")
        while True:
            pass                                                                                                                                                                                                                                                                                                                                  
#                 
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
        sleep(.15)
        
    def one():
        global state 
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=1
        sleep(.15)

    def two():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=2
        sleep(.15)
    
    def three():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=3
        sleep(.15)
    
    def four():
        global state
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=4
        sleep(.15)
    
    def five():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=5
        sleep(.15)

    def six():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=6
        sleep(.15)
        
    def seven():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=7
        sleep(.15)
        
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
        sleep(.15)
    
    def nine():
        global state
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=9
        sleep(.15)
    
    def star():
        global state
        GPIO.output(26, GPIO.HIGH)
        state=10
        sleep(.15)
        
    def a():
        global state
        GPIO.output(4, GPIO.HIGH)
        sleep(.15)
        GPIO.output(4,GPIO.LOW)
        state=11
    
    
    def b():
        global state
        GPIO.output(4, GPIO.HIGH)
        sleep(.15)
        GPIO.output(4,GPIO.LOW)      
        state=12
       
    def c():
        global state
        GPIO.output(4, GPIO.HIGH)
        sleep(.15)
        GPIO.output(4,GPIO.LOW)
        state=13
      
    def d():
        global state
        GPIO.output(4, GPIO.HIGH)
        sleep(.15)
        GPIO.output(4,GPIO.LOW)
        state=14
     
    GPIO.setmode(GPIO.BCM)
    GPIO.output(rowNum, GPIO.HIGH)
    if GPIO.input(COL_PINS[0])==1:
        #col_1 is 12
        if rowNum==18:
            print("1")
            reset()
            one()
            pressed = 1
            
        if rowNum==23:
            print("4")
            reset()
            four()
            pressed = 1
            
        if rowNum==24:
            print("7")
            reset()
            seven()
            pressed = 1
            
        if rowNum==25:
            print("*")
            reset()
            star()
            pressed = 1
            
    if GPIO.input(COL_PINS[1])==1:
         #col_ is 16
        if rowNum==18:
            print("2")
            reset()
            two()
            pressed = 1
            
        if rowNum==23:
            print("5")
            reset()
            five()
            pressed = 1
            
        if rowNum==24:
            print("8")
            reset()
            eight()
            pressed = 1
            
        if rowNum==25:
            print("0")
            reset()
            zero()
            pressed = 1
        
    if GPIO.input(COL_PINS[2])==1:
         #col_1 is 20
        if rowNum==18:
            print("3")
            reset()
            three()
            pressed = 1
            
        if rowNum==23:
            print("6")
            reset()
            six()
            pressed = 1
            
        if rowNum==24:
            print("9")
            reset()
            nine()
            pressed = 1
            
        if rowNum==25:
            print("#")
            while(True):
                toggleClock(clk1)
                toggleClock(clk2)
                toggleClock(clk3)
                toggleClock(clk4)
                reset()
                sleep(0.2)
                if GPIO.input(COL_PINS[2])==1:
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
#                                              
        
    if GPIO.input(COL_PINS[3])==1:
         #col_1 is 21
        if rowNum==18:
            print("A")
            reset()
            a()
            state = 11
            pressed = 1
            
        if rowNum==23:
            print("B")
            reset()
            b()
            state = 12
            pressed = 1
            
        if rowNum==24:
            print("C")
            reset()
            c()
            state = 13
            pressed = 1
            
        if rowNum==25:
            print("D")
            reset()
            d()
            state = 14
            pressed = 1
       
    GPIO.output(rowNum, GPIO.LOW)

   


        


   
def SSD1():
    toggleClock(clk1)
    global pressed
    GPIO.setup(clk2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clk3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clk4, GPIO.OUT, initial=GPIO.LOW)
    while True:
        readKeypad(ROW_PINS[0],['1','4','7','*'])
        readKeypad(ROW_PINS[1],['2','5','8','0'])
        readKeypad(ROW_PINS[2],['3','6','9','#'])
        readKeypad(ROW_PINS[3],['A','B','C','D'])
        if pressed == 1:
            sleep(.15)
            pressed=-1
            print("#1 player")
            break
    print("SSD1 value inputted")
    #print("go to SSD2")
    #SSD2()
    #print("came back from SSD2")

def SSD2():
    toggleClock(clk2)
    global pressed
    GPIO.setup(clk1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clk3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clk4, GPIO.OUT, initial=GPIO.LOW)
    while True:
        readKeypad(ROW_PINS[0],['1','4','7','*'])
        readKeypad(ROW_PINS[1],['2','5','8','0'])
        readKeypad(ROW_PINS[2],['3','6','9','#'])
        readKeypad(ROW_PINS[3],['A','B','C','D'])
        if pressed == 1:
            sleep(.15)
            pressed=-1
            print("2 cool for school")
            break
    print("SSD2 value inputted")
    #print("go to SSD3")
    #SSD3()
    #print("came back from SSD3")
        
def SSD3():
    toggleClock(clk3)
    global pressed
    GPIO.setup(clk1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clk2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clk4, GPIO.OUT, initial=GPIO.LOW)
    while True:
        readKeypad(ROW_PINS[0],['1','4','7','*'])
        readKeypad(ROW_PINS[1],['2','5','8','0'])
        readKeypad(ROW_PINS[2],['3','6','9','#'])
        readKeypad(ROW_PINS[3],['A','B','C','D'])
        if pressed == 1:
            sleep(.15)
            pressed=-1
            print("3 is whatever")
            break
    print("SSD3 value inputted")
    #print("go to SSD4")
    #SSD4()
    #print("came back from SSD4")


def SSD4():
    toggleClock(clk4)
    global pressed
    GPIO.setup(clk1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clk2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(clk3, GPIO.OUT, initial=GPIO.LOW)
    while True:
        readKeypad(ROW_PINS[0],['1','4','7','*'])
        readKeypad(ROW_PINS[1],['2','5','8','0'])
        readKeypad(ROW_PINS[2],['3','6','9','#'])
        readKeypad(ROW_PINS[3],['A','B','C','D'])
        if pressed == 1:
            sleep(.15)
            print("4 is cool")
            break
    print("done with setting clock")
    print("                       ")


print("Press buttons on keypad. Ctrl+C to exit.")

try:
    while True:
        #NOTE: in first iteration, 1st ssd does NOT light up...it only light up at the 2nd iteration and along with the 2nd ssd
        SSD1()
        print("SSD1")
        SSD2()
        print("SSD2")
        SSD3()
        print("SSD3")
        SSD4()
        print("SSD4")
        
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       

