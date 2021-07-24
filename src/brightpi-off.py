#!/usr/bin/python3
# Reset BrightPi to default and turn off all LEDs
import time

from brightpi.brightpilib import BrightPi, LED_ALL

brightPi = BrightPi()

print(f"Dimming LED's...")
dim = BrightPi._max_dim
while dim > 0x00:
    dim -= 1
    brightPi.set_led_dim(LED_ALL, dim)
    time.sleep(0.1)

print("Resetting BrightPi...")
brightPi.reset()

print("BrightPi has been turned off!")
