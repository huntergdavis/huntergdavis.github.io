---
layout: post
title: Surface RT Equalizer Visualizer
image: "/content/images/2018/01/00010IMG_00010_BURST20180101112859-1.jpg"
date: '2018-01-01 20:07:27'
---

The Surface (non-pro) was an interesting device.  Running windows RT 8.1 and sporting a 720p display, from the outside this was a half-decent productivity tablet.  It came with a fully usable version of Microsoft office, could share peripherals with the (far superior) surface pro, and was priced to sell. Sadly, the locked-down operating system meant the software landscape was barren, the hacking scene was anemic, and the technology quickly became outdated.  

![](/content/images/2018/01/IMG_20180101_110219.jpg)

You wouldn't think there'd be much you could do with one nowadays, and generally speaking there's not. The device chugs on web browsing after more than a few tabs are open, there's limited software compatibility, and the bootloader has only now been unlocked 5 years later.  Pretty bleak outlook.  On the other hand, the surface has two features that I find really interesting:

*  The color reproduction, black levels, and affinity for sub-pixel rendering make it a visually beautiful display. 
* The USB driver stack is fairly robust, and supports all manner of USB audio devices. 

Having run across a v1 surface RT on the cheap, I sought to make use of these great qualities.  My first thought was to use the JavaScript audio bridge I hacked together for a previous article, but sadly web audio is not supported in the version of IE that's locked to windows RT 8.1 (and sadly, no Chrome.) 

So, I searched the store proper for an audio visualizer.  I got lucky and found Kauna, and what do you know the free version supports both waveform and VU meter visualization.  

![](/content/images/2018/01/IMG_20180101_113051.jpg)

Next, I found an old USB->RCA audio bridge in my box of project ideas. It worked without issue.  I adjusted the input gain and all was well.  Still, the wires hanging off the side of the RT didn't look great, and I wanted to up the nice factor a bit.  I decided to fashion a frame for it, such that I can mount it above my rack-mount stereo in the future.

![](/content/images/2018/01/IMG_20180101_113046.jpg)

With some tape, scissors, an old cardboard box, and a little patience, I fashioned a MVP frame for the visualizer. It's not professional grade, but it'll do for now.  At some point I may pick up some faux-wood veneer and give it that 70s component vibe, but for now I'm happy with how it turned out.  I'm also especially happy I could make use of some "obsolete" tech that's only a few years old, and has many many years of use left.

![](/content/images/2018/01/IMG_20180101_112949.jpg)

![](/content/images/2018/01/00000XTR_00000_BURST20180101112859-ANIMATION.gif)
 