# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.D5
num_pixels = 20

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)



print('Starting!')


def setAll(r, g, b):
   for a in range(20):
       pixels[a]=(r, g, b)
   pixels.show()


def setAlternate(r, g, b,r2,g2,b2):
   for a in range(20):
        #pixels[a]=(r,g,b) if a%2 > 0 else pixels[a]=(0,0,0) 
        if a%2 == 0:
            pixels[a]=(r,g,b)
        else: 
            pixels[a]=(r2,g2,b2)
   pixels.show()

while True:
    print('starting main loop again')

    time.sleep(1)
    pixels.brightness=0.7
    setAlternate(255,0,0,0,255,0)
    time.sleep(1)
    pixels.brightness=0.3
    setAlternate(100,255,100,255,100,255)
    





