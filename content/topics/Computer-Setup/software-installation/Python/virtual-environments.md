---
title: "Configure Python Virtual Environments"
description: "Python environment manager using venvwrapper package: how to set up virtual environments, create or delete environments, add packages to them, create requirements.txt file containing packages versions, switch environments."
keywords: "venvwrapper, virtual, environment, manage, configure, packages"
date: 2023-04-20
weight: 6
author: "Ana Bianca Luca"
authorlink: "https://tilburgsciencehub.com/contributors/anabiancaluca/"
aliases:
  - /configure/virtual/environments
  - /create/environment
  - /use/venvwrapper
---

## Overview

When working on multiple Python projects that require different packages and libraries, we may run into the issue of needing different versions of packages for each project. To avoid upgrading or downgrading versions each time we work on a different project, we can make use of virtual environments. The core idea of a virtual environment is to create an isolated environment that has the packages a project needs contained within it, that can be easily "turned on" and "turned off" as needed. This topic explains how to set up and manage virtual environments using the Python package `venvwrapper`.

## Advantages of virtual environments

Virtual environments allow us to keep certain combinations of package versions required for each project and access them when we work on the respective projects. This way, it is easy to separate project requirements and also ensure that the project scripts will continue to run even if we make changes to some package versions outside the project. Having virtual environments also helps to keep a clear overview of packages from each project and to easily reproduce workflows, even if it is on the same computer or a different one. 

## Windows Users

The first step we need to take is to **install** the package. For this, open the Command Prompt and type:

{{% codeblock %}}
```bash
pip install virtualenvwrapper-win

```
{{% /codeblock %}}


Next, we navigate to the folder where we want to create our virtual environments, which can be in the same folder as the script of the project or in a separate folder where we keep all environments. To **create** a virtual environment type the following in the Command Prompt:

{{% codeblock %}}
```bash
mkvirtualenv name_of_env

```
{{% /codeblock %}}


To **activate** the created environment, or switch between environments, we use:

{{% codeblock %}}
```bash
workon name_of_env
```
{{% /codeblock %}}


Now, we have this newly created environment open, so we can **add** packages with `pip install name_of_package`.

After we install all the packages we want for our project in the environment, we can **create a text file** which contains all installed packages and their versions. This is useful for keeping track of the configurations of the virtual environments, but also for easily replicating the configuration. To create this list and install packages from it we use the following commands in `cmd`:

{{% codeblock %}}
```bash
#create requirements list of installed packages
pip freeze > requirements.txt

#for replicating environments, we can install all packages from requirements.txt
pip install -r requirements.txt
```
{{% /codeblock %}}

We can **see the installed packages** by using one of the following commands in the `cmd`:

{{% codeblock %}}
```bash
pip list  
#or
lssitepackages
```
{{% /codeblock %}}

Equivalently, we can **see all the created environments** by using:

{{% codeblock %}}
```bash
lsvirtualenv
```
{{% /codeblock %}}

We can **deactivate** the environment and return to the 'basic' one, type in `cmd`:

{{% codeblock %}}
```bash
deactivate
```
{{% /codeblock %}}

To **delete** virtual environments, we use:

{{% codeblock %}}
```bash
rmvirtualenv name_of_env
```
{{% /codeblock %}}


## Mac and Linux Users

To configure virtual environments on Mac OS, the commands are somehow similar to Windows, but additionally we need to set up path and virtual environment variable.
We start by **installing** `virtualenvwrapper` by typing in the Terminal:

{{% codeblock %}}
```bash
pip install virtualenvwrapper
```
{{% /codeblock %}}

Next, we need to **define environment variables** that contain the path to the Python installation folder, as well as a path location for where we want to create the virtual environments. We also need to add the path where `virtualenvwrapper` was installed.

{{% codeblock %}}
```bash
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 export 
VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh
```
{{% /codeblock %}}

Remember to replace the above path with your own installation location.

Then, we can **create** a virtual environment.

{{% codeblock %}}
```bash
mkvirtualenv name_of_env
```
{{% /codeblock %}}

We can **add packages** to the environment with:

{{% codeblock %}}
```bash
pip install name_of_package
```
{{% /codeblock %}}


We can **see all the installed packages** in the environment with:

{{% codeblock %}}
```bash
lssitepackages
```
{{% /codeblock %}}

To **see all the created environments** we use:

{{% codeblock %}}
```bash
ls $WORKON_HOME
```
{{% /codeblock %}}


To **create the _requirements.txt_ file**, **switch environments**, **deactivate** or **delete environments**, we use the same commands from Windows.


## Commands overview

{{%table%}}
|   | Windows | Mac | Linux |
| --- | --- | --- | --- |
|Install `virtualenvwrapper` | pip install virtualenvwrapper-win | pip install virtualenvwrapper | pip install virtualenvwrapper |
|Configuration | - | export WORKON_HOME=~/Envs <br /> mkdir -p $WORKON_HOME <br /> VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 export <br /> VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv <br /> source /usr/local/bin/virtualenvwrapper.sh | export WORKON_HOME=~/Envs <br /> mkdir -p $WORKON_HOME <br /> VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 export <br /> VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv <br /> source /usr/local/bin/virtualenvwrapper.sh |
|Create environment | mkvirtualenv name_of_env | mkvirtualenv name_of_env | mkvirtualenv name_of_env |
|Activate/switch environment | workon name_of_env | workon name_of_env | workon name_of_env |
|Install packages | pip install name_of_package | pip install name_of_package | pip install name_of_package | 
|Create list of packages | pip freeze > requirements.txt | pip freeze > requirements.txt | pip freeze > requirements.txt |
|See installed packages | lssitepackages | lssitepackages | lssitepackages |
|See created environments | lsvirtualenv | ls $WORKON_HOME | ls $WORKON_HOME | 
|Deactivate environment | deactivate | deactivate | deactivate |
|Delete environment | rmvirtualenv name_of_env | rmvirtualenv name_of_env | rmvirtualenv name_of_env |
{{%/table%}}

## Other virtual environment packages


Besides `venvwrapper`, there are other packages that create and manage virtual environments:
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
- [conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

## See also

- [Python Virtual Environments - a Primer](https://realpython.com/python-virtual-environments-a-primer/)
