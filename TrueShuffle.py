#!/usr/bin/env python2.7
# Version 1.0.0

# import items
import RPi.GPIO as GPIO

print("Running TrueShuffle.py")

try:
        # Setting GPIO mode
        print("Setting GPIO mode")
        GPIO.setmode(GPIO.BOARD)

        # setup pin number associations to buttons
        print("Setting pin numbers")
        playPin = 11
        pausePin = 12
        stopPin = 13
        likePin = 15
        dislikePin = 16
        offPin = 18

	# var to hold paused or playing
	paused = False

        # buttons must be wired to 3v3
        # using builtin pull-down resistors
        print("Setting up pins to be pulled down to ground")
        GPIO.setup(playPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pausePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(stopPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(likePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(dislikePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(offPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # callback functions for events
        print("Defining callbacks for the interrupts")
        def playCallBack(channel):
                print("Play Pressed")

        def pauseCallBack(channel):
		global paused
		if (paused):
			paused = False
			print("Unpaused Pressed")
		else:
			paused = True
			print("Paused Pressed")

        def stopCallBack(channel):
		print("Stop Pressed")

        def likeCallBack(channel):
                print("Like Pressed")

        def dislikeCallBack(channel):
                print(Dislike "Pressed")

        # add event detection
        print("Adding event detection for the buttons")
        GPIO.add_event_detect(playPin, GPIO.RISING, callback=playCallBack)
        GPIO.add_event_detect(pausePin, GPIO.RISING, callback=pauseCallBack)
        GPIO.add_event_detect(stopPin, GPIO.RISING, callback=stopCallBack)
        GPIO.add_event_detect(likePin, GPIO.RISING, callback=likeCallBack)
        GPIO.add_event_detect(dislikePin, GPIO.RISING, callback=dislikeCallBack)

        # getting rid of the endless loop to free the proc up
        GPIO.wait_for_edge(offPin, GPIO.RISING)
        print("Off Pressed. Stopping program")

finally:
        # clean gpio
        print("Cleaning GPIO")
        GPIO.remove_event_detect(playPin)
        GPIO.remove_event_detect(pausePin)
        GPIO.remove_event_detect(stopPin)
        GPIO.remove_event_detect(likePin)
        GPIO.remove_event_detect(dislikePin)
        GPIO.remove_event_detect(offPin)
        GPIO.cleanup()
        print("TrueShuffle.py finished")
