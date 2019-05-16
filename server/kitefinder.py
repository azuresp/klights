import imutils
import cv2

def find_kite(image):
    #cv2.imshow("#preview", image)
    
    # load the image, convert it to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY)[1]

    # find contours in the thresholded image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    #TODO: we may need a "threshold calibrator" which will fish for the possible range of thresholds
    #and pick a reasonable one.

    if len(cnts) > 1:
        print(str(len(cnts)) + " contours found - too many!")
        return

    if len(cnts) == 0:
        print("not enough contours!")
        return

    # loop over the contours
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)

        if M["m00"]!=0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            print(str(cX) + ', ' + str(cY))
        else:
            print("We're missing stuff - change the threshold?")