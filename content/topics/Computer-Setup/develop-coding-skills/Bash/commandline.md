---
title: "Set up Command Line Tools"
description: "A command-line interface or command language interpreter (CLI), also known as a terminal, is a means of interacting with a computer program."
keywords: "CLI, terminal, Homebrew, brew, cygwin, command"
weight: 2
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /configure/cli
---

## What are Command Line Tools

A *command-line* interface or command language interpreter (CLI), also known as a terminal, is a means of interacting with a computer program where the user issues commands to the program in the form of successive lines of text (command lines).

Throughout the course, we will emphasize the use of the terminal and executing commands within it as our modus operandi. Command line tools are software programs controlled through text-based commands entered in a terminal. They perform tasks like file manipulation, system administration, and data processing. These tools offer efficiency, flexibility, and scripting capabilities, making them valuable for tasks across programming, system management, and data analysis, providing direct access to a computer's operations.

## Installation

### Windows Users

We will use the recently-launched Windows Subsytem for Linux (WSL) because it enables us to use Bash on Windows and to run Windows and Linux commands at the same time within a single, unified command prompt. WSL is useful as a command line tool because it offers greater functionality than the standard Windows command prompt and facilitates the use of Linux and its distributions (e.g., Ubuntu) on a Windows machine. 

We can install the features necessary to run WSL by running the following command in the Windows command prompt or PowerShell. Make sure to run the Windows command prompt or PowerShell **as administrator**. 

{{% codeblock %}}
```powershell
wsl --install
```
{{% /codeblock %}}

After running this command, we have to wait until the Linux distribution is fully installed. By default, running the above command installs the Ubuntu distribution. We can install additional distributions by running the following command:

{{% codeblock %}}
```powershell
wsl --install <Distribution Name>
```
{{% /codeblock %}}

{{% warning %}}
If the command prompt returns an error stating that the syntax of the command is incorrect, try using "wsl --install Distribution Name" instead, without the <> operators. 
{{% /warning %}}

{{% tip %}}
In order to check which Linux distributions are available, we can run the following command:
{{% codeblock %}}
```powershell
wsl --list --online
```
{{% /codeblock %}}
{{% /tip %}}

After installation is complete, we will have to create a Linux username and password. Once we have done that, we can restart our machine and start using WSL as our unified command line tool. Note that, by default, this procedure installs WSL 2, the most recent version of WSL. 

### Mac Users

A command line interface comes already installed with MacOS.

You will need to install some other software from the terminal throughout the course, so it will be useful to install some additional "command line tools" now:

*   First we want to install X-code command line tools. Open a terminal by searching for it with spotlight, `cmd + spacebar` then type terminal and press `Return` when it appears. Then, copy and paste the following

```
xcode-select --install
```

If you get an answer that the command line tools are already installed, you can just continue to the next step.

* Second, install [Homebrew](https://brew.sh) by opening a terminal and pasting the following command:

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/homebrew/install/master/install)"
```

* To verify that Homebrew is installed correctly, enter the following into your terminal
```
brew doctor
```
And you should see the following output
```
Your system is ready to brew
```

* Now we can use Homebrew to easily install the software. To use the current R version 3.5.1, we want to make sure you have some basic system tools that some packages require. Let's (re)install them real quick. First `libxml2`:

```
brew reinstall libxml2
```

If you system tells you that it is not yet installed, then try  ```brew install libxml2``` instead.

We also want to link this so that the terminal finds it later:

```
echo 'export PATH="/usr/local/opt/libxml2/bin:$PATH"' >> ~/.bash_profile
```

* Second, we also need `openssl`:

```
brew reinstall openssl
```
Again, if it is already installed, then use ``` brew install openssl``` instead.

Again, we need it to link to the terminal:

```
echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile
```



* Finally, we need `libgit2`:

```
brew install libgit2
```

If the terminal tells you it is not yet installed, then go for ```brew reinstall libgit2```

### Linux Users

To use the current R version, we need to install some system tools. For this open a terminal session with `Ctrl` + `Alt` + `T`.

* Now copy the following command into the terminal and press `Enter`:

```
  sudo apt-get install libcurl4-gnutls-dev librtmp-dev
```

* After the installation succeeded successfully repeat this one-by-one with the following two other commands:

```
sudo apt-get install libxml2-dev
sudo apt-get install libssl-dev
```
