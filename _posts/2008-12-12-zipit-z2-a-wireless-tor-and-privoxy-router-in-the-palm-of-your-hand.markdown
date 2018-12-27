---
layout: post
title: Zipit Z2 - A Wireless TOR and Privoxy router in the palm of your hand
date: '2008-12-12 11:15:28'
---


So I’ve got a new pet project, the zipit z2. If you don’t know this 50$ handheld is actually a moderately powerful computer. 32 megs of ram, a 2g sd card, and a 300mhz arm processor means I can do quite a bit of interesting stuff (we’ve certainly worked with less!). After doing the prerequisite install of Angstrom linux, I decided to see what it would take to run tor and privoxy on it.

[![Zipit Z2](http://66.147.244.180/~hunterda/content/images/2008/12/zipit1.jpg)](http://66.147.244.180/~hunterda/content/images/2008/12/zipit1.jpg "Zipit Z2")

Turns out, not much.

I’ll be posting quite a bit more on this in the future, but for those enterprising zipit hackers out there who need an anonymous connection to the outside world, look no further than this post.

Changes required for tor:  
 If you attempt to bitbake tor, you’ll receive c++ build errors about duplicate declarations of a couple of functions. This is due to unnecessary forward declarations of these functions in the .h files. Simply open the .h files mentioned by the errors, and delete the offending line. Tor will then compile fine.

Changes required for privoxy:  
 If you attempt to bitbake privoxy, you’ll receive an error from the configuration script about your build environment. Luckily, it’s harmless. Browse into the source tree and open up the ‘configure’ script. Search for the “incorrect host” (or whichever particular message you received) and delete the if/fi codeblock surrounding it. Do this 3 more times (its in there multiple times) and privoxy will compile fine.

And that’s it. Just set your /etc/privoxy/config to forward to socks port 9050 (standard privoxy config) and you’re secret squirrel!


