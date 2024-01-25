import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT,initial=GPIO.LOW)

while True:
    p = GPIO.PWM(4, 1000)   # 1 Hz, or 1 blink per second
    p.start(50)        #   50% duty cycle  
    time.sleep(100)