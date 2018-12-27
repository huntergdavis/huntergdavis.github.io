---
layout: post
title: Building a completely automated, web/ssh/vnc controlled, home automation server
  from a clamshell ibook (with a faulty cd drive) and 10$ worth of elect
date: '2007-12-19 16:33:24'
---


Ok, so i’ve got this old clamshell ibook. The main weakness of these models was the screen, a paltry 800×600 resolution. The main sweetness of the project:

> 1. Control your house lights from your phone, any web browser, any ssh client, etc
> 2. Automate your lights, run complex temperature analysis and face detection.
> 3. Run ubuntu linux, fully support all hardware functions on ppc architecture, failsafe in case of power failure .
> 4. Dns forwarding from easy to remember address.
> 5. Future development: laser calibration.

Ok, first thing’s first, what will we need?  
 1. ibook clamshell  
 2. 1x usb->serial adapter (~1$)  
 3. 1x x-10 heyu compatible adapter (~10$ ebay)  
 4. whatever x10 controllers you’d like (lights, power outlets) cheap on ebay  
 5. any old usb camera should work (firewire maybe? stay tuned!)  
 The ibook has the following specs, but any computer ~ these specs would be fine:  
 366mz g3 ppc proc.  
 368mb ram  
 10gb hdd  
 800×600 lcd  
 1x usb 1.1 port  
 1x firewire port  
 Ok first of all, let’s get linux installed on here. Because the cd-rom drives tend to die in these units, this was the case here. The solution was to burn an ~12mb iso image to a cd – The ubuntu mini ppc.iso image, and keep retrying this boot disk till the laptop booted the cd (about 20 tries). You could also use any other macbook in firewire host mode (check the mac forums for that). The feisty image (works great!, install xubuntu) supports the airport card and the Ethernet port naively, so that was nice. Remember to hold the ‘c’ key on your mac to boot from the cdrom.

 

While you have that running, let’s do some multitasking. First head over to dyndns and get yourself a dns forwarding address (if you don’t want to have to remember your constantly changing ip address). While you’re at the site, check out their guide to inadyn, some cool open source software to update dyndns with your dynamic ip. Also, if you have a router, make sure to forward the ports for whatever services you want (20-25 ssh, telnet, ping etc, 80 or 8080 etc for web, 5090-5092 vnc, etc)

 

Ok so at this point we’ve got an ibook running xubuntu feisty, let’s install some packages. We’ll want to:  
 Rock open a terminal and break out your su hat. sudo aptitude install the following packages and the firewall software of your choice.  
 openssh-server //this is if you want ssh access to your machine  
 inadyn //this will automatically update your dydns  
 tightvnc-server //if you’re into vnc  
 gnome-power-preferences, gnome-power-settings //easy power profiles (i.e. close the lid, blank the screen)

 

Now it’s time to plug in you usb->serial adapter. I broke down and paid 5$ on ebay for one, but I’ve seen them locally for about 1$. In a terminal, cat /var/log/messages, and look for lines like ‘usb 1-1, pl2303 (or your chipset) converter now attached to ttyUSB0’. This is your new serial port, and what you’ll specify to hey-u (software to control your serial port controlled x-10 power line controller). Now go download hey-u. In terminal, run the whole configure/make/sudo make install shebang. The install is pretty user friendly, and they ask you for your serial port (which we got earlier from /var/log/messages). Time to try ‘heyu info’ Fingers crossed…  
 It works!

 

It should be immediately apparent if your device is found, you’ll get firmware info as well.

 

At this point things are coming together. We’ve got remote access from any ssh capable device to a command line interface to all the x10 power devices in our house. Next up, if you have a way to get jar files onto your phone, or your phone has a browser, I highly recommend midpssh from [here](http://www.xk72.com/midpssh/).

 

At this point the sky is the limit, but first thing I recommend is installing a web frontend to hey-u like the one found [here](http://domus.link.co.pt/screenshots/). So for this, we’ll need apache and php. So get your fix with a ‘sudo tasksel install lamp-server’. I also recommend that right after installing apache, you ‘sudo touch /var/www/index.html’, so your web directory isn’t open. How about a fusion of web/ssh access?  
 I recommend grabbing the isnetwork release of mindterm ssh for java applet from [here](http://downloads.planetmirror.com/pub/hobbes/java/apps/isnetworksmindterm1.2.1scp3.zip)  
 Just move everything in the applet directory in the zip into a folder on your website, change the netscape.html to index.html, and you’ve got an ssh client available from any computer that has java. Sweet.


