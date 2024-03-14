import RPi.GPIO as GPIO

# GPIO pin setup
clk = 13
dt = 6
sw = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw, GPIO.IN)

# Initialize the counter and the encoder turn
counter = 0
lastClkState = GPIO.input(clk)

# Debounce parameters
debounce_delay = 5  # Debounce delay in milliseconds
state = 0  # State variable for debounce state machine

while True:
    time.sleep(.3)
    # Check states of the pins
    clkState = GPIO.input(clk)
    dtState = GPIO.input(dt)

    # Debounce state machine
    if state == 0:
        if clkState != lastClkState:
            state = 1
            debounce_time = debounce_delay
    elif state == 1:
        if clkState == lastClkState:
            state = 0
        else:
            debounce_time -= 1
            if debounce_time == 0:
                if dtState != clkState:
                    print("Clockwise")
                    counter += 1
                else:
                    print("Counterclockwise")
                    counter -= 1
                print("Counter:", counter)
                state = 0

    lastClkState = clkState  # Update last clk state
