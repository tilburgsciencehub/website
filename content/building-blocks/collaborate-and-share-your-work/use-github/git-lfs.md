---
title: "Working With Large Files on GitHub"
description: "GitHub limits the size of files allowed in repositories. Use Git lfs and upload large files to GitHub. Follow how to install, set up, and use git lfs."
weight: 7
keywords: "github, git-lfs, large files, versioning, organizing, git lfs, install"
#date: 2021-01-06T22:01:14+05:30
#draft: false
author: "Andrea Antonacci"
authorlink: "https://www.tilburguniversity.edu/staff/a-d-antonacci"
aliases:
  - /use/git-lfs
  - /share/large-files-on-github
---

<!-- This is a template. Please replace the content while keeping this structure.
Make sure to read our contribution guide to learn how to submit your content to Tilburg Science Hub. -->
<!-- Goal of the Building Block -->

## Overview

GitHub limits the size of files allowed in repositories. It warns you if you're trying to push a 50MB file, and completely stops you if the push exceeds 100MB.

However, even if it didn't stop you, versioning large files would be very impractical. That's because **a repository contains every version of every file** – that's the point of versioning, right?
Having multiple versions of large files cloned locally can become expensive in terms of disk space and fetch time.

The solution?

Well, first, you should ask yourself whether to store large files in the first place. Sometimes, large files are generated on the basis of existing data and code, and hence can always be "reconstructed" using existing files.

However, sometimes you wish to store raw data with moderate file sizes (let's say, between 5 and 50MB). For this, use **[Git LFS](https://git-lfs.github.com)**, an open-source Git extension for "large file storage". In short, Git LFS allows you to version large files while saving disk space and cloning time, using the same Git workflow that you're used to. It does **not** keep all your project's data locally. It only provides the version you actually **need** in your checked out revision.

When you mark a file as LFS file, the extension replaces the actual large file with a small *pointer* on your PC. The actual files - and all their versions - are located on the LFS remote server and *only the pulled* files are stored in a local cache. In other words, when you `pull` to your local repository, the pointer is replaced with the file and only the actual version you've requested gets stored locally.

Check out this video for a brief explanation on how Git LFS works.

{{< youtube 9gaTargV5BY iframe-video-margins >}}

## Install Git LFS <!-- Provide your code in all the relevant languages and/or operating systems. -->

Make sure that [Git is already installed](/building-blocks/configure-your-computer/statistics-and-computation/git/).

- Go to [git-lfs.github.com](https://git-lfs.github.com) and download directly. Or, if you use [`Brew`](/building-blocks/configure-your-computer/automation-and-workflows/commandline/#mac-users):

``` bash
brew install git-lfs
```

If you used Brew, go to the next step. If you downloaded directly from the website, open the terminal and change the current working directory to the downloaded and unzipped folder of Git LFS. Then, install:

``` bash
./install.sh
```

- Once installed, set up LFS for your account:

``` bash
git lfs install
```

If it was successful, you should see ```Git LFS initialized```.

## Usage

Git LFS doesn't do anything autonomously for you. You need to **explicitly tell it which files to track**.

``` bash
git lfs track "largefile.png"
```

Or, to track a file type (if you don't want to manually specify every single file you wish to track):

``` bash
git lfs track "*.png"
```

{{% warning %}}
**Be careful!** Do not forget the quotes around your file name.
{{% /warning %}}

Now you can resume your usual Git workflow. You just need to make sure to track the `.gitattributes` file too.

``` bash
git add .gitattributes
```
Simply add your file(s), commit and push as you'd normally do!

``` bash
git add largefile.png
git commit -m "Add large file"
git push origin master
```

Note: To clone a repository and to pull the most recent changes before working on it, use:
``` bash
git lfs clone {url}
git lfs pull
```

## Advanced use cases

You may be tempted to store your large files on a different server than the default LFS one.

- GitHub provides a [Git LFS server](https://github.com/git-lfs/lfs-test-server) that implements the Git LFS API which you can set up so that your binary files can be uploaded to a server that you administer. However, as of today, this is not in a "production ready state" and it is suggestedd to be used for testing only.

- In case you'd like to go serverless and back up these files on external services like Amazon S3, you can use one of the [Git LFS implementations](https://github.com/git-lfs/git-lfs/wiki/Implementations), like [this one](https://github.com/meltingice/git-lfs-s3) for AWS S3. However, bear in mind that these are some external open-source implementations that have not been verified by GitHub.

You can follow [this tutorial by Atlassian](https://www.atlassian.com/git/tutorials/git-lfs) for more advanced use cases, like moving a LFS repository between hosts or deleting local LFS files.

<!-- For example: ‘devising and organizing the project’,
‘data collection’, ‘data analysis’ and ‘article writing’. -->

## Store really large files

If you're hitting the limits of Git LFS, or only want to store *one* version of a file, object storage (e.g., such as the one on AWS S3) may be a better way to handling large files.
