---
layout: post
title: AutoRoboIntercom Updated With Remote Command Protocol, Battery Monitor
image: http://www.hunterdavis.com/content/images/2014/03/choo-choo-choose.png
date: '2014-03-13 04:55:16'
---


[![choo-choo-choose](http://www.hunterdavis.com/content/images/2014/03/choo-choo-choose-168x300.png)](http://www.hunterdavis.com/content/images/2014/03/choo-choo-choose.png)

AutoRoboIntercom has been updated to include the underpinnings of a remote command protocol, as well as the first example “Battery Monitor”.

Simply click on any of the clients in the client list, select ‘Battery Level’, and you’ll shortly hear a voice say to you “The Battery in “Room Name” is X Percent Full”.

Under the hood there’s a network call/response mechanism between the clients requesting battery info from each other and filtering out unnecessary messages. In this way it is much like the token-ring networks of days long past.

As usual it’s fully open source on [GitHub](https://github.com/huntergdavis/AutoRoboIntercom). For those interested, there’s some very straightforward code involved and it starts us off on the path of automatically connected remote clients with a range of capabilities, my original design for AutoRoboIntercom.

You can download a pre-compiled apk [here](https://github.com/huntergdavis/AutoRoboIntercom/raw/master/artifacts/builds/AutoRoboIntercom-debug-unaligned.apk). This still doesn’t feel ready for the play store.


