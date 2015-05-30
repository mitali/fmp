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

In order to extract and return audio from video file:
ffmpeg -i filename.mp4 filename.mp3

In order to remove audio from video file, execute following command:

    ffmpeg -i input.flv -an -vcodec copy output.flv
    
In order to extract a video file and save it in mp4 format, execute (e.g.):

    youtube-dl -o videos/coyote.mp4 'https://youtu.be/b5cVYeeMzGI'
    
In order to crop a video file from minute 10.50 to 12.50

    ffmpeg -i mr_bean.mp4 -ss 00:10:50.00 -c copy -t 00:02:00.00 mr_bean_clip.mp4
    
In order to concatenate multiple mp3 files:

    ffmpeg -i concat:"file1.mp3|file2.mp3|file3.mp3|..." -codec copy output.mp3
    
In order to convert .wav to .mp3

    ffmpeg -i input.wav -vn -ar 44100 -ac 2 -ab 192k -f mp3 output.mp3
    
In order to add audio to a video

    ffmpeg -i input.mp4 -i input.mp3 -c copy -map 0:0 -map 1:0 output.mp4

List of contributors:

    - Mitali Dargani



