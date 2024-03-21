import RPi.GPIO as GPIO
from time import sleep
import simpleaudio as sa
import numpy as np

GPIO.setmode(GPIO.BCM)
LED_PIN = 16
SPEAKER_PIN = 27
GPIO.setup([LED_PIN, SPEAKER_PIN], GPIO.OUT)

morse_code_dict = {'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ',
                   'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ', 'j': '.--- ',
                   'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ',
                   'p': '.--. ', 'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ',
                   'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ', 'y': '-.-- ',
                   'z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
                   '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
                   '9': '----. '}

# def open_read(file_name):
#     global lines
#     with open(file_name) as file:
#         lines = [line for line in file.readlines()]


def write_file(character, morse_code_dict, output_file):
    if character.lower() in morse_code_dict:
        morse_code = morse_code_dict[character.lower()]
        with open(output_file, 'a') as file:
            pass
    else:
        with open(output_file, 'a') as file:
            pass

def encode_to_morse(input_txt, output_file):
    with open(output_file, 'w') as file:
        pass
    
    # splits input text 
    words = input_txt.split()

    for word in words: 
        for char in word: 
            write_file(char, morse_code_dict, output_file)
        with open(output_file, 'a') as file:
            file.write('\n')
    
    # for char in input_txt:
    #     if char != ' ':
    #         write_file(char, morse_code_dict, output_file)
    #     else:
    #         with open(output_file, 'a') as file:
    #             file.write('    | space\n')

    # for char in input_txt.lower():
    #     if char in morse_code_dict:
    #         morse_code = morse_code_dict[char]
    #         with open(output_file, 'a') as file:
    #             file.write(morse_code + ' | ' + char + '\n')
    with open(filename, inputfile):
        lines = [line.rstrip() for line in file.readlines()]
    f = open(filename, 'w')

    word_morse = ' '.join([morse_code_dict[char] for char in input_txt.lower() if char in morse_code_dict])
    
    with open(output_file, 'a') as file:
        file.write(word_morse + ' | ' + input_txt.lower() + '\n')

input_text = "Hello World"
output_file = "morse.txt"

encode_to_morse(input_text, output_file)
#try:
# file_name = input("Enter what file to open: ")
    # open_read(message.txt)
    #write_file("message.txt",character, morse_code_dict, "morse.txt")
    
    
# except KeyboardInterrupt:
#     GPIO.cleanup()