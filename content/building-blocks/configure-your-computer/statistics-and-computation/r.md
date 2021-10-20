---
title: "Set up R and RStudio"
description: "R is a widely used language for statistical computing and graphics. Learn how to set it up on your computer."
keywords: "R, statistics, install, software, RStudio, PATH, learn R, get R, install R, setup"
#date: 2020-11-11T22:02:51+05:30
draft: false
#weight: 4
aliases:
  - /get/r
  - /install/r
---

## Installing R and RStudio

R is a language for statistical computing and graphics. R's use in the data science, econometrics and marketing communities has taken off over recent years and (at a bare minimum) should be considered as an open source replacement to Stata and SPSS.

### Installing R

Watch our YouTube video, in which we walk you through the setup on Windows.

{{< youtube xvw4Xha10qg iframe-video-margins >}}

Go to the [R website and download the most recent installer for your operating system](https://cran.r-project.org/).

- Windows users: choose the "base" subdirectory, then proceed to the download.
- Mac users: pick the release listed under "latest release" (pick the first, if it does not work, try the second).

We strongly suggest you to install R in the directory `C:\R\R-4.x.x\` rather than the default directory, `C:\Program Files\R\R-4.x.x\`.

### Installing RStudio

RStudio provides an easy to work with interface to R, and its format should feel familiar to other software environments like Stata or SPSS.

Download and install the **free version of RStudio** for your operating system from [here](https://www.rstudio.com/products/rstudio/download/).

## Verifying your Installation

Open RStudio from the start menu. After starting up, you should see the version corresponding to the one chosen on the website.

![Screenshot of R Studio](../r.png)

## Installing additional R Packages

You may need some additional libraries to work with R (e.g., some extra code that helps you to run your statistical analyses).

To install packages, open RStudio (if not already opened in the previous step). In the **console**, copy and paste the following:

```r
packages <- c("reshape2", "rmarkdown",
              "data.table", "Hmisc", "dplr",
              "stargazer", "knitr",
              "xtable","tidyverse",
              "RSQLite", "dbplyr")

install.packages(packages)
```

* If you are asked if you want to install packages that need compilation, type `n` followed by `Return`. Package compilation is likely to cause some errors, and you're all good going with packages that have already been compiled (typically, these are earlier versions of the package).
* Wait until all the packages have been installed and the you are done. It *may* take a while, so be patient

## Making R available on the command prompt

You have just installed R and RStudio, and learnt how to open RStudio from the start menu.
However, for many of the applications that follow, you are required to access R directly from the command prompt.
For example, this will enable you to run a series of R scripts in batch - which will significantly ease the burden of
building complex data workflows.

### Windows

For you to be able to use R from the command prompt, **Windows users** need to follow the steps below.
On Mac and Linux, R is available from the command line by default.

{{% warning %}}
**Making R available via the PATH settings on Windows.**

We need to update our PATH settings; these settings are a set of directories that Windows uses to "look up" software to startup.

- Open the settings for environment variables
    - Right-click on Computer.
  	- Go to "Properties" and select the tab "Advanced System settings".
  	- Choose "Environment Variables"
- Alternatively, type "environment variable" (Dutch: omgevingsvariabelen) in your Windows 10 search menu, and press Enter.

-  Select `Path` from the list of user variables. Choose `Edit`.
- **Windows 7 and 8 machines:**
	If you chose your installation directory to be C:\R\R-4.x.x\ during your installation (i.e., you did not use the default directory), copy and paste the following string without spaces at the start or end:

        `;C:\R\R-4.x.x\bin` (replace `4.x.x` by your actual version number!)

- **Windows 10 machines:**
	- Click `New` and paste the following string:

        `C:\R\R-4.x.x\bin` (replace `4.x.x` by your actual version number!)

	- Click on `OK` as often as needed.
{{% /warning %}}

{{% warning %}}

**Making R available via the PATH settings on Mac/Linux**

- Paste this command in your terminal: `nano ~/.bash_profile`
- Add the following two lines to it:

```
export R_HOME="/Library/Frameworks/R.framework/Resources"
export R_USER="/Library/Frameworks/R.framework/Resources"
```

{{% /warning %}}


{{% tip %}}
Keep in mind that after you add a new directory to the `PATH` variable, you need to start a *new* command prompt/terminal session to verify whether it worked. Sometimes it may take a couple of minutes until your PATH is recognized by the terminal.

{{% /tip %}}

**Now let's verify whether we can open R from the command prompt**

Open the command prompt/terminal and enter:

```bash
R --version
```

followed by pressing `Return`. The expected return begins with:

```bash
R version 4.x.x (20xx-xx-xx) -- "Some Funky Name"
```

Great job - you've managed to install R and configure it for use for data-intensive projects!

## Making R find packages on the command prompt
You can now access R directly from the command prompt. Nevertheless, code that runs perfectly on R Studio might return `Error in library(x)` on the command prompt.

Why is that? Sometimes, when running R from the command line, it doesn't find the packages that were installed in your *user library* paths.

**Solution:** Tell R where to find your user library.

{{% warning %}}
**Making R find your user library via the PATH settings on Windows.**

  - In RStudio, type `.libPaths()` and note the path to your user directory (typically the one that contains your user name).

  - Open the settings for environment variables

      - Right-click on Computer.

      - Go to "Properties" and select the tab "Advanced System settings".

      - Choose "Environment Variables"

  - Select `New` and name it **`R_LIBS_USER`**. `Variable value` is the path (that you previously noted) to your user directory.
  
  - Check whether `.libPaths()` only specifies your allocated user directory by typing `.libPaths()` into a new RStudio session. 
  
  	- If not, it is likely that you do not have Admin rights on your computer and R is installed elsewhere. Add another environment variable and name it **`R_LIBS_SITE`**. `Variable value` is the path that is listed second in the `.libPaths()` output.

Rather want to set `R_LIBS_USER` on a Mac or Linux machine? [Read more here](https://tilburgsciencehub.com/setup/environment).

{{% /warning %}}

**Verify that you can access your packages**

Close all command prompts/terminals. Open one again, type `R` to open R and then enter:

```bash
library(x)
```

Note that the command `library` requires you to specify the package name without quotation marks (e.g., `library(tidyverse)`, *not* `library("tidyverse")`).

Expect a return beginning with:
```bash
Attaching package: 'x'
```

Get an error message? Try reinstalling the package using `install.packages("name_of_the_page")`.
