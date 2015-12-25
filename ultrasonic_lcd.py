
from grovepi import *
from grove_rgb_lcd import *

ultrasonic_port = 4

while True:
	try:
		distance = ultrasonicRead(ultrasonic_port)
		print "Distance:", distance
		
		setRGB(168,0,168)
		setText("Distance: " + str(distance))
	except (IOError,TypeError) as e:
		print "Error"
