import RPi.GPIO as GPIO
import pigpio
from time import sleep
import simpleaudio as sa
import numpy as np

GPIO.setmode(GPIO.BCM)
LED_PIN = 16
SPEAKER_PIN = 27
GPIO.setup([LED_PIN, SPEAKER_PIN], GPIO.OUT)
global counter
counter = 0

morse_code_dict = {'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ',
                   'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ', 'j': '.--- ',
                   'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ',
                   'p': '.--. ', 'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ',
                   'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ', 'y': '-.-- ',
                   'z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
                   '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
                   '9': '----. '}

def write_morse_code(char, morse_code_dict, output_file):
    with open(output_file, 'a') as file:
        if char.lower() in morse_code_dict:
            file.write(morse_code_dict[char.lower()])
            var= morse_code_dict[char.lower()]
            for dot_dash in var:
                LED_flash(dot_dash)
        else:
            file.write('\n' + char)

def LED_flash(char):
    if char == "-":
        print("-")
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        sleep(1)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)

        
    if char == ".":
        print(".")
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        sleep(.15)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        print()
        
    else:
        sleep(.5)
        print("Space")
        GPIO.output(16, GPIO.LOW)

def encode_to_morse(input_file, output_file):
    global counter
    with open(output_file, 'w') as file:
        pass
    
    with open(output_file, 'a') as file:
        file.write('-.-.- | attention\n')

    with open(input_file, 'r') as infile:
        for line in infile:
            words = line.split()
            if counter > 0:
                with open(output_file, 'a') as file:
                    file.write('- . - | over\n')
            for word in words:
                for char in word:
                    write_morse_code(char, morse_code_dict, output_file)
                with open(output_file, 'a') as file:
                    file.write('| ' + word + '\n')
            counter += 1
    with open(output_file, 'a') as file:
        file.write('-.- | over\n')
        file.write('-.-.-. | out\n')


                    

encode_to_morse("message.txt", "morse.txt")