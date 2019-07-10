print("This was run from locate.py")

import argparse
import cv2
import kitefinder
from datetime import datetime, timedelta


image = cv2.imread("/green-ir.jpg")
start_time = datetime.utcnow()
kitefinder.find_kite(image)

endtime = datetime.utcnow()
diff = endtime - start_time
print(str(diff.microseconds))
