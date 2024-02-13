import RPi.GPIO as GPIO
import time
#setting row pins
ROW_1 = 18
ROW_2 = 23
ROW_3 = 24
ROW_4 = 25
#setting column pins
COL_1 = 12
COL_2 = 16
COL_3 = 20
COL_4 = 21

GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)
#from instructions: GPIO pins connected to the 'X' lines will be setup as inputs to the pad/output from the PI
GPIO.setup(ROW_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_4, GPIO.OUT, initial=GPIO.LOW)
#from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
#if needed set low by default: pull_up_down=GPIO.PUD_DOWN
GPIO.setup(COL_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def readKeypad(rowNum, char):
    GPIO.output(rowNum, GPIO.HIGH)
    if GPIO.input(COL_1)==1:
        print(char[0])
    if GPIO.input(COL_2)==1:
        print(char[1])
    if GPIO.input(COL_3)==1:
        print(char[2])
    if GPIO.input(COL_4)==1:
        print(char[3])
    # else: 
    GPIO.output(rowNum, GPIO.LOW)
    # return curVal #check this SIMLINE
    # print(characters[0])
#physical keyboard layout
#loop checking each row
print("Press buttons on keypad. Ctrl+C to exit.")
try:
    while True:
        readKeypad(ROW_1,['1','2','3','A'])
        readKeypad(ROW_2,['4','5','6','B'])
        readKeypad(ROW_3,['7','8','9','C'])
        readKeypad(ROW_4,['*','0','#','D'])
        time.sleep(0.2)
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       
