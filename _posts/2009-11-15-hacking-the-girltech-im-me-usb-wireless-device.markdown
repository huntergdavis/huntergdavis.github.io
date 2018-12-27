---
layout: post
title: Hacking the Girltech IM-ME USB Wireless device
date: '2009-11-15 07:34:32'
---


The Girltech IM-ME is a basic usb radio transmiter paired with a small console like device. It was suggested to me on the TP hacking thread I posted up a while ago. Hacking the IM-ME turned out to be an easy reverse-engineer, as there is no crypto to worry about and everything is sent in cleartext hex (everything). For 12$, this makes quite a nice little wireless console device. Read on for the protocol and info on implementing your own driver ![im-me instant messenger device](http://www.hunterdavis.com/im_me.jpg)  
  
 After ordering the IM-ME as a filler item on Amazon (what won’t I do for super-saver shipping), I plugged it in to my linux box. It was recognized as a standard HID device. This is good, as Girltech obviously didn’t go to any great lengths to protect the communication coming off this thing. At this point, I could have either loaded up a windows VM with a promiscuous USB driver at the host OS level, or loaded up a windows VM with snoopypro installed. I went (as I usually do when reverse-engineering usb protocols) with snoopypro. The output driver strings are quite easy to read and patterns are colored by communication direction.

I set up a user ‘toastc2c’ with a password ‘password’. The default software install (windows only) is basically an online multiplexer. You log into their software, which syncs with their website. Each instant message is sent to the handheld with a identifier string, which is used by the device to pagify the different messages. This is great, as it’s pretty much arbitrary as to what we pipe down to the device. I figured I would need to inject some custom messages to the device (standard crypto protocol breaking stuff like huge messages and repeated characters etc) to get a handle on the communication scheme, but that wasn’t really necessary. Turns out it’s all clearhex, all the time. Either initialize with a VM and inject your own messages, or copy the init strings out of the spreadsheet I post below and init/multiplex with libusb.

[Here is a spreadsheet](http://www.hunterdavis.com/immeusblog.log.ods) with the initialization strings and username/password authentication. This is more than enough to write an interface driver in with libusb. I’m not sure about the DMCA implications of releasing a driver, but there’s a script out there to ease the process for you if you’re new to it. Note the device receives data in one hex byte strings which are each padded with hex 00. My username is ‘toastc2c’, which you can see is clearly transmitted and accepted by the receiving device (IM-ME usb dongle->console pairing). Happy Hacking


