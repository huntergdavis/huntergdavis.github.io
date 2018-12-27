---
layout: post
title: NDA Lifted!  (OpenGL Cable Box Fan.TV Featuring Rhapsody Release Announcement!)
image: http://www.hunterdavis.com/content/images/2014/04/Rhapsody-Fan-TV.jpg
date: '2014-04-22 23:23:36'
---


Eagle-eyed readers may recall about a year ago I mentioned that I was working on an exciting futuristic cable box with a gorgeous API backed by OpenGL. Imagine my excitement when I saw the [official](https://www.fan.tv/tv) [product](http://news.rhapsody.com/2014/04/22/rhapsody-available-on-fan-tv-for-time-warner-cable-at-launch/) [announcement](http://www.ubergizmo.com/2014/04/rhapsody-is-exclusive-music-streaming-service-for-fan-tv/?utm_source=mainrss) begin to hit the [newsfeeds](http://www.cnet.com/news/fan-tv-gets-time-warner-cable-support-and-q2-release-date/)!

[![Rhapsody-Fan-TV](http://www.hunterdavis.com/content/images/2014/04/Rhapsody-Fan-TV-300x190.jpg)](http://www.hunterdavis.com/content/images/2014/04/Rhapsody-Fan-TV.jpg)

Full Disclosure: I work at Rhapsody and was the sole developer of the Rhapsody app for Fan.TV. It’s one of the many cool things I’ve gotten to do at Rhapsody. ([one](http://www.hunterdavis.com/?s=rhapsody) [of](http://www.hunterdavis.com/2013/10/27/rhapsody-for-android-gets-an-equalizer/) [many](http://www.hunterdavis.com/2014/03/31/rhapsody-and-napster-add-chromecast-support/).)

Last summer the trial of the (now known as Fan.TV) box featuring Rhapsody was a resounding success. I worked my butt off getting this gorgeous app out the door, but I couldn’t tell anyone! Fast forward to today, when the announcement has been made, the NDA has been lifted and I can officially talk about my work with Fan.TV.

When I first set out to write Rhapsody for Fan.TV a little over a year ago I didn’t know what to expect. All I knew is that they wanted Rhapsody in their summer trial, and they needed an architect to implement a radical new vision of Rhapsody in a short amount of time. I flew down to their office to meet with their CTO and technical team and was immediately impressed by their technology. The Fan box runs at a rock solid 60 fps while displaying live cable feeds, streaming video, dynamic overlays, and a fully animated set of contextual windows. Everything is hardware accelerated and running on OpenGL.

[![fan-tv-main3](http://www.hunterdavis.com/content/images/2014/04/fan-tv-main3-300x120.jpeg)](http://www.hunterdavis.com/content/images/2014/04/fan-tv-main3.jpeg)

When given the option between implementing a standard HTML 5 experience vs a native one, I almost always go native. It’s not that you can’t do great things with HTML views (just look at the work we did on Rhapsody+Chromecast), but I try to get down as close to the metal as possible. The same holds true for the Rhapsody on Fan.TV experience. Working with an innovative OpenGL-backed graphics and windowing API the talented Fan.TV developers created, the features flowed quickly.

Having each button, widget, text item, background, and image you see within the Rhapsody for Fan.TV app backed by OpenGL made the experience much like developing with a robust game engine. Everything is animated. Anything can be transformed, faded, made transparent dynamically. You can quick-scroll through thousands of artist images in seconds. The experience is optimized for beauty. Browse to an artist page and the background morphs into artist artwork as their discography comes into view. You can jump between their albums, top tracks, and related artists quickly. In fact, “quickly” is how everything responds in this implementation. This is the snappiest, quickest, and most beautiful way to interact with your music collection on your television, no contest.

[![fan-tv-with-hand](http://www.hunterdavis.com/content/images/2014/04/fan-tv-with-hand-300x300.jpg)](http://www.hunterdavis.com/content/images/2014/04/fan-tv-with-hand.jpg)

Everything has been designed to integrate with the innovative Fan.TV remote and support the “peek” browsing paradigm they’ve implemented (to great effect.) I’ve crafted an authentic Rhapsody experience that should both surprise and delight audiophiles who are used to the watered-down weak-sauce set-top box experiences our competitors have been crapping out for years. Get ready to rock.

Much thanks to my tireless QA engineer Ed who once again kept me on my toes throughout the implementation.


