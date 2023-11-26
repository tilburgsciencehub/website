---
title: "Use Google Colab to Run Python in the Cloud"
description: "Learn Google Colab and collaborate on python code remotely. Our tutorial explains how to run your Jupyter notebook in the cloud on the servers of Google for free"
keywords: "cloud, python, jupyter, slow computer, fast, collaborate, google, google colab, colab python"
date: 2022-04-08T10:01:14+05:30
draft: false
author: "Cas Ruger"
# authorlink: "https:/"
aliases:
  - /use/colab

---

## What is Google Colab?
Colab is a product from Google Research that allows anybody with an internet connection to write and execute python code through a browser. Colab is free to use, and there is no setup on your computer needed. It is especially useful if you have a slow computer since Google hosts your Jupyter notebook and thus uses their GPU free of charge. Or if you want to work together on the same code, since you can collaborate on the same cloud file with multiple editors.

## How to get started
It is time to create your own Colab notebook!


1. Go to https://colab.research.google.com/
2. Press **New notebook**, or if you already have a file, choose this one from the list
3. Save your notebook to either Google drive or GitHub via **File** > **Save a copy in ...**


## How to use Colab
Once you are in your Colab notebook you can use it just like any offline Jupyter notebook.

Type your code in the darker gray box and press the run arrow to run the code. Your output will be placed below the box. To create a new code box, press **+ Code** in the navigation bar.

![A screenshot of Google Colab](../images/googlecolab.jpg)


### Import packages
Colab environment already has a number of pre-installed packages such as ``pandas``, ``pytorch``, ``scipy``, ``tensorflow`` and ``numpy``. To check all installed packages use **pip freeze**
```bash
!pip freeze
```
If a package is already installed, import these by importing them with **import
{packages name}**
```bash
import pandas
```

If a package is not yet installed, install the package inside the Colab notebook by adding the code **!pip install {package name}**
```bash
!pip install cartopy
import cartopy
```

## Adding collaborators
To add other collaborators, go to the right corner and press **Share**. Now choose to either invite people via e-mail or by sending them a link. It is also possible to change the permissions to 'Commenter' or 'Viewer' by pressing ![the gear icon](../images/settings_image.JPG).

### Connect to google drive
If you want to import a dataset or any other file stored on your pc, the easiest way to do so is by connecting Google Colab to your Google drive. To do so, follow the steps below!
1. Upload your files to Google drive
2. Run the following lines in a Colab shell
```bash
from google.colab import drive
drive.mount('/content/drive')
```
3. Press **Connect to Google Drive**
4. Login to your Google account
5. Press **Allow**

You can now import, and export files like you are used to with offline notebooks
