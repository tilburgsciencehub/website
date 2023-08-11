---
title: "How to Automatically Install R Packages Used in a Project"
description: "Discover how to identify and auto-install the necessary R packages for a given project."
keywords: "R, R packages, automatic installation, project setup, code automation, dependency management, find, gist"
#date: 2021-01-06T22:01:14+05:30
weight: 3
draft: false
aliases:
  - /install/r-packages
  - /setup/r-environment
---

## Overview

You can use the following code to easily find all the the R packages used in a project, and automatically install the uninstalled ones on your machine.

Put this script in the root directory of your R project, and either source it or run it from the command line: ```> Rscript install_packages.R```

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
