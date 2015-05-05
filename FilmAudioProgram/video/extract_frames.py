'''
Created on May 5, 2015

@author: Mitali
'''

import cv2

vidcap = cv2.VideoCapture('videos/badeggs_pixar.avi')
success, image = vidcap.read()

count = 0

while success:
    
    success, image = vidcap.read()
    cv2.imwrite("frames/frame%d.jpg" % count, image)
    
    if cv2.waitKey(10) == 27:
        break
    
    count += 1
    
