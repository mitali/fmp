'''
Created on May 5, 2015

@author: Mitali
'''

import cv2
import os

def breakdown(video):

    vidcap = cv2.VideoCapture(video)
    success,image = vidcap.read()
    
    #filename = os.path.basename(video)
    
    count = 0
    
    while success:
        
        print "succeeded"
        
        success,image = vidcap.read()
        
        #cv2.imwrite("/Users/Mitali/Desktop/IndividualProject/fmp/video/frames2/frame%d.jpg" % count, image)
        cv2.imwrite("frames/frame%d.jpg" % count, image)
        
        if cv2.waitKey(10) == 27:
            break
        
        count += 1
        
## to remove the following bit

breakdown('/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos/example.avi')

    
