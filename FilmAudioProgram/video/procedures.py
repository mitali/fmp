'''
Created on May 27, 2015

@author: Mitali
'''

from processing.extract_frames import breakdown
#from processing.save_shot import save_shot_details
from processing.bash_script import call_bash_script

#tmp
from processing.bash_script import call_bash_script_2_args

### ----------------- WRAPPERS TO BE USED IN MAIN -------------------

# removes audio from video
def strip_audio(video):   
    call_bash_script(video, "strip_audio_specific.sh")
    return

# takes a video and breaks it down into frames - TODO: fix
def breakdown_video(video):
    breakdown(video)
    return

# takes a video and breaks it into shots
def shot_breakdown(video):
    call_bash_script(video, "shot_detect.sh")
    return

# saves shot details in array & calculates length per shot saved in diff array
def save_shots(video):
    #save_shot_details(video)
    return
    
# loops over frames and plots histograms 
def plot_histogram(self):
    return

# takes 2 histograms and compares them
def compare_histograms(self):
    return
    
# determines most dominant colour in frame, 2nd most and 3rd most dominant 
# (e.g. green, blue, red)
def colour_distrib(self):
    return
    
# takes dominant colour and assigns mood category to frame
def scene_mood(self):
    return
    
# takes mood and chooses soundtrack
def choose_audio(self):
    return;
    
# loops soundtrack according to scene length
def loop_by_length(self):    
    return
    
# inserts looped soundtrack in scene + outputs new video
def insert_audio(self):
    return

# temporary procedure that takes video length, loops audio accordingly +
# inserts
def tmp(video):
    call_bash_script("nature", "loop_audio.sh")
    call_bash_script_2_args("nature", video, "insert_audio_in_mp4.sh")

### ---------------------------------------------------------------
    