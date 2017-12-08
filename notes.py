#!/usr/bin/python

# Stranger Things Christmas Lights
# Author: Paul Larson (djhazee@gmail.com)
#
# -Port of the Arduino NeoPixel library strandtest example (Adafruit).
# -Uses the WS2811 to animate RGB light strings (I am using a 5V, 50x RGB LED strand)
# -This will blink a designated light for each letter of the alphabet


# Import libs used

from neopixel import *
import sys
import time

# LED strip configuration:
LED_COUNT = 100
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

#Predefined Colors and Masks
OFF = Color(0,0,0)
RED = Color(255,0,0)
GREEN = Color(0,255,0)



def off(strip):
	for i in range(LED_COUNT):
		strip.setPixelColor(i,OFF)
	strip.show()

def initLights(strip, count):

	
	#Initialize all LEDs
	for i in range(count):
		if i % 2 == 0:
				strip.setPixelColor(i, GREEN)
		else:
				strip.setPixelColor(i,RED)
	strip.show()

def note(strip,count,ontime,offtime):
	initLights(strip,count)
	time.sleep(ontime)
	off(strip)
	time.sleep(offtime)
	
def rest(offtime):
	time.sleep(offtime)



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
  strip.begin()

 
while True:
    #initialize all the lights
	note(strip,80,0.25,0.25)
	rest(0.25)
	note(strip,95,0.25,0.25)
	rest(0.25)
	note(strip,60,0.25,0.25)
	rest(0.25)
	note(strip,75,0.25,0.25)
	rest(0.25)
	note(strip,80,0.25,0.25)
	rest(0.25)

    


    
