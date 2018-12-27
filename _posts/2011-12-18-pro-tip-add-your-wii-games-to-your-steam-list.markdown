---
layout: post
title: Pro Tip - Add your Wii Games To Your Steam List
date: '2011-12-18 09:26:03'
---


If you’re like me, you ditched your Wii in favor of a pure emulation solution once you realized you could play your legally purchased disks in full 1080p emulated using the Dolphin Wii/GameCube emulator. It’s fast as crap, improves the graphics, and is free. Plus the ability to save my disks as .ISO files and play them at my leisure is a time saver. One thing that I’ve gotten used to on the PC is playing PC games from Steam, and I’m looking forward to their new 10 foot living room view. So I decided to put them together. Turns out it’s not that hard. Read on for the mini-tutorial.

[![](http://66.147.244.180/~hunterda/content/images/2011/12/steam_skyward1-300x294.png "steam_skyward")](http://66.147.244.180/~hunterda/content/images/2011/12/steam_skyward1.png)

It turns out that Steam doesn’t like to launch batch files, and Dolphin doesn’t have an option to auto-load the last game you were playing. So you have to use a batch to exe converter program to turn a small script into an exe you can pass to steam. I’ve removed the link to the Batch Converter, as it raised malware flags. Use at your own risk.

First you’ll need to make a batch file that directly launches your game of choice. For this tutorial, I’ll be using my backup copy of my real disk of the newest Zelda game. If you haven’t played it, it’s pretty great. Anyway, my batch file ended up looking like this:

```
<br></br>
cd "C:Program FilesDolphin"*<br></br>
start Dolphin.exe -e "c:UsersHunterROMSwiiws_tlozss_ntsc_multi3.iso"<br></br>```

Load this batch file up in bat-to-exe converter, and save the resulting .exe file somewhere safe (perhaps in your Dolphin directory). Now fire up Steam, and select “Add non-Steam game to Steam” from the menu. Browse to your Skyward Sword.exe file, and add it in. That’s that.

[![](http://66.147.244.180/~hunterda/content/images/2011/12/dolphinsteam1-300x190.png "dolphinsteam")](http://66.147.244.180/~hunterda/content/images/2011/12/dolphinsteam1.png)


