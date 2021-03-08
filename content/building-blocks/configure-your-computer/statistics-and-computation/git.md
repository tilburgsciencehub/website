---
title: "Git and GitHub for Version Control"
description: "Git is an open source version control system (VCS) that has gained a lot of traction in the programming community."
keywords: "git, github, installation, software, configuration, versioning, account"
date: 2020-11-11T22:02:51+05:30
draft: false
weight: 11
aliases:
  - /get/git
  - /install/git
---

## Installing Git and Setting Up Accounts

Git is an open source version control system (VCS) that has gained a lot of traction in the programming community. We will use version control to keep track of the files we write, and the changes we make to them. Using Git, we can roll back to any previous version of a file, and easily collaborate with others on source code.

## Let's create a GitHub account

GitHub is a (commercial) platform which allows you to host your source code online.
It also offers a set of collaborative tools to manage "Issues",
and track progress on project boards.

- Please [register for a GitHub account](https://github.com/join), and
  claim your [education benefits for students and professors](https://education.github.com) afterwards.
- You can also watch our YouTube video where we will walk you through the sign-up procedure.

{{< youtube 3KOnOgz_dAA >}}

## Installation

Watch our YouTube video, in which we walk you through the setup on Windows.

{{< youtube VUzv5RcnW60 >}}

Download and install the latest versions of Git [here](https://git-scm.com/download).

### Additional instructions for Windows Users

After installing the programs use Windows Explorer to go to a folder that contains some documents (any folder) and right click on it.

You should see some additional items - "Git Bash here", or "Git GUI here" appear in the context menu upon right-clicking.

<!--Whenever you wish to open Git, you

!!! danger "Making Git available via the PATH settings on Windows"
    We need to update our PATH settings; these settings are a set of directories that Windows uses to "look up" software to startup.

    - Right-click on Computer.
    - Go to "Properties" and select the tab "Advanced System settings".
    - Choose "Environment Variables" and select `Path` from the list of system variables.
    - Choose `Edit`.
    	- **Windows 7 and 8 machines:**
    		If you chose your installation directory to be C:\R\R-3.6.1\ during your installation (i.e., you did not use the default directory), copy and paste the following string without spaces at the start or end:

            `;C:\Program Files\Git\bin`

    	- **Windows 10 machines:**
    		- Click `New` and paste the following string:

            `C:\Program Files\Git\bin`

    		- Click on `OK` as often as needed.
-->

### Additional instructions for Mac Users

Download the setup files from the link above. If your system says the file can't be opened (because it is from an unidentified developer), then open it via right-lick and `open`.

<!--Also install the command-line auto-completion script. For this go to [this website](https://github.com/git/git/raw/master/contrib/completion/git-completion.bash). You should now see a the text file starting with

```
# bash/zsh completion support for core Git.
#
# Copyright (C) 2006,2007 Shawn O. Pearce <spearce@spearce.org>
# Conceptually based on gitcompletion (http://gitweb.hawaga.org.uk/).
# Distributed under the GNU General Public License, version 2.0.
```

save this file as `git-completion.bash` to your user folder by pressing `CMD+s`. If you want to know where your user folder is, open a terminal and type ```pwd```. For Uli it is for example under `/Users/ubergmann`.

If you use Safari, make sure to save the file as `Page Source` and don't append a `.txt` to its filename (Chrome does this automatically). If everything went right, you can now type `ls` in your terminal window and should see `git-completion.bash` there between other files.
-->

<!--
### Linux Users

Follow the steps documented [here](https://git-scm.com/download/linux) to install on Linux from the terminal.

!!! danger
    To install system software using `apt-get`, you need `Super User` rights. So please add `sudo` in front of each `apt-get` command in the document above, like so: ```sudo apt-get install git```
-->
<!--
## Verifying your installation

<!-- We will need to make Git accessible from the command line. Windows and Mac users will need to follow the steps on the page "Modifying Path Settings." Linux users will already have git accessible from the command line. -->

<!--
To verify your installation, type the following command in a terminal and press the return key:

```bash
       git --version
```

You should get an output that looks like:

```bash
        git version 2.18.0
```

Ensure that you have a version greater than `2.15.0` installed.
-->
