---
layout: post
title: 'Tutorial: Achievements and Leaderboards with Google Play Services'
image: http://www.hunterdavis.com/content/images/2013/09/magic_achievements.png
date: '2013-09-24 05:37:00'
---


I took today off to play Grand Theft Auto 5 and relax. After a few hours of play, and a few more hours of relaxing, I realized that I hadn’t written an article about Android in a while. I also haven’t updated [The Grind](https://play.google.com/store/apps/details?id=com.hunterdavis.thegrind) in a while, which is a shame because it’s one of my favorite casual games and also one of my more popular ones.

So, I decided to update The Grind with Achievements and Leaderboards using the new Google Play Services framework. As with all of my apps and games, this is fully [open sourced on GitHub](https://github.com/huntergdavis/The_Grind) (BSD licensed) so you can use the code, icons, graphics, and ideas however you wish.

**Prerequisites**  
 Before you do anything, you’ll need to have a Google Developer account, and a working knowledge of Android/Java programming. Feel free to [go through](https://github.com/huntergdavis) the ~70 android apps I’ve open sourced on GitHub to brush up on things.

[![gitthub](http://www.hunterdavis.com/content/images/2013/09/gitthub-300x164.png)](http://www.hunterdavis.com/content/images/2013/09/gitthub.png)

Follow the [Google Player Services setup guide](https://developer.android.com/google/play-services/setup.html), and make sure your project can be built with the play services ‘library project’ referenced.

Now, clone the [‘basegameutils’](https://github.com/playgameservices/android-samples) library for an easier time implementing your auth flow.

**Setting Up Your Game Details On Google Play**

Go through the text-heavy Google Play Developer Console “Game Services” setup and enter all your app information.

[![gamedetails](http://www.hunterdavis.com/content/images/2013/09/gamedetails-300x162.png)](http://www.hunterdavis.com/content/images/2013/09/gamedetails.png)

You can import most of your information from an existing listing, if you have one.

[![gamedetails](http://www.hunterdavis.com/content/images/2013/09/gamedetails-300x162.png)](http://www.hunterdavis.com/content/images/2013/09/gamedetails.png)

When you’re finished, you’ll also need to grab your generated app ID from the developer console or API console and append it to your metadata app tag in AndroidManifest.xml

[![gameservices](http://www.hunterdavis.com/content/images/2013/09/gameservices-300x199.png)](http://www.hunterdavis.com/content/images/2013/09/gameservices.png)

**Choosing your Achievements**

[![newachievement](http://www.hunterdavis.com/content/images/2013/09/newachievement-300x162.png)](http://www.hunterdavis.com/content/images/2013/09/newachievement.png)

Always make sure you throw in at least one Spaceballs reference.

[![spaceballs](http://www.hunterdavis.com/content/images/2013/09/spaceballs-300x162.png)](http://www.hunterdavis.com/content/images/2013/09/spaceballs.png)

**Creating your Icons**  
 One of the great things about Wikipedia Commons is the vast troves of images which are available for unlicensed use. If you’re not a great artist and you wish to create an armor icon, why not base it off a public domain image of a real piece of 15th century armor?

[![armorup](http://www.hunterdavis.com/content/images/2013/09/armorup1-253x300.png)](http://www.hunterdavis.com/content/images/2013/09/armorup1.png)

[![armorup](http://www.hunterdavis.com/content/images/2013/09/armorup-300x300.png)](http://www.hunterdavis.com/content/images/2013/09/armorup.png)

**Creating a Leaderboard – Google Play Authentication**

For any of this to work, you’re going to need to link it to your Google Play account. That means you’ll need to implement sign-in related functions in your app.

Derive from ‘BaseGameActivity’, then add the following methods:

```
<br></br>
    @Override<br></br>
    public void onSignInFailed() {```

 }

 @Override  
 public void onSignInSucceeded() {

 }

Depending on your game design, you may or may not need to actually implement anything in the above methods.

**Hooking Up Your Leaderboard In Your Game**  
 The developer documents are always a good reference, and the Leaderboard docs (though sparse) should still be your first stop when looking to code up a feature. Google has made it very easy to implement this functionality. Your leaderboard is essentially just a large integer table. Simply update your score in the same function you save your game state or in a menu option with the following snippet.

```
<br></br>
 getGameClient().submitScore(leaderBoard, player1.experience);<br></br>```

[![new_play_menu_items](http://www.hunterdavis.com/content/images/2013/09/new_play_menu_items-168x300.png)](http://www.hunterdavis.com/content/images/2013/09/new_play_menu_items.png)

**Displaying Your Leaderboard In Your Game**  
 Google has also made is very easy to display your leaderboard and global rankings as follows.

```
<br></br>
startActivityForResult(getGamesClient().getLeaderboardIntent(LEADERBOARD_ID), JUST_AN_INTEGER_VALUE);<br></br>```

[![leaderboard](http://www.hunterdavis.com/content/images/2013/09/leaderboard-168x300.png)](http://www.hunterdavis.com/content/images/2013/09/leaderboard.png)

**Hooking Up Your Achievements In Your Game**  
 Hooking up achievements is as simple as implementing a function to send achievements to the server. Easy as pie.

```
<br></br>
    public void getAnAchievement(GamesClient gc, String achievementId) {<br></br>
        gc.unlockAchievement(achievementId);<br></br>
    }<br></br>```

From here, you’ll likely want to save all these achievement IDs as strings in your resource file so they can be referenced and adjusted in an easier fashion.

[![achievements](http://www.hunterdavis.com/content/images/2013/09/achievements-300x163.png)](http://www.hunterdavis.com/content/images/2013/09/achievements.png)

**Displaying Your Achievements In Your Game**  
 Finally, Google has once again made it easy to display your achievements as follows:

```
<br></br>
startActivityForResult(getGamesClient().getAchievementsIntent(), JUST_AN_INTEGER_VALUE);<br></br>```

[![magic_achievements](http://www.hunterdavis.com/content/images/2013/09/magic_achievements-168x300.png)](http://www.hunterdavis.com/content/images/2013/09/magic_achievements.png)

And that’s that. You’ve just brought your Game into the age of achievements.


