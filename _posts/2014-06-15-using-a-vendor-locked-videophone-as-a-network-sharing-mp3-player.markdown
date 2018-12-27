---
layout: post
title: Using a Vendor-Locked VideoPhone as a Network Sharing MP3 Player
image: http://www.hunterdavis.com/content/images/2014/06/CameraZOOM-20140615151520685.jpg
date: '2014-06-15 20:12:14'
---


The AVN 3000 used to be a pretty interesting platform. Sadly, interest died off as people realized video-calling just wasn’t catching on in the way they thought it would. I picked one up at a thrift store for 12$ today, and decided to get it doing something.

I cracked open the unit, and booted. I started out by setting a static IP address in the settings page. This way it doesn’t look for SIP servers while getting a DHCP address. Didn’t appear to be running SSH/Telnet, so I started to Google around. I then found where some folks had figured out what file the SD card looks for to run scripts on boot, the version of linux it is running, how to chroot to Debian, etc. All with the intention of using the device as a SIP phone (as intended by the original firmware). Yawn.

[![CameraZOOM-20140615122203743](http://www.hunterdavis.com/content/images/2014/06/CameraZOOM-20140615122203743.jpg)](http://www.hunterdavis.com/content/images/2014/06/CameraZOOM-20140615122203743.jpg)

> I decided to gut the device, and see if I could make it really useful.

I found a link on Hackaday where a fellow hacker had gotten an SDL game he had written to boot off the SD card. That’s fun, but no mention of how exactly he got it working. I bet I could get it to play music! But first, let’s get rid of this ugly case!

I ripped out everything but the LCD screen and the motherboard/bottom plastic. Much better! Now I have a system with no USB HID/keyboard support, no input, and nothing but an embedded Linux system that can run arbitrary commands from a script on the SD card. Sounds just about perfect 🙂

[![CameraZOOM-20140615134959354](http://www.hunterdavis.com/content/images/2014/06/CameraZOOM-20140615134959354.jpg)](http://www.hunterdavis.com/content/images/2014/06/CameraZOOM-20140615134959354.jpg)

First, I decided to alter the SD card script to save off a list of all the filesystem contents, environment variables, etc. I wrote an sh script to test out some system parameters, and dropped it into the SD card.

```
<br></br>
#! /bin/sh<br></br>
sleep 5<br></br>
/mnt/sd/testfb &<br></br>
mount -t tmpfs -o size=20m none /mnt/ramdisk```

ls -al /mnt/ >> /mnt/sd/lsResults  
 ls -al /bin/ >> /mnt/sd/binResults  
 ls -al / >> /mnt/sd/fsResults  
 ls -al /usr/sbin >> /mnt/sd/sbinResults  
 ls -R / >> /mnt/sd/lsresursiveResults  
 env >> /mnt/sd/envResults  
 ifconfig -a >> /mnt/sd/ifconfigResults

This provided me with all sorts of good info about the binaries and executables that were already available to me on the system. I was hoping for a system filled with fun executables, so there’d be no need to cross-compile or chroot. There actually were some pretty good utilities on there, so I decided to edit the script and see what else could be done.

First off, I found a ton of interesting things. Madplay for mpeg playback, alsa utilities, exports (NFS….), vi, find, bash and the like. It’s funny how happy I get from a little set of *nix utilities. At any rate, let’s see what fun things we can get into with all this good times.

The Test: Play MP3s from SD card.

For this test I simply dropped an mp3 file onto the SD card. I also added in a check for exports and attempted to start xterm (for future tests.)

I updated the script to be:  
```
<br></br>
#! /bin/sh<br></br>
sleep 5<br></br>
/mnt/sd/testfb &<br></br>
mount -t tmpfs -o size=20m none /mnt/ramdisk```

cat /etc/exports > /mnt/sd/results/exportsOutput

ps -ef > /mnt/sd/results/psOutput

xterm &

/usr/bin/madplay /mnd/sd/2gether.mp3

It didn’t work, but it let me know there were no exports and there was also no sound coming out. Not Great, so I updated the script to set a static IP and attempted to telnet in.

```
<br></br>
#! /bin/sh<br></br>
sleep 5<br></br>
/mnt/sd/testfb &```

ifconfig eth0 192.168.1.69 netmask 255.255.255.0 up

sleep 5

[![CameraZOOM-20140615151520685](http://www.hunterdavis.com/content/images/2014/06/CameraZOOM-20140615151520685.jpg)](http://www.hunterdavis.com/content/images/2014/06/CameraZOOM-20140615151520685.jpg)  
 Success! I logged in as root/root and started to look around. I used alsamixer to unmute, and playback now came from the earpiece on the headset. Good enough for me 🙂

Unfortunately, the company who makes this appears to be in violation of the GPL, and doesn’t release their kernel changes publicly. So I can’t compile a new kernel with controller support without some serious headache. Time to scrap for parts and move on.

So I’ve got yet another embedded system with a locked-down kernel that no-one’s interested in. It’ll happily serve up NFS shares and play MP3s. I’ll likely use the LCD in another project but I think I’m done with closed hardware for now. Just makes me want to use a rasPi or Bunny’s open source laptop instead.

In the meantime, perhaps I’ll use it as another makeshift pirate box, servin up files for freedom. The irony is not lost on me.


