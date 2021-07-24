#!/usr/bin/python3
# Turn on all LEDs and set brightness to max.

from brightpi.brightpilib import BrightPi, LED_ALL, ON

brightPi = BrightPi()

print(f"Setting gain to max ({BrightPi._max_gain})...")
brightPi.set_gain(BrightPi._max_gain)

print("Turning LEDs on...")
brightPi.set_led_on_off(LED_ALL, ON)

print(f"Setting LED's to max brightness ({BrightPi._max_dim})...")
brightPi.set_led_dim(LED_ALL, BrightPi._max_dim)
