---
title: "Linux file permissions"
description: "Learn how to change file permissions in linux using command line"
keywords: "file, research cloud, linux, ubuntu, directory, data mangement"
weight: 2
draft: false
aliases:
  - /permission-linux
authorlink: "https://tilburgsciencehub.com/contributors/krzysztofwiesniakowski/"
author: Krzysztof Wiesniakowski

---
## Changing file permissions in Linux

When working in a Linux environment, it is common to encounter situations where you need to change file permissions. This guide will help you understand how to modify file permissions using the `chmod` command.

## Understanding file permissions

Linux file permissions are broken down into three types:

1. **User (u)**: The owner of the file.
2. **Group (g)**: The group that owns the file.
3. **Others (o)**: Everyone else.

Permissions are also divided into three categories:

- **Read (r)**: Permission to read the file.
- **Write (w)**: Permission to modify the file.
- **Execute (x)**: Permission to execute the file.

## Viewing current permissions

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

- `rwxr-xr-x`: The permissions for the file, broken down as follows:
    - `rwx`: The permissions for the user (owner) of the file.
      - `r` (read): The user can read the file.
      - `w` (write): The user can write to (modify) the file.
      - `x` (execute): The user can execute the file.
    - `r-x`: The permissions for the group that owns the file.
      - `r` (read): The group members can read the file.
      - `-` (no write permission): The group members cannot write to (modify) the file.
      - `x` (execute): The group members can execute the file.
    - `r-x`: The permissions for others (everyone else).
      - `r` (read): Others can read the file.
      - `-` (no write permission): Others cannot write to (modify) the file.
      - `x` (execute): Others can execute the file.

- `1`: Number of hard links.
- `user`: The owner of the file.
- `group`: The group that owns the file.
- `4096`: The size of the file in bytes.
- `Jun 17 12:34`: The last modification date and time.
- `filename`: The name of the file.

## Changing permissions
The `chmod` command is used to change the permissions of a file or directory.

## Using symbolic mode
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

## Understanding numerical values for permissions

File permissions in Linux can also be represented using numerical (octal) values. Each permission type is assigned a specific value:

- `4` (read)
- `2` (write)
- `1` (execute)

These values are combined to form the total permission for the user, group, and others. The permissions are specified in the order: owner, group, and others.

Here is a detailed breakdown of the numerical values:

- `400`: Read by owner
- `040`: Read by group
- `004`: Read by anybody
- `200`: Write by owner
- `020`: Write by group
- `002`: Write by anybody
- `100`: Execute by owner
- `010`: Execute by group
- `001`: Execute by anybody

### Example calculation

Summing up all the values above gives us `775`. Therefore, it grants:
- Read, write, and execute permissions to the owner (4+2+1=7)
- Read and execute permissions to the group (4+1=5)
- Read and execute permissions to others (4+1=5)


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

## Recursively changing permissions
To change permissions for a directory and all its contents, use the -R option:
755 grants all permissions (read, write, execute) to the user (owner) but only read and execute permissions to the group and others.
{{% codeblock %}}
```bash
chmod -R 755 directory
```
{{% /codeblock %}}


## Conclusion
Understanding and managing file permissions is essential for maintaining security and proper access control in a Linux environment. With the `chmod` command, you can easily modify permissions to suit your needs.