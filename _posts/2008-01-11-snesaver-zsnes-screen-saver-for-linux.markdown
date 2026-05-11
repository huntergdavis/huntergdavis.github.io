---
layout: post
title: Snesaver - Zsnes screen saver for linux
date: '2008-01-11 16:15:36'
tags:
- snes-roms-screensaver
---


Ok, so here’s a fun bit of perl code I wrote last night. It’s called snesaver, [and you can download it here](/snesaver.pl "snesaver - snes screen saver"). Here’s how it works,

1. You’ll need to be running some flavor of *nix (self=ubuntu), with perl installed  
 2. You’ll need to have xscreensaver set up as your screensaver (though it should be simplicity itself to do this for most any other screensaver)  
 3. You’ll need to have zsnes installed  
 4. You’ll have to supply your own roms (legality), and record your own rom state movies in zsnes (simple simple!)

And that’s about all you’ll need. Just open up your ~/.xscreensaver file and put an entry for snesaver.pl (should be in your path) under the “programs” section. Then edit the script to point to /your/rom/directory/structure/ and you’re all set.

Here’s a youtube video of it in action.

<iframe width="425" height="355" src="https://www.youtube-nocookie.com/embed/46vB8-7PLLY" frameborder="0" allowfullscreen></iframe>

/H


