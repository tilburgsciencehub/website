---
title: "Set up Pandoc"
<<<<<<< HEAD
description: "Learn to set up and install Pandoc on windows, Linux, and Mac. Follow the tutorial to add Pandoc to path and to check the Pandoc version"
=======
description: "Learn to install Pandoc on Windows, Linux, and Mac. Follow the tutorial to add Pandoc to the path and to check the Pandoc version"
>>>>>>> master
keywords: "Pandoc, install, software, configuration, path, windows, pandoc version"
#date: 2020-11-11T22:02:51+05:30
draft: false
weight: 3
aliases:
  - /get/pandoc
  - /install/pandoc
---

<<<<<<< HEAD
## What is Pandoc 

Pandoc is an extremely useful 'swiss army knife' for converting between different types of markup languages from the command line. For example, it readily builds PDFs with latex, and markdown - both of which are heavily used in academic research.

<!--We do not actively address how to use Pandoc - but we will utilize it in some lessons where we produce PDF, Word or HTML output from plain text files.-->

## Installing Pandoc

### Linux

Open a terminal window and type

```bash
sudo apt install pandoc
```

to install pandoc from the command line

### Mac

Open a terminal window and type
```bash
brew install pandoc
```

to install pandoc from the command line

### Windows

Go to the [Pandoc Homepage](https://pandoc.org/) and follow the installation instructions for your operating system.


## Verify Your Installation

Verify your install by typing the following into a command line:

```bash
pandoc --version
```

The expected output starts with the following information:

```bash
pandoc 3.1.6.1

```
Ensure you have at least version 3.1.6 installed.

{{% warning %}}
Because we want Pandoc available from the command line (it is by default for Mac and Linux), we again need to update our PATH settings.

Right-click on Computer. Then go to "Properties" and select the tab "Advanced System Settings". Choose "Environment Variables" and select `Path` from the list of system variables.

Check whether the following path has been added:

        ;C:\Users\username\AppData\Local\Pandoc

**Windows 7 or 8 machines:**
If it has not been, and you accepted all defaults during your installation, and didn't have any other non-default setting prior to starting this guide, copy and paste the following string without spaces at the start or end, updating the `username`:

        ;C:\Users\username\AppData\Local\Pandoc

**Windows 10 machines:**
If it has not been added, Click `New` and paste the following string, updating the username:

        C:\Users\username\AppData\Local\Pandoc

Click OK as often as needed.

After you have done this, open a **new** terminal and try and verify your install.
{{% /warning %}}
=======
## Overview 

[Pandoc](https://www.pandoc.org/) is an extremely useful "Swiss army knife" for converting between different types of markup languages from the command line. For example, it readily builds PDFs with LaTeX and Markdown - both of which are heavily used in academic research. This guide will help you install Pandoc. To get started using it, refer to [this topic](/pandoc)!

## How to install Pandoc

### Windows

- Visit the [Pandoc installing page](https://www.pandoc.org/installing.html) and click on the blue "Download the latest installer" button. 

- Choose the file ending with `windows-x86_64.msi` to download the Windows Installer package. 
- Click on the installer in your download history. A set-up wizard will appear.
- Follow the wizard; accept the conditions and click Install. 
- Click Finish to close the setup wizard once the installation is complete. 

To make Pandoc available from the command line, we need to update our PATH settings:

- Right-click on "Computer", select "Properties" and go to "Advanced System Settings".
- Click on "Environment Variables" and find `Path` in the list of system variables.

Check if the following path is added:

```bash
;C:\Users\username\AppData\Local\Pandoc
```

*For Windows 7 or 8:*
If the path is not added, and you used default settings during installation, add the following string, replacing `username` with your actual username:

```bash
;C:\Users\username\AppData\Local\Pandoc
```

*For Windows 10:*

If the path is not added, click `New` and paste the following string, replacing `username` with your actual username:

```bash
C:\Users\username\AppData\Local\Pandoc
```

Click OK as often as needed to save your changes.


### Mac

- Go to the [Pandoc installing page](https://www.pandoc.org/installing.html) and click on the blue "Download the latest installer" button. 
- Choose the file ending with `macOS.pkg` to download the macOS Installer package. 
- Navigate to the download folder and double-click the `.pkg` file to start the installer. 
- Follow the installation wizard, agree to the license agreement, and click Install.
- Once the installation is complete, click Close.

Alternatively, you can install Pandoc directly from the command line on a Mac device. Open a terminal window and type:

{{% codeblock %}}
```bash
brew install pandoc
```
{{% /codeblock %}}


### Linux

To install Pandoc from the command line, open a terminal window and type:

{{% codeblock %}}
```bash
sudo apt install pandoc
```
{{% /codeblock %}}


## Verify your installation

To ensure Pandoc is installed correctly, open a new terminal and type:


{{% codeblock %}}
```bash
pandoc --version
```
{{% /codeblock %}}

The output should start with the version information, such as:

```bash
pandoc 3.2

```
Make sure you have at least version 3.2 installed. 
If so, you're all set!


## Other installation methods

For instructions on running Pandoc in a Docker container or with GitHub Actions, visit the [Pandoc installing page](https://www.pandoc.org/installing.html).


{{% summary %}}

Now that Pandoc is installed, you can start using it. Continue with this [topic](/pandoc) to learn how to begin working with Pandoc!

{{% /summary %}}



>>>>>>> master
