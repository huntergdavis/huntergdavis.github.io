---
layout: post
title: Chromecast your LPs With a Little Help From WebAudio
image: "/content/images/2017/07/justtheeq.png"
date: '2017-07-24 01:23:27'
---

As it usually does, this all started in the thrift store. I was perusing the usual DVD racks and furniture when something caught my eye.  It was an ion USB turntable, the kind with no speakers.  These types of cheap turntables clutter the electronics sections of most thrift stores, as the replacement needle is generally more valuable than the turntable itself.  Nevertheless I decided to take a look.

![](/content/images/2017/07/IMG_20170723_170150.jpg)

Lo and behold, the needle still had the plastic sleeve on, and had never been used, for 5$ I was in!  One small problem, as I generally listen to my music through a Chromecast audio device, and I'd like to be able to cast this from my Linux desktop. For some strange reason, you can't currently cast a Linux desktop to a Chromecast audio device.  

![Why must you hurt me when I love you so Chromecast Audio](/content/images/2017/07/IMG_20170723_170213.jpg)

What to do?  Hack it somehow!  We've only got one connection on this thing, and that's a USB out, so we're talking a software hack. 

![](/content/images/2017/07/IMG_20170723_170154.jpg)

I realized that if I could get a tab broadcasting the audio, then I'd be in business, as you can cast a tab to a Chromecast audio device? (I know right, I should just VNC in from a tab or something) I quickly found an [HTML5 audio demo using some open source tech](https://webaudiodemos.appspot.com/AudioRecorder/index.html) I could hack up to play the audio as it was coming in.  

After downloading the source code, I began to dig in.  Simple HTML and Javscript, just how I like.  For ease of use and sharing out you can try this on my GitHub Pages [here](https://huntergdavis.github.io/loopbackHTML5Audio/index.html). 

The solution was simply to add an audio output destination node to the webaudio processing workflow.

![](/content/images/2017/07/propstoatomeditor.png)

And that's that!  I can listen to my records and Chromecast them to Chromecast audio devices. 

![](/content/images/2017/07/Screenshot-from-2017-07-23-18-16-32.png)
 