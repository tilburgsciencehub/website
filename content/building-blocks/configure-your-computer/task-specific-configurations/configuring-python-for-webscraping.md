---
title: "Configuring Python for Web Scraping"
description: "Learn to web scrape using ChromeDriver, Selenium, and Webdriver manager for python. Web scraping using an automated browser by installing ChromeDrive"
keywords: "web scraping, scraping, automation, browser, chromedriver, install chromedriver, selenium"
weight: 2
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /configure/python-for-scraping
  - /get/chromedriver
---

# Web Scraping Using an Automated Browser

Sometimes when we scrape the web, we need to automate our computer to open a web browser to gather information from each page. This is especially true when the site we want to scrape has content that is loaded dynamically with javascript.

We will install one package to help us here: [ChromeDriver](https://chromedriver.chromium.org). Below we show two different ways of installing it.

## Install ChromeDriver

In order to install ChromeDriver, make sure you have already installed:

* [Google Chrome](https://www.google.com/chrome/browser/desktop/index.html).

* **Selenium**: by typing in the command `pip install selenium`.
  - Alternatively, open Anaconda Prompt (Windows) or the Terminal (Mac), type the command `conda install selenium`, and agree to whatever the package manager wants to install or update (usually by pressing `y` to confirm your choice).

* **Webdriver Manager for Python**: by typing in the command `pip install webdriver_manager`

Once you have obtained these packages, you can now install ChromeDriver as follows:
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
If for any reason the prior did not work or if you simply prefer installing ChromeDriver manually, follow the operating-system-specific steps below.

### Windows Users

Watch our YouTube video, in which we walk you through the setup on Windows.

{{< youtube l2aRxtYN3eY iframe-video-margins >}}

*   Install Google Chrome from [here](https://www.google.com/chrome/browser/desktop/index.html).
*   Download the windows version of Chromedriver from [here](https://chromedriver.storage.googleapis.com/index.html?path=2.41/).
*   Extract the contents from the zip file, and extract them into a new directory under `C:\chromedriver`. If you do not have admin rights, you can put the file also in another folder, for example `C:\Program Files\chromedriver`, or `C:\Users\[your-username]\chromedriver`. It does not matter where exactly the file will be put, as long as you remember where it is (it's not a good idea though to leave it in your downloads folder).
*   Make sure that the chromedriver.exe file is directly under the PATH you specified, i.e. under `C:\chromedriver` (or an alternative path). If your zip unpacker created a new folder with a different name inside your specified folder, move the .exe file to that path.
*   Add the directory `C:\chromedriver` (or whichever directory you chose above) to your PATH as described before (for instructions, see below)
*   If this went successfully, open a terminal/command prompt, and enter `chromedriver --version`, you should get output that looks like `ChromeDriver [version number]`

{{% warning %}}
**Making `chromedriver` available via the PATH settings on Windows.**

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

Make sure your `Homebrew` package is up-to-date. To do so, open a terminal and enter

```
brew update
```

If that returns an error, `Homebrew` is not installed.

- To install Homebrew, open a terminal and paste the following command:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

- To verify that Homebrew installed correctly, enter the following into your terminal

```
brew doctor
```

...and you should see the following output

```
Your system is ready to brew
```

Sometimes, `brew doctor` returns some warnings. While it's advisable to fix them (eventually), you typically don't have to do it to get started with Chromedriver - so just try to continue from here.

#### Let's proceed to installing Chromedriver

* We assume you have Google Chrome installed. If not, do this first, please.

*   Install `chromedriver` via Homebrew:

```
brew cask install chromedriver
```

*   Verify your install, by entering the following in your terminal. The expected output is `ChromeDriver XX`

```
chromedriver --version
```
### Linux Users

*   Open a terminal session
*   Install Google Chrome for Debian/Ubuntu by pasting the following and then pressing `Return`
```
sudo apt-get install libxss1 libappindicator1 libindicator7
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome*.deb
sudo apt-get install -f
```

*   Install `xvfb` so chrome can run 'headless' by pasting the following and then pressing `Return`
```
sudo apt-get install xvfb
```

*   Install Chromedriver by pasting the following and then pressing `Return`:
```
sudo apt-get install unzip

wget -N https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```
*   Your install worked, you should get `ChromeDriver XX` returned if the installation was successful
```
chromedriver --version
```
