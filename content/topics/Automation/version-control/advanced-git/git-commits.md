---
title: "Best Practices for Git Commits"
description: "A guide to writing good Git commit messages; how large should commits be; basic rules and formatting guidelines for git commits"
keywords: "git, commits, best, practices, basic, rules, format, messages, commit, github"
date: 2023-04-23
weight: 5
author: "Ana Bianca Luca"
authorlink: "https://tilburgsciencehub.com/contributors/anabiancaluca/"
aliases:
  - /write/commits
  - /best/practices
  - /formatting/guidelines

---

## Overview

When collaborating on projects, it is important to have conventions for making Git commits to ensure consistency in the way of working. In this topic, we outline some of the most common best practices for Git commits. In the end, we will be able to answer the questions:

- How large should a commit be? 
- How often should we make a commit? 
- How to write better commit messages?


### 1. Relate every commit to a specific change

Each commit should correspond to an issue or branch. Thus, if there are two different issues to be solved, each of them should have a commit. This way, smaller and specific commits are easier to follow and make the progress easier to track.

### 2. Commit often

It is better to commit small and frequent changes, than piling up more tasks and committing them rarely. But remember to always relate them to an issue or branch.


### 3. Commit only completed changes

Although it is good practice to make often and rather small commits, they should always contain completed tasks. 


### 4. Write meaningful commit messages

- The message can have a short summary and a description - in general, the summary should be less than 50 characters; the summary should be separated from the description with an empty line.
- Keep it short - stick to the main idea.
- Use the imperative of the present tense - e.g. "fix", "change".
- The message should answer these questions - What was the reason for the change? How has it changed?

### 5. Check changes before committing

Make sure to carefully test or check the implemented changes before making a commit. This avoids complications and more future work.



{{% summary %}}

- Link every commit to an issue or branch.
- Commit often but only completed changes.
- Verify changes before committing.
- Write concise commit messages in the imperative present tense.

{{% /summary %}}
