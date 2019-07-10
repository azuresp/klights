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
        theradio.send(recipient_id, ba, attempts=3, waitTime=100)