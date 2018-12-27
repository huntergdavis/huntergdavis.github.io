---
layout: post
title: Using the Dockstar as a full Home Theater Replacement - Part 1
date: '2011-08-09 22:12:54'
---


As you’re probably already aware if you are reading this, I’ve got a thing for embedded systems. I guess we all do now, what with Android and iPhone tearing up the sales numbers. That said, I’ve never before had the guts to try and replace my aging Sony Dream Theater stereo system that’s hooked up to my beloved record player. Although the sound quality coming off the head unit is quite good (I replaced the speakers long ago with some good ones), it only has two extra inputs and no support for internet streaming or mp3 playback etc. I’d also like to be able to use standard remote controls (Sony HATES standards), Bluetooth devices, cell phones, network control, etc. Although I’m using the Dockstar, this tutorial would generically apply to any Debian (arm or otherwise) system. Read on for the first part in my new walkthrough series entitled “Using the Dockstar as a full Home Theater Replacement”:

[![](http://66.147.244.180/~hunterda/content/images/2011/08/PICT00081-300x225.jpg "dockstar")](http://66.147.244.180/~hunterda/content/images/2011/08/PICT00081.jpg)

If you haven’t flashed your Dockstar with Linux yet, check out [Jeff Doozan](http://jeff.doozan.com/debian/)‘s script on it, and my [previous article](http://hunterdavis.com/archives/843) on the subject. I’m going to assume you’re using a base Debian system from here out.

**Basic Stereo Support and local file support**

The first step is to set up some basic audio support on your device. If your device has an audio port already, you can skip adding a usb audio device. Otherwise, plug in your usb audio-out and check that your dmesg log shows it being recognized. Every one I have tried is recognized without an issue, and I have tried dozens. I am starting to think they are all pretty standardized. Add a user to your system. I know this seems off to many embedded folks but logging in as root is a bad idea for anything on the network. Make sure your user is in the audio, cdrom, and dialout groups, as well as any admin groups you want them in. Pull in some basic prerequisites for a networked audio system with

```
apt-get install alsa alsa-utils apmd alsa-oss mpg123 libasound2-plugins git alsa-headers build-essential sudo<br></br>
nfs-kernel-server nfs-common alsa-base alsaplayer alsaplayer-text alsa-utils libasound2 vlc```

This will pull in some basic media players and the alsa architecture. If your USB audio is like mine, the levels will be off. Edit a file called /etc/asound.conf, and paste [the attached text](http://www.hunterdavis.com/plainpcmfile.txt) This will up the levels. Reboot your system, then immediately open up alsamixer and drop the levels down to 80% each. The right level will take a LOT of down arrow presses, so don’t think that it isn’t working. It’s actually just going through a larger volume level that’s being scaled down to 100% by alsamixer.

**Networked Digital Music**

If you’re like me, you’ve already got a NFS or Samba share set up on your network. While there’s nothing abnormal about setting up NFS on an embedded system versus any other, if you’re uninitiated it’s a pretty esoteric process. It basically boils down to setting up a client and a server. We’ll want to run both on this system, as we’ll want to stream in NFS shares from across the network, and we’ll want to share whatever is plugged into this over the network. To set up the client, we’ll simply add entries to our /etc/fstab in the following format.

` IP_ADDRESS_OF_SERVER:/share/sharedir     /localdir/localsharedir   nfs     defaults        0      0`

To set up the server, we’ll simply add entries to our /etc/exports in the following format.

`/srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)`

After a reboot, you should be sharing and seeing your shares from the network in your mounted locations. Make sure you’ve created directories for the mounts beforehand, or they’ll fail during automount.

**RSD Remote Audio Server**

[![](http://66.147.244.180/~hunterda/content/images/2011/08/vlcncurses1-300x223.png "vlcncurses")](http://66.147.244.180/~hunterda/content/images/2011/08/vlcncurses1.png)

VLC comes with a nice ncurses interface you can use for testing audio playback. Just execute `vlc -I ncurses` from any terminal and you’ll get the ncurses interface. Shift-B gives you a nice file browser ala DOS. At this point you should be able to SSH into your box and play audio files from the command line interface.

**VNC and Window Maker**

Command line interfaces are great, as are SSH terminals… but there’s a lot to be said for a nice graphical playlist manager. VNC is a nice lightweight way to keep one of these playlist managers open, so we’ll go ahead and install that with

` sudo apt-get install tightvncserver xorg`

From here, give yourself a vnc password by executing `vncpasswd` It’ll ask for a view-only password as well. This is optional, but pretty handy for VJ-ing and screen sharing. Now simply execute a vnc session for your user with `vncserver`.

Now on whatever box you’re going to VNC in from, install a VNC viewer. If you’re using windows or another platform which supports java, I recommend the [new beta](http://www.tightvnc.com/ssh-java-vnc-viewer.php) of tightvnc+ssh (java). It’s recent, has built-in ssh tunnelling (which improves both overhead and security), and is cross-platform. Install your client, then connect to your arm box using the password you just created. You’re going to see a plain X desktop with a single console. I first recommend installing aptitude, as it’ll make finding new packages much easier visually.

[![](http://66.147.244.180/~hunterda/content/images/2011/08/vnc1-300x243.png "vnc")](http://66.147.244.180/~hunterda/content/images/2011/08/vnc1.png)

Next I strongly recommend installing a better window manager. [Window Maker](http://windowmaker.org/) is quite good, and I haven’t featured it yet in a hack. I like to rotate through window managers to give em all some love. You can install it with `sudo apt-get install wmaker `

[![](http://66.147.244.180/~hunterda/content/images/2011/08/betterdesktop1-300x243.png "betterdesktop")](http://66.147.244.180/~hunterda/content/images/2011/08/betterdesktop1.png)

**A Side Note About Conky**

Ok so the biggest issue with the dockstar is it’s limited (128mb) memory. This isn’t such a huge deal, as many of us grew up with computers which had far less memory. It does mean we have to keep an eye on our memory usage though. For some unknown reason, I could not find conky in the debian arm repository. Gnome-system-monitor is in there and works fine, but takes up a whopping 20% of the CPU when its generating graphs. Not really acceptable. So I set out to compile [conky](http://conky.sourceforge.net/). If you like conky too, just

1. Create a directory in which to compile conky, and change into that directory
2. Init the directory with `git init`
3. Pull conky with `git clone git://git.omp.am/conky.git`
4. Change to the subdirectory conky
5. Create a directory called build, and change into that directory
6. Install the prerequisites for conky with `sudo apt-get install cmake liblua5.1 liblua5.1-dev libx11-dev cmake-gui libpthread-stubs0-dev libfreetype6-dev libxft-dev gawk ncurses-dev libncurses-* xmms2 libxdamage-dev libxext-dev `
7. You could execute the cmake pre-build with `cmake ../` , but I prefer to disable a ton of features I won’t need. Just open up cmake-gui and point it at the conky directory. Then disable almost everything. I leave math, music players, xmms2, xdamage, freetype, and the x11 options checked. Everything else I get rid of. If you want more feature, there may be additional prerequisites not listed here.
8. Change into the build directory of conky, and execute a `make`
9. Execute a `sudo make install` this will install conky into the system for user access

[![](http://66.147.244.180/~hunterda/content/images/2011/08/conkyrunning1-300x241.png "conkyrunning")](http://66.147.244.180/~hunterda/content/images/2011/08/conkyrunning1.png)

<strongheavyweight managers="" playlist=""></strongheavyweight>

Ok, since we know Xmms installs and runs, we may as well see how far we can push it. I set out to see exactly how large a playlist I can add to Audacious (a lightweight xmms2/beep-based media player) without filling up all the memory. Unfortunately Audacious segfaults. So I went about compiling [Beep](http://sourceforge.net/projects/beepmp/) from source, just so I’d have it. The following is therefore optional. This had a few prerequisites, which were taken care of with a `sudo apt-get install libgstreamer-* xorg-dev xserver-xorg-dev sqlite3 libstartup-notification* libgtkmm-2.4-dev libglade2-dev libglademm-2.4-dev libneon27-dev libnotify-dev glibmm* gamin libgamin-dev libmusicbrainz4-dev libtaglib* libsqlite3-dev  libhal-storage-dev libhal-dev<br></br>` Simply extract the Beep source file, execute the classic `./configure && make &&sudo make install` , and you’re good to go. If it fails to compile, it’s because of a reference to an old PRIVATE_ variable in gtk. Simply delete the offending line (103 in widgets/bmp_tooltips.c). You may also need to add `#include <cstdlib></cstdlib>` for any file which complains about memcpy not being defined, or `#include <cstring></cstring>` for any file which complains about strlen. After all that, and quite a bit of time for compilation and linking, everything should compile fine. For the purposes of smooth compilation you may want to [add an extra 512mb swap file](http://www.cyberciti.biz/faq/linux-add-a-swap-file-howto/).

After testing out a lot of the lightweight audio players, I was starting to thing VLC was the best option. It is actually a pretty terrific program, even on embedded arm boards. You can literally play a 480p video stream on the arm board, and stream the video over VNC at a reasonable rate. On a whim I decided to use a more heavyweight audio player “banshee”. It actually seemed to fit well into the memory profile, so I pointed it at a 40 gig music share on an nfs drive and told it to “import”. It took awhile (at least an hour, it was late and I passed out. The beauty of a 6 watt arm device is not worrying too much about the carbon offset), and at times about 200 megs of swap, but it finished. And I had a 40gig mp3 collection in a full featured audio player over the network. Not a bad start, but there’s too much processing power in our laptops and mobile devies nowadays to waste it all while an arm box does decoding. Another, (one of many) less memory and processing intensive solution is remote audio playback.

[![](http://66.147.244.180/~hunterda/content/images/2011/08/banshee2-300x242.png "banshee")](http://66.147.244.180/~hunterda/content/images/2011/08/banshee2.png)

**Compiling and Testing rSound **

[rSound ](https://github.com/Themaister/RSound)is a terrific project from Themaister which aims to be a lightweight networked sound server/client. It has support for all windows, OSX, and unix-based platforms and is built into a number of PS3 emulators. You have to compile the server from source, but it’s fairly straightforward.

1. Create a new directory for your rsound project, and init it with `git init`
2. Pull the rSound git repository with `git pull https://github.com/Themaister/RSound.git`
3. Execute a `./configure` This should say alsa and alsa headers are installed. If not, double check your apt-get from above completed and you have all headers necessary
4. Execute a `make`
5. Execute a `sudo make install`
6. Edit the following file as root `sudo vim /etc/init.d/rsd`
7. Paste in the following code, changing YOUR_IP_ADDRESS to your device’s ip address  
```
<br></br>
#!/bin/sh<br></br>
/usr/local/bin/rsd --resampler 5 --syslog --daemon<br></br>```
8. Make this file executable with `sudo chmod 755 /etc/init.d/rsd`
9. Make it run on startup with `sudo update-rc.d rsd defaults 80`
10. Reboot

At this point, RSD (the rSound daemon) has been installed on your embedded arm box. It has a built-in resampler which will resample any audio up to the maximum setting (5). Installing it on a Linux system is the same process, so I’ll describe installing in on a windows box, and using it with the media player classic client. This only uses about 15% of cpu at any given time, so is pretty efficient.

**Remote Sound with Media Player Classic**

Download the rSound for windows library files from [here](http://blackbird.usask.ca/wordpress/?p=327). Download media player classic (32-bit) from [here](http://mpc-hc.sourceforge.net/). I prefer to download the .zip file version, as you can have a local version which contains the rSound dlls on hand for easily moving between systems and virtual machines. Extract the media player classic zip you just downloaded into a folder. If you wish to use the 64-bit version of a program, you’ll need to compile a 64-bit version of the rSound windows library from source [here](http://blackbird.usask.ca/wordpress/?p=327). Next extract the contents of the rSound library zip into that same folder. Make sure there were no sub-folders created by mistake, as you’ll want all these files in the same directory.

In your windows control panel, open up the system panel. Inside the system panel, go to advanced system settings, then click on environment variables. Click “new”, and enter `RSD_SERVER` as the name field, and the IP address of your arm system as the value field. Click “new” again, and enter `RSD_LATENCY` as the name field, and `200ms` as the value field. I chose 200 as my arm box is behind 2 wireless bridges and at least two hops from all my other devices. This tends to incur some network latency, and let’s not even talk about interference. Anyway, reboot your system. When it fires back up, open media player classic and go to the options->output options menu. Select “directsound – rSound networked audio” as the output device.

[![](http://66.147.244.180/~hunterda/content/images/2011/08/rsound1-300x248.png "rsound")](http://66.147.244.180/~hunterda/content/images/2011/08/rsound1.png)

And that’s that. You can now stream sound from most every application on your PC to your arm box. And this is just the beginning. For the time being, the Sony system is still being used as an amplifier, and to switch between signals and control audio. In future articles I’ll talk about adding remote support (bluetooth, wifi, infrared, etc), multiple audio-in and audio-out options, stereo re-mixing, auto-streaming, timers, power control, amplifiers, LCD and video out, and so much more!

[![](http://66.147.244.180/~hunterda/content/images/2011/08/success1-300x194.png "success")](http://66.147.244.180/~hunterda/content/images/2011/08/success1.png)


