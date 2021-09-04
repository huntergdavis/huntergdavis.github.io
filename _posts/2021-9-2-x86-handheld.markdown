---
layout: post
title: The Steamin' Deck, A Low-End X86 Handheld 
date: '2021-09-02 08:33:24'
featured_img: 'https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/portablepsychonauts.png'
---

Y'all probably know, I love games.  I'm also way into handheld gaming, portable consoles, processors, embedded systems and retro gaming in a major way.  I pick up every cheap chinese handheld I can find, love my switch, and am just a major portable and retro gaming enthusiast.  So you can imagine my excitement when the Steam deck was announced.  Of course I preordered, hell I've bought everything GPD has ever released.  

However, it got me thinking.  That thinking turned to pondering, and stewing.  More than a little concerned, I realized that we, as an industry and as a culture of gamers, are missing a critical option.  We've taken a wrong turn at the low-end, and it's holding us back.

**We're missing a generation of games on the go no longer!**

<iframe width="900" height="600" src="https://www.youtube.com/embed/2uorZ2MeuFE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/portablepsychonauts.png" width="500">

See, here's the thing. For the past decade or so, if I pick up a cheap chinese handheld (think 20-60$, my sweet spot), I know what I'm getting.  A dual or quad core processor, probably right around a gigahertz, running an ARM or MIPS instruction set.  Somewhere between 128 and 1gb of ram. an SD Card for storage.  A low-resolution screen.  You've seen these devices, hell they are my bread and butter for fun porting projects.  These are the anerbics, the gpis, the compute module handhelds.  They are varied and sip battery power oh so slowly.  And they top out at emulating consoles from the 90s. (And some GBA, which in my mind is really a 90s console that released in the 2000s.)

We, as a gaming culture, have hit the 'trough of sorrow' when it comes to our low-end devices. There's an entire segment missing in our market.  At the high-end, we've got plenty of competition.  300-1200$ devices, high-end X86 processors that are capable of running the newest (or nearly newest) games at high resolution and high speed. In the mid-range, that's when we switch processor architectures.  Mid-range gaming portables are universally ARM devices, running a low power chipset with an ARM instruction set.  Think the GPD XD, razor android gaming handheld, etc. At the low-end, the market is saturated with cheap MIPS and low-end ARM processors.  Why is this a problem?

The problem is emulation overhead.  We can emulate a PS1 on these low-end chipsets.  To emulate a PS2 still requires a top of the line system.  The top of the line steam deck may still struggle to emulate some PS2 titles. It may be another 10 or 20 years before we can emulate a PS2 on a cheap 50$ handheld, if ever.  And it has been this way for over a decade. 

It doesn't have to be though!  A one gigahertz processor, a gig of ram, if we were running these games directly instead of emulating the original hardware, that would be more than enough!  Indeed, in the following article I show that it is, and there are a great number of PS2-era games I show running in full speed.  You might just be surprised how powerful 1ghz really is.  Interested?  Read on!  

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/simpsons.png" width="640">

I set about to put together an X86 handheld.  A really shitty one, the lowest end hardware I could find.  I figured if I can show these games running on the lowest spec chip available, that'll really prove the point.  I made some mistakes and bad assumptions along the way, while also learning a ton and even challenging some of my own assumptions. 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/serioussam.png" width="640">

*The section wherein I spec the hardware.*

I started by searching around (I usually start on Hackaday or github) for anyone else who has built an x86 handheld lately.  I found a couple of interesting articles:

[Wherein a hacker uses a stick PC](https://forum.level1techs.com/t/building-a-x86-handheld-gaming-pc/146654)

[Wherein a hacker uses an old laptop](https://hackaday.com/2018/07/12/old-laptop-reborn-as-mobile-x86-game-system/)

This is certainly not a new or novel idea, that's good news!!  

I especially liked the idea of using a stick PC.  Easily upgradeable, many were produced quite cheaply, and standard I/O (hdmi/SD card/ USB/wifi/bluetooth)

I stumbled upon the lowest end intel compute stick. 1gb ram, 8gb rom, intel atom x86 processor at 1.4ghz.  These can be found regularly on ebay for 30$ or so, given that the operating system they come with is fundamentally broken.  You see, the original intel compute stick 1gb/8gb came with stock ubuntu.  Stock ubuntu now requires more than 8gb of space to update, and thus these sticks run out of storage space on intitial boot-up, requiring a new OS.  That's too much work for most users, but no touble for my needs, I'll be installing linux fresh anyway.  

So 30$ into this build, and I make my first truly wrong assumption.  I assumed that for this project a display would need to be 800x600.  Any LCD I use for this project, I'm going to want a 4:3 aspect ratio.  During the time period these games were made, there were really three main resolutions most everything supported.  At the top end: 1024x768.  More common in the mid-range was 800x600.  Finally there was the low-end 640x480, which to my recollection was a more common resolution a bit earlier in the 90s.  (an incorrect assumption on my part)

While I can easily test the compute stick on it's own using my nexdock, it doesn't support those 3 target resolutions.  In order to test the games, I was going to need to pick up a test monitor.  I ended up finding a 4:3 8" eyoyo security camera monitor that supported 1024x768, 800x600, and 640x480. They sell a bunch of similar models, here's there (corporate homepage?) [Eyoyo](https://eyoyomall.com/)

OK, so we have display and processing, what about storage?  Well, the 8gb it comes with is certainly enough to install a lightweight linux (I've found that Bodhi is a nice balance of small install size and full features).  I also wanted to know how games perform in other scenarios, whether playing directly from SD card, usb thumb drive, or SSD. The results were surprising!

*The section wherein I talk about disk performance.*

So, I set about to test PS2-era games on this hardware, using a variety of storage mechanisms.  Here are the results:
- M2 SSD over USB 2.0 port. -> Slow slow slow!  The USB port on these devices is rather limited, and I never saw over 20mb/sec transfer rate.  Random access was anecdotally abysmal. 
- USB thumb drive over USB 2.0 port -> Slow slow slow!  Again, the USB port is the limiter here.  
- SD card via internal SD card slot -> Not bad actually! System boot time is a bit slower compared to internal MMC, but game performance is equivalent.  This was unexpected!
- Internal MMC -> About the same as the SD card slot, just a bit faster on boot.  

To swap or not to swap?  
For the above hardware scenarios, I tested out four different swap methodologies. 
1. No swap at all
2. Swapfile
3. Swap partition co-located on same device as data partition
4. Swap partition on internal MMC, data on separate device.

There are scenarios where having a swap file helps, but that's mostly because of Steam.  For example, when playing the Steam version of Saints Row 2 (or Portal) there's not enough memory to hold both Steam, and a game like Saints row. With 1gb of ram total and 128mb of that allocated towards the GPU, we're sitting around 881mb of usable memory.  Steam can easily use 500mb.  Saints Row 2 does as well.  Enabling swap allows the steam memory usage to get swapped out to disk, at which point you can play the game without major stuttering. 

That said, the real solution here is quite simple.  DON'T USE STEAM.  

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/portalneedssteam.jpg" width="640">

Don't get me wrong, I love Steam.  LOVE IT.  I've been on the platform since half life 2 launch day, average about 200 purchases per year since launch, I'm invested in the platform.  Steam however, is not good for a 1gb system.  The webviews are slow, large libraries will take forever to load, and even with 'low bandwidth' and 'low performance' mode turned on, your experience will be poor. Also you won't have enough ram leftover to run most games. 

No, my recommendation here is quite straightforward: [GOG.com](https://www.gog.com) and [Lutris](https://lutris.net/)

I'm a big fan of GOG.  They are invested in preserving classic games, and they release them DRM-free.  It's that DRM that often makes games unplayable on modern systems or via linux/wine/proton, and most Steam games will be drm'd up to hell.  (Props to the folks at DoubleFine, the Steam linux version of Psychonauts is DRM-free!)

I've also recently found out about [Lutris](https://lutris.net/), a community-driven interface for installing windows games within linux via wine.  It automates most of the process, keeps a low memory profile, and the resultant installs are portable across installs (helpful if you're re-installing different versions of linux on the daily, as I was for this article.)

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/lutris.jpg" width="640">

After trying a great number of combinations of linux distros and window managers, here's how I ended up setting up my linux partitions and install.
- No Swap whatsoever.  
- 50mb (yes megabyte) fat16 EFI partition, first partition of the internal 8gb MMC.  You'll need fat16 here as the minimum fat32 partition size is 256mb
- 7gb (remaining space) ext4 partition, second partition of the internal 8gb MMC.  Mounted as / (root directory of linux filesystem)
- 128gb (or whatever size SD card you have) ext4 partition, first partition of the SD card inserted into the SD card slot.  I use a cheap microcenter U3 SD card (12$)

I went with [Bhodhi Linux](https://www.bodhilinux.com/), for the following reasons:
- Supports fat12/fat16 efi boot partitioning in the installer
- A full 1gb less space used for root filesystem than even #!++ distro(this was a surprise!)
- enlightenment window manager, no screen tearing, low resource usage
- debian based, easy to install Lutris from PPE and steam from .deb package

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/linux.jpg" width="640">

So, at this point we have our Linux base system.  You can do a few things from here. 
- I tend to immediately install vim (I'm spoiled, sorry vi)
- apt install wine and winetricks
- apt install steam_latest.deb (downloaded from store.steampowered.com).  If you're like me, you've got a ton of Steam games, some of which are DRM-free (looking at you Tim Schaefer)
- add the lutris PPA 
- Adjust your screen resolution.  I'll discuss this more shortly, but 640x480 is actually a great resolution for every single game tested.  No need to scour for an 800x600 LCD. 

Let's talk Games!

When I think about the PS2, my thoughts go back to my neighbor who had one.  He had Need for Speed:Underground 2, and he would be playing it every single time I came over.  It was a great game, and "Riders on the Storm" + Snoop Dogg became a touchpoint in our lives.  That was a long time ago now, but it was a blast to play it on the go.  Same with The Simpsons: Hit and Run, Psychonauts, the first Portal and Clive Barker's Undying.  Games I hadn't played in years. 

Here's a video of 2 of these surprise games: Portal and Need for Speed Underground 2

<iframe width="900" height="600" src="https://www.youtube.com/embed/FoPb4Hd53iU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The best part of this project has been getting to actually play all of my favorite games from the early 2000s.  Here's the full list of games I tested, all running at 640x480 

- Psychonauts 
- Need for Speed Underground 2
- Clive Barker's Undying
- The Simpsons: Hit and Run
- Fallout and Fallout 2
- Halo: CE
- No One Lives Forever
- Portal
- Saints Row 2
- Warcraft 3 
- XIII Classic
- Beyond Good and Evil
- Prince of Persia - The Sands of Time
- Rayman 3
- Serious Sam: The First Encounter
- Freddy Pharkas Fontier Pharmacist (bonus, not really a tough game to run)


<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/fallout2.png" width="640">

A word about Psychonauts 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/psychonauts.png" width="640">

You knew this was going to be top of the list this week!  I've been mightly impressed with Psychonauts 2, and it's got me wanting to dive back into the original.  When I found out the Steam version was (1: linux native) and (2: DRM free), it warranted a special mention. 

*Notes ->*
- Version: I installed the steam-linux native version, copied it out of /.local/steam/steamapps/common and into my games directory.
- Visual Settings: 640x480, low detail.  
- Swap concerns: No swap needed. 
- Input: XInput Controller supported

Here's a video I put together, using a direct HDMI capture from the compute stick, showing a few minutes of most of the games mentioned in this article. 

<iframe width="900" height="600" src="https://www.youtube.com/embed/eus8CUsRFEY" title="gaming on the compute stick" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

OK, so I've shown that this chipset is capable of running games that are a generational leap over other low-end handhelds. How cheaply can we put one together ourselves?

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/sandsoftime.png" width="640">

Parts list:
- Intel 8gb/1gb compute stick.  eBay - 30$
- 640x480 5" LCD w/ HDMI compatible controller board and video cable.  26$
- 32gb U3 class microsd, microcenter checkout aisle special.  5$
- generic wireless mini keyboard+trackpad combo, 13$
- 2x 2000mah usb battery packs (one for display, one for CPU), 5$ at any supermarket

So, retail cost using off-the-shelf components, 79$.  How would we bring this price down if we were designing our own system?
- Swap out the keyboard/touchpad for a cheap microcontroller/arduino and some button switches/hats.  Could shave off 5$ here.
- Purchase the LCD controller+display in bulk instead of one-off, the above is sourced from a set of replacement parts for off the shelf LCD displays. Preferably a simpler controller board that eschews the AV/BNC/VGA connections.  Could shave off a few dollars here. and there, but honestly the big savings would need to come in the cost of the LCD, or the SBC used to drive the device.  

So for now, 80$ is the low-end of the DIY 'Steamin Deck'  I'll be keeping my eye on the sbc market, always on the look-out for an affordable, underpowered x86 chipset.  Handheld makers hear my plea, the low-end market is ripe for upheaval!   

With that said, I set about to put together an alpha version of the Steamin Deck using parts I had around my house, and the aforementioned test display. 

First, how to connect a controller?  I have a few clips around, I'll sacrifice one for this project.  A little bit of dremel work later, and we've got a controller clip that'll slide right under the hdmi port.

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/steaminwithcontroller.jpg" width="1000">

As always, there's quite a bit of leftovers once things are assembled. 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/leftovers.jpg" width="1000">

From there, I start to assemble the rest of the parts.  First, I use a u-bend hdmi connector so the compute stick is parallel to the screen.  A rubber bumper keeps it from bending too far. 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/steaminback.jpg" width="1000">

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/steaminside.jpg" width="1000">

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/steaminbacktop.jpg" width="1000">

This seemed precarious, and likely to snap off, so I added a metal bracket to relieve some of the pressure on the controller clip

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/steaminsupportbracket.jpg" width="1000">

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/steaminbackbracket.jpg" width="1000">

From here, it's straightforward.  Boot into Linux and load some games! 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/steamingrub.jpg" width="1000">


<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/portablesimpsons.png" width="500">


Here's a video of Psychonauts now "on the go!" 

<iframe width="900" height="600" src="https://www.youtube.com/embed/Q4a1jqBOFpM" title="Psychonauts Portable" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For an alpha handheld, the Steamin' Deck meets 3 out of the 4 main criteria I have for a handheld
1. Portable
2. Plays the games I want to play, right now
3. It's cheap
4. ~~Fits in my pocket~~

I'm pretty sure I can tackle the pocketability with a few improvements for the next version

1. Use a telescoping game controller, center of gravity above screen. Smaller and no need for the strain-relief bolt.
2. Find some smaller usb battery packs, the one I have at home is gigantic. 
3. Switch from an 8" screen to a 5" screen or smaller. 


Until then, be excellent to each other and game on!
