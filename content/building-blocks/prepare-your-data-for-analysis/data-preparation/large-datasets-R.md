---
title: "Import Large Datasets Into R"
description: "Importing large datasets in R is made easy by data.table R package. The package makes importing and manipulating huge datasets (like big data) in R faster"
weight: 2
keywords: "import, data, data preparation, big data, large datsets, memory, RAM, data.table, big data, R"
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /import/large-datsets
---

## Overview

Many R-users rely on the `dplyr` or `read.table` packages to import their datasets as a dataframe. Although this works well for relatively small datasets, we recommend using the `data.table` R package instead because it is significantly faster. This building block provides you with some practical tips for dealing with large datsets in R.

## Code
As a starting point, make sure to clean your working environment in RStudio. Oftentimes, there are datasets stored memory that you have worked with earlier but you're no longer using. Click on the broom icon in the top right window to remove all objects from the environment. 

In addition, switching from the `read.csv()` function to `fread()` can greatly improve the performance of your programme in our experience. Below we illustrate how you can import a (subset of the) data, determine the object size, and store the derivative version of the file for future use.


{{% codeblock %}}
```R
# import package
library(data.table)

# import data with data.table package
df <- fread(<YOUR_DATASET.csv>)

# only import the first couple of rows for exploratory analysis 
df <- fread(<YOUR_DATASET.csv>, nrows=500)

# only import the data you actually use 
df <- fread(<YOUR_DATASET.csv>, select=c(1, 2, 5))  # column indices
df <- fread(<YOUR_DATASET.csv>, select=c("date", "country", "revenue"))  # column names

# print object size in bytes (for a quick comparison)
object.size(df)

# store the derivative file for future use
fwrite(df, <YOUR_CLEANED_DATSET.csv>)
```
{{% /codeblock %}}
