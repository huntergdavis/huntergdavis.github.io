---
layout: post
title: Half a line of shell to display to screen while compressing output... The most
  useful shell I've written in forever
date: '2008-06-10 08:11:16'
---


Ok, so here’s the deal. I write a lot of C in my line of work, so when I get the chance to write some clever shell script, I relish it. I do a lot of long supercomputer simulations, which tend to be hard to debug (especially when a problem arrises 3 days into a 4 day run). This is where logfiles come in handy, I know I’m not alone in this. Unfortunately, for really long runs these logfiles can add up to hundreds of gigs of space, which is a hard to come by commodity on supercomputing clusters. I found numerous solutions online, all of them tending to be long and overly complex shell scripts… No thanks!, when I want something done on shell it needs to follow the shell paradigm, small and powerful.

The problem:  
 I want to see the logfiles as they are created, but I also want them stored and compressed and not taking up space.

The solution:  
 ———————————————————  
` | tee >(gzip > logfile.tgz) `  
 ———————————————————  
 Let’s break it down one bit at a time  
` | tee `  
 Standard output is piped through tee, the unix t-shaped pipe, pretty much comes standard with all *nixes. Tee has two outputs, first it outputs to a file (or file handle), and second it pipes the output to the screen.

` >() `  
 This right caret/parenthesis pair comes in very handy. It opens a sub shell, leaving an implicit file handle that can be piped to. Tee sees this as a regular file, and begins piping standard output to it.

`gzip > logfile.tgz`  
 Gzip defaults to standard in for the input if no file handle is given. It uses lz77 encoding along with Huffman trees in a 32k sliding window. Decoding data (Huffman trees) are placed at the beginning of each block. This means

6. that it can compress iteratively
7. the CPU/memory overhead is pretty much nil.
——————————————————–  
`| tee >(gzip > logfile.gz) `  
 ——————————————————–  
 Putting it all together, we pipe standard output to tee which pipes to screen as well as the implicit file handle created by the sub shell. The sub shell is gzipping the piped standard input at maximum compression and outputting the resultant gzip file to logfile.gz. Just pipe any huge log file through this bit of code, and you’ve taken your space requirements from gigs to megs, with virtually no cpu/memory overhead. Handy, and fits easily into most launch scripts.


