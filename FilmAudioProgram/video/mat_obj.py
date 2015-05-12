'''
Created on May 11, 2015

@author: Mitali
'''

import cv2
import numpy as np

size = 200, 200, 3
m = np.zeros(size, dtype=np.uint8)
#m = cv2.cvtColor(m, cv2.COLOR_GRAY2BGR)

p1 = (0,0)
p2 = (200,200)
cv2.line(m, p1, p2, (255, 0, 0), 10)

cv2.namedWindow("draw", cv2.CV_WINDOW_AUTOSIZE)

while True:
    cv2.imshow("draw", m)
    
    ch = 0xFF & cv2.waitKey(1)
    
    if ch == 27:
        break;
    
cv2.destroyAllWindows()