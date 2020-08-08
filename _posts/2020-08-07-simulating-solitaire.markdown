---
layout: post
title: Simulating Solitaire
date: '2020-08-07 08:33:24'
cardsimulator: true
---


Like many of us, I've been spending the past 6 months living in a frightening emotional rollercoaster.  Covid-19 has devestated so many lives, and the extent of the long-term increase in mental illness, depression, and negative feelings are still unknown, but likely to continue.  I, like many, have been dealing with feelings of lonileness and isolation.

What does this have to do with solitaire?  Well, let me take you back.  When I was young, the internet wasn't mainstream.  My parents couldn't afford the long-distance phone calls needed to dial into a remote BBS or one of the fledgling ISPs.  I lived far from town, and I was a lonely kid, obsessed with the technology we had available to us in the late 1980s.  

I don't like to dwell on my childhood, but these past months of social distancing have brought me back to those days.  One of the shared obsessions many of us had back in the day was computer solitaire.  It has some very interesting qualities.  1.  It's easy to play, but you're not guaranteed a win.  Not at all, many forms of solitaire are quite difficult to win. 2.  You can play it alone, with nothing but a deck of cards and your mind.  

When I was young, 
So, I set about to create my own solitaire variant.  As usual, I went way overboard, then spent many iterations removing features and scope-cutting till I had a fun core game loop.  

I started with a huge design guide.  Dungeons and Dragons or Magic the Gathering as my inspiration.  The deck itself provides the random number generator instead of dice.  Each card was an enemy on an enemy table.  Complex rules, Pokemon style card battling and capturing mechanics.  It neither playtested well nor was it easy to remember.  There were elements I enjoyed though. 

I enjoyed the card capture / battle mechanics.  I enjoyed the progression across a game board (like dungeon solitaire).  I enjoyed the feeling of winning against tough odds (more on those odds later!)

So, I began to cut scope.  A v2 began to take shape.  Each card suit mapped to a creature type, and battle mechanics were still too complex. It didn't play-test well, but I could tell there was something there.  The core game loop was starting to become fun, but needed some balancing. 

By the time I cut it down to a few easy core rules, the fun began to come back into it.
