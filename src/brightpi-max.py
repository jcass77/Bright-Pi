#!/usr/bin/python3
# Turn on all LEDs and set brightness to max.
import time

from brightpi.brightpilib import BrightPi, LED_ALL, ON

brightPi = BrightPi()

if (
    brightPi.get_gain() == BrightPi._max_gain
    and all(state == ON for state in brightPi.get_led_on_off(LED_ALL))
    and all(dim == BrightPi._max_dim for dim in brightPi.get_led_dim())
):
    print("BrightPi is already at max! Skipping...")

brightPi.set_gain(BrightPi._max_gain)

brightPi.set_led_dim(LED_ALL, 0x00)  # Lowest brightness setting
brightPi.set_led_on_off(LED_ALL, ON)  # Turn LED's on

print(f"Setting LED's to max brightness ({BrightPi._max_dim})...")
dim = 0x00
while dim < BrightPi._max_dim:
    dim += 1
    brightPi.set_led_dim(LED_ALL, dim)
    time.sleep(0.1)

print("BrightPi is at max!")
