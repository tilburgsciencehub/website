---
tutorialtitle: "Running Computations Remotely"
type: "running-computations-remotely"
title: "Move Files"
indexexclude: "true"
description: "Learn how to run computations remotely"
keywords: "cloud computing, azure, amazon, google, virtual machine"
weight: 103
draft: false
aliases:
  - /learn/cloud/move-files
  - /topics/more-tutorials/running-computations-remotely/move-files
---

# Move Files

## Terminal (Mac)

1. `cd` into the directory that contains the files that you want to transfer.

2. Type `scp -i $KEY -r $(pwd) ec2-user@$HOST:/home/ec2-user` to copy your entire working directory to the home directory of your VM. (tip: this method assumes you're not connected yet. If you are though, press Ctrl + D to disconnect).


## FileZilla (Mac & Windows)
![Move files](../img/move-files.gif)

1. Alternatively, install File Transfer Protocol (FTP) client [FileZilla](https://filezilla-project.org/).
2. Click on File > Site Manager > New Site.
3. Change the protocol to "SFTP".
4. Use the public IPV4 DNS address (see AWS console) as the host name.
5. Choose "Key file" as the logon type, set the username to `ec2-user`, and add your `*.pem` file as the key file.
6. Click on "Connect". On the right side, all files on the EC2 Instance are listed, and on the left side you can find the files on your local machine. To copy files from one place to another, you can simply drag and drop them between both windows.
