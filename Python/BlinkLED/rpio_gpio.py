# # Part 1 RPi.GPIO 

# # import
# import RPi.GPIO as GPIO
# import time
# from time import sleep

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM) # calls the GPIO from the physical board 
# GPIO.setup(4,GPIO.OUT,initial=GPIO.LOW) #setup pin 4 as output

# #running while loop 
# while True:
  
#   GPIO.output(4, GPIO.HIGH)   #set output to high
#   print("LED is ON")
  
#   sleep(0.5) # keep LED on for 0.04 second 
  
#   GPIO.output(4,GPIO.LOW) # set LED output to low 
#   print("LED is off") 

#   sleep(0.5) # keep LED on for 0.04 second 

