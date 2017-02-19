import RPi.GPIO as GPIO
import time

# BCM is short for something.
GPIO.setmode(GPIO.BCM)
# I don't care.
GPIO.setwarnings(False)

# 517 cycles are about a full rotation
cycles = 30;

# defining the ports.
port0 = 22;
port1 = 23;
port2 = 24;
port3 = 25;


# setup of ports.
GPIO.setup(port0,GPIO.OUT)
GPIO.setup(port1,GPIO.OUT)
GPIO.setup(port2,GPIO.OUT)
GPIO.setup(port3,GPIO.OUT)


print "Tiny motor enabled, goodluck!"
print "Spinning right."
for n in range(1,cycles):
	try:
			#Right, spinning right!
			GPIO.output(port3,1)
			time.sleep(0.01)
			GPIO.output(port3,0)
			GPIO.output(port2,1)
			time.sleep(0.01)
			GPIO.output(port2,0)
			GPIO.output(port1,1)
			time.sleep(0.01)
			GPIO.output(port1,0)
			GPIO.output(port0,1)
			time.sleep(0.01)
			GPIO.output(port0,0)
	except Exception as e:
		# I don't care, replace this once the mechanics are in place.
		pass
print "Spinning left."
for n in range(1,cycles):
			GPIO.output(port0,1)
			time.sleep(0.01)
			GPIO.output(port0,0)
			GPIO.output(port1,1)
			time.sleep(0.01)
			GPIO.output(port1,0)
			GPIO.output(port2,1)
			time.sleep(0.01)
			GPIO.output(port2,0)
			GPIO.output(port3,1)
			time.sleep(0.01)
			GPIO.output(port3,0)
		except Exception as e:
			# still don't care.
			pass

# Just in case, this resets our pins to normal.
GPIO.cleanup()
