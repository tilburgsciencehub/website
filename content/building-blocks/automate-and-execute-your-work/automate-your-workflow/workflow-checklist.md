---
title: "Use this Checklist to Improve Your Project's Structure and Efficiency"
description: "Audit data, create and organize efficient projects."
weight: 7
keywords: "make, makefile, automation, recipes, checklist, project, plan, workflow, project organization, code structure, project checklist"
date: 2021-01-06T22:01:14+05:30 #updated 2023-08-12
aliases:
  - "/audit/workflow-checklist"
  - "/audit/organize-your-projects"
---

## Learning Goals

- Understand the essential guidelines to structure and maintain a well-organized project.
- Learn best practices for efficient and reproducible project workflows.

## Overview

As projects progress, they can become disorganized and difficult to navigate. A structured approach not only facilitates collaboration and understanding but also ensures that the project remains efficient and reproducible. 

This building block offers a comprehensive checklist to guide you towards achieving this goal.

## Checklist

### Project level
* Implement a consistent [directory structure](/tutorials/project-management/principles-of-project-setup-and-workflow-management/directories/#working-example): data/src/gen
* Include [readme with project description](/tutorials/project-management/principles-of-project-setup-and-workflow-management/documenting-code/#main-project-documentation) and technical instruction how to run/build the project
* Store any authentication credentials outside of the repository (e.g., in a JSON file), NOT clear-text in source code
* Mirror your `/data` folder to a secure backup location; alternatively, store all raw data on a secure server and download relevant files to `/data`

### Throughout the Pipeline
#### File/directory structure  
* Create subdirectory for source code: /src/[pipeline-stage-name]/
* Create subdirectories for generated files in /gen/[pipeline-stage-name]/: temp, output, and audit.
* Make all file names relative, and not absolute (i.e., never refer to C:/mydata/myproject, but only use relative paths, e.g., ../output)
* Create directory structure from within your source code, or use .gitkeep
* Create subdirectories for generated files in `/gen/[pipeline-stage-name]/`: `temp`, `output`, and `audit`.
* Make all file names relative, and not absolute (i.e., never refer to C:/mydata/myproject, but only use relative paths, e.g., ../output)
* Create directory structure from within your source code, or use .gitkeep


#### Automation & documentation
* Have a [`makefile`](/automate/project-setup)
* Alternatively, include a [readme with running instructions](/tutorials/project-management/principles-of-project-setup-and-workflow-management/documenting-code/#main-project-documentation)
* Make dependencies between source code and files-to-be-built explicit, so that `make` automatically recognizes when a rule does not need to be run (properly define targets and source files)
* Include function to delete temp, output files, and audit files in makefile

#### Versioning
* Version all source code stored in `/src` (i.e., add to Git/GitHub)
* Do not version any files in `/data` and `/gen` (i.e., do NOT add them to Git/GitHub)
* Want to exclude additional files (e.g., files that (unintentionally) get written to `/src`? Use .gitignore for files/directories that need not to be versioned

#### Housekeeping
* Have short and accessible variable names
* Loop what can be looped
* Break down "long" source code in subprograms/functions, or split script in multiple smaller scripts
* Delete what can be deleted (including unnecessary comments, legacy calls to packages/libraries, variables)
* Use of asserts (i.e., make your program crash if it encounters an error which is not recognized as an error)

#### Testing for portability
* Tested on own computer (entirely wipe `/gen`, re-build the entire project using `make`)
* Tested on own computer (first clone to new directory, then re-build the entire project using `make`)
* Tested on different computer (Windows)
* Tested on different computer (Mac)
* Tested on different computer (Linux)

{{% warning %}}
**Versioned any sensitive data?**

Before making a GitHub repository public, we recommend you check that you have not stored any sensitive information in it (such as any passwords).
This tool has worked great for us: [GitHub credentials scanner](https://geekflare.com/github-credentials-scanner/).
{{% /warning %}}


## See Also

- [This tutorial](/tutorials/project-management/principles-of-project-setup-and-workflow-management/overview/) covers the fundemantal principles of project setup and workflows underlying this checklist.
