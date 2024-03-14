import pigpio
from xyimport import StepperMotor
from pigpio_encoder.rotary import Rotary


pi = pigpio.pi()
motor_x = StepperMotor(pi, 24, 23, delayAfterStep = .001) 
motor_y = StepperMotor(pi, 25, 12, delayAfterStep = .001) 
motor_z = StepperMotor(pi, 16, 26, delayAfterStep = .0019) 

last_counter = 0  # Initialize last_counter outside the function

def rotary_callback_x(counter):
    global last_counter

    # print("Counter value:", counter)

    if counter > last_counter:
        last_counter = counter
            # print("clockwise + 10")
        up_callback_x(16)
    elif counter < last_counter:
        last_counter = counter
        if pi.read(9)==1:
            return
        else:
        # print("counterclockwise - 10")
            down_callback_x(16)
    else:
        print("else of x")


def rotary_callback_y(counter):
    global last_counter

    # print("Counter value:", counter)

    if counter > last_counter:
        last_counter = counter
        if pi.read(10)==1:
            return
        else:
            up_callback_y(16)
        # print("clockwise + 10")
    elif counter < last_counter:
        last_counter = counter
        down_callback_y(16)
        # print("counterclockwise - 10")
    else:
        print("else of y")

global state
state=1
def sw_short_y():
    global state
    if state==1:
        pen_down(200)
        state=2
        return
    else:
        pen_up(200)
        state=1
    
def pen_down(x):
    for _ in range(x):
        motor_z.doCounterclockwiseStep()
        # time.sleep(.0025)

def pen_up(x):
    for _ in range(x):
        motor_z.doClockwiseStep()
        # time.sleep(.0025)



def up_callback_x(x):
    for _ in range(x):
        motor_x.doClockwiseStep()
def up_callback_y(x):
    for _ in range(x):
        motor_y.doClockwiseStep()

def down_callback_x(x):
    for _ in range(x):
        motor_x.doCounterclockwiseStep()
def down_callback_y(x):
    for _ in range(x):
        motor_y.doCounterclockwiseStep()

my_rotary_y = Rotary(
    clk_gpio=13,
    dt_gpio=6,
    sw_gpio=5
)
my_rotary_y.setup_rotary(
    min=0,
    max=10000000,
    scale=1,
    debounce=200,
    rotary_callback=rotary_callback_y
)
# my_rotary_y.setup_switch(
#     debounce=200,
#     long_press=True,
#     sw_short_callback=sw_short,
# )

#my_rotary_y.watch()

my_rotary_x = Rotary(
    clk_gpio=22,
    dt_gpio=27,
    sw_gpio=17
)
my_rotary_x.setup_rotary(
    min=0,
    max=10000,
    scale=1,
    debounce=200,
    rotary_callback=rotary_callback_x
)
# my_rotary_x.setup_switch(
#     debounce=200,
#     long_press=True,
#     sw_short_callback=sw_short
# )

# my_rotary_x.watch()


my_rotary_z= Rotary(
    clk_gpio=13,
    dt_gpio=6,
    sw_gpio=5
)

my_rotary_z.setup_switch(
    debounce=200,
    long_press=True,
    sw_short_callback=sw_short_y
)

my_rotary_z.watch()


