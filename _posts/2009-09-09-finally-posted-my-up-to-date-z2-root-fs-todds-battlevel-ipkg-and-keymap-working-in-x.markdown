---
layout: post
title: 'Updated* Follow thread for new packages and images!: MyAliosa27''s up to date
  Z2 root FS, Todd''s battlevel ipkg and keymap working in X'
date: '2009-09-09 14:04:38'
---


So I finally sanitized my root fs and managed to get it down to about 200 megs, grab it [here](http://www.hunterdavis.com/zipit.tgz).  
 Todd got the correct keymap working in X, grab it[ here](http://www.hunterdavis.com/todd-zipit.tgz)  
 Todd built a battlevel ipkg , grab it[ here](http://www.hunterdavis.com/battlevel_1.0-r2.3_armv5te.ipk) (From Todd: “To get the battery meter to work I had to manually create some inodes, with: mknod /dev/i2c-0 c 89 0”)

Untar this to the root of your sd card. Log in as root, lots of .sh launch scripts in the root homedir. Sorry for the size but there are LOTS of packages installed. Like thousands, java, fluxbox, enlightenment, gpe, xorg, kdrive, firefox fceu, scummvm, etc etc. You’ll want to set up a swapfile and copy over your wireless modules as described on the wiki. GTK applications won’t have font’s rendered correctly, so you’ll want to grab sweetlilmre’s xorg packages or the angstrom ones like Todd did to get that going. Same with sound. Hopefully this should keep you busy till we post a fresh image with those already working. Sweetlilmre working on a new fluxbox image with sound etc, so we’re all looking forward to that too.


