print("This was run from locate-continuous.py")

# import the necessary packages
import argparse
import imutils
import cv2
import kitefinder
import kitetalker
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from datetime import datetime, timedelta
from RFM69 import Radio, FREQ_915MHZ

###################Setup for basic tracking
ir_on = kitetalker.command()
ir_on.command_type=2
ir_on.ir=1

indigo = kitetalker.command()
indigo.r=128
indigo.b=255

green = kitetalker.command()
green.g=255

off = kitetalker.command()

node_id = 1
network_id = 100
recipient_id = 2

with Radio(FREQ_915MHZ, node_id, network_id, isHighPower=True, verbose=True) as radio:
    indigo.send(radio)
    ir_on.send(radio)

RESOLUTION = (1024, 768)

# Initialise Raspberry Pi camera
camera = PiCamera()
camera.resolution = RESOLUTION

# set up stream buffer
rawCapture = PiRGBArray(camera, size=RESOLUTION)
# allow camera to warm up
time.sleep(0.1)
print("PiCamera ready")

# Initialise OpenCV window
#cv2.namedWindow("#preview")

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # as raw NumPy array
    image = frame.array.copy()
    kitefinder.find_kite(image)

    # clear stream for next frame
    rawCapture.truncate(0)

    # Wait for the magic key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
        break
        
# When everything is done, release the capture
with Radio(FREQ_915MHZ, node_id, network_id, isHighPower=True, verbose=True) as radio:
    green.send(radio)
    ir_off.send(radio)

camera.close()
cv2.destroyAllWindows()