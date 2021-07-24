#!/usr/bin/python3
# Reset BrightPi to default and turn off all LEDs
import time

from brightpi.brightpilib import BrightPi, LED_ALL, ON, OFF

brightPi = BrightPi()

if all(state == OFF for state in brightPi.get_led_on_off(LED_ALL)):
    print("BrightPi is already switched off! Skipping...")
else:
    print("Dimming LED's...")
    dim = BrightPi._max_dim - 1
    while dim >= 0x00:
        brightPi.set_led_dim(LED_ALL, dim)
        dim -= 1
        time.sleep(0.05)

    brightPi.set_led_on_off(LED_ALL, OFF)

    print("Resetting BrightPi...")
    brightPi.reset()

    print("BrightPi has been turned off!")
