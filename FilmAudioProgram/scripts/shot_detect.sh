#!/bin/bash

# script that breaks a video into shots and returns an xml with details
# furthermore it retains details and writes them to a txt file

cd /Users/Mitali/Desktop/Shotdetect/build

./shotdetect-cmd -i /Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos/$1.mp4 -o /Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos -s 60 -w -v -f -l -m -r -a $1

cd /Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos/$1/shots





