---
title: "Import Large Datasets Into R"
description: "Importing large datasets in R is made easy by data.table R package. The package makes importing and manipulating huge datasets (like big data) in R faster"
weight: 2
keywords: "import, data, data preparation, big data, large datsets, memory, RAM, data.table, big data, R, dataframe, object size"
date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /import/large-datsets
---

## Overview
Many R-users rely on the `dplyr` or `read.table` packages to import their datasets as a dataframe. Although this works well for relatively small datasets, we recommend using the `data.table` R package instead because it is significantly faster. This building block provides you with some practical tips for dealing with large datasets in R.

## Code

Switching from the `read.csv()` function to `fread()` can greatly improve the performance of your program. The code block below illustrates how you can import your whole dataset as well as subsets of it, determine the size of the resulting object, and store your new/clean versions of the data as a new file for future use.

{{% tip %}}

Oftentimes, datasets you previously worked with remain stored in memory, even if they're no longer in use. Click on the broom icon in the top right window to remove all objects from the environment. By removing objects which are no longer in use you will help improve RStudio's performance and reduce the risk of errors and conflicts.

{{% /tip %}}


{{% codeblock %}}
```R
# import package
library(data.table)

# import data with data.table package
df <- fread("YOUR_DATASET.csv")

# only import the first couple of rows for exploratory analysis 
df <- fread("YOUR_DATASET.csv", nrows=500)

# only import the data you actually use 
df <- fread("YOUR_DATASET.csv", select=c(1, 2, 5))  # column indices
df <- fread("YOUR_DATASET.csv", select=c("date", "country", "revenue"))  # column names

# print object size in bytes (for a quick comparison)
object.size(df)

# store the derivative file for future use
fwrite(df, "YOUR_CLEANED_DATSET.csv")
```
{{% /codeblock %}}
