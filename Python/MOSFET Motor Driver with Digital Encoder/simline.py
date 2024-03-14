import RPi.GPIO as GPIO

# GPIO pin setup
CLK_PIN = 13
DT_PIN = 6
SW_PIN = 5

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize variables
last_clk_state = GPIO.input(CLK_PIN)
last_dt_state = GPIO.input(DT_PIN)
debounce_counter = 0
debounce_threshold = 3  # Adjust as needed

# Define callback functions
def clockwise_callback():
    print("Clockwise")

def counterclockwise_callback():
    print("Counterclockwise")

# Main loop
try:
    while True:
        # Read current state of CLK and DT pins
        clk_state = GPIO.input(CLK_PIN)
        dt_state = GPIO.input(DT_PIN)
        
        # Check for stable state changes
        if clk_state != last_clk_state or dt_state != last_dt_state:
            debounce_counter += 1
        else:
            debounce_counter = 0
        
        # If stable state change detected
        if debounce_counter >= debounce_threshold:
            # Determine direction of rotation
            if clk_state != dt_state:
                clockwise_callback()
            else:
                counterclockwise_callback()
            
            # Reset debounce counter
            debounce_counter = 0
        
        # Update last states
        last_clk_state = clk_state
        last_dt_state = dt_state

except KeyboardInterrupt:
    GPIO.cleanup()
