---
title: "Export Your Tables for Print-ready Publications"
description: "Learn how to quickly and efficiently export your tables for your paper."
keywords: "stargazer, latex, paper, lyx, r"
weight: 104
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /export/tables
  - /use/stargazer
---

## Overview

**[Stargazer](https://www.rdocumentation.org/packages/stargazer/versions/5.2.2/topics/stargazer)** is an easy-to-use R package that creates nicely-formatted, high-quality tables from your R data in ASCII, {{< katex >}}\LaTeX{{< /katex >}}, and HTML code.

It automatically recognizes the kind of data you provide. If you provide a set of regression model objects, it will produce a regression table. Instead, if you feed it with a data frame, it will produce a summary statistics table.

## An Example

Convert regression coefficients of `mdl_1` and `mdl_2` into a HTML file that can be copied into a paper.

{{% codeblock %}}
```R
library(stargazer)

stargazer(mdl_1, mdl_2,
          title = "Figure 1",
          column.labels = c("Model 1", "Model 2"),
          type="html",
          out="output.html"  
          )
```
{{% /codeblock %}}
