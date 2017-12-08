#!/usr/bin/python

# Stranger Things Christmas Lights
# Author: Paul Larson (djhazee@gmail.com)
#
# -Port of the Arduino NeoPixel library strandtest example (Adafruit).
# -Uses the WS2811 to animate RGB light strings (I am using a 5V, 50x RGB LED strand)
# -This will blink a designated light for each letter of the alphabet


# Import libs used
import time
import random
from neopixel import *
import argparse

#Start up random seed
random.seed()

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

#Predefined Colors and Masks
OFF = Color(0,0,0)
WHITE = Color(255,255,255)
RED = Color(255,0,0)
GREEN = Color(0,255,0)
BLUE = Color(0,0,255)
PURPLE = Color(128,0,128)
YELLOW = Color(255,255,0)
ORANGE = Color(255,50,0)
TURQUOISE = Color(64,224,208)
RANDOM = Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))



def initLights(strip):
	"""
	initializes the light strand colors 

	inputs: 
	strip = color strip instance to action against

	outputs:
	<none>
	"""
	parser = OptionParser()
	(options, args) = parser.parse_args()
	print(args)
	#Initialize all LEDs
	for i in range(LED_COUNT):
		strip.setPixelColor(i+LIGHTSHIFT, RED)
		strip.show()

# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:

			##Initialize all LEDs
			#for i in range(len(ALPHABET)):
			#strip.setPixelColor(i+LIGHTSHIFT, Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
			#strip.show()

			#initialize all the lights
		initLights(strip)
    


    
