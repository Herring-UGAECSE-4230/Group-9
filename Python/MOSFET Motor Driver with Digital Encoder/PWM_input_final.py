import RPi.GPIO as GPIO
import time

#GPIO pin set up
clk=13
dt=6
sw=5
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw, GPIO.IN)

#initialize the counter and the encoder turn
counter=0
lastClkState=GPIO.input(clk)
lastSwState=GPIO.input(sw)

#debouncing method, without one click would increment counter by 2
def debounce():
    time.sleep(.2)
state=1
while True:
#     debounce()
    #checks states if the pins
    clkState=GPIO.input(clk)
    dtState=GPIO.input(dt)
    swState=GPIO.input(sw)
    
    #check if button is pressed
#     if swState!=lastSwState:
#         print("button pressed")
# #         debounce()
    
    #if statement to check for a turn
    if clkState!=lastClkState:
        if dtState!=clkState and state==1:
            print("clockwise")
            counter+=1

        else:
            print("counterclockwise")
            counter-=1
        lastClkState=clkState #update last clk state
        print(counter)
#         debounce()
    else:
        pass
#         print("none")



