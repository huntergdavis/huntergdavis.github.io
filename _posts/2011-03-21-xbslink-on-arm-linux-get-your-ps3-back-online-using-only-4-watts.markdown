---
layout: post
title: XBSLink on (ARM) Linux - Get Your PS3 Back Online Using Only 4 Watts
date: '2011-03-21 15:05:49'
tags:
- net
- arm
- installation
- libpcap
- linux
- mono
- mono-net
- tutorial
- xblslink
---


As someone who hacks up every console he’s ever gotten, my PS3 has been rocking a Linux enabled CFW for some time now (remember [that tutorial](http://hunterdavis.com/archives/125) I did way back on turning your Linux PS3 into a cross-compilation powerhouse?). As such, I’ve gotten the banhammer from Sony PSN networks, and if I want to play some multiplayer games with my PS3, I’m out of luck except for LAN play. This is fine, as there’s always tunneling applications such as Xlink Kai, or so I thought. It’s been quite a while since I last looked into XLink Kai. This article was originally going to be titled “Xlink Kai Arm Port”, however the XLink Kai developers have decided to close source their project. That’s their prerogative and if they feel it contributes to the quality of their project it’s within their purveyance to do so. That said, it just doesn’t jive with me. One can argue the effectiveness of closed source solutions but at the end of the day Xlink Kai would have had a fully working ARM port working on all the billions of Arm devices today if they had left their source open, because I would have ported it this weekend.

Anyway, things being what they are I decided to get their main competitor (XBSLink) running on the ARM platform. Some of the ps3 [hacker](http://www.ps3-hacks.com/2011/03/19/alternatives-to-psn-game-online-elsewhere/) [blogs ](http://www.ps3hax.net/2011/03/no-psn-try-xbslink-v0-9-2-0/)have been talking about XBSLink lately, and I thought it’d be an optimal application for a little ARM box (a pogoplog perhaps). This will allow you to run the XBSLink daemon on your ARM based Linux box (hopefully pulling 4 watts or less like mine is) and save you the hassle of running a full 400 watt multi core many gigahertz PC for a frikkin port forwarding application. Read on for the setup tutorial. I had gone into this article prepared to walk you through a full compilation and porting tutorial, but it turns out it’s not necessary. Read on for the full guide!

[![](http://66.147.244.180/~hunterda/content/images/2011/03/XBSLink1-300x189.png "XBSLink")](http://66.147.244.180/~hunterda/content/images/2011/03/XBSLink1.png)

**Install Prerequisites**  
 XBSLink requires mono and libpcap, so install them with `apt-get install libpcap-dev mono-runtime libmono-* mono-winforms*`

**Snag the executable**  
 Create a directory for XBSLink and pull the newest Linux tarball with `wget  http://www.secudb.de/~seuffert/xbslink/downloads/36`

**Find the Capture Device**  
 After extracting the executable, execute it with `sudo mono XBSlink.exe -l` to list your capture devices. In my case I’ll use eth0 as the capture device, the first Ethernet port. You’ll also want to find your ipaddress with ifconfig, as you’ll need to pass this value to XBSLink.

**Starting the XBSLink Service – Looking for Clouds**  
 The XBSLink service works by creating private “clouds” of folks in a virtual network. You can list the currently running clouds (and thus the games you can join) once you connect to the service as follows. You’ll need to pass your ip address, the capture device to use, and your nickname to the XBSLink service. You’ll probably also want to use UPNP services, so you’ll enable that with the -u parameter. In my case the ip address of my ARM device was 10.10.0.175, so my command line was `sudo mono XBSlink.exe -u -i eth0 -o 10.10.0.175 -n huntergdavis` Once this is up and running, press c to list the available clouds. Also note the UPNP address that XBSLink maps to, you’ll specify this in your PS3 cloud name (in my case 192.168.1.47). Also note all these PS3 workaround are both temporary and not necessary for use with the Xbox 360.

**Caveats and Workarounds for PS3**  
 You’ll notice that when you list the clouds that PS3 related clouds have their IP address in the cloud name. Currently PS3 systems need to be on the same subnet to play LAN games together. There’s a workaround in progress by the developer, but for now you’ll need to join clouds which have the same subnet as your PS3 (or create your own cloud and let others do the network switcharoo).

**Creating your Cloud and Playing Online**  
 And that’s that. Say you wanted to start up a game of Homefront on the PS3 and let others play with you. Just start up a cloud (specifying your external IP address so others can play with you!) with the following command:  
` sudo mono XBSlink.exe -u -i eth0 -o 192.168.0.175 -n huntergdavis -c "PS3 Homefront IP 192.168.1.47"`


