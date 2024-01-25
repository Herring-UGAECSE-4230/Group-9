# import
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # calls the GPIO from the physical board 
GPIO.setup(4,GPIO.OUT,initial=GPIO.LOW) #setup pin 4 as output

p = GPIO.PWM(4,100)
p.start(0)

while True:
        for dc in range(0,101,5):
            p.ChangeDutyCycle(dc)
            time.sleep(.5)
        for dc in range(100,-1,-5):
            p.ChangeDutyCycle(dc)
            time.sleep(.5)

# p.stop()
# GPIO.cleanup()


# while True:
  
#   GPIO.output(4, GPIO.HIGH)   #set output to high
#   print("LED is ON")
  
#   sleep(.5) # keep LED on for 0.04 second 
  
#   GPIO.output(4,GPIO.LOW) # set LED output to low 
#   print("LED is off") 

#   sleep(.5) # keep LED on for 0.04 second 

