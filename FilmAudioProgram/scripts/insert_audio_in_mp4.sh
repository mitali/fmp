#!/bin/bash

# change to directory where videos are stored - TODO: Change this
cd /Users/Mitali/Desktop/IndividualProject/fmp_sounds

ffmpeg -i input.mp4 -i input.mp3 -c copy -map 0:0 -map 1:0 output.mp4

# wait 10 secs for any errors on terminal
sleep 10