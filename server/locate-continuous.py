print("This was run from locate-continuous.py")

# import the necessary packages
import argparse
import imutils
import cv2
import kitefinder
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from datetime import datetime, timedelta

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
