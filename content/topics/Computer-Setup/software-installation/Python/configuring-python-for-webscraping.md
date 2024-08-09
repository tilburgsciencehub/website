---
title: "Configure Python for Web Scraping"
description: "Learn to web scrape using ChromeDriver, Selenium, and Webdriver manager for python. Web scraping using an automated browser by installing ChromeDrive"
keywords: "web scraping, scraping, automation, browser, chromedriver, install chromedriver, selenium"
weight: 5
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /configure/python-for-scraping
  - /get/chromedriver
---

## Overview

Web scraping often requires automating a web browser to gather information, especially when dealing with sites that dynamically load content using JavaScript. 

This guide will show you how to set up your environment to use the package [ChromeDriver](https://chromedriver.chromium.org) with Selenium and WebDriver Manager for Python. We will show you two different ways of installing these tools below.

## Install ChromeDriver

Before installing ChromeDriver, make sure you have the following already installed:

* [Google Chrome](https://www.google.com/chrome/browser/desktop/index.html).

* *Selenium*: Install it using the command `pip install selenium`. 
  - Alternatively, you can install it via Anaconda Prompt (Windows) or the Terminal (Mac) with the command `conda install selenium`, and agreeing to whatever the package manager wants to install or update (usually by pressing `y` to confirm your choice).

* *Webdriver Manager for Python*: Install it using the command `pip install webdriver_manager`.

Once these packages are installed, you can set up ChromeDriver with the following Python code: 

{{% codeblock %}}
```Python
# Make selenium and chromedriver work for Untappd.com

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://untappd.com/"
driver.get(url)

```
{{% /codeblock %}}

## Manually Installing ChromeDriver

If the automatic installation does not work, or if you simply prefer to install ChromeDriver manually, follow the instructions for your operating system below. 

### Windows Users

Watch our YouTube video, in which we walk you through the setup on Windows.

{{< youtube l2aRxtYN3eY iframe-video-margins >}}

*   Install Google Chrome from [here](https://www.google.com/chrome/browser/desktop/index.html).
*   Download the windows version of Chromedriver from [here](https://chromedriver.storage.googleapis.com/index.html?path=2.41/).
*   Extract the contents of the zip file into a new directory under `C:\chromedriver`. If you do not have admin rights, you can use a different folder, like `C:\Program Files\chromedriver`, or `C:\Users\[your-username]\chromedriver`. The exact location of the file does not matter, as long as you remember where you placed it. (However, it's not advisable to leave it in your Downloads folder.)
*   Make sure that the chromedriver.exe file is directly under the PATH you specified, i.e. under `C:\chromedriver` (or an alternative path). If your zip unpacker created a new folder with a different name inside your specified folder, move the .exe file to that path.
*   Add the directory `C:\chromedriver` (or whichever directory you chose above) to your PATH as described before (for instructions, see below)
*   If this went successfully, open a terminal/command prompt, and enter `chromedriver --version`, you should get output that looks like `ChromeDriver [version number]`

{{% warning %}}
*Adding ChromeDriver to PATH on Windows.*

We need to update our PATH settings; these settings are a set of directories that Windows uses to "look up" software to startup.

- Open the settings for environment variables
  - Right-click on Computer.
  - Go to "Properties" and select the tab "Advanced System settings".
  - Choose "Environment Variables"
- Alternatively, type "environment variable" (Dutch: omgevingsvariabelen) in your Windows 10 search menu, and press Enter.

-  Select `Path` from the list of user variables. Choose `Edit`.
- **Windows 7 and 8 machines:**
	If you chose your installation directory to be `C:\chromedriver` during your installation (i.e., you did use the default directory), copy and paste the following string without spaces at the start or end:

        `;C:\chromedriver`

- **Windows 10 machines:**
	- Click `New` and paste the following string:

        `C:\chromedriver`

	- Click on `OK` as often as needed.
{{% /warning %}}

### Mac Users

#### Let's install Homebrew first!

* Make sure your `Homebrew` package is installed and up-to-date. To do so, open a terminal and enter:

{{% codeblock %}}
```bash
brew update
```
{{% /codeblock %}}

If `Homebrew` is not installed, an error will return. 

* To install Homebrew, open a terminal and paste the following command:

{{% codeblock %}}
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
{{% /codeblock %}}

* Verify the installation by entering the following command into your terminal:

{{% codeblock %}}
```bash
brew doctor
```
{{% /codeblock %}}

You should see the following output:

```bash
Your system is ready to brew
```

Sometimes, `brew doctor` returns some warnings. While it's advisable to fix them (eventually), you typically don't have to do it to get started with Chromedriver - so just try to continue from here.

#### Let's proceed to installing Chromedriver

* We assume you have Google Chrome installed. If not, do this first, please.

*   Install `chromedriver` via Homebrew with:

{{% codeblock %}}
```bash
brew install chromedriver --cask
```
{{% /codeblock %}}

*   Verify the installation by running the following in the terminal:

```bash
chromedriver --version
```

The expected output is the version number (`ChromeDriver XX`).

### Linux Users

*   Open a terminal session
*   Install Google Chrome for Debian/Ubuntu by pasting the following and then pressing `Return`:

{{% codeblock %}}
```bash
sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
```
{{% /codeblock %}}

*   Install `xvfb` for "headless" browsing with:

{{% codeblock %}}
```bash
sudo apt-get install xvfb
```
{{% /codeblock %}}


*   Install Chromedriver with:

{{% codeblock %}}
```bash
sudo apt-get install unzip

wget -N https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```
{{% /codeblock %}}

*   Verify the installation by running the following in the terminal:

{{% codeblock %}}
```bash
chromedriver --version
```
{{% /codeblock %}}

You should see the version number if the installation was successful.