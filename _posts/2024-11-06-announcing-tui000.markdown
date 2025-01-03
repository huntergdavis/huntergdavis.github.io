---
layout: post
title: Announcing Tui000  
date: '2024-11-07 01:00:24'
image: "/content/images/2024/play_screen_11_7_2024.png"
---

Announcing Tui000 (sounds like 'three thousand') 

Source and download here -> [Tui000](https://github.com/huntergdavis/tui000/tree/main)

Tui000 is a passive game / screensaver for your terminal.  Watch virtual avatars make life decisions, visit the graveyard to see how each life measured out. Passive, small. Now is the time for small joys, for silver linings. I feel 2025 will need as much joy as possible, and I've been inspired to put more little moments of joy out there for folks like I used to. 

I had an idea one day just relaxing and thinking about Johnny Castaway. 
I had already ported Johnny to as many platforms as I was interested in.
What I really missed was that feeling of fun and writing software. 

Some of my best work was made famous not by my original intention.
Rather, it was the creativity of others that brought purpose to "meaningless" software. 
After all these years, I keep coming back to the terminal. 

So, in an attempt to recreate that feeling, in the terminal, here's the start and the pitch.
You only have 3000 weekends, on average, in your adult life. The life-map assumes that each major choice you make in your life will become the focus, on average, of 12 weekends. Some a lot more, some a lot less, but on average let's take a wild swing at 12 or so. 
 
So you get 240 decisions, some many times over, with how to spend your time.  Sounds like a lot, goes by quick.  Just like life. Probably not of interest to most folks, but of great interest to me.  Useless, silly, simplistic, exactly what I had envisioned.  All future improvements are fun additions to the base concept, and I've got a ton in mind. 


Design:

Constraints: Must target / be usable in 80x24 terminal window. 

Launching the app spawns a character.
The character makes choices, indicated by colors which map to life categories. 
These choices add up to weave the tapestry of each life, the colorful headstone.
When the character dies, each is written out to a json file in ./graveyard/

Running the App:
Run with python after installing requirements.txt

Pass the -debug flag for more logging and 100x speed

Building with Docker:
sudo docker build -t tui000 .

Running with Docker:
docker run -it --name tui000-container tui000


You can find the repository below, including original design docs and screenshots. 

[Tui000](https://github.com/huntergdavis/tui000/tree/main)

Main Graveyard Screen -> 
<img src="https://github.com/huntergdavis/tui000/raw/main/screenshots/graveyard_like_concept.png" width=400>
<img src="https://github.com/huntergdavis/tui000/raw/main/concept_art/death_screen.jpg" width=400>
