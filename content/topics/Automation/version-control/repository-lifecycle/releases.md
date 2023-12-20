---
title: "Export Repositories With GitHub Releases"
description: ""
keywords: "git, github, releases, drafts, slide deck, intermediate files, repositories, export"
weight: 3
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /releases
---

## Overview

GitHub releases provide a powerful way to export and organize specific snapshots of your repository, ensuring accessibility and reproducibility for downstream activities. Examples include:
* Draft of a paper for posting or submission
* Presentation slide decks
* Cleaned data files to be used in other repositories or projects
* Intermediate data files to be used in the current repository that we want to maintain in a stable and replicable state

For a comprehensive release, ensure that not only the essential files but also adequate information for replication are included. This often involves documenting the commit associated with the released files or even the complete repository state at that specific juncture.

When the released files are PDFs of papers, talks, etc. we create releases on GitHub. When the released files are data or other large files we create releases on Dropbox.

## Creating a GitHub release

A release on GitHub consists of a tag to a specific commit, a zip archive of the repository (excluding any large files handled by LFS), and additional binary files that may be attached by hand. To create a GitHub release:
* Navigate to the GitHub releases section in a web browser
* Choose "Draft a new release"
* Choose a descriptive title (e.g., "Econometrica Second Submission 10_2020") and a descriptive short tag (e.g., "Ecma2ndSubmission")
* Attach the released files (e.g., PDF of a paper or talk) as binaries

{{% summary %}}
GitHub releases serve as an invaluable tool for encapsulating distinct stages of your repository's evolution. They offer a seamless mechanism to disseminate files and information, enabling effective collaboration and reproducibility. Employing this approach empowers you to curate and share your work, ensuring its accessibility and viability for future usage.
{{% /summary %}}

