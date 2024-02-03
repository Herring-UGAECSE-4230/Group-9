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
GPIO.setup(ROW_1, GPIO.IN)
GPIO.setup(ROW_2, GPIO.IN)
GPIO.setup(ROW_3, GPIO.IN)
GPIO.setup(ROW_4, GPIO.IN)

#from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
#if needed set low by default: pull_up_down=GPIO.PUD_DOWN
GPIO.setup(COL_1, GPIO.OUT)
GPIO.setup(COL_2, GPIO.OUT)
GPIO.setup(COL_3, GPIO.OUT)
GPIO.setup(COL_4, GPIO.OUT)

def readKeypad(rowNum, char):
    GPIO.output(rowNum, GPIO.HIGH)
    If GPIO.input(COL_1==1):
        curVal = char[0]
    If GPIO.input(COL_2==1):
        curVal = char[1]
    If GPIO.input(COL_3==1):
        curVal = char[2]
    If GPIO.input(COL_4==1):
        curVal = char[3]
    GPIO.output(rowNum, GPIO.LOW)
    return curVal #check this SIMLINE

#physical keyboard layout
#loop checking each row
print("Press buttons on keypad. Ctrl+C to exit.")
try:
    while True:
        readKeypad(ROW_1,[1,2,3,'A'])
        readKeypad(ROW_2,[4,5,6,'B'])
        readKeypad(ROW_3,[7,8,9,'C'])
        readKeypad(ROW_4,['*',0,'#','D'])
        time.sleep(0.2)
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       
        
