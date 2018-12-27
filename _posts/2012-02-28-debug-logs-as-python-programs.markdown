---
layout: post
title: Debug Logs as Python Programs
date: '2012-02-28 16:52:41'
tags:
- debugging
- hacks-2
- programs-2
- python
- tips
- tricks
---


As a programmer (or sysadmin, IT professional, cluster maintenance worker, scrum leader, etc) there will absolutely be times that a debugger isn’t powerful enough or optimal enough or simple enough.  For some classes of problems, whether they be visual (graphs, animations), size (too much stuff changing too quickly), security (only munged objects come with this module) etc, a debugger will only hinder your ability to work.  We inevitably go to data logging for these classes of problems, as it’s quite simple to learn and generally the first method that we’re taught.  Unfortunately, it’s also the most lackluster and limited method of debugging information that we have.  However, it doesn’t have to be.  I’m going to be highlighting a super simple but powerful idea that may just change the way you debug.  Debug logs that are fully executable Python programs.  Read on for more info and some examples.

<div class="wp-caption alignnone" id="attachment_2586" style="width: 306px">[![Seriously, you can do a lot with debug images](http://www.hunterdavis.com/content/images/2012/02/Screen-Shot-2012-02-28-at-8.48.56-AM-300x242.png "Do Your Debug Logs Look Like This?")](http://www.hunterdavis.com/content/images/2012/02/Screen-Shot-2012-02-28-at-8.48.56-AM.png)Do your debug logs do this?

</div>Think about it, the glorious wonderland of easy includes, graphing, data processing etc that comes built into Python is probably already installed on every workstation in your office, and executes non-compiled textual information.  You can take the idea as far as you wish.  If you just need a simple email sent off, perhaps the output of your program is piped directly into a Python execution environment.  If you need to analyze data after it’s been pushed to a database, perhaps your program outputs a script that is run immediately upon output.  Maybe you want to do some serious computation with your logs, but only at a later date or if something goes wrong.  Just output a python script for posterity.  (As an aside, I think that’s a great catch phrase.  “How should we log this data Bob?”  “Just output a python script for posterity!”).  Here are a few real-world examples to get you started.  Feel free to post up suggestions, I’d love to hear more recipes from other folks who use Python to debug.

**Having your Logs Graph Data**

This one’s an especially easy one.  I like to use matplotlib, but you can easily use any number of Python graphing utilities.  Just make sure you output the correct ‘include’ statement.

1. Include matplotlib
2. Set a variable for X values equal to your range(0,rangetop)
3. Set a variable for Y values which are equal to the data you wish to graph, you can add elements to this array in a loop etc
4. Set the axis scaling for an appropriate range if you don’t wish to auto-scale
5. Plot the graph!

**Having your Logs Animate Data**

This one is just a minor tweak on the above graph.

1. Include matplotlib and time
2. Call ion() before your animation loop
3. Set a variable for X values equal to your range(0,rangetop)
4. Set a variable for Y values which are equal to the data you wish to graph, you can add elements to this array in a loop etc
5. Set the axis scaling for an appropriate range if you don’t wish to auto-scale
6. set a variable equal to your Plot the graph function
7. Update the Y values you wish to change in your animation
8. Update the Y values in the graph with a call to variable.set_ydata(Updated Y Values)
9. Call plot.draw() after the y values have been set.  You may wan to call this 20 or 30 times to match your desired frames per second.

**Having your Logs Process and Email Data**

This works best if your program output is being piped or executed directly after program execution.  Let’s say you know the content of your output in advance, and want to match it to an MD5 hash previously known

1. Import md5 and smtplib
2. Set a variable to md5.new(‘your data to be md5 validated’).digest(), this is your generated md5 hash
3. Compare it to the known md5 (or read it in from a text file)
4. If it doesn’t match, generate strings for TO, FROM, MESSAGE, SUBJECT, etc as per the [Python documentation](http://docs.python.org/library/email-examples.html)
5. Use these strings to send an email via smtp as per the linked documentation

The world of Python is at your fingertips.  As you’ve seen above debug logs don’t have to be static blocks of incomprehensible text.  With a little bit of forethought, your logs can be infinitely flexible and incredibly powerful tools for all who use your system.  When was the last time you could say that about a debug break point?


