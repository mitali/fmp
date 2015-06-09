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

# grab img channels, initialize tuple of colors, fig and flattened feature vect
chans = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
features = []

# loop over img channels
for(chan, color) in zip(chans, colors):
    # create histogram for curr. channel and concatenate resulting hist for each
    # channel
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    features.extend(hist)
    
    # plot hist
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
    
plt.show()
    
print "flattened feature vector size: %d" % (np.array(features).flatten().shape)
