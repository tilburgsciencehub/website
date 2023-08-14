---
title: "Avoid Getting Blocked While Scraping"
description: "Take steps to make sure your scraper keeps on running!"
keywords: "scrape, webscraping, headers, timers, proxies"
#weight: 3
#date: 2020-11-11T22:02:51+05:30
draft: false
icon: "fa-solid fa-database"
category: "reproducible"
aliases:
  - /scrape/avoid-getting-blocked
  - /collect-data/avoid-getting-blocked
---

## Overview
For better or worse, web servers can implement anti-scraping measures. For example, they want to protect users' privacy and avoid overloading their server by blocking unsuspicious traffic. To ensure the consistency of your data collection, it's therefore recommended to take steps to make sure your scraper keeps on running!

## Code

### Timers
Briefly pausing between requests, rather than constantly visiting the same website, avoids that your IP address (i.e., numerical label assigned to each device connected to the internet) gets blocked, and you can no longer visit (and scrape) the website. For example, the `sleep` method below forces Python to wait for 5 seconds before it proceeds and executes the print statement.

{{% codeblock %}}
```Python
from time import sleep
sleep(5)
print("I'll be printed to the console after 5 seconds!")
```
{{% /codeblock %}}


### HTTP Headers
Every time you visit a website meta-data associated with your HTTP request is sent to the server. This way, the server can distinguish a regular visitor from a bot or scraper, and may even decide to limit certain functionalities on the website. Some websites will automatically block requests with headers that indicate that they are accessing their server with a script rather than a regular web browser. Fortunately, you can work around this by passing a `headers` object to the `request` to set the meta-data to whatever you want.

{{% codeblock %}}
```Python

headers = {'User-agent': 'Mozilla/5.0'}

# you can also replace the user agent with the exact
# user agent you are using on your computer.
# just visit https://www.whatismybrowser.com/detect/what-is-my-user-agent/
# to find out what your user agent is.

requests.get(url, headers=headers)
```
{{% /codeblock %}}

The most common headers types are:
* User-agent =  a string to tell the server what kind of device and browser you are accessing the page with. The Scrapy user agent [package](https://pypi.org/project/scrapy-user-agents/), for example, randomly rotates between a list of [user agents](https://developers.whatismybrowser.com/useragents/explore/software_name/googlebot/).
* Accept-Language = preferred language (e.g., Russian may be more suspicious for a Dutch client's IP location).
* Referrer = the previous web page’s address before the request is sent to the web server (e.g., a random origin website seem more plausible)


### Proxies
The idea is that you use an IP address that is not your own. Hence, if get blocked, you switch to another IP address. Either you can use a package like [`scrapy-proxy-pool`](https://github.com/rejoiceinhope/scrapy-proxy-pool) or you use a Virtual Private Network (VPN) to alternate between IP addresses.

There are also many for-pay services, such as https://scraperapi.com, and https://zyte.com.
