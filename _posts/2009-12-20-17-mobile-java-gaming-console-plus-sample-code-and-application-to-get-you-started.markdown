---
layout: post
title: 17$ Mobile Java Gaming Console - Plus Sample Code and Application To Get You
  Started!
date: '2009-12-20 20:32:15'
---


I finally had a few minutes to start working through the new list of ‘to hack’ items this weekend, so I started with the Nickelodean NPower fusion gaming console. Buy.com had these for 17$, and I’ve seen them at various secondhand retailers here in southern California for about the same. It supports j2me, cldc1.1, and midp2. For 17$ this would be a fantastic target for a beginning java games developer. The absolute rock bottom price would allow for some fun opportunities like beta test groups, without the terrible expense usually incurred purchasing mobile devices. ![npower fusion with custom java](http://66.147.244.180/~hunterda/content/images/2009/12/npowerjava1.jpg)

After plugging it in, it’s recognized as a 1gb photo storage device. There are a couple of .wmv videos installed stock, as well as an enticing java_vm folder, which will load .jar/.jad files. My goals were simple, get a custom application running on the Npower, and get some system information and a sample application for other developers to use as an example.

I started by downloading the JavaME SDK. It comes with a few sample applications, I chose the UI demo app as a good starting point. JavaME supports the java.lang.runtime class, so I figured a couple of quick system monitors would be useful. The GaugeDemo seemed like a good starting target, so I built it fresh to ensure it would run on the fusion. It installed and ran fine, so I set about altering the page to display the system memory as it changes. I first added a label to the frame which contained the total and free memory. Looks like the Npower is allocating Java around 2mb of ram. That’s about 10x more than is required by the cldc1.1, and more than enough for some hefty (and fun) mobile java development. As the free memory doesn’t change, I drop the gauge to zero every 3 ticks to show change in memory.  
![npower fusion stock](http://66.147.244.180/~hunterda/content/images/2009/12/nmp4075sbs1.jpg)  
[You can download the changed source files and .jar/.jad file here](http://www.hunterdavis.com/freememuidemo.zip). Just install it to your npower, then navigate to games->UIDemo->gauge, and there’s your memory gauge. Fun! Happy Programming.


