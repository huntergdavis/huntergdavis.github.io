---
layout: post
title: What Unlimited Storage Really Means In America - Bandwidth Limitations
date: '2012-01-19 21:53:40'
---


So I’m on my lunchbreak, browsing the hot deals forums over at Fatwallet.  I stumble upon what appears to be a very solid deal, 24 months of JustCloud unlimited storage backup service for 35 bucks.  Can it live up to the hype (EDIT – Nope, it pretty much sucks for me, but their cancellation process is painless…)?  Is it even possible to stress test this in the land of bandwidth caps and SOPA hearings?  I’m going to find out.

For those of you just finding this blog, I’m a complete media glutton.  I’ve (legally, at least for now) made digital backups of every DVD, audio CD, BLU-Ray, cartridge game, Playstation game or eBook I’ve ever owned or created.  On top of that, I tend to keep a local store repository of my 600+ steam game collection for fast retrieval (and if they decide to later pull any of the games I bought).  Add in the couple hundred gigs of personal photos I’ve taken as well as tons of software projects, virtual machines, disk images, dev environments, half-finished projects, etc  and you’re looking at about 5 terabytes of data.  This is locally spread out over my two Drobo storage bots full of 2tb drives.  Unfortunately, some facts about the internet here in America come into play:

[![](http://www.hunterdavis.com/content/images/2012/01/Holly_pumping_engine_New_Catechism_of_the_Steam_Engine_1904-300x169.png "Holly_pumping_engine_(New_Catechism_of_the_Steam_Engine,_1904)")](http://www.hunterdavis.com/content/images/2012/01/Holly_pumping_engine_New_Catechism_of_the_Steam_Engine_1904.png)

JustCloud and Me – by the numbers:

1.  35$ for 24 months of unlimited storage backups, ~1.50$ a month.  
 3. My limited bandwidth means I can upload roughly  8 gigs per day.  
 2. My full 5tb of data uploaded over my 768kb pipe will take roughly the entire 2 years of uploading nonstop.

With this knowledge, it is clear JustCloud cannot become my one-stop online backup.  However, if the service remains low-cost, it does provide me with a very interesting alternative backup solution.  Consider my digital landscape:

- Google+/Picasa provides me infinite storage space for photos.  I’ve already uploaded my 100gb of personal photos there.
- Google Music provides me 20,000 song uploads for music.  This literally is double the size of my music collection.
- Google Docs provides 1gb of storage space for word documents and excel sheets.  This is generally sufficient
- Netflix/Hulu/Crackle cover at least 50% of my video collection currently.  This percentage will likely rise in the future.
- Steam stores the majority of my games in the cloud already

Considering this, I am left with the following classes of data to store:

- Virtual Machines and Work Documents (40gb – 5 days of uploading)
- Source Code and Hack Plans (100gb – 12 days of uploading)
- Personal Documents (10gb – 1.25 days of upload)
- eBooks (50gb – 7.5 days of uploading)
- The Sims/Sims 2/Sims 3 neighborhood and save data (30gb – 4 days of uploading)

Going over this new battle plan, I should be able to upload these data items within one month.  This will take ~250 gigs of storage space on their servers, plus the 250 gigs for the initial transfer.  To compare, Amazon EC2 would charge me 15$ monthly to store this data, and 30$ to download it all if I ever needed to.  As such, if JustCloud stays in business they will have saved me a couple of hundred dollars in online storage costs, as well as given me a bit more peace of mind.  Only time will tell if my expectations will be met.  I’ll keep you updated as events transpire.


