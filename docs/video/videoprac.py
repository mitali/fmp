__author__ = 'Mitali'

import numpy as np
import sys
import cv2

sys.path.append('/usr/local/lib/python2.7/site-packages')

cap = cv2.VideoCapture(0)

while True:
    # capture frame by frame
    ret, frame = cap.read()

    # frame operations
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cap.release()
cv2.destroyAllWindows()