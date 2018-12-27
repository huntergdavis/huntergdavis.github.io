---
layout: post
title: Z2 quickie video followup - (debian) Bomberclone running (with sound, SDL ,etc)
  on the Z2
date: '2009-10-03 11:10:34'
---


Just a quick followup to the debian image video.

<object height="344" width="425"><param name="movie" value="http://www.youtube.com/v/2re-2xClC0M&rel=0&color1=0xb1b1b1&color2=0xcfcfcf&feature=player_profilepage&fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowScriptAccess" value="always"></param><embed allowfullscreen="true" allowscriptaccess="always" height="344" src="http://www.youtube.com/v/2re-2xClC0M&rel=0&color1=0xb1b1b1&color2=0xcfcfcf&feature=player_profilepage&fs=1" type="application/x-shockwave-flash" width="425"></embed></object>

  
 Bomberclone is in the debian repository. It loads, but at 640×480. <del datetime="2009-10-04T07:23:53+00:00">You can change this in the source code and re-compile if you wish, however it’s still (mostly) playable at 640</del> Just edit .bomberclone.cfg and change the xres to 320 and yres to 240!! Works perfect and netplay! Wormux installs but fails to fully load at 640×480 as well. Haven’t looked into the source yet, probably have to replace the sdl-render options like with dosbox last year.  
 Note*  
 If you are having trouble with the mouse/keyboard in flux, download aliosa27’s z2mouse-option and keymap.map files and add them to the /bin/startfluxbox script as mentioned in the comments thread for the debian image tutorial.


