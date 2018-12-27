---
layout: post
title: Rhapsody for Android Gets An Equalizer
image: http://www.hunterdavis.com/content/images/2013/10/2013-10-27-10-59-46.png
date: '2013-10-27 18:15:17'
---


I don’t often post up about what I’m doing in the industry. Hell these past few weeks I haven’t posted up much at all. I’m sure my readers are wondering why I haven’t posted a game review in almost as long. The answers are twofold:

1. I’ve been playing through the original Saints Row (2006) and am slowly preparing that review.  
 2. I’ve been tweaking the new audio equalizer I wrote that comes with Rhapsody for Android.

[![2013-10-27-10-59-20](http://www.hunterdavis.com/content/images/2013/10/2013-10-27-10-59-20-168x300.png)](http://www.hunterdavis.com/content/images/2013/10/2013-10-27-10-59-20.png)

Working for a large service-based company like Rhapsody, I get to write a lot of cool features that go out to a million+ people. Just this latest release I implemented three different sets of video APIs and an audio equalizer. That’s the one I’m most excited about, my new audio equalizer that comes with our Android client. It’s something that our users have been asking for forever, and it touches on some of my favorite areas of expertise.

I’ve written many times before about the various audio engines I’ve written in the past. Some are locked away in the IP of huge corporations/universities/governments, some are open source on my GitHub page, some are lost to the winds of time. That doesn’t concern me as much as you might think. Like our own DNA, the underlying code for most major audio engines is 99% the same across all vendors. Those little differences almost always comes down to a combination of hardware specific functionality, and hardware specific workarounds.

Our EQ is no different. I spent quite a bit of time patching, bugfixing and re-factoring initialization routines and audio event handlers to ensure a consistent, excellent experience across Android devices. And now that it’s out, I find myself adjusting levels and showing it off to whoever I meet. My RK3066 Android-TV stick is finally getting some much needed love. I finally have a decent equalizer that I can use in my car. It’s absolutely a 100% better experience, and it’s been pushing my own daily listening hours up ever higher.

[![2013-10-27-10-59-46](http://www.hunterdavis.com/content/images/2013/10/2013-10-27-10-59-46-168x300.png)](http://www.hunterdavis.com/content/images/2013/10/2013-10-27-10-59-46.png)

And how do our users find the results of my (and our most excellent test team’s) effort? I’ll let the bevy of 5-star reviews that have started to pour in speak for themselves.

[Try it for yourself](https://play.google.com/store/apps/details?id=com.rhapsody), if you’re so inclined, and let me know what you think. I’ve got a ton of great ideas for new features, and some really big stuff coming out here in a month or so. That’s good times.


