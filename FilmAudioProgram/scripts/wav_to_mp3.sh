#!/bin/bash

# A script that takes in the scene genre/mood as an argument, chooses a random file from
# the folder of sounds and if it is not in mp3 format then converts it to mp3.

dir_head='/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/audio/bank'

# change to directory where sounds are stored - variable 1 from command line TODO: randomise files in directory
cd $dir_head/$1

# get random file from directory - gshuf relies on coreutils. just shuf in linux
rand_filename=$(find . -iname "*.wav" -print | gshuf -n 1)
rand_filename=${rand_filename:2} # strip first 2 characters ./
rand_filename=${rand_filename%%.*} # parse name out to remove suffix

# echo $rand_filename

# check mp3 file doesn't already exist
if [ ! -f "$dir_head/$rand_filename.mp3" ]; 
	then 
	
	# convert .wav to .mp3 and store in audio folder of project
	ffmpeg -i $rand_filename.wav -vn -ar 44100 -ac 2 -ab 192k -f mp3 $dir_head/$1/$rand_filename.mp3;

fi

#rm $rand_filename.wav

# wait 10 secs for any errors on terminal
sleep 10