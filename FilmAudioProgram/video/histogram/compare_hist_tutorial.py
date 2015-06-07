'''
Created on Jun 5, 2015

@author: Mitali
'''

# this works!

#from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
#import numpy as np
import cv2
import argparse
import glob

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to directory of images")
args = vars(ap.parse_args())

index = {}
images = {}

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    filename = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)
    images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    hist = cv2.calcHist([image],[0,1,2],None,[8,8,8],
        [0,256,0,256,0,256])
    hist = cv2.normalize(hist).flatten()
    index[filename] = hist

OPENCV_METHODS = (("Correlation", cv2.cv.CV_COMP_CORREL),
                  ("Chi-Squared", cv2.cv.CV_COMP_CHISQR),
                  ("Intersection", cv2.cv.CV_COMP_INTERSECT),
                  ("Bhattacharyya", cv2.cv.CV_COMP_BHATTACHARYYA))

for (methodName, method) in OPENCV_METHODS:
    results = {}
    reverse = False
    
    if methodName in ("Correlation", "Intersection"):
        reverse = True
        
    for (k, hist) in index.items():
        d = cv2.compareHist(index["frame210.jpg"], hist, method)
        results[k] = d
        
    results = sorted([(v,k) for (k,v) in results.items()], reverse = reverse)
    
    fig = plt.figure("Query")
    ax = fig.add_subplot(1,1,1)
    ax.imshow(images["frame210.jpg"])
    plt.axis("off")
    
    fig = plt.figure("Results: %s" % (methodName))
    fig.suptitle(methodName, fontsize = 20)
    
    for (i, (v,k)) in enumerate(results):
        ax = fig.add_subplot(1,len(images),i+1)
        ax.set_title("%s: %.2f" % (k,v))
        
        plt.imshow(images[k])
        plt.axis("off")
        
plt.show()
    
    