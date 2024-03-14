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

while True:

    #checks states if the pins
    clkState=GPIO.input(clk)
    dtState=GPIO.input(dt)
    swState=GPIO.input(sw)

    #if statement to check for a turn
    if clkState!=lastClkState:
        if dtState!=clkState:
            print("clockwise")
            counter+=.5

        else:
            print("counterclockwise")
            debounce
            counter-=1
        lastClkState=clkState #update last clk state
        print(counter)



