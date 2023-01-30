# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
#from rainbowio import colorwheel
import neopixel
import random

# digitalio is used to read from pins on the itsybitsy
from digitalio import DigitalInOut, Direction, Pull


# asyncio and countio are used for interrupts
import asyncio
import countio

pixel_pin = board.D5
num_pixels = 20

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def getState():
    #Brent: will probably want to read from 5 pins


    #read from pin 1, shift left x times, add ping 2 shift x-1 times, etc pin1 << x + pin2 << (x-1)
    state = 0

    #taken from: https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
    #possibly better guide: https://learn.adafruit.com/circuitpython-digital-inputs-and-outputs


    # For Gemma M0, Trinket M0, Metro M0 Express, ItsyBitsy M0 Express, Itsy M4 Express, QT Py M0
    pin2 = DigitalInOut(board.D2)
    pin2.direction = Direction.INPUT
    pin2.pull = Pull.UP

    pin3 = DigitalInOut(board.D3)
    pin3.direction = Direction.INPUT
    pin3.pull = Pull.UP
    # switch = DigitalInOut(board.D5)  # For Feather M0 Express, Feather M4 Express
    # switch = DigitalInOut(board.D7)  # For Circuit Playground Express

    return state


def setAll(r, g, b):
   for a in range(20):
       pixels[a]=(r, g, b)
   pixels.show()

def setAlternate(r, g, b, r2, g2, b2):
   for a in range(20):
        #pixels[a]=(r,g,b) if a%2 > 0 else pixels[a]=(0,0,0) 
        if a%2 == 0:
            pixels[a]=(r,g,b)
        else: 
            pixels[a]=(r2,g2,b2)
   pixels.show()

#rand = random.random()

#will want this to when any of hte pins change:
#   state value is updated from pins
#   new state value determines the light pattern to show
#
# 
# ###################################################
# State number  |   State meaning   |   Pattern call
#       0                  off          flashing red
# ###################################################

async def catch_interrupt(pin):
    """Print a message when pin goes low."""
    with countio.Counter(pin) as interrupt:
        while True:
            if interrupt.count > 0:
                interrupt.count = 0
                print("interrupted!")

                currentState = getState()

                if currentState == 0:
                    setAll(255,0,0)
                elif currentState == 1:
                    setAll(0,255,0)
                else:
                    setAlternate(0,0,255,255,0,0)
            # Let another task run.
            await asyncio.sleep(0)


async def main():
    interrupt_task = asyncio.create_task(catch_interrupt(board.D3))
    await asyncio.gather(interrupt_task)

asyncio.run(main())