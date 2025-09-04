---
type: "hugo-tutorial"
title: "(Part 2) Install Hugo Extended on Windows using winget"
description: "Instructions for installing Hugo Extended on Windows using winget"
draft: false
weight: 2
date: 2025-07-07
author: "Harold Miesen"
---

## (Part 2) Install Hugo Extended on Windows using winget

Use winget to easily install and update the latest system-wide version of Hugo on Windows
via the command line. __**Winget**__ (Windows Package Manager) is Microsoft’s official
command-line tool for installing software on Windows, much like brew on macOS or apt on Linux.

### Step 1: Open PowerShell

Search for PowerShell in the Start Menu and open it.

### Step 2: Install Git (if not already installed)

```
winget install --id Git.Git -e --source winget
```

> If `git` is not yet installed, the command above will install it.

Check Git installation:
```
git --version
```

You should see a version number if Git is correctly installed.

### Step 3: Install Hugo Extended

Uninstall any previous Hugo version first to avoid conflicts.

```
winget uninstall Hugo.Hugo.Extended
```

After removal, check:

```
hugo version
```

If Hugo has been succesfully removed from your system, you should see the following error
message: `hugo : The term 'hugo' is not recognized...`. 

Next, install Hugo Extended by means of the following command:

```
winget install Hugo.Hugo.Extended
```
### Step 4: Confirm Installation

After install, check:

```
hugo version
```

You should see a version number if Hugo is correctly installed.
E.g., `hugo v0.148.2-40c3d8233d4b123eff74725e5766fc6272f0a84d+extended linux/amd64 
BuildDate=...

Look for `+extended` in the output.
Hugo Extended is now installed on Windows!

---

Done installing? Proceed to the 
[Launch Site](../4-launch-site/) page
or go back to
[Hugo Tutorial: Start Here](../1-index/).
