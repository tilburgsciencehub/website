---
title: "Package Management for R: renv"
description: "How to work with renv R package to manage project environments"
keywords: "renv, package, environment, management, R, Packrat, alternative"
date: 2023-04-29
weight: 2
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /manage/packages
  - /use/renv
  - /replace/packrat
---

## Environment management for R projects with renv

`renv` is a dependency management tool for R projects, facilitating the reproducibility of environments across computers or platforms.
As a package management tool, `renv` helps to make projects: 
- **isolated** : installing or updating a certain package in one project doesn't affect other packages from other projects
- **portable** : projects can easily be transferred to different devices
- **reproducible** : `renv` makes it easy to reproduce projects by recording all package versions of each project


## Workflow

### 1. Install `renv`
First thing we need to do is to install the `renv` package.

{{% codeblock %}}
```R
install.packages("renv")

```

{{% /codeblock %}}


### 2. Initialize new project environment
Then we can move to initializing the local environment of the project. We can do that with the following command:

{{% codeblock %}}
```R
renv::init() 

```
{{% /codeblock %}}

### 3. Install/remove packages
After initializing the project, we can install or remove packages from it:

{{% codeblock %}}
```R
#install packages
install.packages()
#or
renv::install()

#remove packages
remove.packages()
#or
renv::remove()

```
{{% /codeblock %}}

### 4. Save library of project in `lockfile`
After configuring the project, we should save the configuration into a `lockfile`, in which all packages versions are recorded. 

{{% codeblock %}}
```R
renv::snapshot()

```
{{% /codeblock %}}

We can also check the status of the library with:
{{% codeblock %}}
```R
renv::status()

```
{{% /codeblock %}}


If we continue to make changes to the packages after making the `lockfile`, but then we would like revert to the previous state (as recorded in the `lockfile`), we can use:

{{% codeblock %}}
```R
renv::restore()

```
{{% /codeblock %}}

### Directory overview

After running all the commands above, the directory in which the project was created should contain the following files:

<p align = "center">
<img src = "../img/directory.png" width="500">
</p>

| File | Usage |
| ---  |  ---  |
|.`Rprofile` | File that activates renv for the new R sessions |
| `renv.lock` | The created lockfile containing all packages and versions |
| `renv/activate.R` | Activation script run by `.Rprofile` |
| `renv/library` | Private project library |
| `renv/settings.json` | Project settings |

## From packrat to renv

{{% warning %}}

[Packrat](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/packrat/) is now deprecated. To switch from Packrat to renv, use `renv::migrate()` to migrate projects.

{{% /warning %}}

## Why renv is better than groundhog

`groundhog` is another R package that makes projects reproducible. However, it doesn't work by keeping records of packages versions necessary for each project, like `renv` does. Instead you have to manually load libraries with the option of giving a date on when the wanted version was available. Thus, `renv` has more advantages because it can load all necessary packages in one go, without having to manually input the dates certain versions were available on.



