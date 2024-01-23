# Part 1 RPi.GPIO 

# import
import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # calls the GPIO from the physical board 
GPIO.setup(4,GPIO.OUT,initial=GPIO.LOW) #setup pin 

# running while loop 
while True:
  GPIO.output(4, GPIO.HIGH)    
  sleep(0.5)
  GPIO.output(4,GPIO.LOW)


