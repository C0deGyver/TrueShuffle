#!/usr/bin/env python2.7
# Version 0.0.1
# pre-versioning guess work

# import items
import RPi.GPIO as GPIO


try:
	# Setting GPIO mode
	GPIO.setmode(GPIO.BOARD)

	# setup pin number associations to buttons
	pin = 11

	# buttons must be wired to 3v3 and pin in with a pull down
	GPIO.setup(pin, GPIO.IN)

	# add event detection
	GPIO.add_event_detect(pin, GPIO.RISING)
	
	while True:
		if GPIO.event_detected(pin):
			print("Pressed!")
			GPIO.remove_event_detect(pin)

except KeyboardInterrupt:
	print("Keyboard Interrupt!")

finally:
	# clean gpio
	GPIO.cleanup()