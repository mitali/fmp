'''
Created on May 2, 2015

@author: Mitali
'''

import cv2

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.BackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    
    if k == 27:
        break;
    
cap.release()
cv2.destroyAllWindows()

