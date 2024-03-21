from time import sleep
import RPi.GPIO as GPIO
import simpleaudio as sa
import numpy as np

# Setup GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 16
SPEAKER_PIN = 27
#unit_length = float(input('Enter the desired unit length in seconds: '))
GPIO.setup([LED_PIN, SPEAKER_PIN], GPIO.OUT)

# Morse code translations
morse_code_dict = {'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ',
                   'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ', 'j': '.--- ',
                   'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ',
                   'p': '.--. ', 'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ',
                   'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ', 'y': '-.-- ',
                   'z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
                   '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
                   '9': '----. '}

# Translate character to Morse code
def translate(char):
    return morse_code_dict.get(char.lower(), ' ')

# Translate word to Morse code
def word_to_morse(word):
    if word.lower() == 'attention':
        return '-.-.-'
    if word.lower() == 'over':
        return '-.-'
    if word.lower() == 'out':
        return '.-.-.'
    return ''.join(translate(i) for i in word)

# Write Morse code output to file
def write_morse_code(filename, input_file):
    with open(input_file) as file:
        lines = [line.rstrip() for line in file.readlines()]
    with open(filename, 'w') as f:
        f.write(word_to_morse('attention') + '| ' + 'attention' + '\n') 
        for line in lines:
            line = line.split(' ')
            for i, word in enumerate(line):
                f.write(('       ' if i > 0 else '') + word_to_morse(word) + '| ' + word + '\n')
            f.write(word_to_morse('over') + '| ' + 'over' + '\n')
        f.write(word_to_morse('out') + '| ' + 'out' + '\n')

# Output Morse code to LED and speaker
def output_morse_code(filename):
    with open(filename) as file:
        lines = [line.rstrip().split('|')[0].strip() for line in file.readlines()]
    for line in lines:
        for ch in line:
            if ch == '-':
                beep(0.5 * unit_length)
            elif ch == '.':
                beep(0.25 * unit_length)
            else:
                sleep(0.25 * unit_length)

# Beep function for audio and LED
def beep(duration):
    GPIO.output([LED_PIN, SPEAKER_PIN], 1)
    play_audio(500, duration)
    GPIO.output([LED_PIN, SPEAKER_PIN], 0)
    sleep(0.5 * unit_length)

# Play audio at a specific frequency
def play_audio(frequency, duration):
    Fs = 44100  # Sampling frequency
    t = np.linspace(0, duration, int(duration * Fs), False)  # Generate time array
    note = np.sin(frequency * t * 2 * np.pi)  # Create sine wave
    audio = note * (2**15 - 1) / np.max(np.abs(note))  # Normalize audio
    audio = audio.astype(np.int16)  # Convert to 16-bit format
    play_obj = sa.play_buffer(audio, 1, 2, Fs)  # Play audio
    play_obj.wait_done()  # Wait for audio to finish playing

# Main loop
try:
    while True:
        file_name = input('Enter a file to decode: ')
        write_morse_code('message.txt', file_name)
        output_morse_code('message.txt')
except KeyboardInterrupt:
    GPIO.cleanup()
