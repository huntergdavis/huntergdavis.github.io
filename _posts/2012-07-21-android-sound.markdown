---
layout: post
title: Adding New Features to your Old Games and Apps using Android Libraries - Part
  1
date: '2012-07-21 00:58:33'
---


About a year ago, I wrote many, many Android apps. Some of them were games. All of them were written under a “one app in one day” constraint and as such the games never had any sound. No sound effects, no background music, no waveform generation, nothing. Fast forward a year and they’ve all become open source on GitHub. I’d wanted to update them all while re-using as much code as possible. How then was I to maximize the effect (all the games get all the features) while minimizing the effort of adding sound to all of those previous games simultaneously? And how best to share the effort with other Android programmers? In this, the first of a three part article series, you’ll find out. For part 1, I create the project, setup the environment, make a plan, and update the waveform generation code on my currently in-market apps. You can follow-along with this article series in real-time by watching the commit log to the [Android Simple Game Audio](https://github.com/huntergdavis/Android_Simple_Game_Audio) project on GitHub. And stay-tuned for the upcoming part 2, wherein I become a Foley artist and make use of some interesting and (not quite) antiquated technology.

[![](http://www.hunterdavis.com/content/images/2012/07/soundatlast-1024x404.png "soundatlast")](http://www.hunterdavis.com/content/images/2012/07/soundatlast.png)

**[Creating an Android Library Project](http://www.hunterdavis.com/2012/07/21/android-sound/#a1)**  
**[Including an Android Library Project in Your Android Project (Yo Dawg)](http://www.hunterdavis.com/2012/07/21/android-sound/#a2)**  
**[Planning (Knowing Exactly What You Want To Accomplish)](http://www.hunterdavis.com/2012/07/21/android-sound/#a4)**  
**[Iterating (One Feature At A Time)](http://www.hunterdavis.com/2012/07/21/android-sound/#a5)**  
**[Low Bar: Waveform Generation](http://www.hunterdavis.com/2012/07/21/android-sound/#a6)**  
**[Update Your Markets and Ad Copy](http://www.hunterdavis.com/2012/07/21/android-sound/#a12)**  
**[Mid Goal: Sound Effects](http://www.hunterdavis.com/2012/07/21/android-sound/#a7)**

**[Creating an Android Library Project]()**

This is a good time to talk about workspace organization. Whenever starting a new project that is going to touch a bunch of my other projects, I like to create a new development workspace. As I use eclipse for Android development, this has the effect of lowering my overall build-all time (as only relevant projects are in the workspace to be built). For this project, I picked the 13 most relevant Android apps that contained patterns or code I was likely to re-use.

This tends to confuse people, but Android library projects are simply regular Android projects with the ‘is Library’ flag set. You’ll still need to declare any activities you create in the manifest, but for the most part you can simply tick ‘is library’ during your project setup and you’re good to go.

[![](http://www.hunterdavis.com/content/images/2012/07/islibrary-300x167.png "islibrary")](http://www.hunterdavis.com/content/images/2012/07/islibrary.png)

**[Including an Android Library Project in Your Android Project (Yo Dawg)]()**

Now that you’ve created your library project, you’ll need to include it in your other Android apps. Fire up Eclipse, open up the project properties and head down to the ‘Android’ tab. Scroll down to the ‘Library’ section, select your previously created library project as a ‘library’ and you’re good to go.

**[Planning (Knowing Exactly What You Want To Accomplish)]()**

Sometimes the hardest part of a project is figuring out the features you *don’t* want to implement. Gather up all the projects that you’ll wish to use your library, and consider the features they’ll need. There should be a base feature set that emerges across all projects. That is your first release. For the ‘Easy Sound Manager’ library, there were three main features I needed.  
 1. Waveform Generation (code re-use from Super Whistle)  
 2. Sound Effects (with thread pool etc, code re-use from Easy Sound Board/AirBeats)  
 3. Background Music (intelligent handling, code re-use from AirBeats)

**[Iterating (One Feature At A Time)]()**

Like a recursive algorithm or a marathon runner, you’ll need to start somewhere and push forward hard if you’re going to get anywhere. I like to split feature implementation up into daily chunks that I can finish up in what little spare time I get. For this project which featured three main feature sets, it was an easy workload to divvy.

**[Low Bar: Waveform Generation]()**

Quite a few of my apps were waveform generators of some sort, so I first set about to take the waveform generation from ‘Super Whistle’ and port it over to my ‘Easy Sound Manager’ library. Super whistle was using a simple runnable wrapped from within a ‘play frequency’ function. I ported that over, made it a bit more generic (adjustable playtime), and added a couple of niceness functions for ‘play note’ and ‘play random note’. I also switched from using threads to using asynctasks, which are recommended for background operations with easy thread management. Once I had implemented these new features, I set about to back-port this into Super Whistle.

First, I added ‘EasyAudioManager’ as a library class to Super Whistle. I then removed all audio manager classes and references from Super Whistle, and hooked up the new ‘Easy Sound Manager’ class. I then made sure that the ‘stop’ button was still being handled by the implementation, and proceeded to update GitHub and Google Play Market with new code and binaries.

**[Update Your Markets and Ad Copy]()**

When updating a game or app for the Google Play Market, it’s a good idea to update your ad copy and version numbers, strings, etc to reflect your newly added features. Also note that the simple act of making the app smaller, faster, more intelligent on the back-end, etc are totally acceptable features for releases. Release often to keep momentum, as they say. You may want to update your Ad Banners to include a ‘NEW FEATURE HERE!’ stamp or sub-banner. These sorts of things may seem cheesy but they do catch the eye, just make sure to keep it informative. A user can understand a red ribbon banner with a new feature if it’s informative to them. Keep it descriptive and positive with short info-packed sentences like “Now with Audio!”, “New Sound Effects!”, “Faster Audio Engine!”, etc.

With one project already updated in the Play market and the ‘Easy Audio Manager’ library coming along nicely, it was time to move on to planning for the ‘mid-goal’: Sound Effects.

**[Mid Goal: Sound Effects]()**

For me, an open source sound effects library needs to include features that make it stand out or more usable than the competitors. This is difficult in the case of a game sound library as Google has gone to great lengths to make writing simple audio (not real-time or analysis etc, but simple audio) effects and background music trivial. Most implementations will be little more than wrappers around SDK examples and bug fixes for various platforms. That being the case, I think that the inclusion of actual sound effects I’ve created and released under a Creative Commons license will help make this a useful contribution. What that means is even if you’re not interested in the source code or waveform generators etc, you can still download the project and use all of the bleeps and bloops that I create in your own projects, for FREE, forever. So if you’re playing one of my games, and you hear a ting or a hi-hat or a roaring ‘Game Over’; that’s actually me in my kitchen with some pots and pans and spoons and a microphone cooking up some mischief (like 90s west coast rap). Same goes for when you’re jamming on the background music. That’ll be out there too (Part 3 of this article series will cover background music). One will just need to head to the [Easy Game Audio project on GitHub](https://github.com/huntergdavis/Android_Simple_Game_Audio) to grab the newest set of files. But how to capture these sounds in a clear and clean way, using easily accessible audio editing software (open source, of course!) and the hardware I have around my workbench (well ok, a [laptop stand](http://www.hunterdavis.com/2012/04/25/quick-pro-tip-add-a-tablet-holder-to-your-laptop-table/))?

For the answers to those questions, you’ll have to wait for part 2 of this article series. Coming soon! And remember, if you’re itching for the next article and you’re wondering how things are coming along, you can always grab the latest source code from the project’s [GitHub page](https://github.com/huntergdavis/Android_Simple_Game_Audio).


