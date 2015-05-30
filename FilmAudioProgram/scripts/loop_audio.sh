#!/bin/bash

# change to directory where videos are stored - TODO: Change this
cd /Users/Mitali/Desktop/IndividualProject/fmp_sounds

# extract line with length of audio clip

#ffmpeg -i 'path/to/original.mp3' 2>&1 | grep 'Duration:' > audio_len_tmp.txt
ffprobe -i path/to/original.mp3 -show_entries format=duration -v quiet -of csv="p=0" > audio_len_tmp.txt

# al = parsed length of audio clip from temp file
al = typeset -i variable=$(cat audio_len_tmp.txt) 

# sl = assume/get length of scene
sl = 10 # temporary

# determine number of loops required by
# loops = sl/al + 2 (2 extra in case. 1 might be required anyway)
loops = ($sl/$al) + 2

# create temp file with list of repeated audio path
for i in {1..$loops}; do echo -e "path\n"; done > list_tmp.txt

# ffmpeg command to concat list
ffmpeg -t $sl -f concat -i list_tmp.txt -c copy -t $sl output.mp3

# delete temp files
rm audio_len_tmp.txt
rm list_tmp.txt

# wait 10 secs for any errors on terminal
sleep 10