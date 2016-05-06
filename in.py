import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

MAIL_CHECK_FREQ = 1
PORT=12
GPIO.setup(PORT, GPIO.IN)
while True:
	if GPIO.input(PORT):
		print "on"
	else:
		print "off"
	time.sleep(MAIL_CHECK_FREQ)

