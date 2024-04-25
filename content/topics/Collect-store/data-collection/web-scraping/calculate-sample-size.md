---
title: "Calculate Sample Sizes for Web Scrapers"
description: "Learn how to determine the number of units that can be obtained from a website or API."
keywords: "sample size, sample, n, data collection, compute, sampling, website"
weight: 7
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /calculate/sample-size
  - /collect-data/sample-size-calculation
---

## Overview
Sampling from websites and APIs can be tricky: limits to server load (e.g., retrieval limits) or snowballing effects (e.g., a seed of 100 users, sample 100 of their peers and obtain all of their peers’ consumption patterns for 50 weeks). In addition to the minimum sample size necessary to satisfy statistical power requirements, an important consideration is therefore the *technically feasible sample size*. That is the sample size that can be obtained from a website or API while considering resource constraints.


## Formula

$N = \frac{req \times S}{r \times freq}$

whereby
- $N$ = sample size (i.e., number of instances of an entity to extract data from),
- $req$ = retrieval limit (maximum number of requests per time unit, allowed for each scraper or authenticated API user),
- $S$ = number of scrapers used (e.g., computers with separate IP addresses, or authenticated users of an API),
- $r$ = number of URL calls to make to obtain data for each instance, and
- $freq$ = the desired sampling frequency for each entity per time unit.

{{% tip %}}
Convert all input parameters to the same time unit (e.g., the retrieval limit may initially be expressed in fifteen-minute intervals but needs to match the desired sampling frequency, which may be expressed in hours)!
{{% /tip %}}


## Example
Suppose you wish to know the technically feasible sample size for collecting data from an online social network. In other words, you want to solve for $N$.

The input parameters are:

- $req$ = 5 requests per second = 5 x 60 x 60 requests per hour (18,000)
- $S$ = 1 scraper, authenticated via the service's API
- $r$ = 2 (the scraper needs to visit two URLs: one to obtain users' meta data, and one to obtain users' usage history)
- $freq$ = Each user should be visited at least once every fifteen minutes (once every 15 minutes = 4 times per hour).

$N = \frac{req \times S}{r \times freq} = \frac{18,000 \times 1}{2 \times 4} = 2,250$
