---
layout: post
title: Food (and diet) management for the unix geek, a python script
date: '2008-07-14 15:39:05'
---


For many a scientist like myself, the pear-shaped waistline which has become synonymous with the unix guru has become all too familiar. While there are a number of mitigating factors, I’m going to chalk it up to the sedentary lifestyle of the typical programmer. A study posted on Digg last week showed that on average, dieters who kept a food journal lose twice as much weight as those who don’t. That’s a pretty powerful tool. Carrying around a notepad doesn’t make a lot of sense for me, as I’m almost never without my laptop, so I’ve been keeping a csv spreadsheet like below:  
```
<br></br>
07:53 ,oatmeal        , 160<br></br>
07:55 ,water          , 000<br></br>
10:40 ,kudos          , 100<br></br>
10:40 ,water          , 000<br></br>```
  
 Which is fine. It accomplishes what needs to be accomplished, with regards to the diary at least. However, I would like some statistics with my diet. How many calories do I have left in the day, how many glasses of water, how many calories did I eat at lunch, etc. These little statistics and calculations really drive home the message. I always keep today’s .food file on my desktop, and I have my .bashrc set up to show me my dietary information whenever I login or open a shell like so:

```
<br></br>
# display how many calories I've left/eaten today<br></br>
echo "Remember to fill in your .food file today"<br></br>
echo "-----------------------------------------"<br></br>
~/Scripts/DotFoodStatistics.py ~/Desktop/*.food | grep today<br></br>
echo "-----------------------------------------"<br></br>```

Attached->[python “food processor” diet statistics](http://hunterdavis.com/content/images/2008/07/dotfoodprocessing.py "python “food processor” diet statistics")


