---
layout: post
title: "It happens so fast now, Johnny Castaway RetroArch released"
date: '2026-08-28 20:57:00'
image: "/content/images/2026/johnny-castaway-retroarch-web-player.png"
tags: [johnnycastaway, retroarch, libretro, webassembly, port]
featured: true
featured_group: johnny
---

*No AI was used to draft this post, these are my words fully.*

What does it mean, when your hard-fought efforts can be replaced in a moment of inspiration and a few dollars of tokens.  I find myself asking that very question today, as I watch an AI agent put the finshing touches on a port of Johnny Castaway to retroarch.

I mean, why not? I started on this project years ago and got distracted and discouraged and eventually distanced from it. Why wouldn't I ask an AI to finish it up, to port Johnny to dozens (or more) of systems in one fell swoop.

One month after I released my magnum opus, Johnny Castaway on the PS1, which itself took every spare moment of my life for a year to release, I asked an AI to write a retroarch port. It did a great job. There's so many systems he can run on now. It took one day.

A year of my life... one day. So many of us in our industry are wrestling with what that means for our profession.  I'm wrestling with what that means for my hobby. Every day I see a dozen new reverse engineering projects, ports to older systems, impossible things.  Things which used to take years and months and sweat and years of tears.

I'm lucky.  I spend most of my time coaching leaders, making decisions, weighing options. I know exactly what AI means to my business and my engineering departments.  Review, at a speed never imagined. Creation is no longer the bottleneck or the primary domain of humans. It's review, curation, selection, and manual oversight after all the AI guardrails and systems.  Always a human reviewing. That's medical software in 2026, and I don't think that'll change next year. At home though?  In entertainment?  In games?  In mods and hacks and custom firmware and reverse engineering?  The human is so often becoming just the spark at the beginning. And I find myself thinking of that.  One year... one day. How much what I expect from my computing environment has changed even day to day. I'm still in the terminal, but i'm in a terminal on some far future sci-fi fantasy novel. Every day, multiplexed and dunked 10x.

Do I mourn what's lost or celebrate what's gained? Even setting aside the societal cost, it's made for a turbulence and a negative shift in my industry. I'm on optimist though, and I believe we can lead our way through it with empathy and understanding.

That said, here's Johnny Castawy ported to retroarch.  I've kept some of my personal improvements (closed captions, scene descriptions, chapter select, extra holidays.) This should run on a lot more systems now, here's the full list (library and package releases):

- Linux
      - x86_64
      - x86
      - ARM64
      - ARMv7/VFP
      - ARMv7/NEON

  - Windows
      - x64
      - x86

  - Android
      - ARM64
      - ARMv7
      - x86_64
      - x86

  - Apple
      - macOS (Intel and Apple Silicon)
      - iPhone and iPad
      - Apple TV
      - iOS and tvOS simulators

  - Web
      - Emscripten/RetroArch Web

  - Sony
      - PlayStation Portable
      - PlayStation Vita and Vita TV
      - PlayStation 2

  - Nintendo
      - Nintendo Switch
      - Nintendo 3DS
      - GameCube
      - Wii
      - Wii U

Direct installable packages are available for :

- PSP: EBOOT.PBP with a Memory Stick directory layout
- Switch: .nro
- Nintendo 3DS: .3dsx and .cia
- GameCube and Wii: .dol
- Wii U: .rpx
- PlayStation Vita: .vpk
- PlayStation 2: .elf

Here's the GitHub project: [github.com/huntergdavis/johnny-castaway-retroarch](https://github.com/huntergdavis/johnny-castaway-retroarch)

Here's the project site: [hunterdavis.com/johnny-castaway-retroarch](https://hunterdavis.com/johnny-castaway-retroarch/)

Here's the [live Web player](https://hunterdavis.com/johnny-castaway-retroarch/play/) (RetroArch version, which makes this my fourth JC Web player).
