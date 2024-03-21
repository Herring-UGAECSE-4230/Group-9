import RPi.GPIO as GPIO
import time

#GPIO Pin Setup for PWM
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

#Setting Up GPIO pin for PWM Output
pwm = GPIO.PWM(12, 50)

#Changing PWM Frequency by Hertz
pwm.ChangeFrequency(100000)

#Starting the PWM Output - Duty Cycle of 50%
pwm.start(50)

#Keeping PWM Running for 500 seconds
time.sleep(500)

#Stopping PWM Output
pwm.stop()





