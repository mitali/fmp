'''
Created on May 5, 2015

@author: Mitali
'''

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/Mitali/Desktop/IndividualProject/InterimReport/img1.jpg', 0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # hide tick values on X and Y axis 
plt.show()