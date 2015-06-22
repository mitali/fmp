'''
Created on Jun 9, 2015

@author: Mitali
'''

import argparse
import sys
import procedures

### -------------------------  MAIN PROGRAM -------------------------

# get path to video from argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "Input path to the video")
ap.add_argument("-y", "--youtube", help = "Input YouTube URL for the video")

args = vars(ap.parse_args())
    
if ap.video:
    
    input_video = args["video"]
    
    # remove audio from input file
    procedures.strip_audio(input_video)

    # break video file down into frames
    #program.shot_breakdown(input_video)

    # tmp call
    procedures.tmp(input_video)
    
elif ap.youtube:
    
    input_video = args["youtube"]
    procedures.youtube_convert(input_video)
    
else:
    
    print "Error: Please input an mp4 file or YouTube link"



sys.exit(0)
