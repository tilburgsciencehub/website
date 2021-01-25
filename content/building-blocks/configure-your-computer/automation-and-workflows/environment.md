---
title: "Making Path Settings Permanent"
description: "For our workflow to be command line driven, we need to be able to call software from the command line."
keywords: "PATH, add, terminal, cli"
weight: 4
date: 2020-11-11T22:02:51+05:30
draft: false
---

For our workflow to be command line driven, we need to be able to call software from the command line.
Whilst much of the software we have installed as automatically made this possible, it is not universally the case.
Here we will make the extra few changes we need to complete the installation guide.

## Windows Users (for Windows 8 and 10)

You will need local administration rights for your computer, but you should have these on your personal computers or ones owned by the Department.

Right-click on Computer. Then go to "Properties" and select the tab "Advanced System settings". Choose "Environment Variables" and select "Path" from the list of system variables.

Choose “Edit” and append (i.e., do not overwrite the previous value):

        C:\Path\to\program.exe

to the variable value – make sure the rest remains as it is and do not include spaces between the ";" and the text.

Click on OK as often as needed.

If you accepted all defaults during your installation, and didn't have any other non-default setting prior to starting this guide, modifying the following string, with your relevant username *should* work:

        ;C:\Users\ldeer\AppData\Local\atom\bin
        ;C:\Program Files\Git\bin
        ;C:\Program Files\R\R-3.X.X\bin
        ;


## Mac Users (Slight Modifications for Linux Users)

You will need to add a line to the file ".bash_profile" or potentially create the file if it didn't already exist.
This file lives in your home directory and it is hidden from your view by default.

We now provide a guide of how to create / adjust this file using a tiny editor called nano, if you are familiar with editing text files, just use your editor of choice.

Open a Terminal and type:

        nano ~/.bash_profile

If .bash_profile already existed, you will see some text at this point. If so, use the arrow keys to scroll all the way to the bottom of the file.

Add the following line at the end of the file:

        export PATH="${PATH}:/path/to/program/inside/package"

for each program we need to make accessible.

For example to make matlab accessible from the command line:

        export PATH="${PATH}:/Applications/MATLAB_R2016a.app/bin/matlab

Please do this for the following software:

* Sublime Text
* Git
* Matlab
* R

Once you have finished,  press Return and then ctrl+o (= WriteOut = save) and Return once more.

Your default locale settings may conflict with some of the programs we'll need.
If you want to be on the safe side, add these lines to your .bash_profile file:

        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8

Thanks for Hans-Martin von Gaudecker, and in turn Matthias Bannert for the tip on locale settings.

**Linux users**: For most distributions, everything here applies to the file .bashrc instead of .bash_profile.
