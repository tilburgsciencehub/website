---
title: "Archiving Repositories When They Are Done"
description: "Your repository is completed and no further work is expected? Keep it in good condition by making it ready to use again in the future if needed."
keywords: "git, github, mothball, archive, repository, requirements"
weight: 2
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /mothball
---

As projects evolve, there may come a time when the active development of a repository needs to be temporarily paused. This can occur for various reasons, such as shifting priorities, resource limitations, or the completion of a particular phase of work. However, even during such periods of dormancy, maintaining a repository's integrity and ensuring its readiness for potential future continuation is of paramount importance. This is where the concept of mothballing repositories comes into play.

## What are mothball repositories?

A *[mothballed](http://npic.orst.edu/images/mothballNN.gif)* repository refers to a repository where no further active work is expected but the repository is kept in a condition such that work can readily begin again.

## Requirements for mothballing a repository

When considering the mothballing of a repository, certain prerequisites must be met to effectively preserve the project's progress and facilitate seamless future engagement. The following requirements serve as essential steps to ensure a repository is suitably mothballed:

1. **Closure of issues**: All current issues have been closed with clear deliverables (if the issue was complete) or clear summaries of what was done / not done (if the issue was incomplete).

2. **Branch management**: All branches have been merged to master if they contain completed work that we would like to keep. Once relevant branches have been merged to master, all branches should be deleted.

3. **Data documentation**: Complete copies of all relevant data (both raw and cleaned) have been documented and stored somewhere safe and easily accessible.

4. **Mothball Page in the Repository Wiki**: A "Mothball" page has been added to the repository wiki with a summary of what we did in the project, why we decided to pause work, and the state we are leaving the project in.