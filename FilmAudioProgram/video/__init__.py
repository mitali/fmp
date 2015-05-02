__author__ = 'Mitali'

# COIN SEGMENTATION

import numpy as np
import cv2

# instantiate VideoCapture class
cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 720)

# read frames + convert them to gray
while True:
    ret, frame = cap.read()
    roi = frame[0:500, 0:500]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
# adaptive thresholding
gray_blur = cv2.GaussianBlur(gray, (15,15), 0)
thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 11, 1)

# applying morphological operators
kernel = np.ones((3,3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=4)

# contour detection and filtering

cont_img = closing.copy()
contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)


    
