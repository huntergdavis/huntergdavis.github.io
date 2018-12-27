---
layout: post
title: Npower Fusion - Breakdown Tutorial and Chipset Info
date: '2009-12-24 11:33:38'
---


So a few of you had asked for a detailed chipset list for the npower fusion java console. Sounded like fun, so here it is. Turns out to be a pretty interesting device. For the super impatient among you, 200mhz 8mb ram arm SoC, possible [rockbox](http://www.rockbox.org) target. Read on for photos and follow along instructions.  
![front lcd and buttons](http://66.147.244.180/~hunterda/content/images/2009/12/PIC_00881.jpg)

1. Using your thumbnail or a flat screwdriver, pry up the front face. This is what holds the dpad and the 3 buttons in, so don’t let them fall under the couch when you pop this sucker off. Trust me, you don’t want to go under there.  
![npower no faceplate](http://66.147.244.180/~hunterda/content/images/2009/12/PIC_00551.jpg)
2. Using a small phillips screwdriver, remove the 4 face screws from the front corners of the device.
3. Using a small flathead scredriver, insert it into the 4 slots on the outer edge of the device, this will allow you to pop open the rear plate and expose the motherboard  
![npower motherboard](http://66.147.244.180/~hunterda/content/images/2009/12/PIC_00621.jpg)
4. Now that the mb is exposed we immediately see 2 chips, the hynix kor 713a firmware (apparently common in ipod clones) and Telechip tcc8200 200mhz arm SoC (very interesting), as well as 3 chips covered in spacer tape. This leads me to believe we may be able to get the rockbox distribution flashed on this…. The rockbox wiki has a page on this chipset which appears to have graphics acceleration of some sort? You can see the page [here](http://www.rockbox.org/wiki/TelechipsInfo).  
![npower chipset](http://66.147.244.180/~hunterda/content/images/2009/12/PIC_00631.jpg)
5. Removing the first spacer tape reveals a K4M56323 8mb sdram chip. So the device has 8mb sdram in 4 banks of 2mb, with 2mb being allocated to the test java program. [Here’s a page](http://www.datasheetarchive.com/) with a pdf of the datasheet.
6. The center spacer tapes are covering 1.8v caps, so leave them on there
7. The spacer tape next to the hynix chip is covering some unsoldered leads, maybe worth getting a multimeter on there later?
8. At this point, we’ve seen all there is to see on the rear face of the MB, time to flip it over. Using a small screwdriver remove the 4 small screws on the mb
9. And there’s the LCD. Looks like it’s on there pretty good, not worth taking off. So that’s that! Interesting stuff all around.  
![front lcd assembly in red](http://66.147.244.180/~hunterda/content/images/2009/12/PIC_00721.jpg)


