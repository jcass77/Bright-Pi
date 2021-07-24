#!/usr/bin/python3
# Reset BrightPi to default and turn off all LEDs
import time

from brightpi.brightpilib import BrightPi, LED_ALL, OFF

brightPi = BrightPi()

if brightPi.set_led_on_off(LED_ALL, OFF):
    print("BrightPi is already switched off! Skipping...")

print("Dimming LED's...")
dim = BrightPi._max_dim
while dim > 0x00:
    dim -= 1
    brightPi.set_led_dim(LED_ALL, dim)
    time.sleep(0.1)

brightPi.set_led_on_off(LED_ALL, OFF)

print("Resetting BrightPi...")
brightPi.reset()

print("BrightPi has been turned off!")
