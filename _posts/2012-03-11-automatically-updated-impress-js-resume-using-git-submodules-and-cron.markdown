---
layout: post
title: Automatically Updated Impress.js Resume using Git Submodules and Cron
date: '2012-03-11 00:11:59'
---


As someone who has hired and been hired many times, I’ve seen and written my fair share of resumes.  Clean white sheets tree pulp embossed and inked with the accomplishments of the writer.  What an outdated system!  Worse still are the PDF and Word resumes, emulating the old pulp and ink model.  Ignoring the fact that you can’t convey motion, video, or interactivity in a paper resume, the main downside from my perspective is a lack of open source spirit.  All these resumes floating around and they’ve never taught anyone anything besides a written history of a job candidate.  Bleh.

[![](http://www.hunterdavis.com/content/images/2012/03/impressjsresumecontents-300x232.png "impressjsresumecontents")](http://www.hunterdavis.com/content/images/2012/03/impressjsresumecontents.png)

So I set out to change that.  I’m re-writing my resume as an HTML page with CSS transforms and interactive Javascript and HTML5 elements.  I’ve also released the project as open source on GitHub, so anyone can follow along as I learn more about impress.js, snag the source for their own resume, or just poke around at the guts.  I’ve started preliminary work on the resume, and it’ll get updated steadily as I get more free time.  I realized after the first couple of commits that I’d like to have a live version of the latest code always available online.  Preferably without any interaction or external script wizardry from me.  As it turns out, It’s no easy task to accomplish through the use of GitHub Pages and git submodules.  My resume pulls impress.JS as a Git submodule, but GitHub doesn’t forward links to submodules in Pages.  The end result is that the use of another open source project as a submodule is not a viable option for GitHub Pages sites.  This is unfortunate, but I worked around it using the tools available to me on Bluehost.

First, I ssh’d into my account and cloned my resume repository into a /resume/ directory with

git clone https://github.com/huntergdavis/Hunter-Davis-impressjs-Resume.git resume

Next, in that same SSH shell I created a bash script that could be run with cron that would update this repo every hour:  
 #!/bin/bash  
 cd ~/public_html/  
 cd resume  
 git pull  
 git submodule update

Finally, I used the BlueHost control panel to tell my cron script to run every hour.  That’s that!

You can always view my latest impress.js resume at [www.hunterdavis.com/resume/](http://www.hunterdavis.com/resume/)


