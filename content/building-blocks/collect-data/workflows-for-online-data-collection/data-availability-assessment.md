---
title: "Assess what Data is Available"
description: "Learn how to assess which particular data is available on the site or API."
keywords: "data availability, assessment, API, webscraping, scraping"
#weight: 1
#date: 2021-03-05T22:01:14+05:30
draft: false
aliases:
  - /assess/data-availability
---

## Overview

Assessing data availability is vital to guarantee a minimum level of rigor. Investigating data availability may help you to enhance the relevance of your study.

## Entity Coverage and Linkages

### Which entities are available?

Familiarize yourself with the structure of the website or API to understand which entities (e.g., consumers, products, reviews) are available.

{{% example %}}
An e-commerce website like Amazon lists information on the products, sellers, reviews, and reviewers.
{{% /example %}}

### How many entities are available?
Try to understand how many entities are available on the site, and how many of those you can actually retrieve.

{{% example %}}
The category pages on Amazon.com only list a few hundred products - out of potentially ten thousand products per category. So, while it seems data is abundantly available, it’s not so straightforward that all data can be retrieved easily.
{{% /example %}}

### How are entities identified?
The location of most entities typically consists of a URL of a website or API appended with an identification number.

{{% example %}}
Amazon uses ASINs (UPCs) to point to a product page (e.g., https://www.amazon.com/dp/B087BC4DJH/), and the same ID is used to also point to the review pages (e.g., https://www.amazon.com/product-reviews/B087BC4DJH/).
{{% /example %}}

### How are entities linked to one another?
A crucial assessment to make is how entities are linked to one another, if at all.

{{% example %}}
The product overview pages at Amazon list the ASINs of each product in the website’s source code. Using this list, you can then visit the product pages of each product, and thereby start constructing your data set.
{{% /example %}}

### How can entities be linked to external entities?

After assessing the internal linkage structure, critically reflect on how entities may potentially be linked to external data sources.

{{% example %}}
In its early days, music intelligence provider Echonest.com allowed users to query their API for so-called Musicbrainz IDs. These identifiers were and still are used widely by other services.
{{% /example %}}

### Which lists could serve as potential seeds?

Which entities serve as an entry point for your data collection? These “entry points” are commonly referred to as “seeds”.

{{% example %}}
Datta et al. (2018) visited the service’s “recently active users” page for 1 month, collecting thousands of user names, from which a final sample of 5,000 users was drawn that entered the actual data collection.
{{% /example %}}

## Time Coverage

### For what period is data available?
The period that your website or API covers.

{{% example %}}
Amazon lists historical data on reviews which means you can easily go back in time and download all of these reviews.
{{% /example %}}

### How is time encoded, and how accurate is it?

Timestamps can be given in a user's time zone but also in UTC. Check whether you need to convert the time to a common format for storage. Also, check for the accuracy of the timestamps as some providers aggregate timestamps in descriptions (e.g., "more than a year ago")

{{% example %}}
In the Spotify playlist data retrieved via the Chartmetric API, most of the music tracks have been added to playlists in January, 2016. However, that does not mean it took place like this. The addition dates in January, 2016 merely reflect the starting point of Chartmetric’s data collection.
{{% /example %}}

### Can data be modified after it has been published?

What looks like archival data does not need to be strictly archival. Users can often change and delete their contributions after publication.

{{% example %}}
Social music network Last.fm set the bootstrap flag to 1 in case users have reset their profiles, which may render their historical data incomplete.
{{% /example %}}

### How often is the site/endpoint refreshed?

When you plan to scrape data in real-time from a website, try to get a feeling for how often the site is actually refreshed. This may help you to decide how often you need to collect data from the site.


## Algorithmic Transparency

### Which mechanisms affect the display of data?

Design choices and algorithms that make a site easily navigable can cause problems in collecting and using data for scientific purposes. Typical mechanisms that affect the display and retrieval of data are sorting algorithms, recommendation algorithms, experimental conditions, and sampling.

{{% example %}}
Suppose you want to calculate average prices in a product category, and you start scraping data from Amazon.com. Chance is you’ll end up scraping prices for only the most popular products - which certainly are not representative of the whole product assortment on the platform.
{{% /example %}}

### Can the researcher exert control over the data display?

When screening a site for data availability, it’s crucial to look out for options to exert control over which data is shown.

{{% example %}}
You can sort products alphabetically, which - arguably - isn’t related to popularity, and may hence be a better sampling scheme if you’re interested in random samples.
{{% /example %}}
