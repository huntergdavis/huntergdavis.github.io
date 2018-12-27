---
layout: post
title: New Video - HULU on the Zipit Z2
date: '2009-09-28 19:57:07'
---


And not just HULU, anything that you can dynamically transcode and serve on the network, you can watch or listen to on the Z2. 30 rock on the Zipit Z2? Oh YES THANKS. Instructions after the jump.

<object height="344" width="425"><param name="movie" value="http://www.youtube.com/v/yJzGlgaymZc&hl=en&fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed allowfullscreen="true" allowscriptaccess="always" height="344" src="http://www.youtube.com/v/yJzGlgaymZc&hl=en&fs=1" type="application/x-shockwave-flash" width="425"></embed></object>

Though this has been possible from the first image posted, I only today finally sat down and set it all up. Essentially, you are going to transcode audio or video on the fly to the Z2 using a windows or linux computer.

1. First, setup your transcoder machine. For the most part this is beyond the scope of this guide, but I’ll give a windows example
2. For the windows users, I recommend TVersity. It’s free to try for as long as you like, and they are really good to their customers
3. Setup your data sources, In TVersity add your HULU/youtube username (for your online video queues) and any audio/video folders you wish
4. Now setup the transcoder, for TVersity set the maximum video and image size to be 320×240. In the general settings, set your playback device to be mpeg1/2 device, and set the port for the web interface (and if you’re really lazy, set your port to be 80)
5. On your trancoding machine, obtain the ip address (ipconfig (windows) / ifconfig(linux)
6. If you want to stream your files over the net, forward incoming connections to the ip/port combination above on your external router
7. Now, on the Z2 create a script with the following contents  
```
<br></br>
#/bin/sh<br></br>
mplayer -vo fbdev -vf rotate=2 -bandwidth 100000 %1<br></br>```
8. This tells mplayer to rotate the framebuffer (who wants the overhead of X11 or flux…) 90 degrees ccw (non-flipped) and limit the bandwidth to 100k
9. Connect your zipit to your wireless network, and use dillo or links etc to browse to the ip address of your server
10. Browse to the audio or video file you wish to watch, and copy that shortcut (or output to file). You may want to just wget/grep for the shortcut if you are comfortable on the command line
11. Pass the shortcut (or paste it into a script, etc) into the script you created earlier.
12. Voila! Streaming Audio/Video etc on the Z2 in great quality! Bet you didn’t think it’d do that eh? If you’re feeling adventurous, you can set the link handler for dillo or fennec to open the script and be fully GUI


