I encountered an issue when trying to upload homework 6 using git. My inital pickled classifier 
was too large to upload to github when I first tried to commit and push my homework. I tried to 
undo this commit and recommit the files, this time with a zipped pickled classifier, but failed 
because my previous commit containing the large pickled file was persisting. I made various 
attempts at undoing the initial commit (>>git reset HEAD, >>git reset, >>git reset --hard) but 
none of these worked and each time I tried to recommit, I ended up adding more and more files 
locally to be commited, but couldn't do a git push since my original commit was still there. I 
tried to use git revert but ended up deleting one of my previous homework directories. At this 
point I stopped and added the files to my github by dragging and dropping my homework 6 directory 
directly into the github online GUI.