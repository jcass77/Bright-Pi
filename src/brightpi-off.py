#!/usr/bin/python3
# Reset BrightPi to default and turn off all LEDs
import time

from brightpi.brightpilib import BrightPi, LED_IR, LED_WHITE, OFF

brightPi = BrightPi()

print("Turning off LED's...")
brightPi.set_led_on_off(LED_IR, OFF)
for led in LED_WHITE:
    brightPi.set_led_on_off((led,), OFF)
    time.sleep(0.5)

print("Resetting BrightPi...")
brightPi.reset()

print("BrightPi has been turned off!")
