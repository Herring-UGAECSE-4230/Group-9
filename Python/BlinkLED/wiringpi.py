import wiringpi


wiringpi.wiringPiSetupGpio() # calls the GPIO pins by their GPIO pin number
wiringpi.softToneCreate(23) # using GPIO Pin # 23 


freq = 20 # variable to set frequency 
wiringpi.softToneWrite(23, freq) # sets desired freq 

while True:
    # creates an empty loop to keep the program running while the LED is blinking
    pass 
