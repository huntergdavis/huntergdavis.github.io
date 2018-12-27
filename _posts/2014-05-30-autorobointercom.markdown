---
layout: post
title: AutoRoboIntercom
image: http://www.hunterdavis.com/content/images/2014/03/speaknow.png
date: '2014-05-30 04:22:04'
---


[![choo-choo-choose](http://www.hunterdavis.com/content/images/2014/03/choo-choo-choose-168x300.png)](http://www.hunterdavis.com/content/images/2014/03/choo-choo-choose.png)

I’ve finally figured out what folks can do with those 4-year old Android phones, and I’ve just finished writing up version .01! Announcing my newest “pet project” [AutoRoboIntercom](https://github.com/huntergdavis/AutoRoboIntercom)!

First Version and Backstory:

AutoRoboIntercom is your basic auto-discovering intercom system, with a twist or two. It can be used without an internet connection, and won’t compromise your security.

Simply load AutoRoboIntercom on your Android 2.1+ device and connect it to your Wifi network. You now have a robotic intercom system. That’s it, no configuration necessary (though you can set your room/user name from the menu.)

[![nokeyboard](http://www.hunterdavis.com/content/images/2014/03/nokeyboard-168x300.png)](http://www.hunterdavis.com/content/images/2014/03/nokeyboard.png)

You can type or talk (speech to text) and it will be broadcast to all connected clients on the network. Clients hear “(Name) said (Message)”.

This means AutoRoboIntercom can be used as an intercom system using old phones around your house, or an ‘around-the-house’ type intercom system using the phones in your pocket. You never need to think about domain configuration or pay for some proprietary software that will probably spy on you later.

So for example you’re in a house with 5 rooms, named:  
 Hunter’s Den  
 The Garage  
 Sallie’s Room  
 Jen’s Room  
 The Kitchen

Hunter has just finished work on his latest app, and wants to let the rest of the house know it’s done. He taps the ‘record’ button in AutoRoboIntercom on his ancient HTC Hero Phone (Android 2.1) and says “Hey everyone! Come check this out I just finished an app!”

[![speaknow](http://www.hunterdavis.com/content/images/2014/03/speaknow-168x300.png)](http://www.hunterdavis.com/content/images/2014/03/speaknow.png)

Sallie, Jen, Mom, and Ben (working in the Garage) all hear:

“Hunter’s Den said “Hey everyone! Come check this out I just finished an app!”

Everyone hears this message read to them in the text-to-speech voice which is installed on their various Android phones throughout the house. They know who said it, so they’ve got the context and know just where to go. Some reply with a “be right there!” while others just run down to the den. Hunter hears the replies in proper queue order without worrying about having to say “over” or messages coming in simultaneously like on the walkie talkie system he had back in the 1980s.

This is all working today. Right now. Ready to go. This is done now, and the era of AutoRoboIntercom is now.

[![keyboardpopped](http://www.hunterdavis.com/content/images/2014/03/keyboardpopped-168x300.png)](http://www.hunterdavis.com/content/images/2014/03/keyboardpopped.png)

/begin technical discussion

One of the cool things about AutoRoboIntercom is that it’s my first public project to use the [Gradle](http://www.gradle.org/) build system. Those who are not using Gradle should still be able to compile just fine, and I’m not using any external libraries.

AutoRoboIntercom came about as a result of my desire for an easy to use intercom system which absolutely had to meet the following criteria:

1. Free and Open Source
2. Easy to Use
3. Easy to Demonstrate (for pedagogy)
4. Easy to Build Upon
5. Does NOT require internet access

I had no desire to bring in all of UPNP just for the discovery protocol, and I believe the file streaming aspect is based on http file directory protocol anyway. Likewise I had no desire to pay for a product which could potentially spy on my home or required internet access to use. AutoRoboIntercom requires Wifi, but does not require internet access. Both speech-to-text and text-to-speech libraries can be installed for offline use. This means the security conscious can install a separate WiFi network with no upstream internet access!

I have big plans for AutoRoboIntercom. I separate these into two categories: obvious upgrades, and not-so-obvious upgrades.

Obvious Upgrades

- Audio/Video data
- Chat Log
- Selective Broadcasts (Just send to these X clients)
- Photo/URL sharing

Not-So-Obvious Upgrades

- Tasker/Pushbullet/Muzei Integration
- Content Provider to Allow Any Program to Send A System-Wide Message
- Plugin System
- Hardware events support (see Tasker integration above)

> You could have the system’s currently playing music information broadcast out to clients as they detect your sender’s bluetooth mac address. Your music could literally follow you around the house…

Think of the possibilities! With Tasker alone comes some really wild functionality. You could use AutoRoboIntercom to message the house when one room’s temperature goes too high/low. You could have the system’s currently playing music information broadcast out to clients as they detect your sender’s bluetooth mac address. Your music could literally follow you around the house…(I mean, I DO work on Rhapsody Android client… maybe I should do this one first)

That’s some good times there!

Update 1:

AutoRoboIntercom has been updated to include the underpinnings of a remote command protocol, as well as the first example “Battery Monitor”.

Simply click on any of the clients in the client list, select ‘Battery Level’, and you’ll shortly hear a voice say to you “The Battery in “Room Name” is X Percent Full”.

Under the hood there’s a network call/response mechanism between the clients requesting battery info from each other and filtering out unnecessary messages. In this way it is much like the token-ring networks of days long past.

As usual it’s fully open source on [GitHub](https://github.com/huntergdavis/AutoRoboIntercom). For those interested, there’s some very straightforward code involved and it starts us off on the path of automatically connected remote clients with a range of capabilities, my original design for AutoRoboIntercom.

You can download a pre-compiled apk [here](https://github.com/huntergdavis/AutoRoboIntercom/raw/master/artifacts/builds/AutoRoboIntercom-debug-unaligned.apk).

You can also download at the [Google Play Store](https://play.google.com/store/apps/details?id=com.hunterdavis.autorobointercom)

https://play.google.com/store/apps/details?id=com.hunterdavis.autorobointercom


