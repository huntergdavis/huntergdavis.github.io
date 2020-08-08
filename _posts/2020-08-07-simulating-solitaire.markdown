---
layout: post
title: Simulating Solitaire
date: '2020-08-07 08:33:24'
cardsimulator: true
---
 
 
Like many of us, I've been spending the past 6 months living in a frightening emotional rollercoaster.  Covid-19 has devastated so many lives, and the extent of the long-term increase in mental illness, depression, and negative feelings are still unknown. I, like many, have been dealing with feelings of loneliness and isolation.
 
What does this have to do with solitaire?  Well, let me take you back.  When I was young, the internet wasn't mainstream.  My parents couldn't afford the long-distance phone calls needed to dial into a remote BBS or one of the fledgling ISPs.  I lived far from town, and I was a lonely kid, obsessed with the technology we had available to us 30 years ago. 
 
I don't like to dwell on my childhood, but these past months of social distancing have brought me back to those days.  One of the shared obsessions many of us had back in the day was computer solitaire.  It has some very interesting qualities.  1.  It's easy to play, but you're not guaranteed a win.  Not at all, many forms of solitaire are quite difficult to win. 2.  You can play it alone, with nothing but a deck of cards and your mind. 
 
So, I set about to create my own solitaire variant.  As usual, I went way overboard, then spent many iterations removing features and scope-cutting till I had a fun core game loop. 
 
I started with a huge design guide.  Dungeons and Dragons or Magic the Gathering as my inspiration.  The deck itself provides the random number generator instead of dice.  Each card was an enemy on an enemy table.  Complex rules, Pokemon style card battling and capturing mechanics.  Monster affinity and weakness types. Complex stats.  It neither playtested well nor was it easy to remember.  There were elements I enjoyed though.

![Solitaire V1](https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/solitaire-1-1.jpg)
![Solitaire V1](https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/solitaire-1-2.jpg)
![Solitaire V1](https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/solitaire-1-3.jpg)
![Solitaire V1](https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/solitaire-1-4.jpg)

 
I enjoyed the card capture / battle mechanics.  I enjoyed the progression across a game board (like dungeon solitaire).  I enjoyed the feeling of winning against tough odds (more on those odds later!)
 
So, I began to cut scope.  A v2 began to take shape.  Each card suit mapped to a creature type, and battle mechanics were still too complex. It didn't play-test well, but I could tell there was something there.  The core game loop was starting to become fun, but needed some balancing.

![Solitaire V2](https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/solitaire2.jpg)

 
By the time I cut it down to a few easy core rules, the fun began to come back into it.  When I realized the board could be dealt a hand at a time "encounter style" such that you only need a small space to play, I started to really enjoy this "commander solitaire" variant (as one of my playtesters coined it.)
 
![Solitaire V3](https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/solitaire3.jpg)


It started to feel very playable, and fun, but it felt like I almost never won!  How to quantify that though, and how to balance?
 
Why, monte-carlo simulation of course.  I coded up the ruleset using the most excellent "Deck of Cards" library from Juha Lindstedt, available at https://github.com/pakastin/deck-of-cards
 
And as it turns out, there were really only a couple of twists to the ruleset that made the game really pop, and balance to roughly 25% win ratio, plus or minus a few percent depending on the "level" you're playing.
 
So, at the bottom of this post I'll share the ruleset to "Commander Solitaire", as well as the Javascript simulator.  Source is all available in my github repo, feel free to tweak the rules, run a few million games, see what you think!
 
Rules of commander solitaire
- Select a level, 1-6.  This determines your hand size and difficulty.
- Draw a card, this is your commander.  They are always in play, and cannot be swapped.
- Draw a number of cards equal to your level.  Each one is in play.
- The final card you drew in the previous step is your 'suit' card.  All cards of this suit are worth double this game.
- Each game has 7 encounters with enemy groups
- Draw a number of "enemy" cards as follows.  Level,Level,Level+1,Level+2,Level+2,Level+2, Boss card.  For example, if you select a 'level 3' game, and it's the third round, you'll draw Level+2 cards = 5 cards.
- Add up the total value of your cards.  (remember to double the value of cards that match this level's suit)
- Add up the total value of your enemy cards (remember to double the value of cards that don't match this level's suit)
- If your cards total more than your enemy's cards, you win this round.  You are allowed to swap ONE of your enemy's cards with one of your non-commander cards.
- When you reach level 7, that's the boss level.  Same rules, but there's only one boss, and they are worth 3*level*value.  (i.e. if the boss is a queen of spades, and the level suit is hearts, and you're playing a level 4 game, the boss is worth (queen)*3*level = 11*3*3 = 99)
 
 
And those are all the rules.  I've been quite verbose above, it's generally quite simple, simple enough for young children and easy enough to remember when you're stressed, bored, or just can't look at a computer screen any longer.
 