#!/usr/bin/python3
# Demo code showing main and subclass and various methods invocation

from brightpi.brightpilib import (
    BrightPi,
    BrightPiSpecialEffects,
    ON,
    OFF,
    LED_IR,
    LED_WHITE,
    LED1,
    LED2,
    LED3,
)
import time

brightPi = BrightPi()
brightSpecial = BrightPiSpecialEffects()

leds = (1, 3)
brightSpecial.reset()

brightSpecial.set_led_on_off(leds, ON)
time.sleep(2)
print(brightSpecial)

time.sleep(2)

brightSpecial.set_led_on_off(LED_WHITE, OFF)
brightSpecial.set_led_on_off(LED_IR, ON)
brightSpecial.set_gain(9)
print(brightSpecial)
time.sleep(2)

brightSpecial.set_led_on_off(LED1, ON)
print(brightSpecial)

time.sleep(2)

brightSpecial.set_gain(2)
brightSpecial.set_led_on_off(LED3, ON)
brightSpecial.set_led_dim(LED3, 10)
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

brightSpecial.reset()

brightSpecial.set_led_on_off(leds, ON)

leds = LED_IR
brightSpecial.set_led_on_off(leds, OFF)
print(brightPi)
time.sleep(1)

leds = LED_WHITE
brightSpecial.set_led_on_off(leds, ON)
print(brightPi)
time.sleep(1)

leds = LED_WHITE
brightSpecial.set_led_on_off(leds, OFF)
print(brightPi)
time.sleep(1)

leds = LED2
brightSpecial.set_led_on_off(leds, ON)
print(brightPi)
time.sleep(1)

leds = [1, 2, 3, 4, 5, 6, 7, 8]
brightSpecial.set_led_on_off(leds, OFF)
print(brightPi)

for led in range(0, 8):
    brightSpecial.set_led_on_off((led + 1,), ON)
    print(brightPi)
    time.sleep(1)

leds = [1, 2, 3, 4, 5, 6, 7, 8]
brightSpecial.set_led_on_off(leds, OFF)
print(brightPi)
