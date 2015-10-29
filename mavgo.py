#!/usr/bin/env python
__author__ = 'abroda'

from gopigo import *
import sys


def led_test():
    print("GoPiGo testing LEDs...")

    led_on(LED_L)
    time.sleep(1)
    led_on(LED_R)
    time.sleep(1)
    led_off(LED_L)
    led_off(LED_R)

    print("Done.")


def motor_test():

    set_speed(255)
    fwd()
    time.sleep(1)
    set_speed(180)
    time.sleep(1)

    set_speed(180)
    left()
    time.sleep(3)
    right()
    time.sleep(3)

    bwd()
    time.sleep(3)

    stop()

motor_test()
