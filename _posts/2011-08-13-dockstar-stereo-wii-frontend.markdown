---
layout: post
title: Dockstar Stereo + Wii Frontend
date: '2011-08-13 16:21:08'
---


Chris Irwin alerted me in a previous article about MPD, the music playing daemon. While I was planning on installing this as both a client and a server on the dockstar stereo, It turns out there’s a MPD frontend for the Wii. I hadn’t been giving my Wii very much love lately, being so active in the PS3 scene. On a whim I picked up a little tv to use as a monitor for the Dockstar stereo, and I hooked the Wii up to it to see how things were going in the Wii homebrew community. I was BLOWN away. Not only has the wii media center grown tremendously, (it streams from samba shares), all the emulators have been updated (ps1 games from samba shares!), and there’s a tremendously dynamic game modification community (check out smashmods for some of the coolest in-ram game modification you will EVER see). The wii VNC client works quite well as a head unit for the dockstar stereo, but it’s got a native MPD frontend that I thought would be fun to get running. Read on for the setup of MPD on the Dockstar Stereo (or any embedded arm linux).

[![](http://66.147.244.180/~hunterda/content/images/2011/08/IMG_20110813_1442451-300x224.jpg "IMG_20110813_144245")](http://66.147.244.180/~hunterda/content/images/2011/08/IMG_20110813_1442451.jpg)

  
**Installing MPD**  
 First, install the MPD prerequisites with:

`sudo apt-get install mpd mpc sonata`

This will set you up with the basic daemon and the sonata graphica client. After that finishes installing, edit the system wide configuration with `sudo vim /etc/mpd.conf` and change the settings to your liking. Specifically,

1. Un-comment the two zeroconf_ lines to be enabled if you wish to have zeroconf/avahi support (nice)
2. Change the music_directory to point to your actual music directory
3. Uncomment the mixer_type = software line
4. I like to have MPD settings stored under /user/mpd, so change all references to /var/mpd to /usr/mpd and create a /usr/mpd directory that is user readable with `sudo mkdir /usr/mpd && sudo chmod 777 /usr/mpd`

Now save this file, and then restart MPD with:  
`sudo /etc/init.d/mpd restart`

This will also restart the database creation process if you've changed the location in the configuration as I did above. It'll take a while for the database creation to finish, I recommend throwing up a top screen and checking it every once in a while. You can load up Sonata in a VNC session (or wiiVNC if you like) and get some playlists made, start a playlist playing, play tracks, etc.

**Using WiiMPC**

Install WiiMPC as you would any other homebrew app (homebrew channel, homebrew launcher, etc). Ftp over to your wii (or pop out the SD card and insert it into your computer) and edit a new file called `/YOURWIISDCARDROOT/apps/wiimpc/wiimpc.conf`  
 Enter into this file a single line containing your MPD server address like:  
`MPD_HOST = 192.168.0.161`

Now load up wiiMPC in your wii and you should be connected to your Dockstar Stereo and ready to play some music 🙂


