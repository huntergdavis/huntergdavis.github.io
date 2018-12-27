---
layout: post
title: Secure SSH Terminal in your Steam Overlay
date: '2011-03-06 12:19:53'
tags:
- fun
- games
- linux
- ssh
- steam
- terminal
- windows
---


Here’s a fun thing I came up with for those Steam users out there. Ever wanted to use an SSH client in the middle of a Steam game? I’ve got an arm based server running constantly at my house (4 watts average power usage) doing menial chores like downloading and file serving and queuing up print jobs, playing music, etc. I prefer to SSH into a screen or byobu session, start a long task, then disconnect and check back later. If you’re relaxing at home playing a game in Steam however, you may not want to alt-tab out of your game session. Besides, if you’re running in Wine there’s a fairly good chance this will crash your game in some fashion. Short of booting up another computer or opening ports on your router to allow web-based ssh services to work, what is one to do? Read on for my solution to the problem.  
[![](http://66.147.244.180/~hunterda/content/images/2011/03/IMG_68921-300x225.jpg "Terminal In Steam")](http://66.147.244.180/~hunterda/content/images/2011/03/IMG_68921.jpg)

Steam is great. They keep adding new features, they have consistent and heavily discounted game sales, and they have a great shift-tab interface which allows you to open a steam browser window or take a screenshot of your game. I like the open source alternative [Taksi ](http://sourceforge.net/projects/taksi/files/)for taking screenshots myself, but that’s just me. What Steam does not offer is an ssh client or terminal. Though there are web based ssh solutions you can never really trust their security if you’re not running the service yourself, and who wants to open up ports to an outside service? I prefer to keep everything inside a local subnet.

This is where [Anyterm ](http://anyterm.org/download/index.html)comes in handy. It’s a GPL webservice that gives you a console. As you compile it from source, I didn’t have any trouble compiling it on my debian-based ARM server. The steps are pretty straightforward. However it can be even simpler than that. After setting up Anyterm I stumbled across [Ajaxterm](http://antony.lesuisse.org/software/ajaxterm/), a similar program with a much easier installation. I’ll run you through the installation for Ajaxterm below, with the installation for AnyTerm at the bottom of the article for anyone not wishing to run python on their server.  
**Installation of Ajaxterm (The Easy Way)**

1. Install prerequisites with `sudo apt-get install python`
2. Download and extract Ajaxterm with `wget http://antony.lesuisse.org/software/ajaxterm/files/Ajaxterm-0.10.tar.gz && tar -xvzf Ajaxterm*.tar.gz `
3. If you want to connect from other machines on your network without bothering with SSL (dangerous, you can still set up an stunnel as I show below), you can edit the file ajaxterm.py, and change “localhost” to be “IP_OF_YOUR_AJAXTERM_BOX” on line 560
4. Likewise, if you’d like to fiddle with the terminal rows/cols size you can directly edit the w/h variables on line 499
5. Execute the server daemon with `./ajaxterm.py -d -c 'bash'` This will keep a daemon running locally till you reboot your machine.
6. On any computer with access to your machine’s IP, fire up steam and open up the game browser. Head on over to `http://IP_OF_YOUR_AJAXTERM_BOX:8022` and you’ll be terminally happy

**Installation of Anyterm (The Hard Way)**

1. Install pre-requisites with `apt-get install zlib1g-dev libboost-dev stunnel4` (stunnel4 is optional)
2. Get the source code from subversion or a tarball, I pulled the latest copy from their subversion repository with `svn co http://svn.anyterm.org/anyterm/tags/releases/1.1/1.1.29/ anyterm-1.1.29`
3. Compile the anytermd daemon with `make` If smtpclient.cc fails to compile, just add a `#include <cstdio> `
4. Copy the resulting anytermd executable somewhere, and make sure you have permission to run it.
5. I recommend tunneling through stunnel4 as described on the [anyterm installation page](http://anyterm.org/1.1/install.html), otherwise you can ignore anything related to stunnel
6. Generate your SSL certificate for stunnel with the following commands `openssl req -new -x509 -nodes -days 365 -out stunnel.pem -keyout stunnel.pem`  
`dd if=/dev/urandom of=temp_file count=2`  
`openssl dhparam -rand temp_file 512 >> stunnel.pem`  
` ln -sf stunnel.pem `openssl x509 -noout -hash <br></br>chmod 600 stunnel.pem`
7. Start the anytermd daemon with `anytermd  -p 4567--user=YOURUSERNAME -c 'bash'` This will spawn a daemon in the background, which will continue running till reboot.
8. Start the stunnel proxy server with `stunnel -d 6789 -r 4567 -p stunnel.pem -P ''` This will also spawn a daemon that will run till you reboot.
9. Now, on any computer with access to this machine's IP, fire up steam and shif-tab into a browser. Enter `https://IP_OF_YOUR_ANYTERMD_BOX:6789/` and you're ready to administrate while gaming 🙂


