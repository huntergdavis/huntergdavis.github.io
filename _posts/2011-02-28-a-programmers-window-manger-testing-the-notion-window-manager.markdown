---
layout: post
title: A Programmer's Window Manger - Testing the Notion Window Manager
date: '2011-02-28 14:43:21'
tags:
- desktop
- ion
- ion3
- linux
- notion
- programming
- shell
- window-managers
---


Following up on my previous post, NeonLicht suggested I try out the Ion window manager. Being a big fan of alternative window managers etc, I decided to give it a whirl. Turns out that the most current version of Ion, Ion3 has been branched and reborn as the [Notion window manager.](http://notion.sourceforge.net/) After some general use I’ve come to the conclusion that while it’s not for everyone, it’s a terrifically interesting and forward-facing implementation of a window manager. Also, providing you’re willing to compile the source from git (instructions after the jump), the setup for an ideal programmer’s desktop becomes rather simplified from my last post. Read on for all the detailed info.  
[![](http://66.147.244.180/~hunterda/content/images/2011/02/2011-02-28-132358_1600x900_scrot1-300x168.png "Notion Desktop")](http://66.147.244.180/~hunterda/content/images/2011/02/2011-02-28-132358_1600x900_scrot1.png)  
  
**Compilation and Installation**  
 First you’ll want to checkout the project from git. Create a nice working directory, then execute a `git clone git://notion.git.sourceforge.net/gitroot/notion/notion<br></br>` in said directory. This will check out the Notion source code. This comes with a nice writeup on how to install. For other Ubuntu/Debian users, it basically boils down to a quick 4-step install.

1. Install Prerequisites
2. Edit system.mk
3. Compile and install
4. Create an Entry for GDM

**Installing Prerequisites**  
 As per the instructions on the [Notion Wiki,](http://sourceforge.net/apps/mediawiki/notion/index.php?title=Development) you’re going to need to install and compile some prerequisites for Notion. If you’ve done this for Ion, you should be used to the process by now. First, install the prerequisite libraries from apt with `sudo apt-get install lua5.1 liblua5.1-0-dev libx11-dev libxext-dev libsm-dev gettext`

Next, you’re going to need to pull the git libraries for libtu and libextl. In the same Notion project director you created above, execute the following 2 git checkout commands. `git clone git://notion.git.sourceforge.net/gitroot/notion/libtu`  
 and  
`git clone git://notion.git.sourceforge.net/gitroot/notion/libextl`  
 These check out the libtu and libextl libraries, needed by Notion (and Ion3).

**Edit System.mk**  
 Edit the system.mk file that came with Notion, and uncomment the 4 Debian/Ubuntu LUA_ variables starting on line 74. You’ll also need to edit the system.mk file that came with the lbiexl library above, and uncomment the 4 Debian/Ubuntu LUA_ variables starting on line 62.

**Compile and Install**  
 First, compile and install libtu and libextl with the usual `make && sudo make install` . Once these have finished installing, you are free to proceed with the main Notion compilation.  
 Compile and install Notion with `make && sudo make install`

**Adding An Entry to GDM**  
 For those of you coming from Ubuntu/Debian and are using a GDM type login manager, you’ll want a selectable entry when you login. Edit a file named `/usr/share/xsessions/notion.desktop`, and paste the following text within.  
```
<br></br>
[Desktop Entry]<br></br>
Encoding=UTF-8<br></br>
Name=Notion<br></br>
Comment=This session logs you into Notion<br></br>
Exec=notion<br></br>
Icon=<br></br>
Type=Application<br></br>```

**Day to Day Usage**  
 There are a few things that a typical Gnome desktop user may find confusing or irritating when they first startup Notion. First, if you’re not attached to NetworkManager, I recommend installing WICD. It’s a terrific network manager and runs without the need for a taskbar.  
 For those needing to start quickly, remember the F2, F9, and F12 keys. F2 opens a terminal into a current frame, and F12 opens the main menu at the bottom of the screen (much like vim or emacs). Frames are set locations which programs open into, in a tabbed fashion (like Chromium or Firefox). You can resize these frames with alt+right-click, though once you have a nice desktop full of frame positions this shouldn’t be a common operation. Multiple pressings of F12 will cycle through the standard menu options, and the F12 run… menu allows for automatic terminal completion of actual commands. Configuration and menu entries are controlled via text files ala Fluxbox. Workspaces as a concept still remain, though they are created on the fly. Create a new workspace with F9, which you can use to tab through all available workspaces. You can also directly switch between workspaces with alt->#, where # is the workspace number. Finally, if you’re constantly switching between terminals and leaving some open in screen windows etc, it’d be handy if your bash history was constantly updating. Just edit your .bashrc and append `PROMPT_COMMAND="history -a; history -n"` This has the added effect of enabling you to keep a window with a running log of all your shell activity for each window using `tail -f ~/.bash_history`

For those following the previous article, you can setup the same programmer’s background near instantly as follows.

1. Split the Left Frame Vertically. I like to use alt + right-click to resize the windows to about the 75% mark
2. Split the Right Frame Vertically
3. Split the Top Right Frame Horizontally
4. Attach Terminal (F2) to the Top Left Frame
5. Attach Terminal (F2) to the Bottom Left Frame
6. Attach Terminal (F2) to the Bottom Right Frame
7. Attach gedit (F12->run…->gedit) to the Center Right Frame
8. Attach conky (F12->run…->conky) to the Right Right Frame

And that’s it! Ideally, you should never really need to use the mouse for window manager operations, though typical browser and gedit copy/pasting causes me to relapse often. Now get coding!


