---
layout: post
title: Wallclock 3.0 - 200x Microscope Edition
date: '2009-08-13 09:50:08'
---


Every once in a while you come across a busted piece of kit that you know you make useful again. This week, it was an ACN Video Phone. For the unknowing, ACN sells ip phone/video phone service bundled to their video phone hardware. On the upside, the resale value is very low. On the downside, this means it’s worthless without the monthly fees.![ACN Video Phone after teardown and reassembly](http://66.147.244.180/~hunterda/content/images/2009/08/Screenshot11.png)… Or IS IT??

  
 First thing I needed to do was determine the features which are available to non-paying customers. Nmap showed an open sip port, and an open admin port whose password I couldn’t find online. So the software hacking route was potentially open. The “screensaver” option worked, with a current calander and ip address being displayed. The “preview” option worked as well, allowing video from the internal camera, and the ethernet connectivity successfully got the date from my local NTP server. . From what I could gauge online, it appears others have tried unsuccessfully to get the external video in to work (indeed it didn’t work for me either…initially). It was time for teardown. I stripped off the outer plastic casing, and began to disassemble the internal components. From a look at the back of the breadboard, it appears that the external video in and the internal camera in are both lead into the same gate.

It couldn’t be as easy as shorting the camera ground could it? Turns out it could. After removing the camera and shorting its ground, the external video input began to accept an ntsc signal. I gutted all non-essential parts, folded the circuit board back in on themselves and re-attached with shorter length wires, and hooked up a 200x digital microscope to the input jack. Quite a handy little device for 15$ worth of thrift store parts and a kid’s microscope. ![paper magnified 200x](http://66.147.244.180/~hunterda/content/images/2009/08/Screenshot21.png) Here’s a snap from a magazine magnified 200x, you can see the individual ink dots. Very cool.


