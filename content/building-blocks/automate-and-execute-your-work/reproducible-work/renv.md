---
title: "Package Management for R: renv"
description: "How to work with renv R package to manage project environments"
keywords: "renv, package, environment, management, R, Packrat, alternative"
date: 2023-04-29
weight: 3
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /manage/packages
  - /use/renv
  - /replace/packrat
---

## Environment management for R projects with renv

{{% warning %}}

[Packrat](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/packrat/) is now deprecated. To switch from Packrat to renv, use `renv::migrate()` to migrate projects.

{{% /warning %}}

Although it comes as a replacement for the `Packrat` package, `renv` still has the same characteristics: it is **isolated**, **portable** and **reproducible**. It is a dependency management tool for R projects, facilitating the reproducibility of environments across computers or platforms. 


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
After initializing the project, we can install or remove packages on it:

{{% codeblock %}}
```R
#install packages
install.packages()

#remove packages
remove.packages()

```
{{% /codeblock %}}

### 4. Save state of project in `lockfile`
After configuring the project, we should save the configuration into a `lockfile`, in which all packages versions are recorded. 

{{% codeblock %}}
```R
renv::snapshot()

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

