import pigpio
import time 
from time import sleep 

# pi=pigpio.pi('group9', 8889) # selects the local pi for control with
pi = pigpio.pi()             # exit script if no connection
if not pi.connected:
   exit()
freq = 100000 # sets frequency variable 
pi.set_PWM_frequency(23, freq) # set GPIO 23 
pi.set_PWM_dutycycle(23, 128) # PWM 1/2 on aka duty cycle=  %50 
print(f"{freq}")

while True: 
    # empty loop that keeps program running while the LED is blinking.
    pass
