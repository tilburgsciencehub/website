---
title: "The HonestDiD Approach to Handle Violations of the Parallel Trends Assumption"
description: ""
keywords: ""
weight: 
author: "Valerie Vossen"
draft: false
aliases:
  - /honest-did
  - /honestdid
---

## Overview

The parallel trends assumption, introduced in the [Intro to Difference-in-Difference topic](/canonical-DiD), is crucial for a valid DiD design to establish causality. However, there are scenarios where the validity of this assumption might be uncertain. This topic discusses what to do when the parallel trends assumption is violated, introducing a new approach by [Rambachan & Roth (2019)](https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf). The `HonestDiD` package in R makes it easy to implement this approach, which is demonstrated with an example.

## Reasons for an invalid parallel trends assumption

{{% tip %}}

*Reasons for an invalid parallel trends assumption*

The parallel trends assumption can be violated in different scenarios. For example: 

1. *Different pre-treatment trends*: Pre-treatment trends are found to be different for treatment and control groups.

2. *Hidden trends*: Even if no significant pre-trends are found, non-parallel trends can still exist. For example, with non-linear trends, similar pre-trends at the baseline can hide an underlying difference in trends, especially with a short pre-treatment period. 

3. *Low power*: The statistical power is too low to detect violations of parallel trends, even if they are present. 

4. *Economic shock*: A shock occurs around the time of the treatment, causing differences in post-treatment trends, even if the pre-treatment trends were similar. 

Rejecting the hypothesis of pre-trends does not confirm that the trends are similar. Always justify the parallel trends assumption in your research context, instead of solely relying on a statistical test outcome!

{{% /tip %}}

## A new approach

[Rambachan & Roth (2019)](https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf) introduce a new method to handle potential violations of the parallel trends assumptions by relaxing this assumption. 

### Extrapolating a pre-existing difference

The usual assumption of parallel pre-trends allows us to interpret the difference between treated and control groups post-treatment as the causal effect of interest. Essentially, if the groups would have followed similar trends without treatment, any post-treatment difference can be attributed to the treatment. 

Instead of assuming that the pre-treatment differences in trends are zero, an alternative is to *extrapolate the existing difference to the post-treatment period*. This approach still identifies the causal effect but requires the post-treatment difference in trends to be precisely similar to the pre-treatment difference. However, this strong assumption is not always realistic. 

### Restrictions on the pre-existing difference

Rambachan & Roth's framework builds on this idea of extrapolation but with milder assumptions. They allow for an *interval of differences in trends*, conditional on the pre-existing difference. They acknowledge that the post-treatment difference in trends of untreated potential outcomes between the treated and control groups is often not exactly the same as the pre-treatment difference, but it is similar *to some degree*.

{{% summary %}}
The key idea is to restrict the possible values of the post-treatment difference to a certain interval based on the known pre-trend difference.

As an interval is estimated instead of one precise coefficient, this method results in *partial identification*. 
{{% /summary %}}


### How to choose these restrictions?

Choosing the right restrictions on how much the pre- and post-treatment trends can differ depends on the specifics of your study. The economic context and your knowledge about potential confounding factors will guide these choices.
Here are two possible approaches to formalize these restrictions:

1. *Relative magnitude bounds*

This approach is suitable if you believe that the confounding factors causing deviations from parallel trends after treatment are similar in size to those before treatment. The pre-treatment trend differences are used to set limits on how much post-treatment trends differ, helping us account for the violation. Specifically, parameter $\bar{M}$ sets bounds on the size of the post-treatment violations based on observed pre-treatment violations. For example, setting $\bar{M}$ to 1 assumes post-treatment violations are, at most, the same size as pre-treatment violations. And with $\bar{M}$ = 2, the post-treatment violations can be up to twice the size of the pre-treatment violations. 

{{% example %}}

Following the example in section 6.2 of the paper..

Benzarti and Carloni (2019) estimate the effect of a value-added tax decrease on restaurants profits in France, and are concerned about unobserved macroeconomic shocks that affect restaurants (treatment group) differently than other service sectors (control group), resulting in a violation of the parallel trends violation. However, we can reasonably assume that the difference in trends after the tax change are not much larger than the differences observed before the tax change. This motivates the use of the Relative Magnitude bounds approach in this context. 

{{% /example %}}

2. *Smoothness restriction*

This approach is suitable when you expect the differences in trends between the treatment and control group to evolve smoothly over time, without any sharp changes. The post-treatment violation is assumed to not deviate much from a linear extrapolation of the pre-trend violation, while M > 0 allows for the trends to not be perfectly linear. [HonestDiD GitHub page](https://github.com/asheshrambachan/HonestDiD) 

<p align = "center">
<img src = "../images/smoothness-restriction.png" width="500">
<figcaption> Smoothness restriction visualization. Source: HonestDiD GitHub page (https://github.com/asheshrambachan/HonestDiD)
</figcaption>
</p>



{{% example %}}

Lovenheim and Willén (2019) study the impact of a certain law concerning students on adult labor market outcomes of the students affected by these laws. They compared people across states and birth cohorts, leveraging the different timings of the law implementation. 

Their main concern was the presence of long-term trends that might differ systematically with treatment, such as changes in labor supply or educational attainment. These trends likely evolve smoothly over time, so using a smoothness restriction approach makes sense. This approach assumes that any deviations from the pre-law trends after the law is enacted will change radually rather than abruptly.

{{% /example %}}


{{% tip %}}

*Additional possible restrictions*

- *Combination of smoothness and RM bounds*

If you believe that trends change smoothly over time but are unsure about the exact level of smoothness (M ≥ 0), you can combine the smoothness and relative magnitude bounds approaches to set reasonable limits on trend changes. Specifically, you assume that any non-linear changes after the treatment are limited by the non-linear changes observed before treatment. 

- *Sign and monotonicity*

If you expect the bias to always go in a particular direction (either always positive or always negative), you can include this as a restriction as well.

{{% /tip %}}


## R code example with `HonestDiD`:

We continue with the example that is introduced in the [DiD regression topic](/canonical-DiD). We are interested in the effect of a newly introduced Q&A feature on subsequent book ratings, with the website Goodreads as the treatment and Amazon as the control group. So, we have 2 groups (Amazon vs Goodreads) and 2 time periods (pre Q&A and post Q&A). You can download the full code of the baseline DiD analysis [here](https://gist.github.com/srosh2000/f52600b76999e88f0fe316e8f23b419e). 

The baseline analysis relies on the parallel trend assumption. Suppose we are worried about the validity of this assumption, we can conduct a sensitivity analysis with the [`HonestDiD` package](https://github.com/asheshrambachan/HonestDiD). 

First, install the package:

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


Estimate the baseline model and save the resulting coefficients and covariance matrix:

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

1. The relative magnitude bounds approach

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

- `lb` = lowerbound
- `ub` = upperbound

The results show that if Mbar is set at 0.5 or 1 (assuming the post-Q&A trend violation is at most as large as the pre-Q&A trend violation), a negative effect of the Q&A feature on book ratings is found. With Mbar set larger than 1, the upper bound is larger than zero so the interval contains zero, so nothing can be said. 

Let's create a plot, comparing the baseline approach with the results of the RM approach, showing the threshold to find an impact is Mbar = 1.

{{% codeblock %}}
```R

plot_rm <- HonestDiD::createSensitivityPlot_relativeMagnitudes(delta_rm_results, originalResults)

plot_rm

```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/rm-plot.png" width="500">
</p>

2. The smoothness approach 

The smoothness approach as a sensitivity analysis, if we assume that the confounding trends are smoothly evolving over time, i.e. the slope of the parallel trend violation does not deviate more than M between periods.

{{% codeblock %}}
```R
delta_sd_results <- createSensitivityResults(betahat = betahat,
                                      sigma = sigma,
                                      numPrePeriods = 1,
                                      numPostPeriods = 1,
                                      Mvec = seq(from = 0, to = 0.05, by =0.01))

delta_sd_results

```
{{% /codeblock %}}

Let's plot the results.





## Implications 

- Comparing the approaches -> depends on number of pre-periods which is best to use
- Make table to summarize the three approaches and compare on important things:
  - not too different from pre-trend: RM
  - smoothly evolving trends: smoothness


good summary of choice
- Additional restrictions; if researcher knows of a confounding policy that would have a positive effect on post-treatment difference -> make additional restriction that bias is positive in post-trend. 


Second recommendation; Once baseline class of restrictions is chosen, recommended to conduct sensitivity analysis with different M's -> governs how different post-treatment violations of parallel trends can be from pre-trends. 

Report sensitivity of causal conslusion to choice of this parameter, and the "breakdown" parameter value at which hypothesis can no longer be rejected. 


conclusion 
- report confidence sets under economically motivated restrictions on parallel trends
- conduct formal sensitive analysis, in which they report confidence sets for the causal effect of interest under a variety of possible restrictions on the underlying trends --> make transparent what assumptions are needed in order to draw particular conclusions


## References 

- https://blogs.worldbank.org/en/impactevaluations/revisiting-difference-differences-parallel-trends-assumption-part-ii-what-happens

- paper Rambachan and Ruth (2019): https://www.jonathandroth.com/assets/files/HonestParallelTrends_Main.pdf
