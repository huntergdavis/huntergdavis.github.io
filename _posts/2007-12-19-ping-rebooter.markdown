---
layout: post
title: Ping Rebooter
date: '2007-12-19 16:29:14'
---


Ping Rebooter is a simple but useful application, basically it pings a website at some time interval if the website does not return, it uses wget to execute your cable/dsl modem’s reset string. The default reset string is: http://192.168.100.1/gscan.cgi?freq=331000000 This works for my linksys cable modem and has been tested on a few others. **I find this useful**

1. if your modem stops working due to power outage
2. if your modem gets disconnected due to torrent use, file sharing, etc.

This is simply a open source linux remake of the windows version I released to a few friends 2 years ago. Since then i’ve decided to completely get rid of all MS software, so it was time for a ground up re-write. This version has not yet been tested on many systems, but it’s fairly simple code so not much to worry about. Download it [Here](file:///home/hunter/website/public_html/pingreboot.tar.gz), it should work on posix type systems (linux,unix,macos) and cygwin, it requires wget and ping to be installed.


