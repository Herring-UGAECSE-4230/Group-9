import RPi.GPIO as GPIO
import time
from time import sleep

#Rotary Encoder initialization
clk=13
dt=6
sw=5


#GPIO set up
GPIO.setmode(GPIO.BCM)

#for encoder
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#other variable initialization
counter = 0
totalTurns = 0
turnsPerSecond = 0
lastClkState=GPIO.input(clk)
currentTime= time.time()

buttonPress = 0
lastPress = 0

debounce_scale = 1
turn_momentum = 0

direction_tracker = []

is_turning = False

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        
        if clkState!=lastClkState:
            is_Turning = True
            turns_per_second = 1/((time.time() - currentTime)*38.75)
            if dtState!=clkState:
                if turn_momentum > 0:
                    counter+= 1
                    print("Clockwise at", str(turns_per_second)[:5] + "turns/second", "Turn: " + str(totalTurns))
                    direction_tracker.append([1])
                    totalTurns += 1
                if turn_momentum != debounce_scale:
                    turn_momentum += 1
                currentTime = time.time()
            else:
                if turn_momentum < 0:
                    counter -= 1
                if turn_momentum != -(debounce_scale):
                    turn_momentum -= 1
                    print("CounterClockwise at", str(turns_per_second)[:5] + "turns/second", "Turn: " + str(totalTurns))
                    direction_tracker.append([0])
                    totalTurns += 1
                if turn_momentum != debounce_scale:
                    turn_momentum -= 1
                currentTime = time.time()
        if (clkState and dtState == 1) and (time.time() - currentTime > 2):
            print("Not Turning")
            time.sleep(.1)
        buttonPress = GPIO.input(sw)
        if buttonPress == 0 and buttonPress != lastPress:
            print("pressed")
        lastPress = buttonPress
        lastClkState = clkState
finally:
    print("done")
                    
