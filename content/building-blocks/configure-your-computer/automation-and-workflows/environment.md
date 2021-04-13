---
title: "Making Path Settings Permanent"
description: "For our workflow to be command line driven, we need to be able to call software from the command line."
keywords: "PATH, add, terminal, cli, bash"
#weight: 4
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /setup/environment
  - /setup/path-settings
---

## Overview

For our workflow to be command line driven, we need to be able to call software from the command line. Whilst much of the software we have installed as automatically made this possible, it is not universally the case.
Here we will make the extra few changes we need to complete the installation guide.

### Windows Users

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


### Mac and Linux Users 

You will need to add a line to the file ".bash_profile" or potentially create the file if it didn't already exist.
This file lives in your home directory and it is hidden from your view by default.

We now provide a guide of how to create / adjust this file using a tiny editor called nano, if you are familiar with editing text files, just use your editor of choice.

Open a Terminal and type:

```bash
nano ~/.bash_profile
```

You should now see something similar to this. It's a text editor within the Terminal. Here you can add your environment variables.

![PATH variables in the Bash profile](../img/bash-profile.png)

{{% warning %}}
If .bash_profile did not exist already, you need to create it.
{{% /warning %}}

You can add your environment variable by adding a new line:
```bash
export PATH=$PATH:/path/to/folder
```

You can save by pressing `Ctrl + O` and exit by pressing `Ctrl + X`.

Once you're done, you'll need to reload `bash`. Close and launch again a new Terminal session, the type:

```bash
. ~/.bash_profile
```

Do this for each program you need to make accessible from the command line. Do this for:

* Sublime Text
* Git
* Matlab
* R

For example, to make MATLAB accessible from the command line:
```bash
export PATH=$PATH:/Applications/MATLAB_R2016a.app/bin/matlab
```



Your default locale settings may conflict with some of the programs we'll need.
If you want to be on the safe side, add these lines to your .bash_profile file:

        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8

Thanks for Hans-Martin von Gaudecker, and in turn Matthias Bannert for the tip on locale settings.

**Linux users**: For most distributions, everything here applies to the file .bashrc instead of .bash_profile.
