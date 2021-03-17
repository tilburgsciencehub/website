---
title: "Learn Web Scraping"
description: "Learn how to scrape information from websites."

keywords: "learn, website, webscraping, scraping, internet, beautifulsoup"
weight: 3
date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /collect-data/web-scraping
---

## Overview
Say that you want to capture and analyze data from a website. Of course, you could simply copy-paste the data from each page. But, of course, this manually executed job would have severe limitations. What if the data on the page gets updated (i.e., would you have time available to copy-paste the new data, too)? Or what if there are simply so many pages that you can't possibly do it all by hand (i.e., thousands of product pages)?

Web scraping can help you overcome these issues by *programmatically* grabbing data from the web. Before we can extract/grab/capture elements from a website, we need a bit of background on how websites work technically, so let's focus on that first.

## Code

### Requests

The `get()` method of the `requests` package offers a straightforward way to store the source code of a website into Python.

{{% codeblock %}}

```python
import requests

url = "https://www.abcdefhijklmnopqrstuvwxyz.nl"

# make a get request to the URL
request_object = requests.get(url)

# return the source code from the request object
source_code = request_object.text
```
{{% /codeblock %}}

### Beautifulsoup

#### Finding content in a website's source code 
While the `.find()` method always prints out the first matching element that it finds, the `find_all()` method captures all of them and returns them as a list. More often that not, you are specifically interested in the text you have extracted and less so in the HTML tags. To get rid of them, you can use the `.get_text()` method. 

{{% codeblock %}}
```Python
from bs4 import BeautifulSoup

soup = BeautifulSoup(source_code, "html.parser")

# the first matching <h1> element
print(soup.find('h1'))

# all matching <h2> elements (returns a list of elements)
print(soup.find_all('h1'))

# first elementin in the list
print(soup.find_all('h2')[0])

# strip HTML tags from element
print(soup.find_all('h2')[0].get_text())
```
{{% /codeblock %}}


{{% tip %}}
In practice, you often find yourself in situations that require chaining one or more commands, for example: `soup.find('table').find_all('tr')[1].find('td')` looks for the first column (`td`) of the second row (`tr`) in the `table`.
{{% /tip %}}

#### Selectors

You can further specify which elements to extract through HTML attributes, classes and identifiers: 

{{% codeblock %}}
```Python
# element attributes
soup.find("a").attrs["href"]

# HTML classes (note the underscore!)
soup.find(class_ = "<CLASS_NAME>")

# HTML identifiers
soup.find(id = "<ID_NAME>")
```
{{% /codeblock %}}


{{% tip %}}
You can combine HTML elements and selectors like this:   
```soup.find("h1", class_ = "menu-header"]```
{{% /tip %}}


### Selenium
#### Finding content in a website's source code 
While it's easy to get started with Beautifulsoup, it has limitations when it comes to dynamic websites. That is, websites of which the content changes after each page refresh. Selenium can handle both static and dynamic websites and mimic user behavior (e.g., scrolling, clicking, logging in). It launches another web browser window in which all actions are visible which makes it feel more intuitive. 

{{% codeblock %}}
```Python
import selenium.webdriver

driver = selenium.webdriver.Chrome()
driver.get("https://www.abcdefhijklmnopqrstuvwxyz.nl")
```
{{% /codeblock %}}


{{% tip %}}
The first time you will need to (1) install the Python package for Selenium, (2) download a web driver to interface with a web browser, and (3) configure Selenium to recognize your web driver.
1. Open Anaconda Prompt (Windows) or the Terminal (Mac), type the command `conda install selenium`, and agree to whatever the package manager wants to install or update (usually by pressing `y` to confirm your choice). 
2. Once we run the scraper, a Chrome browser launches which requires a web driver executable file. Download this file from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) (open [this](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have) site in Chrome to identify your current Chrome version). 
3. Unzip the file and move it to the same directory where you're running this notebook. Either you can set a `chrome_path` manually (e.g., `/Users/Pieter/Documents/webscraping/chromedriver`) or ideally you make Chromedriver available through a so-called PATH variable so that you can access it regardless of your current directory. To do so, ...
    * Windows users can follow the steps described [here](https://tilburgsciencehub.com/building-blocks/configure-your-computer/task-specific-configurations/configuring-python-for-webscraping/). If that doesn't work for you, [this](https://zwbetz.com/download-chromedriver-binary-and-add-to-your-path-for-automated-functional-testing/) guide may help.
    * Mac users need to move the `chromedriver` file to the `/usr/local/bin` folder. `cd` to the directory of the `chromedriver` file and type `mv chromedriver /usr/local/bin`.
{{% /tip %}}

#### User interactions
One of the distinguishable featuers of Selenium is the ability to mimic user interactions which can be vital to get to the data you are after. For example, older tweets are only loaded once you scroll down the page.

{{% codeblock %}}
```Python
# scroll down the page 
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# click on element (e.g., button)
element_to_be_clicked = driver.find_element_by_class_name("<CLASS_NAME>")
element_to_be_clicked.click()
```
{{% /codeblock %}}


## Advanced Use Cases

### Timers

Sending many requests at the same time can overload a server. Therefore, it's highly recommended to pause between requests rather than sending them all simultaneously. This avoids that your IP address (i.e., numerical label assigned to each device connected to the internet) gets blocked, and you can no longer visit (and scrape) the website.

{{% codeblock %}}
```Python
from time import sleep
sleep(5)
print("I'll be printed to the console after 5 seconds!")
```
{{% /codeblock %}}

### Task Scheduling
See the building block on [task automation](http://localhost:1313/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/) on how to schedule the execution of the web scraper (e.g., every day). Keep in mind that this only works with Python scripts, so if you're currently working in a Jupyter Notebook you need to transform it into `.py` file first.


### Seed Generation


{{% codeblock %}}
```Python
base_url = # the fixed part of the URL that stays the same
num_pages = # the number of pages you're after
page_urls = []

for counter in range(1, num_pages):
  full_url = base_url + "page-" + str(counter) + ".html"
  page_urls.append(full_url)
```
{{% /codeblock %}}

{{% tip %}}
Rather than inserting a fixed number of pages (`num_pages`), you may want to leverage the page navigation menu instead. For example, you could extract the next page url (if it exists) from a "Next" button.  
{{% /tip %}}

