from RFM69 import Radio, FREQ_915MHZ
import argparse
import kitetalker
import time
from datetime import datetime, timedelta

###################Setup for basic tracking
ir_off = kitetalker.command()
ir_off.command_type=2
ir_off.ir=0

off = kitetalker.command()

node_id = 1
network_id = 100
recipient_id = 2

with Radio(FREQ_915MHZ, node_id, network_id, isHighPower=True, verbose=True) as radio:
    off.send(radio)
    ir_off.send(radio)