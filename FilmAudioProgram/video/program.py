'''
Created on May 27, 2015

@author: Mitali
'''

import subprocess

class program:

    # 1. function that takes a video and breaks it down into frames
    def breakdown_video(self):
        return;
    
    # 2. function that loops over frames and segments them 
    def segment(self):
        return;
    
    # 3. function that determines most dominant colour in frame, 2nd most 
    #     and 3rd most dominant (e.g. green, blue, red)
    def dominant_colours(self):
        return;
    
    # 4. function that takes dominant colour and assigns mood category to frame
    def scene_mood(self):
        return;
    
    # 5. function that takes mood and chooses soundtrack
    def choose_audio(self):
        return;
    
    # 6. function that determines length of a scene and stores it (using segmentation)
    def scene_length(self):
        i = 3
        return i;
    
    # 7. function that loops soundtrack according to scene length (ffmpeg)
    def loop_by_length(self):
        
        return;
    
    # 8. function that inserts looped soundtrack in scene + stores new video
    def insert_audio(self):
        return;
    
    # 9. function that outputs final video
    def output(self):
        return;
    
    #################################################################