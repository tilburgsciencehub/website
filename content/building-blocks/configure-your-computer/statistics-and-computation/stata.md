---
title: "Stata"
description: "Stata is a proprietary statistical software frequently used by scientific users."
keywords: "Stata, software, installation, configuration, statistics"
#date: 2020-11-11T22:02:51+05:30
draft: false
#weight: 5
aliases:
  - /get/stata
  - /install/stata
---

## Installing Stata

Stata is a proprietary statistical software frequently used by scientific users.
First check with your local IT support whether your institution has Stata licenses available.

If not, you can purchase a copy on [Stata's website](https://www.stata.com/) and follow the [installation guide](https://www.stata.com/install-guide/).

## Making Stata Available on the Command Prompt

You have just installed Stata. Later, we'd like to access Stata from the
command prompt to automatically execute our source code. That way, you will
be able to run a series of scripts in batch - which will significantly ease the burden of
building complex data workflows.

### Windows users
For you to be able to use Stata from the command prompt, follow the steps below.

{{% warning %}}
**Making Stata available via an environment variable.**

We need to update our environment variables.

- Right-click on Computer.
- Go to "Properties" and select the tab "Advanced System settings".
- Choose "Environment Variables" and create a new variable, which you call `STATA_BIN`.
- Choose `Edit`.
	- Environment variable name: `STATA_BIN`
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
{{% /warning %}}

### Mac users

For you to be able to use Stata from the command line, you have to add Stata to your environmental variables. A tutorial follows.

{{% warning %}}
**Making Stata available via the PATH settings on Mac.**

- Open the Terminal.
- Type `nano ~/.bash_profile`.
- Add Stata to the environmental variables:
		- Add `export STATA_BIN=/Applications/Stata/StataMP.app/Contents/MacOS/stataMP` to a new line. You may need to replace stataMP to stataSE or so, which depends on which Stata you install on Mac.
		- Save by pressing `Ctrl + O` and exit by pressing `Ctrl + X`.
		- Relaunch the Terminal. Then type `source ~/.bash_profile` to bring the new .bash_profile into effect.
- Type `$STATA_BIN -v` to check availability. Remember to type the `$` before `STATA_BIN`.
{{% /warning %}}

<!--- Linux users not available yet
-->


## Verifying the installation

To verify that Stata has been correctly installed and configured via your PATH settings,
follow the instructions below.

### Windows users

Open a **new** terminal interface and enter:

```bash
%STATA_BIN%
```

followed by hitting the `Return` key. You can check the Stata version.

{{% warning %}}
If you obtain the following error:
```bash
'C:\Program' is not recognized as and internal or external command
```
Add " " to your variable path, for instance
`"c:\Program Files (x86)\Stata15\StataSE-64.exe"`.
{{% /warning %}}

### Mac users

Open a **new** terminal interface and enter:

```bash
echo $PATH
```

followed by hitting the `Return` key.
