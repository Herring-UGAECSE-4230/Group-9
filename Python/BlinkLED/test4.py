import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
while True:
    p = GPIO.PWM(4,.5,)
    p.start(50)
    input('Press return to stop:')   # use raw_input for Python 2
    # time.sleep(10)

p.stop()
GPIO.cleanup()

