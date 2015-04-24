__author__ = 'Mitali'

import cv2
import numpy as py
import sys

sys.path.append('/usr/local/lib/python2.7/site-packages')

Mat A, C

A = imread(argv[1], CV_LOAD_IMAGE_COLOR)

Mat B(A)

C = A


