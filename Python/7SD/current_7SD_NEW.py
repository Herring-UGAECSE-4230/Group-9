import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)

#global variables 
global state #state of each number being pressed; 0-14\
global pressed
global counter

#initialized variables
state = -1 
pressed = -1
counter = 0

#setting row pins
ROW_PINS = [18,23,24,25]

#setting column pins
COL_PINS = [12,16,20,21]

# clock pins
CLK_PINS = [8, 10, 9, 11]

# Define the pin numbers for the segments of the 7-segment display
segments = [2, 3, 27, 22, 5, 6, 13, 26] #data pins from DFF

#GPIO setup for clk pins 
GPIO.setup(CLK_PINS[0], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(CLK_PINS[1], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(CLK_PINS[2], GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(CLK_PINS[3], GPIO.OUT, initial=GPIO.LOW)




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
for pin in segments:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

# GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW) #A
# GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) #B
# GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) #C
# GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) #D
# GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)#E
# GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)#F
# GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)#G
# GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)#Dp

# LED GPIO Setup
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)


#function to toggle on and off clock
def toggleClock(clkpin):
    GPIO.output(clkpin, GPIO.HIGH)
    sleep(0.0001)
    print("clk on")

    GPIO.output(clkpin, GPIO.LOW)
    sleep(0.0001)
    print("clk off")

# def toggleClock(clk_pin):
#     # Read the current state of the pin
#     current_state = GPIO.input(clk_pin)
#     # Toggle the pin state
#     new_state = GPIO.LOW if current_state == GPIO.HIGH else GPIO.HIGH
#     GPIO.output(clk_pin, new_state)



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
    print("reset")



#function to interpret which button was pressed
def readKeypad(rowNum,char):
    global state, pressed, counter
    
    def hashtag():
        print("#")
        # checks if all GPIO segments are OFF
        while True:
            if GPIO.output(27, GPIO.LOW) and GPIO.output(22, GPIO.LOW) and GPIO.output(13, GPIO.LOW) and GPIO.output(2, GPIO.LOW) and GPIO.output(5, GPIO.LOW) and GPIO.output(6, GPIO.LOW) and GPIO.output(26, GPIO.LOW) and GPIO.output(3, GPIO.LOW):
                print("dog")
                if state==0:
                    zero()
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
        GPIO.output(4, GPIO.HIGH)
        sleep(.5)
        GPIO.output(4,GPIO.LOW)
#         GPIO.output(27, GPIO.HIGH)
#         GPIO.output(2, GPIO.HIGH)
#         GPIO.output(22, GPIO.HIGH)
#         GPIO.output(5, GPIO.HIGH)
#         GPIO.output(13, GPIO.HIGH)
#         GPIO.output(3, GPIO.HIGH)
        state=11
        
    
    def b():
        global state
        GPIO.output(4, GPIO.HIGH)
        sleep(.5)
        GPIO.output(4,GPIO.LOW)
#         GPIO.output(2, GPIO.HIGH)
#         GPIO.output(3, GPIO.HIGH)
#         GPIO.output(5, GPIO.HIGH)
#         GPIO.output(13, GPIO.HIGH)
#         GPIO.output(6, GPIO.HIGH)
        state=12
       
    def c():
        global state
        GPIO.output(4, GPIO.HIGH)
        sleep(.5)
        GPIO.output(4,GPIO.LOW)
#         GPIO.output(27, GPIO.HIGH)
#         GPIO.output(2, GPIO.HIGH)
#         GPIO.output(5, GPIO.HIGH)
#         GPIO.output(6, GPIO.HIGH)
        state=13
      
    def d():
        global state
        GPIO.output(4, GPIO.HIGH)
        sleep(.5)
        GPIO.output(4,GPIO.LOW)
#         GPIO.output(22, GPIO.HIGH)
#         GPIO.output(3, GPIO.HIGH)
#         GPIO.output(5, GPIO.HIGH)
#         GPIO.output(13, GPIO.HIGH)
#         GPIO.output(6, GPIO.HIGH)
        state=14
     
    GPIO.setmode(GPIO.BCM)
    GPIO.output(rowNum, GPIO.HIGH)
##################################################
    if GPIO.input(COL_PINS[0])==1:
        #col_1 is 12
        if rowNum==18: 
            print("1")
            pressed = 1
            counter += 1
            reset()
            one()
        if rowNum==23:
            print("4")
            pressed = 1
            counter += 1
            reset()
            four()
        if rowNum==24:
            print("7")
            pressed = 1
            counter += 1
            reset()
            seven()
        if rowNum==25:
            print("*")
            pressed = 1
            counter += 1
            reset()
            star()
            
    if GPIO.input(COL_PINS[1])==1:
         #col_ is 16
        if rowNum==18:
            print("2")
            pressed = 1
            counter += 1
            reset()
            two()
        if rowNum==23:
            print("5")
            pressed = 1
            counter +=1 
            reset()
            five()
        if rowNum==24:
            print("8")
            pressed = 1
            counter +=1 
            reset()
            eight()
        if rowNum==25:
            print("0")
            pressed = 1
            counter +=1 
            reset()
            zero()
        
    if GPIO.input(COL_PINS[2])==1:
         #col_1 is 20
        if rowNum==18:
            print("3")
            pressed = 1
            counter +=1
            reset()
            three()
        if rowNum==23:
            print("6")
            pressed = 1
            counter +=1
            reset()
            six()
        if rowNum==24:
            print("9")
            pressed = 1
            counter +=1
            reset()
            nine()
        if rowNum==25:
            print("#")
            while(True):
                toggleClock(CLK_PINS[0])
                toggleClock(CLK_PINS[1])
                toggleClock(CLK_PINS[2])
                toggleClock(CLK_PINS[3])
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
                                    
            
        
    if GPIO.input(COL_PINS[3])==1:
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



#physical keyboard layout
#loop checking each row
print("Press buttons on keypad. Ctrl+C to exit.")


#     
#     # Turn on/off the segments based on the number
#     for i, segment_pin in enumerate(segments):
#         GPIO.output(segment_pin, numbers[number][i])

def clkReset():
    for clk_pin in CLK_PINS:
        GPIO.output(clk_pin, GPIO.LOW)
        #print(f"this clock pin is low:{clk_pin}")
        
def clkON():
    for clk_pin in CLK_PINS:
        GPIO.output(clk_pin, GPIO.HIGH)

def displaySSD(clk_pin):
    global pressed
    global counter
    
    GPIO.output(clk_pin, GPIO.HIGH)

    readKeypad(ROW_PINS[0],['1','4','7','*'])
    readKeypad(ROW_PINS[1],['2','5','8','0'])
    readKeypad(ROW_PINS[2],['3','6','9','#'])
    readKeypad(ROW_PINS[3],['A','B','C','D'])
    print(clk_pin)

    
    print("pressed success")


try:
    clkON()
    reset()
    clkReset()
    
    print("1st reset")
    while True:
        
        while counter != 4:
            if counter == 0:
                pressed = -1
                displaySSD(CLK_PINS[0])
                GPIO.output(CLK_PINS[0], GPIO.LOW)
       
                print(f"this is the counter {counter}")
                sleep(0.20)
               
            if counter == 1:
                pressed = -1
                displaySSD(CLK_PINS[1])
                GPIO.output(CLK_PINS[1], GPIO.LOW)

             
                print(f"this is the counter {counter}")
                sleep(0.25)
                
            if counter == 2:
                pressed = -1
                displaySSD(CLK_PINS[2])
                GPIO.output(CLK_PINS[2], GPIO.LOW)

        
                print(f"this is the counter {counter}")
                sleep(0.25)
                
            if counter == 3:
                pressed = -1
                displaySSD(CLK_PINS[3])
                GPIO.output(CLK_PINS[3], GPIO.LOW)

                print(f"this is the counter {counter}")
                sleep(0.25)
                
        while counter == 4:
            counter-=4
            sleep(0.25)
   
        
#         readKeypad(ROW_PINS[0],['1','4','7','*'])
#         readKeypad(ROW_PINS[1],['2','5','8','0'])
#         readKeypad(ROW_PINS[2],['3','6','9','#'])
#         readKeypad(ROW_PINS[3],['A','B','C','D'])
#         time.sleep(.2)
#         
#         toggleClock(clk1)
#         toggleClock(clk2)
#         toggleClock(clk3)
#         toggleClock(clk4)
        
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       
