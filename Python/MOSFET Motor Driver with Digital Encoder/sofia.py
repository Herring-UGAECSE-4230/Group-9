import RPi.GPIO as GPIO
import time
from time import sleep
import threading

#IR sensor initialization
IR_pin = 21
measured_RPM = 0
set_RPM = 1000

#Rotary Encoder initialization
clk=13
dt=6
sw=5

#motor initialization
# motor_pin = 26

#GPIO set up
GPIO.setmode(GPIO.BCM)

#for IR sensor
GPIO.setup(IR_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#for encoder
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#for motor
GPIO.setup(26, GPIO.OUT)
motor = GPIO.PWM(26,50)
motor.ChangeFrequency(500)
motor.start(50)

#other variable initialization
counter = 0
motor_on = True
duty_cycle = 10
totalTurns = 0
lastClkState=GPIO.input(clk)
currentTime= time.time()
debounce_scale = 1
turn_momentum = 0



def IR_detection():
    global currentTime, measured_RPM, set_RPM, motor, duty_cycle
    GPIO.setmode(GPIO.BCM)
    last_value = 0
    while True:
        cycle_read = 0
        while time.time() - currentTime < .4:
            if last_value == 1 and GPIO.input(IR_pin) == 0:
                last_value = 0
                cycle_read += 1
            last_value = GPIO.input(IR_pin)
        measured_RPM = (60*cycle_read)/(3*.4)
        currentTime= time.time()

thread = threading.Thread(target=IR_detection)
thread.start()
GPIO.add_event_detect(IR_pin, GPIO.RISING, callback=IR_detection)


try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if set_RPM >= measured_RPM and duty_cycle + .00001*(set_RPM - measured_RPM) < 100:
            duty_cycle += .00001(set_RPM - measured_RPM)
            try:
                pass
            finally:
                pass
        else:
            if duty_cycle + .00001*(set_RPM - measured_RPM) > 0:
                duty_cycle += .00001*(set_RPM - measured_RPM)
                try:
                    pass
                finally:
                    pass
        if clkState!=lastClkState:
            is_Turning = True
            if dtState!=clkState:
                if turn_momentum > 0:
                    counter+= 1
                    set_RPM += 25
                    totalTurns += 1
            else:
                if turn_momentum < 0:
                    counter -= 1
                    set_RPM -= 25
                    totalTrusn += 1
                if turn_momentum != -(debounce_scale):
                    turn_momentum -= 1
        print("Measured RPM: " + str(measured_RPM)[:6] + " | Set RPM: " + str(set_RPM) + " "*10, end="\r")
finally:
    motor.stop()
    GPIO.cleanup()

