---
title: "Exclude Files from Versioning"
description: "Not all files should be tracked (e.g., datasets, or sensitive information). Learn how to exclude them from versioning!"
keywords: "git, github, versioning, gitignore, remove, sensitive, version, control, data, file, files, directory"
weight: 4
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /learn/gitignore
  - /use/gitignore
---

# Overview

In this building block, you will learn how to exclude files and directories from versioning, optimizing your Git/GitHub workflow.

By default, Git/GitHub tracks *all* files you create. However, there are instances where you want to exclude specific files, such as:
- Large data files unfit for GitHub uploads
- Automatically generated code files (that hence do not need to be versioned)
- Sensitive passwords inadvertently stored in your code

## The file and directory exclusion technique

Luckily, Git offers a convenient way to __exclude files and directories from versioning__. Here's how you do it:

1. Create a new file in your project's root directory, and call it `.gitignore` (remember the initial `.`)

2. Open `.gitignore` and specify the files or directories to exclude. For instance, `**/DIRNAME` excludes any directory called `DIRNAME`, while `*pdf` excludes all PDF files.

3. Save `.gitignore` and run `git status` in your repository - the excluded files and directories won't show up anymore!

## Example

For inspiration, explore some [example `.gitignore` files](https://github.com/rgreminger/example-make-workflow/blob/master/.gitignore), or copy-paste the following to your own `.gitignore`:

{{% codeblock %}}
```txt
**/rbin/
**/raw/
*RData
*pdf
**/audit
**/input
**/output
**/temp
**/zip
*csv
*xlsx
*~*
*log
*.Rhistory
**/exports
**.ipynb_checkpoints
**__pycache__
*.log
slides/*.gz
slides/*.snm
slides/*.toc
slides/*.nav
slides/*.out
slides/*.aux
.RProfile
```
{{% /codeblock %}}

{{% summary %}}
Effortlessly enhance your version control by employing this file and directory exclusion technique: create a `.gitignore` file in which you specify the directories and files you would like to be excluded from versioning.
{{% /summary %}} 

