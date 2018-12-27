---
layout: post
title: New Video - From Stock Z2 to Fully Flashed with Audio, Fluxbox, Mouse, Aliosa27's
  Latest Userland
date: '2009-09-23 23:10:16'
---


Here is a video Mark and I made of the complete flashing and installation process, and a tour of the new userland features.  
<object height="344" width="425"><param name="movie" value="http://www.youtube.com/v/x_LrI2g2VT8&hl=en&fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed allowfullscreen="true" allowscriptaccess="always" height="344" src="http://www.youtube.com/v/x_LrI2g2VT8&hl=en&fs=1" type="application/x-shockwave-flash" width="425"></embed></object>  
  
 For those following along at home, the required setup artifacts are below. You will need

- Your zipit z2
- A linux computer with an internet connection (to download the packages below) and gparted installed
- A microSD card

Do you have everything ready? Let’s get to it!

1. Head over to http://sourceforge.net/projects/openzipit and downloaded the autoflasher
2. Download Aliosa27’s new kernel image and userland [here](http://aliosa27.net/projects/zipit2/zipit2-audio+x+mouse.gz)
3. Grab the latest mouse emu from [here](http://aliosa27.net/projects/zipit2/z2mouseemu)
4. Using Gparted, Format your microSD to a fat16 partition (I did 300 megs but you really need much less than 100
5. Extract the autoflasher to the fat16 partition
6. (as root)Extract the kernel + userland image somewhere on your pc
7. From the extracted files, copy out the ./boot/zImage-2.6.29 to the root of your microSD as kernel.bin
8. Boot the Z2 and allow it to flash and reboot to the new Linux logo
9. This will also make a copy of your original kernel and wifi firmware, copy them off the microSD somewhere safe
10. Using Gparted, Format the microSD into 2 new partitions, ext2 (the majority of the card) and swap (the remaining 256 megs)
11. Rename and copy the wifi firmware back to the Z2 as described [here](http://sourceforge.net/apps/mediawiki/openzipit/index.php?title=Getting_Started_with_Open_Embedded_and_the_Z2#WIFI_firmware)


