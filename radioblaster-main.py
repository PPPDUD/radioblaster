# Imports go at the top
from microbit import *
import radio, time
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    prev_time = time.ticks_ms()
    for i in range(255):
        for j in range(83):
            radio.config(group=i, channel=j, power=7)

            for k in range(4):
                #print("Dangerous ping #" + str(k + 1), "at", str(i) + "," + str(j))
                radio.send_bytes(bytes([5,5,53,4,4]))

    print("[DEBUG] Completed one round of blasting in", str(time.ticks_diff(time.ticks_ms(), prev_time)/1000), "seconds.")
