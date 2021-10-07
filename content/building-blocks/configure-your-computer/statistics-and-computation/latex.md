---
title: "Set up LaTeX"
description: "LaTeX is a great typesetting system that includes a lot of features that allow to produce scientific documents."
keywords: "latex, tex, lyx, install, software, configuration, paper, writing, text, typesetting"
#date: 2020-11-11T22:02:51+05:30
draft: false
#weight: 10
aliases:
  - /get/latex
  - /install/latex
---

## Installing Latex

{{< katex >}}\LaTeX{{< /katex >}} is [a great typesetting system](https://www.latex-project.org) that includes a lot of features that allow to produce scientific documents. Many researchers use Latex to produce their papers and presentations, and many journals require authors to hand in their articles in a TeX format.

Latex is free to use. To use the Latex system, a TeX distribution needs to be installed. Detailed instructions for the different platforms are provided below.

### Windows

Download the file `install-tl-windows.exe` from **[here](https://www.tug.org/texlive/acquire-netinstall.html)** and follow the instructions.

### MacOS

You can install MacTeX from the **[official website](https://www.tug.org/mactex/)** or using [`Homebrew`](/configure/cli):

```bash
brew cask install mactex
```

### Linux (Ubuntu-based)

Install it from the terminal using:

```bash
sudo apt-get install texlive-latex-extra
```

## Check your Installation

After following the instructions, check whether everything worked by checking the output of the following command:

```bash
tex --version
```

This should give an output similar to this one, where version numbers and details will change depending on your platform.

```bash
TeX 3.14159265 (TeX Live 2019/Debian)
kpathsea version 6.3.1
Copyright 2019 D.E. Knuth.
There is NO warranty.  Redistribution of this software is
covered by the terms of both the TeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the TeX source.
Primary author of TeX: D.E. Knuth.
```

Note that additional packages for Tex Live should be installed through the apt package manager as well (using `tlmgr` leads to problems due to different versions)

## Installing LyX, a $\LaTeX$ Alternative

### Get LyX

LyX is an open source document processor based on Latex. [Download LyX](https://www.lyx.org/Download).

### Making LyX Available on the Command Prompt

You have just installed LyX and may need to access LyX from the command line.

#### Windows users
For you to be able to use LyX from the command prompt, follow the steps below.

{{% warning %}}
**Making LyX available via the PATH settings on Windows**

We need to update our PATH settings; these settings are a set of directories that Windows uses to "look up" software to startup.

- Right-click on Computer.
- Go to "Properties" and select the tab "Advanced System settings".
- Choose "Environment Variables" and select `Path` from the list of system variables.
- Choose `Edit`.
	- Environment variable name: LYX_BIN
	- **Windows 7 and 8 machines:**
		If you chose the default installation directory, copy and paste the following string without spaces at the start or end:

       `c:\Program Files (x86)\Lyx`

	- **Windows 10 machines:**
		- Click `New` and paste the following string:

       `c:\Program Files (x86)\Lyx`

		- Click on `OK` as often as needed.
{{% /warning %}}

#### Mac users

For you to be able to use LyX from the command line, you have to add LyX to your environmental variables:

{{% warning %}}
**Making LyX available via the PATH settings on Mac**

- Open the Terminal.
- Type `nano ~/.bash_profile`.
- Add LyX to the environmental variables:
- Add `export LYX_BIN=/Applications/LyX.app/Contents/MacOS/lyx` to a new line.
- Save by pressing `Ctrl + O` and exit by pressing `Ctrl + X`.
- Relaunch the Terminal. Then type `source ~/.bash_profile` to bring the new .bash_profile into effect.
- Type `$LYX_BIN` to check availability. Remember to type the `$` before `LYX_BIN`.
{{% /warning %}}

<!--- Linux users not available yet
-->


### Check your Installation

To verify that LyX has been correctly installed and configured via your PATH settings,
open a **new** terminal interface and enter:

```bash
$LYX_BIN
```

followed by hitting the `Return` key.
