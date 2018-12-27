---
layout: post
title: Fun Pro-Tip - ArmFP + Debian Unstable + X11 + Sound = Actually Usable Linux
  on Android
date: '2012-05-21 01:50:22'
---


Here’s a quick pro-tip for a lazy Sunday. Want to run an obscure Linux app on your rooted android tablet? Maybe you want to do some Wireshark Snooping, run a Linux game with sound, or download a set of Linux images at maximum speed? With the convergence of a few awesome technologies, we can now install and run pretty much any Linux application or environment on your Android device. Follow the steps below or check out some of the example photos of apps running on my Dell Streak 7.

[![](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520183639702-300x225.jpg "CameraZOOM-20120520183639702")](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520183639702.jpg)

1. Install Linux in a chrooted environment, you can use [Install Linux](https://play.google.com/store/apps/details?id=com.galoula.LinuxInstall) from the app store to save time.
2. (For first-timers, open setup under the ‘menu’ in ‘Install Linux’, allow writing to root filesystem and set your loop device size and you should be good to go)
3. For more advanced users, choose ‘Armhp’ for the hard floating point speed improvements and Debian testing for the additional package support. There will be some broken packages as a result from both, but the performance increase is worth it.
4. Install [Xserver ](https://play.google.com/store/apps/details?id=au.com.darkside.XServer&)(for graphical apps), or you can use a [VNC client](https://play.google.com/store/apps/details?id=android.androidVNC) if you wish.
5. Install an [SSH client](https://play.google.com/store/apps/details?id=org.connectbot) to connect to your installation
6. Run the ‘X Server’ application
7. Connect to localhost via terminal (select ‘local’ in connectbot), run ‘linuxchroot’. This will give you a root console on your local Linux installation if you like.
8. Switch back to your terminal and set your display variable with `export DISPLAY=127.0.0.1:0.0`
9. Still in the terminal, install xterminal with `apt-get install xterm`. This will install a bunch of X prerequisites as well.
10. Fire up an X terminal for your X Server app with `xterm &`
11. The X terminal process will continue to run in the background, so switch on over to your ‘X Server’ application and you should see your XTerm!
12. From here the sky’s the limit. You can install a window manager, try out expiramental packages, play games with sound, install SSH and FTP servers, etc.

Let’s say there’s an extremely rare Linux distribution from Russia that you can only download from an encrypted private torrent tracker. These things happen, but your android bittorrent application may not support protocol encryption. This is easy to do with your new Linux install.

[![](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520170429856-300x225.jpg "CameraZOOM-20120520170429856")](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520170429856.jpg)

1. Open up a console either graphical or text as describe above.
2. Install your client of choice (deluge, say) with `apt-get install deluge`
3. Fire it on up with `deluge &`
4. Add the Torrent
5. Voila! Even with the crappy screens on most Android tablets it’s pretty useful. (check out my 800×480 Streak downloading an Ubuntu torrent)
6. For others with limited screen space, transmission-daemon is good as you can interface with it through Android’s local browser.

<table><tr><td>[![](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520160732671-150x150.jpg "CameraZOOM-20120520160732671")](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520160732671.jpg)</td><td>[![](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520164950292-300x225.jpg "CameraZOOM-20120520164950292")](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520164950292.jpg)</td><td>[![](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520174440850-150x150.jpg "CameraZOOM-20120520174440850")](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520174440850.jpg)</td></tr><tr><td>[![](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520174549905-150x150.jpg "CameraZOOM-20120520174549905")](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520174549905.jpg)</td><td>[![](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520180937970-150x150.jpg "CameraZOOM-20120520180937970")](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520180937970.jpg)</td><td>[![](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520181213148-150x150.jpg "CameraZOOM-20120520181213148")](http://www.hunterdavis.com/content/images/2012/05/CameraZOOM-20120520181213148.jpg)</td></tr></table>
