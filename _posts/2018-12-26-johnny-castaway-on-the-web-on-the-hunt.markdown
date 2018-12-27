---
layout: post
title: Johnny Castaway - On The Web, On The Hunt
image: "/content/images/2018/12/johnny_web.png"
date: '2018-12-26 23:59:37'
---

Longtime readers of this blog may recall my slight obsession with an old screensaver: Johnny Castaway.  Johnny was a Windows 3.1 screensaver, part of Sierra's 'Screen Antics' collection.  Fitting handily on a single 3.5" floppy disk, Johnny spent his time alone on a deserted island.  He fished, he napped, he went on dates with a mermaid.  It was a fascinating, subversive tale.  The true moral of the story was that Johnny wasn't happy until he was on that island, but he didn't realize it until after he had been rescued.  The 'ending' scene is of Johnny parachuting back onto his desert island, leaving his old programming job and city life behind.  

You can see how this tale would resonate with me, and truly it's stuck with me for the past 26 years.  I always have Johnny running somewhere.  He's running on an old android tablet (running dosbox) at my work desk at Avvo.  He's running on an old iPad (with dosbox sideloaded) at my gaming desk at home.  

Most recently, (and the crux of this post) he's running on the web at https://huntergdavis.github.io/johnnycastaway/

Before I get to that though, _I have a special request for folks!_

**I am interested in acquiring the Johnny Castaway intellectual property**  <br><br>I'd love to re-implement Johnny Castaway for modern systems, maybe open-source it, allow folks to add more scenes, graphics packs, etc.  At the minimum I'd like to be able to host it without fear of DMCA.  Before I go off on an epic quest to find the current rights holders, Sierra, Jeff Tunnell, etc, I'll give crowd-sourcing a shot.<br>  
#### **Does anyone know who currently owns the rights to Johnny Castaway?**  

If you do, _please email me directly -> hunter@hunterdavis.com_

Anyway, back to our regularly scheduled post.  While I had originally set about to write a bespoke emulator for Johnny, I happened upon a couple of projects that made my task much, much easier.

* [Em-Dosbox](https://github.com/dreamlayers/em-dosbox) - Dosbox compiled via Emscripten (dosbox running in JavaScript!)
* [js-dos](https://js-dos.com/) - A set of JavaScript APIs to interact with and style Em-Dosbox
* [GitHub Pages](https://pages.github.com/) - Host your project site from GitHub, very easily

My task was essentially just building a zip file image of a Windows 3.1 instance running Johnny Castaway and calling the appropriate APIs.  You can find the source code here: https://github.com/huntergdavis/johnnycastaway

I'm now using [Wallpaper Engine](https://store.steampowered.com/app/431960/Wallpaper_Engine/) to display Johnny as my desktop wallpaper (and loving it!)

![](/content/images/2018/12/johnny_castway.png)

p.s. If you're having trouble resizing the DosBox instance appropriately for an embedded use case (as I was), I've added a url parameter to set the zoom level on the page.  I've found that a zoom of 4.5 feels right on a 4K monitor running Wallpaper Engine, which would use the following URL: https://huntergdavis.github.io/johnnycastaway/?zoom=4.5
