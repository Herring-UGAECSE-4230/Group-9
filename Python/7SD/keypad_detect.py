import RPi.GPIO as GPIO
import time

def event_callback(pin):
    value = GPIO.input(pin)
    print(f"pin :: {pin}, value is {value}")
  
if __name__ == '__main__':
    BUTTON_pin = 23 # column pins
    ROW_pin = 17 # row pins

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #GPIO pins connected to the 'X' lines will be setup as inputs to the pad/output from the PI
    GPIO.setup(ROW_pin, GPIO.IN) 
    #pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
    GPIO.setup(BUTTON_pin, GPIO.OUT) #add this if needed: pull_up_down = GPIO.PUD_UP 

    GPIO.output(row_pin, GPIO.LOW)

    # events can be GPIO.RISING, GPIO.FALLING, or GPIO.BOTH
    GPIO.add_event_detect(BUTTON_pin, GPIO.BOTH, callback = event_callback, bouncetime=300)

    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        GPIO.cleanup()