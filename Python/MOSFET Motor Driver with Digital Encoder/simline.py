import pigpio
import RPi.GPIO as GPIO
# from xyimport import StepperMotor
from pigpio_encoder.rotary import Rotary
import time

last_counter = 0  # Initialize last_counter outside the function
pi = pigpio.pi()
last_time = time.time()
# motor = StepperMotor(pi, 23, 24, delayAfterStep = .001) 

# SIMLINE'S IDEA: if you have a timer running and there is no rotation with the rotary encoder, then "none" would be printed??
# Anotha idea: we can also make a function where it counts the number of turns per second based upon the timing function and rotary_callback() as well

#turns = counter
#print(f"turns/second: {turns}")

#VERSION 1
# def rotary_callback(counter):
#     global last_counter
#     #print("Counter value:", counter)
#     start = time.time()
#     if counter > last_counter:
#         last_counter = counter
#         print("clockwise + 1")
#         end = time.time()
#     elif counter < last_counter:
#         last_counter = counter
#         print("counterclockwise - 1")
#         end = time.time()
#     else:
#         print("none")
#     print("Counter value:", counter)
#     
#     #turns/second
#     timing = end - start
#     print(timing)
# #     if (timing % 1 == 1):
# #        turns_per_second = counter/timing
# #     print(f"turns/second: {turns_per_second}")
    
    
#VERSION 2
# including do not turn....
#what works: getting number of turns per sec
#need: print cw/ccw and not go into none automatically
#possible solution: make overall clock to account for "do not turn" or "none" per second while not affecting cw/ccw
def rotary_callback(counter):
    global last_counter, last_time
    curr_time = time.time()
    elapsed_time = curr_time - last_time
    
    if elapsed_time != 0:
        turns_per_sec = (counter - last_counter) / elapsed_time
        print("turns/sec:", turns_per_sec)
        
    last_counter = counter
    last_time = curr_time
        
    if counter > last_counter:
        last_counter = counter
        print("clockwise + 1")
    elif counter < last_counter:
        last_counter = counter
        print("counterclockwise - 1")
#     else:
#         print("none")
    print("Counter value:", counter)
    print(" ")
    

    

def sw_short():
    print("press")

#def sw_long():
#    print("Switch long press")

#sets up the rotary encoder pins
my_rotary = Rotary(
    clk_gpio=6,
    dt_gpio=13,
    sw_gpio=5
)

#sets up the range for the counter of the rotary encoder, debouces, and establishes the callback used when the encoder is turned
my_rotary.setup_rotary(
    min=0,
    max=1100,
    scale=1,
    debounce=200,
    rotary_callback=rotary_callback
)

#sets up the call backs for if the switch is short pressed and long pressed
my_rotary.setup_switch(
    debounce=200,
    long_press=True,
    sw_short_callback=sw_short,
#    sw_long_callback=sw_long
)

my_rotary.watch()

# while True:
#     state = " "
#     print(state)
#     print(counter)
