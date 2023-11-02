---
title: "Validation and Falsification Analysis for RDD"
description: "Validation and falsification analysis methods for the RD designs. Explanation of methods, how to implement them for both continuity and local randomization approaches, how to interpret results"
keywords: "regression, discontinuity, validation, falsification, analysis"
date: 2023-07-17
weight: 30
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /validation/analysis
  - /falsification/analysis
---

## Introduction

The Regression Discontuinity Design (RDD) assumes **no precise manipulation** at the cutoff. 

Precise manipulation happens if subjects know the cutoff and manipulate accordingly whether they end up below or above the cutoff, which determines whether they belong to the treatment or control group. As a result, treatment assignment is not as good as random anymore at the cutoff value of the running variable. An example of precise manipulation would be if in a targeted aid program for lower-income groups, some subject position themselves just below the cutoff of income level to qualify for this aid. 

In this building block we discuss validation methods, based on various empirical implications of the unobservable RD assumptions that are expected to hold in most cases. These methods are explored within both the standard [continuity-based approach](/continuity/approach) and the extended [local randomization approach](/local/randomization). 

{{% tip %}}
__Falsification Test__
A falsification test serves to "falsify" (=prove something to be false) other discontinuities at the cutoff. By doing this test and proving there are no other discontinuities, we can be sure the observed effects are not the result of other factors and ensure the robustness of the RD Design.
{{% /tip %}}

## 1. Falsification test: Observable variables

The first and most important falsification test examines whether units near the cutoff (in both treatment and control groups) are similar in terms of observable characteristics. For the validity of the RDD to hold, the units with scores just above and below the cutoff should be similar in the variables that could not have been affected by the treatment.

These variables include:
- **Predetermined covariates**: variables that are determined before the treatment is assigned
- **Placebo outcomes**: variables that are determined after the treatment is assigned and that could not have been affected by the treatment

The principle behind this test is that all predetermined covariates and placebo outcomes are analyzed in the same way as the outcome of interest. The null hypothesis is: the treatment effect is 0 for each predetermined covariate and placebo outcome. 

If the p-value is lower than 0.05, the H0 can be rejected and other discontinuities than just the treatment effect on the outcome variable are found around the cutoff. Thus, for the validity of the RDD to hold, the p-value should be higher than 0.05 such that the $H_0$ cannot be rejected.

### The continuity-based approach

For each observed variable, an optimal bandwidth should be chosen first. Then, the `rdrobust` can be used to conduct local polynomial estimation within this chosen bandwidth. In the [continuity-based approach building block](/continuity/approach), this method is discussed in more detail. 

In the code below, the bandwith (`bw`) is set to 0.2 and the kernel used is the triangular kernel. 

{{% codeblock %}}
```R
# Continuity-Based Approach
out <- rdrobust(Y, X, bw = 0.2, kernel = "triangular")
summary(out)
```
{{% /codeblock %}}

If the p-value is higher than 0.05, the H0 cannot be rejected and the validity of the RDD is ensured. 

### The local randomization approach

In the local randomization approach, the analysis is conducted within the window where the assumption of randomization is assumed to hold. The `rdrandinf` function should be run using each covariate as outcome. `wl` and `wr` represent the left and right bounds of the window and the `seed` parameter is used for setting the random seed.

{{% codeblock %}}
```R
# Local Randomization Approach
out <- rdrandinf(Y, X, wl = -2.5, wr = 2.5, seed = 50)
summary(out)
```
{{% /codeblock %}}

Again, if the p-values are above 0.05, it indicates that the variables are balanced inside the window, suggesting that no other discontinuities are found around the cutoff, thus reinforcing the validity of the RD design.


### Density of Running Variable

The test for the density of running variable analyzes whether in a neighborhood around the cutoff the number of observations below the cutoff is very different from the number of observations above. The assumption is that if units don't have the ability to change the scores, the number of treated observations above the cutoff should be similar to the number of control observations below it.  

For the **continuity-based approach** the null hypothesis is that the density of the running variable is continuous at the cutoff. Thus, the test consists of a density estimation of observations near the cutoff using the `rddensity` function from the `rddensity` library, which only requires the running variable as argument. If the p-value is above .05 there is no difference in the density of the treated and control variables at the cutoff.

For the **local randomization approach** the null hypothesis is that within the window where the treatment is assumed to be random, the number of treated and control observations is consistent with the assumed assignment mechanism inside the window. To test this we can use the `rdwinselect` function of the `rdlocrand` package, with the score and `nwindows = 1` as arguments. When the p-value is above .05 there is no evidence against the null hypothesis.

### Placebo Cutoffs

This analysis studies the treatment effects at artificial or placebo cutoff values. This artificial value replaces the true cutoff. The test then performs estimation and inference using the artificial cutoff. The goal is that no significant treatment effect occurs at the placebo cutoff values. 

For the **continuity-based approach** this test is implemented using the local polynomial estimation by employing `rdrobust` and specifying the artificial cutoff as argument. A p-value higher than .05 would show that the outcome of interest doesn't jump at the artificial cutoff.

In the **local randomization approach** this test is conducted using a randomization-based analysis of the outcome using a symmetric window equal to the original window around each of the chosen artificial cutoffs. The necessary function is `rdrandinf`.

### Sensitivity of Observations around the Cutoff

This test investigates how sensitive the results are to the response of units located very close to the cutoff. If there is any manipulation of the score, the units closest to the cutoff are most likely to be involved in the manipulation. The goal is to exclude these units and redo the estimation using the remaining sample. 

In the **continuity-based approach** we can simply use `rdrobust` on the remaining subset of data. The goal is that the new result remains largely unchanged compared to the original result containing the entire sample of data.

### Sensitivity to Bandwidth Choice

This method analyzes the sensitivity of the results to the bandwidth choice as units are added or removed at the end points of the neighborhood. 

In the **continuity-based approach** this test is conducted by changing the bandwidth used for local polynomial estimation. An increased bandwidth leads to an increased bias of the local polynomial estimator and a decreased variance. A broadly consistent result under different bandwidth choices is preferred. For more details on bandwidth selection, see the [Continuity-based approach](https://tilburgsciencehub.com/building-blocks/analyze-data/regression-discontinuity/continuity-approach/) building block.

### Sensitivity to Window Choice

This test is the **local randomization approach** equivalent of the Sensitivity to Bandwidth choice of the **continuity-based approach**. Here, the sensitivity to the window choice is analyzed instead of the bandwidth choice. This analysis should consider smaller windows than the original one, since a larger window would not lead to reliable results because the treated and control groups would be imbalanced in such windows. 

To implement it, we can simply use the `rdrandinf` function to specify a smaller window and analyze the results. As the statistic test of this function is the difference in means, a p-value higher than .05 shows no significant difference in the results when a smaller window is implemented. 


## See also
[A Practical Introduction to Regression Discontinuity Designs: Foundations - Cattaneo, Idrobo & Titiunik (2020)](https://rdpackages.github.io/references/Cattaneo-Idrobo-Titiunik_2020_CUP.pdf)

[A Practical Introduction to Regression Discontinuity Designs: Extensions - Cattaneo, Idrobo & Titiunik (2023)](https://rdpackages.github.io/references/Cattaneo-Idrobo-Titiunik_2023_CUP.pdf)