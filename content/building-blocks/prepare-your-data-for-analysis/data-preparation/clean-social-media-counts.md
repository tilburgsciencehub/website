---
title: "Clean Data Scraped From Social Media"
description: "This is a handy function that can be used to clean social media data scraped from the web."
weight: 3
keywords: "clean, wrangling, scraping, follow, likes, network"
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /clean/social-media-counts
---

## Overview

This is a handy function that can be used to clean social media data scraped from the web.

Usually, when scraping social media, the output data can contain letters like K's (Thousands), M's (Millions) and B's (Billions). You are won't be able to analyze them unless you first replace these letters with the appropriate zero digits.

## Code

{{% codeblock %}}
```R
# Function to convert textual social media counts to proper digits
social_media_cleanup <- function(x) {
  if (class(x)%in%c('integer','numeric')) {
    warning('Input is already numeric.')
  }
  numerics <- gsub('[A-Za-z]','',x)
  units <- gsub('[0-9]|[.]|[,]','',x)
  multipliers <- rep(1, length(x))
  multipliers[grepl('K', units, ignore.case = T)]<-1000
  multipliers[grepl('M', units, ignore.case = T)]<-1E6
  multipliers[grepl('B', units, ignore.case = T)]<-1E9

  return(as.numeric(numerics)*multipliers)
}

# Example
social_media_cleanup(c('21.5k', '214m', '1204', 'NA', '642b'))
```
{{% /codeblock %}}
