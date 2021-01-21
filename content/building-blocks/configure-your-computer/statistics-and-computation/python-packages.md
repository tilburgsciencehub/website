---
title: "Python Packages"
description: "Learn how to install new Python packages with package management tools like pip."
keywords: "python, pip, packages, selenium"
date: 2020-11-11T22:02:51+05:30
draft: false
weight: 4
---

Anaconda's Python Distribution comes with many of the packages we need to do scientific computing. If you're interested in all the packages included, click [here](https://docs.continuum.io/anaconda/packages/pkg-docs) and go to the Python 3.x tab.

## pip

Howevever, you may come across packages that are not installed by default.
In this case we recommend you use the `pip` package management tool to install them.

{{% warning %}}
If your python 3 was found via `python3 --version` on the previous page, then type `pip3` instead of `pip` for all of the following python plugins.
{{% /warning %}}

First let us update pip by typing the following into the terminal

```bash
pip install --upgrade pip
```

If you get an error, try typing instead:
```bash
python -m pip install --upgrade pip
```

You also need the package `Selenium` as part of the web scraping tool kit we will build up. First let us install a depency for it via

```bash
pip install msgpack
```

We then install `selenium` by entering the following into a terminal:

```bash
pip install selenium
```

`pip` will then go through and install the package we asked for, and any other dependencies.
If this succeeded, the last line it printed out should be:

```
Successfully installed selenium-3.x.0
```

{{% tip %}}
**No administrator rights?**

If you do not have administrator rights to the computer you are using,
please install packages only for your account.
You can do so by typing `pip install --user packagename`, e.g., `pip install --user selenium`.

{{% /tip %}}

## More Packages

Please also install the following packages:

```bash
pip install textblob
```
