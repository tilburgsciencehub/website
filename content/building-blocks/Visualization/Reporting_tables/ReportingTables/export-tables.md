---
title: "Stargazer: Exporting Publication-Ready Tables in R"
description: "Learn how to quickly and efficiently export your tables for your paper."
keywords: "stargazer, latex, paper, lyx, r, table, paper, example, package, html, code, export, exporting, rstudio, code,  publication-ready, tables"
weight: 4
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /export/tables
  - /use/stargazer
  - /building-blocks/share-your-results-and-project/write-your-paper/export-tables/
---

## Overview

Easily transform your R data into beautifully-formatted tables with the aid of **[Stargazer](https://www.rdocumentation.org/packages/stargazer/versions/5.2.3)**, an easy-to-use R package. Regardless of whether you're working with ASCII, {{< katex >}}\LaTeX{{< /katex >}}, or HTML code, Stargazer seamlessly adapts to your preferences. 

This package automatically recognizes the type of data you provide. For example, if you supply a set of regression model objects, it will generate a regression table. Similarly, if you feed it a data frame, it will create a summary statistics table.

## An Example
Let's delve into an example that showcases the power of Stargazer.  

Assume you have regression coefficients from models `mdl_1` and `mdl_2`, and you want to showcase them in a HTML-formatted table, ready to be included in your research paper. 

{{% codeblock %}}
```R
# Load required packages
library(stargazer)
library(dplyr)

# Sample data
data <- data.frame(
  y = c(10, 20, 30, 40, 50),
  x1 = c(2, 3, 4, 5, 6),
  x2 = c(0, 1, 0, 1, 0)
)

# Fit regression models
mdl_1 <- lm(y ~ x1, data = data)
mdl_2 <- lm(y ~ x1 + x2, data = data)

# Create HTML-formatted regression table
stargazer(mdl_1, mdl_2,
          title = "Figure 1",
          column.labels = c("Model 1", "Model 2"),
          type="html",
          out="output.html"  
          )

```
{{% /codeblock %}}

The code above creates an HTML-formatted regression table and the output will be saved as an HTML file. 

{{% tip %}}
To present the results in LaTeX or plain text format instead of HTML, simply change the "type=" function and set it to "latex" or "text". 
{{% /tip %}}






