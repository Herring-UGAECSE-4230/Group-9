import pigpio
import time 
from time import sleep 

pi=pigpio.pi() # selects the local pi for control with

freq = 1000 # sets frequency variable 
pi.set_PWM_frequency(23, freq) # set GPIO 23 


while True: 
    pi.set_PWM_dutycycle(23, 128) # set the duty cycle 50 % 
    
    # empty loop that keeps program running while the LED is blinking.
    pass 

wiringpi.softToneWrite(23, 0) # set the pin frequency to 0 to shut it off 
 
