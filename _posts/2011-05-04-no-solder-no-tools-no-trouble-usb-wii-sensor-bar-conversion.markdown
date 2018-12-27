---
layout: post
title: No Solder, No Tools, No Trouble USB Wii Sensor Bar Conversion
date: '2011-05-04 10:49:47'
tags:
- conversion
- emulation
- hacks-2
- sensor-bar
- usb
- wii
- wii-usb
- wireless-sensor-bar
---


Like many of my readers, I’m excited about the prospect of playing New Super Mario Brothers in 1080p with 16xAF and 8x AA and 3x the internal graphical resolution. Of course I’m not talking about the recently announced Wii 2, but the Dolphin emulator, which is currently running New Super Mario at a crisp 60fps with the above settings on my laptop. The wiimote and accessories connect fine via internal bluetooth, but what about the sensor bar? Turns out if you’ve bought yours recently you may not need anything other than a pair of scissors to convert yours to USB.

[![](http://66.147.244.180/~hunterda/content/images/2011/05/SprintPhoto_bk1aea1-300x225.jpg "Mario Galaxy 2 Emulated with USB Wii Sensor Bar")](http://66.147.244.180/~hunterda/content/images/2011/05/SprintPhoto_bk1aea1.jpg)  
 Read on to find out how!

If you search google for USB Wii sensor bar hack, you’ll find a ton of them. It’s easy to see why. The wii sensor bar is simply a 10-LED IR transmitter running at 7.5V, with no internal logic. Cracking open a Wii sensor bar made during the first few years of the Wii (and when the sensor bar hack tutorials seem to have been written), and you’ll find 2 simple 5-led IR series connected. The majority of hacks either stepped up the USB voltage to 7.5v with a battery or separate USB plug, but that is no longer necessary.

If you crack open a sensor bar made lately, you’ll see there’s been a change in design. I used a stock sensorbar that came with my (used) Wii, but I also purchased another to test (from Deal extreme [here ](http://www.dealextreme.com/p/infrared-sensor-bar-for-wii-3305)) and it also has the new design. That’s particularly interesting, as the product image for the sensorbar on that page shows the original design. Four of the LEDs have been removed internally, meaning there are only three IR emitters on each side of the sensor bar. This is good news, as it means we no longer need the 7.5v line coming down from the wii, and should be able to get by with anywhere from 4.5 to 7 volts. As such, a stock usb line will work.

[![](http://66.147.244.180/~hunterda/content/images/2011/05/SprintPhoto_baexg51-300x225.jpg "3 LED Wii Sensor Bar")](http://66.147.244.180/~hunterda/content/images/2011/05/SprintPhoto_baexg51.jpg)

Take that pair of scissors I mentioned, and snip the sensorbar cable. Also find a usb cable, and snip that too. Twist together the yellow wire from the sensor bar to the silver shielding within the usb cable. Now twist the red wire from the usb cable to the red wire of the sensorbar cable. Tape together if you like, and you’re done. Thirty seconds to make a USB sensorbar (provided you’re cracking open a v2 sensorbar).

[![](http://66.147.244.180/~hunterda/content/images/2011/05/SprintPhoto_bwfef51-300x225.jpg "USB and IR Lines Together R-R Y-S")](http://66.147.244.180/~hunterda/content/images/2011/05/SprintPhoto_bwfef51.jpg)


