---
title: "Install Python Packages"
description: "Learn how to install new Python packages with package management tools like pip."
keywords: "python, pip, packages, selenium"
#date: 2020-11-11T22:02:51+05:30
draft: false
<<<<<<< HEAD
weight: 4
=======
weight: 2
>>>>>>> master
aliases:
  - /get/python-packages
  - /get/pip
  - /install/python-packages
---

<<<<<<< HEAD
## What are Python packages 

Python packages are collections of modules and functions that provide additional functionality beyond what is available in the Python standard library. They allow developers to easily extend Python's capabilities by including pre-written code for specific tasks, such as data analysis, web development, machine learning, and more. 

## Installing Python packages

Anaconda's Python Distribution comes with many of the packages we need to do scientific computing. If you're interested in all the packages included, click [here](https://docs.continuum.io/anaconda/packages/pkg-docs) and go to the Python 3.x tab.

However, you may come across packages that are not installed by default. In this case we recommend you use the `pip` package management tool to install them.
### Installation steps

{{% warning %}}
If your python 3 was found via `python3 --version` on the previous page, then type `pip3` instead of `pip` for all of the following python plugins.
{{% /warning %}}

First let us update pip by typing the following into the terminal
=======
## Overview 

[Python packages](/https://docs.python.org/3/tutorial/modules.html#packages) are collections of modules and functions that provide additional functionalities beyond the standard library. They enable developers to extend Python's capabilities easily with pre-written code for specific tasks, such as data analysis, web development, machine learning, and more. This guide will teach you how to install and update Python packages.

## Installing Python packages

The [Anaconda Python Distribution](/install/python) includes many of the packages we need for scientific computing. If you're interested in all the included packages, click [here](https://docs.continuum.io/anaconda/packages/pkg-docs) and select the `Python 3.x` tab.

However, you may come across packages that are not installed by default. In such cases, we recommend using the `pip` package management tool to install them.

{{% warning %}}

If you verified your Python installation in the [setup process](/get/python) using `python3 --version`, use `pip3` instead of `pip` for all the following commands.

{{% /warning %}}

### The installation steps

First, update `pip` by typing the following command in the terminal:
>>>>>>> master

{{% codeblock %}}
```bash
pip install --upgrade pip
```
{{% /codeblock %}}

<<<<<<< HEAD

If you get an error, try typing instead:
=======
If you get an error, try the following command instead:

>>>>>>> master
{{% codeblock %}}
```bash
python -m pip install --upgrade pip
```
{{% /codeblock %}}

<<<<<<< HEAD

You also need the package `Selenium` as part of the web scraping tool kit we will build up. First let us install a depency for it via
=======
To build your web scraping toolkit, you will need the `selenium` package. Start by installing a dependency:
>>>>>>> master

{{% codeblock %}}
```bash
pip install msgpack
```
{{% /codeblock %}}

<<<<<<< HEAD

We then install `selenium` by entering the following into a terminal:
=======
Next, install `selenium` by entering:

>>>>>>> master
{{% codeblock %}}
```bash
pip install selenium
```
{{% /codeblock %}}

<<<<<<< HEAD

`pip` will then go through and install the package we asked for, and any other dependencies.
If this succeeded, the last line it printed out should be:
=======
`pip` will install the requested package and any necessary dependencies. If this succeeded, the last line displayed will be:
>>>>>>> master

```bash
Successfully installed selenium-4.x.0
```

<<<<<<< HEAD

## Updating packages

In order to update already installed packages on your system use the following command in your terminal: 
=======
## Updating packages

To update an already installed package on your system, use the following command in your terminal: 
>>>>>>> master

{{% codeblock %}}
```bash
pip install --upgrade selenium
```
{{% /codeblock %}}

<<<<<<< HEAD
### Common problems

{{% tip %}}
**No administrator rights?**

If you do not have administrator rights to the computer you are using,
please install packages only for your account.
You can do so by typing `pip install --user packagename`, e.g., `pip install --user selenium`.
=======

{{% tip %}}

*No administrator rights?*

If you do not have administrator rights on the computer you are using, install packages only for your account. You can do this by typing `pip install --user packagename`, e.g., `pip install --user selenium`.
>>>>>>> master

{{% /tip %}}
