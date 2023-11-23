---
title: "Learn Bash Commands"
description: "Learn how to navigate the terminal and command prompt"
keywords: "cmd, command prompt, terminal, cd, ls, dir, mv"
date: 2020-11-11T22:02:51+05:30
#draft: false
weight: 1
aliases:
  - /learn/bash
---

## Overview

The command line lets you communicate with your computer without using your mouse. It's a text-based interface where you communicate using text alone. The commands differ between Unix-based systems (e.g., Mac / Linux) and Windows computers. On Apple and Windows computers the command line tool is called the Terminal and Command Prompt, respectively.

With this building block, we will help you navigate the command line (Terminal and Command Prompt) and describe the various commands that are used to do so.

But before we start, it is important to be familiar with two important terms: Directories and file paths.

### Directories
In programming, all folders are called directories and a directory within another directory is called a `subdirectory`. A `working directory` is the directory in which the user is working currently. The default working directory when the user logs in is known as the `home directory`. So when you open up a new Terminal window, you are automatically situated in your home directory.


### File Paths
Your computer understands two kinds of paths, absolute and relative ones. An absolute path starts from the root (or home directory). A relative path, on the other hand, starts from the current directory (for instance, your desktop).

{{% codeblock %}}
```bash
absolute_path = "/Users/Pieter/Desktop/images/photo1.jpg"

relative_path = "images/photo1.jpg"  # provided that your working directory is "Desktop"
```
{{% /codeblock %}}


## How to open the Command Line?
*Mac*  
Open the Terminal by going into your Applications folder, and then into your Utilities folder, and then double-clicking on the Terminal icon. Alternatively, you can use Spotlight to search for the program (e.g. Cmd + Space).

*Windows*  
Type `cmd` into the search bar and hit enter, it should launch the Windows Command Prompt.


## Commands

### Print Working Directory
*Mac*  
To see the full path for your working directory, you can use the `pwd` command, which stands for print working directory.

![terminal_pwd](../images/terminal_pwd.gif)

*Windows*  
If you type `pwd` in the Windows Command prompt, it doesn't recognize the command. Instead, type `cd` (or `chdir`) to view the current working directory.

### List Files
*Mac*  
Unlike the graphical user interface, you cannot see what other directories or files are present just by being in a particular directory. You have to explicitly tell your computer to list them for you using the `ls` command.

![terminal_ls](../images/terminal_ls.gif)

If you’d like to explore another directory, you need to use ls with a path. For example, `ls ~/Documents` will show you what's inside Documents.

*Windows*  
The `dir` command lists all files and folders in the current directory. In addition, it returns the file size, file type, and the date and time the file was last updated.

{{% tip %}}
Press the up and down arrows on your keyboard to cycle through previously used commands in the terminal. Also, you can press `TAB` for auto-complete suggestions.
{{% /tip %}}

### Change Directories
*Mac & Windows*  
The command `cd` allows you to change directories; it's the equivalent of double-clicking on a folder. For example, if you want to move from the `samspade` directory into its subdirectory `Documents`, you would write `cd Documents`. To move back up to your home directory, you can use the `cd ..` command.

Note that the path in front of `$` indicates your working directory. This helps you keep track of where you're at.

![terminal_cd](../images/terminal_cd.gif)


{{% tip %}}
A handy shortcut to start in a specific directory immediately is to look up the folder in Finder, right-click on it, and choose "New Terminal at Folder".
{{% /tip %}}

### Create Folder
*Mac & Windows*   
To make a new directory, you can use the `mkdir` command which takes the name of the new directory and the destination path of the directory. So, the command `mkdir to-do-lists Documents` would create a new to-do lists directory inside the documents folder.

{{% tip %}}
Generally speaking, it's better to avoid special characters in directory names, you can use quotes to create a folder name that includes spaces (e.g., `mkdir "to do lists" Documents`).
{{% /tip %}}


### Remove Files & Directories
*Mac*  
You can delete a directory along with any files or subdirectories by running the `rm -r` command. For example, `rm -r to-do-lists` removes the to-do lists folder and its contents. Note that you can list multiple files and directories after `rm -r` to remove them all.

*Windows*   
Separate files can be removed with the `del` command (e.g., `del to-do-list.txt`). To remove a directory, use the command `rmdir`.

{{% warning %}}
You can't undo the `rm` and `del` commands, so be careful when you delete files. Removing files in command line is not the same as moving a file to the trash - it's permanent!
{{% /warning %}}


### Move & Rename Files
*Mac*  
The `mv` command has two applications: moving and renaming files. It uses the following syntax:

{{% codeblock %}}
```bash
# move directories or files to a new location
mv [FILE_NAME] [LOCATION]

# rename files
mv [FILE_NAME] [NEW_FILE_NAME]
```
{{% /codeblock %}}

Examples:
* `mv monday_tasks.txt To_Do_Lists` moves the text file from its current directory to the 'to-do list' folder.
* `mv 'Monday Tasks.txt' monday_tasks.txt` renames the file by stripping the spaces.

*Windows*  
The syntax to move and rename files is exactly the same as on Mac, but instead of `mv` you need to use the commands `move` and `rename` respectively. Note that you cannot use `move` to rename files on Windows!

## See Also
* This [guide on the "art of command line"](https://github.com/jlevy/the-art-of-command-line).
* This building block draws on material of [this](https://generalassembly.github.io/prework/cl/#/) interactive tutorial by General Assembly which is absolutely worth checking out!
* [Cheatsheet](http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf) with the most common Windows Command Prompt commands.
