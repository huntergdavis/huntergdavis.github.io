---
layout: post
title: Johnny Castaway Native Live CD 
date: '2021-03-10 08:33:24'
featured_img: 'https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/vbox_johnny.png'
---
Once again, I am reminded of how much the past influences our future, and the choices we make.  In my case, it's a twisty tale that starts simply enough, but ends with Johnny Castaway running natively from a ramdisk on systems with as little as 64mb.  Interested?  Read on.  Want to download it for yourself right now?  Skip to the end!

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/vbox_johnny.png" width="640">

 

[And here's a nice video from VirtualBox :)](https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/64mb_ram_vm_boot.webm)


This story starts with wonderful news, one of the talented developers working to re-implement Johnny Castaway has done so in a languge I quite enjoy (ansi c), and quite successfully.  When I stumbled upon the newest code for 'Johnny Reborn' (https://github.com/jno6809/jc_reborn), written by the talented Jérémie GUILLAUME, a few things stood out to me:

1. This is a fully baked re-implementation of Johnny Castaway
2. It's currently working 
3. It's written in ansi C-99 and SDL 2
4. The above code is quite clean, enjoyably so
5. It is criminally under-exposed for how good it is (2 watchers, 8 stars, 1 fork (mine))

There have been a few re-implementations of Johnny over the years, but I've always chosen to emulate Johnny using Dosbox or Wine.  Why?  These re-implementations used resource-intensive high-level languages and libraries.  They wouldn't run particularly well on a 25 year old PC!  I know that's not a use case most folks still have, but it's of special interest to me :) So when I dug into this re-implementation, I knew it was something special.  Clean, straightforward code.  Runs in a few megs of ram, no noticeable memory leaks, low CPU usage even on ancient (486) class machines.  Immediately made me smile in a way I hadn't in some time.  

So, I did what anyone in my situation would do, I set out to cross-compile a 32-bit version of Johnny I could boot live on low-end systems (edit: tested working with as low as 64mb ram!).  [download that binary, or a live linux ISO] (https://github.com/huntergdavis/jc_reborn/ )

This worked well enough, but unfortunately at least one of the laptops I was booting it on doesn't support Xvesa/Xorg.  Framebuffer was an option through, so I set about to boot to console and execute in console-FB.

Bummer, SDL 2.0 doesn't support console framebuffer any longer.  I was facing a large number of hoops to try and layer in xfcb-dev onto tinycore and boot on my particular craptop, and I realized something. 

Lightbulb moment!  Why not just re-write the graphics layer of johnny-reborn in SDL 1.2?.  That does support framebuffer backends, and it's fairly similar to SDL 2!  So that's just what I did, a quick SDL 2.0->1.2 backport for Johnny.  [Source here](https://github.com/huntergdavis/jc_reborn/tree/SDL1.2 )

Second Lightbulb moment!  SDL 1.2 doesn't just support framebuffer backends.  It's fifteen+ years old at this point, and it supports some popular systems of that era.  One in particular caught my eye - the Sega Dreamcast.  Why?

1. I love the Sega Dreamcast.  So Much.
2. It supports 640x480 natively, default resolution for JC_reborn, no need to write a scaler
3. You can craft an ISO with the right audio track and boot on many stock Dreamcast units. 
4. Emulators are plentiful and run on all kinds of hardware (Android, game devices, etc)
 

So, I set about my plan. 

1.  Install the kallistos libraries and cross-compile environment
2.  compile kallistos-ports (including sdl1.2)
3.  update the init and file i/o for johnny to dreamcast flavor 
4.  compile elf executable, convert to bin, scramble bin, convert to 1ST_RUN.BIN
5.  assemble IP.BIN, assemble iso, convert to CDI
6.  test on emulator

Out of scope for this initial release
1. Updating dc-specific features (i.e. VMU support)
2. Testing on actual hardware (I'll need to buy one that supports reading CD-R disks, pre-2000 manufacture date)

How did that go?  Well, I've found out something that many Dreamcast developers know very well, it's very hard to debug i/o in an emulator!  Much easier on actual hardware.  So, pending my next purchase of a Dreamcast, those preliminary commits are available for anyone looking to try. [here](https://github.com/jno6809/jc_reborn/compare/master...huntergdavis:dreamcast?expand=1)

Anyway, back to the live CD, I was looking to boot with a dynamically linked SDL 1.2 with console-framebuffer support (SDL 1.2 only allowed static linking if you buy a pro license, boo!).  There were still a couple of hoops to jump through though:

1.  Mouse support!  Not likely.  Export SDL_NOMOUSE=1 (you'll see this in /home/tc/.profile on the ISO)
2.  pass ''text' parameter to grub on boot (don't attempt to startx)
3.  set the desired vga output for FBconsole.  This gets picked up from the vga=XXX grub boot parameter (640x480x32 is vga=786)
4.  auto-start johnny directly.  For the live CD I just add this to /home/tc/.profile and busybox will pick it up on autologin.


And that's about it!  You can download a live ISO that'll boot to ram from any supported medium (17 megabytes or above, sorry floppy friends!)  [here](https://github.com/huntergdavis/jc_reborn/blob/SDL1.2/johnny_dc.iso)  A giant thanks to [Jérémie GUILLAUME](https://github.com/jno6809) for re-implementing Johnny in a clean, portable format that really made my day!! 

[Here's a video of that very ISO booting from a burnt-CD (remember those!) on my beloved 2001 era Thinkpad (256mb RAM)](https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/thinkpad_johnny_960.webm)







 
