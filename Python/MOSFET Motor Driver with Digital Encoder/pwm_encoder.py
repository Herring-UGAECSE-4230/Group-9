import RPi.GPIO


# encoder gpio pins 
SW_pin = 5
DT_pin = 6
CLK_pin = 13

# gpio setup
GPIO.setup(SW_pin, GPIO.OUT)
GPIO.setup(CLK_pin, GPIO.IN, pull_up_down  GPIO.PUD_UP)