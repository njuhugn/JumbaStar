Git Instructions
================

These are the instructions for Lec-13-lab

# Objectives
Learn how to use github for collaboration.

# Instructions
Git installed in your VM. Open a terminal on your VM and
follow the instructions.

Follow instructions here for setting up git
https://help.github.com/articles/set-up-git/

We are going to connect over ssh. Generate your ssh keys
Generating ssh keys https://help.github.com/articles/generating-ssh-keys/

Clone a repo
Create a directory for all your repos. Clone the test repo.

```
mkdir repos
cd repos
git clone git@github.com:ucb-stat-157/Test.git
cd Test
ls
```

Making changes. Let's make a personal copy of dt.py and submit it to the
repository.
```
cp dt.py dt_<githubId>.py
git add dt_<githubId>.py
git commit -m "adding my dt file"
git push origin master
```

