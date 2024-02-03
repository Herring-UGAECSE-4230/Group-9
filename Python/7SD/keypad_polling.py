import RPi.GPIO as GPIO
import time

#setting row pins
ROW_1 = 26
ROW_2 = 19
ROW_3 = 13
ROW_4 = 6

#setting column pins
COL_1 = 5
COL_2 = 22
COL_3 = 27
COL_4 = 17

GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)

#from instructions: GPIO pins connected to the 'X' lines will be setup as inputs to the pad/output from the PI
GPIO.setup(ROW_1, GPIO.OUT)
GPIO.setup(ROW_2, GPIO.OUT)
GPIO.setup(ROW_3, GPIO.OUT)
GPIO.setup(ROW_4, GPIO.OUT)

#from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
#if need: initial = GPIO.LOW
GPIO.setup(COL_1, GPIO.IN) #if needed set low by default: pull_up_down=GPIO.PUD_DOWN
GPIO.setup(COL_2, GPIO.IN) #if needed set low by default: pull_up_down=GPIO.PUD_DOWN
GPIO.setup(COL_3, GPIO.IN) #if needed set low by default: pull_up_down=GPIO.PUD_DOWN
GPIO.setup(COL_4, GPIO.IN) #if needed set low by default: pull_up_down=GPIO.PUD_DOWN

def readKeypad(rowNum, char):
    GPIO.output(rowNum, GPIO.HIGH)
    if GPIO.input(COL_1==1):
        curVal = char[0]
    if GPIO.input(COL_2==1):
        curVal = char[1]
    if GPIO.input(COL_3==1):
        curVal = char[2]
    if GPIO.input(COL_4==1):
        curVal = char[3]
    GPIO.output(rowNum, GPIO.LOW)
    return curVal #check this SIMLINE


# def event_callback(pin):
#     value = GPIO.input(pin)
#     print(f"pin is {pin}, value is {value}")
#     #this callback below registers the key that was pressed if no other key is currently pressed
#     #global keypadPressed
#     #if keypadPressed == -1:
#         #keypadPressed = pin
  


# # events can be GPIO.RISING, GPIO.FALLING, or GPIO.BOTH
# GPIO.add_event_detect(ROW_1, GPIO.BOTH, callback = event_callback, bouncetime=300)
# GPIO.add_event_detect(ROW_2, GPIO.BOTH, callback = event_callback, bouncetime=300)
# GPIO.add_event_detect(ROW_3, GPIO.BOTH, callback = event_callback, bouncetime=300)
# GPIO.add_event_detect(ROW_4, GPIO.BOTH, callback = event_callback, bouncetime=300)


#physical keyboard layout
#loop checking each row
print("Press buttons on keypad. Ctrl+C to exit.")
try:
    while True:
        readKeypad(ROW_1,[1,2,3,'A'])
        readKeypad(ROW_2,[4,5,6,'B'])
        readKeypad(ROW_3,[7,8,9,'C'])
        readKeypad(ROW_4,['*',0,'#','D'])
        time.sleep(0.1)
except KeyboardInterrupt:
        print("\nApplication Interrupted") 
        GPIO.cleanup()       
        
