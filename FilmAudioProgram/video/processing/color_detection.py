'''
Created on May 13, 2015

@author: Mitali
'''

import numpy as np
import cv2
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])

# define the list of boundaries according to BGR
boundaries = [
              ([17, 15, 100], [50, 56, 200]),
              ([86, 31, 4], [220, 88, 50]),
              ([25, 146, 190], [62, 174, 250]),
              ([103, 86, 65], [145, 133, 128])
              ]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create numpy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    
    # find the colours within specified boundaries & apply mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    
    # show images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)