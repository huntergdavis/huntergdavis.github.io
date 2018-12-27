---
layout: post
title: rexVM - A virtualBox Appliance for Developing for The REX 6000
date: '2010-08-23 23:55:19'
tags:
- cloud
- hack
- hacking
- linux
- live
- open-source
- ubuntu
- virtual-machine
- virtualbox
---


As most of you readers probably know, I have been terribly remiss in my postings of late. That isn’t to say that I haven’t been hacking. Oh no. Bootstrapping a startup requires hacking all over the place. During the past week alone I’ve

1. Gotten to know my franchise tax agent on a first name basis
2. Authored contracts, which in my opinion should be written in python
3. Authored a research paper on novel methods for efficient bulk virtual machine storage and retrieval (stay tuned for that one!)
4. Reminded myself daily why I use git, while writing features integrating svn, cvs, etc
5. Created what, I am fairly sure, is the world’s largest openWRT/BCM5354 firmware image/executable set
6. Created at least 10 new project virtual machines

Which actually brings me out of my /startup header and back into :/publish . One of the terrific things about founding a startup (ducks!) is the flexibility you get while setting up your workflow. Long a proponent of integrating virtual machines into business processes, I have been enjoying the real freedom a robust virtualized system can provide. I’ll get into the detailed workflow later in the post. For those ‘first page only’ readers I’ll get to the golden ticket, I recently picked up a REX 6000 credit card PDA for 6$ at the local thrift.

![REX 6000](http://upload.wikimedia.org/wikipedia/commons/3/37/Rex_6000.jpg)

Read on for (much) more and download links!

In 10 years this 4mhz z80 compatible PDA has remained unrivaled in terms of portability and size. Though I’ve started (in the few non work-related hours I get each month) prototyping work on an e-ink version of the REX 6000, it still has a long way to go before it’s usable. In the meantime, I’ve been enjoying my REX 6k immensely. There were quite a few user programs written for the device in the years after Intel bought and squashed the project, and the history of the device is as fascinating a look at a hacker subculture as you’ll ever find.

Anyway, if you want to develop for the device, there’s a useful SDK that’s been updated to work with new compilers and versions of linux available [here](http://www.ipd.bth.se/ska/sim_home/rex_utils.html). As I am using the REX 6000 for prototyping (something I often do at work), I figured I would apply my professional workflow to this my personal project. This means a tight, low overhead virtual machine in .ovf format using all open source software which you can import from a vmRepo and be up to speed in seconds (cloud friendly!).

DOWNLOAD LINKS:  
 If you work or are visiting Discursive Labs, you can download rexVM from the VMrepo [here](vmr://public/hunter/rexVM). For everyone else, you can download it directly from hunterdavis.com [here](http://hunterdavis.com/rexVM.zip).  
 971,810,614 Bytes, will be available 6am Pacific Time August 24th 2010 …

One forum post which has saved me immense amounts of time in this process has been [this one at ubuntuforums](http://ubuntuforums.org/showthread.php?t=575456). I could have (and many many times have) built debian based VM’s from scratch/stock/server Ubuntu distros and it is just not the same as when you build from a minimal system that’s got just what you want in it. Here’s how I setup rexVM. I use a set of scripts at DL but for personal projects I don’t mind starting from a fresh interactive command line. Assuming Ubuntu, and wanting to use Puppy (for smallest size… installing make and svn could be easier …). We’re going to do this a bit backwards. Puppy likes running in live cd mode, especially when you want to have the devx (compiler) package running. We’re going to install puppy in hard drive mode, then copy the contents of the devx package into our compiler.

1. Download puppy linux 5.1, this is a great tight base image to start building from
2. Fire up VirtualBox, and create a new VM named rexVM. For tightly bound development I like to have a 10gb expanding size disk and a small amount of ram ~256mb -i.e. lots of room for libraries and enough ram to compile
3. Add the puppy-510.iso to your virtual media manager
4. On the rexVM details page, add the puppy-510.iso as the ide secondary master (cd-drive)
5. Boot up the VM, and in puppy select ‘system->puppy universal installer’
6. Open gParted, device->create partition table, then partition your virtual HDD to 9.5gb ext3/.5gb swap
7. Set the boot flag to on for the partition you just created
8. Close gParted and the installer will commence-do a full install and install grub to sda1
9. Shutdown the VM and de-attach the pupper live iso from the system
10. Once it boots up, open system->quickpet and install the xorg_high driver
11. Reboot or restart the x-server to activated
12. Open the puppy package configuration utility and add extra repositories
13. Close the package utility and download the [devx package from here](http://distro.ibiblio.org/pub/linux/distributions/puppylinux/puppy-5.1/lupu_devx_510.sfs)
14. Click on the devx_510.sfs in a ROX-Filer window to mount it.
15. Open a terminal in the mounted directory. (/mnt/+lupu_devx_510.sfs)
16. `cp -a --remove-destination ./* /mnt/home/`
17. Reboot the VM
18. At this point we should be ready for the compiler, so make yourself a project directory
19. `mkdir /projects/rexVM`
20. Enter that directory, and checkout the rxSDK
21. `svn co https://mondragon.tek.bth.se/svn/main/world/ska/rex/trunk/rxsdk/`
22. (you’ll need to accept his security cert..which may be expired bleh)
23. cd into the rexSDK directory, and edit the Makefile
24. Change the sdcc: svn root target to be https://sdcc.svn.sourceforge.net/svnroot/sdcc/trunk/sdcc sdcc
25. (Make sure you’ve got the extra /sdcc/trunk/sdcc on the end of that link!! )
26. Now copy over the sdcc-sparse link directory with `cp -rp ./sdcc-sparse/link/ ./sdcc/ `
27. Now, in that same directory, make the project with a standard `make`
28. This may take a while, grab a snack, or cheat a little and up the ram/cpus on your VM during this compile 😉
29. Once sdcc has finished compiling, execute a ` make install_sdcc `
30. Once sdcc has finished installing, softlink the z80 assemler command ` ln -s /usr/local/bin/sdasz80 /usr/local/bin/as-z80 `
31. Execute the next make step with ` make build_rxsdk `
32. Once rxsdk has finished compiling, execute a ` make install_rxsdk `
33. If install_rxsdk barfs on librex, manually finish the tool compile install with `cd rxsdk/tools/rxbuild && make install`
34. At this point, you have a nice build environment for your REX 6000 (and really most z80 based chipsets)
35. If you’re like me, you’ll want to export the virtual appliance as a .ovf and add it to your vmRepo

And that’s that. Time for me to setup – hours. Time for each developer after me to setup a REX 6000 development environment? The time taken to download a ~970mb zip file. About 20 seconds over my local wifi network — not bad! You can more generically use these instructions to create any number of custom compile environments. Like the 300mb Z2 image I posted so long ago, I’ll post the 1gb rexVM for as long as it doesn’t start to eat up my bandwidth. Considering there’s probably 50 REX users left out there, (only one of whom I’m sure reads this blog) I’m not too worried. Happy Hacking!!


