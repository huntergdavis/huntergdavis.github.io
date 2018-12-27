---
layout: post
title: A Programmer's Desktop Background
date: '2011-02-21 12:31:54'
---


While not famous in any sense of the word, I’m pretty used to having folks come up to me in public and ask me questions. These are usually along the lines of “I’ve never seen a laptop like that before..did you build it?” (yes I did) or “how did you get it to do that?” (Linux, mostly). Lately, I’ve had a few people comment on my somewhat unique desktop “wallpaper” I use on my laptop, and I thought I’d do a quick tutorial for those coming in off google searches :). This is basically a 5-up devilspie embedded application background consisting of terminals, text editors, and conky. I keep these on my primary desktop in Ubuntu at all times, and this is the configuration I’ve found to be optimal. Read on for the detailed setup guide and rationale behind this configuration

[!["Embedded Windows As Desktop Background](http://66.147.244.180/~hunterda/content/images/2011/02/5updesktop1-1024x576.png "5 Window Desktop Background")](http://66.147.244.180/~hunterda/content/images/2011/02/5updesktop1.png)

Now, I know what many of you are thinking. You’re thinking, “why not just embed one huge terminal and run a 4-plex screen instance inside? I actually preferred that setup for many years, but I’ve since switched to a split layout featuring a gedit window and conky. Why? Well first of all screen is an excellent screen multiplexer, but it becomes quite an involved problem when you start to squeeze oddly shaped terminal sizes together. Using devilspie to adjust each window as a separate profile is quick and allows us to load programs separately at our leisure.

I also know what others are thinking. You’re thinking, “Are you not effectively just putting together an IDE?”. It’s a fair question. We are effectively embedding an IDE into the background, however the components of this IDE are highly decoupled. While one terminal may be editing a C file, another outputting from a log, and yet a third stepping through GDB, these three processes may be for completely different projects. For me at least, IDES’s are of the most use when you’re using all their features cohesively on a single task. While this is great when you’re working on that single feature for that huge project or deadline, most of the time your attention is split three ways ten times over. And it’s during this time that a decoupled interface provides the most benefit.

As it is a web-focused world, I keep a chromium instance at the ready in Desktop 2 for fast web browsing. The vast majority of my time on the computer not spent web browsing can be split into the following four activities.

1. Editing Source
2. Git Commits
3. File Operations
4. Writing Myself Notes

As such, I prefer to have a dedicated window for each task at the ready. In addition, I want to know the current status of the system at a glance, see the current state of the message log, and have a visual copy-paste buffer. My memory isn’t what it used to be, and I tend to have 5-10 items in my copy-paste scratchpad at any one time. To fulfill each of these requirements simultaneously I need a minimum of 5 windows.

1. Editing Source Window –> Xterm 1
2. Git Commits Window –> Xterm 2
3. File Operations Window –> Xterm 2
4. Message Log Window –> Xterm 3
5. Writing Myself Notes Window –> gedit
6. System Status Window –> conky

I’ll go over the configuration of each of these in detail below. You can skip any sections that are not of interest, as the highly decoupled nature of our “IDE” allows us to work on each section as its own self contained tutorial. I’d also be interested to hear from any of you on what layout/configuration works best for you. For each of the below sectins, ensure you’ve installed devilspie and created a devilspie directory with `sudo apt-get install devilspie && mkdir ~/.devilspie` My desktop resolution is 1600×900, so if yours is larger/smaller remember to adjust the below height/width values to account for the difference in screen size. Ensure that devilspie runs on startup, and before any of the below applications (system->startup applications).

**Editing Source Window –> Xterm**  
 For our editing source window, I prefer a left-top window orientation (the F-shaped reading pattern). Fire up an editor, and paste the following code into `~/.devilspie/EditSource.ds`  
```
<br></br>
(if<br></br>
        (matches (window_name) "EditSource")<br></br>
        (begin<br></br>
                (set_workspace 1)<br></br>
                (below)<br></br>
                (undecorate)<br></br>
                (skip_pager)<br></br>
                (skip_tasklist)<br></br>
                (wintype "utility")<br></br>
                (geometry "721x625+4+29")<br></br>
        )<br></br>
)<br></br>```
  
 Now just add the following line to your startup applications, after devilspie. `xterm -T "EditSource" bash`

**Git Commits & File Operations Window –> Xterm**  
 For our git commits and file log window, I prefer a right-bottom window orientation (similar to the assembly output bar in most IDEs). Fire up an editor, and paste the following code into `~/.devilspie/GitWindow.ds`  
```
<br></br>
(if<br></br>
        (matches (window_name) "LogWindow")<br></br>
        (begin<br></br>
                (set_workspace 1)<br></br>
                (below)<br></br>
                (undecorate)<br></br>
                (skip_pager)<br></br>
                (skip_tasklist)<br></br>
                (wintype "utility")<br></br>
                (geometry "870x254+730+650")<br></br>
        )<br></br>
)<br></br>```
  
 Now just add the following line to your startup applications, after devilspie. `xterm -T "GitWindow" bash`

**Message Log Window –> Xterm**  
 For our message log window, I prefer a left-bottom window orientation (similar to the debug output bar in most IDEs). Fire up an editor, and paste the following code into `~/.devilspie/LogWindow.ds`  
```
<br></br>
(if<br></br>
        (matches (window_name) "LogWindow")<br></br>
        (begin<br></br>
                (set_workspace 1)<br></br>
                (below)<br></br>
                (undecorate)<br></br>
                (skip_pager)<br></br>
                (skip_tasklist)<br></br>
                (wintype "utility")<br></br>
                (geometry "721x251+4+675")<br></br>
        )<br></br>
)<br></br>```
  
 Now just add the following line to your startup applications, after devilspie. `xterm -T "LogWindow" -e "tail -f /var/log/messages"`

**Writing Myself Notes Window –> gedit**  
 For our gedit window, I prefer a middle window orientation, right in the center of things. I like to have a scratchpad open for visual copy-paste, as well as my bash_history open for quick lookup of previous commands. Fire up an editor, and paste the following code into `~/.devilspie/ScratchWindow.ds`  
```
<br></br>
(if<br></br>
        (is (application_name) "gedit")<br></br>
        (begin<br></br>
                (if (contains (window_name) "scratchpad.txt")<br></br>
                (begin<br></br>
                        (set_workspace 1)<br></br>
                        (below)<br></br>
                        (undecorate)<br></br>
                        (skip_pager)<br></br>
                        (skip_tasklist)<br></br>
                        (wintype "utility")<br></br>
                        (geometry "543x615+730+29")<br></br>
                )<br></br>
                )<br></br>
        )<br></br>
)<br></br>```
  
 Now just add the following line to your startup applications, after devilspie. `gedit ~/scratchpad.txt ~/.bash_history`

**System Status Window –> conky**  
 For our conky window, I prefer a right-middle window orientation (similar to an instant message friends list). Fire up an editor, and paste the following code into `~/.devilspie/ConkyWindow.ds` Please note, if you have conky setup to display your hostname you’ll need to change your application name to “conky (yourhostname)”. I prefer to leave some free space around the left side of the Conky window as some of my storage names are dynamic and can get quite long.  
```
<br></br>
(if<br></br>
        (is (application_name) "conky")<br></br>
        (begin<br></br>
                (set_workspace 1)<br></br>
                (below)<br></br>
                (undecorate)<br></br>
                (skip_pager)<br></br>
                (skip_tasklist)<br></br>
                (wintype "utility")<br></br>
                (geometry "310x600+1290+39")<br></br>
        )<br></br>
)<br></br>```
  
 Now just add the following line to your startup applications, after devilspie. `conky`


