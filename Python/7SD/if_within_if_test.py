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
# Define the pin numbers for the segments of the 7-segment display
segments = [2, 3, 27, 22, 5, 6, 13, 26] #data pins from DFF

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

# 18, 12): 1, (18, 16): 2, (18, 20): 3, (18, 21): "A",
#     (23, 12): 4, (23, 16): 5, (23, 20): 6, (23, 21): "B",
#     (24, 12): 7, (24, 16): 8, (24, 20): 9, (24, 21): "C",
#     (25, 12): "*", (25, 16): 0, (25, 20): "#", (25, 21): "D"}


#keypad_value= 2
def readKeypad(rowNum,char):
    GPIO.output(rowNum, GPIO.HIGH)
    if GPIO.input(COL_1)==1:
        #col_1 is 12
        if rowNum==18:
            print("1")
        if rowNum==23:
            print("4")
        if rowNum==24:
            print("7")
        if rowNum==25:
            print("*")
    if GPIO.input(COL_2)==1:
         #col_1 is 16
        if rowNum==18:
            print("2")
        if rowNum==23:
            print("5")
        if rowNum==24:
            print("8")
        if rowNum==25:
            print("0")
    if GPIO.input(COL_3)==1:
         #col_1 is 20
        if rowNum==18:
            print("3")
        if rowNum==23:
            print("6")
        if rowNum==24:
            print("9")
        if rowNum==25:
            print("#")
      
       
    if GPIO.input(COL_4)==1:
         #col_1 is 21
        if rowNum==18:
            print("A")
        if rowNum==23:
            print("B")
        if rowNum==24:
            print("C")
        if rowNum==25:
            print("D")
       
    GPIO.output(rowNum, GPIO.LOW)
    # return curVal #check this SIMLINE
    
#         
# def compare(row, col):
#     #rowNum = 0
#     #colNum = 0
#     if rowNum == 0:
#         if colNum == 0:
#             GPIO.output(rowNum, GPIO.HIGH) #row
#             GPIO.input(colNum, GPIO.HIGH) #col
#         elif colNum == 1:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 2:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 3:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#     elif rowNum == 1:
#         if colNum == 0:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 1:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 2:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 3:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#     elif rowNum == 2:
#         if colNum == 0:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 1:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 2:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 3:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#     elif rowNum == 3:
#         if colNum == 0:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 1:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 2:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#         elif colNum == 3:
#             GPIO.output(rowNum, GPIO.HIGH) 
#             GPIO.input(colNum, GPIO.HIGH)
#     print(f"row: {rowNum}")
#     print(f"col: {colNum}")
        
#physical keyboard layout
#loop checking each row
print("Press buttons on keypad. Ctrl+C to exit.")


# Function to light up segments for a given number
def display_number(number):
    # Define the segments required to display each number
    numbers = {
        0: [1, 1, 1, 1, 1, 1, 0, 0],
        1: [0, 1, 1, 0, 0, 0, 0, 0],
        2: [1, 1, 0, 1, 1, 0, 1, 0],
        3: [1, 1, 1, 1, 0, 0, 1, 0],
        4: [0, 1, 1, 0, 0, 1, 1, 0],
        5: [1, 0, 1, 1, 0, 1, 1, 0],
        6: [1, 0, 1, 1, 1, 1, 1, 0],
        7: [1, 1, 1, 0, 0, 0, 0, 0],
        8: [1, 1, 1, 1, 1, 1, 1, 0],
        9: [1, 1, 1, 1, 0, 1, 1, 0],
        10: [0, 0, 0, 0, 0, 0, 0, 1] #dp
    }
    i=number
    print(numbers[i])
#     
#     # Turn on/off the segments based on the number
#     for i, segment_pin in enumerate(segments):
#         GPIO.output(segment_pin, numbers[number][i])


try:
    while True:
        readKeypad(ROW_1,['1','4','7','*'])
        readKeypad(ROW_2,['2','5','8','0'])
        readKeypad(ROW_3,['3','6','9','#'])
        readKeypad(ROW_4,['A','B','C','D'])
        time.sleep(.2)
    
# 
#         readKeypad(ROW_1,['1','2','3','A'])
#         readKeypad(ROW_2,['4','5','6','B'])
#         readKeypad(ROW_3,['7','8','9','C'])
#         readKeypad(ROW_4,['*','0','#','D'])
#         time.sleep(0.2)
#         
#         print(display_number(keypad_value))
# #         print(keypad_value)
#         compare(rowNum, colNum)
        
except KeyboardInterrupt:
        print("\nKeypad Application Interrupted") 
        GPIO.cleanup()       


