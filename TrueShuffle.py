#!/usr/bin/env python2.7
# Version 0.1.2
# pre-versioning guess work

# import items
import RPi.GPIO as GPIO

print("Running TrueShuffle.py")

try:
        # Setting GPIO mode
        print("Setting GPIO mode")
        GPIO.setmode(GPIO.BOARD)

        # setup pin number associations to buttons
        print("Setting pin numbers")
        pin = 11
        pin2 = 12
        pin3 = 13
        pin4 = 15
        pin5 = 16
        pin6 = 18

        # buttons must be wired to 3v3
        # using builtin pull-down resistors
        print("Setting up pins to be pulled down to ground")
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pin5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pin6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # callback functions for events
        print("Defining callbacks for the interrupts")
        def pinFunc(channel):
                print("Pressed!")

        def pin2Func(channel):
                print("Pressed 2!")

        def pin3Func(channel):
                print("Pressed 3!")

        def pin4Func(channel):
                print("Pressed 4!")

        def pin5Func(channel):
                print("Pressed 5!")

        # add event detection
        print("Adding event detection for the buttons")
        GPIO.add_event_detect(pin, GPIO.RISING, callback=pinFunc)
        GPIO.add_event_detect(pin2, GPIO.RISING, callback=pin2Func)
        GPIO.add_event_detect(pin3, GPIO.RISING, callback=pin3Func)
        GPIO.add_event_detect(pin4, GPIO.RISING, callback=pin4Func)
        GPIO.add_event_detect(pin5, GPIO.RISING, callback=pin5Func)

        # getting rid of the endless loop to free the proc up
        GPIO.wait_for_edge(pin6, GPIO.RISING)
        print("Pressed 6. Stopping program")

finally:
        # clean gpio
        print("Cleaning GPIO")
        GPIO.remove_event_detect(pin)
        GPIO.remove_event_detect(pin2)
        GPIO.remove_event_detect(pin3)
        GPIO.remove_event_detect(pin4)
        GPIO.remove_event_detect(pin5)
        GPIO.remove_event_detect(pin6)
        GPIO.cleanup()
        print("TrueShuffle.py finished!")
