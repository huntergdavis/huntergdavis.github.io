---
layout: post
title: "Full Steam on Termux, Because Why Not?"
date: '2026-08-09 18:25:16'
tags: [termux, linux, steam, android]
---


I've been having so much fun running full steam games on my switch lite! Just this weekend I got Psychnauts running well (with no overclocks!) These can be good times even if they are complicated times. Sometimes, you just need to know something is possible before it becomes easy for everyone. That's what I'm hoping for here.  I've got a proof of concept that's working well enough to share, but I'm sure it could be much better done in a bespoke manner by a developer with more time. Full graphics-accelerated steam and steam games, inside a termux linux session , running on an unrooted stock galaxy s9+ tablet. 

Here's how it came together. Obviously I've been enjoying how easy it's become to run steam games on the switch lite. Gamehub and GameNative and Winlator are all great pieces of software, but I'm never goign to really feel comfortable putting my steam auth information into a 3rd party tool. There will always be some spectre of doubt and the fear that my account could somehow be compromised. So the desire is there, latent, waiting for the situation. 

Then it hits me.  I've got a tablet that I use for programming while I'm on the road.  It's got 5g internet built in, and I got a sweet deal on a payment plan from T-Mobile.  Cheap and quite powerful. I have Termux installed with Termux-X11 and graphics acceleration working. I run herdr, coding harnesses, compilers, a full KDE desktop (sans root). It works better than you'd expect, franky most folks would think I'm just running a kde distro on a small tablet computer, if not for the T-Mobile chime on boot. Why then, should I have to swap out to some third party to play my steam games? 

So I fire up an agent, tell it to start monitoring syscalls, and I give it a shot. One problem at a time.  This is missing, that is crashing. Before too long the steam interface comes up.  Then EA. Then some games. A little progress, but progress. A small proot patch, some launch scripts, nothing wacky. 

Yes, I used a coding assistant LLM to perform rote tasks, generate code, and run tests overnight.  No, I don't think that means the code is poisoned by the well of AI. I just wanted to show that it was possible, and not far out of reach. I really do think Valve will release something like this but 100 times better on their own, eventually. In the meantime here's the code: 