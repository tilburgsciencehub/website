---
title: "Working with Large Files on GitHub"
description: "GitHub limits the size of files allowed in repositories. Use Git LFS and upload large files to GitHub. Follow how to install, set up, and use Git LFS."
weight: 9
keywords: "github, git, git-lfs, large files, versioning, organizing, Git LFS, install, large, file, storage"
#date: 2021-01-06T22:01:14+05:30
#draft: false
author: "Andrea Antonacci"
authorlink: "https://www.tilburguniversity.edu/staff/a-d-antonacci"
aliases:
  - /use/git-lfs
  - /share/large-files-on-github
---

## Overview

When using Git repositories, the challenge of accommodating large files emerges. GitHub imposes limitations on file sizes within repositories. You are met with a warning when attempting to push a file exceeding 50MB, and the threshold is further constrained at 100MB, completely halting your push.

But even if these limits didn't exist, versioning large files would be very impractical. 

#### Why versioning large files poses challenges

A fundamental concept of versioning is that repositories retain every iteration of each file, ensuring a comprehensive historical record. However, this comes with a trade-off. Cloning repositories that include multiple versions of large files can rapidly consume disk space and impede fetch times. 

This building block explains a solution to this: **Git Large File Storage (LFS)**! 
It is structured into the following sections:
- Git LFS
  - Installation
  - Explicit tracking
  - Resuming workflow
- Advanced use cases
- Storing extremely large files

## Git LFS

Before delving into Git LFS, you should ask yourself whether storing large files is necessary in the first place. Often, these large files are generated on the basis of existing data and code and hence can be reconstructed using existing files.

However, sometimes you wish to store raw data with moderate file sizes (between 5MB and 50MB). For this, use **[Git LFS](https://git-lfs.github.com)**, an open-source Git extension designed to address the intricacies of handling large files. 

In short, Git LFS allows you to version large files while saving disk space and cloning time, using the same Git workflow that you’re used to. It does not keep all your project’s data locally. It only provides the version you need in your checked-out revision.

{{% tip %}}
*How Git LFS works*

When you mark a file as an LFS file, the extension replaces the actual large file with a small *pointer* on your PC. The actual files (and all their versions) are located on the LFS remote server and *only the pulled* files are stored in a local cache. When you `pull` to your local repository, the pointer is replaced with the file and only the actual version you've requested gets stored locally.
{{% /tip %}}

{{% summary %}}
**The benefits of Git LFS:**

- Facilitates versioning of large files without bloating your local repository.
- Enhances cloning and fetch times by conserving storage.
- Maintains the same Git workflow that you are used to.
{{% /summary %}}

{{% tip %}}
Watch this informative video for a brief explanation of how Git LFS works.

{{< youtube 9gaTargV5BY iframe-video-margins >}}
{{% /tip %}}


### Installation 

- Ensure you have Git installed. If not, follow this [building block](/building-blocks/configure-your-computer/statistics-and-computation/git/) to set it up. 

- Next, download Git LFS from [git-lfs.github.com](https://git-lfs.github.com) or use [`Brew`](/building-blocks/configure-your-computer/automation-and-workflows/commandline/#mac-users) for macOS users:

{{% codeblock %}}
```bash
brew install git-lfs
```
{{% /codeblock %}}

- If you used Brew, go to the next step. If downloaded directly, open the terminal and change the current working directory to the downloaded and unzipped folder of Git LFS. Then, install:

{{% codeblock %}}
``` bash
./install.sh
```
{{% /codeblock %}}

- Once installed, set up LFS for your account:

{{% codeblock %}}
``` bash
git lfs install
```
{{% /codeblock %}}

- If it was successful, you should see the message ```Git LFS initialized```.

### Explicit tracking

Git LFS doesn't autonomously manage files: you must **explicitly tell it which files to track**.

- To track a specific file, use:
{{% codeblock %}}
``` bash
git lfs track "largefile.png"
```
{{% /codeblock %}}

- Alternatively, to track multiple files of a specific type: 

{{% codeblock %}}
``` bash
git lfs track "*.png"
```
{{% /codeblock %}}

{{% warning %}}
Always enclose file names in quotes!
{{% /warning %}}

### Resuming workflow

Now you can resume your usual Git workflow. You just need to make sure to track the `.gitattributes` file too.

{{% codeblock %}}
``` bash
git add .gitattributes
```
{{% /codeblock %}}

Simply add your file(s), commit, and push as you'd normally do!

{{% codeblock %}}
``` bash
git add largefile.png
git commit -m "Add large file"
git push origin master
```
{{% /codeblock %}}

{{% tip %}}
To clone a repository and to pull the most recent changes before working on it, use:

{{% codeblock %}}
``` bash
git lfs clone {url}
git lfs pull
```
{{% /codeblock %}}

{{% /tip %}}

## Advanced use cases

For advanced scenarios, consider external LFS servers and storage options. 

- GitHub provides a [Git LFS server](https://github.com/git-lfs/lfs-test-server) that implements the Git LFS API which you can set up so that your binary files can be uploaded to a server that you administer. However, as of today, this is not in a "production ready state" and it is suggested to be used for testing only.

- In case you'd like to go serverless and back up these files on external services like Amazon S3, you can use one of the [Git LFS implementations](https://github.com/git-lfs/git-lfs/wiki/Implementations), like [this one](https://github.com/meltingice/git-lfs-s3) for AWS S3. However, bear in mind that these are some external open-source implementations that have not been verified by GitHub.

{{% tip %}}
You can follow [this tutorial by Atlassian](https://www.atlassian.com/git/tutorials/git-lfs) for more advanced use cases, like moving an LFS repository between hosts or deleting local LFS files.
{{% /tip %}}


## Storing extremely large files

If you're hitting the limits of Git LFS, or only want to store *one* version of a file, object storage (e.g., such as the one on AWS S3) may be a better way to handle large files.

{{% summary %}}
Managing large files within Git repositories can be a challenge due to file size limitations and the storage demands of versioning. Git LFS presents an elegant solution by allowing you to incorporate large files while maintaining a lean local repository. With explicit tracking, effortless integration, and advanced options, Git LFS offers a versatile approach to handling large assets within your Git workflow.
{{% /summary %}}

