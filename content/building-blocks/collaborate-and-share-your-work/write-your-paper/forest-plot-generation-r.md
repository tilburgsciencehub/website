---
title: "Forest Plot Generation in R"
description: "Forest Plots in R - using forest plots to gain insights on your data"
keywords: "data, visualization, r, forest, plot"
date: 2023-10-10
weight: 3
author: "Matteo Zicari"
authorlink: "https://www.linkedin.com/in/matteozicari/"
aliases:
  - /visualize/data
  - /r/forest plots
---

## Overview

`Forest plots` are a visual representation of findings from various scientific studies that investigate a common research question. They find significant application in the field of `meta-analysis`, a type of statistical analysis that combines and examines results from a number of independent studies. 
More practically, forest plots identify a statistic that is common to such set of studies and report the various instances of that statistic. This, in turn, allows to compare the different results and the significance of the overall pooled summary effect. <br/>
<br/>

Among the **benefits** of forest plots, we find:

* clear and concise `visual representation` of results;
* `effect size` and `confidence interval` comparison across different studies;
* overall, useful tool to evaluate the consistency and strength of evidence, identify potential sources of bias, 
  and make informed judgments about the effect of interventions or exposures.


## Code 

One of the most popular packages used for forest plots is [forestploter](https://cran.r-project.org/web/packages/forestploter/vignettes/forestploter-intro.html). Compared to other packages (e.g., forestplot), `forestploter` focuses entirely on forest plots, which are treated as a table. Moreover, it allows to control for graphical parameters with a theme and to have confidence intervals spread across multiple columns and divided by groups.

<br/>

The code snippet below shows how to create a `basic layout` for the forest plot:

{{% codeblock %}}
```R
# Load necessary packages
library(forestploter)
library(grid)

# Retrieve example dataset from the `forestploter` package
data <- read.csv(system.file("extdata", "example_data.csv", package = "forestploter"))

# Data manipulation
data <- data[,1:6]

data$Subgroup <- ifelse(is.na(data$Placebo), 
                      data$Subgroup,
                      paste0("   ", data$Subgroup))

data$Treatment <- ifelse(is.na(data$Treatment), "", data$Treatment)
data$Placebo <- ifelse(is.na(data$Placebo), "", data$Placebo)
data$se <- (log(data$hi) - log(data$est))/1.96

data$` ` <- paste(rep(" ", 20), collapse = " ")

data$`HR (95% CI)` <- ifelse(is.na(data$se), "",
                             sprintf("%.2f (%.2f to %.2f)",
                                     data$est, data$low, data$hi))

```
{{% /codeblock %}}

Drawing simple forest plot:

{{% codeblock %}}
```R
p <- forest(data[,c(1:3, 8:9)],
            est = data$est,
            lower = data$low, 
            upper = data$hi,
            sizes = data$se,
            ci_column = 4,
            ref_line = 1,
            arrow_lab = c("Placebo Better", "Treatment Better"),
            xlim = c(0, 4),
            ticks_at = c(0, 1, 2, 3),
            footnote = "This is the demo data. Please feel free to change\nanything you want.")

print(p)

```
{{% /codeblock %}}


{{% tip %}}
Type `help(forest)` in your R terminal for more info about the `forest()` function arguments.
{{% /tip %}}


