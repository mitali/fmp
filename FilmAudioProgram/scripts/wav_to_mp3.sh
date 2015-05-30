#!/bin/bash

# change to directory where sounds are stored - TODO: Change this
cd /Users/Mitali/Desktop/IndividualProject/fmp_sounds

# command to convert .wav to .mp3 and store in audio folder of project
ffmpeg -i frogs.wav -vn -ar 44100 -ac 2 -ab 192k -f mp3 /Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/audio/tests/frogs.mp3

# wait 10 secs for any errors on terminal
sleep 10