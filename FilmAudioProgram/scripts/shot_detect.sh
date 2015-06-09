#!/bin/bash

# script that breaks a video into shots and returns an xml with details
# furthermore it retains details and writes them to a txt file

# takes just name of file as input (no .mp4 or full directory)

cd /Users/Mitali/Desktop/Shotdetect/build

./shotdetect-cmd -i /Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos/$1.mp4 -o /Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos -s 60 -w -v -f -l -m -r -a $1

curr_dir=/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos/$1/shots

cd $curr_dir

> shots_file.txt

for filename in *.jpg
do

  # break filename into significant bit, frame no. & start/finish time
  sig=$(echo "$filename" | cut -d'_' -f2)
  sig=${sig//-/' '}

  echo $sig >> shots_file.txt

done

echo "left loop"





