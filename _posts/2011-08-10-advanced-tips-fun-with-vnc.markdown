---
layout: post
title: Advanced Tips - Fun with VNC
date: '2011-08-10 14:53:35'
tags:
- access
- access-models
- arm
- embedded
- fun
- hacking
- linux
- login-tag
- logon
- network
- networks
- programming
- scripts
- security
- tricks
- unix
- vnc
---


While it will be a bit before my next full update in the”Using the Dockstar as a full Home Theater Replacement” series (conveniently shortened to Dockstar Stereo), I’m always tweaking and installing things. While these may not warrant a full update, they’re usually fun little additions or tweaks that come in handy. While I mentioned in the [last Dockstar Stereo article](http://hunterdavis.com/archives/2269) that you could run a video or Window Maker session over VNC, I never went into any details on the fun things you can do with VNC sessions. Read on for a couple of fun VNC tricks and tips that you may not have heard before. I assume you to be using a Linux installation. I’m running all examples on the ‘Dockstar Stereo’, an integrated arm board with limited memory.

[![](http://66.147.244.180/~hunterda/content/images/2011/08/vnssesh1-300x176.png "vnssesh")](http://66.147.244.180/~hunterda/content/images/2011/08/vnssesh1.png)

  
**Single Application Sessions**

[![](http://66.147.244.180/~hunterda/content/images/2011/08/fullscreen1-300x168.png "fullscreen")](http://66.147.244.180/~hunterda/content/images/2011/08/fullscreen1.png)

When tightvnc server loads up, it loads a shell script located at /home/username/.vnc/xstartup . Generally, people use this to start window managers or startup programs but it isn’t really necessary. It’s also a regular old shell script, that fully supports environment variables. For this reason we can comment out what we don’t want in the script, and add an environment variable for the startup application. I recommend installing ratpoison (`sudo apt-get install ratpoison`) as it auto-maximizes single application sessions. Edit your .vnc/xstartup so that it looks like the following: ```
<br></br>
xrdb $HOME/.Xresources<br></br>
xsetroot -solid grey<br></br>
#x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &<br></br>
#x-window-manager &<br></br>
# Fix to make GNOME work<br></br>
export XKL_XMODMAP_DISABLE=1<br></br>
#/etc/X11/Xsession<br></br>
ratpoison &<br></br>
$APP &<br></br>```

Now whenever you start a vncserver session, you’ll preface it with the name of the app. For instance, `export APP=banshee;vncserver ` will open a vncserver session with banshee as the only running item. This could be a full window manager such as window maker, but it could also be a single application session such as banshee or ssh. Below are some fun screenshots that may give you some fun ideas. You can set up a view-only password and do some viewcasting, or maybe do some collaborative document or playlist editing. Perhaps you just like having all of your apps concurrently available from anywhere, any device, etc. Sometimes the fact that this is all running on tiny 6-watt devices scattered throughout my house is mind blowing.

`export APP=banshee;vncserver `

[![](http://66.147.244.180/~hunterda/content/images/2011/08/banshee11-300x241.png "banshee")](http://66.147.244.180/~hunterda/content/images/2011/08/banshee11.png)

`export APP=conky;vncserver `

[![](http://66.147.244.180/~hunterda/content/images/2011/08/conky1-286x300.png "conky")](http://66.147.244.180/~hunterda/content/images/2011/08/conky1.png)

`export APP=gnome-system-monitor;vncserver `

[![](http://66.147.244.180/~hunterda/content/images/2011/08/gnome-system-monitor1-300x242.png "gnome-system-monitor")](http://66.147.244.180/~hunterda/content/images/2011/08/gnome-system-monitor1.png)

`export APP=gedit;vncserver `

[![](http://66.147.244.180/~hunterda/content/images/2011/08/gedit1-300x240.png "gedit")](http://66.147.244.180/~hunterda/content/images/2011/08/gedit1.png)

**Application Specific USERS**

Yes you read that correctly. Nowadays when most of us tech savvy folk connect to a VNC server we do so over an SSH session (even on my android phone). As such, in the background we’re actually logging into an ssh session on the host computer, tunneling the VNC port to our local machine, and connecting to that. As such, we’re actually authenticating twice. Once through SSH, and once through VNC. We can eliminate one of these authentication measures if we choose (blank passwords on VNC sessions, duplicate passwords for VNC and authentication, etc), but I’ll leave you to debate the merit of that security move. Rather, we’re going to take advantage of some of the built-in features that come with user authentication (like the security model). Users are placed into groups which restrict access to certain subsystems (i.e. audio, cdrom, network, dialout, superuser, etc). By modeling users after the functions they are allowed to perform (like smurfs), we can do some really fun things and ironically allow for a more “open” environment. Where could this come in handy? Imagine these scenarios:

- You’re running a coffee shop. You’ve got an embedded linux box doing double duty as the cafe firewall and the digital jukebox in the back, and you’d like to let your baristas queue up new music or let your customers view the currently playing track.
- You’re having a lan party. You’d like a simple leaderboard to be visible by all on any devices, but editable by the admins. You don’t know HTML, and have never set up apache.
- You don’t know how to program at all, but you’d like to host a VJ party for your friends.
- You have a merchant shop, with rotating displays you’d like to be displayed on all terminals, and you hate powerpoint
- You run a programming lab, and you’d like to easily try pair programming.
- You have 15 Linux boxes scattered throughout the world recording data. You want to be able to remotely administer them, while allowing your assistant to remotely view your progress
- You’re a hard-boiled FBI agent tracking down a hacker and serial killer who is on the loose. You want to set up a honeypot to give him false information, and you need an enticing target for your hacker to be able to “look over your shoulder” as it were.

Luckily for all of us each of these scenarios can be easily resolved with the same simple set of steps, and a liberal application of VNC. Let’s add a user Jukebox whose sole purpose in life is to play music.

1. Add the user jukebox with `sudo adduser jukebox`
2. This will prompt you for a password and username, set these according to your security preferences
3. Add the user jukebox to the bin, audio, and ssh groups with ` usermod -a -G bin jukebox && usermod -a -G audio jukebox && usermod -a -G ssh jukebox`
4. Log in as this user with `su jukebox`, then set a vncpassword for this user with `vncpasswd`
5. This will prompt you to set a vnc password, and a vnc view-only password.
6. Test that a basic vnc session works with `vncserver`
7. Edit your ~/.vnc/xstartup to contain only the program you wish this user to run as we did above.
8. Add vncserver to the user’s .profile (so it starts when we ssh in) with `echo vncserver >> ~/.profile`

And that’s that. Each of the scenarios above is just a customization of the security settings for the above steps. For instance in the coffee shop example above you could have the manager ssh into the jukebox when it first loads to start up a VNC session, then have the baristas connect using the normal VNC password and the customers connect using the view-only password.

[![](http://66.147.244.180/~hunterda/content/images/2011/08/vnssesh1-300x176.png "vnssesh")](http://66.147.244.180/~hunterda/content/images/2011/08/vnssesh1.png)


