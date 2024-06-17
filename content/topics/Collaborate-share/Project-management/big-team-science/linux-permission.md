---
title: "Linux files permission"
description: "Learn how to change file permissions in linux using command line"
keywords: "file, research cloud, linux, ubuntu, directory, data mangement"
weight: 2
draft: false
aliases:
  - /permission-linux
authorlink: "https://tilburgsciencehub.com/contributors/krzysztofwiesniakowski/"

---
# Changing File Permissions in Linux

When working in a Linux environment, it's common to encounter situations where you need to change file permissions. This guide will help you understand how to modify file permissions using the `chmod` command.

### Understanding File Permissions

Linux file permissions are broken down into three types:

1. **User (u)**: The owner of the file.
2. **Group (g)**: The group that owns the file.
3. **Others (o)**: Everyone else.

Permissions are also divided into three categories:

- **Read (r)**: Permission to read the file.
- **Write (w)**: Permission to modify the file.
- **Execute (x)**: Permission to execute the file.

## Viewing Current Permissions

To view the current permissions of a file, use the `ls -l` command:

{{% codeblock %}}
```bash
ls -l filename
```
{{% /codeblock %}}

The output will look something like this

{{% codeblock %}}
```bash
-rwxr-xr-x 1 user group 4096 Jun 17 12:34 filename
```
{{% /codeblock %}}

Here’s what each part means:

- `rwxr-xr-x`: The permissions for the file.
- `1`: Number of hard links.
- `user`: The owner of the file.
- `group`: The group that owns the file.
- `4096`: The size of the file in bytes.
- `Jun 17 12:34`: The last modification date and time.
- `filename`: The name of the file.


### Changing Permissions
The `chmod` command is used to change the permissions of a file or directory.

### Using Symbolic Mode
Symbolic mode uses letters to represent the permissions. Here are some examples:

Add read permission for the user:
{{% codeblock %}}
```bash
chmod u+r filename
```
{{% /codeblock %}}


Remove write permission for the group:

{{% codeblock %}}
```bash
chmod g-w filename
```
{{% /codeblock %}}

Add execute permission for others:
{{% codeblock %}}
```bash
chmod o+x filename
```
{{% /codeblock %}}


Add read, write, and execute permissions for the user, and read and execute permissions for the group and others
{{% codeblock %}}
```bash
chmod u+rwx,g+rx,o+rx filename
```
{{% /codeblock %}}

### Using Numeric Mode
Numeric mode uses numbers to represent permissions. Each type of permission is assigned a value:

- Read (r) = 4
- Write (w) = 2
- Execute (x) = 1

To set permissions, add the values together. For example, to set read, write, and execute permissions, use 7 (4+2+1). Here are some examples:

Set read, write, and execute permissions for the user, and read and execute permissions for the group and others (755):

{{% codeblock %}}
```bash
chmod 755 filename
```
{{% /codeblock %}}

Set read and write permissions for the user, and read permissions for the group and others (644):

{{% codeblock %}}
```bash
chmod 644 filename
```
{{% /codeblock %}}

### Recursively Changing Permissions
To change permissions for a directory and all its contents, use the -R option:

{{% codeblock %}}
```bash
chmod -R 755 directory
```
{{% /codeblock %}}


## Conclusion
Understanding and managing file permissions is essential for maintaining security and proper access control in a Linux environment. With the `chmod` command, you can easily modify permissions to suit your needs.