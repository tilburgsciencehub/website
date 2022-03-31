---
title: "Packrat for R"
description: "Isolated, portable and reproducible dependency management system for R."
keywords: "packrat, R, package management system"
weight: 2

draft: false
aliases:
- /reproduce/packrat
---
# What is Packrat? Why use it?

Suppose you’re trying to run someone else’s codes and are bombarded with package installation errors, it can be frustrating to guess what R packages are needed to be installed, right? Or, have you ever updated a package to get code in one of your projects to run, only to find that the updated package makes code in another project stop working?

Packrat is the solution to such dependency issues. It is a dependency management system for R packages which is isolated, portable, and reproducible.

- **Isolated**: packrat gives each project its own **private package library** so installing a new or updated package for one project won’t affect other projects you may be working on. So, next time you start an R session in a packrat project directory, R will only look for packages in your private library and all changes to the packages are made in this private package.
- **Portable**: Easy to transfer your R projects from one machine to another, or even across platforms.
- **Reproducible**: Packrat saves the exact package version your project depends on, so those exact versions are installed always whenever you run the project anywhere.
# Get started with Packrat

## Install packrat

{{% codeblock %}}
```R
install.packages("packrat")

# Alternatively, you can also install the development version of Packrat with:
install.packages("devtools")
devtools::install_github("rstudio/packrat)
```
{{% /codeblock %}}

{{% warning %}}
You’ll also need to make sure your machine is able to build packages from source. See [Package Development Prerequisites](https://support.rstudio.com/hc/en-us/articles/200486498-Package-Development-Prerequisites?_ga=2.2309360.1597475521.1648472256-414577321.1648472256) for the tools needed for your operating system.
{{% /warning %}}

## Initialize Packrat

Before starting to write the codes for your R project, initialize packrat by running `packrat::init("...")` and enter your project directory path inside the parantheses.

Now, you’re in a Packrat project which has its own private package library. Any packages installed from inside a packrat project are only available to that project and the ones installed outside of the project are not avilable to the project. This is basically the “isolation” feature of Packrat.

Once you run this initialization code, you’ll see a “packrat” folder created in your project directory which contains the following files:

- **`packrat/packrat.lock`:** This contains a list of the package versions that satisfy the dependencies. Note that this file should never by edited manually by the user!
- **`packrat/packrat.opts`:** This file contains project-specific packrat options and can be queried and set with `get_opts` and `set_opts`; see `?"packrat-options"` for more information.
- **`packrat/lib/`:** This is the private package library for the current project.
- **`packrat/src/`:** This folder contains the source packages of all the dependecies packrat has detected.
- **`.Rprofile`:** Instructs R to use the private package library when starting the project.
## Adding, removing, and updating packages

Simply install the packages as you normally would with `install.packages()` and these packages now get installed in your project’s private package library. Then, take a **snapshot** to save these changes to Packrat by running:
{{% codeblock %}}
```R
# take snapshot of the packages installed
packrat::snapshot()
```
{{% /codeblock %}}
## Restoring snapshot

So let’s say you are collaborating with a co-author/teammate on github and you made changes to your R project and took snapshot of the packages BEFORE comitting the changes. Now your collaborator fetches these changes by pulling the commits made to their local machine. They can check “status” which shows the differences between the project’s packrat dependencies, its private package library, and R scripts. Then they can “restore” the changes made.
{{% codeblock %}}
```R
# Check status
packrat::status()

# restore packages
packrat::restore()
```
{{% /codeblock %}}

Now, packrat installs all the dependencies and your collaborator’s private library looks just like yours did when you wrote the codes and they will be able to run all the codes smoothly.

## Cleaning up packages

As your project progresses, your package libraries may have outgrown and some of the packages installed may no longer be needed. Packrat can analyze your .R script files and filter packages that are needed depending on your codes and keep the package library tidy.
{{% codeblock %}}
```R
# View changes made since last snapshot
packrat::status()
# Remove unwanted packages
packrat::clean()
```
{{% /codeblock %}}

{{% tip%}}

# Use “Pacman” to load multiple packages in one go!

# What is Pacman? Why use it?

One usually loads packages requires using the `library()` function but if you want to load multiple libraries, it gets a bit tedious.

# Get started with Pacman

## Step 1: Install packman
```R
install.packages("pacman")
```

## Step 2: Load multiple packages with p_load()

```R
pacman::p_load(dplyr,ggplot2,psych) # example
```
{{%/tip%}}

Now you're all set to "Packrat-away" your package dependency issues!
