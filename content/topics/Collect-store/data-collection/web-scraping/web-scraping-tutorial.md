---
tutorialtitle: "Web Scraping and API Mining"
title: "Web Scraping and API Mining"
description: "Learn to extract data from the web and APIs"
keywords: "scrape, webscraping, internet, beautifulsoup, static website, dynamic website, website, api, application programming interface"
weight: 1
draft: false
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /learn/web-scraping-and-api-mining
  - /topics/more-tutorials/web-scraping/web-scraping-tutorial/
---

## Overview: Web Scraping vs. API

Web scraping usually involves programmatically collecting content displayed in a web browser. Usually, the websites/ web apps are publicly accessible which enables one to generate the datasets without involving data providers.
On the contrary, API mining usually involves requiring permission from data providers to access their internal databases.

{{% wide-table %}}

|  | Web scraping | Application <br> Programming <br> Interfaces (APIs) |
| --- | --- | --- |
| **Usage scope** | Extract any content <br> displayed in a web <br> browser/websites/apps | Extract any content <br> made available by <br> the API provider |
| **Data extraction & <br> content format** | Browse the website <br> programmatically and <br> extract information <br> available in the website’s <br> HTML source code | Extract information <br> directly from API <br> interfaces which are <br> typically in JSON or <br> XML format |
| **Cost** | Free | Usually on a <br> subscription but <br>  some can be free |
| **Scalability** | Moderate | High |
| **Legal risks** | Low-high | Low-moderate |
| **Example sources** | E-commerce (amazon.com); <br> Online review (yelp.com) | Discussion forum <br> (Reddit API); <br> Social media <br> (Twitter API) |

{{% /wide-table %}}

## Objectives of this tutorial
- Learn how to scrape static websites
- Learn how to scrape dynamic websites
- Familiarize yourself with techniques to avoid getting blocked while scraping
- Learn how to extract data from APIs
- Learn how to convert the API mined data into compatible formats
- Configuring environment variables


## Web Scraping

### Prerequisites
In order to web scrape using an automated browser, you need to first set up Python and install ChromeDriver.

Follow [this](/configure/python-for-scraping) building block for further instructions and code snippets.

### Scrape static websites
The large scale of data collection from many web pages at once might be a key challenge when extracting data from static websites.

In order to scrape a static website, one has to first store the source code of a website (which is in HTML format) into Python. Then, you generate seeds which are basically the multitude of links from which you scrape data. Finally, in order to extract specific elements from the imported HTML source code- use the `BeautifulSoup` package.

Follow [this](/scrape/static-website) building block for more instructions and code snippets.

### Scrape dynamic websites
Scraping dynamic websites comes with another challenge as the data on such pages keep updating. The applicability of `BeatifulSoup` reaches its limit in this case and the `Selenium` package proves to be superior in handling both dynamic and static websites.

Follow [this](/scrape/dynamic-website) building block for more instructions and code snippets.

### Avoid getting blocked while scraping
Web scraping may not be as smooth of a ride after all with some web servers implementing anti-scraping measures. Some possible solutions:

- **Timers**: This technique involves pausing between extraction requests.
- **HTTP Headers**: The meta-data associated with one’s HTTP request is sent to the server everytime a website is visited in order to distinguish a regular visitor from a bot or scraper. One can circumvent this issue by changing the meta-data set up.
- **Proxies**: This approach involves alternating between IP addresses.

Follow [this](/scrape/avoid-getting-blocked) building block for more instructions and code snippets to execute the solutions.

## API Mining
Here are some code snippets that guide you through each step of API mining:

- Step 1: [Extract data from APIs](/collect-data/extract-data-api)
- Step 2: [Read & Write data from API](/collect-data/read-write-data-api)


For API authentication purposes, you may need to access some personal credentials or secret keys and creating environment variables comes handy in such cases.
- [Learn how to configure environment variables](/configure/environment-variables)
