---
title: "Validation and Falsification Analysis"
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

The main advantage of regression discontinuity (RD) designs is that the treatment assignment rule is known and based on observable features. However, this is not enough to guarantee that the needed assumptions to recover the RD effect are met.

If units know the cutoff, they can actively change the value of their score when they barely miss the treatment, which can threat the validity of the RD design. For this, there are validation methods based on various empirical implications of the unobservable RD assumptions that are expected to hold in most cases. We discuss them next, both from the stand point of continuity-based approach and local randomization approach. 

### Predetermined Covariates and Placebo Outcomes

The first and most important falsification test is examining if near the cutoff the treated units are similar to the control units, in terms of observable characteristics. The units with scores just above and below the cutoff should be similar in the variables that couldn't have been affected by the treatment. These variables are:
- **predetermined covariates**: variables that are determined before the treatment is assigned
- **placebo outcomes**: variables that are determined after the treatment is assigned and that couldn't have been affected by the treatment

The principle of this analysis is that all predetermined covariates and placebo outcomes should be analyzed the same as the outcome of interest.

The null hypothesis of this analysis becomes: the treatment effect is zero for each predetermined covariate and placebo outcome (no treatment effect). Since the predetermined covariate or placebo outcome couldn't have been affected by the treatment, the null hypothesis shouldn't be rejected if the RDD is valid.

In the **continuity-based approach** for each predetermined covariate or placebo outcome, an optimal bandwidth should be chosen first, and then use local polynomial techniques within that bandwidth to estimate the treatment effect. By contrast, in the **local randomization approach**, all covariates and placebo outcomes are analyzed within one window, a window where the assumption of local randomization is assumed to hold. 

For the **continuity-based approach** the test consists of the local polynomial estimation steps discussed in the [Continuity-based approach](https://tilburgsciencehub.com/building-blocks/analyze-data/regression-discontinuity/continuity-approach/) building block. Specifically, `rdrobust` function should be run using each covariate of interest as the outcome variable. If the resulting p-values are higher than .05, then there is no evidence of discontinuities in the variables. 

For the **local randomization approach** `rdrandinf` function should be run using each covariate as outcome. Again, if the p-values are above .05 it means the covariates are balanced inside the window.

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