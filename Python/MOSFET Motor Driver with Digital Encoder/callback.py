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

#debouncing method, without one click would increment counter by 2
def debounce():
    time.sleep(.5)

while True:
    debounce()

    #checks states if the pins
    clkState=GPIO.input(clk)
    dtState=GPIO.input(dt)
    #if statement to check for a turn
    if clkState!=lastClkState:
        if dtState!=clkState:
            print("clockwise")
            counter+=1
            debounce()
#             time.sleep(10)
        else:
            print("counterclockwise")
            counter-=1
        lastClkState=clkState #update last clk state
        print(counter)
        debounce()



