---
title: "Stata"
date: 2020-11-11T22:02:51+05:30
draft: false
---
# Installing Stata

Stata is a proprietary statistical software frequently used by scientific users.
First check with your local IT support whether your institution has Stata licenses
available.

If not, you can purchase a copy on [Stata's website](https://www.stata.com/) and follow the [installation guide](https://www.stata.com/install-guide/).

## Making Stata Available on the Command Prompt

You have just installed Stata. Later, we'd like to access Stata from the
command prompt to automatically execute our source code. That way, you will
be able to run a series of scripts in batch - which will significantly ease the burden of
building complex data workflows.

### Windows users
For you to be able to use Stata from the command prompt, follow the steps below.

!!! danger "Making Stata available via an environment variable"
    We need to update our environment variables.

    - Right-click on Computer.
    - Go to "Properties" and select the tab "Advanced System settings".
    - Choose "Environment Variables" and create a new variable, which you call `STATA_BIN`.
    - Choose `Edit`.
    	- **Windows 7 and 8 machines:**
    		Please check where you have installed Stata on your computer, and
        note the name of the Stata program file (on some machines, it is called
          `StataSE.exe`, on others it is called `StataMP-64.exe`.

          Then, update the path if required, and copy and paste the following string without spaces at the start or end:

          `c:\Program Files (x86)\Stata15\StataSE-64.exe`

    	  Using a different Stata version? Change the version number then in the path above.

    	- **Windows 10 machines:**
    		- Click `New` and paste the following string:

            `c:\Program Files (x86)\Stata15\StataSE-64.exe`

    		- Click on `OK` as often as needed.

### Mac users

For you to be able to use Stata from the command line, you have to add Stata to your bash file. A tutorial follows.

!!! danger "Making Stata available via the PATH settings on Mac"
      - Open `Terminal`.
      - Type `echo "export PATH=$PATH: Your Stata Path" >> ~/.bash_profile`. For example,
  		`export PATH=$PATH: /Applications/Stata/StataMP.app/Contents/MacOS/  >> ~/.bash_profile`

<!--- Linux users not available yet
-->


## Verifying that the installation was successful

To verify that Stata has been correctly installed and configured via your PATH settings,
follow the instructions below.

### Windows users

Open a **new** terminal interface and enter:

```bash
%STATA_BIN%
```

followed by hitting the `Return` key. Stata will now start.

### Mac users

Open a **new** terminal interface and enter

```bash
echo $PATH
```

followed by hitting the `Return` key.
