---
layout: post
title: Using an Original SNES Controller and Cartridge with your PC, PS3, or Dockstar
  (Retrode Pre-Order glory)
date: '2012-01-09 02:05:16'
tags:
- dockstar
- gaming
- marvel-vs-capcom
- ps3
- retro
- retro-gaming
- retrode
- snes
- usb
- zsnes
---


I’ve mentioned the Retrode before, and if you don’t know it’s a terrific device by [Matthias Hullin](http://retrode.org/) which allows you to use your original Super Nintendo and Genesis controllers with anything USB.  I set out to use an original SNES controller and original cartridge to play Mario Kart.  I ended up doing just that on a couple of interesting platforms, and I’m terrifically pleased with the finished product.  Read on for more photos, videos of the PS3 and Retrode working together, and good times.

[![](http://www.hunterdavis.com/content/images/2012/01/PICT0042-300x225.jpg "retrode top")](http://www.hunterdavis.com/content/images/2012/01/PICT0042.jpg)

When I heard a knocking on my door this Saturday morning, I never expected it to be my mail carrier.  There she was, holding a book-sized box covered in stamps from Germany.  I knew immediately what it was.  I hardly noticed Matthias’ name was on the outside of the box, such was my rush to get to this device.   The Super Nintendo got me through some tough times as a kid, and I was eager test the device on some of my treasured cartridges.  I plugged Mario Kart into the nicely fitting port on the top of the case, inserted the SNES controller, and fired up ZSnes on my gaming PC.  The Retrode immediate showed up as an external drive containing three files, Super Mario Kart.14BB.smc (the rom), Super Mario Kart.14BB.srm (the save) and Retrode.cfg (the Retrode configuration). The controller was recognized as an USB input device.  Ten seconds of configuration in ZSnes, and I was reliving the silver age of gaming on my PC with the original hardware, perfectly.  Sweet…  But not enough!

[![](http://www.hunterdavis.com/content/images/2012/01/PICT0037-300x225.jpg "box from germany")](http://www.hunterdavis.com/content/images/2012/01/PICT0037.jpg) [![](http://www.hunterdavis.com/content/images/2012/01/PICT0043-300x225.jpg "retrode and pc")](http://www.hunterdavis.com/content/images/2012/01/PICT0043.jpg) [![](http://www.hunterdavis.com/content/images/2012/01/PICT0045-300x225.jpg "retrode and zsnes")](http://www.hunterdavis.com/content/images/2012/01/PICT0045.jpg) [![](http://www.hunterdavis.com/content/images/2012/01/PICT0041-300x225.jpg "genesis slot")](http://www.hunterdavis.com/content/images/2012/01/PICT0041.jpg)

My first thought was to plug this into an ARM device with video out and throw the resultant image up on the big screen.  Having given out a great deal of the smaller arm devices I used to hoard around, that seemed unlikely to happen today and my eyes began to wander.  They landed on my Dockstar, a small arm board (with no video) that’s been crashed and re-flashed and frankensteined in a thousand ways just this week.  That’s the glory of Linux, the infinite customization, and still it reminds me so much of DOS sometimes.  Anyway, I plugged the Retrode into the tiny Linux box to see if I could get a response, and lo and behold:

input: Matthias Hullin Retrode as /devices/platform/orion-ehci.0/usb1/1-1/1-1.3/1-1.3:1.1/input/input0  
 generic-usb 0003:0403:97C1.0001: input: USB HID v1.11 Joystick [Matthias Hullin Retrode ] on usb-orion-ehci.0-1.3/input1  
 input: Matthias Hullin Retrode as /devices/platform/orion-ehci.0/usb1/1-1/1-1.3/1-1.3:1.2/input/input1  
 generic-usb 0003:0403:97C1.0002: input: USB HID v1.11 Mouse [Matthias Hullin Retrode ] on usb-orion-ehci.0-1.3/input2  
 scsi 4:0:0:0: Direct-Access Retrode .17 PQ: 0 ANSI

Yep!  I’m now able to natively access SNES and Genesis cartridges and controllers directly from Linux.  This is pretty sweet, but without local video out it’s not terribly exciting for this article.  The chance to use a SNES controller to play rogue is fun and all, but still, there’s one more platform I had to try.  The PS3.  I’ve already got a number of emulators installed, I know it supports the vast majority of USB HID device profiles, and it’s plugged into my projector locally, no network latency for video!  I proceeded to plug the Retrode into the PS3.

[![](http://www.hunterdavis.com/content/images/2012/01/PICT0051-300x225.jpg "retrode and ps3")](http://www.hunterdavis.com/content/images/2012/01/PICT0051.jpg)

Glorious success!  The Mario Kart cartridge shows up as USB003, and the SNES controller is natively mapped as a PS3 controller.  This means you can use it to play PS3 games as well!  Below are a couple of videos of the end result!  Game on!  This leaves me no doubt the Retrode will work on a multitude of existing and upcoming platforms such as the RasberryPi, OLPC, tablet PCs etc.  Don’t forget that the Retrode can also support Genesis/Atari compatible controllers and numerous other cartridge formats besides SNES/Genesis through the use of [plug-in adapters](http://www.retrode.org/plug-in-adapters/) and a whole world of COMPLETELY legal (absolutely no grey area here) hacking and modding opens up.  Want to see where things are going?  Head on over to the [Retrode ](http://www.retrode.org/)site and check out the [community forums](http://forum.retrode.org/).

Here’s a video of me playing Marvel VS Capcom 3 using a Super Nintendo Controller.

<iframe allowfullscreen="" frameborder="0" height="525" src="http://www.youtube.com/embed/I4NXk3IJJN4?feature=oembed" width="700"></iframe>

Here’s a video of me playing Mario Kart (from the original cartridge) using a PS3 Controller and a SNES controller).

<iframe allowfullscreen="" frameborder="0" height="525" src="http://www.youtube.com/embed/tAiAaTUan60?feature=oembed" width="700"></iframe>

 


