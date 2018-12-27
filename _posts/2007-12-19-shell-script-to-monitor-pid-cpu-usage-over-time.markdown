---
layout: post
title: Shell Script to Monitor PID cpu usage over time
date: '2007-12-19 16:30:50'
---


Sometimes I feel like all the world’s problems can be solved with shell scripts. Here’s one that’s short and sweet. You give it a PID, interval, and outfile, and it keeps track of the PID given till the PID dies (or you kill the script). These values are plotted against time with gnuplot. I wrote it while keeping an eye on ‘top’ on a server. [Snag it here](http://www.hunterdavis.com/pidgraph.sh)


