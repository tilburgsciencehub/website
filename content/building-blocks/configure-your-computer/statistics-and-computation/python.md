---
title: "Set up Python"
description: "Python is widely use programming language. Learn how to set it up on your computer."
keywords: "install, python, anaconda, conda, distribution, configure, PATH, statistics"
#date: 2020-11-11T22:02:51+05:30
draft: false
#weight: 3
aliases:
  - /get/python
  - /install/python
  - /setup/python/
  - /tutorials/other-category/implement-an-efficient-and-reproducible-workflow/setup/python.md
---

## Installing Anaconda Python

Anaconda is a pre-packaged Python distribution for scientific users. To customize Python with packages and properly use it in combination with [automation tools](/building-blocks/configure-your-computer/automation-and-workflows/make/), we prefer a *locally installed Anaconda distribution* over cloud-based alternatives.

Watch our YouTube video, in which we walk you through the setup on Windows.

{{< youtube hGZSAuDcmQc iframe-video-margins >}}

### Instructions
Direct your browser to [Anaconda download page](https://www.anaconda.com/download/) and download the Python 3.x Graphical Installer for your machine.
Sometimes, the download defaults to Mac, so if you're on Windows or Linux, make sure to select the right version.

Then, follow the steps provided on the website.

{{% warning %}}
During the installation you will be asked whether you want Anaconda Python to be added to your PATH. **Click yes!**
Even if the installation window gives a warning about adding it to your PATH, please still check that box.
{{% /warning %}}

Note that the installation of Anaconda may take about 5-10 minutes, dependening on how fast your computer is.

{{% warning %}}
**For Windows Users**

*   When asked if you want single or multiple user installation, choose **single user**.
*   Accept all defaults that are set in the installation window.
*   Check the box for adding Anaconda to your PATH.
*   In the last step, you are asked if you want Visual Studio, click **Yes**.
{{% /warning %}}
{{% warning %}}
**For Linux Users**

For some users Python was not added to the path. To quickly do this, please open a terminal window, paste ```echo '$HOME/anaconda3/bin:$PATH' >> ~/.bashrc``` and press `Return`.
{{% /warning %}}

## Verifying that the installation was successful

To verify that the correct version of Python has been installed and was made available in your PATH settings, close your terminal and open a **new** terminal interface and enter:


```bash
python --version
```
followed by hitting the `Return` key.

You should see the following information returned:

### Windows users

```bash
Python 3.x.x :: Anaconda, Inc.
```

### Mac & Linux/Ubuntu users

```bash
Python 3.x.x :: Anaconda custom (64-bit)
```

{{% tip %}}
**Python 2 versus Python 3**

Python 2 and 3 are incompatible in syntax.
If you had Python 2 previously installed on your machine,
you might have seen `Python 2.x.x` above. In that case try typing

```python3 --version```

instead. Now you should see a message like the one above and are good to go.

{{% /tip %}}
