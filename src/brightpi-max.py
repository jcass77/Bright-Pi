#!/usr/bin/python3
# Turn on all LEDs and set brightness to max.
import time

from brightpi.brightpilib import BrightPi, LED_ALL, LED_IR, LED_WHITE, ON

brightPi = BrightPi()

print(f"Setting gain to max ({BrightPi._max_gain})...")
brightPi.set_gain(BrightPi._max_gain)

brightPi.set_led_dim(LED_ALL, 0x00)  # Lowest brightness setting

print("Turning on LED's...")
brightPi.set_led_on_off(LED_IR, ON)
for led in LED_WHITE:
    brightPi.set_led_on_off((led,), ON)
    time.sleep(0.5)

print(f"Setting LED's to max brightness ({BrightPi._max_dim})...")
dim = 0x00
while dim < BrightPi._max_dim:
    dim += 1
    brightPi.set_led_dim(LED_ALL, dim)
    time.sleep(0.1)

print("BrightPi is at max!")
