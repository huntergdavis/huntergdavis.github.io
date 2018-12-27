---
layout: post
title: Aliosa27's new Z2 image with X, Audio, and KEYMOUSE
date: '2009-09-20 10:53:57'
---


Aliosa27 continues his trend of FANTASTIC progress read on below  
  
 Continued from the last article post, from Aliosa27>>>

Here you go All..

For the ones that want a mouse with there existing images, note that you need  
 the uinput module and the evdev module .

If your running 2.6.29-r2 then here are the links

[http://oracle.aliosa27.net/zipit2/ipk/zipit2/kernel-module-uinput_2.6.29-r2.3_zipit2.ipk](http://oracle.aliosa27.net/zipit2/ipk/zipit2/kernel-module-uinput_2.6.29-r2.3_zipit2.ipk)

[http://oracle.aliosa27.net/zipit2/ipk/zipit2/kernel-module-evdev_2.6.29-r2.3_zipit2.ipk](http://oracle.aliosa27.net/zipit2/ipk/zipit2/kernel-module-evdev_2.6.29-r2.3_zipit2.ipk)

you will want them to load on boot..

Xorg will need the evdev driver. if your running any of the images I have posed then you allready have this.

Here is the link to a new image with audio,X,sound, and mouse supported.  
[http://aliosa27.net/projects/zipit2/zipit2-audio+x+mouse.gz](http://aliosa27.net/projects/zipit2/zipit2-audio+x+mouse.gz)

and here is a link to the userspace mouse driver.

[http://aliosa27.net/projects/zipit2/z2mouseemu](http://aliosa27.net/projects/zipit2/z2mouseemu)

does not fork so you will want to add it to your x startup script with an &

There is no config options at this point , there will at some point…  
 It is pretty basic, works for my needs…

dpad is mapped to mouse events  
 the center button,and the stop button are the 2 mouse buttons.

you can drag and whatnot as well….

One issue/2 issues to note are, keymapping is way of for number keys/etc// working on that today..and you only have basic up down left right controls on the mouse…..

Enjoy(more to come)


