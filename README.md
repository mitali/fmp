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

In order to remove audio from video file, execute following command:

    ffmpeg -i input.flv -an -vcodec copy output.flv
    
In order to extract a video file and save it in mp4 format, execute (e.g.):

    youtube-dl -o videos/coyote.mp4 'https://youtu.be/b5cVYeeMzGI'

List of contributors:

    - Mitali Dargani



