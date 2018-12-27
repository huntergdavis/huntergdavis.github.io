---
layout: post
title: 90's Tech to The Rescue (network monitor)
date: '2010-05-10 14:25:33'
tags:
- hacking
- linux
- netgear
- networks
- palm
- paperclips
- serial
---


Like many of you, I am throttled by the uplink speed of my network. Unfortunately, my upstream router (which also supplies my HDTV channels) is supplied by my ISP, and I do not have root access. The cable company also doesn’t release metrics for line usage, data transfer for television shows, etc. Fortunately, it uses standard ip networking over Ethernet. I ended up using a 90’s era netgear router and an old Palm V to display link statistics, throughput, etc. The connection was made using paper-clips…. more info after the break!

![palm v router information](http://www.hunterdavis.com/palmvrouter.jpg)

The netgear 314 I had in my closet is actually a re-branded ZyXEL Prestige 314. This is nice as it comes with a serial terminal interface already set up. By inserting this router into your network between your router and the upstream port you can easily set up a syslog rebroadcaster to a linux box on your network. That’s the easy way…..

As I also had an old Palm V sitting around, I figured it’d be more fun to do it the hard way. There’s an old serial terminal program for palm called ptelnet that I recommend. It has macro functionality, so also I recommend setting your macros to be your favorite system info commands for the Zyxel interface (net show tables, ip address, etc).

If you’ve got a null modem cable around (f-f adapter) you can plug straight in. Otherwise you’ll have to roll your own. Lucky for us the serial protocol only needs 3 lines (power, rx, tx (pins 2,3,5)). The netgear expects hardware flow control to be on, so you’ll also need to bridge those lines as well (pins 7,8). I used paper clips (dangerous!!!!), but I would recommend using shielded wires.

Once you’ve got all your pins connected (or swapped depending on your cabling..), fire up your terminal emulator and power on your router. You’re all set to get all sorts of nice statistics your ISP may not want you knowing about.


