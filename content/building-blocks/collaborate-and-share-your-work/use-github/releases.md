---
title: "Export Repositories with Github Releases"
description: ""
keywords: "git, github, releases, drafts, slide deck, intermediate files"
weight: 11
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /releases
---
## Github Releases
A release is an export of all or part of a repository that we want to be able to access for some downstream use. Examples include:
* Draft of a paper for posting or submission
* Slide deck for a presentation
* Cleaned data files to be used in other repositories or projects
* Intermediate data files to be used in the current repository that we want to maintain in a stable and replicable state

Releases should include the files we intend to use downstream as well as sufficient information to reproduce those files. That typically means recording the commit at which the released files were produced and/or the state of the full repository at that time.

When the released files are PDFs of papers, talks, etc. we create releases on Github. When the released files are data or other large files we create releases on Dropbox.

## Creating a release: GitHub Release

A release on Github consists of a tag to a specific commit, a zip archive of the repository (excluding any large files handled by LFS), and additional binary files that may be attached by hand. To create a Github release:
* Navigate to the Github releases section in a web browser
* Choose "Draft a new release"
* Choose a descriptive title (e.g., "Econometrica Second Submission 10_2020") and a descriptive short tag (e.g., "Ecma2ndSubmission")
* Attach the released files (e.g., PDF of a paper or talk) as binaries
