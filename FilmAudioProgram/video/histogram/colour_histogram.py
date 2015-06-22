'''
Created on Jun 3, 2015

@author: Mitali
'''

# plot a colour histogram for an image in RGB space

import cv2
import numpy as np
from matplotlib import pyplot as plt

#392
img = cv2.imread('../frames/frame390.jpg', -1)
cv2.imshow('cartriges', img)

color = ('b', 'g', 'r')
for channel,col in enumerate(color):
    histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
plt.title('Histogram for colour scale picture')
plt.show()
plt.savefig("histogram392")

while True:
    k = cv2.waitKey(0) & 0xFF
    if k==27: break
    
cv2.destroyAllWindows()
