---
layout: post
title: No x86 Handheld Needed 
date: '2021-10-09 08:33:24'
featured_img: 'https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/pi400beyondgoodandevil.jpg'
---

I was working on a follow-up to the previous article on my x86 handheld, when I stumbled upon a technology that totally superseded it.  


Backing up, in what little free time I've had these past few months, I've been installing and configuring linux/wine/lutris on bay trail devices.  You can pick up these tablets on eBay for under 40$ fully decked out, and it's just this year that linux/alsa/wine all work together well without much headache on these tablets.  The only problem is that they're used, in short supply, and they are not making any more.  So it's not a permanent solution, but it is a nice option.  


Then comes [TwisterOS](https://twisteros.com/about.html) and changes the game.  Now I can hop over to the Microcenter, pick up a 35-75$ board that plugs into any TV and uses any peripheral, and they're going to manufacture compatible units till the end of time. Nice. 


One interesting tidbit that I did glean from my time buying intel baytrail tablets (you know, the ones that have a 32-bit bios and a 64-bit processor?) is that Fedora 35 supports all of the ones I had out of the box, fully.  I can't even say that for windows 10.  It's a rock solid experience and a great way to play the Simpsons Hit and Run and many other games I wrote about in the previous article, quite cheaply (like 30-40$ for a used tablet cheaply.)


But no, there's no need for that now.  I read about TWISTER OS, a linux distribution for arm boards (like the raspberry pi) but tuned for running x86 software.  They've got box86 and wine running together, and I was quite skeptical that emulating both the CPU and the GPU would produce a playable experience on a modern arm device. 


I was way wrong!  Check out this video of The Simpsons: Hit and Run playing full speed (1024x768 resolution) on a raspberry pi 400.  Honestly this is a game changer, and as compatibility rises you can be certain this will get more attention.  


<iframe width="900" height="600" src="https://www.youtube.com/embed/mnX5fogHdoQ" title="Simpsons Hit and Run on the Pi 400" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


I wasn't able to get the windows version of Psychonauts running (at least on the first try), nor Clive Barker's Undying, but I'm going to dig in with lutris configurations and see if I can't get them going.  SimCity 3000 worked like a champ out of the box.  So did Beyond Good and Evil!  


<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/pi400simcity3000.jpg" width="640">


Then I saw it.  That little Steam icon.  Could it really be, could I really just click Steam, install some games and rock on?


I clicked, Steam loaded.  I entered my information, confirmed my Steam guard code, and snap.  I was in.  


It crashed a few times installing Portal, but I eventually got it installed.  Portal was a game I was surprised to see running at all in Linux on the bay trail chipsets, and I wanted to see how it runs on the Pi 400.  


It's about the same as the bay trail devices.  A bit choppy, but playable on low settings. 


<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/pi400portal.jpg" width="640">


I then proceeded to import my GOG.com games into Lutris, and install Prince of Persia.  


It's quite amazing how well some of these games run.  Prince of Persia: Sands of time was choppy on a bay trail processor with some amount of tweaking. It's almost perfect on the pi 400, out of the box!  Lower end games like SteamWorld Dig ran flawlessly without any configuration at all. 


All in all, I am so excited for what this represents.  For me, it's bespoke game images for my raspberry pi.  This usb thumbstick boots straight up into the Simpsons Hit and Run, this one into Prince of Persia, this one into the Sims.  I know they'll boot on any pi-4 or above, and for sure there will be a host of portable options built around the pi CM4.  A whole new generation of games just became playable on the next generation of mid-range handhelds and low-end consoles, and I'm here for it! 
