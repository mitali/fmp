#!/bin/bash

# Script that takes in two arguments, first one being the genre of the scene and the second being the video name
# and merges the audio with the video file assuming they have identical length (need to add a check for this)

# arguments are: genre, video

# change to directory where videos are stored
dir_head='/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/audio/bank'
video_dir='/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos'

cd $dir_head/$1/looped # go to directory for specific genre

# get random file from directory - gshuf relies on coreutils. just shuf in linux
rand_filename=$(find . -iname "*.mp3" -print | gshuf -n 1)
rand_filename=${rand_filename:2} # strip first 2 characters ./
rand_filename=${rand_filename%%.*} # parse name out to remove suffix

echo $rand_filename

# merge pre-looped audio with video file
#ffmpeg -i $video_dir$2.mp4 -i $rand_filename.mp3 -c copy -map 0:0 -map 1:0 $2_processed.mp4
ffmpeg -i $video_dir/$2_silent.mp4 -i $rand_filename.mp3 -c copy -map 0:0 -map 1:0 $video_dir/$2_processed.mp4

rm $video_dir/$2_silent.mp4

# wait 10 secs for any errors on terminal
#sleep 10