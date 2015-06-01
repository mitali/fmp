#!/bin/bash

# change to directory where videos are stored
dir='/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos'

cd $dir

for filename in $dir/*.mp4; do

	name=${filename%%.*}

	# strip audio from video file and return this
	ffmpeg -i $name.mp4 -an -vcodec copy ${name}_silent.mp4
done

# wait 10 secs for any errors on terminal
sleep 10