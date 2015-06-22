/* Mitali Dargani - Individual Project 2014-2015 - Film Audio Program */

Main repository for the Film Audio Program.

- A program that takes a short video file as input, analyses the scenes in the file
and appropriately inserts a score for each scene.

To build, you require the following dependencies:

    - Python (v2.7)
    - OpenCV
    - Ffmpeg (v2.6.2)
    - NumPy
    - MatPlotLib
    - Bash
    - Nose (for testing)
    - Youtube-dl (for extracting YouTube videos)
    
To run program:

    cd fmp/FilmAudioProgram/video
    
    python main.py -v input.mp4 
    
    OR
    
    python main.py -y http://www.youtube.com/My_URL
    
Bulk of code is in fmp/FilmAudioProgram/video/processing

Sound bank and themes can be found in fmp/FilmAudioProgram/audio/bank


List of contributors:

    - Mitali Dargani


