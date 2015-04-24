__author__ = 'Mitali'

import cv2

video_capture_object = cv2.VideoCapture(0)
should_i_stop = input("Type False when you want me to stop recording you.\n")

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while True:
    if(should_i_stop):
        # capture frame by frame
        ret, frame = video_capture_object.read()

        # frame operations
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        video_capture_object.release()
        cv2.destroyAllWindows()
        break