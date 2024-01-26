# Part 1 RPi.GPIO 

# import
import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # calls the GPIO from the physical board 
GPIO.setup(4,GPIO.OUT,initial=GPIO.LOW) #setup pin 4 as output

freq = 50   # sets a low frequency 

#running while loop 
while True:

  sleep(1/(freq * 2))  # delay for blinking 
  GPIO.output(4, GPIO.HIGH)   #set output to high; turns ON LED 
  print("LED is ON")   
  
  sleep(1/(freq * 2)) # delay for blinking 
  GPIO.output(4,GPIO.LOW) # set LED output to low; turns OFF LED 
  print("LED is off") 

  GPIO.cleanup()
