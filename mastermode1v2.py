import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)



inir11 = 3
inir12 = 29
inir13 =
outie1G = 5
outie1R = 7
GPIO.setup(inir11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie1G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie1R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

def UseState1(current11):
	if current11:
		print "The green signal is enabled at lane 1"
		GPIO.output(outie1G, True)
		GPIO.output(outie1R, False)
		if current12:
			print "The traffic density at lane 1 is at level 2"
            time.sleep(15)
		else:
			print "The traffic density at lane 1 is at level 1"
			time.sleep(10)
    print "The red signal is enabled at lane 1"
	GPIO.output(outie1G, False)
	GPIO.output(outie1R, True)
    
		
	else:
		print "The traffic density at lane 1 is very low"
		print "The green signal is enabled for 5 seconds (buffer/extra seconds are not given)"
		GPIO.output(outie1G, True)
		GPIO.output(outie1R, False)
		time.sleep(5)
		print "The red signal is enabled for lane 1"
		GPIO.output(outie1G, False)
		GPIO.output(outie1R, True)

inir21 = 11
inir22 = 31
inir23 = 
outie2G = 13
outie2R = 15
GPIO.setup(inir21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie2G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie2R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
		
def UseState2(current21):
	if current21:
		print "The green signal is enabled at lane 2"
		GPIO.output(outie2G, True)
		GPIO.output(outie2R, False)
		if current22:
			print "The traffic density at lane 2 is at level 2"
            time.sleep(15)
		else:
			print "The traffic density at lane 2 is at level 1"
			time.sleep(10)
    print "The red signal is enabled at lane 2"
	GPIO.output(outie2G, False)
	GPIO.output(outie2R, True)
    
		
	else:
		print "The traffic density at lane 2 is very low"
		print "The green signal is enabled for 5 seconds (buffer/extra seconds are not given)"
		GPIO.output(outie2G, True)
		GPIO.output(outie2R, False)
		time.sleep(5)
		print "The red signal is enabled for lane 2"
		GPIO.output(outie2G, False)
		GPIO.output(outie2R, True)
        
        
inir31 = 19
inir32 = 33
inir33 = 
outie3G = 21
outie3R = 23
GPIO.setup(inir31, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setip(inir32, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir33, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie3G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie3R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
		
def UseState3(current31):
	if current31:
		print "The green signal is enabled at lane 3"
		GPIO.output(outie3G, True)
		GPIO.output(outie3R, False)
		if current32:
			print "The traffic density at lane 3 is at level 2"
            time.sleep(15)
		else:
			print "The traffic density at lane 3 is at level 1"
			time.sleep(10)
    print "The red signal is enabled at lane 3"
	GPIO.output(outie3G, False)
	GPIO.output(outie3R, True)
    
		
	else:
		print "The traffic density at lane 3 is very low"
		print "The green signal is enabled for 5 seconds (buffer/extra seconds are not given)"
		GPIO.output(outie3G, True)
		GPIO.output(outie3R, False)
		time.sleep(5)
		print "The red signal is enabled for lane 3"
		GPIO.output(outie3G, False)
		GPIO.output(outie3R, True)
        
        
inir41 = 22
inir42 = 35
inir43 = 
outie4G = 24
outie4R = 26
GPIO.setup(inir41, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir42, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(inir43, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie4G, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(outie4R, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

def UseState4(current41):
	if current41:
		print "The green signal is enabled at lane 4"
		GPIO.output(outie4G, True)
		GPIO.output(outie4R, False)
		if current42:
			print "The traffic density at lane 4 is at level 2"
            time.sleep(15)
		else:
			print "The traffic density at lane 4 is at level 1"
			time.sleep(10)
    print "The red signal is enabled at lane 4"
	GPIO.output(outie4G, False)
	GPIO.output(outie4R, True)
    
		
	else:
		print "The traffic density at lane 4 is very low"
		print "The green signal is enabled for 5 seconds (buffer/extra seconds are not given)"
		GPIO.output(outie4G, True)
		GPIO.output(outie4R, False)
		time.sleep(5)
		print "The red signal is enabled for lane 4"
		GPIO.output(outie4G, False)
		GPIO.output(outie4R, True)

GPIO.output(outie1R, True)
GPIO.output(outie2R, True)
GPIO.output(outie3R, True)
GPIO.output(outie4R, True)



    
while True:
    current11 = GPIO.input(inir11)
    current12 = GPIO.input(inir12)
    UseState1(Current11)
    current21 = GPIO.input(inir21)
    current22 = GPIO.input(inir22)
    UseState2(Current21)
    current31 = GPIO.input(inir31)
    current32 = GPIO.input(inir32)
    UseState3(Current31)
    current41 = GPIO.input(inir41)
    current42 = GPIO.input(inir42)
    UseState4(Current41)
    

GPIO.cleanup()
