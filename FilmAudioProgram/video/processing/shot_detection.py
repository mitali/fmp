'''
Created on Jun 1, 2015

@author: Mitali
'''

import cv2
import sys

def shot_detect(video):
 
    cap = cv2.VideoCapture(video)
    #cap.open(video)
     
    if not cap.isOpened():
        print "Fatal error - could not open video %s" % video
        return
    else:
        print "Parsing video %s..." % video
         
    # stuff here
     
    width = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
     
    print "Video Resolution: %d x %d" % (width, height)
     
    while True:
        (rv, im) = cap.read()
        if not rv:
            break;
         
    frame_count = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
     
    print "Read %d frames from video." % frame_count
     
    cap.release()
     
shot_detect('/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos/cars_silent.mp4')

