import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for the LED
led_pin = 4
GPIO.setup(led_pin, GPIO.OUT)

# Set up PWM on the LED pin with a default frequency of 100 Hz
pwm_led = GPIO.PWM(led_pin, 100)
pwm_led.start(0)  # Start with 0% duty cycle (LED off)

while True:
        # Get user input for PWM and duty cycle
        pwm_value = int(input("Enter PWM value (0-100): "))
        duty_cycle = int(input("Enter duty cycle (0-100): "))

        # Validate input values
        pwm_value = max(0, min(pwm_value, 100))
        duty_cycle = max(0, min(duty_cycle, 100))

        # Set PWM and duty cycle
        pwm_led.ChangeFrequency(pwm_value)
        pwm_led.ChangeDutyCycle(duty_cycle)

        # Blink the LED
        time.sleep(.5)  # Blink duration

# 1oClean up GPIO on keyboard interrupt
pwm_led.stop()
GPIO.cleanup()