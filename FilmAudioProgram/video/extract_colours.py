'''
Created on May 29, 2015

@author: Mitali
'''

# this works!

import cv2
import numpy as np

cap = cv2.VideoCapture('videos/coyote.mp4')

while(1):
    
    # take each frame
    _, frame = cap.read()
    
    # convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # threshold hsv image to get only blue
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # bitwise-and mask with original image
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()