import pigpio
import RPi.GPIO
# from xyimport import StepperMotor
from pigpio_encoder.rotary import Rotary

last_counter = 0  # Initialize last_counter outside the function
pi = pigpio.pi()
# motor = StepperMotor(pi, 23, 24, delayAfterStep = .001) 

def rotary_callback(counter):
    global last_counter
    print("Counter value:", counter)
    if counter > last_counter:
        last_counter = counter
        print("clockwise + 1")
    elif counter < last_counter:
        last_counter = counter
        print("counterclockwise - 1")
    else:
        print("none")

def sw_short():
    print("Switch short press")

def sw_long():
    print("Switch long press")

clk_gpio=13
GPIO.setup(clk_gpio,GPIO.IN, pull_up_down = GPIO.PUD_UP) #later on5
def stateCheck():
    count = 0
    lastClkState = GPIO.input(clk_gpio)
    while True:
        clkState = GPIO.input(clk_gpio)
        dtState = GPIO.input(dt_gpio)
        if clkState != lastClkState:
            if dtState != clkState:
                count+=1
                print("clockwise + 1")
            else:
                count+=1
        lastClkState=clkState
        print(count)

#sets up the rotary encoder pins
my_rotary = Rotary(
    clk_gpio=13,
    dt_gpio=6,
    sw_gpio=5
)

#sets up the range for the counter of the rotary encoder, debouces, and establishes the callback used when the encoder is turned
my_rotary.setup_rotary(
    min=0,
    max=1100,
    scale=1,
    debounce=200,
    #rotary_callback=rotary_callback
    rotary_callback=stateCheck
)

#sets up the call backs for if the switch is short pressed and long pressed
my_rotary.setup_switch(
    debounce=200,
    long_press=True,
    sw_short_callback=sw_short,
    sw_long_callback=sw_long
)

my_rotary.watch()



