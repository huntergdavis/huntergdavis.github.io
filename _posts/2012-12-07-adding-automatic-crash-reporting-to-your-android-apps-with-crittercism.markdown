---
layout: post
title: Adding Automatic Crash Reporting to Your Android Apps with Crittercism
date: '2012-12-07 17:34:45'
---


While pushing out an update to ‘[The Grind](https://play.google.com/store/apps/details?id=com.hunterdavis.thegrind)‘ this week, I had a few users who reported crashes with the newest content pack update. Unfortunately, Google Play’s dev console did not show the errors, and the users were not sure where the crashes were occurring. What is a developer to do?

Keep reading for a quick tutorial on setting up [Crittercism](http://www.crittercism.com/) crash reporting in your app.

![Crittercism Logo](https://www.crittercism.com/images/critters/hamster-bg.png)

**Setting up A Crittercism Account**  
 First, you’ll want to head over to [Crittercism](http://www.crittercism.com/) and set up a free account (Full disclosure: I have no affiliation with the Crittercism folks but I do like their product.)

**Setting up an App in Crittercism**  
 Log into your Crittercism account and select the ‘apps’ tab. This will give you a left-nav option to ‘register a new app’. Click this, and enter your application name. That’s that. All the other relevant details will be derived by crittercism from the application itself.

**Adding the Crittercism Library to your Android Project**  
 Log into your Crittercism account and select the ‘downloads’ tab. Click on the ‘android’ banner, and download the newest version of Crittercism. This will give you a .jar file which you then drop into the /libs/ directory in your Android project. That’s that.

**Initializing Crittercism in your Android App**  
 Log into your Crittercism account and select the Android app you set up in the previous step. Select ‘settings’. This will give you your dev key to be used.

Now, open up your project’s AndroidManifest.xml and paste in the following activity.  
`<br></br><br></br>`

Also make sure you’re requesting the ‘internet’ permission with  
`<br></br><br></br>`

Finally, you’ll want to open your applications main activity, and instantiate Crittercism with the app id you found in your app settings.  
```
<br></br>
Crittercism.init(getApplicationContext(), "CRITTERCISM_APP_ID");<br></br>```

Congratulations, you now have crash reporting in your app. You can now upload your app to Google Play and the crash reports will start to flow in.

**Viewing your crash logs online**

Now that crash reporting is in your app, simply log into Crittercism, click on the application you registered, and click the ‘crash reports’ tab.

[![](http://www.hunterdavis.com/content/images/2012/12/crittercismlog-207x300.png "crittercismlog")](http://www.hunterdavis.com/content/images/2012/12/crittercismlog.png)


