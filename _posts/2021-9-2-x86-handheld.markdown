---
layout: post
title: The Steamin' Deck, A Low-End X86 Handheld 
date: '2021-09-02 08:33:24'
---

Y'all probably know, I love games.  I'm also way into handheld gaming, portable consoles, processors, embedded systems and retro gaming in a major way.  I pick up every cheap chinese handheld I can find, love my switch, and am just a major portable and retro gaming enthusiast.  So you can imagine my excitement when the Steam deck was announced.  Of course I preordered, hell I've bought everything GPD has ever released.  

However, it got me thinking, pondering, stewing.  More than a little concerned, I realized that we, as an industry and as a culture of gamers, are missing a critical option.  We've taken a wrong turn at the low-end, and it's holding us back.  

We're missing a generation of games. 

See, here's the thing. For the past decade or so, if I pick up a cheap chinese handheld (think 20-60$, my sweet spot), I know what I'm getting.  A dual or quad core processor, probably right around a gigahertz, running an ARM or MIPS instruction set.  Somewhere between 128 and 1gb of ram. an SD Card for storage.  A low-resolution screen.  You've seen these devices, hell they are my bread and butter for fun porting projects.  These are the anerbics, the gpis, the compute module handhelds.  They are varied and sip battery power oh so slowly.  And they top out at emulating consoles from the 90s. (And some GBA, which in my mind is really a 90s console that released in the 2000s.)

We, as a gaming culture, have hit the 'trough of sorrow' when it comes to our low-end devices. There's an entire segment missing in our market.  At the high-end, we've got plenty of competition.  300-1200$ devices, high-end X86 processors that are capable of running the newest (or nearly newest) games at high resolution and high speed. In the mid-range, that's when we switch processor architectures.  Mid-range gaming portables are universally ARM devices, running a low power chipset with an ARM instruction set.  Think the GPD XD, razor android gaming handheld, etc. At the low-end, the market is saturated with cheap MIPS and low-end ARM processors.  Why is this a problem?

The problem is emulation overhead.  We can emulate a PS1 on these low-end chipsets.  To emulate a PS2, still requires a top of the line system.  The top of the line steam deck may still struggle to emulate some PS2 titles. It may be another 10 or 20 years before we can emulate a PS2 on a cheap 50$ handheld, if ever.  And it has been this way for over a decade. 

It doesn't have to be though!  A one gigahertz processor, a gig of ram, if we were running these games directly instead of emulating the original hardware, that would be more than enough!  Indeed, in the following article I show that it is, and there are a great number of PS2-era games I show running in full speed.  You might just be surprised how powerful 1ghz really is.  Interested?  Read on!  

I set about to put together an X86 handheld.  A really shitty one, the lowest end hardware I could find.  I figured, if I can show these games running great on the lowest spec chip available, that'll really prove the point.  I made some mistakes and bad assumptions along the way, while also learning a ton and even challenging some of my own assumptions. 

The section wherein I spec the hardware. 

I started by searching around (I usually start on Hackaday or github) for anyone else who has built an x86 handheld lately.  I found a couple of interesting articles:

[Wherein a hacker uses a stick PC](https://forum.level1techs.com/t/building-a-x86-handheld-gaming-pc/146654)
[Wherein a hacker uses an old laptop](https://hackaday.com/2018/07/12/old-laptop-reborn-as-mobile-x86-game-system/)

This is certainly not a new or novel idea, that's good news!!  

I especially liked the idea of using a stick PC.  Easily upgradeable, many were produced quite cheaply, and standard I/O (hdmi/SD card/ USB/wifi/bluetooth)

I stumbled upon the lowest end intel compute stick. 1gb ram, 8gb rom, intel atom x86 processor at 1.4ghz.  These can be found regularly on ebay for 30$ or so, given that the operating system they come with is fundamentally broken.  You see, the original intel compute stick 1gb/8gb came with stock ubuntu.  Stock ubuntu now requires more than 8gb of space to update, and thus these sticks run out of storage space on intitial boot-up, requiring a new OS.  That's too much work for most users, but no touble for my needs, I'll be installing linux fresh anyway.  

So 30$ into this build, and I make my first truly wrong assumption.  I assumed that for this project a display would need to be 800x600.  Any LCD I use for this project, I'm going to want a 4:3 aspect ratio.  During the time period these games were made, there were really three main resolutions most everything supported.  At the top end: 1024x768.  More common in the mid-range was 800x600.  Finally there was the low-end 640x480, which to my recollection was a more common resolution a bit earlier in the 90s.  (an incorrect assumption on my part)

While I can easily test the compute stick on it's own using my nexdock, it doesn't support those 3 target resolutions.  In order to test the games, I was going to need to pick up a test monitor.  I ended up finding a 4:3 8" security camera monitor that supported 1024x768, 800x600, and 640x480.

OK, so we have display and processing, what about storage?  Well, the 8gb it comes with is certainly enough to install a lightweight linux (I've found that Bodhi is a nice balance of small install size and full features).  I also wanted to know how games perform in other scenarios, whether playing directly from SD card, usb thumb drive, or SSD. The results were surprising!

The section wherein I talk about disk performance. 

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

There are scenarios where having a swap file helps, but that's mostly because of Steam.  For example, when playing the Steam version of Saints Row 2 there's not enough memory to hold both Steam, and Saints row. With 1gb of ram total and 128mb of that allocated towards the GPU, we're sitting around 881mb of usable memory.  Steam can easily use 500mb.  Saints Row 2 does as well.  Enabling swap allows the steam memory usage to get swapped out to disk, at which point you can play the game without major stuttering. 

That said, the real solution here is quite simple.  DON'T USE STEAM.  

Don't get me wrong, I love Steam.  LOVE IT.  I've been on the platform since half life 2 launch day, average about 200 purchases per year since launch, I'm invested in the platform.  Steam however, is not good for a 1gb system.  The webviews are slow, large libraries will take forever to load, and even with 'low bandwidth' and 'low performance' mode turned on, your experience will be poor. Also you won't have enough ram leftover to run most games. 

No, my recommendation here is quite straightforward: [GOG.com](https://www.gog.com) and [Lutris](https://lutris.net/)

I'm a big fan of GOG.  They are invested in preserving classic games, and they release them DRM-free.  It's that DRM that often makes games unplayable on modern systems or via linux/wine/proton, and most Steam games will be drm'd up to hell.  (Props to the folks at DoubleFine, the Steam linux version of Psychonauts is DRM-free!)

I've also recently found out about [Lutris](https://lutris.net/), a community-driven interface for installing windows games within linux via wine.  It automates most of the process, keeps a low memory profile, and the resultant installs are portable across installs (helpful if you're re-installing different versions of linux on the daily, as I was for this article.)






EVERYTHING BELOW THIS LINE IS FROM THE LAST ARTICLE

While I was in the process of porting Johnny Castaway over to RetroFW devices, I got to know a bit more about the firmware, and these devices.  I realized it would be possible to bridge the static usb debugging networks generated by each device.  I show here that even a Raspberry Pi Zero is more than capable of acting as a bridge host for multiple systems. 

As this is a full networking solution, this opens the door to netplay for any emulator or application which supports ip networking.  Yes, multiplayer SNES, GB/GBC/GBA link cable emulation, Doom, cross-platform networking and more are all achievable now.  You can also watch a quick co-op game of Duke Nukem between an RG300 and an LDK game system over at [my YouTube channel](https://www.youtube.com/watch?v=C1WritVPKYI)

<iframe width="853" height="480" src="https://www.youtube.com/embed/C1WritVPKYI" title="RG300 vs LDK" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

First, a little backstory. I love Johnny Castaway. For the past 33 years I've found a way to get it running on every system within arms reach.  Lately that's meant porting the c version to various game consoles. Last week, that meant RetroFW devices like the LDK Game, RG3xx, and RS-97 series of handhelds and arcade machines.  I was having some trouble getting it running, and I had tried everything to capture the error logs.  I had tried graphical pop-ups, file output, nothing worked.  I was getting frustrated, and I began to go through the [RetroFW Source Code](https://github.com/retrofw/) and [documentation](https://github.com/retrofw/retrofw.github.io/wiki/Configuring-a-Toolchain).

When I read that there was a hidden debugging network created when you plug the device into a host, I knew my troubles were over.  I could telnet straight in, execute my binary, and figure out the problem.  The problem, by the way, was that these devices don't ship with an SDL2 library built-in.  They do for SDL1 though, and I had already backported Johnny to SDL1.2, so that wasn't a big deal.  After that, it was smooth sailing. 

Anyway, fast forward a week and I've been thinking about that debugging network all week.  Even though these devices don't support mounting other devices in host mode, they do present a virtual USB ethernet network in client mode.  A Raspberry pi zero costs 5-10$, that's a reasonable cost for a bridge device, barely more than  the cost of a USB cable. I set about to see if it were possible, and it turns out it's ridiculously easy.  Read on as I detail the four files you can edit to enable USB networking (and thus, multiplayer) on any RetroFW device. 

Here's the gist of it. 
- Step 1: Edit the network settings and launch link for RetroFW Device 1
- Step 2: Edit the network settings and launch link for RetroFW Device 2
- Step 3: Enable ipv4 forwarding on your bridge device
- Step 4: Plug it all it, power it all on, and launch
- Success!


First, we'll edit the default network on the RetroFW device we want to be the 'server' for our Duke Nukem multiplayer lan party!  

Mount the filesystem of your first RetroFW device, in this case an RG300, and edit '/etc/networking/interfaces' You're going to want to change the subnet address from 169.254.1.1 to 169.254.2.1.  Your interfaces file will look like

    auto lo
    iface lo inet loopback

    allow-hotplug usb0
    iface usb0 inet static
           address 169.254.2.1
           netmask 255.255.255.0
           network 169.254.2.0
           broadcast 169.254.2.255
           up dnsmasq
           up route add default gw 169.254.2.2
           down killall dnsmasq


Next, update your '/etc/dnsmasq.conf' file to match, like so:

    interface=usb0
    port=0
    dhcp-range=169.254.2.2,169.254.2.2,255.255.255.0,12h
    dhcp-option=3 

Next, let's create a launch link for our duke nukem server launch. (make sure you've installed the RetroFW version of duke nukem 3d, most come with it installed by default.)  Here's what my '/RETROFW/apps/gmenu2x/sections/games/serverduke32.default.retrofw.lnk' looks like:

    title=Server-EDuke32
    description=Duke Nukem 3D port
    icon=/home/retrofw/Ports.Pack/eduke32.opk#eduke32.png
    opk[icon]=eduke32.png
    exec=/home/retrofw/Ports.Pack/eduke32.opk
    params=eduke32.elf -server
    manual=eduke32.man.txt


Next, we'll edit the default network on the RetroFW device we want to be the 'client' joining our Duke Nukem multiplayer lan party!! 

Mount the filesystem of your second RetroFW device, in this case my trusty LDK game, and edit '/etc/networking/interfaces' You're going to want to change the subnet address from 169.254.1.1 to 169.254.3.1.  Your interfaces file will look like

    auto lo
    iface lo inet loopback

    allow-hotplug usb0
    iface usb0 inet static
           address 169.254.3.1
           netmask 255.255.255.0
           network 169.254.3.0
           broadcast 169.254.3.255
           up dnsmasq
           up route add default gw 169.254.3.2
           down killall dnsmasq


Next, update your '/etc/dnsmasq.conf' file to match, like so:

    interface=usb0
    port=0
    dhcp-range=169.254.3.2,169.254.3.2,255.255.255.0,12h
    dhcp-option=3 

Next, let's create a launch link for our duke nukem client launch.  Here's what my '/RETROFW/apps/gmenu2x/sections/games/clientduke32.default.retrofw.lnk' looks like:

    title=Client-EDuke32
    description=Duke Nukem 3D port
    icon=/home/retrofw/Ports.Pack/eduke32.opk#eduke32.png
    opk[icon]=eduke32.png 
    exec=/home/retrofw/Ports.Pack/eduke32.opk 
    params=eduke32.elf -connect 169.254.2.1 
    manual=eduke32.man.txt


Next, we'll enable ipv4 forwarding on our bridge device.  Mount up your bridge device filesystem, in this case our RasPi Zero, and enable ipv4 forward in (at least for debian-esque systems) '/etc/sysctl.conf'.  

Find the line that looks like:

    #net.ipv4.ip_forward=1

and uncomment it to look like:

    net.ipv4.ip_forward=1

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/ip_forwarding.png" width="1126">


For most systems, that's enough.  For raspbian, it doesn't include network manager by default.  Simply run:

    sudo apt install network-manager network-manager-gnome

and you'll be good to plug and play as many devices into your raspberry pi as you like, with no additional configuration. 

Here you can see all of the files you need to edit, across all 3 systems in this scenario, in one photo:

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/retrofw_config_files.png" width="1126">


Finally, let's get it all running.  I use a cheap microSD card I picked up at MicroCenter, and it's not particularly fast.  In this case it takes a full 2 minutes to boot.  Plug the Pi Zero into a power supply, in this case a cheap usb battery pack. I've found that even a cheap usb battery pack will keep this raspi bridge running for many, many hours. At any rate, wait a full 2 minutes before you plug in a device. 

After your bridge device has booted, plug in your first RetroFW device to the RasPi. When the prompt to 'mount filesystem' comes up, hit 'b' for 'charge only', and after 5 seconds the virtual ethernet port will come up with the static IP that you set for the first device. 

Next, plug in your second RetroFW device to the RasPi. When the prompt to 'mount filesystem' comes up, hit 'b' for 'charge only', and after 5 seconds the virtual ethernet port will come up with the static IP that you set for the client.

At this point, provided ipv4 packet forwarding is working properly on your bridge device, your RetroFW devies are fully networked.  You know what that means, it's Duke Nukem 3D time!!

Launch the 'Server-Duke3d' link we created above first.  Select your server options and launch the game proper. 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/duke_nukem_server.jpg" width="1126">


After you're in, you can launch the client link we created above on any other RetroFW devices we're networked to.  Finally, we'll power it all on and get to gaming!

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/duke_nukem_coop.jpg" width="1126">


And that's that.  I've noticed that the RetroFW port of snes9x still has the netplay code compiled in, that's a logic next target for multiplayer gaming via "link cable."  Stay tuned!
