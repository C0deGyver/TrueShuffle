#!/usr/bin/env python2.7
# Version 0.1.0
# pre-versioning guess work

# import items
import RPi.GPIO as GPIO


try:
	# Setting GPIO mode
	GPIO.setmode(GPIO.BOARD)

	# setup pin number associations to buttons
	pin = 11
	pin2 = 12
	pin3 = 13

	# buttons must be wired to 3v3
	# using builtin pull-down resistors
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	# callback functions for events
	def pinFunc(channel):
		print("Pressed!")

	def pin2Func(channel):
		print("Pressed 2!")

	# add event detection
	GPIO.add_event_detect(pin, GPIO.RISING, callback=pinFunc)
	GPIO.add_event_detect(pin2, GPIO.RISING, callback=pin2Func)

	# getting rid of the endless loop to free the proc up
	GPIO.wait_for_edge(pin3, GPIO.RISING)
	print("Pressed 3. Stopping program")

finally:
	# clean gpio
	GPIO.remove_event_detect(pin)
	GPIO.remove_event_detect(pin2)
	GPIO.remove_event_detect(pin3)
	GPIO.cleanup()
