#!/bin/bash

# Script that takes scene length, a random mp3 file within the given genre and loops the mp3 file enough times
# to match the scene length.

# need video info for scene length
dir_head='/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos'

# directory containing audio files
audio_dir='/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/audio/bank'
loop_dir=$audio_dir/$1/looped

echo $loop_dir

cd $audio_dir/$1

# get random file from directory - gshuf relies on coreutils. just shuf in linux
rand_filename=$(find . -iname "*.mp3" -print | gshuf -n 1)
rand_filename=${rand_filename:2} # strip first 2 characters ./
rand_filename=${rand_filename%%.*} # parse name out to remove suffix

echo $rand_filename

#echo $audio_dir/$1/$rand_filename.mp3

# extract line with length of audio clip
#ffmpeg -i 'path/to/original.mp3' 2>&1 | grep 'Duration:' > audio_len_tmp.txt
ffprobe -i $audio_dir/$1/$rand_filename.mp3 -show_entries format=duration -v quiet -of csv="p=0" > audio_len_tmp.txt

# al = parsed length of audio clip from temp file
# typeset -i before cat
al_init=$(cat audio_len_tmp.txt)

al=$(printf "%.0f" $al_init) 

# sl = assume/get length of scene in seconds - TODO: Add scene functionality
sl=111 # temporary

# determine number of loops required by
# loops = sl/al + 2 (2 extra in case. 1 might be required anyway)
loops=$(((sl/al)+2))

echo $loops

# create temporary file
> list_tmp.txt

# create temp file with list of repeated audio path
for i in $(eval echo "{1..$loops}")
do 
	echo -e "file $audio_dir/$1/$rand_filename.mp3"
done >> list_tmp.txt

# ffmpeg command to concat list
ffmpeg -t $sl -f concat -i list_tmp.txt -c copy -t $sl $loop_dir/${rand_filename}_looped.mp3
#ffmpeg -f concat -i list_tmp.txt -c copy ${rand_filename}_looped.mp3

# delete temp files
rm audio_len_tmp.txt
rm list_tmp.txt

# wait 10 secs for any errors on terminal
sleep 10