# Part 1 RPi.GPIO __________________________________________

# imports necessary libraries
import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # calls the GPIO from the physical board 
GPIO.setup(23,GPIO.OUT,initial=GPIO.LOW) #setup pin 4 as output

freq = 100000   # sets a low frequency 
print(f"{freq}")
#running while loop 
while True:

  sleep(1/(freq*2))  # delay for blinking 
  GPIO.output(23, GPIO.HIGH)   #set output to high; turns ON LED    
    
  sleep(1/(freq*2)) # delay for blinking 
  GPIO.output(23,GPIO.LOW) # set LED output to low; turns OFF LED 
GPIO.cleanup()

# Part 2 Wiringpi ____________________________________________

import wiringpi 

wiringpi.wiringPiSetupGpio() # calls the GPIO pins by their GPIO pin number
wiringpi.softToneCreate(23) # using GPIO Pin # 23 


freq = 20 # variable to set frequency 
wiringpi.softToneWrite(23, freq) # sets desired freq 

while True:
    # creates an empty loop to keep the program running while the LED is blinking
    pass 


# Part 3 pigpio  _____________________________________________

import pigpio

pi = pigpio.pi()           

freq = 100000 # sets frequency variable 
pi.set_PWM_frequency(23, freq) # set GPIO 23 
pi.set_PWM_dutycycle(23, 128) # PWM 1/2 on aka duty cycle= 50% 
print(f"{freq}") # prints out the frequency

while True: 
    # empty loop that keeps program running while the LED is blinking.
    pass
