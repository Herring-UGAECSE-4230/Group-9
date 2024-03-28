#TESTING DECODER
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

l_to_m = {'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ',
          'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ', 'j': '.--- ',
          'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ',
          'p': '.--. ', 'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ',
          'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ', 'y': '-.-- ',
          'z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
          '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
          '9': '----. '}

m_to_l = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
          '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
          '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
          '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
          '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
          '--..': 'z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
          '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
          '----.': '9'}

#GPIO Setup
GPIO.setmode(GPIO.BCM)
key_pin = 12 #pin to telegraph
GPIO.setup(key_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.input(key_pin, key_pin)
    start_time = time()
    GPIO.edge_wait(key_pin, GPIO.RISING)
    end_time = time()
    duration = end_time - start_time

    if duration < 0.3:
        morse += '.'
    elif:
        morse += '-'
    else:
        morse += ' '

try:
    morse_detect()
except KeyboardInterrupt:
    GPIO.cleanup()

