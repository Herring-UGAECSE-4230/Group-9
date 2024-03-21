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

def write_morse_code(char, morse_code_dict, output_file):
    #morse_list = []
    #word_list = []
    #count = 0
    with open(output_file, 'a') as file:
        if char.lower() in morse_code_dict:
            #morse_list.append(morse_code_dict[char.lower()])
            #count += 1
            #file.write(morse_code_dict[char.lower()] + ' | ' + char.lower() + '\n')
            #for char in len(word):
            file.write(morse_code_dict[char.lower()])
            #print("loop")
        else:
            #file.write('unknown char: ' + char + '\n')
            file.write('\n' + char)

def encode_to_morse(input_file, output_file):
    with open(output_file, 'w') as file:
        pass

    with open(input_file, 'r') as infile:
        for line in infile:
            #print(line)
            words = line.split()
            #for word in line.split():
            print(words)
            for word in words:
                #print(word)
                #for char in line.strip():
                for char in word:
                    #if char != ' ':
                    #    write_morse_code(char, morse_code_dict, output_file)
                    #else:
                    #    with open(output_file, 'a') as file:
                    #file.write('\n')
                    write_morse_code(char, morse_code_dict, output_file)
                with open(output_file, 'a') as file:
                    file.write('| ' + word + '\n')
                

            #with open(output_file, 'a') as file:
                #file.write('|' + line.strip() + '\n')
                #file.write('| ' + word + '\n')
                    

encode_to_morse("message.txt", "morse.txt")


#try:
# file_name = input("Enter what file to open: ")
    # open_read(message.txt)
    #write_file("message.txt",character, morse_code_dict, "morse.txt")
    
    
# except KeyboardInterrupt:
#     GPIO.cleanup()