---
layout: post
title: Home Automation + Gmail in Ubuntu
date: '2007-12-19 16:41:21'
---


 Ok, now that we have a working home automation server setup (see article 1), let’s plug in a lamp module and have it flash when our gmail arrives. First up, plug in the light module, select your house code (‘heyu info’ will tell you your house code) and an unused x10 number on the dial.  
 Find a lamp you’d like to have flash (or turn on, or dim etc etc) and plug it into any other outlet. Turn on the lamp, you want to be sure the light is actually on before you start cursing at your x10 module. Now plug the ‘on’ light into the x10 module. Let’s try turning on the module with a heyu on A3 Where A is your house code and 3 is your module number. Voila, you should have light. a quick heyu off A3 will get us back to the off state. There are many heyu options (dimming !) to try out, but they all work in this manner. Now, let’s install gmail-notify with a sudo aptitude install gmail-notify Gmail notify is a great python script to notify you when you have gmail. We will insert an execute command into the python code (very simple) so when gmail-notify runs and we have an unread email, flash the light (or dim the light, or turn on your lava lamp, etc.)

Fire up your favorite editor (I prefer vim, but most guides prefer nano) sudo nano /usr/lib/gmail-notify/notifier.py Now head down to line 208 (it was 208 as of 9/07). You are looking for this block of code: if attrs[1]>0: print str(attrs[1])+” new messages” We will change it to: if attrs[1]>0: path = ‘/usr/bin/gmflash.sh’ os.system(path) #execute gmflash print str(attrs[1])+” new messages” What we’ve done is told gmail-notify to execute the script /usr/bin/gmflash.sh when there is new gmail. Now we’ll need to create this script with a sudo nano /usr/bin/gmflash.sh Here we’ll tell the x10 light to flash on, then off. It takes my x10 module 1 second to deactivate a light and 1 seconds to activate one. It takes my light 2 seconds to ‘warm up’ to bright. We’ll want our script to pause for at least (1 + cycle time + bulb time) seconds, so in my case that’s 4. Insert into your editor window: heyu on A3 sleep 4 heyu off A3 Save it, close it, and make it executable with: sudo chmod +x /usr/bin/gmflash.sh

That’s all there is to it. Fire up gmail-notify, put in your gmail settings, and send yourself a test email to check. If your light doesn’t flash, try executing /usr/bin/gmflash.sh. If this doesn’t work, time to re-check your setup. Fin.


