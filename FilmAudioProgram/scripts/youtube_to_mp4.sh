#!/bin/bash

# change to directory where videos are stored
cd /Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos

# extract from youtube URL the mp4 file and save into videos/ folder
youtube-dl $1

# wait 10 secs for any errors on terminal
sleep 10