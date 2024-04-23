import RPi.GPIO as GPIO
import time

#GPIO pin set up for input (project part 1)
clk=13
dt=6
sw=5
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT) #GPIO Pin Setup for octocoupler
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw, GPIO.IN)

#declare and initialize
global freq

# PART 1 CODE
def encoder():
    #initialize the counter and the encoder turn
    counter=0
    lastClkState=GPIO.input(clk)
    lastSwState=GPIO.input(sw)

    #debouncing method, without one click would increment counter by 2
    def debounce():
    time.sleep(.2)
    state=1
    while True:
        #checks states if the pins
        clkState=GPIO.input(clk)
        dtState=GPIO.input(dt)
        swState=GPIO.input(sw)
        
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
        else:
            pass
        
        
#PART 2 CODE
def octo():
    global freq
    #Setting Up GPIO pin for PWM Output
    pwm = GPIO.PWM(19, 50)

    #Changing PWM Frequency by Hertz
    pwm.ChangeFrequency(freq) #should be set by user when turning encoder

    #Starting the PWM Output - Duty Cycle of 50%
    pwm.start(50)

    #Keeping PWM Running for 500 seconds
    time.sleep(500)

    #Stopping PWM Output
    pwm.stop()
    


try:
    while True:
        #check if turn is changing frequency by 25 RPM
        encoder()
        
except KeyboardInterrupt:
    print("\nProgram terminated by user.")