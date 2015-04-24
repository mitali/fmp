__author__ = 'Mitali'

import cv2

video_capture_object = cv2.VideoCapture(0)

while True:
    # capture frame by frame
    ret, frame = video_capture_object.read()

    # frame operations
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

video_capture_object.release()
cv2.destroyAllWindows()