# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel
#import random

###############################################
#   Setup variables
###############################################

pixel_pin = board.D5    #pin the led strip is contected to
num_pixels = 20         #number of light pixels on the light strip
brightness = .3         #default brightness of strip

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = .3, auto_write=False) #initialize the lightstip objectusing the default parameters

pixel_list = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]

loop_counter = 0

###############################################
#   End setup variables
###############################################


# test area
i=0


# end test area

#sequence patterns
def set_All(r, g, b):
   pixels.brightness = brightness
   for a in range(20):
       pixels[a]=(r, g, b)
   pixels.show()


def set_TwoColors(r, g, b,r2,g2,b2):
   pixels.brightness = brightness
   for a in range(20):
        if a%2 == 0:
            pixels[a]=(r,g,b)
        else: 
            pixels[a]=(r2,g2,b2)
   pixels.show()
        

def set_ThreeColors(r,g,b,r2,g2,b2,r3,g3,b3): #this is not correctly assigning colors at the endpoints
    pixels.brightness = brightness
    for a in range(20):
        if a % 3 == 0:
            pixels[a] = (r,g,b)
        elif a % 3 == 1:
            pixels[a] = (r2,g2,b2)
        else:
            pixels[a] = (r3,g3,b3)
    pixels.show()
    time.sleep(.15)
    
#animations
def animate_fade():
    steps = 100
    while True:
        for a in range(steps):
            pixels.brightness = a / steps
            time.sleep(1/steps)
            pixels.show()
        
        for a in range(steps,-1,-1):
            pixels.brightness = a / steps
            time.sleep(1/steps)

            pixels.show()

def animate_colorchase():
    temp_list = [(0,0,0)]*20
    while True:
        for a in range(len(pixels)):
            pos = (a + 1) % 20
            temp_list[pos] = pixels[a]
        for a in range(len(temp_list)):
            pixels[a] = temp_list[a]
        pixels.show()
        time.sleep(.15)

def animate_colorchase_slicer():
    pixels.brightness = brightness
    pixels[:] = pixels[1:]+pixels[:1]
    pixels.show()
    time.sleep(.15)
#unique states:
def set_Alliance():
    #read in from pin
    if 1 == 1:
        set_All(255,0,0)
    else:
        set_All(0,0,255)

#rand = random.randrange(8)
#print('test')
while True:
    print('Main loop num:',loop_counter)


    #read alliance pin and set alliance color

    #setAll(0,255,0)
    #time.sleep(2)


    
    #setAlternate(255,0,0,0,0,255)
    #time.sleep(2)
    
    set_ThreeColors(255,255,0,0,255,255,255,0,255)
    animate_colorchase()
    
    #chase needs to keep running in order to work

    loop_counter += 1