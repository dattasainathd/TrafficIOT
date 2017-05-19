import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

innie1 = 3
outie1G = 5
outie1R = 7
GPIO.setup(innie1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie1G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie1R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

def UseState1(current1):
	if current1:
		print "The traffic density at lane 1 is at level 1"
		print "The green signal will be enabled for 5 seconds"
		GPIO.output(outie1G, True)
		GPIO.output(outie1R, False)
		time.sleep(5)
		print "The red signal will be enabled for 15 seconds"
		GPIO.output(outie1G, False)
		GPIO.output(outie1R, True)
		time.sleep(15)
		
	else:
		print "The traffic density at lane 1 is nil"
		print "The red signal will be enabled for 15 seconds"
		GPIO.output(outie1G, False)
		GPIO.output(outie1R, True)
		time.sleep(15)

innie2 = 11
outie2G = 13
outie2R = 15
GPIO.setup(innie2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie2G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie2R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
		
def UseState2(current2):
	if current2:
		print "The traffic density at lane 2 is at level 1"
		print "The green signal will be enabled for 5 seconds"
		GPIO.output(outie2G, True)
		GPIO.output(outie2R, False)
		time.sleep(5)
		print "The red signal will be enabled for 15 seconds"
		GPIO.output(outie2G, False)
		GPIO.output(outie2R, True)
		time.sleep(15)
	else:
		print "The traffic density at lane 2 is nil"
		print "The red signal will be enabled for 15 seconds"
		GPIO.output(outie2G, False)
		GPIO.output(outie2R, True)
		time.sleep(15)

innie3 = 19
outie3G = 21
outie3R = 23
GPIO.setup(innie3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie3G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie3R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
		
def UseState3(current3):
	if current:
		print "The traffic density at lane 3 is at level 1"
		print "The green signal will be enabled for 5 seconds"
		GPIO.output(outie3G, True)
		GPIO.output(outie3R, False)
		time.sleep(5)
		print "The red signal will be enabled for 15 seconds"
		GPIO.output(outie3G, False)
		GPIO.output(outie3R, True)
		time.sleep(15)
	else:
		print "The traffic density at lane 3 is nil"
		print "The red signal will be enabled for 15 seconds"
		GPIO.output(outie3G, False)
		GPIO.output(outie3R, True)
		time.sleep(15)
innie4 = 22
outie4G = 24
outie4R = 26
GPIO.setup(innie4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie4G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie4R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

def UseState4(current4):
	if current:
		print "The traffic density at lane 4 is at level 1"
		print "The green signal will be enabled for 5 seconds"
		GPIO.output(outie4G, True)
		GPIO.output(outie4R, False)
		time.sleep(5)
		print "The red signal will be enabled for 15 seconds"
		GPIO.output(outie4G, False)
		GPIO.output(outie4R, True)
		time.sleep(15)
	else:
		print "The traffic density at lane 4 is nil"
		print "The red signal will be enabled for 15 seconds"
		GPIO.output(outie4G, False)
		GPIO.output(outie4R, True)
		time.sleep(15)

GPIO.output(outie1R, True)
GPIO.output(outie2R, True)
GPIO.output(outie3R, True)
GPIO.output(outie4R, True)

while True:
	current1 = GPIO.input(innie1)
	UseState1(current1)
	current2 = GPIO.input(innie2)
	UseState2(current2)
	current3 = GPIO.input(innie3)
	##UseState3(current3)
	current4 = GPIO.input(innie4)
	##UseState4(current4)

GPIO.cleanup()
