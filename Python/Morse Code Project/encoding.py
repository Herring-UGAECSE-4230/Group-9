<<<<<<< HEAD
# MC Encoder - Group 9 
import RPi.GPIO
from time import sleep
import simpleaudio
import numpy

=======
import RPi.GPIO as GPIO
from time import sleep
import simpleaudio as sa
import numpy as np

# Initialize GPIO pins
led_pin = 16  # Assuming the LED is connected to GPIO pin 18
speaker_pin = 27  # Assuming the speaker is connected to GPIO pin 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(speaker_pin, GPIO.OUT)

# Define Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' ',  # space character
    'OVER': ' - - -   .   - . - .   - - - ',  # Separator for "over"
    'OUT': '. - . - .   | '  # Separator for "out"
}

# Function to play audio at a specific frequency
def play_audio(frequency, duration):
    Fs = 44100  # Sampling frequency
    t = np.linspace(0, duration, int(duration * Fs), False)  # Generate time array
    note = np.sin(frequency * t * 2 * np.pi)  # Create sine wave
    audio = note * (2**15 - 1) / np.max(np.abs(note))  # Normalize audio
    audio = audio.astype(np.int16)  # Convert to 16-bit format
    play_obj = sa.play_buffer(audio, 1, 2, Fs)  # Play audio
    play_obj.wait_done()  # Wait for audio to finish playing

# Function to encode text into Morse code
def encode_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            morse_code += "/ "  # Placeholder for unknown characters
    return morse_code

# Function to display Morse code using LED and speaker
def display_morse_code(morse_code, unit_length):
    for symbol in morse_code.split():
        if symbol == '.':
            GPIO.output(led_pin, GPIO.HIGH)
            play_audio(500, unit_length)
            GPIO.output(led_pin, GPIO.LOW)
            sleep(unit_length)
        elif symbol == '-':
            GPIO.output(led_pin, GPIO.HIGH)
            play_audio(500, 3 * unit_length)
            GPIO.output(led_pin, GPIO.LOW)
            sleep(unit_length)
        elif symbol == '|':
            sleep(2 * unit_length)  # Pause for separators
        elif symbol == '/':
            sleep(4 * unit_length)  # Pause for unknown characters

# Main function
def main():
    messages = [
        "ATTENTION", "THIS", "IS", "A", "TEST",
        "CONSIDERED", "SECOND", "MESSAGE"
    ]
    unit_length = float(input("Enter the unit length (in seconds): "))

    # Encode each message to Morse code and display using LED and speaker
    for message in messages:
        morse_code = encode_to_morse(message)
        display_morse_code(morse_code, unit_length)
        print("over")  # Indicate end of message

    # End transmission
    print("out")

if __name__ == "__main__":
    try:
        main()
    finally:
        GPIO.cleanup()  # Clean up GPIO pins on exit
>>>>>>> 85126b96ff93ac0f1979fbe10f3c9cd9f9f9bdff
