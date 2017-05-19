import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

inir11 = 3
inir12 = 5
inir13 = 7
outie1G = 11
outie1R = 13
GPIO.setup(inir11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie1G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie1R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

def UseState1(current11, current12, current13):
	print "The green signal is enabled at lane 1"
	GPIO.output(outie1G, True)
	GPIO.output(outie1R, False)
	if current11:
		if current12:
			if current13:
				print "The traffic density at lane 1 is at level 3"
				print "The green signal is enabled for 20 seconds (10 Buffer/Extra seconds are given)"
				time.sleep(20)
			else:
				print "The traffic density at lane 1 is at level 2"
				print "The green signal is enabled for 15 seconds (5 Buffer/Extra seconds are given)"
				time.sleep(15)
		else:
			print "The traffic density at lane 1 is at level 1"
			print "The green signal is enabled for 10 seconds (Buffer/Extra seconds are not given )"
			time.sleep(10)	
	else:
		print "The traffic density at lane 1 is very low"
		print "The green signal is enabled for 5 seconds (buffer/extra seconds are not given)"
		time.sleep(5)
	print "The red signal is enabled at lane 1"
	GPIO.output(outie1G, False)
	GPIO.output(outie1R, True)

inir21 = 15
inir22 = 19
inir23 = 21
outie2G = 23
outie2R = 29
GPIO.setup(inir21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie2G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie2R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
		
def UseState2(current21, current22, current23):
	print "The green signal is enabled at lane 2"
	GPIO.output(outie2G, True)
	GPIO.output(outie2R, False)
	if current21:
		if current22:
			if current23:
				print "The traffic density at lane 2 is at level 3"
				print "The green signal is enabled for 20 seconds (10 Buffer/Extra seconds are given)"
				time.sleep(20)
			else:
				print "The traffic density at lane 2 is at level 2"
				print "The green signal is enabled for 15 seconds (5 Buffer/Extra seconds are given)"
				time.sleep(15)
		else:
			print "The traffic density at lane 2 is at level 1"
			print "The green signal is enabled for 10 seconds (Buffer/Extra seconds are not given )"
			time.sleep(10)	
	else:
		print "The traffic density at lane 2 is very low"
		print "The green signal is enabled for 5 seconds (buffer/extra seconds are not given)"
		time.sleep(5)
	print "The red signal is enabled at lane 2"
	GPIO.output(outie2G, False)
	GPIO.output(outie2R, True)
        
        
inir31 = 31
inir32 = 33
inir33 = 35
outie3G = 37
outie3R = 40
GPIO.setup(inir31, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir32, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir33, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie3G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie3R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
		
def UseState3(current31, current32, current33):
	print "The green signal is enabled at lane 3"
	GPIO.output(outie3G, True)
	GPIO.output(outie3R, False)
	if current31:
		if current32:
			if current33:
				print "The traffic density at lane 3 is at level 3"
				print "The green signal is enabled for 20 seconds (10 Buffer/Extra seconds are given)"
				time.sleep(20)
			else:
				print "The traffic density at lane 3 is at level 2"
				print "The green signal is enabled for 15 seconds (5 Buffer/Extra seconds are given)"
				time.sleep(15)
		else:
			print "The traffic density at lane 3 is at level 1"
			print "The green signal is enabled for 10 seconds (Buffer/Extra seconds are not given )"
			time.sleep(10)	
	else:
		print "The traffic density at lane 3 is very low"
		print "The green signal is enabled for 5 seconds (buffer/extra seconds are not given)"
		time.sleep(5)
	print "The red signal is enabled at lane 3"
	GPIO.output(outie3G, False)
	GPIO.output(outie3R, True)
        
        
inir41 = 38
inir42 = 36
inir43 = 32
outie4G = 26
outie4R = 24
GPIO.setup(inir41, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir42, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir43, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie4G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie4R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

def UseState4(current41, current42, current43):
	print "The green signal is enabled at lane 4"
	GPIO.output(outie4G, True)
	GPIO.output(outie4R, False)
	if current41:
		if current42:
			if current43:
				print "The traffic density at lane 4 is at level 3"
				print "The green signal is enabled for 20 seconds (10 Buffer/Extra seconds are given)"
				time.sleep(20)
			else:
				print "The traffic density at lane 4 is at level 2"
				print "The green signal is enabled for 15 seconds (5 Buffer/Extra seconds are given)"
				time.sleep(15)
		else:
			print "The traffic density at lane 4 is at level 1"
			print "The green signal is enabled for 10 seconds (Buffer/Extra seconds are not given )"
			time.sleep(10)	
	else:
		print "The traffic density at lane 4 is very low"
		print "The green signal is enabled for 5 seconds (buffer/extra seconds are not given)"
		time.sleep(5)
	print "The red signal is enabled at lane 3"
	GPIO.output(outie4G, False)
	GPIO.output(outie4R, True)

GPIO.output(outie1R, True)
GPIO.output(outie2R, True)
GPIO.output(outie3R, True)
GPIO.output(outie4R, True)



    
while True:
    current11 = GPIO.input(inir11)
    current12 = GPIO.input(inir12)
	current13 = GPIO.input(inir13)
    UseState1(current11, current12, current13)
    current21 = GPIO.input(inir21)
    current22 = GPIO.input(inir22)
	current23 = GPIO.input(inir23)
    UseState2(current21, current22, current23)
    current31 = GPIO.input(inir31)
    current32 = GPIO.input(inir32)
	current33 = GPIO.input(inir33)
    UseState3(current31, current32, current33)
    current41 = GPIO.input(inir41)
    current42 = GPIO.input(inir42)
	current43 = GPIO.input(inir43)
    UseState4(current41, current42, current43)

	
GPIO.cleanup()