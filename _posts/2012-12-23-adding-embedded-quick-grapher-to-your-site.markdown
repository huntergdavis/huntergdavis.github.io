---
layout: post
title: Adding Embedded Quick Grapher to Your Site
date: '2012-12-23 18:30:27'
---


So you’ve seen the power of Quick Grapher and want to add it to your site? What’s the absolute fastest way to do this? Well, you can always grab the source from the GitHub repo, but if you don’t want to mess with all that, just include the files from hunterdavis.com like:  
`<br></br><br></br><br></br><br></br><br></br>`

And that’s that! As for using embedded Quick Grapher, just follow the guide below:

Here’s the Original Embedded Quick Grapher Tutorial :

**A New Kind of Graphing Tool**  
 If you’ve been using any of the betas at www.quickgrapher.com you may have found yourself wondering how it works, what libraries we use, and if the tech is available for public consumption. QuickGrapher is based on two of our pure Javascript libraries, our solver library and our graphing library. Due to the increased interest in these libraries, we’ve bundled them both together into a single javascript library you can include on your site, which allows you unprecedented graphing power in a fully client-side javascript environment. You can display unlimited graphs with scores of points and complex equations faster than you ever thought possible, and without requiring your users to download a bandwidth-intensive image or flash applet. Our graph+solve library allows you to embed a graph of arbitrary algorithmic and point complexity using a single “graph” tag, just like any other html tag. Our library is compatiblie with Chrome, Safari, Opera, IE, and even embedded browsers for your iPhone, Blackberry, and Android devices.

**Gallery**

<table><tr><td><graph equation1="3x+2y" style="height:100px; width:150px; " title="2Vars" vars1="5,9"></graph></td><td><graph equation1="2a-3b" style="align:right; height:100px; width:150px; " title="2More" vars1="9,5"></graph></td><td><graph equation1="tree-leaf" minstepmax1="1,3,33;1,5,90" style="height:100px; width:150px; float:left;position: relative; left: 0px;" vars1="4,3"></graph></td><td><graph label="awesome Points" label2="awesome Line" style="height:100px; width:150px; float:left;" title="Point+Line" type="point" type2="line" values="1,1;2,2;3,3;1,3;2,3" values2="4,4;5,5;4,6;6,6"></graph></td></tr><tr><td><graph label="awesome Points" style="height:100px; width:150px;float:left;" type="point" values="1,1;2,2;3,3;1,3;2,3;1.5,1.5;3,3.3;2.123,4.33;5,5"></graph></td><td><graph label1="awesome spots on a line" style="height:100px; width:150px;position: relative; left: 0px;" type1="line" values1="1,1;2,2;3,3;1,3;2,3"></graph></td><td><graph equation1="sin(x)" label="awesome Points" label2="awesome Line" style="height:100px; width:150px;" title="Point+Line+Eq" type="point" type2="line" values="1,1;2,2;3,3;1,3;2,3" values2="4,4;5,5;4,6;6,6"></graph></td><td><graph equation1="3+x" equation2="sin(f)" minstepmax1="1,5,50" style="height:100px; width:150px;" title="Multi Eqs" vars1="3" vars2="5"></graph></td></tr></table>**Seriously Easy**  
 Ok, so you’re writing a post in your blog and you want to display your data on a graph. Maybe you’re a huge corporation with thousands of employees, maybe you’re an election enthusiast who wants to show some key demographic, or maybe you’re just writing in your personal WordPress blog. You don’t pay for application hosting, and even if you did you don’t know or don’t have the time to install a server process to generate graphs. Why should it be so complicated? Why can’t you just do it with a single html tag?  
 Now you can. Graph+Solve allows you to instantly and easily insert graphs anywhere into your site. Fully stylable via CSS and HTML5 compliant, Graph+Solve allows any level of user from novice to web designer the power to visually display your data.

**Example 1**  
 Say you’re writing a blog post about trigonometry. Maybe you’re an engineer, maybe you’re a student, maybe you just like math. You’re explaining sin and cos waves, and you’d like to show their periodicity. You could use traditional methods (screenshots of math utilities, excel sheets, etc), or you could have it done in 5 second with Graph+Solve library. Graph+Solve allows you to graph sine, cosine, and many more functions in a single tag. The following tag is all that is required to generate a graph of cosine and sine.  
<small><graph equation1=”sin(x)” equation2=”cos(y)” /></small>  
<graph equation1="sin(x)" equation2="cos(y)" minstepmax1="0,.01,30" minstepmax2="0,.01,30" title="Example Sine and Cosine Graph"></graph>

**Versatile Options**  
 Graph+Solve supports a wide range of options and CSS styles. Simply by setting the correct attributes one may use Graph+Solve to instantly create cross-platform maps and terrain graphs. Dimensions, colors, backgrounds, grids, legends and so much more can be easily set using standard html and css tag attributes. Perhaps you’re not interested in a background grid, XY coordinates, multiple equations, legends, etc. Graph+Solve allows you to set exactly the options you care about, and can auto-generate any necessary attributes not specified by the user.

**Example 2**  
 Say you’re writing a blog post about military tactics. Maybe you’re a soldier, maybe you’re a history buff, maybe you just like tactics. You’d like to show the positions of soldiers on a battlefield grid, and you don’t want to have to continually edit maps by hand. With Graph+Solve, you can instantly share your strategies with no image editing. The following tag is all that is needed to generate the following graph.  
<small><graph values=”10,10;30,11;40,12;20,8;50,7;60,15;70,5;21,10;33,12;44,24;” label=”confederate soldiers” type=”point” values2=”3,20;10,20;15,23;20,25;33,28;30,22;40,18;55,22;70,18″ type2=”point” label2=”union soliders” background=”http://www.hunterdavis.com/discursivelabs/images/3lakes.png” title=”Battle of The Three Lakes” style=”height:400px; width:400px;”/></small>

<graph background="http://www.hunterdavis.com/discursivelabs/images/3lakes.png" label="confederate soldiers" label2="union soliders" style="height:400px; width:400px;" title="Battle of The Three Lakes" type="point" type2="point" values="10,10;30,11;40,12;20,8;50,7;60,15;70,5;21,10;33,12;44,24;" values2="3,20;10,20;15,23;20,25;33,28;30,22;40,18;55,22;70,18"></graph>

**Serious Bandwidth Reduction**  
 Our pure clientside Javascript graph+solve library in its entirety weighs in at 40 kilobytes. That’s roughly equivalent to a very small, highly compressed jpeg from a camera phone circa 2005. With this one 40 kilobyte library (less than what adsense loads), you can replace every single graph or equation plot on your website. If you’re running a graph heavy website this can be a reduction of many thousands of times. What’s more, our graph+solve library is used by many websites, and may be cached by the users browser. If a user is coming in from another graph+solve enabled site, they download nothing. This is a serious reduction in page load times for all browsers, but especially for those on 3g networks or hampered by a slow connection.

**Example 3**  
 Let’s say you’re writing an article on statistics, and you’d like to show a random distribution. A really large random distribution would be best, as the more data the better visual. You could generate a million points using a programming language, then feed it into an existing tool such as excel or matlab. Then, using the same tool you could plot another guide line along the median to show where the mean distribution should be. That is, if you can figure out how to add a line to a plot graph. Or, you could do it in ten seconds in a single line of html using the Graph+Solve library. The following line of html generates a hundred random points and plots a line across the median of the graph. Note how you are able to style the graph using standard CSS tags, and simultaneously display line graphs, point graphs, and equation graphs using the same tag.  
<small> <graph equation1=”rand(x)” minstepmax1=”0,10,1000″ title=”Mean Random Distrubtion” values1=”1,.5;100,.5″ label2=”Median Line” type2=”line”/></small>  
  
<graph equation1="rand(x)" label2="Median Line" minstepmax1="0,10,1000" style="height:200px; width:600px;" title="Mean Random Distrubtion" type2="line" values1="1,.5;100,.5"></graph>

**Serious Efficiency**  
 Just because graph+solve is executed by a client’s browser, don’t expect it to be slow. Graph+solve requires no external plugin of any kind, Flash or otherwise. It speedily graphs thousands of points in a few moments on a Pentium 3 class computer, quite ancient now in 2011. Graphs of complex equations with thousands of data points and complex algebraic functions load faster than a single equivalent image on mobile 3g devices.

**Example 4**  
 So you’re looking to plot a large number of data points in a graph, and you want it to be easy? Good luck! Unless you’re using our Graph+Solve library, you are in for a headache. Find the data source, paste it into your graph generator, save it as an image, upload that image to your web host and align for your page. Need to update a single data point? You’ve got to do it over. Want to change to a plot graph from a line graph? You’ve got to do it over. What to update the graph styling, size, etc? You’ve got to do it over. Want it to look good on all devices? Well you’d better make a new image size for each device! Starting to get frustrated? Do it with a single line of QuickGrapher, update it whenver you like in moments, and never think of it again. The following two lines of html generate line graphs using points taken from an graphing calculator games worksheet. As you can see, switching between a point and a line graph is as simple as selecting “point” or “line”  
<small>  
 <graph title=”Our Mystery Point Graph” values=”20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;” label=”Mystery Points” type=”point” style=”width:250px;float:left;” />   
 <graph title=”Not A Mystery Anymore” values=”20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;” label=”Point Connecting Lines” type=”line” style=”width:250px;float:left;align:right;” />   
</small>

<table><tr><td><graph label="Mystery Points" style="width:250px;float:left;" title="Our Mystery Point Graph" type="point" values="20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;"></graph></td><td><graph label="Point Connecting Lines" style="width:250px;float:left;align:right;" title="Not A Mystery Anymore" type="line" values="20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;"></graph></td></tr></table>
