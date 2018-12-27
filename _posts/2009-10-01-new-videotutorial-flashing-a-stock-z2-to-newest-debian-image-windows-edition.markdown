---
layout: post
title: New Video/Tutorial - Flashing a Stock Z2 to Newest Debian Image (Windows edition)
date: '2009-10-01 22:19:00'
---


So you’ve only got a windows machine handy, and you want to flash your Z2 to the newest debian (apt-get! no more cross-compiling!) image with wireless? This video is for you. Full Text after the jump.

<object height="344" width="425"><param name="movie" value="http://www.youtube.com/v/txUFH7uPh7A&hl=en&fs=1"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed allowfullscreen="true" allowscriptaccess="always" height="344" src="http://www.youtube.com/v/txUFH7uPh7A&hl=en&fs=1" type="application/x-shockwave-flash" width="425"></embed></object>

You’ll need

1. Either Aliosa27’s [1gb](http://openzipit.svn.sourceforge.net/viewvc/openzipit/debian/debianZ2-1G-image.rar) or [2gb](http://openzipit.svn.sourceforge.net/viewvc/openzipit/debianZ2-diskimage-2G.rar?revision=36&pathrev=36) disk image posted to the SF page.
2. [Aliosa27’s latest oe userland image](http://aliosa27.net/projects/zipit2/zipit2-audio+x+mouse.gz)
3. [phsydiskwrite ](http://m0n0.ch/wall/physdiskwrite.php) (I recommend the GUI version for ease of use)
4. The [autoflasher script](http://sourceforge.net/projects/openzipit/files/autoflasher/r2/AutoFlasher-r2.zip/download)
5. (if windows can’t see the fat partition) [Windows ext2 filesystem driver](http://sourceforge.net/projects/ext2fsd/files/Ext2fsd/0.48/Ext2Fsd-0.48.exe/download)

Ready?

1. First, flash the zipit. Extract the autoflasher bundle to a fat16 formatted memory card
2. Open Aliosa27’s wireless+x+audio.tar.gz file, and copy out the /boot/linux-2.6.29 file to your memory card
3. Rename this file kernel.bin
4. Boot the zipit with the SD card inserted. If this does not start the linux flash, go to settings->reset to default and it should soft-reset
5. Some SD cards are reported to not work, or not always be seen by the zipit. Try both with and without the power cable plugged in
6. The z2 will boot linux and copy the wifi firmware to the sd card before flashing linux to the Z2
7. Copy off the 2 wireless firmware files gspsi.bin and gpspsi_helper.bin to a folder, you will copy these back to the memory card after we write the image
8. IMPORTANT — rename helper_gspi.bin to be gspi8686_hlp.bin or it will not load later!
9. Extract the 1/2gb image to a folder
10. Extract phsydiskwrite to a folder
11. Insert your microSD card into the computer (adapter, usb stick, etc)
12. Run phsygui.exe from within the folder you extracted psydiskwrite to (requires .net framework)
13. right-click on the drive letter for your SD card, select the first menu item, and then select the 1/2gb image you extracted earlier (.img)
14. After it writes, safely remove the disk then plug it back in. if windows can see the fat partition copy the firmware files to it
15. If windows cannot see this fat partition, congratulations! Windows sucks! Dowload the ext2 filesystem driver, run it, then copy the firmware files over to /lib/firmware/notlibertas/ (yes notlibertas, the fat filesystem is mounted as /lib/firmware/libertas so you can’t use that)
16. Insert the sd card into the Z2, and boot. Login as root, password debian. Congrats! You’ve got debian on the zipit!
17. If windows couldn’t see your fat32 partition, copy the firmware files from /lib/firmware/notlibertas to /lib/firmware/libertas. You may need to run fsck if linux can’t see the files.
18. Reboot, and you should have wireless device when you type iwconfig. Configure the wireless settings, and you’re ready. I like to `apt-get install ssh` right away, as that’s what I use most of all. Ahhhhhhh! Doesn’t it feel refreshing to install new software to the Z2 without cross-compiling?
19. Install ssh/sshd with `apt-get install ssh` You’ll also have to force-move the real start-stop-daemon back in place with `mv /sbin/start-stop-daemon.REAL /sbin/start-stop-daemon`


