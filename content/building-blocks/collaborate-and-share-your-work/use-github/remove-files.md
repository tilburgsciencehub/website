---
title: "Remove Sensitive or Large Files From Your Repository"
description: "Accidentally committed large data sets or sensitive information to your repository? Here is how to entirely remove files from your repository's history!"
keywords: "git, github, versioning, remove, sensitive, password"
weight: 8
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /remove/commited-files
  - /remove/sensitive-information
  - /remove/large-files
  - /building-blocks/collaborate-and-share-your-work/use-github/remove-files.md
---

Git will eventually become the long-term memory of your project, and you may decide to make the repository public so others can learn from or use your work.

Normally, versioning really is a good thing, unless...
- you accidentally stored sensitive information in your source code that you really do not want to be out in the public (e.g., API credentials, passwords),
- you accidentally stored files (e.g., large data sets, images) in your repository, that you cannot upload to GitHub (and hence can't synchronize your repository anymore)

Luckily, there are ways out!

## Simply undo your last commit

If you have *just* committed the file that you shouldn't have committed, simply roll back to the last version of your repository.

`git reset --soft HEAD~1`

## Entirely remove files

If you have committed sensitive data to your Git repository, use thef following resources to remove the file and all its previously issued commits.

1. Navigate to your repository (i.e., the main directory of your repository), and open Git Bash.
2. In Git Bash, type `git filter-branch --index-filter 'git rm --cached --ignore-unmatch file_to_remove' --prune-empty -- --all`. Replace `file_to_remove` by the path and file name of the file that you want to wipe out.
3. If the command doesn't work, verify you have used the correct file name and path name. Typically, the file name and path are indicated in a Git error message when trying to push or pull. Thanks to [StackOverflow](https://stackoverflow.com/questions/10676128/remove-deleted-files-from-git-history) for this solution!

Check out the GitHub manuals for a [step-by-step guide](https://docs.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository)! Alternatively, use [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/), a convenient tool to remove unwanted files from your project.

{{% tip %}}
__Prevent committing specific files in the first place__

Had to deal with removing sensitive information or unwanted files, and want to avoid making the same mistake twice?

Learn how to [exclude files from versioning](../git-ignore).

{{% /tip %}}
