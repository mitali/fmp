/* Mitali Dargani - Individual Project 2014-2015 - Film Music Program */

Main repository for the Film Music Program.

- A program that takes a short video file as input, analyses the scenes in the file
and appropriately inserts a score for each scene.

To build, you require the following dependencies:

    - Python v2.7
    - OpenCV
    - Ffmpeg
    - NumPy
    - MatPlotLib
    - Bash
    - Nose (for testing)

In order to remove audio from video file, execute following command:

    ffmpeg -i input.flv -an -vcodec copy output.flv

List of contributors:

    - Mitali Dargani



