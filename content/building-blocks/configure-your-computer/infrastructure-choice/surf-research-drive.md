---
title: "Set up SURF Research Drive and Rclone to Store Data"
description: "Learn how to set up a Research Drive account, upload and download files, share files and folders, and use rclone to selectively retrieve files from command line and code."
keywords: "surf, rd, rclone, large files, webdav, store, storage"
weight: 3
draft: false
aliases:
  - /setup/research-drive
  - /use/research-drive
  - /setup/rclone
---

## What is Research Drive?

**[Research Drive](https://www.surf.nl/en/research-drive-securely-and-easily-store-and-share-research-data)** is a data storage service by SURF. It's useful to store files that are too big for GitHub (even with LFS), files that need to be shared across multiple projects, archives from pre-GitHub projects, and other kinds of files that don't have a natural home in repositories (e.g., raw data). Think of it as a sort of Dropbox.

{{% warning %}}

SURF services are only available for researchers affiliated with Dutch institutions.

{{% /warning %}}

## Obtain an Account

If you are an employee at Tilburg University, you can request access to Research Drive by contacting the **[Research Data Office](https://www.tilburguniversity.edu/intranet/research-support-portal/rdm/advice)**. Ask then a a member of your team to give you access to the appropriate directories you will need for your project(s).

## Access your Files

### Via Web

The easiest way to access Research Drive is via the browser.

1. Visit [researchdrive.surfsara.nl/index.php/login](https://researchdrive.surfsara.nl/index.php/login) or the institutional instance of your institution. For Tilburg University, that is via the following link: **[tilburguniversity.data.surfsara.nl/index.php/login](https://tilburguniversity.data.surfsara.nl/index.php/login)**.

2. Login via **SURFconext** if you have an university account, or use the credentials given to you if you are an external guest.

3. You can now access your folders and files in your Research Drive. You can also upload and download files directly from your browser, like how you would do on Google Drive or Dropbox.

### With `rclone`

**[Rclone](https://rclone.org)** is an open-source command line program to manage files on cloud storage. You can use it to selectively access, download, upload, move and delete data on Research Drive. This will save you disk space - you won't need to download the entire project directory on your local disk, but only the files that you need.

The key advantage of using `rclone` is that you can work with files programmatically, **from the command line or your code directly**.

1. First, you will need to install `rclone`. Download from [rclone.org](https://rclone.org/downloads/), or run the following command on your personal machine:
{{% codeblock %}}
```bash
brew install rclone
```
{{% /codeblock %}}
{{% tip %}}
On computing services and research clusters, make sure that `module load rclone` is in your `./bash_profile`.
{{% /tip %}}

2. Run the following command to configure `rclone`:
{{% codeblock %}}
```bash
rclone config
```
{{% /codeblock %}}

You will be now guided through the configuration. Read this **[comprehensive guide](https://wiki.surfnet.nl/display/RDRIVE/4.+Access+Research+Drive+via+Rclone)** on how to configure it properly.

3. Have fun!

## Use rclone

### Some useful commands

#### List all files in directory
```
rclone ls RD:
```

#### Copy source directory to destination directory
```
rclone copy /my/folder RD:my/destination/folder
```

{{% tip %}}
You can find these and many more command examples on this **[comprehensive guide on using rclone with Research Drive](https://wiki.surfnet.nl/display/RDRIVE/4.+Access+Research+Drive+via+Rclone)**.
{{% /tip %}}

### Use rclone in your code

In order to use `rclone` directly in your code, you will need a wrapper like `python-rclone` for Python. You can install it with:
```bash
pip install python-rclone
```

You can find instructions on how to use it **[here](https://pypi.org/project/python-rclone/)**.

## Share your Files

You may want to share your files with other colleagues. You can do so by either sharing them with other Research Drive users or via a public link. Follow **[this guide](https://wiki.surfnet.nl/display/RDRIVE/How+to+share+a+folder+or+file)** to learn how to do it.

{{% warning %}}

Tilburg University disabled sharing with public links for safety reasons.

{{% /warning %}}
