---
layout: post
title: "Announcing Johnny Castaway PS1"
date: '2026-05-15 10:00:00'
image: "/content/images/2026/johnny6-ps1-date-dream.png"
tags: [johnnycastaway, sierra, c, assembly, PS1, port]
---

## Introduction

This has been a project well over a year in the making.  I'm proud to announce version 1.0 of Johnny Castaway PS1, a port of Johnny Castaway to the Playstation 1 console, with enhanced features and options like freeplay/sandbox mode. It's the version of Johnny I always wished existed, and my most ambitious port to date. 

## TLDR;
If you're less interested in the history and development of this project (which is an interesting case study in modern development, debugging, and optimization techniques), you can find the download and full website here: [hunterdavis.com/johnny-castaway-ps1](https://www.hunterdavis.com/johnny-castaway-ps1/)

<img src="/content/images/2026/fishing1-ps1-cast.png" alt="Johnny Castaway PS1 fishing" width="640">

## History

I've ported the jc_reborn codebase (and many others) to a few platforms over the years. I find porting enjoyable work, creative at times and necessitating compromise and cleverness. It was five years ago now when I released Johnny for the Dreamcast.  It was a bit of a slapdash port, back-porting jc_reborn to SDL1 for the DC. A year or two after it released, I receive an email from a game store owner who enjoyed it, but found that it crashed after about a half an hour (likely due to memory pressure from a large scene on the 8mb dreamcast)

I let them know I'd take a look.  Truth is, I hadn't touched a DC toolchain in the years since, and re-creating it was a mountain to climb for someone with just an hour or two per week sometimes of free project time. Though I didn't find the time, I thought about that email a lot. 

Fast forward to 2025. It was (ironic, I know), AI coding agents that got me back into programming in my spare time.  The ability to parallelize my work with another developer (in this case an agentic one), brought some fun back into it for me.  I guess after all these years as an executive I'm a social butterfly. At any rate, I started to think about that email again.  I decided the best thing to do was write a version of jc_reborn with an extremely low memory footprint, then I could simply re-port to DC with SDL1 calls and solve the issue (if memory truly was the issue.)

That effort went very well and through research, hard work and an agentic partner we proved we could get the memory well below 8mb.  And that's when that thing happens.  You know, that thing engineers do where they skip an easy problem for a harder one?  Yeah, I started to think about my large collection of gaming handhelds throughout the years. How many of them could run a dreamcast game? Only the newer ones, and not all of them.  How many though, could run a Playstation 1 game? Almost all of them, actually: from my first psp way back in 2004 to my steam deck and every phone for the past 15+ years. 

Then it clicked for me, hard. The PS1 could do 640x480 interlaced. That's Johnny's native resolution. It had 600mb+ of space for assets. It's been emulated, FPGA'd, and directly ran via chipset compatibility in the first four generations of playstation. Heck, maybe it could even run on the dreamcast via bleemcast? 

So it began, in 2025.  First locally, as part of the jc_reborn project.  Then it grew in scope.  I wanted freeplay mode, background music, scene skipping, chapter selection, seed pinning, closed captions, memory card support. Everything anyone could possibly want in a version of Johnny for the playstation.  Something that actually could have come out at the time (maaaybe). 

<img src="/content/images/2026/activity9-ps1-boat.png" alt="Johnny Castaway PS1 waving at a boat" width="640">


## The Journey Here

As with any major project, this one came in fits and starts. A straight port failed, with constant memory issues and minor bugs.  I spent months refining, before pivoting a few times into a methodology that actually worked.  A combination of host-pre-processing (essentially trading space for complexity) and relentless optimization. 

I found it though.  That magical flow state that all software developers crave. After months and months of pain, custom tooling, hacking, AI after AI, I settled on a flow that brought me great joy, and huge gains. 


- **Window 1**: Dunking Bird, double dunking on OpenAI Codex and Anthropic Claude
- **Window 2**: Claude, in an infinite editorial loop documenting progress on website/blog. 
- **Window 3**: Codex, in an infinite refinement loop regressing scenes against micro-optimizations in code and technique using headless docker containers.
- **Window 4**: Fresh editor (used to use vim), for direct coding and code browsing
- **Window 5**: Bottom monitor, keeping an eye on CPU, Memory, and Temperature
- **Window 6**: Duckstation Emulator, running a visual regression for me

All of this running on an old surface laptop (quite beat up, bought at thrift store), running KDE Neon, remote desktop'd in from my laptops/tablets/etc. A dream coding desktop always at my fingertips from anywhere. 

I mean, think about it.  I'm coding up new features or fixing small bugs while two AI agents spend every minute of every day refining speed and documentation. This is all running on a machine costing less than 100$ and the pro tier of codex and claude.  Bonus, while I'm at home I connect a bluetooth controller to it and test freeplay mode and menus directly. While I'm far remote, those get tested via headless session instrumentation. 

It feels incredibly futuristic, and the proof is in the result.  In this single year I've been able to complete my most ambitious port yet, all while maintaining a full time job and significant family responsibilities. 


## The Realness

There's some AI slop/crap in the website.  It's true.  It's also 100x better than the site I would have written for it.  You know my project sites: blog post, header image, links to download, credits.  That's about it. This has feature articles, guides, how-tos, real documentation, technical articles that are actually kind of interesting, and sometimes put an insightful spin on the technical challenges I faced.  These are not things I have the time to do, nor the inclination most days.  Yet here we are, with a really fun and informative project site. I'll review what I can, write when I can, but when I can't, I think this is a pretty interesting workflow for technical documentation.  An agent writes it as you struggle, not when you're finished. It's the struggle I find interesting, the challenge, the setbacks.  That's the good part. 

## The Desktop

Here's said workflow in action:

<img src="/content/images/2026/dev-environment-2026-05-06-w1600.jpg" alt="Johnny Castaway PS1 development environment" width="600">

[Full Version](/content/images/2026/dev-environment-2026-05-06.png)


## Getting It Over The Finish Line

This past month, I've actually engaged in an even more aggressive triple-dunking setup. You see, performance and correctness are often at odds with each other. Throw in memory pressure, and you have a real iron triangle situation.  Any change to one affects the other two significantly. My strategy to get this over the finish line was essentially a phased re-prioritization of efforts.  In the beginning, my focus was purely on getting things running at all.  Towards the end of the project, I rotated that iron triangle in phases.  Correctness, then speed, then correctness again.  Once I had all scenes working perfectly, I rotated that triangle and focused on speed.  Once I had the speed optimized for all scenes, I rotated back focused on correctness again.  Bouncing back and forth, regressing stray pixels and timing issues. 

<img src="/content/images/2026/triple-dunking.png" alt="Johnny Castaway PS1 late stage triple dunking screenshot." width="600">

Will this port ever be at the point where I call it 100% perfect?  I don't honestly know.  As I'm drafting this post we're less than 0.3% slow for 20% of the scenes.  A third of a percent. Acceptable?  Probably.  Perfect? No, and I'll continue to refine and update as I get the time.  Maybe someone else will too.  That's my hope with this mountain of documentation and how-tos and regression suites etc etc.  It should be straightforward for anyone with interest to set up a development environment and try something out, and know exactly how that's affected the runtime. Pretty cool, I think. In the meantime, we'll see how close to 100% I get this port for my planned V1 release mid-may. 

## Try It Out

**GitHub Repository**: You can find the complete source code, installation instructions, .bin/.cue files and documentation on GitHub: [huntergdavis/johnny-castaway-ps1](https://github.com/huntergdavis/johnny-castaway-ps1)

**Project Website**: You can find all the above, and so much more on the official project website. 
[hunterdavis.com/johnny-castaway-ps1](https://www.hunterdavis.com/johnny-castaway-ps1/)

## Have Some Fun

This is designed to run forever (or as long as your machine can take it), perfect for emulators, virtual CD drives, FPGAs etc.

<img src="/content/images/2026/johnny1-ps1-the-end.png" alt="Johnny Castaway PS1 ending scene" width="640">

## Why Johnny, Really?

Johnny Castaway was the software I couldn't afford on the computer I couldn't afford in 1992.  By the time I had one that could run screensavers, they were far out of vogue. Still, when I was able to I ran Johnny on whatever I could.  The story really resonated with me.  Here's someone trapped (perhaps a parallel to how you feel trapped in poverty), finding a way to have adventures and live life with very limited resources.  Making friends, finding love, and realizing what's really important in life.  By the time he's rescued and back to his programming job, he's dreaming of the place he found happiness, back on that island. The struggle wasn't the only thing he found on the island, he found himself and the way he wanted to live.  That's always stuck with me, and the ending scene where he's happily back on the island, that's powerful. Jeff Tunnell created this little, silly screensaver that's also somehow profound. I'm thankful for his efforts, and every port is an homage to the original, and his vision. 

---
