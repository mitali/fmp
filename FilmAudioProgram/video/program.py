'''
Created on May 27, 2015

@author: Mitali
'''

import argparse
import subprocess
import os

from processing.extract_frames import breakdown

scripts_dir = '/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/scripts/'

# function that removes audio from video
def strip_audio(video):
    directory = scripts_dir + "strip_audio_specific.sh"
    os.chmod(directory, 0o755)
    command = directory + " " + video
    subprocess.Popen([command], shell=True, executable="/bin/bash")
    return;

# function that takes a video and breaks it down into frames - TODO: fix
def breakdown_video(video):
    breakdown(video)
    return;

# function that takes a video and breaks it into shots
def shot_breakdown(video):
    return;
    
# function that loops over frames and segments them/plots histograms 
def segment(self):
    return;
    
# function that determines most dominant colour in frame, 2nd most 
#     and 3rd most dominant (e.g. green, blue, red)
def dominant_colours(self):
    return;
    
# function that takes dominant colour and assigns mood category to frame
def scene_mood(self):
    return;
    
# function that takes mood and chooses soundtrack
def choose_audio(self):
    return;
    
# function that determines length of a scene and stores it (using segmentation)
def scene_length(self):
    i = 3
    return i;
    
# function that loops soundtrack according to scene length (ffmpeg)
def loop_by_length(self):    
    return;
    
# function that inserts looped soundtrack in scene + stores new video
def insert_audio(self):
    return;
    
# function that outputs final video
def output(self):
    return;
    
#################################################################

# get path to video from argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "Input path to the video")
args = vars(ap.parse_args())
input_video = args["video"]

# remove audio from input file
strip_audio(input_video)

# break video file down into frames
shot_breakdown(input_video)

