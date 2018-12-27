---
layout: post
title: webGL + HTML5 Audio  = Web Strobe Tuner
date: '2012-03-14 22:38:25'
---


As some of you may know, I spent the past 8 months or so working at a great little music startup in Los Angeles called Miso Media.  Though I’m moving forward with my own projects up in Seattle, I look back on the work I created there with a terrific sense of accomplishment.  A great deal of my time was spent porting their proprietary FFT, affine transformation, and pitch detection algorithms to various embedded platforms.  I did some fun stuff with openGL texture transforms and shaders, but the real meat of the work I did was in optimizing for embedded platform efficiency.  As such, the porting of their polyphonic pitch detection algorithms to client-side Javascript became a feasible option and the last bit of my tenure at Miso I spent porting the fruits of my optimization efforts to HTML5, Javascript, and webGL.

While you may have used an iOS or Android strobe tuner, or perhaps a multi-thousand dollar real-life tuner, I guarantee you’ve never seen anything like this before.

Miso Media will be officially launching this HTML5 web strobe tuner on their [corporate site](http://www.misomedia.com) before their Shark Tank episode this week.  It uses Flash to provide microphone access until browsers support HTML5 audio in.  For you musicians and vocalists out there, this is huge.  Head over to the web tuner, and use your laptop or PC microphone to tune your instrument on a full stroboscopic tuner in real-time.  Everything happens client-side, with nothing sent to the server and no data usage for users who may be on mobile plans.  There is nothing to purchase, no complex hardware to lug around, and no setup required.

That said, not everybody has Flash and I’m certainly no big fan of Adobe’s business model.  I wrote the web tuner in a completely modular way, with Flash being used for only the most bare minimum of microphone functions.  Because of this, I’ve created a ‘demo’ HTML5 strobe tuner that you can use with audio files.  No Flash is required, but you will need a browser that supports the html5 audio tag (Chrome for now, all other browsers to come soon).  A musician I forwarded this to told me: ‘This is one of the coolest things I’ve ever seen on the web, period.”  I don’t know if it stands up to said proclamation, but I am terrifically proud of my work, and hope you enjoy it.  The code is minified to protect their IP, but my hope is that some future version will be open source as their algorithms change over time.

You can try out the pure HTML5 Strobe tuner [here](http://www.hunterdavis.com/resume/tunerdemo/tuner.html), and you can view it embedded in my impress.JS resume [here](http://www.hunterdavis.com/resume/#/webtuner2).

[![](http://www.hunterdavis.com/content/images/2012/03/Screen-Shot-2012-03-14-at-3.26.43-PM-300x250.png "Screen Shot 2012-03-14 at 3.26.43 PM")](http://hunterdavis.com/resume/#/webtuner2)


