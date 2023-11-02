---
title: "How to Automatically Install R Packages Used in a Project"
description: "Discover how to identify and auto-install the necessary R packages for a given project."
keywords: "R, R packages, automatic installation, project setup, code automation, dependency management, gist, automation"
#date: 2021-01-06T22:01:14+05:30
#updated: 2023-08-11
weight: 3
draft: false
aliases:
  - /install/r-packages
  - /setup/r-environment
---

## Learning goals

- Detect required packages from R scripts and R markdown files.
- Compare and install any missing packages from the CRAN repository.

## Overview

Configuring the essential R packages for your project can be time-consuming. Rather than installing each package individually, there is a simplified approach. You can identify every R package your project requires and automatically auto-install the ones missing from your system. 

All you need to do is save the code block shown below as an Rscript file in the root directory of your R project, as an example, let's name it *install_packages.R*. 

After that, you can either run it directly or execute the command: `Rscript install_packages.R` in the command line.

{{% warning %}}

Before proceeding, ensure that Rscript.exe is added to your system's PATH environment variable. This ensures that the Rscript command can be recognized and executed from any command prompt or terminal session. If you're unsure how to do this, consult the [R installation guide](https://cran.r-project.org/doc/manuals/r-release/R-admin.html) or your system's documentation on modifying PATH variables.

<p align = "center">
<img src = "../images/Rscript-not-recognized.png" width="500" style="border:1px solid black;">
<figcaption> Make sure Rscript.exe command is recognized</figcaption>
</p>
{{% /warning %}}

## Code

{{% codeblock %}}
```R
# Identify all source code files in (sub)folders
files <- list.files(pattern='[.](R|rmd)$', all.files=T, recursive=T, full.names = T, ignore.case=T)

# Extract the source code
code = unlist(sapply(files, scan, what = 'character', quiet = TRUE))

# Filter out only source code that starts with the library command
code <- code[grepl('^library', code, ignore.case=T)]
code <- gsub('^library[(]', '', code)
code <- gsub('[)]', '', code)
code <- gsub('^library$', '', code)
code <- gsub('["\']', '', code)  # Remove quotation marks

# Retain only unique package names and trim any white spaces
uniq_packages <- unique(trimws(code))

# Remove any "empty" package names
uniq_packages <- uniq_packages[!uniq_packages == '']

# Organize the list alphabetically
uniq_packages <- uniq_packages[order(uniq_packages)]

cat('Required packages: \n')
cat(paste0(uniq_packages, collapse= ', '), fill=T)
cat('\n\n\n')

# Fetch the list of currently installed packages
installed_packages <- installed.packages()[, 'Package']

# Check availability of packages for the current R version
available_packages <- rownames(available.packages(repos = 'https://cloud.r-project.org'))
to_be_installed <- setdiff(uniq_packages, intersect(uniq_packages, available_packages))

if (length(to_be_installed) == length(uniq_packages)) {
  cat('All packages need to be installed.\n')
} else if (length(to_be_installed) > 0) {
  cat('Some packages already exist; installing remaining packages.\n')
} else {
  cat('All packages installed already!\n')
}

# Install the missing packages
if (length(to_be_installed) > 0) {
  install.packages(to_be_installed, repos = 'https://cloud.r-project.org')
}

cat('\nDone!\n\n')
```
{{% /codeblock %}}

The output should look like this:

<p align = "center">
<img src = "../images/success-install-R-packages.png" width="300" style="border:1px solid black;">
<figcaption> Succesfull packages installation</figcaption>
</p>

## Additional Resources
- [Efficient ways to install and load R packages](https://statsandr.com/blog/an-efficient-way-to-install-and-load-r-packages/)
- [Auto-install R packages](https://gist.github.com/mtandon09/4a870bf4addbe46e784059bce0e5d8d6)
