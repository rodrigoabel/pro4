#!/usr/bin/python

import bluetooth
import time
import RPi.GPIO as GPIO, os


print "in / out program"

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)

while True:
	print "checkeando" + time.strftime("%a, %d %b %Y %H: %M: %S", time.gmtime())

	result = bluetooth.lookup_name('00:1E:7C:25:D5:16',timeout=5)
	if (result != None):
		print "IN :D"
		GPIO.output(23, True)
	else:
		print "OUT :("
		GPIO.output(23, False)

	time.sleep(1)

