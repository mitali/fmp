#!/bin/bash

youtube-dl "https://www.youtube.com/watch?v=MAj2h9-ZA_8" -o hogayapyar.mp4

ffmpeg -i hogayapyar.mp4 -an -vcodec copy hogayapyar_silent.mp4
