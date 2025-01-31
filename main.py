# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel

# digitalio is used to read from pins on the itsybitsy
from digitalio import DigitalInOut, Direction, Pull


# asyncio and countio are used for interrupts
import asyncio
#import countio

###############################################
#   Setup variables
###############################################

pixel_pin = board.D5    #pin the led strip is contected to
num_pixels = 20         #number of light pixels on the light strip
brightness = .3         #default brightness of strip

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = .3, auto_write=False) #initialize the lightstip objectusing the default parameters

alliance_length = 4
alliance_color = (0,255,0) #default value is green so we can see if there a problem

loop_counter = 0

###############################################
#   End setup variables
###############################################
# test area
pin9 = DigitalInOut(board.D9)
pin9.direction = Direction.INPUT
pin9.pull = Pull.DOWN

pin10 = DigitalInOut(board.D10)
pin10.direction = Direction.INPUT
pin10.pull = Pull.DOWN

pin11 = DigitalInOut(board.D11)
pin11.direction = Direction.INPUT
pin11.pull = Pull.DOWN
# end test area
#
'''
def initialize():
    return 0


#sequence patterns
def set_All(r, g, b):
   pixels.brightness = brightness
   for a in range(20):
        if a < alliance_length:
            pixels[a]=alliance_color
        else:
            pixels[a]=(r, g, b)
   pixels.show()


def set_TwoColors(r, g, b,r2,g2,b2):
   pixels.brightness = brightness
   for a in range(20):
        if a < alliance_length:
            pixels[a] = alliance_color
        elif a%2 == 0:
            pixels[a]=(r,g,b)
        else: 
            pixels[a]=(r2,g2,b2)
   pixels.show()


def set_ThreeColors(r,g,b,r2,g2,b2,r3,g3,b3): #this is not correctly assigning colors at the endpoints
    pixels.brightness = brightness
    for a in range(20):
        if a < alliance_length:
            pixels[a] = alliance_color
        elif a % 3 == 0:
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
    for a in range(steps):
        pixels.brightness = a / steps
        time.sleep(1/steps)
        pixels.show()
    
    for a in range(steps,-1,-1):
        pixels.brightness = a / steps
        time.sleep(1/steps)
        pixels.show()

def animate_colorchase(): 
    temp_list = [(0,0,0)]*(20-alliance_length)
    for a in range(len(temp_list)):
        pos = (a + 1) % (20-alliance_length)
        temp_list[pos] = pixels[a+alliance_length]
    for a in range(len(temp_list)):
        pixels[a+alliance_length] = temp_list[a]
    pixels.show()
    time.sleep(.15)

def animate_colorchase_slicer():
    pixels.brightness = brightness
    pixels[:] = pixels[:alliance_length]+pixels[alliance_length+1:]+pixels[alliance_length:alliance_length+1]
    pixels.show()
    time.sleep(.15)

#unique states:
def set_Alliance():
    #read in from pin
    global alliance_color
    if 1 == 1:
        alliance_color = (255,0,0)
    else:
        alliance_color = (0,0,255)

'''

print('line133')

async def blink():  
    steps = 100
    for a in range(steps):
        pixels.brightness = a / steps
        #time.sleep(1/steps)
        await asyncio.sleep(.15)
        pixels.show()
    
    for a in range(steps,-1,-1):
        pixels.brightness = a / steps
        #time.sleep(1/steps)
        await asyncio.sleep(.15)
        pixels.show()
    await asyncio.sleep(.15)

async def main(): 
    led_task = asyncio.create_task(blink())
    await asyncio.gather(led_task)  # Don't forget the await!
    print("done")


asyncio.run(main())

'''
while True:
    print('Main loop num:',loop_counter)
    #read alliance pin and set alliance color
    
    if(pin10.value): 
        set_All(128,255,128)
        print('pin10 true',pin10.value)
        time.sleep(2)
    else:
        set_All(0,255,0)
        print('pin10 false')
        time.sleep(2)
    print('pin9:',pin9.value)
    print('pin10:',pin10.value)
    print('pin11:',pin11.value)
    '''
'''
    set_Alliance()
    set_All(0,255,0)
    time.sleep(2)
    
    set_TwoColors(255,0,0,0,0,255)
    time.sleep(2)
    
    set_ThreeColors(255,255,0,0,255,255,255,0,255)
    time.sleep(2)

    animate_colorchase()
    #animate_colorchase_slicer()
    animate_fade()
    
    loop_counter += 1
    '''