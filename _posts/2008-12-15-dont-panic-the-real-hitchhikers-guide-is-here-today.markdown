---
layout: post
title: Don't Panic!  The REAL HitchHikers Guide is here TODAY
date: '2008-12-15 10:21:25'
---


As it turns out, with a little bit of effort you can put together a cheap (50$), handheld, wireless, graphical wikipedia browser ala the HitchHiker’s Guide.

[![Don’t panic!  A real guide to everything (Wikipedia)](http://66.147.244.180/~hunterda/content/images/2008/12/dontpanic1.png)](http://66.147.244.180/~hunterda/content/images/2008/12/dontpanic1.png "Don’t panic!  A real guide to everything (Wikipedia)")

Prerequisites:  
 Install Linux (wifi), Xfbdev (x11) and Dillo (browser) on your Zipit Z2 as described [here](http://linux.zipitwireless.com/wiki/OpenEmbedded).

DilloRC:  
 Here’s the custom part. After launching dillo for the first time, you’ll have a ~/dillo/dillorc file in your home directory. Open that up, and customize the layout to your liking. Personally, I just enable “fullscreen mode” at startup and it hides all the buttons. Then head on down to the “search url” and enter in:  
```
<br></br>
"http://google.com/search?btnI=1&q=en.wikipedia.org +%s"<br></br>```

This tells dillo to use google’s “I’m feeling lucky” search on wikipedia for the search term. This allows for instant wikipedia browsing over wireless ala the hitchhiker’s guide. All for under 50$ nice!


