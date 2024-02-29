import RPi.GPIO as GPIO
import time
from time import sleep
import datetime
import pytz

GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)

#global variables 
global state, pressed, counter, new, invalid, waiting_for_valid_input, LED #state of each number being pressed; 0-14\
global eastern, current_time, hour, minute_string, minute_digits_list

#initialized variables
state = -1 
pressed = -1
counter = 0
invalid = 0
waiting_for_valid_input = 0

#initializes var associated with time
eastern=pytz.timezone("US/Eastern") #sets eastern time zone
current_time= datetime.datetime.now(eastern).time() #gets current time
hour= current_time.hour #gets current hour
minute_string= str(current_time.minute)#converts current minutes to string
minute_digits_list = [int(digit) for digit in minute_string] #puts two digits of current minutes into list

#setting row pins
ROW_PINS = [18,23,24,25]

#setting column pins
COL_PINS = [12,16,20,21]

# clock pins
CLK_PINS = [10, 9, 11, 8]

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

# LED GPIO Setup
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)


#function to toggle on and off clock
def toggleClock(clkpin):
    GPIO.output(clkpin, GPIO.HIGH)
    sleep(0.0001)
    #print("clk on")

    GPIO.output(clkpin, GPIO.LOW)
    sleep(0.0001)
    #print("clk off")

# function that turns all GPIO off 
def reset():
    GPIO.output([22,13,2,5,6,26,27,3], GPIO.LOW)
    print("og reset")

#function to interpret which button was pressed
def readKeypad(rowNum,char):
    global state, pressed, counter, invalid
    
    def hashtag():
        print("#")
        # checks if all GPIO segments are OFF
        while True:
            if GPIO.output([27,22,13,2,5,6,26,3], GPIO.LOW):
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
        GPIO.output([27,22,13,2,5,6,26], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=0
        
    def one():
        global state 
        GPIO.output([22,13], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=1

    def two():
        global state
        GPIO.output([27,22,3,5,6], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=2
    
    def three():
        global state
        GPIO.output([27,22,3,13,6], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=3
    
    def four():
        global state
        GPIO.output([2,3,22,13], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=4
    
    def five():
        global state
        GPIO.output([27,2,3,13,6], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=5
        
    def six():
        global state
        GPIO.output([27,2,5,6,13,3], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=6
        
    def seven():
        global state
        GPIO.output([27,22,13], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=7
        
    def eight():
        global state
        GPIO.output([27,22,13,2], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=8
    
    def nine():
        global state
        GPIO.output([27,2,22,3,13], GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        state=9
    
    def star():
        global state
        GPIO.output(26, GPIO.HIGH)
        state=10
        
    def a():
        global state, invalid
        GPIO.output(4, GPIO.HIGH)
        state=11
        invalid = 1
    
    def b():
        global state, invalid
        GPIO.output(4, GPIO.HIGH)
        state=12
        invalid = 1
       
    def c():
        global state, invalid
        GPIO.output(4, GPIO.HIGH)
        state=13
        invalid = 1
      
    def d():
        global state, invalid
        GPIO.output(4, GPIO.HIGH)
        state=14
        invalid = 1
     
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
            LED=1
        if rowNum==23:
            print("4")
            pressed = 1
            counter += 1
            reset()
            four()
            LED=1
        if rowNum==24:
            print("7")
            pressed = 1
            counter += 1
            reset()
            seven()
            LED=1
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
            LED=1
            
        if rowNum==23:
            print("5")
            pressed = 1
            counter +=1
            reset()
            five()
            LED=1
            
        if rowNum==24:
            print("8")
            pressed = 1
            counter +=1
            reset()
            eight()
            LED=1
            
        if rowNum==25:
            print("0")
            pressed = 1
            counter +=1
            reset()
            zero()
            LED=1
        
    if GPIO.input(COL_PINS[2])==1:
         #col_1 is 20
        if rowNum==18:
            print("3")
            pressed = 1
            counter +=1
            reset()
            three()
            LED=1
            
        if rowNum==23:
            print("6")
            pressed = 1
            counter +=1
            reset()
            six()
            LED=1
            print(f"...................{LED}")
            
        if rowNum==24:
            print("9")
            pressed = 1
            counter +=1
            reset()
            nine()
            LED=1
            
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
                            invalid = 1
                        if state==12:
                            b()
                            invalid = 1
                        if state==13:
                            c()
                            invalid = 1
                        if state==14:
                            d()
                            invalid = 1
                        break
                                    
            
        
    if GPIO.input(COL_PINS[3])==1:
         #col_1 is 21
        if rowNum==18:
            print("A")
            reset()
            a()
            state = 11
            invalid = 1
            LED=1
            
        if rowNum==23:
            print("B")
            reset()
            b()
            state = 12
            invalid = 1
            LED=1
            
        if rowNum==24:
            print("C")
            reset()
            c()
            state = 13
            invalid = 1
            LED=1
            
        if rowNum==25:
            print("D")
            reset()
            d()
            state = 14
            invalid = 1
            LED=1
       
    GPIO.output(rowNum, GPIO.LOW)

#wukk set all clock pins to low
def clkReset():
    for clk_pin in CLK_PINS:
        GPIO.output(clk_pin, GPIO.LOW)
        #print(f"this clock pin is low:{clk_pin}")

#will set all clock pins to high
def clkON():
    for clk_pin in CLK_PINS:
        GPIO.output(clk_pin, GPIO.HIGH)
        print(clk_pin)

#function to display a value on a SSD
def displaySSD(clk_pin):
    global pressed, counter, waiting, invalid, waiting_for_valid_input

    GPIO.output(clk_pin, GPIO.HIGH)
    
    if invalid == 0 or waiting_for_valid_input == 1234567: # false
    
        readKeypad(ROW_PINS[0],['1','4','7','*'])
        readKeypad(ROW_PINS[1],['2','5','8','0'])
        readKeypad(ROW_PINS[2],['3','6','9','#'])
        readKeypad(ROW_PINS[3],['A','B','C','D'])
        
        print(clk_pin)
        
    elif invalid == 1: # true, if ABCD is pressed
        GPIO.output(4, GPIO.HIGH)
        waiting_for_valid_input = 1234567
        

def segON():
    GPIO.output([22,13,2,5,6,26,27,3], GPIO.HIGH)

def blink(clk_pin):
    global pressed
    toggleClock(clk_pin)
    segON()
    sleep(.15)
    GPIO.output(clk_pin, GPIO.HIGH)
    GPIO.output(clk_pin, GPIO.LOW)
    reset()
    sleep(.15)
    GPIO.output(clk_pin, GPIO.HIGH)
    
def start():
    global state
    #clkON()
    GPIO.output([27,22,13,2,5,6,26], GPIO.HIGH)
    state=0
    

    
def minute_fun():
    global eastern, current_time, hour, minute_string, minute_digits_list
    if len(minute_digits_list)==1:
        minute_digits_list.insert(0,0) #add a 0 at index 0 to the list
        print(minute_digits_list)
    else:
        print(minute_digits_list)

def datetime_A():
    global eastern, current_time, hour, minute_string, minute_digits_list
    
    
    if hour==0: #it is 12 am
        hour+=12
        hour_string= str(current_time.hour) #converts current hour to string
        hour_digits_list = [int(digit) for digit in hour_string] #makes a list of the hour digits
        print(hour_digits_list)
        minute_fun()
    
    elif hour==12: #it is 12pm             #add a dot indicating Pm!!!!!!!!!!!!!!!!!!!!!!!!!
        hour_string= str(current_time.hour) #converts current hour to string
        hour_digits_list = [int(digit) for digit in hour_string] #makes a list of the hour digits
        print(hour_digits_list)
        minute_fun()
        
       
        
    elif (0<hour<12): #it is the morning
        hour_string= str(current_time.hour) #converts current hour to string
        hour_digits_list = [int(digit) for digit in hour_string] #makes a list of the hour digits
        if len(hour_digits_list)==1: #if only one digit is in the hour list 
            hour_digits_list.insert(0,0) #add a 0 at index 0 to the list
            print(hour_digits_list)
            minute_fun()
    
        else:
            print(hour_digits_list)
            minute_fun()
            
    elif (hour>12): #it is the night            #add a dot indicating Pm!!!!!!!!!!!!!!!!!!!!!!!!!
        hour-=12 #subtract 12
        hour_string= str(current_time.hour) #converts current hour to string
        hour_string=str(hour) #sets current hour not in military format to string 
        hour_digits_list = [int(digit) for digit in hour_string] #makes a list of the hour digits
        if len(hour_digits_list)==1: #if only one digit is in the hour list 
            hour_digits_list.insert(0,0) #add a 0 at index 0 to the list
            print(hour_digits_list)
            minute_fun()
        else:
            print(hour_digits_list)
            minute_fun()
    
    combined_list = hour_digits_list + minute_digits_list
    return combined_list
            
    #return minute_digits_list

print("Press buttons on keypad. Ctrl+C to exit.")

try:
#     datetime_A()
    clkON()
    #reset()
    #start()
    #clkReset()
    GPIO.output(CLK_PINS[0], GPIO.HIGH)
    GPIO.output([27,22,13,2,5,6,26], GPIO.HIGH)

    combined_list = datetime_A()
    ssd_1 = combined_list[0]
    ssd_2 = combined_list[1]
    ssd_3 = combined_list[2]
    ssd_4 = combined_list[3]

    
    
    while True:
        
        
            
        
        while counter != 4: # while count is no equal to 4, will run the if statements
#             blink(CLK_PINS[counter])
            
            if counter == 0: # when counter = 0 -> corresponds to SSD1
                pressed = -1
                print(f"state: {state}")
                if state==0:
                    GPIO.output([27,22,13,2,5,6,26], GPIO.HIGH)
                if state==1: # if state == (0-14) then it will call each numbers function to turn the GPIO segments ON 
                    GPIO.output([22,13], GPIO.HIGH)
                if state==2:
                    GPIO.output([27,22,3,5,6], GPIO.HIGH)
                if state==3:
                    GPIO.output([27,22,3,13,6], GPIO.HIGH)
                if state==4:
                    GPIO.output([2,3,22,13], GPIO.HIGH)
                if state==5:
                    GPIO.output([27,2,3,13,6], GPIO.HIGH)
                if state==6:
                    GPIO.output([27,2,5,6,13,3], GPIO.HIGH)
                if state==7:
                    GPIO.output([27,22,13], GPIO.HIGH)
                if state==8:
                    GPIO.output([27,22,13,2], GPIO.HIGH)
                if state==9:
                    GPIO.output([27,2,22,3,13], GPIO.HIGH)
                if state==10:
                    GPIO.output(26, GPIO.HIGH)
            
                    
                displaySSD(CLK_PINS[0]) #calls displaySSD function to display on SSD
                
                
                
                GPIO.output(CLK_PINS[0], GPIO.LOW) # turns clk1 off 
                print(f"this is the counter {counter}")
                sleep(0.15)
               
            if counter == 1:
                pressed = -1
                state = ssd_2
                print(f"state: {state}")
                GPIO.output(CLK_PINS[0], GPIO.HIGH) #stores the value of the SSD1
                if state==0:
                    GPIO.output([27,22,13,2,5,6,26], GPIO.HIGH)
                if state==1: # if state == (0-14) then it will call each numbers function to turn the GPIO segments ON 
                    GPIO.output([22,13], GPIO.HIGH)
                if state==2:
                    GPIO.output([27,22,3,5,6], GPIO.HIGH)
                if state==3:
                    GPIO.output([27,22,3,13,6], GPIO.HIGH)
                if state==4:
                    GPIO.output([2,3,22,13], GPIO.HIGH)
                if state==5:
                    GPIO.output([27,2,3,13,6], GPIO.HIGH)
                if state==6:
                    GPIO.output([27,2,5,6,13,3], GPIO.HIGH)
                if state==7:
                    GPIO.output([27,22,13], GPIO.HIGH)
                if state==8:
                    GPIO.output([27,22,13,2], GPIO.HIGH)
                if state==9:
                    GPIO.output([27,2,22,3,13], GPIO.HIGH)
                if state==10:
                    GPIO.output(26, GPIO.HIGH)
            ###################################################
                if state==11:
                    invalid = 1
                if state==12:
                    invalid = 1
                if state==13:
                    invalid = 1
                if state==14:
                    invalid = 1
        
                displaySSD(CLK_PINS[1])
                GPIO.output(CLK_PINS[1], GPIO.LOW)
                print(f"this is the counter {counter}")
                sleep(0.15)
                
            if counter == 2:
                pressed = -1
                state = ssd_3
                print(f"state: {state}")
                GPIO.output(CLK_PINS[1], GPIO.HIGH) #stores the value of the SSD2
                if state==0:
                    GPIO.output([27,22,13,2,5,6,26], GPIO.HIGH)
                if state==1: # if state == (0-14) then it will call each numbers function to turn the GPIO segments ON 
                    GPIO.output([22,13], GPIO.HIGH)
                if state==2:
                    GPIO.output([27,22,3,5,6], GPIO.HIGH)
                if state==3:
                    GPIO.output([27,22,3,13,6], GPIO.HIGH)
                if state==4:
                    GPIO.output([2,3,22,13], GPIO.HIGH)
                if state==5:
                    GPIO.output([27,2,3,13,6], GPIO.HIGH)
                if state==6:
                    GPIO.output([27,2,5,6,13,3], GPIO.HIGH)
                if state==7:
                    GPIO.output([27,22,13], GPIO.HIGH)
                if state==8:
                    GPIO.output([27,22,13,2], GPIO.HIGH)
                if state==9:
                    GPIO.output([27,2,22,3,13], GPIO.HIGH)
                if state==10:
                    GPIO.output(26, GPIO.HIGH)
                 ###################################################
                if state==11:
                    #GPIO.output(4, GPIO.HIGH)
                    invalid = 1
                if state==12:
                    #GPIO.output(4, GPIO.HIGH)
                    invalid = 1
                if state==13:
                    #GPIO.output(4, GPIO.HIGH)
                    invalid = 1
                if state==14:
                    #GPIO.output(4, GPIO.HIGH)
                    invalid = 1
                
                displaySSD(CLK_PINS[2])
                GPIO.output(CLK_PINS[2], GPIO.LOW)
                print(f"this is the counter {counter}")
                sleep(0.25)
                
            if counter == 3:
                pressed = -1
                state = ssd_4
                print(f"state: {state}")
                GPIO.output(CLK_PINS[2], GPIO.HIGH) #stores the value of the SSD3
                if state==0:
                    GPIO.output([27,22,13,2,5,6,26], GPIO.HIGH)
                if state==1: # if state == (0-14) then it will call each numbers function to turn the GPIO segments ON 
                    GPIO.output([22,13], GPIO.HIGH)
                if state==2:
                    GPIO.output([27,22,3,5,6], GPIO.HIGH)
                if state==3:
                    GPIO.output([27,22,3,13,6], GPIO.HIGH)
                if state==4:
                    GPIO.output([2,3,22,13], GPIO.HIGH)
                if state==5:
                    GPIO.output([27,2,3,13,6], GPIO.HIGH)
                if state==6:
                    GPIO.output([27,2,5,6,13,3], GPIO.HIGH)
                if state==7:
                    GPIO.output([27,22,13], GPIO.HIGH)
                if state==8:
                    GPIO.output([27,22,13,2], GPIO.HIGH)
                if state==9:
                    GPIO.output([27,2,22,3,13], GPIO.HIGH)
                if state==10:
                    GPIO.output(26, GPIO.HIGH)
                 ###################################################
                if state==11:
                    #GPIO.output(4, GPIO.HIGH)
                    invalid = 1
                if state==12:
                    #GPIO.output(4, GPIO.HIGH)
                    invalid = 1
                if state==13:
                    #GPIO.output(4, GPIO.HIGH)
                    invalid = 1
                if state==14:
                    #GPIO.output(4, GPIO.HIGH)
                    invalid = 1
                
                displaySSD(CLK_PINS[3])
                GPIO.output(CLK_PINS[3], GPIO.LOW)
                print(f"this is the counter {counter}")
                sleep(0.25)
                
        while counter == 4:
            GPIO.output(CLK_PINS[3], GPIO.HIGH) #stores the value of the SSD4
            #counter-= 4
            sleep(0.25)
        
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       




