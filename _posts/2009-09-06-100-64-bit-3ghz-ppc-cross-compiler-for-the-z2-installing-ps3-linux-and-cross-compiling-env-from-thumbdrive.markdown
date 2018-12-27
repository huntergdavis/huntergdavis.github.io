---
layout: post
title: 100$ 64-bit 3ghz ppc cross compiler for the Z2 (Installing PS3 Linux and Cross
  Compiling Env from Thumbdrive)
date: '2009-09-06 20:26:36'
---


![ps3 ydl logo](http://66.147.244.180/~hunterda/content/images/2009/09/YDL-PS3-Logo1.jpg) I’ve been seeing a lot of PS3s come up on craigslist with broken optical drives, usually around 100$. Figuring this was a great way to free up my quadcore from mundane cross-compiling duty, I set about purchasing one and setting up the Z2 cross compiling environment. It took a bit of doing, but it works. Here’s a step by step guide for setting yours up.

I picked up an old 40gb ps3 with a broken optical drive for 100$. Everything else I had laying around. Here’s how I got the Z2 environment cross compiling.

1. I am using YDL 6.2. You can grab the newest 6.2 release from [here](http://mirror.anl.gov/yellowdog/iso/)
2. You’ll need a usb thumb drive formatted fat32 128mb or above to install the ng bootloader you can download [here](http://wiki.pdaxrom.org/index.php/Bootloader_for_PS3)
3. Youll need a usb thumb drive formatted ext3 4gb or above, or a 1gb thumb drive formatted ext3 with a way to share the iso over the network
4. On the fat32 thumb drive, create a directory structure /PS3/otheros/
5. Copy the ng bootloader.bld to /PS3/otheros/otheros.bld
6. Boot the PS3, go to settings->system settings, format system and split the drive up for your linux install
7. In the PS3 menu, go to settings->system settings, install other os and insert your fat32 thumb drive, this will install the ng bootloader
8. In the PS3 menu, go to settings->system settings, default os and select ‘other os’, then shutdown
9. Extract the contents of the ISO (but not the YellowDogLinux folder) to the ext3 thumbdrive
10. At this point you can either copy the iso to the root of the thumb drive, or make it available over a network share
11. Insert the ext3 thumbdrive into the ps3 and reboot with a usb keyboard attached, selecting the thumb drive as the bootable device
12. At this point you are in the YDL text installer, select the ISO or the network file share, and continue to graphical installation
13. During the graphical install, you’ll be given the mac address, I like to use this to setup static IP and tunneling while the system is installing
14. Continue through graphical installation, making sure to set a root password and install any dev libraries you may want (saves you some downloading later)
15. Watch a movie. Or two. Maybe the LOTR Trilogy. Seriously this will take a while
16. While the install is running, if you setup static IP for the PS3 mac you can setup your Z2’s package manager, on the z2. just `vim /etc/ipkg/*` and replace all instances of “Your IP HERE” with the static IP you setup for your PS3.
17. Once the graphical install finishes and you’ve set up your user, it’s time to start installing software as listed on the beagleboard port page
18. `yum install python m4 make wget curl ftp cvs subversion tar bzip2 gzip unzip python-psyco ccache perl`
19. `yum install texinfo texi2html diffstat openjade docbook-style-dsssl docbook-style-xsl docbook-dtds`
20. `yum install docbook-utils sed bison bc glibc-devel glibc-static gcc binutils pcre pcre-devel git`
21. `yum install quilt groff linuxdoc-tools patch linuxdoc-tools gcc gcc-c++ help2man perl-ExtUtils-MakeMaker python-sqlite2`
22. now compile the bitbake env. (this will dl the git objects ~150 megs as well) `cd ~/oe && source ./oe_zipit2.sh`
23. `make`
24. At this point, I log out of E17 and into a shell (ctrl-alt-f1). With only 200megs ram we want to conserve ram
25. Likewise, I like to decrease the number of bitbake threads in oe/zipit2/conf/local.conf from 8 to 1 and disable make threads
26. re-source oe_zipit2.sh and bitbake something small to get the skeleton directory made (this will take a long time) `bitbake tree`
27. If you told apache to install during graphical installer, run it now with `/etc/init.d/httpd start`. Otherwise install first.
28. Make a symbolic link from /var/www/zipit to your zipit deploy target, this allows the Z2 to see the packages you compiled `ln -s /var/www/zipit /home/zipituser/oe/zipit2-tmp/deploy/glibc/ipk `
29. on the ps3 (you will need to do this after every set of packages you compile) `bitbake package-index`
30. on the z2 (you will need to do this after every set of packages you compile) `ipkg update`
31. That’s that! Install and test your package on the Z2 with `ipkg install tree && tree`
32. Repeat for each package you wish to install, It’ll be SLOW, but you can stash the ps3 in a closet somewhere and be content it won’t red ring like certain consoles… even if it does thrash with 200megs ram.. happy bitbaking!


