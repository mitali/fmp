'''
Created on Jun 3, 2015

@author: Mitali
'''

import cv2
import numpy as np

# read 2 images and convert to HSV
img1 = cv2.imread('frames/frame300.jpg')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
img2 = cv2.imread('frames/frame392.jpg')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)

h = np.zeros((300,256,3))

bins = np.arange(256).reshape(256,1)
color = [(255,0,0),(0,255,0),(0,0,255)]

for ch, col in enumerate(color):
    hist_item1 = cv2.calcHist([img1],[ch],None,[256],[0,255])
    hist_item2 = cv2.calcHist([img2],[ch],None,[256],[0,255])
    
    cv2.normalize(hist_item1,hist_item1,0,255,cv2.NORM_MINMAX)
    cv2.normalize(hist_item2,hist_item2,0,255,cv2.NORM_MINMAX)
    
    sc = cv2.compareHist(hist_item1,hist_item2, cv2.cv.CV_COMP_CORREL)
    
    print sc
    
    hist = np.int32(np.around(hist_item1))
    pts = np.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)
    
h = np.flipud(h)
cv2.imwrite('my_histogram.png', h)