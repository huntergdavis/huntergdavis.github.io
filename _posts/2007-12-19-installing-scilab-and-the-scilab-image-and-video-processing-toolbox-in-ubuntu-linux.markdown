---
layout: post
title: Installing scilab and the scilab image and video processing toolbox in ubuntu
  linux.
date: '2007-12-19 16:36:03'
---


For some time now I’ve been into computer vision. However, much of computer vision is done on matlab, a 1000$ piece of software that doesn’t jive with my open source philosophy. Luckily, there are a number of open source alternatives. I prefer scilab, though octave is a good alternative. However, scilab has the advantage of an open source video toolbox. In this first article, I’ll show you how to setup scilab, opencv (the intel open computer vision library), and the sivp toolbox. Then we’ll verify its working by processing video from an avi file or in this case, a live webcam stream.

1. First, lets start by installing scilab and preparing our system to compile ffmpeg and opencv
`sudo aptitude install scilab`

3. Now follow [this](http://dircweb.king.ac.uk/reason/opencv_cvs.php#Feisty) guide to get opencv and ffmpeg compiled. Remember to make sure ffmpeg, v4l, and v4l2 are compiled options, or we’ll be unable to process video, webcam, or newer webcam video
4. Now head on over to the SIVP [webpage](http://sivp.sourceforge.net/doc.php) and follow the typical `./configure && make && sudo make install`
5. At this point we should have video streaming in scilab. Fire up scilab from the command line `scilab`
6. Here, we’ll want to make sure the video/image toolbox is loaded. Hit the toolbox menu, then the sivp toolbox. You should get a message about it being loaded
7. Now, hit the examples button, and make sure your main scilab window stays open. From here click the sivp section, and we can grab straight from a videocam, image, video etc.
8. The best part about the examples is the (very simple) code is displayed in your main scilab window, very cool!

From here the sky is the limit!


