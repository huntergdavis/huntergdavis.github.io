---
layout: post
title: I hacked the new Atari Mini Pong Jr. Console
date: '2020-12-20 08:33:24'
---
 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/dec/recentfiles.jpg" width="200">

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/dec/Screenshot_1970-01-02-08-46-26.png" width="200">


This story starts, as most of my hardware hacking stories do: a stupid impulse purchase.  In this case, it's the Atari mini pong Jr.  I'm pretty sure (judging from stock levels) I'm the only one dumb enough to pick this one up.  So, I set about to hack the thing.  It's almost disappointing, as this isn't as much of a 'hack' as it is 'this system is wide open.'  Here's what I've been able to determine/do with zero hardware modification. (TLDR; Everything.  Install and run apps, usb devices, adb shell, etc)


I started by simply connecting to my linux laptop via usb-micro.  Adb devices showed an open debug device, and adb connect worked.  From there, you can install anything, launch packages or apps, etc.  Usb peripherals work, and from the looks of it usb ethernet would also allow for internet connectivity and wireless adb.  Given the under-powered nature of the device (see geekbench below) I don't find it's particular worthwhile to install retroarch etc, but if you're looking to get some more mileage out of your device it'll be easy peasy. 

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/dec/Screenshot_1970-01-02-08-46-02.png" width="200">

Random thoughts / info -> 

1.  This is simply an android device without a touchscreen.  Wide open, with adb enabled. 
2.  You can hit ctrl-t for a framecounter
3.  You can hit print-screen for a screenshot
4.  Alt-tab works.
5.  Adb shell lists the following default installed packages (plus I installed geekbench), there's some interesting stuff in there (minipongautotest) leading me to believe this device was rushed out. 
6.  There are 2 gigs free on the device.
7.  The pong app is a unity app, and it struggles to maintain a solid 60fps.
8.  Apps installed will show up on the default launcher (it's not parsing config files etc, it's a standard android launcher, see screenshot)
9.  Mali 400 gpu, I installed geekbench, Arm sun8i at 1.34ghz, half a gig of ram
10.  This is definitely not worth 130$, a bit of a cash grab if you ask me.
11.  The addition of an 18650 battery (pictured below) allows charging and playback from battery.

<img src="https://github.com/huntergdavis/huntergdavis.github.io/raw/master/content/images/2020/dec/18650.jpg" width="200"> 

Package list ->

- root@astar-y3:/ # pm list packages -f
- package:/system/app/PrintSpooler.apk=com.android.printspooler
- package:/system/priv-app/DefaultContainerService.apk=com.android.defcontainer
- package:/system/framework/framework-res.apk=android
- package:/system/priv-app/Settings.apk=com.android.settings
- package:/system/priv-app/ContactsProvider.apk=com.android.providers.contacts
- package:/data/app/com.UNIS.MiniPongAutoTest-1.apk=com.UNIS.MiniPongAutoTest
- package:/system/priv-app/ExternalStorageProvider.apk=com.android.externalstorage
- package:/system/app/PartnerBookmarksProvider.apk=com.android.providers.partnerbookmarks
- package:/system/app/LatinIME.apk=com.android.inputmethod.latin
- package:/system/priv-app/TeleService.apk=com.android.phone
- package:/system/app/BasicDreams.apk=com.android.dreams.basic
- package:/system/app/WisdomTest.apk=com.wisdom.WisdomTest
- package:/system/priv-app/ProxyHandler.apk=com.android.proxyhandler
- package:/system/app/HTMLViewer.apk=com.android.htmlviewer
- package:/system/app/AllApp.apk=com.rk_itvui.allapp
- package:/system/priv-app/SystemUI.apk=com.android.systemui
- package:/system/app/LiveWallpapersPicker.apk=com.android.wallpaper.livepicker
- package:/system/app/SpeechRecorder.apk=com.android.speechrecorder
- package:/system/app/KeyChain.apk=com.android.keychain
- package:/system/priv-app/InputDevices.apk=com.android.inputdevices
- package:/system/app/PackageInstaller_WD.apk=com.android.packageinstaller
- package:/system/priv-app/hc_sy.apk=com.hc.rotation
- package:/system/app/TelephonyProvider.apk=com.android.providers.telephony
- package:/system/app/LiveWallpapers.apk=com.android.wallpaper
- package:/system/app/FileExplore.apk=com.softwinner.explore
- package:/system/priv-app/PicoTts.apk=com.svox.pico
- package:/system/priv-app/OneTimeInitializer.apk=com.android.onetimeinitializer
- package:/system/app/DownloadProviderUi.apk=com.android.providers.downloads.ui
- package:/system/app/UserDictionaryProvider.apk=com.android.providers.userdictionary
- package:/system/app/Update.apk=com.softwinner.update
- package:/system/app/DocumentsUI.apk=com.android.documentsui
- package:/system/priv-app/SharedStorageBackup.apk=com.android.sharedstoragebackup
- package:/system/priv-app/FusedLocation.apk=com.android.location.fused
- package:/system/priv-app/BackupRestoreConfirmation.apk=com.android.backupconfirm
- package:/system/priv-app/SettingsProvider.apk=com.android.providers.settings
- package:/system/priv-app/VpnDialogs.apk=com.android.vpndialogs
- package:/system/priv-app/Keyguard.apk=com.android.keyguard
- package:/system/app/Provision.apk=com.android.provision
- package:/data/app/com.UNIS.MiniPong-1.apk=com.UNIS.MiniPong
- package:/system/app/PacProcessor.apk=com.android.pacprocessor
- package:/system/priv-app/MediaProvider.apk=com.android.providers.media
- package:/system/priv-app/Shell.apk=com.android.shell
- package:/system/app/CertInstaller.apk=com.android.certinstaller
- package:/system/priv-app/DownloadProvider.apk=com.android.providers.downloads


 
