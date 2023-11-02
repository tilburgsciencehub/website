---
title: "Import Large Datasets Into R"
description: "Importing large datasets in R is made easy by data.table R package. The package makes importing and manipulating huge datasets (like big data) in R faster"
weight: 2
keywords: "import, data, data preparation, big data, large datsets, memory, RAM, data.table, big data, R, dataframe, object size"
date: 2023-10-26
author: "Matthijs ten Tije"
draft: false
aliases:
  - /import/large-datsets
---

## Overview
Many R-users rely on the base R `read.csv` command or the `read.table` package to import their datasets as a dataframe. Although this works well for relatively small datasets, we recommend using the `data.table` package or the `readr` package instead because it is significantly faster.  
This building block provides you with some practical tips for dealing with large datasets in R.

### Advantages of the  `data.table` package and the `readr` package

Why should you use the `data.table` package or the `readr` package instead of `read.csv`:

1 **Both `data.table`'s `fread()` and `readr` `read_csv` functions are significantly faster.**

Take for example, loading in this specific dataset containing 1809903 rows and 12 columns, both functions are 2 or 3 times faster than the base R `read.csv` function.

{{% codeblock %}}
```R
library(readr)
library(data.table)

system.time(dt <- read.csv("GB_full.txt")) # Base R
system.time(dt <- read_csv("GB_full.txt")) # readr
system.time(dt <- fread("GB_full.txt")) # data.table
dim(dt)
```
{{% /codeblock %}}


<p align = "center">
<img src = "../img/figure1-import-large-dataset-r.png" width="200">
<figcaption> Downloading time using different packages </figcaption>
</p>



2 **Using `data.table` makes data manipulation with big datasets much quicker than using other popular tools like `dplyr`.**

As easy as the `dplyr` package is, the `data.table` package provides enough room for tasks such as aggregating, filtering, merging, grouping and other related tasks.  
For example: `data.table` has processed the task underneath more than 100x faster than dplyr!

Why is it so fast? Well, it's smart about how it uses your computer's memory. Unlike `dplyr`, which makes a complete new copy of your data during each step, `data.table` just makes a simple reference to the original data. This means it doesn't use up as much memory, making it faster.


{{% codeblock %}}
```R
library(dplyr)

system.time(dt %>% group_by("Variable 1") %>% 
                   filter("Variable 2" == "England") %>%                                     
                   summarise(mean("Variable 3"))) #with dplyr

system.time(dt["Variable 2" =="England", mean("Variable 3"), by = "Variable 1"])
```
{{% /codeblock %}}

<p align = "center">
<img src = "../img/figure2-import-large-dataset-r.png" width="200">
<figcaption> Running time using different packages </figcaption>
</p>

3 **Both `readr` and `data.table` packages are massively quicker when writing files compared to `write.csv()`.**
  
The `fwrite()` function in `data.table` is perfectly suited as well as the `write_csv` function of `readr`.

{{% codeblock %}}
```R
# creating a 1 million by 10 data frame
df <- data.frame(matrix(rnorm(1000000*10), 1000000,10))

system.time({write.csv(my_df, "base.csv", row.names=FALSE) }) # base R
system.time({fwrite(my_df, "datatable.csv") }) # data.table 
system.time({write_csv(my_df, "readr.csv") }) # readr
```
{{% /codeblock %}}

<p align = "center">
<img src = "../img/figure3-import-large-dataset-r.png" width="200">
<figcaption> Writing files running time using different packages </figcaption>
</p>

<br>

## Using the `readr` package to import a large dataset
`read_csv()` from the `readr` package offers several advantages over the base R function `read.csv()`:
- **Integration and Type Detection**: `read_csv()` works well with other tidyverse packages and intelligently determines the data type for each variable.
- **Tibble Output**: Unlike `read.csv()`, which produces a data.frame, `read_csv()` outputs a tibble. Tibbles offer enhanced functionality and behave more consistently when subsetting.
- **Character Variable Handling**: `read_csv()` treats text variables as character variables. 
  In contrast, `read.csv()` automatically converts text to factors, which can be inconvenient.   
  
 Overall, `read_csv()` provides a more efficient and user-friendly approach to data handling in R.

{{% codeblock %}}
```R
# import package 
library(readr)

# Import data with the readr package
df <- read_csv("YOUR_DATASET.csv")

# Import a maximum number of rows for exploratory analysis
df <- read_csv("YOUR_DATASET.csv", n_max  = 500)

# Import data that you want to use
df <- read_csv(("YOUR_DATASET.csv"), col_select = c(1, 3:4)) # column indices
df <- read_csv("YOUR_DATASET.csv", col_select = c("date","country","revenue")) # column names

# store the derivative file for future use
write_csv(df, "YOUR_CLEANED_DATASET.csv")
```
{{% /codeblock %}}

{{% tip %}}

`Readr` comes with several other functions. Such as `read_csv2()` for European-friendly variant comma-separated data, `read_tsv()` for tab-separated data, `read_lines()` for line-by-line file extraction and `read.txt()` reading fixed width data. 

{{% /tip %}}

## Using the `data.table` package to import a large dataset

Switching from the `read.csv()` function to `fread()` can greatly improve the performance of your program. It is often dubbed the "fast and friendly file finagler," and is highly efficient and straightforward to use in R. 

One of its key features is that it is designed to import data from *regularly* delimited files directly into R. Here, "regular" implies that each row in your dataset must have the same number of columns. What sets fread() apart is its ability to automatically detect parameters like **sep**, **colClasses**, and **nrows**, making the data import process straightforward. 

The code block below illustrates how you can import your whole dataset using `fread()` as well as subsets of it, determine the size of the resulting object, and store your new/clean versions of the data as a new file for future use.

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
fwrite(df, "YOUR_CLEANED_DATASET.csv")
```
{{% /codeblock %}}

{{% tip %}}

Oftentimes, datasets you previously worked with remain stored in memory, even if they're no longer in use. In RStudio, click on the broom icon in the top right window to remove all objects from the environment. By removing objects which are no longer in use you will help improve RStudio's performance and reduce the risk of errors and conflicts.

{{% /tip %}}

