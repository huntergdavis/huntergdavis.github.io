---
layout: post
title: ScummVM and Monkey Island working on Zipit Z2
date: '2009-08-16 19:08:48'
---


New Zipit Update! I’ve gotten ScummVM working with the new kernel. Xserver-kdrive too, so our memory usage is down again.  
![Scummvm Selector](http://66.147.244.180/~hunterda/content/images/2009/08/scummvm-selector1.jpg)  
  
 You’ll need to edit your .scummvmrc file and add the game entries by hand (I still don’t have the keys as joystick or mouse in), but they play fine. Update your git tree and remove the zipit temp directory, Bitbake intltool, then bitbake xserver-kdrive. Intltool will fail unless you bitbake it directly, and not as a dependency include. Set the graphics scale to 1x and everything is gravy. Screenshots of the Scummvm selector screen and the Monkey Island EGA DRM scheme are below. This is running even better than the dosbox build as there’s not x86 conversion happening!

![Monkey Island Starting Up](http://66.147.244.180/~hunterda/content/images/2009/08/monkeyislandstartup1.jpg)  
![Monkey Island DRM scheme](http://66.147.244.180/~hunterda/content/images/2009/08/monkeyisland-drm1.jpeg)


