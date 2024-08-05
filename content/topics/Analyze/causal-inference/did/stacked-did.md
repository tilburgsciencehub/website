---
title: "Stacked DiD"
description: ""
keywords: ""
draft: false
weight: 8
author: "Valerie Vossen"
aliases:
  - /stacked-did
---

## Overview

[Difference-in-Difference (DiD)](/canonical-DiD) is a powerful technique to evaluate the effects of a treatment by comparing changes in outcomes between treatment and control groups. In our [Staggered DiD article](/staggered-did), we introduced a design where units are exposed to treatment at different times. 

In this article, we introduce the *Stacked DiD* method as an approach to analyze a staggered design. 


## Basic stacked DiD

The *Stacked DiD* method analyzes staggered designs by creating separate datasets for each valid subexperiment, which excludes problematic late-early comparisons. These datasets are then combined, or "stacked", to analyze overall trends. 

{{% tip %}}

For more intuition on these problematic late-early comparisons, see [this topic](/goodman-bacon).

{{% /tip %}}

An important shortcoming of the basic stacked DiD design is *the imbalance in treatment and control trends across different subexperiments*, which can lead to a biased causal parameter. 

## Imbalance in trends

Each subexperiment has different lenghts of pre-and post-treatment periods because some groups are treated earlier than others. When aggregating across different subexperiments, and averaging all the group-specific effects of the treated groups, the composition of the treatment groups changes.

The regression essentially weights treatment and control trends differently across subexperiments. For example, when constructing the aggregate effect of a later time period (e.g. 3 years after the treatment took place), only the early treatment group is included in the "Treated" group, which is compared to the Control group. 

{{% example %}}

Imagine measuring the treatment effect over four time periods, from 2020 to 2024. There is an *early-treated* group (treated in 2020) and a *late treated group* (treated in 2023). The early-treated group experiences a negative effect, while the late-treated group experiences a positive effect.

To find the overall treatment effect, these effects are aggregated. The effect seems to fade out over time. However, this is due to the compositional imbalance: The aggregate treatment effect three years after the treatment only includes on the early-treated group, as the effect on the late-treated group is not observed yet! The year 2026 did not take place yet and is outside of the current data range.

- real practical example (maybe already introduce code example)

{{% /example %}}

The good news is that this bias is known, as it is a function of the sample sizes of each subexperiment. The next section introduces a new weighted approach to address the bias.


## Weighted stacked DiD

This compositional imbalance is addressed in [the working paper of Wing et al. (2024)](https://www.nber.org/papers/w32054), proposing a weighted stacked DiD design. After summarizing their framework, a practical application is given of this *weighted stacked DiD regression*. 


The weighted stacked DiD estimate by [Wing et al. (2024)](https://www.nber.org/papers/w32054) corrects for this imbalance, using sample weights. The framework ...


### Trimming the dataset

It trims the subexperiments to make them balanced over a fixed event time window. In other words, you take out the subexperiments that do not have enough follow-up years. 

Essentially, two inclusion criteria are used to trim the sample and correct for this imbalance:

1. *Adoption event window*

The treatment adoption took place inside the k event window. 

2. *Existence of clean controls*

For this treatment, adoption event a ... 

### Aggregation 

To reach a summary average of estimates, aggregate the subexperiments.

### Estimation 

The last step is estimation. 

## Example in R

Following [Wing et al. (2021)](), a function is available in R to implement their framework of stacked DiD regression. Use [their tutorial]() as a guided implementation of these functions. 

We are interested in the impact of the expansion of ACA (*Affordable Care Act*) Medicaid, a health insurance coverage for low-income groups, on uninsurance rates.

- Dependent variable: `unins`
- Treatment variable: `adopt_year`: first year ACA Medicaid expansion was adopted in this state (`NA` if state never adopted)

1. Load the packages and data

{{% codeblock %}}
```R

```
{{% /codeblock %}}


1. Make a stacked dataset

2. Make the weights

3. Estimate the regression











## See also




- [Example code](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html)

