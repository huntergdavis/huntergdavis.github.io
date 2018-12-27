---
layout: post
title: 'Tutorial: Spruce Up Your GitHub Readme with a Current Source Tree Visualization'
date: '2012-12-24 02:22:06'
---


As programmers, we’re almost universally guilty of it: Boring Readme.md files that nobody wants to read. Why then, shouldn’t we spice up our Readme.md files with some pizzazz? A source tree visualization is easy to add to a Readme.md using GitHub markup, and there’s an open source project which makes the visualization of the tree itself a breeze. While it never found a market as a product, [Source Tree Visualizer](https://github.com/huntergdavis/Source-Tree-Visualizer) (STV) has found a new life since being open sourced last spring. Below, I’ll show you how to add STV to your build process and display the most current version in your README.md file.

Here’s what the Readme.md for “[The Grind](https://github.com/huntergdavis/The_Grind)” looks like:

[![thegrindreadme](http://www.hunterdavis.com/content/images/2012/12/thegrindreadme-300x251.png)](http://www.hunterdavis.com/content/images/2012/12/thegrindreadme.png)

While you read through the tutorial below, I’ll be working on sloooowly converting my ~90 GitHub projects’ README files over to this method as well.

And here’s a graph of a dinosaur, my favorite QuickGrapher promotional graph:

<graph label="Point Connecting Lines" style="width:250px;align:right;" title="Raaawr" type="line" values="20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;"></graph>

I’ll be walking through the basic Debian/Mint/Ubuntu installation and configuration. You *should* be able to compile and run on Windows/OSX, but I can’t vouch for that lately. The steps would be the same.

1. Install your pre-requisites with a `sudo apt-get install git build-essential automake libboost1.42-dev libmagick++-dev libcurl4-openssl-dev libcurl4-gnutls-dev`
2. Check out STV from github with a `git clone https://github.com/huntergdavis/Source-Tree-Visualizer`
3. Inside Source-Tree-Visualizer, initiate a compile with ` make `. If you are having trouble compiling it on your system post back in the comments and I can post up a VirtualBox development image that’s pre-baked and ready to go.
4. Now that you have STV compiled, execute a first interactive run over your repository with `./bin/simple_tree -i`. This will execute an interactive shell which guides you through a tree visualization.
5. If you want to add this to your build process, simply add the direct command for a git project with `./bin/simple_tree -g /path/to/build/tree` Those not using git are still covered, STV supports tree generation from many types of version control.
Here’s what the STV repository itself looks like today:  
[![source_tree_vis](http://www.hunterdavis.com/content/images/2012/12/source_tree_vis-300x300.jpg)](http://www.hunterdavis.com/content/images/2012/12/source_tree_vis.jpg)

7. Now make sure you commit that file to your repository somewhere, and browse to it on GitHub. Click on the ‘raw’ icon to get the raw link to the file.
8. Put the raw link to the file into the following code in your Readme.md file  
`![ScreenShot](https://raw.github.com/yourusername/your/raw/file/location/filename.jpg)`

And Voila! When a user comes to your GitHub page, they’ll be greeted with a visual indicator of the health and layout of your project. And it’s snazzy! Best of all, the absolute location of the file never changes, so your build process can simply write to the same image every build and your Readme.md becomes much more dynamic.

[![nicerReadme](http://www.hunterdavis.com/content/images/2012/12/nicerReadme-300x257.png)](http://www.hunterdavis.com/content/images/2012/12/nicerReadme.png)


