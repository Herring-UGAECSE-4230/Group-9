import RPi.GPIO as GPIO
import time

# #setting row pins
# ROW_1 = 18
# ROW_2 = 23
# ROW_3 = 24
# ROW_4 = 25

# #setting column pins
# COL_1 = 12
# COL_2 = 16
# COL_3 = 20
# COL_4 = 21

# Define the pin numbers for the keypad rows and columns
keypad_rows = [18, 23, 24, 25] #X1-X4
keypad_cols = [12, 16, 20, 21] #Y1-Y4

# Define the mapping of keypad buttons to numbers
keypad_mapping = {
    (0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): "A",
    (1, 0): 4, (1, 1): 5, (1, 2): 6, (1, 3): "B",
    (2, 0): 7, (2, 1): 8, (2, 2): 9, (2, 3): "C",
    (3, 0): "*", (3, 1): 0, (3, 2): "#", (3, 3): "D"
}
# Function to get the pressed key
def get_key():
    for col, col_pin in enumerate(keypad_cols):
        GPIO.output(col_pin, GPIO.LOW)
        for row, row_pin in enumerate(keypad_rows):
            if GPIO.input(row_pin) == GPIO.LOW:
                key = keypad_mapping.get((row, col))
                if key:
                    return key
        GPIO.output(col_pin, GPIO.HIGH)
    return None

GPIO.setwarnings(False)
#BCM numbering
GPIO.setmode(GPIO.BCM)


# Set up GPIO pins for keypad rows and columns
for row_pin in keypad_rows:
    GPIO.setup(row_pin, GPIO.OUT, initial = GPIO.LOW)
for col_pin in keypad_cols:
    GPIO.setup(col_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
    # GPIO.output(col_pin, GPIO.HIGH)
# #from instructions: GPIO pins connected to the 'X' lines will be setup as inputs to the pad/output from the PI

# GPIO.setup(ROW_1, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(ROW_2, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(ROW_3, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(ROW_4, GPIO.OUT, initial=GPIO.LOW)

# #from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
# #if needed set low by default: pull_up_down=GPIO.PUD_DOWN
# GPIO.setup(COL_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(COL_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(COL_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(COL_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readKeypad(rowNum, char):
    GPIO.output(rowNum, GPIO.HIGH)
    if GPIO.input(col_pin)==1:
        print(char[0])
    if GPIO.input(col_pin)==1:
        print(char[1])
    if GPIO.input(col_pin)==1:
        print(char[2])
    if GPIO.input(col_pin)==1:
        print(char[3])
    # else: 
    GPIO.output(rowNum, GPIO.LOW)
    # return curVal #check this SIMLINE
    print(char[0])


#physical keyboard layout
#loop checking each row
print("Press buttosns on keypad. Ctrl+C to exit.")
try:
    while True:
        readKeypad(row_pin,['1','2','3','A'])
        readKeypad(row_pin,['4','5','6','B'])
        readKeypad(row_pin,['7','8','9','C'])
        readKeypad(row_pin,['*','0','#','D'])
        time.sleep(0.2)
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       
        
