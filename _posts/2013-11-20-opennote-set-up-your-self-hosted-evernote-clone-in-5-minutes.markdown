---
layout: post
title: 'OpenNote: Set Up Your Self-Hosted Evernote Clone In 5 Minutes'
image: http://www.hunterdavis.com/content/images/2013/11/Screenshot-from-2013-11-19-171136.png
date: '2013-11-20 01:31:33'
---


I’m still slowly replacing all of my 3rd-party services with open-source alternatives. Lately, I’ve been using Kaiten ([K-9](https://code.google.com/p/k9mail/) derivative) for email, [RoundCube](http://roundcube.net/) and [Thunderbird](http://www.mozilla.org/en-US/thunderbird/) for email, [WordPress](http://wordpress.org/download/source/) for blogging, and Evernote for notes. Until this week, Evernote had been the one glaring exception in my “host on your own server” cloud services list. That job is now being done by an open source project called [OpenNote](https://github.com/FoxUSA/OpenNote).

[![Screenshot from 2013-11-19 17:11:36](http://www.hunterdavis.com/content/images/2013/11/Screenshot-from-2013-11-19-171136-300x168.png)](http://www.hunterdavis.com/content/images/2013/11/Screenshot-from-2013-11-19-171136.png)

It’s actually dead simple to set up on your web server using CPanel or other host-provided tools, and if you’re comfortable on the command line you can probably do it in under a minute.

1. Create a mysql Database
2. Create a mysql User
3. Give the mysql User r/w access to the Database you just created
4. Clone the [OpenNote GitHub repository](https://github.com/FoxUSA/OpenNote)
5. Edit a config file, entering the username/pw/database name combo you just created

And you’re done. Voila. Works great in Android (2.3+ maybe?) stock browser or your browser of choice.  
 If you’re hosting on your own server I recommend you create your user then disable account creation and enable force-ssl. It replicates the Google Notes/Evernote experience and runs solely on your PHP enabled webserver. That’s good times, and you know the big G won’t be pulling the plug on it here in 2 years when they decide it’s not profitable.

[![Screenshot from 2013-11-19 17:09:45](http://www.hunterdavis.com/content/images/2013/11/Screenshot-from-2013-11-19-170945-300x168.png)](http://www.hunterdavis.com/content/images/2013/11/Screenshot-from-2013-11-19-170945.png)


