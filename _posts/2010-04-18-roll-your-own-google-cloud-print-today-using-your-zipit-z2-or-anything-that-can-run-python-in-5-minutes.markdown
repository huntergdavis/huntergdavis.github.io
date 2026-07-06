---
layout: post
title: Roll your own Google Cloud Print, Today, Using Your Zipit Z2 (or anything that
  can run python), in 5 Minutes
date: '2010-04-18 23:04:44'
tags:
- cloud
- computing
- google
- hacking
- linux
- python
- z2
- zipit
project: zipit-z2
---


When I read about Google’s new [strategy](http://mashable.com/2010/04/16/google-cloud-print/) for cloud printing, I thought “hey that’s great!, wish I could use it before 2011!”. Thankfully, I run linux on damn near everything. As I don’t have an android (which would be a pretty ideal running platform for this…), I’ve used the Z2 as my “drop in” cloud print server. Doesn’t seem like it’ll take the manufacturing companies long to integrate this into new product lines, as it’s pretty simple. Instructions and source code links below!  
![cloud printing from the zipit z2](/cloudprint.jpg)

So here’s the plan. We’re going to configure our Z2 to periodically check an email address for emails with attachments. When it finds an email with an attachment, it prints the attachment and archives the email. As you can see from the photo, I place a little notecard on the Z2 which states “Email __EMAILREDACTED___ to print to this printer”. If you want to print to this device “from the cloud”, just email to it. Pretty simple :), and the arm in the Z2 takes up a fairly low wattage overhead as a cloud monitor/print server.

1. First, we’ll want to connect the Zipit to an existing printer. As I’ve got a network printer at work (fairly common situation), I’ll use that as the example case. Using one of the linux (I’m going the debian (easy) route) Z2 distros that’s popular, boot your Z2 up and get it connected to the net/up to a state where it can update via apt get. Then ` apt-get install cups ` for printing., and ` apt-get install gmail-notify ` to install all the relevant pre-reqs for python. That’s one thing that’s great about python on embedded, if you know another popular python program uses all your libraries, just install that first and you’ve got your prerequisites covered…or at least all the ones I can remember 🙂 You can set up cups to handle various filetypes for printing, but it should come with postscript by default and that’s enough for me
3. Next, we’ll configure the Z2 to print to a network printer. This will be your “drop target”. You can either use one of the gui printing configuration tools (select IP Printer from the drop-down list), or the cups command line or web tools. From the [debian wiki](http://wiki.debian.org/SystemPrinting), cups runs a web daemon locally than can be used to configure new printers. After installing cups, you can ` elinks http://localhost:631/ ` to get to an administration website. From here it’s pretty trivial to print, as your apt-get should have pre-configured a lot of cups for you i.e. samba, workgroups info, etc (interactively in my case).
5. As this’ll be an open source solution, there’s no need to re-invent the wheel. [Suresh Kumar wrote](http://code.activestate.com/recipes/498189-imap-mail-server-attachment-handler/) an imap attachment handler in python that’s fairly compact, we can use that as an excellent base to write our script. It’s [PSF licensed](http://python.org/psf/license/), so you know it jives with our GPL sensibilities.
7. Now in this script it stores all attachments into their own hierarchical directory structure. You can remove this if you like, but I kind of like having a print backup, at least for a few weeks. This is the write_file() function. Wherever this is called you can add your own os.system call to print the file. For the lazy, if your printer is named “JACKBAUER” at the end of this function just add `sysCommand = "lpr –P JACKBAUER –#1" + filename` . This fills a string buffer named sysCommand with our command to print using the lpr function (cups standard printing function). Follow this line with ` os.system(sysCommand) `
9. Now that your python script is finished, create a script to execute the attdownload.py with the proper variables (username, server, etc perhaps make it a background process with nohup etc). Make the script executable, and you’re good to go. Either add it to your rc.local so it runs on startup or add it to your bash.rc so it loads on login. Congrats! You live in a world with email capable printers 🙂


