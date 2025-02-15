#!/usr/bin/python3
# Turn on all LEDs and set brightness to max.
import time

from brightpi.brightpilib import BrightPi, LED_ALL, ON, OFF

brightPi = BrightPi()

if (
    brightPi.get_gain() == BrightPi._max_gain
    and all(state != OFF for state in brightPi.get_led_on_off(LED_ALL))
    and all(dim == BrightPi._max_dim for dim in brightPi.get_led_dim())
):
    print("BrightPi is already at max! Skipping...")

else:
    brightPi.set_gain(BrightPi._max_gain)

    brightPi.set_led_dim(LED_ALL, 0x00)  # Lowest brightness setting
    brightPi.set_led_on_off(LED_ALL, ON)  # Turn LED's on

    print(f"Setting LED's to max brightness ({BrightPi._max_dim})...")
    dim = 0x00 + 1
    while dim <= BrightPi._max_dim:
        brightPi.set_led_dim(LED_ALL, dim)
        dim += 1
        time.sleep(0.05)

    print("BrightPi is at max!")
