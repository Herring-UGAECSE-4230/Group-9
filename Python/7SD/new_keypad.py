import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #BCM numbering

#setting the rows and columns on keypad
keypad_rows = [18, 23, 24, 25] #X1-X4
keypad_cols = [12, 16, 20, 21] #Y1-Y4

#setting the respective GPIO pins to data pins to the segments
for row_pin in keypad_rows:
    GPIO.setup(row_pin, GPIO.OUT, initial = GPIO.LOW)
for col_pin in keypad_cols:
    GPIO.setup(col_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
    # GPIO.output(col_pin, GPIO.HIGH)

# #key press interpretation function
# while True:
#     # def readKeypad(keypad_rows, char):
#         for i in keypad_rows:
#             GPIO.output(keypad_rows[i], GPIO.HIGH) #cycles through each row and sets the corresponding GPIO pin high
#             for col in keypad_cols:
#                 if GPIO.input(col)==1:
#                     comparison(row,col)
                

#Define the mapping of keypad buttons to numbers
# keypad_mapping = {
#     (0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): "A",
#     (1, 0): 4, (1, 1): 5, (1, 2): 6, (1, 3): "B",
#     (2, 0): 7, (2, 1): 8, (2, 2): 9, (2, 3): "C",
#     (3, 0): "*", (3, 1): 0, (3, 2): "#", (3, 3): "D"}

keypad_mapping = {
    (18, 12): 1, (18, 16): 2, (18, 20): 3, (18, 21): "A",
    (23, 12): 4, (23, 16): 5, (23, 20): 6, (23, 21): "B",
    (24, 12): 7, (24, 16): 8, (24, 20): 9, (24, 21): "C",
    (25, 12): "*", (25, 16): 0, (25, 20): "#", (25, 21): "D"}

# keypad_mapping = [
#     [[18,12], 1], [[18, 1], 2], [[18, 2], 3],[[18, 3],"A"],
#     [[23,12], 4], [[1, 1], 5], [[1, 2], 6],[[1, 3],"B"],
#     [[24,12], 7], [[2, 1], 8], [[2, 2], 9],[[2, 3],"C"],
#     [[25,12], "*"], [[3, 1], 0], [[3, 2], "#"],[[3, 3],"D"],

# def comparison(row, column):
#     for row,col in keypad_rows,keypad_cols:
#         if row == keypad_rows[0] and col==keypad_cols[0]: # if row = 18 and col =12
#             print("1")
#         elif row == keypad_rows[0] and col==keypad_cols[1]: # if row = 18 and col =16
#             print("2")
#         elif row == keypad_rows[0] and col==keypad_cols[2]: # if row = 18 and col =20
#             print("3")
#         elif row == keypad_rows[0] and col==keypad_cols[3]: # if row = 18 and col =21
#             print("A")
#         elif row == keypad_rows[1] and col==keypad_cols[0]: # if row = 23 and col =12
#             print("4")
#         elif row == keypad_rows[1] and col==keypad_cols[1]: # if row = 23 and col =16
#             print("5")
#         elif row == keypad_rows[1] and col==keypad_cols[2]: # if row = 23 and col =20
#             print("6")  
#         elif row == keypad_rows[1] and col==keypad_cols[3]: # if row = 23 and col =21
#             print("B")     
#         elif row == keypad_rows[2] and col==keypad_cols[0]: # if row = 24 and col =12
#             print("7")
#         elif row == keypad_rows[2] and col==keypad_cols[1]: # if row = 24 and col =16
#             print("8") 
#         elif row == keypad_rows[2] and col==keypad_cols[2]: # if row = 24 and col =20
#             print("9") 
#         elif row == keypad_rows[2] and col==keypad_cols[3]: # if row = 24 and col =21
#             print("C")  
#         elif row == keypad_rows[3] and col==keypad_cols[0]: # if row = 25 and col =12
#             print("*") 
#         elif row == keypad_rows[3] and col==keypad_cols[1]: # if row = 25 and col =16
#             print("0") 
#         elif row == keypad_rows[3] and col==keypad_cols[2]: # if row = 25 and col =20
#             print("#") 
#         elif row == keypad_rows[3] and col==keypad_cols[3]: # if row = 25 and col =21
#             print("D") 


def compare_x(rows, columns, keypad_mapping):
#     result = []
#     for row_val, col_val in zip(keypad_rows, keypad_cols):
#         key = (row_val, col_val)
#         if key in keypad_mapping:
#             result.append(keypad_mapping[key])
#         else:
#             result.append(None)
#         print(result) #prints list
#     return result
    key = (tuple(rows), tuple(columns))
    if key in keypad_mapping:
        return keypad_mapping[key]
    else:
        return None

def readKeypad(row, col):
    for row in keypad_rows:
        GPIO.output(row, GPIO.HIGH)
        for col in keypad_cols:
            if GPIO.input(col) == GPIO.HIGH:
                return row, col
        GPIO.output(row, GPIO.LOW)
    return None, None

# while True:
#     readKeypad(row,keypad_mapping.keys)
#     
# compare_result = compare_x(keypad_rows, keypad_cols, keypad_mapping)
# print(compare_result) #prints actual num

# main loop
try:
    while True:
        row_pressed, col_pressed = readKeypad(keypad_rows, keypad_cols)
        
        if row_pressed is not None and col_pressed is not None:
            print(f"Key pressed: {row_pressed}-{col_pressed}")
            
        # comparing part
            key_result = compare_x([row_pressed], [col_pressed], keypad_mapping)
            
            if key_result is not None:
                print(f"Mapped value: {key_result[0]}")
                
            else:
                print("not mapped")
finally:
    GPIO.cleanup()
