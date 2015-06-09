'''
Created on Jun 9, 2015

@author: Mitali
'''

import argparse
import sys
import program

### -------------------------  MAIN PROGRAM -------------------------

# get path to video from argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "Input path to the video")
args = vars(ap.parse_args())
input_video = args["video"]

# remove audio from input file
program.strip_audio(input_video)

# break video file down into frames
program.shot_breakdown(input_video)

sys.exit(0)