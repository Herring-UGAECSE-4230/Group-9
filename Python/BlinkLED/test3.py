import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT,initial=GPIO.LOW)
p = GPIO.PWM(4, 100)   # 1 Hz, or 1 blink per second

while True:
    p.start(50)        #   50% duty cycle  
    time.sleep(1)