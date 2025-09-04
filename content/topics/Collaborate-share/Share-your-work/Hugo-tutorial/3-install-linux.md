---
type: "hugo-tutorial"
title: "(Part 2) Install Hugo Extended on Linux using snap"
description: "Install Hugo on a Linux environment using snap"
draft: false
weight: 3
date: 2025-07-07
author: "Harold Miesen"
---

## (Part 2) Install Hugo Extended on Linux using snap

Snap is a universal package manager developed by Canonical (the makers of Ubuntu). It allows you to
install software in isolated containers, which include all necessary dependencies—making it easy
to run the latest versions of applications across different Linux distributions.

Using snap to install Hugo ensures:

- You get the Extended version by default,
- Automatic updates,
- Fewer dependency issues across distros.

### Step 1: Update Your System

```
sudo apt update && sudo apt upgrade
```

### Step 2: Install Required Packages

```
sudo apt install git curl wget tar snapd
```

> If `git` is not yet installed, the command above will install it.
> `snapd` is the background service used to manage snap packages.

### Step 2.1: Verify Git Installation

```
git --version
```

You should see a version number if Git is correctly installed.

### Step 3: Install Hugo Extended via Snap

```
sudo snap install hugo --channel=extended --classic
```

> The `--channel=extended` flag ensures you get the Hugo Extended version (required for SCSS/SASS).
> The `--classic` flag gives Hugo permission to access the full system, which is necessary for many
real-world use cases.

### Step 4: Verify Installation

```
hugo version
```

You should see output like:

```
hugo v0.124.1+extended linux/amd64 BuildDate=...
```

Look for `+extended` in the output.
Hugo Extended is now installed on Linux!

---

Done installing? Proceed to the 
[Launch Site](../4-launch-site/) page or go back
 to [Hugo Tutorial: Start Here](../1-index/).
