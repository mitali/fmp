'''
Created on Jun 9, 2015

@author: Mitali
'''

import os
import subprocess

# calls all bash scripts, given a video and script name. Makes them executable
# and then runs them

def call_bash_script(video, script_name):
    
    scripts_dir = '/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/scripts/'
    
    directory = scripts_dir + script_name
    os.chmod(directory, 0o755)
    command = directory + " " + video
    
    #subprocess.Popen([command], shell=True, executable="/bin/bash")
    subprocess.call(command, shell=True)
    
    return

def call_bash_script_2_args(genre, video, script_name):
    
    scripts_dir = '/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/scripts/'
    
    directory = scripts_dir + script_name
    os.chmod(directory, 0o755)
    command = directory + " " + genre + " " + video
    
    #subprocess.Popen([command], shell=True, executable="/bin/bash")
    subprocess.call(command, shell=True)
    
    return
