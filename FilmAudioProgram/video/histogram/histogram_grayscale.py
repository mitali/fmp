'''
Created on May 13, 2015

@author: Mitali
'''

from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# set up argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load img
image = cv2.imread(args["image"])
cv2.imshow("image", image)

# convert img to grayscale, create histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
plt.plot(hist)
plt.xlim([0, 256])

plt.show()


