from RFM69 import Radio, FREQ_915MHZ
import datetime
import time
import random
from picamera import PiCamera
from time import sleep

node_id = 1
network_id = 100
recipient_id = 2

class command:
    def __init__(self):
        self.command_type=1
        self.r=0
        self.b=0
        self.g=0
        self.ir=0
    
    def send(self, theradio):
        ct = self.command_type.to_bytes(1,byteorder='big')[0]
        r = self.r.to_bytes(1,byteorder='big')[0]
        g = self.g.to_bytes(1,byteorder='big')[0]
        b = self.b.to_bytes(1,byteorder='big')[0]
        ir = self.ir.to_bytes(1,byteorder='big')[0]

        ba = list([ct,r,g,b,ir])
        print ("Sending", ct, r, g, b, ir)
        radio.send(recipient_id, ba, attempts=3, waitTime=100)

#color table from https://www.w3schools.com/colors/colors_picker.asp?colorhex=ff0000

red = command()
red.r = 255

orange = command()
orange.r = 255
orange.g = 128

yellow = command()
yellow.r = 255
yellow.g = 255

green = command()
green.g = 255

blue = command()
blue.b = 255

indigo = command()
indigo.r=128
indigo.b=255

violet = command()
violet.r = 255
violet.b = 255

white = command()
white.r=100
white.g=100
white.b=100

ir_on = command()
ir_on.command_type=2
ir_on.ir=1

ir_off = command()
ir_off.command_type=2
ir_off.ir=0


black = command()


camera = PiCamera()
camera.start_preview()
sleep(2)

def docommand(c, r, filename):
    ir_off.send(r)
    c.send(r)
    sleep(1)
    camera.capture(filename + '.jpg')
    sleep(1)
    ir_on.send(r)
    sleep(1)
    camera.capture(filename + '-ir.jpg')
    sleep(1)


with Radio(FREQ_915MHZ, node_id, network_id, isHighPower=True, verbose=True) as radio:
    docommand(red, radio, "red")
    docommand(orange, radio, "orange")
    docommand(yellow, radio, "yellow")
    docommand(green, radio, "green")
    docommand(blue, radio, "blue")
    docommand(indigo, radio, "indigo")
    docommand(violet, radio, "violet")
    ir_off.send(radio)
    green.send(radio)
