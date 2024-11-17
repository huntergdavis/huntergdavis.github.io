---
layout: post
title: Announcing Labrync  
date: '2024-11-16 01:00:24'
image: "/content/images/2024/earlygame.png"
---

Announcing Labrync (like labrynth + ncurses)

Source and download here -> [Labrync](https://github.com/huntergdavis/labrync/)

<img src="https://github.com/huntergdavis/labrync/raw/main/screenshots/earlygame.png" width=400>

Labrync is a passive or active little console toy. I wanted to play with a few maze exploration algorithms (you can see a bunch in the history).  The color palette is going to change as right now it's a 'hotdog stand' level thing. I thought the concept from onelonecoder was really fun and inspiring and wanted to extend it in some fun ways.  Also ported to python cause why not I guess? 

Like I said before, little things that bring me joy.  Things I might dip in and add a feature to once a year, for 30 years. That's what my internet is all about.  Here's another one. 


https://github.com/huntergdavis/labrync/raw/main/screenshots/earlydemo.mp4


Based on and extended from the command line C fps from 
onelonecoder

https://github.com/OneLoneCoder/CommandLineFPS


1. Maps are randomly generated
2. Maps can be auto-solved (screensaver mode, if you will) by passing -a to labrync.py
3. Colors are... supported 
4. Player entering 'X' exit will regenerate the map and start fresh in top left corner
5. Breadcrumbs (or .. reverse breadcrumbs?  Crumpled grass?) To show where you've been.
6. Fog of War (or not) for additional challenge  

