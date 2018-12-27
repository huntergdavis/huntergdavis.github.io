---
layout: post
title: Zipit Z2 New Kernel Update!
date: '2009-06-20 16:40:59'
tags:
- zipit-dosbox-games-hacking-fun-c-source-hack
---


The short story: The flash worked and I’ve got everything working that worked before. The long story?

![wireless+x image running on the z2](http://66.147.244.180/~hunterda/content/images/2009/06/z2angstrom1.jpg "z2angstrom")  
  
 Here’s what I did. This is the new sweetlilmre method  
 1. Headed over to http://sourceforge.net/projects/openzipit and downloaded the autoflasher, and the zipit z2 kernel.bin

2. renamed the z2-2.6.blahblah kernel to kernel.bin and copied to fat32 formatted SD

3. copied the z2flasher.zip to the same fat32 formatted SD and extracted it there

4. Booted the z2, waited till it rebooted itself

5. RE-formatted the SD card as EXT2

6. Svn co the package from here http://sourceforge.net/apps/mediawiki/openzipit/index.php?title=Getting_Started_with_Open_Embedded_and_the_Z2

7. as root, copied the ~/oe/zipit2-tmp/deploy/glibc/images/zipit2/Angstrom-wireless-image-glibc-ipk-2009.X-test-20090606-zipit2.rootfs.tar to the EXT2 SD card

8. on command line in the SD card root, I ‘sudo tar -xf Angstrom*.rootfs.tar .” to extract the wireless image (with x extensions)

That’s that! A really good starting point towards an emulation platform. Next up, getting snes9x working (it bitbaked fine, now to work on prerequisites)


