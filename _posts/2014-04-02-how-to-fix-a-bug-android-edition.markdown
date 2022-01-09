---
layout: post
title: How To Fix A Bug (Android Edition)
image: http://www.hunterdavis.com/content/images/2014/04/page0.png
date: '2014-04-02 02:53:09'
---


For all those who need to know, here it is. Have you ever wondered what it is we programmers do when we say we’re “fixing bugs?” Here’s a helpful guide for those who may find themselves in a “oh snap I need to fix a bug” situation.


![ So you have a bug.. Android Edition](http://www.hunterdavis.com/content/images/2014/04/page0.png)

So you have a bug.. Android Edition

  
![Do you want to fix it? If no, you’re done!](http://www.hunterdavis.com/content/images/2014/04/page1.png)]

Do you want to fix it? If no, you’re done!   

![Quick, save a log! Plug in your device and execute ‘adb logcat > log.txt’ , reproduce 2 times if possible, then hit control-c to stop recording.](http://www.hunterdavis.com/content/images/2014/04/page2.png)

Quick, save a log! Plug in your device and execute ‘adb logcat > log.txt’ , reproduce 2 times if possible, then hit control-c to stop recording.   

![No Logs? No Repro? 1. Check Google Play Dev console for a crash log. 2. Check crittercism/crashlytics/etc for a crash log (and sign up if you haven’t). 3. email-your users and as for logs! 4. Check stack exchange/Google for similar situations  ](http://www.hunterdavis.com/content/images/2014/04/page3.png)

No Logs? No Repro? 1. Check Google Play Dev console for a crash log. 2. Check crittercism/crashlytics/etc for a crash log (and sign up if you haven’t). 3. email-your users and as for logs! 4. Check stack exchange/Google for similar situations   

![OK, so you have a log.. now what? 1. Filter for error level. 2. Look for output (you’re looking for exceptions). These exceptions are your problems!  ](http://www.hunterdavis.com/content/images/2014/04/page4.png)

OK, so you have a log.. now what? 1. Filter for error level. 2. Look for output (you’re looking for exceptions). These exceptions are your problems!   

![No Errors? 1. Up your log filter to warning, then debug, then info. Use ‘cat log.txt | grep “e/”‘ 2. Repeat until you find an error.](http://www.hunterdavis.com/content/images/2014/04/page5.png)

No Errors? 1. Up your log filter to warning, then debug, then info. Use ‘cat log.txt | grep “e/”‘ 2. Repeat until you find an error.   

![So you have an ERROR! That’s a good thing! Now you have a Roadmap!](http://www.hunterdavis.com/content/images/2014/04/page6.png)]

So you have an ERROR! That’s a good thing! Now you have a Roadmap!   

![Anatomy of a message. “Log Level” / “Process Name” : “error” caused by “reason”: “function” at “filename”:”linenumber”. This is a stacktrace! This is great!](http://www.hunterdavis.com/content/images/2014/04/page7.png)

Anatomy of a message. “Log Level” / “Process Name” : “error” caused by “reason”: “function” at “filename”:”linenumber”. This is a stacktrace! This is great!   

![So you have a STACKTRACE. Now what? 1. Can you READ IT? Does your function names look like “a.a.a.b” and “c.a.b.b”? This means it is obfuscated! Your build server or proguard mapping file will allow you to make this READABLE. ](http://www.hunterdavis.com/content/images/2014/04/page8.png)

So you have a STACKTRACE. Now what? 1. Can you READ IT? Does your function names look like “a.a.a.b” and “c.a.b.b”? This means it is obfuscated! Your build server or proguard mapping file will allow you to make this READABLE.   

![So you have a READABLE stacktrace? Awesome! This tells you EXACTLY which file and line is BREAKING!](http://www.hunterdavis.com/content/images/2014/04/page9.png)

So you have a READABLE stacktrace? Awesome! This tells you EXACTLY which file and line is BREAKING!   


![Anatomy of a Stack Trace. functionname at (filename:line) called by functionname at (filename:line) called by functionname at (filename:line) etc etc.](http://www.hunterdavis.com/content/images/2014/04/page10.png) 

Anatomy of a Stack Trace. functionname at (filename:line) called by functionname at (filename:line) called by functionname at (filename:line) etc etc.   

![Time to ask a SERIES OF QUESTIONS. 1. Do you know how to program? No? Go to page # 16](http://www.hunterdavis.com/content/images/2014/04/page11.png)

Time to ask a SERIES OF QUESTIONS. 1. Do you know how to program? No? Go to page # 16   

![So You Know How To Program! Cool! 1. Find function name on or near line # from stack trace. 2. determine which input or state caused the error. 3. FIX or PREVENT the error or state.](http://www.hunterdavis.com/content/images/2014/04/page12.png)

So You Know How To Program! Cool! 1. Find function name on or near line # from stack trace. 2. determine which input or state caused the error. 3. FIX or PREVENT the error or state.   

![Still Not Working? 1. Lookup the API docs for that function, these change often. 2. Validate inputs and thread /race conditions. Check for multiple instantiation, static items.](http://www.hunterdavis.com/content/images/2014/04/page13.png)

Still Not Working? 1. Lookup the API docs for that function, these change often. 2. Validate inputs and thread /race conditions. Check for multiple instantiation, static items.   

![Why Is My Function CRASHING?!?!?! 1. Tried everything? Replace it! There are tons of free libraries for Android! Or Rewrite it! There is always another way!](http://www.hunterdavis.com/content/images/2014/04/page21.png)

Why Is My Function CRASHING?!?!?! 1. Tried everything? Replace it! There are tons of free libraries for Android! Or Rewrite it! There is always another way!   

![Still Broken? 1. Find the first function name in the stack trace. 2. Type it into Google or Stack Overflow. 3. Try all Suggestions, think about similarities. 4. Repeat for every function in file.](http://www.hunterdavis.com/content/images/2014/04/page14.png)

Still Broken? 1. Find the first function name in the stack trace. 2. Type it into Google or Stack Overflow. 3. Try all Suggestions, think about similarities. 4. Repeat for every function in file.   

![Still Broken? 1. Do you have Source Control? No? Pay for GitHub or something! Yes? Cool! Time for…](http://www.hunterdavis.com/content/images/2014/04/page15.png)

Still Broken? 1. Do you have Source Control? No? Pay for GitHub or something! Yes? Cool! Time for…   

![Source Code Archaeology! 1. Find the first version in source control which exhibited this behavior! 2. Look at the CHANGES for this exact version.](http://www.hunterdavis.com/content/images/2014/04/page17.png)

Source Code Archaeology! 1. Find the first version in source control which exhibited this behavior! 2. Look at the CHANGES for this exact version.   

![3. Find the source file and functions which changed, this is your “improvised stacktrace.” 4. go back to the page about stack traces and use your “improvised stacktrace”](http://www.hunterdavis.com/content/images/2014/04/page18.png)

then 3. Find the source file and functions which changed, this is your “improvised stacktrace.” 4. go back to the page about stack traces and use your “improvised stacktrace”   

![Still nothing? 1. Call hunter. This is serious. 2. If you do not have a “hunter” working with you, post up on stack overflow or even XDA-developers.](http://www.hunterdavis.com/content/images/2014/04/page19.png)

Still nothing? 1. Call hunter. This is serious. 2. If you do not have a “hunter” working with you, post up on stack overflow or even XDA-developers.   

![Still haven’t fixed it? 1. Go back to page #1. 2. Sleep on it. 3. Go back to page #1.](http://www.hunterdavis.com/content/images/2014/04/page20.png)

Still haven’t fixed it? 1. Go back to page #1. 2. Sleep on it. 3. Go back to page #1.   

