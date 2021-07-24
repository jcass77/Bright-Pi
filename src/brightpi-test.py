#!/usr/bin/python3
# Demo code showing main and subclass and various methods invocation

import brightpi
import time

brightPi = brightpi.BrightPi()
brightSpecial = brightpi.BrightPiSpecialEffects()

leds = (1, 3)
brightSpecial.reset()

brightSpecial.set_led_on_off(leds, brightpi.ON)
time.sleep(2)
print(brightSpecial)

time.sleep(2)

brightSpecial.set_led_on_off(brightpi.LED_WHITE, brightpi.OFF)
brightSpecial.set_led_on_off(brightpi.LED_IR, brightpi.ON)
brightSpecial.set_gain(9)
print(brightSpecial)
time.sleep(2)

brightSpecial.set_led_on_off(brightpi.LED1, brightpi.ON)
print(brightSpecial)

time.sleep(2)

brightSpecial.set_gain(2)
brightSpecial.set_led_on_off(brightpi.LED3, brightpi.ON)
brightSpecial.set_led_dim(brightpi.LED3, 10)
print(brightSpecial)

time.sleep(2)

brightSpecial.set_led_on_off((1,), 0)
time.sleep(1)
brightSpecial.set_led_on_off((1,), 1)
time.sleep(1)
brightSpecial.set_led_on_off((1, 2, 3, 4), 1)
time.sleep(1)
brightSpecial.set_led_on_off((1, 2, 3, 4), 0)
time.sleep(1)
brightSpecial.set_led_on_off((1, 2, 3, 4), 1)
brightSpecial.beacon(2, 0.1)
print(brightSpecial)
brightSpecial.reset()

brightSpecial.set_gain(8)
print(brightSpecial)
brightSpecial.night_rider(10, 0.1)
brightSpecial.night_rider(10, 0.1, 1)
brightSpecial.dimmer(2, 0.2)
print(brightSpecial)
brightSpecial.reset()
brightSpecial.flash(5, 1)
brightSpecial.alt_flash(5, 0.2)
brightSpecial.alt_flash(5, 0.2, "h")
brightSpecial.alt_flash(5, 0.2, "x")

brightPi.reset()

brightPi.set_led_on_off(leds, brightpi.ON)

leds = brightpi.LED_IR
brightPi.set_led_on_off(leds, brightpi.OFF)
print(brightPi)
time.sleep(1)

leds = brightpi.LED_WHITE
brightPi.set_led_on_off(leds, brightpi.ON)
print(brightPi)
time.sleep(1)

leds = brightpi.LED_WHITE
brightPi.set_led_on_off(leds, brightpi.OFF)
print(brightPi)
time.sleep(1)

leds = brightpi.LED2
brightPi.set_led_on_off(leds, brightpi.ON)
print(brightPi)
time.sleep(1)

leds = [1, 2, 3, 4, 5, 6, 7, 8]
brightPi.set_led_on_off(leds, brightpi.OFF)
print(brightPi)

for led in range(0, 8):
    brightPi.set_led_on_off((led + 1,), brightpi.ON)
    print(brightPi)
    time.sleep(1)

leds = [1, 2, 3, 4, 5, 6, 7, 8]
brightPi.set_led_on_off(leds, brightpi.OFF)
print(brightPi)
