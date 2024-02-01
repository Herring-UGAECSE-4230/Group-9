import pigpio

pi = pigpio.pi()           

freq = 5 # sets frequency variable 
pi.set_PWM_frequency(23, freq) # set GPIO 23 
pi.set_PWM_dutycycle(23, 128) # PWM 1/2 on aka duty cycle=  %50 
print(f"{freq}")

while True: 
    # empty loop that keeps program running while the LED is blinking.
    pass
