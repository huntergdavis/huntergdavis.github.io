---
layout: post
title: Location-Based Advertising For The Thrifty Hacker
image: http://www.hunterdavis.com/content/images/2014/04/2014-04-06-17.19.57.jpg
date: '2014-04-07 01:50:38'
---


So you’re a budget-conscious hacker looking to advertise. A few years ago this would have been an article about soldering boards and compiling kernels. Not to worry. The world has significantly changed for the thrifty hacker over the last decade. While once you needed to carefully scrounge and make sacrifices for your hack, those days are long gone. This is an article about re-using the ever-increasing horde of technological gold we’ve amassed and discarded en-masse.

You see, unbeknownst to most individuals (but perhaps sensed by everyone), computers and computing devices stopped getting better years ago. Really. The vast majority of tech you had 5 years ago is likely sufficient for anything you wish to do today.

Skeptical? Think about your laptop computer, your television, your network router. The advances of late have been iterative and mostly ignored by the public. Embedded computing devices have become “good enough”. It was 4 years ago I [hacked the dockstar](http://www.engadget.com/2010/11/29/dockstar-freeagent-hacked-into-inexpensive-emulation-masterpiece/) into a gaming console (I really love linking that article, I know.) That was a 1ghz embedded arm processor. These can still be found in current production systems in all walks of computing, from phones to tablets to network routers. The truth is, most computing tasks don’t require the amount of power we have to throw at them. Hence the rise of 20-30$ embedded boards (rPi) with “good enough” processors and low cost of ownership.

So when you’re looking to do something as simple as advertise, the world is your oyster. Simply walk into your nearest thrift store, walk to the electronics section with a 5$ bill, and come out with all the parts you need for your hack.

[![2014-04-06 17.19.57](http://www.hunterdavis.com/content/images/2014/04/2014-04-06-17.19.57-300x225.jpg)](http://www.hunterdavis.com/content/images/2014/04/2014-04-06-17.19.57.jpg)

Here’s what I came out with for my 5$ this time: An ATT Mi-Fi router and a 512mb micro-sd card.

I went with the MiFi router over one of the old hackable WRT routers of which there are literally thousands at local thrift shops throughout Seattle. Seriously, there have to be at least a hundred in one shop alone. We made millions of them and the hardware lasts about 20 years longer than you’d think. Any any rate, the MiFi is quite tiny and is powered via a standard 5v micro-usb cable, so there’s a limited power draw (and there’s potential to power via solar or hand-crank at a later date.) It also has a micro-SD slot, which means we’ll not need to solder on any USB ports as we may have had to do with some routers (though I wouldn’t say *most* routers, USB became a hot selling point for wireless routers in the late 2000s.) In theory it also provides GPS location, but this isn’t of much use to a stationary pirate box (though that does give us a jumping off point for a future pirate box hidden on a boat!)

[![2014-04-06 17.53.11](http://www.hunterdavis.com/content/images/2014/04/2014-04-06-17.53.11-300x225.jpg)](http://www.hunterdavis.com/content/images/2014/04/2014-04-06-17.53.11.jpg)

So we’re looking to advertise something, and we’ve got a tiny sort-of router with some storage. Great! The first thing that comes to mind is a [pirate box](http://en.wikipedia.org/wiki/PirateBox)! While pirate boxes are a great way to share files, they are also an excellent way to share knowledge. Simply drop one in or near a public space, put up a QR code or sign with the Access Point name, and you’re advertising! So that’s just what I did.

**Step 1: Figure Out Your Advertisement**  
 Don’t get hung up on the word “advertisement.” There doesn’t have to be a product, and you don’t need to be shilling anything. For me, I wanted to share my open-source fable, [Oubastet’s Wager](http://www.hunterdavis.com/2014/03/20/oubastets-wager/). It’s a ridiculously small file, so I’ll also add a [Linux install CD](http://www.damnsmalllinux.org/) and a [GParted recovery CD image](http://gparted.org/livecd.php) to the SD card to add extra usefulness for folks.

**Step 2: Know And Prepare Your Device**  
 The MiFi is not a device without its quirks. For one, if you attempt to power the device with a normal USB cable you’ll find that the wireless router providing functionality of the device has disappeared. This is because the data line on a USB cable causes the MiFi to go into ‘modem’ mode. Simply cut the data lines on a regular USB cable, use a USB condom, or find a USB cable with no data lines (Blackberry phones used to come with these.)

A quick Google search reveals that each MiFi device has it’s default password printed on a sticker on the battery compartment. If yours is gone, try “admin”, “mifi”, or “attmifi”. Simply connect to the MiFi network which appears when it powers on, and open a web browser to 192.168.1.1 (the default address).

[![login_to_att_mifi](http://www.hunterdavis.com/content/images/2014/04/login_to_att_mifi-300x50.png)](http://www.hunterdavis.com/content/images/2014/04/login_to_att_mifi.png)

From here, it’s a simple task to login using the default password, go to the ‘file sharing’ section, and enable file sharing for the device.

[![samba_settings](http://www.hunterdavis.com/content/images/2014/04/samba_settings-300x170.png)](http://www.hunterdavis.com/content/images/2014/04/samba_settings.png)

**Step 3: Inform Your Audience**  
 Now that we’ve got a tiny pirate box, how do we let folks know about it? One way is to change the WiFi address to be descriptive like “free story” or “free music” etc. This doesn’t work as well as it used to, as people are wary of strange WiFi networks. A better approach may be to simply post up a QR code that lets Android users automatically log-in. [Here’s a tool](http://www.qrstuff.com/) which lets you do just that. I’d also recommend adding a little blurb about the files you are sharing, their location, and why you are sharing them. You see dear hacker, not everyone searches for samba shares every time they get on a new network, though they *should* 😉

[![samba_share](http://www.hunterdavis.com/content/images/2014/04/samba_share-300x278.png)](http://www.hunterdavis.com/content/images/2014/04/samba_share.png)

And with that, you’ve successfully (and for under 5$) created a location-based advertising solution that costs about 1$/year in electricity to maintain. That’s good times.


