---
layout: post
title: Johnny Castaway Text Edition 
date: '2021-12-11 08:33:24'
featured_img: 'https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/johnny_printer.jpg'
---
<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/johnny_printer.jpg" width="640">
I've been enjoying and porting Johnny Castaway to new systems for many years now.  Today though, is the first time I've actually added a fundamentally new feature to Johnny.  I was working on my closed captions branch, adding textual descriptions for the scenery and actions that happen while the game is playing.  It was going along just fine, but I realized that you don't really need the original files, engine, or parsing code at all to simulate the experience textually.  I had already done the hard work to write the descriptions for every scene and item, why not script them all up together into a bash script and reduce the overhead for running Johnny *significantly*?

So, here you are.  The whole of Johnny Castaway, distilled down into a single bash script.  You are now free to run Johnny on devices which do not have graphics output, or on your receipt printers for example. 

If you'd like to use the closed captions in your own ports of Johnny, you can find them in the closed_captions branch.  For the script, you can find that in the [bash branch here](https://github.com/huntergdavis/jc_reborn/tree/bash). 

I also highly recommend adding Johnny to your .profile or .bashrc, such that when you log onto a shell you get an update on how Johnny's doing today :)

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2021/johnny_bash_startup.jpg" width="640">
