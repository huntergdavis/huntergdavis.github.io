---
layout: post
title: A 25$ Gaming/Emulation Powerhouse - Using the Dockstar as a Gaming Console
date: '2010-11-28 08:42:25'
tags:
- arm
- displaylink
- dockstar
- emulation
- gba
- integrated-development
- linux
- n64
- nes
- porting
- snes
- software
---


As most regular readers will probably know, I’ve got a thing for low powered devices. In my [daily work life](http://www.discursivelabs.com), I build clusters with them and write/run scientific computing and visualization software on them. At home though, I’ve got a thing for [game consoles](http://hunterdavis.com/archives/706), [emulation](http://hunterdavis.com/archives/253), and [USB](http://hunterdavis.com/archives/450). I’ve especially got a thing for getting people playing games or running consoles on unusual systems that they would have never thought to use. I think the [Zipit](http://hunterdavis.com/archives/category/zipit-hacking) and [IM-ME](http://hackaday.com/2009/11/30/pink-wireless-terminal-of-wonder/) communities are fairly well aware of this already. What amazed me though, is how few people I found seriously discussing the idea of using a pogoplug device as a game or emulation console. Allow me to get the conversation started with a bang.

<object height="385" width="480"><param name="movie" value="http://www.youtube.com/v/hwVwFHDA5iE?fs=1&hl=en_US"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed allowfullscreen="true" allowscriptaccess="always" height="385" src="http://www.youtube.com/v/hwVwFHDA5iE?fs=1&hl=en_US" type="application/x-shockwave-flash" width="480"></embed></object>

For those with web ADHD:  
 tl;dr – Using a Dockstar and a DisplayLink adapter in tandem for gaming works incredibly well not just as an emulation console, but as a general purpose desktop as well, watch the video below for a multitude of console and PC gaming goodness. I show it running

- Scummvm (Monkey Island 3)
- NES (Contra)
- Doxbox (Warcraft)
- Mednafen–
- Lynx (Lemmings)
- GBA (Aria of Sorrow)
- GBC (Lufia)
- GB (Links Awakening)
- TurboGrafx (Bonk 3)
- NeoGeo Pocket (Last Blade)
- Wonderswan (Guilty Gear Petite 2)
- stella 2600 (Adventure)
- VisualBoyAdvance (Mario World)
- SuperTux
- Abuse – Actually this was cut for time in the youtube clip but it plays perfectly.
- Wesnoth
- yabuase Sega Saturn (Sonic Extreme)
- Quake 3 (OpenArena)

Most with the exception of Saturn and OpenArena run at full playable speed with sound and full or near fullscreen graphics. I have no reason to believe SNES or even Mame and Playstation are out of the picture, with some cleverness. There is so much more below.

For everyone else, read on for photos, configuration files, tips, tricks, explanations, and a thorough walkthrough of the process.

**Wasted MHZ**  
 One of the greatest things about the pogoplug is the ease of finding cheap reference hardware. I have been purchasing Dockstar FreeAgent (pogoplug NAS devices) for 25$ shipped for sometime now, and they make for a great low power cluster node. However, what they are not great at is video. They have no discrete graphics, and only 3 USB and one gigabit ethernet ports to work with. On the other hand, they are rocking 128mb of internal ram, 256megs of rom (for flashing images if desired, I just throw mine on a USB stick), and a 1.2ghz marvell arm processor. For a device which consumes a mere 4-6 watts of power at full load, this is a hell of a powerful processor at this price point.

I mean think about it. That’s 1200 mhz of processing power with 128mb of ram. Among some of the low power machines I have developed for, that’s orders of magnitude beyond what the status quo is. My gameboy advance ran a similar architecture at 17mhz, and I had a hell of a good time playing those games and developing for that system (still an order of magnitude faster than the first systems I wrote code for!). These facts and the fact that debian-arm (which Jeff Doozan has a handy script to [install on a Dockstar](http://jeff.doozan.com/debian/)) has an easy to use apt and deb based install system and a full compiler chain really got me thinking. 6 watts, 1.2ghz, 128mb ram, 25$…. Could the Dockstar be the cheaper alternative to the open Pandora handheld I’d been looking for? (Note – I love the openPandora, and what it stands for. Go buy one now!)

**Ignoring Battery, for now**

Although I intend to eventually turn this into a battery powered handheld system, for the initial tests I’ll be running everything off A/C or my car’s DC socket. No battery array has been built for this system yet. I imagine my next build may use a mimo or lilliput usb powered monitor (built-in displaylink chip) instead of the usb->dvi adapter I used for this test. In the future, I’ll be doing some power requirements testing and perhaps some battery engineering for this. Even using this as a console replacement instead of a handheld replacement, the argument is quite strong. This device uses 20-30 times less power than a PS3. So if you’re running off the grid and you want to emulate yourself some Mario Brothers, for the same power usage you get 5 minutes of PS3 or 2.5 hours of the Dockstar.

**Paying Again and Again**

I have been chastised heavily for this believe for many years now, but if you are not legally backing up/dumping the roms for your arcade or cartridge games you are almost certainly costing yourself money. While many consider emulation to be an underground community by its nature, there are quite legal ways for you to enjoy your existing game library without resorting to theft of intellectual property, or worse re-purchasing the games for each platform as they are slowly re-released by the publisher. Support folks like Matthias_H and back up or play your cartridges legally with solutions like the [retrode](http://www.retrode.org/), a hand coded nes rom dumper [like this one](http://www.barkered.com/old-site-content/nes/rom-dumper/), or at least play some [free homebrew roms.](http://dl.qj.net/psp/homebrew-packs-roms.html)

<div class="wp-caption alignleft" id="attachment_846" style="width: 306px">[![Dockstar Running NES and ScummVM over TightVNC](http://66.147.244.180/~hunterda/content/images/2010/11/epicwin1-300x187.jpg "Dockstar Running NES and ScummVM over TightVNC")](http://66.147.244.180/~hunterda/content/images/2010/11/epicwin1.jpg)Dockstar Running NES and ScummVM over TightVNC

</div>**Proof of Concept**

Before running out to my local computer shop and plunking down the 60$ for a decent USB displaylink adapter, I wanted to make sure the Dockstar was actually capable of emulating a couple of systems. After using Jeff Doozan’s debian install script (which disables the pogoplug service, installs uboot, bootstraps debian onto the USB drive etc) I installed VNC server and Xorg (gotta have those fonts!), and started up two separate VNC sessions. In the first, I emulated contra with a nes emulator from the debian repository, controlled via a usb gamepad I had plugged in via an extra USB port gained from plugging in an old IBM USB keyboard with built-in hub. In the second, I used ScummVM to emulate Monkey Island 2 (both of which I have purchased many, many times). I then streamed both of these over the network to my desktop PC, simultaneously. So, concurrently, there was USB gamepad usage, NES emulation , Scummvm emulation, 2 X servers, 2 framebuffers being compressed with jpeg and tightvnc compression, 2 remote console terminals with byobu screen and a TOP processing showing CPU usage… which never pegged out, and natually was mostly spent on the TightVNC server processes. This gave me a bit of confidence when heading out to the store to purchase more hardware.

<div class="wp-caption alignleft" id="attachment_860" style="width: 252px">[![Alsamixer on the Dockstar Debian System](http://66.147.244.180/~hunterda/content/images/2010/11/alsamixer1-246x300.png "AlsaMixer on the Dockstar Debian System")](http://66.147.244.180/~hunterda/content/images/2010/11/alsamixer1.png)Alsamixer on the Dockstar Debian System

</div>**Easy and Cheap- Audio**

The first missing component on the Dockstar is audio. I picked up a SIIC usb soundwave 7.1 soundcard for about 15 bucks at Frys. I’ve seen similar usb audio plugs for 1$ from sites like DX and meritline, but I prefer to shop local the first go-round in case anything needs to be returned. After pluggin it in, the dmesg log said ```
[  146.847548] usb 1-1.4: New USB device found, idVendor=0d8c, idProduct=0103<br></br>
[  146.854467] usb 1-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0<br></br>
[  146.861822] usb 1-1.4: Product: USB Sound Device<br></br>
[  146.867195] usb 1-1.4: Manufacturer: C-Media INC.<br></br>
[  146.873810] usb 1-1.4: configuration #1 chosen from 1 choice<br></br>
[  147.085508] usbcore: registered new interface driver snd-usb-audio<br></br>```

Looked good to me, so I went ahead and installed alsa and some utilities with ` apt-get install alsa alsa-utils apmd alsa-oss mpg123` This worked without a hitch, and alsamixer showed our PCM line out. A quick test with mpg123 determined sound was working fine, no additional setup required. After a reboot however, this was seemingly no longer working? I tried installing libasound2-plugins, which pulls in a good number of prerequisites,. no no avail. Turns out a ` /usr/bin/alsa reload ` was all that was required to get it working again. So watch out for that.

**Getting Ready – Video**

The USB displaylink linux driver and setup has grown in leaps and bounds since last I had looked into it back in 09. I picked up an IOGEAR USB->DVI external graphics adapter for 50$ open box at Frys (serial GUC2020DW6) as it supported 1080p out of the box. I’ve seen these for as low as 30$, though the price fluctuates around 60$ generally. I imagine any usb->vga or direct usb->lcd solution would also work with the same results. That’s what’s great about running a full Debian Linux distribution on this thing, you get a world of device compatibility out of the box. Having wrestled with a similar IOGEAR graphics adapter in the past, I was fairly confident it used the displaylink chipset and driver. Even better, this particular USB->DVI adapter has a standard USB mini female plug on one end. This means we won’t need to waste a port on the Dockstar, as the male USB mini plug is active and fits the adapter. If you can’t manage to squeeze the adapter onto the plug in the current position, it is only a 5 wire cable attached to the plastic casing. Removing the casing should resolve any spacing issues. I just cut a small hole between the 2 existing usb ports and run the micro usb cable through there.

**Video, Continued**

A quick search turned up a nice tutorial on setting up USB multiseat over at [plugable.com](http://plugable.com/2009/11/16/setting-up-usb-multiseat-with-displaylink-on-linux-gdm-up-to-2-20/). While a bit dated, I figured it was roughly analogous to the Dockstar Debian system I had running and should work. After installing module-assistant, I decided to skip the entire tutorial and just try plugging the device into the Dockstar and a (failing) 15″ vga Monitor from ancient times and seeing what happens… Success! It was a green screen with no borders. This means the driver is loaded and working! A quick test of dmesg showed what I wanted to see

<div class="wp-caption alignleft" id="attachment_870" style="width: 306px">[![DisplayLink Green Screen From Dockstar](http://66.147.244.180/~hunterda/content/images/2010/11/IMG_673211-300x225.jpg "DisplayLink Green Screen From Dockstar")](http://66.147.244.180/~hunterda/content/images/2010/11/IMG_673211.jpg)DisplayLink Green Screen From Dockstar

</div>```
<br></br>
[ 4033.407189] usb 1-1.1: New USB device found, idVendor=17e9, idProduct=0059<br></br>
[ 4033.414104] usb 1-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3<br></br>
[ 4033.421500] usb 1-1.1: Product: IOGEAR External DVI<br></br>
[ 4033.426443] usb 1-1.1: Manufacturer: DisplayLink<br></br>
[ 4033.431080] usb 1-1.1: SerialNumber: 009866<br></br>
[ 4033.444201] usb 1-1.1: configuration #1 chosen from 1 choice<br></br>
[ 4033.509436] udlfb: module is from the staging directory, the quality is unknown, you have been warned.<br></br>
[ 4033.532242] usb 1-1.1: dlfb: allocated 4 65024 byte urbs<br></br>
[ 4033.620197] usb 1-1.1: dlfb: set_par mode 1024x768<br></br>
[ 4033.648492] usb 1-1.1: dlfb: DisplayLink USB device /dev/fb0 attached. 1024x768 resolution. Using 3072K framebuffer memory<br></br>
[ 4033.659751] usbcore: registered new interface driver udlfb<br></br>
[ 4033.665909] VMODES initialized<br></br>```

Success! So I skipped ahead to the Xorg configuration

<div class="wp-caption alignleft" id="attachment_881" style="width: 306px">[![Debian XDM Login On the Dockstar](http://66.147.244.180/~hunterda/content/images/2010/11/IMG_67331-300x225.jpg "Debian XDM Login On the Dockstar")](http://66.147.244.180/~hunterda/content/images/2010/11/IMG_67331.jpg)Debian XDM Login On the Dockstar

</div>  
**Video -Xorg**From here, I decided to see if a reboot would bring up a txt console (and perhaps a login?) on the usb monitor. It produced another green screen. This is good, as it means we’ll not have to be manually stopping fbcon from starting on bootup as many guides have suggested. While I’m not sure if it’s necessary, I went ahead and installed pkg-config and xorg-dev, along with fluxbox and xdm. They pull in a lot of good prerequisites from the Debian apt repository, and may come in handly later.

Speaking of guides, I found a nice article on setting up your Xorg on a DisplayLink device [here](http://mulchman.org/blog/?p=90). Not wanting to re-invent the wheel, I build my xorg.conf using his as a template. I tend to setup fluxbox as my default window manager on new devices as I know its memory footprint is quite minimal, and has worked well for me in the past. I decided to go with XDM as the display manager, as it’s a bit more lightweight than GDM but still gets the job done in an easy fashion.

After installing XDM, a reboot producted me with a XDM debian login window! Now edit your .xsession file to contain `exec startfluxbox` and you should be ready for fluxbox. Success! From here it’s all gravy. ScummVM works. NES emulation works. Web browsing, consoles, fluxbox, full windowing systems, etc etc so much working!!

**Playing Games**

- fceu works great for playing NES roms. Make sure you disable openGL or it will not run correctly.
- ScummVM works great out of the box, even with quite large files. Check the video for me playing Monkey Island 3 (1gb game) flawlessly
- Dosbox – Edit your ~/.dosbox/dosbox-0.74.conf and put your install directory as a mount i.e. `mount c ~/dosbox/images/ `
- Mednafen – Make sure to pass the `-vdriver sdl` argument to mednafen or it will be slow. Use alt-shift-1 to auto-configure your joysticks

Anything in the debian repo should work (no guarantees on speed). I managed to install desmume the ds emulator, but it didn’t run faster than 3fps ever, and didn’t seem to do much.

<div class="wp-caption alignleft" id="attachment_905" style="width: 306px">[![OpenArena On the Dockstar](http://66.147.244.180/~hunterda/content/images/2010/11/IMG_674111-300x225.jpg "OpenArena")](http://66.147.244.180/~hunterda/content/images/2010/11/IMG_674111.jpg)OpenArena On the Dockstar

</div>**Installing Programs/Desktop Usage**

- Do yourself a favor and install aptitude and synaptic! This will help you out greatly during package selection and when searching for new libraries/dependencies/emulators/games/etc.
- OpenArena – This is going to be slow! Edit your ~/.openArena/orig/arena.cfg file and change your render mode to zero for best results.

**Moving Forward – The Sky is The Limit**

Having had a chance to test out the OnLive gaming service and console (and having a roku box at home), I am quite enamored with the idea of a tiny game console. When onlive announced they would soon be charging for access to older (possibly emulated) games, I realized that no cheap console solution existed for emulation fans. Moving forward, I believe I or anyone else can easily get SNES, Neo Geo, PS1, and various Mame backends working at full speed. Considering this is a standard debian system at this point, configuration, and for the most part compilation should be fairly painless and minimal. As soon as I can pick up an original Marvel vs Capcom [cps2 board to dump](http://guru.mameworld.info/CPS2_status.html), I’ll be legally playing that on my tv for the first time since the Dreamcast days.


