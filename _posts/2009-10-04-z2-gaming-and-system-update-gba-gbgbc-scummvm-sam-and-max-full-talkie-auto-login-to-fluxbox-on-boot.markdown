---
layout: post
title: Z2 gaming and system update - GBA, GB/GBC, ScummVM (Sam and Max/Full Throttle
  Full Talkie), auto-login to Fluxbox on boot
date: '2009-10-04 17:24:27'
---


So now that the Z2 is running debian and everything is working, it’s really easy to install new programs and emulators. They are even automatically added to the fluxbox right-click mouse menu. I haven’t changed or recompiled a single C file this time, this is fully “general public” ready! Here’s what I’ve been playing with this weekend.

<object height="344" width="425"><param name="movie" value="http://www.youtube.com/v/CVMef5P02z8&hl=en&fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed allowfullscreen="true" allowscriptaccess="always" height="344" src="http://www.youtube.com/v/CVMef5P02z8&hl=en&fs=1" type="application/x-shockwave-flash" width="425"></embed></object>

  
 Before we get to the fun stuff, let’s set up fluxbox to start (no more console login required)

1. edit a file called /etc/init.d/flux
2. the contents of this script should read  
```
<br></br>
#!/bin/sh<br></br>
su root -c startx<br></br>```
3. now just: `update-rc.d flux defaults`
4. Fluxbox should now start up on boot!

- VisualBoyAdvance (GBA) runs about 10% speed with gba roms, 70% speed with gb/gbc roms. I’m guessing a straight gb/gbc emulator may run 100%
- Scummvm runs perfectly with sound, movies, voice, everything!! when you set scale=1x in the .scummvmrc 1. Monkey Island 2 – 100% perfect
2. Full Throttle – 100% perfect!
3. Zak McKracken – 100% perfect
4. Beneath a Steel Sky – 100% perfect
5. Flight of the Amazon Queen – 100% perfect
6. Indiana Jones and the Fate of Atlantis – 100% perfect
7. Indiana Jones and the last Crusade – 100% perfect
8. Maniac Mansion – 100% perfect
9. Simon the Sorceror 2 – Full CD Talkie – 100% perfect
10. Sam and Max hit the road – Full CD Talkie – 100% perfect


