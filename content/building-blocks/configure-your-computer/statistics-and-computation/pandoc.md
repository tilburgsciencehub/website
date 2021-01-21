---
title: "Pandoc"
description: "Pandoc is an extremely useful 'swiss army knife' for converting between different types of markup languages from the command line."
keywords: "Pandoc, installation, software, configuration"
date: 2020-11-11T22:02:51+05:30
draft: false
weight: 7
---

Pandoc is an extremely useful 'swiss army knife' for converting between different types of markup languages from the command line.
For example, it readily builds PDFs with latex, and markdown - both of which are heavily used in academic research.

<!--We do not actively address how to use Pandoc - but we will utilize it in some lessons where we produce PDF, Word or HTML output from plain text files.-->

## Linux

Open a terminal window and type

```bash
sudo apt install pandoc
```

 to install pandoc from the command line

## Mac

Open a terminal window and type
```bash
brew install pandoc
```

to install pandoc from the command line

## Windows

Go to the [Pandoc Homepage](https://pandoc.org/) and follow the installation instructions for your operating system.


## Verify Your Install

Verify your install by typing the following into a command line:

```bash
pandoc --version
```

The expected output starts with the following information:

```bash
pandoc 1.19.2.1

```
Ensure you have at least version 1.15.1 installed.

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
