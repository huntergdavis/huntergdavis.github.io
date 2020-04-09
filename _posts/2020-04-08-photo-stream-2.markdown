---
layout: post
title: Using GitPod for a Simplified Custom Jekyll Workflow
date: '2020-04-08 16:20:00'
quickgrapher: false
---


Ugh, is there anything worse than token management?  Permissions, scopes, leaks, bleh.  Avoiding the cycle of security patches and constant upkeep is a major reason I migrated this blog to gh-pages. 

So, it was to my dismay when I set up the aforementioned photo-stream on my blog, as I had to hack it together with two separate repositories.  Lame.  Every time I attempted to combine the two, I would run into workflow issues (Github only allows token secrets required to push to a repository in private repositories comes to mind.)  This is on top of the complication of needing to statically link and compile libvips, preventing us from using GitHub's built-in Jekyll workflow. 

I had been meaning to try out GitPod for a while now (it is free for open source projects after all), and with a bit of time on my hands recently I thought I'd give it a shot as a manual workflow replacement for Github actions.  

It works great!  I authenticated it to have read/write access to my photo_stream repository, and you can see the dockerfile I've created. It's a fork from the libvips comment section ;) 

My workflow is very simple now, easy to do on the run.  I simply upload a photo to the originals directory in the photo_stream_backing directory through github (web or client.)  Then I launch a GitPod instance, and it regenerates the site and pushes back to the master branch for serving.  No need for a backing repo, or any user input.  Best of all, I don't have to worry about key management, that's still on GitHub.  
 


- Find Maxvoltar's original source here -> https://github.com/maxvoltar/photo-stream
- Find my modified template here and the generated site combined here -> https://github.com/huntergdavis/photo-stream
