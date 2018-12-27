---
layout: post
title: A Script to Open All The Sources! (I released 70 open source projects today)
date: '2012-04-11 22:50:55'
---


I’ve been studying my site and app traffic for a while now, and I’ve come to a very sure conclusion. Open-sourcing an app does nothing to decrease app sales or ad traffic, but increases web traffic significantly. Therefore I’ve decided to open source everything I’ve ever done, BSD licensed so you can use it at work.

Seriously, all the sources. Every one. To start with, I’ve created repositories for the roughly 70 Android applications I’ve released. As of today, you can browse through them all on my [GitHub account page](https://github.com/huntergdavis).

<iframe allowfullscreen="" frameborder="0" height="360" src="http://www.youtube.com/embed/74BzSTQCl_c?feature=player_embedded" width="640"></iframe>

Unfortunately for me, the task of open sourcing 100+ projects is a daunting one, so I set about writing a script to troll my folders and create GitHub projects. This script itself is also available on GitHub [here](https://github.com/huntergdavis/createGitHubscript). Read on for more info about the construction of the script.

  
 I started with a folder full of my android applications, but you can apply this to any set of directories. You’ll need curl, git, and your GitHub username and API key. The script simply creates a set of repositories with a combination of passed and inferred metadata.

I started by getting my API access key, metadata prefix, and github user-name and read them in via parameter as follows.  
```
<br></br>
# we want k for api key, x for prefix, u for username, h for help<br></br>
# pre-set prefix to APPLICATION<br></br>
PREFIX="APPLICATION";```

while getopts "k:x:h:u:" opt;  
 do  
 case $opt in  
 k) API_KEY=$OPTARG;;  
 x) PREFIX=$OPTARG ;;  
 u) USERNAME=$OPTARG ;;  
 h) echo "Usage: createGitHubscript.sh -k GITHUB_API_KEY -u GITHUB_USERNAME -x DESCRIPTION_PREFIX" ; exit 1 ;;  
 *) echo "Usage: createGitHubscript.sh -k GITHUB_API_KEY -u GITHUB_USERNAME -x DESCRIPTION_PREFIX" ; exit 1 ;;  
 esac  
 done

if [ -z "$API_KEY" ];  
 then  
 echo "Must have a API KEY set!"  
 echo "Usage: createGitHubscript.sh -k GITHUB_API_KEY -u GITHUB_USERNAME -x DESCRIPTION_PREFIX" ;  
 exit 0;  
 fi

if [ -z "$USERNAME" ];  
 then  
 echo "Must have a API KEY set!"  
 echo "Usage: createGitHubscript.sh -k GITHUB_API_KEY -u GITHUB_USERNAME -x DESCRIPTION_PREFIX" ;  
 exit 0;  
 fi

Here I iterate over each folder in the passed-in directory.

```
for dir in `ls "$src/"`<br></br>
do<br></br>
  if [ -d "$src/$dir" ]; then<br></br>```

From the folder name I glean the title of the app, which is used to create the application on GitHub via their yaml api. I also sleep 5 seconds after repository creation, for politeness.

`cleandir="${dir// /_}";`

echo "Time to create a repository for $dir, named $cleandir";  
 curl -F "login=$USERNAME" -F "token=$API_KEY" https://github.com/api/v2/yaml/repos/create -F name="$cleandir" -F description="$PREFIX - $dir";

echo "Now sleep 5 seconds for politeness";  
 sleep 5;

After this is completed, I move into the directory, and initialize a git repository, add all the files, make the first commit, and push it up to GitHub.

```
# init git<br></br>
git init;```

# add everything  
 git add ./* ;

# make a first commit  
 git commit -a -m "initial commit for $dir";

# add the remote origin  
 git remote add origin git@github.com:$USERNAME/$cleandir.git ;

# push it on up  
 git push origin master

And that’s that. You can see the full code at the script’s git repository. Feel free to browse the avalanche of source code that’s hitting GitHub from my computer today 🙂


