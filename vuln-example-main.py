# Imports go at the top
from microbit import *
import radio
radio.config(group=50, channel=70)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    message = radio.receive()

    if message:
        print(message)
