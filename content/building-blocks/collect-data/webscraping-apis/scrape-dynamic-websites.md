---
title: "Scrape Dynamic Websites"
description: "Learn how to scrape data and information from dynamic websites."
keywords: "scrape, webscraping, internet, beautifulsoup, website"
#weight: 2
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /scrape/dynamic-website
  - /collect-data/scrape-dynamic-websites
---

## Overview
While it's easy to get started with Beautifulsoup, it has limitations when it comes to dynamic websites. That is, websites of which the content changes after each page refresh. Selenium can handle both static and dynamic websites and mimic user behavior (e.g., scrolling, clicking, logging in). It launches another web browser window in which all actions are visible which makes it feel more intuitive. Here we outline the basic commands and installation instructions to get you started.

## Code

### Selenium

#### Finding content in a website's source code
Running the code snippet below starts a new Google Chrome browser (`driver`) and then navigates to the specified URL. In other words, you can follow along with what the computer does behind the screens. Next, you can obtain specific website elements by tag name (e.g., `h1` is a header) similar to BeautifulSoup.

{{% codeblock %}}
```Python
import selenium.webdriver

driver = selenium.webdriver.Chrome()
driver.get("https://www.abcdefhijklmnopqrstuvwxyz.nl")

# retrieve first H1 header
driver.find_element_by_tag_name("h1").text
```
{{% /codeblock %}}


{{% tip %}}
The first time you will need to (1) install the Python package for Selenium, (2) download a web driver to interface with a web browser, and (3) configure Selenium to recognize your web driver.

Check our [page](https://tilburgsciencehub.com/building-blocks/configure-your-computer/task-specific-configurations/configuring-python-for-webscraping/) on Configuring Python for Web Scraping to learn how to do it.

{{% /tip %}}

#### Selectors
Alternatively, you can specify which elements to extract through attributes, classes and identifiers:

{{% codeblock %}}
```Python
# HTML classes
driver.find_element_by_class_name("<CLASS_NAME>").text  

# HTML identifiers ()
driver.find_element_by_id("<ID_NAME>").text

# XPath
driver.find_element_by_xpath("<XPATH>").text

```
{{% /codeblock %}}


{{% tip %}}
Within Google Inspector you can easily obtain the XPath by right-clicking on an element and selecting: "Copy" > "Copy XPath".
{{% /tip %}}


#### User interactions
One of the distinguishable features of Selenium is the ability to mimic user interactions which can be vital to get to the data you are after. For example, older tweets are only loaded once you scroll down the page.

{{% codeblock %}}
```Python
# scroll down the page
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# click on element (e.g., button)
element_to_be_clicked = driver.find_element_by_class_name("<CLASS_NAME>")
element_to_be_clicked.click()
```
{{% /codeblock %}}


## Advanced Use Case

### Task Scheduling
See the building block on [task automation](http://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/) on how to schedule the execution of the web scraper (e.g., every day). Keep in mind that this only works with Python scripts, so if you're currently working in a Jupyter Notebook you need to transform it into `.py` file first.


## See Also
* Looking for a simple solution that does the job without any bells and whistles? Try out the BeautifulSoup package and review [this](https://tilburgsciencehub.com/building-blocks/scrape/static-website) complementary building block.
