import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# BCM numbering
GPIO.setmode(GPIO.BCM)

# setting row pins
ROW_1 = 18
ROW_2 = 23
ROW_3 = 24
ROW_4 = 25
# setting column pins
COL_1 = 12
COL_2 = 16
COL_3 = 20
COL_4 = 21

# clock pins
clk1 = 10  # left most DFF
GPIO.setup(clk1, GPIO.OUT, initial=GPIO.LOW)

# Define the pin numbers for the segments of the 7-segment display
segments = [2, 3, 27, 22, 5, 6, 13, 26]  # data pins from DFF

# from instructions: GPIO pins connected to the 'X' lines will be setup as inputs to the pad/output from the PI
GPIO.setup(ROW_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROW_4, GPIO.OUT, initial=GPIO.LOW)

# from instructions: pins connected to the 'Y' lines will be setup as outputs from the pad/inputs to the PI
# if needed set low by default: pull_up_down=GPIO.PUD_DOWN
GPIO.setup(COL_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(COL_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)  # A
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)  # B
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)  # C
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)  # D
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)  # E
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)  # F
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)  # G
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)  # Dp

# Global variables
last_displayed_number = -1
display_state = 1  # 1 for ON, 0 for OFF


# function to toggle on and off clock
def toggleClock():
    # Read the current state of the pin
    current_state = GPIO.input(clk1)
    # Toggle the pin state
    new_state = GPIO.LOW if current_state == GPIO.HIGH else GPIO.HIGH
    GPIO.output(clk1, new_state)


# function to call specific segments and make GPIO HIGH
def reset():
    GPIO.output(22, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)


# function to interpret which button was pressed
def readKeypad(rowNum, char):
    global last_displayed_number
    global display_state

    def hashtag():
        global last_displayed_number
        global display_state

        print("#")
        if (
            GPIO.output(27, GPIO.LOW)
            and GPIO.output(22, GPIO.LOW)
            and GPIO.output(13, GPIO.LOW)
            and GPIO.output(2, GPIO.LOW)
            and GPIO.output(5, GPIO.LOW)
            and GPIO.output(6, GPIO.LOW)
            and GPIO.output(26, GPIO.LOW)
            and GPIO.output(3, GPIO.LOW)
        ):
            print("dog")
            if display_state == 1:  # Display is ON
                if last_displayed_number != -1:
                    display_number(last_displayed_number)
            else:
                reset()
        else:
            reset()

    def zero():        
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        state=0
        
    def one():
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=1
    
    def two():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=2
    
    def three():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=3
    
    def four():
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=4
    
    def five():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=5
        
    def six():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=6
        
    def seven():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=7
        
    def eight():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=8
    
    def nine():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        state=9
    
    def star():
        GPIO.output(26, GPIO.HIGH)
        state=10
        
    def a():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        state=11
        check="a"
    
    def b():
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=12
        check="b"
    def c():
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        state=13
        check="*"
    def d():
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        
        state=14
        check="*"

    display = -1
    GPIO.setmode(GPIO.BCM)
    GPIO.output(rowNum, GPIO.HIGH)
    ##################################################
    if GPIO.input(COL_1) == 1:
        # col_1 is 12
        if rowNum == 18:
            print("1")
            reset()
            display_number(1)
            last_displayed_number = 1
         if rowNum==23:
            print("4")
            reset()
            display_number(4)
            last_displayed_number = 4
        if rowNum==24:
            print("7")
            reset()
            display_number(7)
            last_displayed_number = 7
        if rowNum==25:
            print("*")
            reset()
            display_number(10)
            last_displayed_number = 10

    if GPIO.input(COL_2) == 1:
        # col_1 is 16
        if rowNum == 18:
            print("2")
            reset()
            display_number(2)
            last_displayed_number = 2
        if rowNum==23:
            print("5")
            reset()
            display_number(5)
            last_displayed_number = 5
        if rowNum==24:
            print("8")
            reset()
            display_number(8)
            last_displayed_number = 8
        if rowNum==25:
            print("0")
            reset()
            display_number(0)
            last_displayed_number = 0

    if GPIO.input(COL_3) == 1:
        # col_1 is 20
        if rowNum == 18:
            print("3")
            reset()
            display_number(3)
            last_displayed_number = 3
        if rowNum==23:
            print("6")
            reset()
            display_number(6)
            last_displayed_number = 6
        if rowNum==24:
            print("9")
            reset()
            display_number(9)
            last_displayed_number = 9
        if rowNum==25:
            print("#")
            hashtag()
            

    if GPIO.input(COL_4) == 1:
        # col_1 is 21
        if rowNum == 18:
            print("A")
            reset()
            display_number(11)  # For the '*' character
            last_displayed_number = 11
        if rowNum==23:
            print("B")
            reset()
            display_number(12)  # For the '*' character
            last_displayed_number = 12
            
        if rowNum==24:
            print("C")
            reset()
            display_number(13)  # For the '*' character
            last_displayed_number = 13
            
        if rowNum==25:
            print("D")
            reset()
            display_number(14)  # For the '*' character
            last_displayed_number = 14

    GPIO.output(rowNum, GPIO.LOW)


# Function to light up segments for a given number
def display_number(number):
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

try:
    while True:
        readKeypad(ROW_1, ["1", "4", "7", "*"])
        readKeypad(ROW_2, ["2", "5", "8", "0"])
        readKeypad(ROW_3, ["3", "6", "9", "#"])
        readKeypad(ROW_4, ["A", "B", "C", "D"])
        time.sleep(0.2)

        toggleClock()

except KeyboardInterrupt:
    print("\nKeypad Application Interrupted")
    GPIO.cleanup()
