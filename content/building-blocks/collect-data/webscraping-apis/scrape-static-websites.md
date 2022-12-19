---
title: "Scrape Static Websites"
description: "Learn how to scrape data and information from static websites."
keywords: "scrape, webscraping, internet, beautifulsoup, static website"
#weight: 1
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /scrape/static-website
  - /collect-data/scrape-static-websites
---

## Overview
Say that you want to capture and analyze data from a website. Of course, you could simply copy-paste the data from each page but you would quickly run into issues. What if the data on the page gets updated (i.e., would you have time available to copy-paste the new data, too)? Or what if there are simply so many pages that you can't possibly do it all by hand (i.e., thousands of product pages)?

Web scraping can help you overcome these issues by *programmatically* grabbing data from the web. The tools best suited for the job depend on the type of website: static or dynamic. In this building block, we focus on the former which always return the same information.

## Code

### Requests
Each site is made up of HTML code that you can view with, for example, Google Inspector. This source code contains data about the look-and-feel and contents of a website among others. To store the source code of a website into Python, you can use the `get()` method of the `requests` package:

{{% codeblock %}}

```python
import requests

url = "https://www.abcdefhijklmnopqrstuvwxyz.nl"

# make a get request to the URL
request_object = requests.get(url)

# return the source code from the request object
source_code = request_object.text
```

```
-R-
#install.packages("rvest")
library(rvest)

url = "https://www.abcdefhijklmnopqrstuvwxyz.nl"

# read the html from the URL
source_code = read_html(url)
```
{{% /codeblock %}}

### Seed Generation
In practice, you typically scrape data from a multitude of links (also known as the seed). Generally speaking, each URL has a fixed and variable part. The latter may be a page number that increases by increments of 1 (e.g., `page-1`, `page-2`). The code snippet below provides an example of how you can quickly generate such a list of URLs.

{{% codeblock %}}
```Python
base_url = # the fixed part of the URL
num_pages = # the number of pages you want to scrape
page_urls = []

for counter in range(1, num_pages+1):
  full_url = base_url + "page-" + str(counter) + ".html"
  page_urls.append(full_url)
```
```
-R-
base_url = # the fixed part of the URL
num_pages = # the number of pages you want to scrape
page_urls = character(num_pages)

for (i in 1:num_pages) {
	page_urls[i] = paste0(base_url,"page-",i)}
```
{{% /codeblock %}}

{{% tip %}}
Rather than inserting a fixed number of pages (`num_pages`), you may want to leverage the page navigation menu instead. For example, you could extract the next page url (if it exists) from a "Next" button.  
{{% /tip %}}


### Beautifulsoup

Next, once we have imported he `source_code`, it is a matter of extracting specific elements. The `BeautifulSoup` package has several built-in methods that simplify this process significantly.

#### Finding content in a website's source code
The `.find()` and `.find_all()` methods search for matching HTML elements (e.g., `h1` is a header). While `.find()` always prints out the first matching element, `find_all()` captures all of them and returns them as a list. More often than not, you are specifically interested in the text you have extracted and less so in the HTML tags. To get rid of them, you can use the `.get_text()` method.

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
```
-R-
# the first matching <h1> element
html_element(source_code,'h1')

# all matching <h2> elements (returns a list of elements)
html_elements(source_code,'h2')

# first elementin in the list
html_elements(source_code,'h2')[1]

# strip HTML tags from element
html_text(html_elements(source_code,'h2')[1])
```
{{% /codeblock %}}


{{% tip %}}
In practice, you often find yourself in situations that require chaining one or more commands, for example: `soup.find('table').find_all('tr')[1].find('td')` looks for the first column (`td`) of the second row (`tr`) in the `table`.
{{% /tip %}}

#### Selectors
Rather than searching by HTML tag, you can specify which elements to extract through attributes, classes and identifiers:

{{% codeblock %}}
```Python
# element attributes
soup.find("a").attrs["href"]

# HTML classes (note the underscore after class!)
soup.find(class_ = "<CLASS_NAME>")

# HTML identifiers
soup.find(id = "<ID_NAME>")
```
```
-R-
# element attributes
html_attr(html_elements(source_code,"a"),"href")

# HTML classes (note the . before the class name)
html_elements(source_code,".<CLASS_NAME>")

# HTML identifiers
html_elements(source_code,"#<ID_NAME>>")
```

{{% /codeblock %}}

{{% tip %}}
You can combine HTML tags and selectors like this:   
```soup.find("h1", class_ = "menu-header"]```
{{% /tip %}}


## Advanced Use Case

### Task Scheduling
See the building block on [task automation](http://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/) on how to schedule the execution of the web scraper (e.g., every day). Keep in mind that this only works with Python scripts, so if you're currently working in a Jupyter Notebook you need to transform it into `.py` file first.


## See Also
* If you're aiming to strive a dynamic website, such as a social media site, please consult our building block [web-scraping dynamic websites](/building-blocks/collect-data/webscraping-apis/scrape-dynamic-websites/) building block.
