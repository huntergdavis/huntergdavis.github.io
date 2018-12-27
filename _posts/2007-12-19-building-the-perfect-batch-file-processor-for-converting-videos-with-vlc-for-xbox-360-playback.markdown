---
layout: post
title: Building the Perfect Batch File Processor for Converting Videos with VLC for
  Xbox 360 playback.
date: '2007-12-19 16:06:05'
tags:
- xbox-360-conversion-software
---


[vlcwmvhgd.bat](http://hunterdavis.com/content/images/2007/12/vlcwmvhgd.bat "vlcwmvhgd.bat")This may not be useful anymore after the fall dashboard update, but for those who still have files the 360 can’t play, here’s a nice vlc batch script I wrote a while back.

I added in shift-looping (so you can drag as many files as you like to this bat file initially and let them run overnight), as well as adding the vlc:quit command to the vlc playlist after every file conversion. This ensures the vlc gui closes after encoding so the batch file can move on to the next video to encode w/o human interaction.


