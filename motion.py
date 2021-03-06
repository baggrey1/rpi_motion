import RPi.GPIO as GPIO
import time
import datetime
from astral import Astral

# GPIO configuration
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

# Astral configuration
a = Astral()
a. solar_depression = 'civil'
city_name='Los Angeles'
city = a.city_name

try:
	print "PIR Module Test"
	time.sleep(2)
	print "Ready"

	while True:
		if GPIO.input(PIR_PIN):
			print "Motion Detected"
		time.sleep(1)

except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()
