---
layout: post
title: wireless+x image for zipit z2
date: '2009-08-21 16:43:51'
---


As requested [here it is](http://www.hunterdavis.com/wirelessplusx.rar), for legal reasons you’ll still need to add your own wireless as described [here](http://sourceforge.net/apps/mediawiki/openzipit/index.php?title=Getting_Started_with_Open_Embedded_and_the_Z2#WIFI_firmware). For those interested in building it themselves,

1. bitbake busybox
2. open your /zipit2/recipes/wireless+x/wirleess+x.bb and remove opentyrian (why is this in there??)
3. bitbake wireless+x


