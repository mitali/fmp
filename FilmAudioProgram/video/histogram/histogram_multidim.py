'''
Created on May 13, 2015

@author: Mitali
'''

from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("image", image)

chans = cv2.split(image)
# colors = ("b", "g", "r")
# plt.figure()
# plt.title("'Multidimensional' Color Histogram")
# plt.xlabel("Bins")
# plt.ylabel("No. of Pixels")
# features = []

fig = plt.figure()

# plot 2D colour histogram for green and blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0,1], None
                    [32,32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for Green and Blue")
plt.colorbar(p)

# plot 2D colour histogram for green and red
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0,1], None,
                     [32, 32], [0,256,0,256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for Green and Red")

# plot 2D colour histogram for blue and red
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,
    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for Blue and Red")
plt.colorbar(p)
 
# finally, let's examine the dimensionality of one of
# the 2D histograms
print "2D histogram shape: %s, with %d values" % (
    hist.shape, hist.flatten().shape[0])

