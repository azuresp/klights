# Object location in static image; useful for testing in docker but we
# need to start exercising continuous feed from pi camera.  Maybe
# refactor the extractor into a common file?

print("This was run from locate.py")

# import the necessary packages
import argparse
import imutils
import cv2
from datetime import datetime, timedelta

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread("/green-ir.jpg")
start_time = datetime.utcnow()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY)[1]

#debug dumps
#cv2.imwrite("/dump/green-ir-blur.jpg", blurred)
#cv2.imwrite("/dump/green-ir-thresh.jpg", thresh)

# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(cnts)

#TODO: we may need a "threshold calibrator" which will fish for the possible range of thresholds
#and pick a reasonable one.

print(str(len(cnts)) + " contours found")
if len(cnts) > 1:
    print("too many contours!")
    exit()

if len(cnts) == 0:
    print("not enough contours!")
    exit()

# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)

    if M["m00"]!=0:
        print("we've got all the bits we need!")
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print(str(cX) + ', ' + str(cY))
    else:
        print("We're missing stuff - change the threshold?")
    
endtime = datetime.utcnow()
diff = endtime - start_time
print(str(diff.microseconds))
