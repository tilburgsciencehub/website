---
title: "Manage your R Packages with Packrat"
description: "Isolated, portable and reproducible dependency management system for R."
keywords: "packrat, R, package management, R environment, dependency management, RStudio, package, renv"
weight: 2
draft: false
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
- /reproduce/packrat
---

{{% warning %}}
**`Packrat` is now soft-deprecated** 

It is still maintained, but there will be no new development for it. An updated alternative would be `renv`. 
Do you want to learn about it? Visit [this building block](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/renv/)!
{{% /warning %}}

## Overview

Suppose you’re trying to run someone else’s codes and you are bombarded with package installation errors. It can be frustrating to guess what R packages are needed to be installed, right? Or, have you ever updated a package to get code in one of your projects to run, only to find that the updated package makes code in another project stop working?

With `packrat` you won't be worrying anymore. In this guide you will:

- Understand the benefits of using `packrat` for managing R package dependencies.
- Learn how to initialize, install, and manage packages using `packrat`.
- Grasp how to collaborate efficiently using `packrat` for consistent R environments.

## Get started with Packrat

`Packrat` is one of the most typical solutions to dependency issues. It is a dependency management system for R packages which is:

- **Isolated**: `Packrat` gives each project its own **private package library**, so installing a new or updated package for one project won’t affect other projects you may be working on. As a result, next time you start an R session in a `packrat` project directory, R will only look for packages in your private library and all changes to the packages are made in this private package.
- **Portable**: Easy to transfer your R projects from one machine to another, or even across platforms.
- **Reproducible**: `Packrat` saves the exact package version your project depends on, so those exact versions are installed always whenever you run the project anywhere.

## Install packrat

{{% codeblock %}}
```R
install.packages("packrat")

# Alternatively, you can also install the development version of Packrat with:

install.packages("devtools")
devtools::install_github("rstudio/packrat")
```
{{% /codeblock %}}

{{% warning %}}
You’ll also need to make sure your machine is able to build packages from source. See [Package Development Prerequisites](https://support.rstudio.com/hc/en-us/articles/200486498-Package-Development-Prerequisites#:~:text=Overview,building%20R%20manuals%20and%20vignettes.) for the tools needed for your operating system.
{{% /warning %}}

## Launch Packrat

Before starting to write the codes for your R project, initialize `packrat` by running `packrat::init("...")` and enter your project directory path inside the parantheses. If you already set the working directory to your desired project directory then simple run `packrat::init()`.
<p align = "center">
<img src = "../img/initialize.png" width="700">
<figcaption> If you'd have more packages, they'll be all displayed with their versions </figcaption>
</p>

Now, you’re in a `packrat` project which has its own private package library. Any packages installed from inside a `packrat` project are only available to that project and the ones installed outside of the project are not avilable to the project. This is basically the “isolation” feature of `packrat`.

Once you run this initialization code, you’ll see a `packrat` folder created in your project directory which contains the following files:
<p align = "center">
<img src = "../img/packrat_folder.png" width="550">
<figcaption> Packrat folder overview </figcaption>
</p>

- **`packrat/packrat.lock`:** This contains a list of the package versions that satisfy the dependencies. Note that this file should never by edited manually by the user!
- **`packrat/packrat.opts`:** This file contains project-specific packrat options and can be queried and set with `get_opts` and `set_opts`; see `?"packrat-options"` for more information.
- **`packrat/lib/`:** This is the private package library for the current project.
- **`packrat/src/`:** This folder contains the source packages of all the dependecies packrat has detected.
- **`.Rprofile`:** Instructs R to use the private package library when starting the project.
## Adding, removing, and updating packages

Simply install the packages as you normally would with `install.packages()` and these packages now get installed in your project’s private package library. Then, take a **snapshot** to save these changes to `packrat` by running:
{{% codeblock %}}
```R
# take snapshot of the packages installed
packrat::snapshot()
```
{{% /codeblock %}}
<p align = "center">
<img src = "../img/packrat_snapshot.png" width="700">
<figcaption> Save changes to packrat with a snapshot </figcaption>
</p>


Suppose you made some changes to your code and remove one of the libraries. When you re-run the snapshot command, `packrat` will remove the dependent packages that are no longer required to run the script. Thus, keeping the private `packrat` library up-to-date and tidy.

<p align = "center">
<img src = "../img/updated_snapshot.png" width="700">
<figcaption> Packrat proposes to remove no longer needed packages </figcaption>
</p>

## Restoring snapshot

So let’s say you are collaborating with a co-author/teammate on GitHub and you made changes to your R project and took snapshot of the packages **before** comitting the changes. Now, your collaborator fetches these changes by pulling the commits made to their local machine. They can check “status” which shows the differences between the project’s `packrat` dependencies, its private package library, and R scripts. Then they can “restore” the changes made.
{{% codeblock %}}
```R
# Check status
packrat::status()

# restore packages
packrat::restore()
```
{{% /codeblock %}}

Now, `packrat` installs all the dependencies and your collaborator’s private library looks just like yours did when you wrote the codes and they will be able to run all the codes smoothly.

## Cleaning up packages

As your project progresses, your package libraries may have outgrown and some of the packages installed may no longer be needed. `Packrat` can analyze your .R script files and filter packages that are needed depending on your codes and keep the package library tidy.
{{% codeblock %}}
```R
# View changes made since last snapshot
packrat::status()
# Remove unwanted packages
packrat::clean()
```
{{% /codeblock %}}

{{% tip%}}

**Use “Pacman” to load multiple packages in one go!**

One usually loads packages requires using the `library()` function but if you want to load multiple libraries, it gets a bit tedious. Pacman is a handy tool to load multiple packages with a single code snippet.

**Get started with Pacman:**

- **Step 1: Install pacman**
```R
install.packages("pacman")
```

- **Step 2: Load multiple packages with `p_load()`**

```R
pacman::p_load(dplyr,ggplot2,psych) # for example
```
{{%/tip%}}

Now you're all set to "Packrat-away" your package dependency issues!

{{%summary%}}

Packrat is a system for managing R package dependencies, ensuring consistent, isolated, and reproducible R environments.
The tool ensures that each project has its own private package library, making R projects portable and specific package versions are consistently installed across environments.

- **Package Management:**

Users can initialize, install, snapshot, restore, and clean packages using packrat, ensuring consistent versions of packages across different setups.
The private library keeps the specific versions of packages, which can be updated, and unused packages can be tidied up with specific commands.

- **Deprecation Warning:**

Packrat is soft-deprecated with no new developments planned, and users are advised to consider renv as an alternative for reproducible R environments.

{{%/summary%}}

## Additional Resources

- Packrat [step-by-step](https://rstudio.github.io/packrat/walkthrough.html)
- Most common [commands in Packrat](https://rstudio.github.io/packrat/commands.html)