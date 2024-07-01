---
title: "Handling Parallel Trends Violations with `HonestDiD` in R"
description: "The HonestDiD package in R offers a solution or sensitivity analysis when the parallel trends assumption in DiD analysis seems invalid."
keywords: "honestdid, package, R, did, difference-in-difference, analysis, causal inference, did, staggered, non-staggered"
weight: 5
author: "Valerie Vossen"
draft: false
aliases:
  - /honest-did
  - /honestdid
---

## Overview

The parallel trends assumption, introduced in the [Intro to Difference-in-Difference topic](/canonical-DiD), is crucial for a valid DiD design to establish causality. However, there are scenarios where the validity of this assumption might be uncertain. This topic discusses what to do when the parallel trends assumption is violated, introducing a new approach with the `HonestDiD` package in R by [Rambachan & Roth (2019)](https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf).


{{% tip %}}

*Reasons for an invalid parallel trends assumption*

The parallel trends assumption can be violated in different scenarios. For example: 

1. *Different pre-treatment trends*: Pre-treatment trends are different for treatment and control groups.

2. *Hidden trends*: Non-parallel trends can exist even with similar pre-trends. Non-linear trends may hide an underlying difference, especially with a short pre-treatment period. 

3. *Low power*: The statistical power is too low to detect violations of parallel trends, even if they are present. 

4. *Economic shock*: A shock occurs around the treatment period, causing differences in post-treatment trends, even if the pre-treatment trends were similar. 

Rejecting the hypothesis of pre-trends does not confirm that the trends are similar. Always justify the parallel trends assumption within your research context, rather than relying solely on test outcomes suggesting similar pre-trends!

{{% /tip %}}

## The `HonestDiD` approach

[Rambachan & Roth (2019)](https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf) introduce a new method to handle potential violations of the parallel trends assumptions by relaxing this assumption. 

### The framework

Instead of assuming that the pre-treatment differences in trends are zero, an alternative is to *extrapolate the existing difference to the post-treatment period*. This approach still identifies the causal effect but requires the post-treatment difference in trends to be precisely similar to the pre-treatment difference. However, this strong assumption is not always realistic. 

Rambachan & Roth's framework builds on this idea of extrapolation but with milder assumptions. They allow for an *interval of differences in trends*, conditional on the pre-existing difference. They acknowledge that the post-treatment difference in trends of untreated potential outcomes between the treated and control groups is often not exactly the same as the pre-treatment difference, but it is similar *to some degree*.

{{% summary %}}
The key idea is to restrict the possible values of the post-treatment difference to a certain interval based on the known pre-trend difference.

As an interval is estimated instead of one precise coefficient, this method results in *partial identification*. 
{{% /summary %}}


### How to choose the restrictions?

Choosing the right restrictions on how much the pre- and post-treatment trends can differ depends on the specifics of your study. The economic context and your knowledge about potential confounding factors will guide these choices.
Here are two possible approaches to formalize these restrictions:

{{<katex>}}
{{</katex>}}

1. *Relative magnitude bounds*

If you believe that the confounding factors causing deviations from parallel trends after treatment are similar in size to those before treatment, the *Relative magnitude bounds* is for you. 

The pre-treatment trend differences are used to set limits on how much post-treatment trends differ, helping us account for the violation. Specifically, parameter $\bar{M}$ sets bounds on the size of the post-treatment violations based on observed pre-treatment violations. For example, setting $\bar{M}$ to 1 assumes post-treatment violations are, at most, the same size as pre-treatment violations. And with $\bar{M}$ = 2, the post-treatment violations can be up to twice the size of the pre-treatment violations. 

{{% example %}}

Following the example in section 6.2 of the paper..

Benzarti and Carloni (2019) estimate the effect of a value-added tax decrease on restaurants profits in France, and are concerned about unobserved macroeconomic shocks that affect restaurants (treatment group) differently than other service sectors (control group), resulting in a violation of the parallel trends violation. However, we can reasonably assume that the difference in trends after the tax change are not much larger than the differences observed before the tax change. This motivates the use of the Relative Magnitude bounds approach in this context. 

{{% /example %}}

2. *Smoothness restriction*

When you expect the differences in trends between the treatment and control group to evolve smoothly over time, without any sharp changes, this approach is suitable. The post-treatment violation is assumed to not deviate much from a linear extrapolation of the pre-trend violation, while M > 0 allows for the trends to not be perfectly linear. [HonestDiD GitHub page](https://github.com/asheshrambachan/HonestDiD) 

<p align = "center">
<img src = "../images/smoothness-restriction.png" width="500">
<figcaption> Smoothness restriction visualization. Source: HonestDiD GitHub page (https://github.com/asheshrambachan/HonestDiD)
</figcaption>
</p>


{{% example %}}

Lovenheim and Willén (2019) study the impact of a certain law concerning students on adult labor market outcomes of the students affected by these laws. They compared people across states and birth cohorts, leveraging the different timings of the law implementation. 

Their main concern was the presence of long-term trends that might differ systematically with treatment, such as changes in labor supply or educational attainment. These trends likely evolve smoothly over time, so using a smoothness restriction approach makes sense. This approach assumes that any deviations from the pre-law trends after the law is enacted will change gradually rather than abruptly.

{{% /example %}}


{{% tip %}}

*Additional possible restrictions*

- *Combination of smoothness and RM bounds*

If you believe that trends change smoothly over time but are unsure about the exact level of smoothness (M ≥ 0), you can combine the smoothness and relative magnitude bounds approaches to set reasonable limits on trend changes. Specifically, you assume that any non-linear changes after the treatment are limited by the non-linear changes observed before treatment. 

- *Sign and monotonicity*

If you expect the bias to always go in a particular direction (either always positive or always negative), you can include this as a restriction as well.

{{% /tip %}}


## Non-staggered DiD example

We continue with the example that is introduced in the [DiD regression topic](/canonical-DiD). We are interested in the effect of a newly introduced Q&A feature on subsequent book ratings, with the website Goodreads as the treatment and Amazon as the control group. So, we have 2 groups (Amazon vs Goodreads) and 2 time periods (pre Q&A and post Q&A). 

The baseline analysis relies on the parallel trend assumption. Suppose we are worried about the validity of this assumption, we can conduct a sensitivity analysis with the [`HonestDiD` package](https://github.com/asheshrambachan/HonestDiD). 


1. Load packages and data


{{% codeblock %}}
```R

# Load packages

library(here)
library(dplyr)
library(did)
library(haven)
library(ggplot2)
library(fixest)
library(HonestDiD)
library(readr)
library(tidyverse)
library(readxl)
library(stringr)

# Import data
data_url <- "https://raw.githubusercontent.com/tilburgsciencehub/website/master/content/topics/analyze/causal-inference/did/GoodAma.Rda"

load(url(data_url)) #GoodAma is the final data set

```
{{% /codeblock %}}

2. Install the `HonestDiD` package

{{% codeblock %}}
```R
# Make it possible to install from GitHub 
install.packages("remotes") 

# Don't allow for warning errors stopping the installation
Sys.setenv("R_REMOTES_NO_ERRORS_FROM_WARNINGS" = "true")

# Install HonestDiD package from GitHub
remotes::install_github("asheshrambachan/HonestDiD")
```
{{% /codeblock %}}


3. Estimate the baseline model

The resulting coefficients and covariance matrix are saved under `betahat` and `sigma`. 

{{% codeblock %}}
```R

# Run model
model_4 <- feols(rating ~ i(goodr, qa) | year_month + asin,
                cluster = c("asin"),
                data = GoodAma)

# Save coefficients
betahat <- summary(model_4)$coefficients

# Save the covariance matrix
sigma <- summary(model_4)$cov.scaled

```
{{% /codeblock %}}

4. Estimate DiD with relative magnitude bounds

{{% codeblock %}}
```R

delta_rm_results <- createSensitivityResults_relativeMagnitudes(
    betahat = betahat, #coefficients
    sigma = sigma, #covariance matrix
    numPrePeriods = 1, #num. of pre-treatment coefs
    numPostPeriods = 1, #num. of post-treatment coefs
    Mbarvec = seq(0.5,2,by=0.5) #values of Mbar
  )

delta_rm_results

```
{{% /codeblock %}}

*Output:*

```R
# A tibble: 4 × 5
     lb     ub method Delta    Mbar
  <dbl>  <dbl> <chr>  <chr>   <dbl>
1 -6.74 -2.57  C-LF   DeltaRM   0.5
2 -6.74 -0.344 C-LF   DeltaRM   1  
3 -6.74  2.41  C-LF   DeltaRM   1.5
4 -6.74  5.18  C-LF   DeltaRM   2  
```

The results show that if `Mbar` is set at 0.5 or 1 (assuming the post-Q&A trend violation is at most as large as the pre-Q&A trend violation), a negative effect of the Q&A feature on book ratings is found, as the confidence interval (lower bound `lb`, to upperbound `ub`) includes only negative values. With `Mbar` set larger than 1, the upper bound is larger than zero so the interval contains zero, so nothing can be said. 

5. Create a plot

The plot compares the baseline results with the results of the RM approach, showing the threshold to find an impact is `Mbar = 1`.

{{% codeblock %}}
```R

plot_rm <- HonestDiD::createSensitivityPlot_relativeMagnitudes(delta_rm_results, originalResults)
plot_rm

```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/rm-plot.png" width="500">
</p>


## Staggered DiD example

This example shows how to use the `HonestDiD` approach with a staggered DiD framework, continuing the example of Goodreads in the [staggered DiD topic](\staggered-did). 

The full R code for this example is shared in this [GitHub Gist](https://gist.github.com/valerievossen/7eb07cadac731cfa14ce5cc44a353d4c). 


1. Specify the function

To combine the staggered DiD approach of Callaway and Sant'Anna (with the package `did`) and the `HonestDiD` package, a function is created by Sant'Anna as the packages are now not fully integrated yet. 


Extract the function from the codeblock in the [Callaway and Sant'Anna section of the HonestDiD page](https://github.com/asheshrambachan/HonestDiD), or from the [Gist specifically created for this example](https://gist.github.com/valerievossen/7eb07cadac731cfa14ce5cc44a353d4c).

2. Load data

Run the code in the [Gist](https://gist.github.com/valerievossen/7eb07cadac731cfa14ce5cc44a353d4c) to get the dataset ready-to-use. Or, run the following code to load the final dataset right away:

{{% codeblock %}}
```R

# Load packages
library(HonestDiD)
library(fixest)
library(did)
library(data.table)
library(dplyr)
library(tidyr)
library(zoo)
library(did)
library(lubridate)
library(googledrive)
library(ggplot2)
library(stringr)

# Load data
data_url <- "https://raw.githubusercontent.com/tilburgsciencehub/website/master/content/topics/analyze/causal-inference/did/goodreads_df.Rda"

load(url(data_url)) #goodreads_df is the final data set

```
{{% /codeblock %}}

3. The DiD estimation

Note that the function `honest_did` is specified in Step 1, and the dataset `goodreads_df` is loaded in Step 2. If you did this, the following code gives you the results for the sensitivity analyses including plots.

{{% codeblock %}}
```R

# 3.1. Staggered DiD analysis 

staggered_results <- did::att_gt(yname = "rating", # outcome var
                          tname = "period_review", # time var
                          idname = "asin", # individual var
                          gname = "period_question", # treated
                          control_group = "notyettreated", #control
                          data = goodreads_df, # final dataset
                          allow_unbalanced_panel = TRUE,
                          base_period = "universal")

# Aggregate results 

es <- did::aggte(cs_results, type = "dynamic", na.rm = TRUE)


# 3.2 SENSITIVITY ANALYSIS: RELATIVE MAGNITUDES 

sensitivity_results_rm <-
  honest_did(es,
             e=0,
             type="relative_magnitude",
             Mbarvec=seq(from = 0.5, to = 2, by = 0.5))

HonestDiD::createSensitivityPlot_relativeMagnitudes(sensitivity_results_rm$robust_ci,
                                                    sensitivity_results_rm$orig_ci)


# 3.3 SENSITIVITY ANALYSIS: SMOOTHNESS RESTRICTIONS

sensitivity_results_sd <-
  honest_did(es = es,
             e = 0,
             type="smoothness")


HonestDiD::createSensitivityPlot(sensitivity_results_sd$robust_ci,
                                sensitivity_results_sd$orig_ci)

```
{{% /codeblock %}}

The following plots are output:

1. *Relative magnitudes*

<p align = "center">
<img src = "../images/staggered-rm-plot.png" width="500">
</p>


2. *Smoothness restriction*

<p align = "center">
<img src = "../images/staggered-sd-plot.png" width="500">
</p>

{{% summary %}}
 
The `HonestDiD` approach by Rambachan & Roth (2019) handles violations of the parallel trends assumption in DiD analysis. It extrapolates pre-treatment differences to the post-treatment period, allowing for an interval of differences. Using this approach as a sensitivity analysis can robustly address potential violations of the parallel trends assumption, thereby improving the credibility of causal inference in DiD analyses!

Two main approaches are discussed on how to set restrictions and specify your framework (while alternatives of combinations are possible!):

1. Relative magnitude bounds: Sets bounds on pre-treatment differences. 
2. Smoothness restriction: Assumes trends evolve smoothly over time. 

{{% /summary %}}


### References 

- [Rambachan and Ruth (2019) - A More Credible Approach to Parallel Trends](https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf)

- [GitHub Page HonestDiD, Example Application](https://github.com/asheshrambachan/HonestDiD)

- [Blog post of David Mckenzie: What happens if the parallel trends assumption is (might be) violated?](https://blogs.worldbank.org/en/impactevaluations/revisiting-difference-differences-parallel-trends-assumption-part-ii-what-happens)

