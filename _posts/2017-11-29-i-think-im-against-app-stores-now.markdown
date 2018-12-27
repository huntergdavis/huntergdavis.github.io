---
layout: post
title: I Think I'm Against App Stores Now
image: "/content/images/2017/11/sunset.jpg"
date: '2017-11-29 07:32:30'
---

TLDR; I'm allowing all but two of my android apps to sunset off of the app store in the beginning of the year.  You'll still be able to download them all and their source code from GitHub. 

Here's the thing folks: I'm really starting to worry about app stores. 

I used to think of app stores like package repositories.  Eager developers write useful utilities, get them approved, and that's that.  The compatibility may eventually drop off, but you can be reasonably assured that your software will run as long as the host operating systems maintain backwards compatibility.  

That's way, way off. Without maintenance and significant upkeep, you can neither monetize nor even keep your app available on the app store.  Google has a sliding bar of quality and legal requirements.  This really isn't an issue if you're maintaining an app professionally.  This is a huge issue if you're trying to keep 65 free (and ad-free, more on that later) programs updated. There is no place in that world for the 'micro-app' mindset.  Apps require active maintenance and upkeep. 

Let me take you back to 2011. I had taken the summer off between start-ups to learn Java, and I wrote an Android app a day for 60 days. Things were good, I made about 50$ a month total from everything.  Enough for a pizza dinner, and I used my own apps. Win-win. If users found value in them, win-win-win. Sure, every once in a while I'd need to log into google to respond to a DMCA bot or update an address or email.  It was easy to forget about it. 

Fast forward to 2012, and I've open sourced all of the above apps.  I peaked at 250,000 active users, and they brought in around 75$/mo average in ad income. Enough for drinks and a pizza dinner. For the next 4 years, I continued to receive that 75$/mo in income from an ever-shrinking group of users.  100K, 90K, 50K, but there were always enough core users to pay for that pizza.  

Sometime in 2016, I didn't notice for a few months but revenue had stopped coming in completely.  I had failed to update the ad SDKs in my apps for too long, and they could no longer serve ads. The new SDKs were not drop-in replacements, and with the level of complexity of the apps being what they were, it would be easier to re-write them than re-create the ancient set of libraries and android SDKs used to write them. At least a few hours of work per app.  Not worth it. 

So, I decided to leave them all up ad-free.  No big deal, and there were still a few tens of thousands of users.  Another year and a half goes by, and I receive a notice that my apps will be removed if I don't select whether they are for children only.  "OK" I think, "that's only 65 settings pages to update, no big deal."  So I make the investment to do so, and it only takes a couple of hours. 

Only, the system is delayed.  Soon I had an inbox full of rejection messages.  An app update means it must conform to all new submission guidelines.  This means new graphics, cover images, legal disclaimers, tag lines, short descriptions, and really just a mountain of work.  That's time I should be spending with my family, or hacking on something new!  Not updating the SEO keywords or advertising profile of an old utility app that's still working fine for thousands of people. 

And if I, the formerly self proclaimed king of Android apps can't be bothered to update his old apps, how many will?  What will we lose when the little apps are gone?  It just makes me feel like we can do better, I can do better. Is it progressive web apps?  Web virtual machine containers?  Distributed trust networks?  I dunno, but I think I'm done with walled gardens. 
