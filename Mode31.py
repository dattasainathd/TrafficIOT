import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

input1 = 3
output1 = 5

GPIO.setup(input1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(output1, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

def usestate(current):
	print "program function started"
	if current:
		GPIO.output(output1, True)
		print "we successfully received a signal"
	else:
		GPIO.output(output1, False)
		print "we did not receive any signal"
while True:
	print "program has started"
	current = GPIO.input(input1)
	usestate(current)

GPIO.cleanup()