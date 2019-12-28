---
layout: post
title: A Quick (Grapher) Blast From My Past
date: '2019-12-27 08:33:24'

quickgrapher: true
---


As I was setting up a new development machine this morning, I found myself traversing through my old GitHub projects. One such project that was always close to my heart was QuickGrapher, the JavaScript graphing library Mark and I write during our start-up years.

I realized that I could easily update QuickGrapher to work within my jekyll gh-pages, and update it so the examples and embeds are working again after all these years.  In order to allow embedded graphs in my Jekyll blog posts I've added optional javascript include directives to my post template

So, that's what I ended up doing this morning.  You can see an example of an embedded graph below, and play with the tool here [Quick Grapher](http://www.hunterdavis.com/quickgrapher/)

<small>
 &lt;graph title="Our Mystery Point Graph" values="20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;" label="Mystery Points" type="point" style="width:250px;float:left;" /&gt; <br>
 &lt;graph title="Not A Mystery Anymore" values="20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;" label="Point Connecting Lines" type="line" style="width:250px;float:left;align:right;"  /&gt; <br>
    </small>
<table>
    <tr>
        <td><graph title="Our Mystery Point Graph" values="20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;" label="Mystery Points" type="point" style="width:250px;float:left;" />  </td>
        <td> <graph title="Not A Mystery Anymore" values="20,11;19,6;19,2;17,2;17,6;16,5;15,2;13,2;14,5;14,6;12,6;12,2;10,2;10,4;9,2;7,2;9,6;7,6;4,4;2,3;0,2;1,3;3,5;5,9;9,11;17,11;21,17;23,18;25,17;24,16;20,11;" label="Point Connecting Lines" type="line" style="width:250px;float:left;align:right;" /> </td>
    </tr>
</table>
