'''
Created on May 5, 2015

@author: Mitali
'''

#import numpy as np
import cv2

#load img in grayscale
img = cv2.imread('/Users/Mitali/Desktop/IndividualProject/InterimReport/img1.jpg', 0)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('landscape_gray.png', img)