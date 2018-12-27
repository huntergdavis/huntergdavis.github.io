---
layout: post
title: Dosbox for Zipit Z2!
date: '2008-12-13 12:47:44'
tags:
- zipit-dosbox-games-hacking-fun-c-source-hack
---


[![Pools of Radiance](http://66.147.244.180/~hunterda/content/images/2008/12/poolrad1.jpg)](http://66.147.244.180/~hunterda/content/images/2008/12/poolrad1.jpg "Pools of Radiance")

It turns out that with a bit of source code modification, you can get dosbox running quite well on your zipit z2!! This is HUGE for me, as I’m currently reliving my youth with a Pools of Radiance campaign on my z2! For those impatient to try it out, DL the openembedded ipkg and modified source files at the end of this post.

**Enabling Swap**  
 Follow the directions [here](http://www.redhat.com/docs/manuals/linux/RHL-8.0-Manual/custom-guide/s1-swap-adding.html) for adding a swap file. I recommend a good 64 meg chunk. This will keep dosbox from segfaulting when it searches for available memory.

**Modifying Sources**  
 Head into your dosbox source directory (or the dosbox/src directory in your OE bitbake tree) and do a  
`"grep -r "640" ./* "`.  
 This will return all the source files containing video mode switches. You’re going to want to change all the SDL function calls from 640,480 to 320,240.

**Installing Dosbox**  
 Bitbake your new dosbox and install prerequisites. You’re going to need a whole mess of SDL libraries like sdl-net sdl-image sdl-x11 etc. My usual routine is:  
```
 (bitbake host) bitbake (package name) && bitbake package-index<br></br>
 (z2) ipkg update && ipkg install dosbox<br></br>
  if #2 complains, replace (package name) in #1 with missing package```
  
**  
 Editing Dosbox config and startup**  
 By default dosbox will enable a number of options that are not conducive to use on the zipit z2. Luckily you can pass the dosbox config file location to it on startup. I start dosbox straight from the command prompt, as opposed to from an xterm window. It saves about 1/2 meg memory, and every little bit helps. I start dosbox with the standard xfbdev script ala:  
```
export DISPLAY=:0.0<br></br>
Xfbdev -screen 240x320@90 -hide-cursor -br &<br></br>
dosbox  -conf ./.dosboxconf```

My dosbox.conf is attached with the code below, but at minimum you’ll need to set the following option to enable the arrow keys:  
`usescancodes=false`

And that should get you going. The initial dosbox window will be larger than your display, and the cursor may be scrolled off screen. This will be resolved when you start a game, but I like to add the game start commands to the dosboxconf as below:  
```
<br></br>
[autoexec]<br></br>
# Lines in this section will be run at startup.<br></br>
mount c /home/root/<br></br>
c:<br></br>
cd poolrad<br></br>
start```

And that’s that! You can download the updated source code and ipkg files here.  
[dosbox modified sources and configs](http://hunterdavis.com/content/images/2008/12/dosboxtar.gz "dosbox modified sources and configs")


