# Midterm 02
# GOPH 457 – Physical properties of minerals, soils, and rocks.
*Semester:* W2024
*Instructor:* B. Karchewski
*Author:* Oyedemi Joshua Oluwadamilare.

AI USE:
The use of AI was not lost in completing an ample and gorgeous portion of the implemented code uploaded onto the git repository and in this lab assignment. I used AI to guide code implementation, numerical analysis techniques, and various debugging strategies. It helped in suggesting methods for testing, plotting results effectively and efficiently, and refining function outputs.

HOW TO INSTALL

NOTE!!!: Cloning my remote repository to your local machine;
For You to download and edit my source code and other project files, you will need to clone my repository from the remote on GitHub.
Here are the steps:

1. Open a terminal session on your local machine.
2. Navigate to the directory where you want to store the repository files.
For example:
cd $HOME\Repos\Courses\goph457 # on Windows
cd ~/Repos/Courses/goph457 # on Mac/Linux or whichever directory you prefer. [Note: It is not recommended to store repositories tracked with git and a remote GitHub under a file synchronization
app such as Dropbox or OneDrive because the synchronization may interfere with the operation of git and cause conflicts. Rest assured that using git with a remote server achieves the ability to backup files and work from multiple different machines that is usually the purpose of using file synchronization programs.]
3. If you have an SSH key setup on your machine, clone your new repository with:
git clone <git@github.com>:USER/goph457-w2025-MT02-stOJ.git
If you do not have an SSH key setup, you can use:
git clone <https://github.com/USER/goph457-w2025-MT02-stOJ.git>
and you may need to enter your GitHub password.
If you installed the GitHub CLI, you can use:
gh repo clone USER/goph457-w2025-MT02-stOJ.git.
4. You should now have a directory called goph457-w2025-MT02-stOJ.git,
which you can check by entering:
ls
to list the directory contents and make sure that you see it.
5. Move into the new directory with:
cd goph457-w2025-MT02-stOJ
This is the directory where you will create and track your source code for the project.
6. You can confirm that this directory is tracked with git in a few ways. You can enter:
ls -Hidden # on Windows
ls -a # on Mac/Linux
and confirm that you see the hidden directory .git, which is where git stores
the files needed to track your project’s current state and history. Most of the
time you will not need to enter this directory, but its presence indicates active
tracking by git. You can also enter some git commands and confirm thatyou get sensible output:
git status # to see current state information
git remote -v # to see the name and address of the remote
git log # to page through commit history, q to exit
With the last command, you should see at least one commit already from when
you initialized the repository on GitHub. This is a useful command if you want
to reset to an earlier commit, because you can see the commit messages and
corresponding commit IDs. Now that your repository is initialized on GitHub
and you have a local copy, you should set up a virtual environment for your
Python code development.
7. Later, if you make changes to the repository from a different machine (or other
collaborators make changes), you can update your local copy to the latest
version using:
git pull
which "pulls" any updates by downloading them from the remote server and (if
necessary) asking you to resolve any conflicts with your local version. [Note:
It is a good habit and best practice to pull any updates from the remote before
pushing any local commits because a blind push may overwrite changes made
by collaborators.]
