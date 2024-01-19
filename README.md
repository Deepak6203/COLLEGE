# COLLEGE
##How to Upload In this directory pwd--> /c/Users/deepa/Desktop/College1

### 1$ git status
On branch main
Your branch is up to date with 'origin/main'.

  Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Portfolio/3-Portfolio-alexander-starter/
        Portfolio/5-Portfolio-web0/

### 2$ git branch --list
* main

### 3 deepa@DESKTOP-GUMHF41 MINGW64 ~/Desktop/College1 (main)
$ git add .

### 4$ git commit -m "Two Files Add"


#### 5$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

### 6$ git remote        git remote -v
origin

### 7$ git push origin main
  DONE....

##---------------------------------------------------------------------------------------------------------------------------
IF Not pushing successfully then 
$ git push origin
To https://github.com/Deepak6203/COLLOGE.git<br/>
 ! [rejected]        main -> main (non-fast-forward)<br/>
error: failed to push some refs to 'https://github.com/Deepak6203/COLLOGE.git'


use1 <br/>
Pull Remote Changes:
Run " git pull origin main " (assuming you are on the main branch). This command fetches the latest changes from the remote repository and attempts to merge them into your local branch.<br/>
use2
Push Changes:<br/>
After resolving conflicts, if any, and committing any new changes, you can now try pushing again using " git push origin main " 


##============================================================================================================================
### Example of Other Repo
Quick setup — if you’ve done this kind of thing before <br />
or <br /> 
https://github.com/Deepak6203/COLLEGE.RR.git <br /> 
Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore. <br /> 
…or create a new repository on the command line <br /> 

echo "# RR">> README.md <br /> 
git init <br />
git add README.md <br /> 
git commit -m "first commit" <br /> 
git branch -M main <br /> 
git remote add origin https://github.com/Deepak6203/COLLEGE.RR.git <br /> 
git push -u origin main <br /> 
…or push an existing repository from the command line <br /> 
git remote add origin https://github.com/Deepak6203/COLLEGE.RR.git <br /> 
git branch -M main <br />
git push -u origin main <br />
