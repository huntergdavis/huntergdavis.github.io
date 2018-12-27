---
layout: post
title: Re-Writing the laser pointer paint program (image processing) in C/C++ - 10x
  speed improvement
date: '2007-12-19 16:45:02'
---


 This should significantly increase our capture and processing speed. First, install libcv1 in ubuntu, I like to get the documentation and python bindings as well, and these will install libcv1 anyway. ` sudo aptitdue install python-cv opencv-doc ` Now we’ll start writing some C code. As I have the benefit of writing this article after the code, I know that one can render/display 30fps without processing, and can render/display without lag with processing as well (thank you compiled code!). You can compile opencv code in linux using the following command:

`gcc `pkg-config --cflags opencv` `pkg-config --libs opencv` -o MY_PROJECT_RUNME MY_PROJECT.cpp`

Well that’s simple enough. The structure of the program has a few changes.

1. Program takes first command line argument as the image filter size (try 2-10 for good results)
2. Program no longer does image subtraction for a mask over the image, it’s direct processing now
3. Program is significantly (10x) faster, depending on speed of camera frame grabs
4. Check out the openCV tutorial for grabbing images from a camera, then check out the code below..
5. You can snag it [here](http://www.hunterdavis.com/cam.cpp)
6. Also, please note that ‘escape’ will end the loop and finish the program


