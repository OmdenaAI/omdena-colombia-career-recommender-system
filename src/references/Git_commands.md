# Git Commands
*Compiled by Victor Cuspinera*

### Setting up
| Description | Command |
|---------|-------------|
| add name to your Git configuration | `git config --global user.name 'YOUR NAME HERE'` |
| add email to your Git configuration | `git config --global user.email 'YOUR EMAIL HERE'` |
| see your git configuration | `git config --global --list` |

### Basic commands
| Description | Command |
|---------|-------------|
| create a local copy of a repository in GitHub|`git clone https://github.com/<github_username>/<repository_name>.git`|
| adds a specific file(s) of your local repo to the staging area|`git add <file_name(s)>`|
| adds all files of your local repo to the staging area|`git add .`|
| commit the file that previously was added. You must write a comment!|`git commit -m "WRITE A COMMENT HERE"`|
| upload the changes from your local repo to the remote repo in GitHub|`git push`|
| displays the state of your local repository and the staging area|`git status`|
| update the local repo from the repo in GitHub|`git pull`|

### Remote for collaborative working
| Description | Command |
|---------|-------------|
| add a remote |`git remote add upstream <original_repo_URL>`|
| retrieves the data locally (does not change the state of repo/files)|`git fetch upstream`|
| incorporate the data into your repo|`git merge upstream/master`|

### Useful branching commands

| Description | Command |
|---------|-------------|
| list all local branches | `git branch -v` |
| create a new branch | `git branch <branch_name>` |
| switch to a branch | `git checkout  <branch_name>` |
| create a new branch & immediately switch to it | `git checkout -b <branch_name>` |
| retrieve a branch you don't have locally on your laptop from GitHub| `git checkout --track origin/<branch_name` |
| merge changes from another branch | `git merge <branch_name>` |
| delete a local branch | `git branch -d <branch_name>` |
| push changes to a remote branch | `git push origin <branch_name>` |

### Steps for updating a branch from the master  
[(go to original source)](https://gist.github.com/santisbon/a1a60db1fb8eecd1beeacd986ae5d3ca)

1. update your local master branch
    - `git checkout master`
2. Fetch the remote, bringing the branches and their commits from the remote repository.
    - `git fetch -p origin`
3. Merge the changes from origin/master into your local master
    - `git merge origin/master`
4. Check out the branch you want to merge into
    - `git checkout <feature-branch>`
5. Merge your updated master branch into your feature branch 
    - `git merge master`

### What happens when my feature branch falls behind master?
##### Material from [DSCI 524 - Collaborative Software Development, lecture 1](https://github.ubc.ca/MDS-2019-20/DSCI_524_collab-sw-dev_students/blob/master/lectures/01_lecture-intro-more-git.md)

We experienced a similar issue when working with the fork & pull-request workflow in past projects, to catch up our fork to the source project's fork. We had to do the following:

- ensure the source project's fork was set as upstream
- run `git fetch upstream` to get the changes
- run `git merge origin/master` to merge the changes
- run `git push` (which is short for git push origin master) to push our changes to our fork's remote

To catch up a branch that has fallen behind master we do the following:

- run `git pull origin master` to pull any changes from the remote version of master that we might not have
- run `git checkout <branch>` to make sure we are on the branch we want to catch up
- run `git merge master` to merge the changes
- run `git push origin <branch>` to push our updated branch to the remote

# References:
- [GitHub (2020). GitHub Help, Using Git 2020](https://help.github.com/en/github/using-git)
- [FreeCodeCamp (2020-01-27). Git Pull Explained.](https://www.freecodecamp.org/news/git-pull-explained/)
- [Jenny Bryan. Happy Git and GitHub for the useR, Chapters 21 Git commands and 22 Branches.](https://happygitwithr.com/git-commands.html)
- [git-scm.com. Chapter 2.5 Git Basics - Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [UBC-MDS (2020). DSCI 524-Collaborative Software Development, lecture 1](https://github.ubc.ca/MDS-2019-20/DSCI_524_collab-sw-dev_students/blob/master/lectures/01_lecture-intro-more-git.md)
- [santisbon (2018). Updating a feature branch](https://gist.github.com/santisbon/a1a60db1fb8eecd1beeacd986ae5d3ca)
