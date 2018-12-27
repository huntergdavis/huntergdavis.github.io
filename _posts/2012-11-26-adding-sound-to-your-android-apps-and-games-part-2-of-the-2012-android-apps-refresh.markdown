---
layout: post
title: Adding Sound to Your Android Apps and Games (Part 2 of the 2012 Android Apps
  Refresh)
date: '2012-11-26 02:04:24'
---


This is the second in an article series about Android development, open source software, audio production, and so much more. You can read part 1 [here](http://www.hunterdavis.com/2012/07/21/android-sound/).

**[Preface – A New Game!](http://www.hunterdavis.com/?p=3163/#a0)**  
**[Using the Hardware at Hand](http://www.hunterdavis.com/?p=3163/#a1)**  
**[Capture List, Gotta Capt’ em All!](http://www.hunterdavis.com/?p=3163/#a2)**  
**[Fun with Audio Capture](http://www.hunterdavis.com/?p=3163/#a4)**  
**[Editing your Audio – Audacity](http://www.hunterdavis.com/?p=3163/#a5)**  
**[Removing Ambient Noise with Audacity](http://www.hunterdavis.com/?p=3163/android-sound/#a6)**  
**[Recording a Title Theme with Audacity](http://www.hunterdavis.com/?p=3163/android-sound/#a7)**

**[]()Preface – A New Game!**

When I wrote the first article in this series, I never thought It would take me where it has. I’ve been all over town recording audio samples on my little boom mic, learned quite a bit about basic audio and recording techniques, and received a ton of excellent feedback from friends and strangers alike. My original intention was simply to update all of my previous Android apps to use my new audio library, but the sparks of creativity cannot be contained. I am therefore starting work on a new minigame collection titled ‘5 seconds’. It will; of course, be fully open source. Expect cameos from all of my previous game characters and a good dose of fun. You can also expect site updates describing the game development process and how ‘5 Seconds’ is evolving. You can checkout the GitHub page for it [here](https://github.com/huntergdavis/FiveSeconds).

[![](http://www.hunterdavis.com/content/images/2012/11/fivesecondstitle.png "fivesecondstitle")](http://www.hunterdavis.com/content/images/2012/11/fivesecondstitle.png)

**[]()Using the Hardware at Hand**

Having tried to record some audio clips with my low-end android phone, I became convinced that this was not the way to move forward. Digging through my parts box, I found a (now obsolete) Sony Minidisc recorder and a Memorex 1/4″ high impedance microphone. I used an old Seiko in-line guitar tuner and some RCA patch cables to bring the Microphone line to the 3.5mm input on the Minidisc recorder. Not the prettiest setup, but it gave me ~10 feet of line to work with, certainly enough for a boom pole. Unfortunately I wasn’t bringing the level up enough, and the recording level was too low.

[![](http://www.hunterdavis.com/content/images/2012/07/CameraZOOM-20120722163528873-300x225.jpg "Microphone Setup")](http://www.hunterdavis.com/content/images/2012/07/CameraZOOM-20120722163528873.jpg)

Next I tried using a standard computer headset. This worked well in that the level was much improved, but the mic had terrible range. I finally settled on a ‘TV microphone’ from my ’80’s junk’ box. The audio was coming in at an appropriate level and I had plenty of 3.5mm extension cables to work with. My portable mic setup was ready to go.

**[]()Capture List, Gotta Capt’ em All!**

Each of the games I’m updating for this article (see list below) have their own sound effects requirements. Luckily, there are a number of similar elements and themes running through my games that lend themselves to audio re-use. A bullet is a bullet, lightning sounds like lightning, etc. Knowing in advance what types of sounds I’m trying to capture helps dramatically with the process. So, as usual, I compiled a set of lists and looked for duplicates (**in bold**).

Custom Action Tap

1. **Menu Checkbox Noise**
2. **Tap**
3. **Kill**
4. **Miss**
5. **Bomb**
6. **Lightning**
7. **Death**
8. **Gain a Life**
9. **Game Over**
10. Armageddon
11. Fire Crackle
12. Fire Spread
13. Fire Dies
14. Freeze Bomb
15. Baloon Pop
16. Hammer of Thor Appears
17. Hammer Kill

Custom Comets

1. **Menu Checkbox Noise**
2. **Tap**
3. **Kill**
4. **Miss**
5. **Bullet**
6. **Lose a Life**
7. **Reverse Fire Mode**
8. **Enemy Split**
9. **Game Over**

Custom Onslaught

1. **Menu Checkbox Noise**
2. **Tap**
3. **Kill**
4. **Miss**
5. **Bullet**
6. **Lose a Life**
7. **Reverse Fire Mode**
8. **Enemy Split**
9. **Level Up**
10. **Game Over**
11. Weapon Upgrade
12. Double Bullet
13. Triple Bullet
14. Shotgun
15. Boomstick

Custom Pong (Not on market due to Atari Pong Copyright Takedown)

1. **Menu Checkbox Noise**
2. **Game Over**
3. Ping
4. Pong

Skillful Dodge

1. **Menu Checkbox Noise**
2. **Game Over**
3. Walkin Around
4. Hit a Tree

Skillful Lines

1. **Menu Checkbox Noise**
2. **Game Over**
3. **ScreenShot**
4. **Save Score**

Skillful Surround

1. **Menu Checkbox Noise**
2. **Game Over**
3. **ScreenShot**
4. **Save Score**
5. Doodle Noise

The Grind

1. **Menu Checkbox Noise**
2. **Level Up**
3. Grinding Wheel
4. Enemy Attacks
5. Player Attacks
6. Enemy Spell
7. Player Spell
8. Auto-Grind
9. Enemy Drops loot
10. Player Learns Spell
11. New SubQuest
12. New Quest
13. Resting Up
14. Player Healing
15. Enemy Healing
16. Weapon Up
17. Armor Up
18. Helmet Up
19. One Year Older
20. Stats Up

As you can see, there are a number of duplicate needs that can be served by a single sound file in the library. Please note, I am saying library in the ‘GitHub project’ sense. All of the sound files will not be included in all of the projects themselves or in the android library because that’s just inefficient and causes the library size to grow all sorts of huge.

The final list of sounds to capture for this first iteration of the library ended up being the below 53 sounds.

1. **Menu Checkbox Noise**
2. **Tap**
3. **Kill**
4. **Miss**
5. **Bomb**
6. **Lightning**
7. **Death**
8. **Gain a Life**
9. **Game Over**
10. **Bullet**
11. **Lose a Life**
12. **Reverse Fire Mode**
13. **Enemy Split**
14. **Level Up**
15. **Game Over**
16. **ScreenShot**
17. **Save Score**
18. Armageddon
19. Doodle Noise
20. Weapon Upgrade
21. Double Bullet
22. Triple Bullet
23. Shotgun
24. Boomstick
25. Fire Crackle
26. Fire Spread
27. Fire Dies
28. Freeze Bomb
29. Baloon Pop
30. Hammer of Thor Appears
31. Hammer Kill
32. Ping
33. Pong
34. Walkin Around
35. Hit a Tree
36. Grinding Wheel
37. Enemy Attacks
38. Player Attacks
39. Enemy Spell
40. Player Spell
41. Auto-Grind
42. Enemy Drops loot
43. Player Learns Spell
44. New SubQuest
45. New Quest
46. Resting Up
47. Player Healing
48. Enemy Healing
49. Weapon Up
50. Armor Up
51. Helmet Up
52. One Year Older
53. Stats Up

**[]()Fun with Audio Capture**

Now that I had a portable audio recording system set up that could produce decent results (with a far greater range than my cell-phone microphone), it was time to go out into the world and record some audio. An excellent reason to take an impromptu camping trip! I took my recording setup and list of sounds to capture out into the world. Anything that I didn’t feel had an appropriate sound in nature simply would get recorded as a voice-over (i.e. COMBO!) when I returned home from the trip.

[![](http://www.hunterdavis.com/content/images/2012/08/justmyfeet-300x219.png "justmyfeet")](http://www.hunterdavis.com/content/images/2012/08/justmyfeet.png)

**[]()Editing your Audio – Audacity**

When it comes to editing audio, there are few tools as powerful or as deceptively simple as [Audacity](http://audacity.sourceforge.net/). I prefer to use it over proprietary software for a number of reasons.

1. It doesn’t watermark your audio clips.
2. It’s open source, so no limitations of clip size etc
3. Being open source, I can talk about it pedagogically without worry of corporate bias
4. It’s dead simple to use, and there are some great plugins that come with it

For these and many other reasons, I’ll be referring to Audacity many times throughout this article series. It allows for effortless one-click line-in recording (if you’ve got the ports). This is exactly how I ended up importing the audio samples from my mini disk player. “Why didn’t I transfer them directly as digital files?”, one would naturally ask. “Sony.”, would be my reply. Their anti-consumer efforts did not begin with the Playstation 3, nor do they only extend do their gaming division. While you can transfer audio from your PC and record audio (even optically!) on mini disc players, you cannot transfer the files back to your PC. Seriously. You have to use a line-in cable. Next time I should just go with a reel-to-reel setup and save myself some hassle! Ha!

**[]()Removing Ambient Noise with Audacity**

One of the best plugins that ships with Audacity is the noise removal plugin from Dominic Mazzoni. It’s dead simple to use, and does a very excellent job of removing background and mechanical noise from your audio clips. I’ve uploaded some small clips as mp3s to demonstrate the profound difference in quality between the original and the post-processed version. [Here](http://www.hunterdavis.com/content/images/2012/07/before-processing.mp3) is the original clip, and [here](http://www.hunterdavis.com/content/images/2012/07/post-processing.mp3)is the post-processed clip. Note the hissing and light background noise has been virtually eliminated from the source audio. It’s actually quite an easy process.

1. First, open up your audio clip in Audacity. [![](http://www.hunterdavis.com/content/images/2012/07/pre-processed-wav-150x150.png "pre-processed-wav")](http://www.hunterdavis.com/content/images/2012/07/pre-processed-wav.png)
2. Select a small chunk of your audio clip that is only background noise. [![](http://www.hunterdavis.com/content/images/2012/07/select_some_noise-150x150.png "select_some_noise")](http://www.hunterdavis.com/content/images/2012/07/select_some_noise.png)
3. Next, select Effects->Noise Removal. [![](http://www.hunterdavis.com/content/images/2012/07/select_noise_removal-150x150.png "select_noise_removal")](http://www.hunterdavis.com/content/images/2012/07/select_noise_removal.png)
4. From within the Noise Removal Pane, select “Get Noise Profile”.
5. Hit Ctrl-A to select the entire clip. [![](http://www.hunterdavis.com/content/images/2012/07/ctrl-a-150x150.png "ctrl-a")](http://www.hunterdavis.com/content/images/2012/07/ctrl-a.png)
6. Again, select Effects->Noise Removal
7. Click ‘OK’. That’s all.

**[]()Recording a Title Theme with Audacity**

Audacity is also a great tool for recording simple multi-track loops and vocals. As long as you’ve got a mic plugged in and selected in the preferences, recording your theme song is as easy as pie.

1. Record a small vocal. For my upcoming game ‘5 seconds’ I recorded ‘hurry hurry’
[![](http://www.hunterdavis.com/content/images/2012/11/audacity1-300x300.png "audacity1")](http://www.hunterdavis.com/content/images/2012/11/audacity1.png)

3. Record the same vocal again, in a slightly different pitch
4. Repeat a few times
5. Add some supporting sounds (bass notes, harmonies)
[![](http://www.hunterdavis.com/content/images/2012/11/audacity2-264x300.png "audacity2")](http://www.hunterdavis.com/content/images/2012/11/audacity2.png)

7. That’s that!

Stay tuned for more updates and sneak peeks at my newest game ‘5 Seconds’.


