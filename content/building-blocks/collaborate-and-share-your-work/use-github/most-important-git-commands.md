---
title: "The Most Important Git Commands You Should Know"
description: "A quick recap of the essential Git commands you will be using everyday."
keywords: "git, commands, important, essential, cheat"
#date: 2021-02-08
draft: false
weight: 2
aliases:
  - /use/git-bash
  - /use/git-commands
  - /learn/git-commands
  - /learn/git-bash
---

## Overview

This is a summary of the most important Git commands that you can use in Git Bash. If you're not so familiar with working in the command prompt/terminal, you could also try to check out Git Desktop or Git GUI, which provides a graphical user interface for performing the Git workflow.

## Code

Clone ("download") the repository to your computer.

{{% codeblock %}}
```bash
git clone <URL>
```
{{% /codeblock %}}

{{% warning %}}
Do not clone a repository into another repository!
{{% /warning %}}

---

Check which files/directories have changed since your last commit.

{{% codeblock %}}
```bash
git status
```
{{% /codeblock %}}

---

Add specified file(s) to the staging area, so that any changes can eventually be committed.

{{% codeblock %}}
```bash
git add <file_name>
```
{{% /codeblock %}}

---

Commit staged changes to the version history of your repository. It's good practice to use a clear & concise commit message  ("note to your future self and others") which shows up prominently on your repository at GitHub.com.

{{% codeblock %}}
```bash
git commit -m "<your_message>"
```
{{% /codeblock %}}

---

Push any changes you have done to the repository on your computer to the specified branch of the remote repository (e.g., at GitHub.com).

{{% codeblock %}}
```bash
git push origin <branch_name>
```
{{% /codeblock %}}

---

View your commit history (i.e., a list of commit IDs and your commit messages.

{{% codeblock %}}
```bash
git log
```
{{% /codeblock %}}


## Advanced use cases

### Add all files to the staging area

To add all files that have been changed to the staging area (to eventually commit them), use

{{% codeblock %}}
```bash
git add .
```
{{% /codeblock %}}

That way, you don't have to mention files individually. But beware to not accidentally version files that must not be versioned (e.g., datasets).

### Ignore files from versioning

You can create a `.gitignore` file (e.g., in the root directory of your repository) to tell Git to stop paying attention to files you don't want to version (e.g., datasets, operation-specific files like Mac's `.DS_Store` or R's `.RHistory`.

For example, if you save the snippet below in a file called `.gitignore`, any content in the `my_passwords` folder and any `.csv` files will be ignored - even when using `git add .`!

  ```
  my_passwords/*
  *.csv
  ```

---

### Undo previous commits

It happens to all of us - we sometimes commit stuff that we didn't mean to commit. That can be quite problematic, for example if you've accidentally committed a password. But even for less drastic cases, reverting "wrong" commits is good practice because it keeps your repository clean.

The snippet below undoes the last commit.

{{% codeblock %}}
```bash
git reset --soft HEAD~1
```
{{% /codeblock %}}

Alternatively, you can view the commit history with `git log`, and revert to *any* commit by referring to its unique id (which looks a bit like this: `0hf1u7x2`).

{{% codeblock %}}
```bash
git reset --hard <commit id>
```
{{% /codeblock %}}


## See also

* [Official GitHub Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [Oh Shit, Git!?! A collection of advanced and useful Git commands!](https://ohshitgit.com)
* [Version control on The Turing Way](https://the-turing-way.netlify.app/reproducible-research/vcs.html)
* [Version control at Software Carpentry](http://swcarpentry.github.io/git-novice/)
* [Installation guide for Git and GitHub](/building-blocks/configure-your-computer/statistics-and-computation/git/)
