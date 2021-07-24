#!/usr/bin/python3
# Reset BrightPi to default and turn off all LEDs

from brightpi.brightpilib import BrightPi, LED_ALL, OFF

brightPi = BrightPi()

brightPi.reset()
brightPi.set_led_on_off(LED_ALL, OFF)
