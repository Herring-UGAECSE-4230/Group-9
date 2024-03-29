# Part 1 RPi.GPIO __________________________________________

# imports necessary libraries
import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # calls the GPIO from the physical board 
GPIO.setup(23,GPIO.OUT,initial=GPIO.LOW) #setup pin 4 as output

freq = 5   # sets a low frequency 
print(f"{freq}")
#running while loop 
while True:

  sleep(1/(freq*2))  # delay for blinking 
  GPIO.output(23, GPIO.HIGH)   #set output to high; turns ON LED    
    
  sleep(1/(freq*2)) # delay for blinking 
  GPIO.output(23,GPIO.LOW) # set LED output to low; turns OFF LED 
GPIO.cleanup()
