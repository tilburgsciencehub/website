---
title: "Remove Sensitive or Large Files From Your Repository"
description: "Accidentally committed large data sets or sensitive information to your repository? Here is how to entirely remove files from your repository's history!"
keywords: "git, github, versioning, remove, sensitive, password, large, project, version, control, file, directory"
weight: 8
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /remove/commited-files
  - /remove/sensitive-information
  - /remove/large-files
  - /building-blocks/collaborate-and-share-your-work/use-github/remove-files.md
---

## Overview
Your Git repository will eventually become the long-term memory of your project, and you may decide to make the repository public so others can learn from or use your work.
Versioning is a powerful and good tool to use, unless...
- you accidentally stored sensitive information in your source code that you really do not want to be out in the public (e.g., API credentials, passwords),
- you accidentally stored files (e.g., large data sets, images) in your repository, that you cannot upload to GitHub (and hence can't synchronize your repository anymore)

In such situations, the good news is that solutions exist! These solutions will be discussed in this building block: 
- Undo your last commit
- Entirely remove files

## Undo your last commit

If you have *just* committed sensitive content, simply roll back to the last version of your repository using:

{{% codeblock %}}
```bash
git reset --soft HEAD~1
```
{{% /codeblock %}}

## Entirely remove files

When sensitive data has been committed, follow these steps to wipe out the file and its commits: 

1. Open Git Bash in your repository's main directory.
2. In Git Bash, enter the following command:

{{% codeblock %}}
```bash
git filter-branch --index-filter 'git rm --cached --ignore-unmatch file_to_remove' --prune-empty -- --all
```
{{% /codeblock %}}

Replace `file_to_remove` by the path and file name of the file that you want to wipe out.

3. If the command doesn't work, verify you have used the correct file name and path. Typically, the file name and path are indicated in a Git error message when trying to push or pull. Thanks to [StackOverflow](https://stackoverflow.com/questions/10676128/remove-deleted-files-from-git-history) for this solution!

Check out the GitHub manuals for a [step-by-step guide](https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository)! Alternatively, use [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/), a convenient tool to remove unwanted files from your project.

{{% tip %}}
__Proactive prevention of committing specific files__

Avoid future mishaps by learning to [exclude files from versioning](../git-ignore).

{{% /tip %}}

{{% summary %}}
This guide presents effective strategies for removing sensitive data or unwanted files: 
- Undoing your last commit 
- Entirely eliminating files

By applying these techniques, you can navigate the challenges of preserving the integrity of your repository while sharing your work with the wider community.
{{% /summary %}}

