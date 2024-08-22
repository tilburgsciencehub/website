---
title: "Set up R and RStudio"
description: "Learn how to install R and RStudio on Windows, Linux, or Mac. Follow this tutorial on setting up RStudio and adding R to the Windows PATH."
keywords: "R, RStudio, statistics, install, software, RStudio, PATH, learn R, get R, install R, setup, windows"
#date: 2020-11-11T22:02:51+05:30
draft: false
weight: 1
aliases:
  - /get/r
  - /install/r
  - /topics/other-category/implement-an-efficient-and-reproducible-workflow/setup/r.md
---

## Overview

R is a language for statistical computing and graphics. R has become increasingly popular in the data science, econometrics, and marketing communities in recent years and should be considered at least as a open-source alternative to [Stata](/topics/computer-setup/software-installation/stata/getting-started-with-stata/) and SPSS.

This setup guide includes:

- Installing R
- Installing RStudio
- Installing additional R packages
- Using R in the command prompt
- Finding R packages in the command prompt 

## Installing R

Watch our YouTube video, where we walk you through the setup on Windows.

{{< youtube xvw4Xha10qg iframe-video-margins >}}

### Instructions

- Go to the [R website](https://cran.r-project.org/) and download the most recent installer for your operating system.
  - *Windows users*: Choose the "base" subdirectory, then proceed to the download.
  - *Mac users*: Pick the release listed under "latest release" (if the first doesn't work, try the second).

{{% tip %}}
We strongly suggest installing R in the `C:\R\R-4.x.x\` directory rather than the default directory, `C:\Program Files\R\R-4.x.x\`.
{{% /tip %}}


## Installing RStudio

RStudio provides an easy-to-use interface for R and should feel familiar to users of other software environments like Stata or SPSS. Download and install the *free version of RStudio* for your operating system from [RStudio website](https://www.rstudio.com/products/rstudio/download/).

### Verifying the RStudio installation

Open RStudio from the start menu. You should see the version corresponding to the one chosen on the website.

![Screenshot of R Studio](../images/r.png)

## Installing additional R Packages

You may need additional packages to work with R, such as extra code to help run your statistical analyses. To install packages, open RStudio (if not already open). In the console, copy and paste the following:

{{% codeblock %}}
```R
packages <- c("reshape2", "rmarkdown",
              "data.table", "Hmisc", "dplr",
              "stargazer", "knitr",
              "xtable","tidyverse",
              "RSQLite", "dbplyr")

install.packages(packages)
```
{{% /codeblock %}}

Wait until all the packages have been installed. It may take a while.

If asked whether you want to install packages that need compilation, type `n` followed by `Return`. Package compilation might cause errors, and it's fine to use pre-compiled versions (typically, these are earlier versions of the package).


{{% tip %}}

Check out these additional resources:

- Discover how to automatically install necessary R packages with this [code snippet](/topics/automation/replicability/package-management/auto-install-r-packages/).

- Learn to efficiently manage your R packages using Packrat with [this guide](/topics/automation/replicability/package-management/packrat/)

{{% /tip %}}


## Using R in the command prompt

You have just installed R and RStudio and learned to open RStudio from the start menu. However, many applications require accessing R directly from the command prompt. For example, this enables you to run a series of R scripts in batch mode, easing the process of building complex data workflows.

### Windows Users

To use R from the command prompt, *Windows users* must make R available via PATH settings. (On Mac and Linux, R is available from the command line by default.) Follow these steps to update your PATH settings: 

{{% tip %}}

*Making R available via PATH settings Windows*

PATH settings are a set of directories that Windows uses to "look up" software to start.

1. Open the settings for environment variables:
    - Right-click on Computer.
  	- Go to "Properties" and select the "Advanced System Settings" tab.
  	- Choose "Environment Variables"
    - Alternatively, type "environment variable" (Dutch: *omgevingsvariabelen*) in your Windows 10 search menu, and press Enter.

2. Select `Path` from the list of user variables and choose `Edit`.
- *Windows 7 and 8 machines:* If you chose to install R in the directory `C:\R\R-4.x.x\` (i.e., not the default directory), copy and paste the following string without spaces at the start or end: `;C:\R\R-4.x.x\bin` (replace `4.x.x` by your actual version number!)

- *Windows 10 machines:*
	- Click `New` and paste the following string: `C:\R\R-4.x.x\bin` (replace `4.x.x` with your actual version number!)
	- Click on `OK` as often as needed.

*Making R available via PATH settings on Mac/Linux*

- Paste this command in your terminal: `nano ~/.bash_profile`
- Add the following two lines:

```
export R_HOME="/Library/Frameworks/R.framework/Resources"
export R_USER="/Library/Frameworks/R.framework/Resources"
```
{{% /tip %}}

*Verify whether we can open R from the command prompt*

Keep in mind that after you add a new directory to the `PATH` variable, you need to start a *new* command prompt/terminal session to verify whether it worked. Sometimes, it may take a few minutes for your PATH to be recognized by the terminal.

- Open the command prompt/terminal and enter:

{{% codeblock %}}
```bash
R --version
```
{{% /codeblock %}}


Then press `Return`. The expected output should begin with:

```bash
R version 4.x.x (20xx-xx-xx) -- "Some Funky Name"
```

Great job! You've managed to install R and configure it for data-intensive projects.

## Finding R find packages in the command prompt

You can now access R directly from the command prompt. However, code that runs perfectly on RStudio might return `Error in library(x)` on the command prompt.

Why? Sometimes, when running R from the command line, it doesn't find the packages installed in your user library paths.

*Solution:* Tell R where to find your user library. Follow the instructions in the tip box.

{{% tip %}}
*Make R find your user library via the PATH settings on Windows.*

  1. In RStudio, type `.libPaths()` and note the path to your user directory (typically containing your username).

  2. Open the settings for environment variables

      - Right-click on Computer.
      - Go to "Properties" and select the "Advanced System settings" tab.
      - Choose "Environment Variables".

  3. Select `New` and name it `R_LIBS_USER`. The `Variable value` is the path (that you previously noted) to your user directory.
  
  4. Check whether `.libPaths()` only specifies your allocated user directory by typing `.libPaths()` into a new RStudio session. 
  	- If not, you may not have Admin rights on your computer, and R might be installed elsewhere. Add another environment variable and name it `R_LIBS_SITE`. The `Variable value` is the path listed second in the `.libPaths()` output.

Want to set `R_LIBS_USER` on a Mac or Linux machine? [Read more here](/topics/computer-setup/develop-coding-skills/bash/environment/).

{{% /tip %}}

*Verify that you can access your packages*

- Close all command prompts/terminals.
- Open one again, type `R` to open R, and then enter:

{{% codeblock %}}
```bash
library(x)
```
{{% /codeblock %}}


Note that the `library` command requires specifying the package name without quotation marks (e.g., `library(tidyverse)`, *not* `library("tidyverse")`).

Expect a return beginning with:

```bash
Attaching package: 'x'
```

If you get an error message, try reinstalling the package using `install.packages("name_of_the_page")`.

{{% summary %}}

Now you have R and RStudio set up, you can continue to [learn to code in R](/topics/computer-setup/software-installation/rstudio/getting-started-with-r-overview/).

{{% /summary %}}
