---
title: "Best Practices for Naming Git Branches "
description: "Learn the conventions to properly name the created Git branches"
keywords: "git, github, branching, naming, practices, conventions, name, branch, branches, best"
date: 2023-03-25
weight: 4
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /naming/branching
  - /best/practices
  - /naming/conventions
---

## Overview
Apart from having good [Git Branching Strategies](https://tilburgsciencehub.com/building-blocks/collaborate-and-share-your-work/use-github/git-branching-strategies/), it is important to follow some naming conventions to ensure proper maintenance of the repository and a clear, structured way of separating tasks.  To avoid confusions and have an organised overview of every feature that is being worked on, we go through seven best practices for naming branches.

### 1. Use Separators
When writing a branch name, using separators such as hyphen (-) or slash (/) helps to increase readability of the name. But remember to be consistent with the chosen separator for all branches names.
{{% example %}}

`optimize-data-analysis`  or  `optimize/data/analysis`

{{% /example %}}


### 2. Start Name with Category Word
It is recommended to begin the name of a branch with a **category word**, which indicates the type of task that is being solved with that branch. Some of the most used **category words** are:
| Category Word | Meaning |
| --- | --- |
|`hotfix` | for quickly fixing critical issues, <br> usually with a temporary solution |
|`bugfix` | for fixing a bug |
|`feature` | for adding, removing or modifying a feature |
|`test` | for experimenting something which is not an issue |
|`wip` | for a work in progress |

### 3. Use the ID of the Issue
Using the ID of the related issue in the branch name makes it easy to identify the task and keep track of its progress.

{{% example %}}

`wip-451-optimize-data-analysis`

This name indicates that the task of **optimizing data analysis** related to issue **451** is a **work in progress**. 

{{% /example %}}


### 4. Include Author Name
Another approach is to also include the name of the author working on the branch, to keep track of developers' work. Usually, the name of the author is the first element of the branch name, according to this format: `author-category-name`.

{{% example %}}

`jane.doe-bugfix-broken-link`

{{% /example %}}

### 5. Avoid Using Numbers Only
It's not a good practice to name a branch by only using numbers, because it creates confusion and increases chances of making mistakes. Instead, combine ID of issues with key words for the respective task.


### 6. Avoid Long Branch Names
As much as the branch name needs to be informative, it also needs to be precise and short. Detailed and long names can affect readability and efficiency. 

### 7. Be Consistent 
Consistency is key. After choosing one or more conventions, stick to them throughout the project.


{{% summary %}}

* Keep it short and concise, but make sure to include relevant key words.
* Use category words to easily identify the type of the task.
* Include ID of related issues to help tracking of progress.
* Adding the name of the author helps to keep track of shared work.
* Keep the same name conventions for the whole project.

{{% /summary %}}