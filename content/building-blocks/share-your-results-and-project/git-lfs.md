---
title: "How to Work with Large Files on GitHub"
date: 2021-01-06T22:01:14+05:30
draft: false
---

<!-- This is a template. Please replace the content while keeping this structure.
Make sure to read our contribution guide to learn how to submit your content to Tilburg Science Hub. -->

# How to Work with Large Files on GitHub <!-- Goal of the Building Block -->

GitHub limits the size of files allowed in repositories. It warns you if you're trying to push a 50MB file, and completely stops you if the push exceed 100MB.

However, even if it didn't stop you, versioning large files would be very impractical. That's because **a repository contains every version of every file** – that's the point of versioning, right?
Having multiple versions of large files cloned locally can become expensive in terms of disk space and fetch time.

The solution? Use **[Git LFS](https://git-lfs.github.com)**, an open-source Git extension for "large file storage". In short, it allows you to version large files while saving disk space and cloning time, using the same Git workflow that you're used to. It does **not** keep all your project's data locally. It only provides the version you actually **need** in your checked out revision.

When you mark a file as LFS file, the extension replaces the actual large file with a small *pointer* on your PC. The actual files are located on the remote server and *only the pulled* actual files are stored in a local cache. In other words, when you `pull` to your local repository, the pointer is replaced with the actual file.

Check [this video](https://www.youtube.com/watch?v=9gaTargV5BY) out for a brief explanation on how Git LFS works.

## Install Git LFS <!-- Provide your code in all the relevant languages and/or operating systems. -->

Make sure that [Git is already installed](setup/gitInstall.md).

- Go to [git-lfs.github.com](https://git-lfs.github.com) and download directly. Or, if you use Brew:

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

!!! warning "Be careful"
    Do not forget the quotes around your file name!

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

## Advanced use cases

You can follow [this tutorial by Atlassian](https://www.atlassian.com/git/tutorials/git-lfs) for more advanced use cases, like moving a LFS repository between hosts or deleting local LFS files.

## Keywords

github, git-lfs, large files, versioning, organizing
<!-- For example: ‘devising and organizing the project’,
‘data collection’, ‘data analysis’ and ‘article writing’. -->
