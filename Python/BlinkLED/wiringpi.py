import wiringpi 


wiringpi.wiringPiSetupGpio() # calls the GPIO pins by their GPIO pin number
wiringpi.softToneCreate(23) # using GPIO Pin # 23 


freq = 20 


while True: 
    wiringpi.softToneWrite(23, freq) # sets desired freq 
    wiringpi.delay(10) # delays for 0.2 seconds 

    pass 
