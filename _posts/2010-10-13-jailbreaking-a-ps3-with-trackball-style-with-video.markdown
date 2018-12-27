---
layout: post
title: Jailbreaking a PS3 with Trackball Style (With Video)
date: '2010-10-13 23:17:15'
tags:
- arcade
- arduino
- box
- build
- cheap
- chips
- diodes
- fun
- hacking
- news
- ps3
- repurposing
- resistors
---


After a particularly long (but rewarding) day of prototyping and contract hunting over at Discursive Labs, Mark and I weren’t quite ready to stop creating when the work day ended. Already having his trusty iron handy, and me with my parts (and [MY AXE](http://hunterdavis.com/archives/494)), we decided to unwind and relax by hacking something. Typical Wednesdays right? Anyway, after reading about how the PS3 homebrew scene is blowing up, we decided to see if we could build a PS3 jailbreak device with parts we had around our workbench. After finding an old ‘atari in a joystick’ TV game we had previously stuffed into a PS1 trackball, we had the spark of an idea. Read on for photos, video, a ridiculously scatterbrained photostream, and all around good times.

<object height="344" width="425"><param name="movie" value="http://www.youtube.com/v/Gza4nB5cCfg?hl=en&fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed allowfullscreen="true" allowscriptaccess="always" height="344" src="http://www.youtube.com/v/Gza4nB5cCfg?hl=en&fs=1" type="application/x-shockwave-flash" width="425"></embed></object>

If you’ll recall the ppc/vision work I was doing back in 07′, I have a thing for computer vision and integrated peripherals. Having picked up an Arduino (duemilanove) on Amazon during a prime free trial last year, and having a bucket of resistors and caps, leds diodes and webcam parts, Mark and I began work on the breakout board necessary to interface the duemilanove with the PS3.

[![take a sneak peek inside the trackball!](http://66.147.244.180/~hunterda/content/images/2010/10/IMG_66911-300x225.jpg "Sneak Peek!")](http://66.147.244.180/~hunterda/content/images/2010/10/IMG_66911.jpg)

Not having any zener diodes handy, we opted to start from cyko500’s reference design [here](http://www.ps3hax.net/2010/09/psgroove-for-arduino-megaduemilanove/). We built off a typical 3″ smartboard we had around, about 5$ at Frys or probably 10c online somewhere. Besides the small bit of dremel use to grind the over-sized capacitor leads power tools were not required. It was a straight solder and epoxy job. As you can see, we always properly label and color line connectors for later ease of re-use. Take pride in your cabling and soldering! It will save you HOURS if not years in the long run.  
[!["soldering is all done"](http://66.147.244.180/~hunterda/content/images/2010/10/IMG_66801-300x225.jpg "Arduino plus Breakout Board")](http://66.147.244.180/~hunterda/content/images/2010/10/IMG_66801.jpg)

Just a quick diversion. [![atari tv joystick with the guts removed](http://66.147.244.180/~hunterda/content/images/2010/10/IMG_66571-300x225.jpg "hollow atari joystick ")](http://66.147.244.180/~hunterda/content/images/2010/10/IMG_66571.jpg) Most of the TV games you see are actually based on the same reference design with separate (interchangeable it seems) backplates or faceplates and paint jobs. There are a lot of nice holes and slots already drilled (or more likely molded) and they make a great project case. Plus there are a terrific amount of fun things to do with the guts of them, basically a 1″ by 2″ atari game you can throw in an altoids tin. Next time we’ll have to build one in a SpongeBob game. This time we used the PS1 trackball housing which used to hold the atari stick. It’s fairly spacious inside and there’s plenty of room to mod lights into the buttons etc. If you’re interested in the construction, you should check out my [fairly unorganized flicker set](http://www.flickr.com/photos/huntergdavis/sets/72157625160065178/) of the experience.

As you can see from the video and photos, it kind of feels right having an fat old PS1 trackball as the housing for a ps3 jailbreak. A usb stick with a small indicator is fine and all that (for 160$ they say?… no thanks), but an old trackball you picked up for 2$ at a yard sale? That’s a keeper.

[![The Finished Product](http://66.147.244.180/~hunterda/content/images/2010/10/IMG_66901-150x150.jpg "PS3 JailBreak in a PS1 Trackball")](http://66.147.244.180/~hunterda/content/images/2010/10/IMG_66901.jpg)


