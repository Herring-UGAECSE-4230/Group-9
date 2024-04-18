import RPi.GPIO as GPIO
import pigpio
import time
from pigpio_encoder.rotary import Rotary
from math import e

#GPIO Pin Setup for PWM
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

#pin setup for IR sensor
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Setting Up GPIO pin for PWM Output
pwm = GPIO.PWM(19, 50)

pi = pigpio.pi()

#variable initialization
start_flag = 1
last_counter = 0
desired_RPM = 1861
DC = 0
counter_RPM = 0
restart = 0
tyler = 0
RPM_value = 0
DC = 20
desired_RPM = 0
sofia = 0

#function called when rotary encoder is turned
def rotary_callback(counter):
    global last_counter, desired_RPM, DC, counter_RPM, RPM_value, end_time
    if counter > last_counter:  #if there is a counter-clockwise turn
        last_counter = counter #resets last_counter to be the current counter value
        if pi.read(13)==1: #if pin 13 of the pi is high, aka the clk pin
#             RPM = -789.552 + 884.9955*ln(DC) #equation created from the log regression of some experimental data
            desired_RPM += 50 #increment the desired RPMs by 25 with each encoder spin
            DC = e**((desired_RPM+789.552)/884.9955) #sets the duty cycle to be the necessary value in order to ensure the desired RPMs are met. This is a rearrangement of the RPM equation solved for duty cycle.
            pwm.start(DC) #makes the motor spin at the duty cycle set directly above
            counter = 0 #ya know I don't actually think this does anything, but Im commenting the code rn so I dont want to remove something that might be crucial, TLDR; probs can be removed
            count_for_math = 0 #initalizes a counter that will be used in the while loop for counting when 8 blade rotations will have occured
            start_time = time.time() #gets the start time of the while loop
            switch = 0 #boolean created for switching between a blade being sensed and not sensed
            if tyler == 1: # this while loop just ensures that rotary encoder will be pressed aka has started the motor
                while count_for_math < 8:
                    if pi.read(21) == 1 and not switch: #if the IR sensor is activated
                        count_for_math += 1 #increment counter
                        switch = 1 #switch boolean value
                    else: #if IR sensor is not activated
                        switch = 0 #switch boolean value so previous condition can be met with the next blade activation
                end_time = time.time() #get the end time of when the while loop finishes aka the end time of when two full revolutions are completed
                total_time = end_time - start_time #get the total time it took for the two revolutions to be completed
                time_var = 60/total_time 
                RPM_value = time_var/20 #this calculates the actual RPM value
                
#function called when sw is short pressed
def sw_short():
    global start_flag, tyler
    tyler = 1 #makes the boolean true for when the encoder is pressed, use in the rotary call back function
    if start_flag ==1: #waiting for motor to be started
        start_func() #calls start function
        start_flag = 0 #sets flag to false so next encoder press will result in a stop
    elif start_flag == 0: #flag is now false
        stop_func() #stop function is called
        start_flag = 1 #flag is reset

def start_func(): #function to start motor
    global DC, RPM_value, desired_RPM, sofia
    pwm.ChangeFrequency(1000) #set frequency of the PWM
    DC = 20 #inital duty cycle value the motor will spin with
    pwm.start(DC) #inital started motor at 20% duty cycle
    tyler = 1 
    desired_RPM = 1861 #inital desired_RPMs 
    if sofia == 0: 
        RPM_value = 1761
        sofia = 1
    if sofia == 1:
        pass

def stop_func(): #function called in order to stop motor
    global RPM_value, sofia
    RPM_value = 0 #sets RPM values to 0
    pwm.stop() #Stopping PWM Output aka motor

#setting up the rotary encoders
my_rotary = Rotary(
            clk_gpio=13,
            dt_gpio=6,
            sw_gpio=5
        )
my_rotary.setup_rotary(
            min=0,
            max=100000000,
            scale=1,
            debounce=200,
            rotary_callback=rotary_callback
        )

my_rotary.setup_switch(
    debounce=200,
    long_press=True,
    sw_short_callback=sw_short,
        )

edge_count =0 
def count(GPIO):
    global edge_count
    edge_count += 1

#detects everytime there is a rising edge aka the fan blade activates the IR sensor
GPIO.add_event_detect(IR_pin, GPIO.RISING, callback = count)

# (revolutions / min) / 3 = what we want ***** should actually be /4
try:
    while True:
        print(f"Actual RPM: {RPM_value/2}")
        time.sleep(.3)
        print(f"Expected RPM: {desired_RPM/2}")
        time.sleep(.3)
       
except:
    GPIO.cleanup()
