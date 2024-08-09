---
title: "Install Python Packages"
description: "Learn how to install new Python packages with package management tools like pip."
keywords: "python, pip, packages, selenium"
#date: 2020-11-11T22:02:51+05:30
draft: false
weight: 2
aliases:
  - /get/python-packages
  - /get/pip
  - /install/python-packages
---

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

{{% codeblock %}}
```bash
pip install --upgrade pip
```
{{% /codeblock %}}

If you get an error, try the following command instead:

{{% codeblock %}}
```bash
python -m pip install --upgrade pip
```
{{% /codeblock %}}

To build your web scraping toolkit, you will need the `selenium` package. Start by installing a dependency:

{{% codeblock %}}
```bash
pip install msgpack
```
{{% /codeblock %}}

Next, install `selenium` by entering:

{{% codeblock %}}
```bash
pip install selenium
```
{{% /codeblock %}}

`pip` will install the requested package and any necessary dependencies. If this succeeded, the last line displayed will be:

```bash
Successfully installed selenium-4.x.0
```

## Updating packages

To update an already installed package on your system, use the following command in your terminal: 

{{% codeblock %}}
```bash
pip install --upgrade selenium
```
{{% /codeblock %}}


{{% tip %}}

*No administrator rights?*

If you do not have administrator rights on the computer you are using, install packages only for your account. You can do this by typing `pip install --user packagename`, e.g., `pip install --user selenium`.

{{% /tip %}}
