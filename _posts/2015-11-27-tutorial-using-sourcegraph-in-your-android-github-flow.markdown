---
layout: post
title: "(Tutorial) Using Sourcegraph In Your Android GitHub Flow"
image: http://www.hunterdavis.com/content/images/2015/11/sourcegraph.png
date: '2015-11-27 00:21:27'
tags:
- android
- git
- github
- source-code
---


As I was reading my daily news articles the other day, I came upon a fascinating piece of [oddly-licensed](https://fair.io/) software: [Sourcegraph](https://src.sourcegraph.com/sourcegraph). It’s a Git server with much the same features as GitHub, only with the added “code intelligence” feature. Code intelligence is a parsing engine that allows for the same smart-lookup (and quick-lookup) features you’d find in an IDE, only available in your browser while viewing the repository.

[![sourcegraph](http://www.hunterdavis.com/content/images/2015/11/sourcegraph.png)](http://www.hunterdavis.com/content/images/2015/11/sourcegraph.png)

As it’s free for personal use, I thought I’d give it a spin as a local code intelligence server for use in my personal network. It supports Java and Gradle, so my first project to add was an Android game collection I wrote: [Can’t Stop The Rock](https://github.com/huntergdavis/cantstoptherock).

The first thing to note is that the code intelligence feature needs to be able to correctly execute your gradle scripts. That means upgrading your local gradle binaries to 1.7 or above if you’re using any jcenter libraries. Head on over to [gradle.org](http://gradle.org/) for that, then start the [Sourcegraph install script](https://src.sourcegraph.com/sourcegraph/.docs/install/) for your system.

After installation, you’ll need to add your server’s IP address to the config file. In my case, I only wanted it available while I was remote’d into my development machine, so I chose 127.0.0.1 (localhost.) My config file is therefore:

```
[serve]<br></br>
AppURL = http://127.0.0.1<br></br>
HTTPAddr = :80<br></br>```

Now that your server is up and running, head to the IP address you entered above and set up your first user. You can then create a repository using the command line, in my case:

` src --endpoint=http://127.0.0.1 repo create CantStopTheRock`

From there, it’s as simple as adding the sourcegraph server above as a remote host in your git project, like so:

` git remote add sourcegraph http://127.0.0.1/CantStopTheRock<br></br>`

Now simply push a branch up to your new “sourcegraph” host:

` git push -u sourcegraph master`

And you’re in business! Now you can browse to the IP address above in your browser and see your source repository. As I said before, it’s VERY much like GitHub, but I do find myself quite impressed with the source intelligence feature. One of the great things about the distributed nature of git is that you can push your projects around to various servers without any concern, and the idea that one could have many micro-services each reading and executing from git repositories is quite interesting indeed!


