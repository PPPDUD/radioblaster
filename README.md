# radioblaster
Radio Blaster is a radio-based worm targeting MicroPython IoT devices with the micro:bit hardware. It works by sending malformed strings to nearby micro:bits. Whenever a micro:bit attempts to decode the malformed string, an error occurs and the micro:bit crashes. This makes it possible to stealthily defeat spy devices and security systems without ever touching the target mico:bit.

# Installation
Simply download the supplied Radio Blaster hex file from the Releases tab and put it on your micro:bit. It will automactially start crashing vulnerable micro:bits in around 45 seconds. If the micro:bits return, they will be attacked again and again.

For an example of a vulnerable piece of software, see vuln-software.hex in the Releases tab.

# Prevention
Always wrap any usages of `radio.receive()` in a try-except statement to ensure that your micro:bit will not crash if it is attacked by Radio Blaster.
