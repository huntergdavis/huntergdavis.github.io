---
layout: post
title: 15$ for Direct HDMI Input on Oculus Go 
date: '2021-12-09 08:33:24'
featured_img: 'https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/oculus_hunter.jpg'
---
I'm going to come out and say it.  The Oculus Go is my favorite VR headset of 2021, maybe ever.  Yes, [that Oculus go](https://www.oculus.com/go/), the cheap one they don't sell anymore.  I'm currently playing through a [really awesome puzzle game](https://store.steampowered.com/app/1157200/Magnesium_173/) via Steam Streaming to my PC. 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/cables_for_oculus_hdmi.jpg" width="640">

I had my eye on one since launch, but with the ties to Facebook and the Facebook login requirement, I kept my distance.  When John Carmack released a rooted/unlocked firmware for the device earlier this fall, I knew it was time to pick one up. 

You don't need to have a Facebook account, just submit the form to become an Oculus developer and you can create an Oculus account.  This will let you set up the device for the first time (for now, I'm sure an untethered setup hack is coming soon.)

I was really enjoying playing around with it, streaming Steam games from my PC and Xbox games from the cloud.  Retroarch works great, especially light gun games!  (Duck Hunt, House of the Dead, Confidential Mission)

It is not, however, powerful enough to emulate the Switch.  Hell it's not powerful enough to emulate the Gamecube at a reasonable speed.  So how then, am I going to play Metroid Dread on it?  

OK, for sure, I could emulate it on my PC and stream it on over.  That'll work fine.  What if I don't want to emulate?  What if I want to use any HDMI capable device, directly on the Go, without having any wifi or internet connectivity requirements?

Well, as I found out today, I'm in luck.  It cost me about 15$, and no trouble at all!  

You see, dear reader, the Oculus go is essentially a Galaxy S7 crammed into a VR headset.  Not exactly, but close enough.  Now that we have an unlocked and rooted operating system, the sky is the limit!

What we'll do is use a USB OTG cable (remember those?) and a capture card to bridge out the micro-usb to a full USB-A port. 

Take the OTG cable, and plug in the HDMI->USB capture dongle (15$ at Microcenter).  After that, any HDMI device plugs into the input (my particular capture device supports up to 1080p)

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/cables_for_oculus_hdmi.jpg" width="640">

Android supports this form of USB video well, but you'll need to install a viewer application.  There's a well supported (and ad supported) one that I've found works well called "USB Camera - UVC and EasyCap".  You'll probably want to spring for the pro version, or find one without ads.  For this proof of concept, I don't mind if there are ads while I'm testing the hardware. 

You'll need to enable developer mode and sideloading, then side load in your USB capture software.  

Here's a great guide for enabling developer mode and sideloading on an Oculus Go. 

Once we have all of our cables and software ready, plug them into the Oculus

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/oculus_hdmi_in.jpg" width="640">

Open the app, accept the USB camera permission, and you're off to the races!!  Lots of cool applications for this, and the latency isn't horrible! 

That wraps it up for this one, keep an eye out for some fun Oculus projects coming soon on this blog!  

