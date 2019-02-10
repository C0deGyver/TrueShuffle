#!/usr/bin/env python2.7
# Version 0.0.2
# pre-versioning guess work

# import items
import RPi.GPIO as GPIO


try:
	# Setting GPIO mode
	GPIO.setmode(GPIO.BOARD)

	# setup pin number associations to buttons
	pin = 11
	pin2 = 12

	# buttons must be wired to 3v3 and pin in with a pull down
	GPIO.setup(pin, GPIO.IN)
	GPIO.setup(pin2, GPIO.IN)

	# add event detection
	GPIO.add_event_detect(pin, GPIO.RISING)
	GPIO.add_event_detect(pin2, GPIO.RISING)
	
	while True:
		if GPIO.event_detected(pin):
			print("Pressed!")

		if GPIO.event_detected(pin2):
			print("Pressed!")

except KeyboardInterrupt:
	print("Keyboard Interrupt!")

finally:
	# clean gpio
	GPIO.remove_event_detect(pin)
	GPIO.remove_event_detect(pin2)
	GPIO.cleanup()