import RPi.GPIO as GPIO
from time import sleep

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the pin numbers for the segments of the 7-segment display
segments = [11, 12, 13, 15, 16, 18, 22] #data pins from DFF

#Define the clock pins
clock_1 = [10] # operating only left-most segment currently (reading from left to right)

# Define the pin numbers for the keypad rows and columns
keypad_rows = [18, 23, 24, 25] #X1-X4
keypad_cols = [12, 16, 20, 21] #Y1-Y4

# Set up GPIO pins for segments
for segment_pin in segments:
    GPIO.setup(segment_pin, GPIO.OUT)
    GPIO.output(segment_pin, GPIO.LOW)

# Set up GPIO pins for keypad rows and columns
for row_pin in keypad_rows:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for col_pin in keypad_cols:
    GPIO.setup(col_pin, GPIO.OUT)
    GPIO.output(col_pin, GPIO.HIGH)

# Define the mapping of keypad buttons to numbers
keypad_mapping = {
    (0, 0): 1, (0, 1): 2, (0, 2): 3, (0, 3): "A",
    (1, 0): 4, (1, 1): 5, (1, 2): 6, (1, 3): "B",
    (2, 0): 7, (2, 1): 8, (2, 2): 9, (2, 3): "C",
    (3, 0): "*", (3, 1): 0, (3, 2): "#", (3, 3): "D"
}

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
        10: [0, 0, 0, 0, 0, 0, 0, 1]
    }
    
    # Turn on/off the segments based on the number
    for i, segment_pin in enumerate(segments):
        GPIO.output(segment_pin, numbers[number][i])

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

clk_status = GPIO.output(clock_1, GPIO.LOW)
def running_clk():
    while True:
        clk_status = GPIO.output(clock_1, GPIO.LOW)
        time.sleep(1) #1 second
        clk_status = GPIO.output(clock_1, GPIO.HIGH)
        time.sleep(1) #1 second

# Main loop
try:
    while True:
        key = get_key()
        status = GPIO.output(clock_1, GPIO.HIGH)
        if running_clk() == status and key:
            print("Pressed:", key)
            # Display the pressed key on the SSD
            display_number(key)
        else:
            # Turn off the SSD if no key is pressed
            display_number("*")
        sleep(0.1)  # Add a small delay to avoid excessive polling

finally:
    GPIO.cleanup()  # Clean up GPIO on exit
