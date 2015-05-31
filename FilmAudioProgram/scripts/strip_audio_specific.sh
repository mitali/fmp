#!/bin/bash

cd /Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos

# strip audio from video file and return this
ffmpeg -i $1.mp4 -an -vcodec copy $1_silent.mp4