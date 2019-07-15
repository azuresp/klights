from RFM69 import Radio, FREQ_915MHZ
import datetime
import time
import random
from time import sleep

node_id = 1
network_id = 100
recipient_id = 2

class kite:
    def __init__(self):
        self.radio=Radio(FREQ_915MHZ, node_id, network_id, isHighPower=True, verbose=True)
        self.command_type=1
        self.r=0
        self.b=0
        self.g=0
        self.ir=0
    
    def send(self, color1, color2):
        ct = self.command_type.to_bytes(1,byteorder='big')[0]
        r = color1.r.to_bytes(1,byteorder='big')[0]
        g = color1.g.to_bytes(1,byteorder='big')[0]
        b = color1.b.to_bytes(1,byteorder='big')[0]
        ir = self.ir.to_bytes(1,byteorder='big')[0]

        ba = list([ct,r,g,b,ir])
        print ("Sending", ct, r, g, b, ir)
        self.radio.send(recipient_id, ba, attempts=3, waitTime=100)