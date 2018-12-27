---
layout: post
title: Remixing Open Source Games With Creative Commons Content
image: http://www.hunterdavis.com/content/images/2014/11/device-2014-11-26-193651.png
date: '2014-11-27 03:48:49'
---


One of the great things about open source is that you’re free to modify and redistribute it in whichever way you like. This is real creative freedom that I support. All of my apps and games are open source. A while back, I helped fund the [opening ](http://open.commonly.cc/)of some game music and art assets to the public. Being in the public domain (or having a Creative Commons license as these art assets now do) allows for public remixing and free use of the content. Gotta love that.

Fast forward to this week. I was relaxing on a short stay-cation, playing games and watching TV, and I began to think to myself: “Why not remix one of my games with some of this new creative commons content?” So that’s what I set out to do. You can grab the latest source code from the GitHub page [here](https://github.com/huntergdavis/cantstoptherock). Here’s how it’s looking right now: (**Note any ghosting or slowdown you see is an artifact from screen capture)

<iframe allowfullscreen="" frameborder="0" height="525" src="https://www.youtube.com/embed/6Uj_0MR8Ty8?feature=oembed" width="700"></iframe>

I started by copying the base of my last game, [Pop Them Balloons](https://github.com/huntergdavis/PopThemBalloons). The source is heavily commented, and uses my high-level abstraction libraries to make basic game design a very straightforward task. Title/Credits screens are one-liners in code. This allows me to concentrate on the base gameplay mechanics and refine the core experience without worrying about scrolling end credits text or background music etc.

The concept for my new game “Can’t Stop The Rock” is quite simple. It’s a casual game flipped on it’s head. You play “the level”, dropping balloons that quickly scroll left towards “the rock.”. The rock rolls around the screen dispatching your balloons. I’ll add weapon upgrades and various mechanics from my previous action games for the rock to execute while you drop balloons. The “goal”, if there is one, is to get balloons past the rock. I want the game to be so fast and slick, 60+fps at all times. And I’m going to do it without resorting to native code or OpenGL.

[![device-2014-11-26-102558](http://www.hunterdavis.com/content/images/2014/11/device-2014-11-26-102558.png)](http://www.hunterdavis.com/content/images/2014/11/device-2014-11-26-102558.png)

I kept the balloon abstraction from “Pop Them Balloons,” as well as the difficulty selection screen and the basic game panel structure. Balloons now update to float right to left instead of bottom to top. I also updated the base project to use Gradle as the compilation system.

The rock started out as a simple green circle for prototyping. He slowly moved towards the balloons and didn’t do much else. While I knew it was time to design a better AI system for our little hero, I took some time to start removing the ‘Pop Them Balloons’ branding and music.

I used a slick gradient in [Pinta ](http://pinta-project.com/) to create the icons, title screen, and speed settings buttons. Things were already starting to seem like a very different game.

First, it was time to upgrade the audio. Pop Them Balloons had three main songs, a title theme, a credits theme, and a game theme. I’m going to upgrade that to five songs for Can’t Stop: a title theme, a credits theme, and three game themes. I updated the code to change the game theme depending on the difficulty selected, that way you can have a more casual experience on more casual game modes.

And here I ran into my first creative editing situation. I felt the ‘game over’ theme from HalyconFalconX would make for a great title them on Can’t Stop The Rock… Except for the inclusion of “Fail!” at the end of the song. Not to worry, I opened up Audacity (my favorite open source MP3 editor) and clipped it out of the waveform. That’s the sort of thing you can do with open content.

[![audacity](http://www.hunterdavis.com/content/images/2014/11/audacity.png)](http://www.hunterdavis.com/content/images/2014/11/audacity.png)

I wanted the action to be fast and furious, so I went with high BPM tracks and removed some graphical flourishes for now.

<iframe allowfullscreen="" frameborder="0" height="525" src="https://www.youtube.com/embed/dBl-0xNH544?feature=oembed" width="700"></iframe>

From here I updated the background to pulsate through a known list of pleasant colors, and updated the little rock hero to actually pop some balloons as it crossed them. The gameplay is very fast paced, so much so that my video encoder gives me ghosting when screen capturing on my aging nook tablet.

<iframe allowfullscreen="" frameborder="0" height="525" src="https://www.youtube.com/embed/RS_y7JrntAQ?feature=oembed" width="700"></iframe>

I think some of the best casual gameplay comes around the use of sound and audio to immerse the player in the experience. With that in mind, I set out to add some musical fun to the game. My first thought was to include midi playback, but there’s too much baggage. I ended up heading over to freesound.org and downloading a set of guitar chords, then arranging the play screen into note quadrants. It makes for some interesting music opportunities.

As you can see, as each balloon is placed onto the screen it is painted with a note. This is the note that plays if it gets popped. Right now it doesn’t seem much like most games, and it doesn’t play like most instruments. Pretty fun stuff, and a lot of cool directions to take this in the near future. Next time perhaps I’ll play with the mechanics of color and sound, or add an RPG stat system to our hero. The sky’s the limit.

[![device-2014-11-26-193651](http://www.hunterdavis.com/content/images/2014/11/device-2014-11-26-193651.png)](http://www.hunterdavis.com/content/images/2014/11/device-2014-11-26-193651.png)

And with that, I’m going to break for Thanksgiving holiday here in the US. I’ll update with another article when things have progressed further.


