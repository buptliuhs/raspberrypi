import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

cnt = 0
MAIL_CHECK_FREQ = 5
RED_LED = 21
GPIO.setup(RED_LED, GPIO.OUT)
while True:
	if cnt == 0 :
		GPIO.output(RED_LED, False)
		cnt = 1
		print "off"
	else:
		GPIO.output(RED_LED, True)
		cnt = 0
		print "on"
	time.sleep(MAIL_CHECK_FREQ)

