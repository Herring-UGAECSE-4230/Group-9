# Define the pin numbers for the segments of the 7-segment display
segments = [int(2), int(3), int(2), int(22), int(5), int(6), int(13), int(26)] #data pins from DFF


# #funtion to call specfic segments and make GPIO HIGH
# def readGPIO(pins):
#     for pins in range(segments):
#         GPIO.output(int(pins), GPIO.HIGH)
#         print("12")
import RPi.GPIO as GPIO

def readGPIO(pins):
    GPIO.setmode(GPIO.BCM)
    
    for pins in segments:
        GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
    try:
        for pins in segments:
            GPIO.output(pins, GPIO.HIGH)
            print("!")
    finally:
        GPIO.cleanup()
        

readGPIO(2)