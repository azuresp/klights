# import the necessary packages
import argparse
import kitetalker
import time
from datetime import datetime, timedelta
from RFM69 import Radio, FREQ_915MHZ
import RPi.GPIO as GPIO
from color import color
import patterns

print('starting')

#board IDs,not BCM
left_left_id=7
left_right_id=11
right_left_id=13
right_right_id=35

pattern_plain=1
pattern_alt=2

colormode_whiteorange=1
colormode_bluegreen=2

GPIO.setmode(GPIO.BOARD) #RFM69 library uses this, and we can't mix and match.  :(
GPIO.setup(left_left_id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(left_right_id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(right_left_id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(right_right_id, GPIO.IN, pull_up_down=GPIO.PUD_UP)

new_pattern=0
new_colormode=0

current_pattern=0
current_colormode=0

pattern_executor=patterns.null()

kite = kitetalker.kite()

while True:
    left_left_state = not GPIO.input(left_left_id)
    left_right_state = not GPIO.input(left_right_id)
    right_left_state = not GPIO.input(right_left_id)
    right_right_state = not GPIO.input(right_right_id)
    
    if left_left_state == True:
        new_pattern = pattern_plain
        #print('left handle, left')
    elif left_right_state == True:
        #print('left handle, right')
        new_pattern = pattern_alt

    if right_left_state == True:
        #print('right handle, left')
        new_colormode = colormode_whiteorange
    elif right_right_state == True:
        #print('right handle, right')
        new_colormode = colormode_bluegreen

    if new_pattern != current_pattern:
        if(new_pattern == pattern_plain):
            pattern_executor=patterns.plain(kite, color.white())
        elif(new_pattern == pattern_alt):
            pattern_executor=patterns.alternating(kite, color.white(), color.black())
        current_pattern = new_pattern

    if new_colormode != current_colormode:
        if new_colormode == colormode_whiteorange:
            pattern_executor.setcolor(color.white(), color.orange())
        elif new_colormode == colormode_bluegreen:
            pattern_executor.setcolor(color.blue(), color.green())
        current_colormode = new_colormode
    
    pattern_executor.runtick()

