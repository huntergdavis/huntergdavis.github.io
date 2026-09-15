---
layout: post
title: "Adding Modern Features to Pool of Radiance Mac Classic (1989)"
date: '2026-09-15 12:00:00'
image: "/content/images/2026/poolrad-phlan-party-sidebar.png"
tags: [games, emulation, android, mac, retro, eink, open-source, reverse-engineering]
project: poolrad-macmaps
---

We are living in a tempest of a time, and my mind seeks the familiar. I picked up an 8" android eink tablet, and was pretty surprised at the lack of really good game experiences built for it's black and white display. So I did what anyone who grew up in the 80s would do, I installed mini-VMac emulator and fired up "Pool of Radiance"

It's brilliant, punishing, and an absolute relic of game design long past.  No map, journaling, item/weapons/armor stat lists, spell lists, levels, etc. Lots of manual lookup, with the expectation that you have graph paper handy, along with three chunky books and a code wheel. 

"It's a shame gold box companion wasn't built for the Mac Classic." I had that thought for about ten seconds.  Then I rememberd that it's easier than ever to turn wishes to horses, so let's ride.  A simple enough plan: fork mini-vmac to include custom views and tools for pool of radiance.  



<img src="/content/images/2026/poolrad-phlan-party-sidebar.png" alt="Live New Phlan map with party health bars, armor class and class symbols while Rolf welcomes the party in the original Mac game" width="900">

## The Live Map

It started with the live map, the main view that's missing.  This works well, but I quickly realized I wanted to write notes.

<img src="/content/images/2026/poolrad-phlan-temple-tour.png" alt="The live map tracking the party to the Temple of Tyr, with the original game's own temple artwork below it" width="900">

## Handwritten Notes on the Map

This was the natural extension.  You can place flags on the map, each flag when clicked opens up a scratchpad with a copy of the map you can mark up. 

<img src="/content/images/2026/poolrad-handwritten-note.png" alt="A handwritten note page with TYR sketched by hand, saved against a tile on the New Phlan map" width="900">

<img src="/content/images/2026/poolrad-compact-flag-note.png" alt="A handwritten flag page with compact title-row tools and twice the sketch height; the original game remains visible below" width="900">

## Reading the Game's Own Memory

From there, I wanted to add in an easy to see tactical view (hp, status, char type). 

<img src="/content/images/2026/poolrad-combat-overview.png" alt="A read-only tactical overview of a battle, party marks filled and the rest hollow, above the game's own combat view" width="900">

<img src="/content/images/2026/poolrad-journal-encountered.png" alt="The notebook's encountered list filling itself in with a tavern tale and a proclamation the game named out loud" width="900">

## Offline Reference Tools

Finally, there's a lot of lookup tools so you don't need to leave the game experience to enjoy it all. I added a code wheel lookup, then automated it so it happens automatically on launch, no need to play code wheel lookup or get your reading classes out. 

<img src="/content/images/2026/poolrad-companion-info.png" alt="The companion Info tab with offline spell, weapon, level and journal lookups above the running game" width="900">

## Running It on E-Ink

It's a real joy to play this on an e-ink device. It feels so analog but also kinda futuristic?  Retro futuristic. 

<img src="/content/images/2026/poolrad-eink-proclamations.png" alt="Captured on the e-ink tablet: the map filled in after a long walk, with the game posting its proclamations below" width="900">

<img src="/content/images/2026/poolrad-eink-tavern-tale.png" alt="Captured on the e-ink tablet: a tavern tale overheard across town, with the explored map above it" width="900">

## Getting It

You'll need a boot disk, apple rom, and Pool of Radiance install.  These are easy to find nowadays. Install the APK below, point to your boot disk and rom, and have fun. 

<img src="/content/images/2026/poolrad-boot-bricks.png" alt="The rebuilt boot disk starting straight into the game over a brick desktop pattern" width="900">

The source, the APK releases and all of the research notes are on GitHub:
[huntergdavis/poolrad-macmaps](https://github.com/huntergdavis/poolrad-macmaps).

*Important Note -> This is a proof of concept, heavily written with AI. There will be bugs, and it won't be perfect.  This one is pretty niche, so I honestly don't even know if anyone will check it out.  That's OK, this one's for me. 
