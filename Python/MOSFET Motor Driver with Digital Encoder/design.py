import RPi.GPIO as GPIO
import pigpio
import time
from pigpio_encoder.rotary import Rotary
from math import e

#IR sensor initialization
IR_pin = 21

#GPIO Pin Setup for PWM
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

#pin setup for IR
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Setting Up GPIO pin for PWM Output
pwm = GPIO.PWM(19, 50)

pi = pigpio.pi()

#variabl initialization
start_flag = 1
last_counter = 0
desired_RPM = 1861
DC = 0
counter_RPM = 0
restart = 0
tyler = 0
RPM_value = 0
DC =20
desired_RPM = 0
sofia = 0

#function called when rotary encoder is turned
def rotary_callback(counter):
    global last_counter, desired_RPM, DC, counter_RPM, RPM_value, end_time
    if counter > last_counter:  #counter clockwise
        last_counter = counter
        if pi.read(13)==1:
#             RPM = -789.552 + 884.9955*ln(DC)
            desired_RPM += 25 #increment RPMs by 25 with each encoder spin
            DC = e**((desired_RPM+789.552)/884.9955)
            pwm.start(DC) #makes the motor spin at the desired duty cycle to increase the RPMs by 25
            counter = 0
            count_for_math = 0
            start_time = time.time()
            switch = 0
            if tyler == 1:
                while count_for_math < 8:
                    if pi.read(21) == 1 and not switch:
                        count_for_math += 1
                        switch = 1
                    else:
#                         pi.read(21) == 0 and switch:
                        switch = 0
                end_time = time.time()
                total_time = end_time - start_time
                time_var = 60/total_time  # time_multiplier_to_get_to_60_sec
                RPM_value = time_var/20
                
#function called when sw is short pressed
def sw_short():
    global start_flag, tyler
    tyler = 1
    if start_flag ==1:
        start_func()
        start_flag = 0
    elif start_flag == 0:
        stop_func()
        start_flag = 1

def start_func():
    global DC, RPM_value, desired_RPM, sofia
    #initliazes freqency value
    pwm.ChangeFrequency(1000)
    #starts PWN output aka motor
    DC = 20
    pwm.start(DC)
    tyler = 1
    desired_RPM = 1861
    if sofia == 0:
        RPM_value = 1761
        sofia = 1
    if sofia == 1:
        pass

def stop_func():
    global RPM_value, sofia
    RPM_value = 0
    #Stopping PWM Output aka motor
    pwm.stop()

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

# (revolutions / min) / 3 = what we want
try:
    while True:
        print(f"Actual RPM: {RPM_value/2}")
        time.sleep(.3)
        print(f"Expected RPM: {desired_RPM/2}")
        time.sleep(.3)
       
except:
    GPIO.cleanup()