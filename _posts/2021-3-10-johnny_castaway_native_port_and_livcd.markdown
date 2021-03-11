---
layout: post
title: Porting Johnny Castaway to Dreamcast 
date: '2021-03-10 08:33:24'
---
Once again, I am reminded of how much the past influences our future, and the choices we make.  In my case, it's a twisty tale that starts simply enough, but ends with Johnny Castawy running natively on the dreamcast.  Interested?  Read on.  Want to download it for your dreamcast right now?  Skip to the end!


This story starts with wonderful news, one of the talented developers working to re-implement Johnny Castaway has done so in a languge I quite enjoy (ansi c), and quite successfully.  When I stumbled upon the newest code for 'Johnny Reborn' (https://github.com/jno6809/jc_reborn), written by the talented Jérémie GUILLAUME, a few things stood out to me:

1. This is a fully baked re-implementation of Johnny Castaway
2. It's currently working 
3. It's written in ansi C-99 and SDL 2
4. The above code is quite clean, enjoyably so
5. It is criminally under-exposed for how good it is (2 watchers, 8 stars, 1 fork (mine))

So, I did what anyone in my situation would do, I set out to cross-compile a static 32-bit version of Johnny I could boot up on 486 laptops.  (You can download that binary, or a live linux ISO at https://github.com/huntergdavis/jc_reborn/tree/master/static )

This worked well enough, but unfortunately the 23 year old latop I was booting it on doesn't support Xvesa.  Framebuffer was working through, so I set about to boot to console and execute in console-FB.

Bummer, SDL 2.0 doesn't support console framebuffer any longer.  I was facing a large number of hoops to try and layer in xfcb-dev onto tinycore and boot on my particular craptop, and I realized something. 

Lightbulb moment!  Why not just re-write the graphics layer of johnny-reborn in SDL 1.2.  That does support framebuffer backends!  So that's just what I did, a quick SDL 2.0->1.2 backport.  (Source here https://github.com/huntergdavis/jc_reborn/tree/SDL1.2 )

Second Lightbulb moment!  SDL 1.2 doesn't just support framebuffer backends.  It's fifteen+ years old at this point, and it supports some popular systems of that era.  One in particular caught my eye - the Sega Dreamcast.  Why?

1. I love the Sega Dreamcast.  So Much.
2. It supports 640x480 natively, default resolution for JC_reborn, no need to write a scaler
3. You can craft an ISO with the right audio track and boot on many commodity dreamcast units. 
4. Emulators are plentiful and run on all kinds of hardware (Android, game devices, etc)
 

So, I set about my plan. 

1.  Install the kallistos libraries and cross-compile environment
2.  compile kallistos-ports (including sdl1.2)
3.  update instantiation for johnny to dreamcast specific 
4.  compile executable
5.  assemble iso
6.  test on emulator

Out of scope for this initial release
1. Updating dc-specific features (i.e. VMU support)
2. Testing on actual hardware (I'll need to buy one that supports reading CD-R disks, pre-2000 manufacture date)





<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/dec/recentfiles.jpg" width="600">







 
