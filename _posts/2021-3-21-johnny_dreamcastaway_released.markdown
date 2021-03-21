---
layout: post
title: Johnny Dreamcastaway Released 
date: '2021-03-21 08:33:24'
---
Johnny Castaway for the Dreamcast is now released!  I like to call it Johnny Dreamcastaway, and it didn't take me too long to port. It's working splendidly!  A glorious internal 640x480 screen resolution and a rock-solid 60 FPS carry you forward to your private island with "Johnny Dreamcastaway"

You can download a .CDI image to emulate or burn for a real Dreamcast [here](https://github.com/huntergdavis/jc_reborn/blob/DreamSDK/johnny.cdi)
You can download the unscrambed release .elf to emulate [here](https://github.com/huntergdavis/jc_reborn/blob/DreamSDK/johnny_dreamcastaway.elf)
You can view the source code [here](https://github.com/huntergdavis/jc_reborn/tree/DreamSDK)


<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/vbox_johnny_emu.png" width="1126">


<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/vbox_johnny_load.gif" width="640">


As I wrote last week, I stumbled upon the newest code for 'Johnny Reborn' (https://github.com/jno6809/jc_reborn), written by the talented Jérémie GUILLAUME, and immediately wanted to port it to the Dreamcast.

I had originally started writing this port last week when I backported jc_reborn to SDL 1.2.  I ran into a few issues with my post-compilation build environment, and decided to put it on hold until a physical Dreamcast comes in (since writing I've ordered one on eBay.)   

Well, I couldn't wait.  I did a bit more digging, and it turns out there's a nice packaged environment for the Dreamcast called DreamSDK.  This runs on Windows exclusively, so I flashed the Windows 10 image into my GPD MicroPC and got to work!  

DreamSDK really is quite nice as far as development environments go.  It has a nice integration with CodeBlocks (which I hadn't used in years, and is still quite solid.)  It also has a straightforward build environment and starter project that let me quickly get down to writing and packaging up ELF binaries for the Dreamcast.   

Once I had a starter ELF that I knew worked on emulators, I began adding in all the functionality of 'Johnny Reborn,' moving the assets into a ramdisk and loading them from memory.  This has the added benefit of no drive usage after boot, helpful for those looking to reduce wear and tear on their physical Dreamcast consoles. 

And that's about that!  You can view the source updates and a sample PR necessary to get this running in my jc_reborn/DreamSDK source tree [here](https://github.com/huntergdavis/jc_reborn/compare/SDL1.2...huntergdavis:DreamSDK?expand=1).

And again, here's your downloads: 

You can download a .CDI image to emulate or burn for a real Dreamcast [here](https://github.com/huntergdavis/jc_reborn/blob/DreamSDK/johnny.cdi)
You can download the unscrambed release .elf to emulate [here](https://github.com/huntergdavis/jc_reborn/blob/DreamSDK/johnny_dreamcastaway.elf)
You can view the source code [here](https://github.com/huntergdavis/jc_reborn/tree/DreamSDK)


What next?  Well I'm not sure I'm happy with the boot logo, and I could add in controller or VMU support for some fun times.  Still, I'm thinking I'll set my sights on a Nintendo Switch port next time, shouldn't take too long either!  
 
