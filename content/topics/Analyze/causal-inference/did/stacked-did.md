---
title: "Weighted Stacked DiD: A Robust Method for Staggered Treatment Designs"
description: "The weighted Stacked DiD framework addresses a bias through dataset trimming and weighted aggregation. Explore this method with a straightforward application in R and Stata "
keywords: "staggered, treatment, causal inference, DiD, difference-in-difference, stacked, diff-in-diff, R, Stata, ATT, estimation, regression, analysis"
draft: false
weight: 4
author: "Valerie Vossen"
aliases:
  - /stacked-did
  - /stacked
---

## Overview

The [Difference-in-Difference (DiD) method](/canonical-DiD) is a powerful technique for causal inference. It evaluates the effects of a treatment by comparing the changes in outcomes between treatment and control groups. In our [Staggered DiD article](/staggered-did), we introduced a design where different units receive the treatment at other times. 

In this article, we explore staggered treatment designs further discussing the *Stacked DiD* method. We also introduce the *Weighted Stacked DiD* method by [Wing et al. (2024)](https://www.nber.org/papers/w32054), which addresses the imbalances in treatment and control trends found in the basic Stacked DiD approach.

## The basic Stacked DiD

The *Stacked DiD* method analyzes staggered treatment designs by creating separate datasets for each valid sub-experiment (i.e., treatment adoption event), avoiding problematic late-early comparisons. These datasets are combined, or "stacked", to analyze overall trends. 

{{% tip %}}

For more insights into these problematic late-early comparisons, read [this topic on potential Staggered DiD biases](/goodman-bacon).

{{% /tip %}}

A major shortcoming of the basic stacked DiD design is *the imbalance in treatment and control trends* across different sub-experiments, which can lead to a biased causal parameter. 

### Imbalance in trends

In staggered designs, each sub-experiment has different lengths of pre- and post-treatment periods because some groups receive treatment earlier than others. When these sub-experiments are aggregated and all group-specific effects are averaged, the composition of the treatment group changes over time. Consequently, the regression assigns different weights to treatment and control trends across sub-experiments.





{{% example %}}

Suppose you are measuring the treatment effect over four periods, from 2020 to 2024. There is an *early-treated* group (treated in 2020) and a *late-treated group* (treated in 2023). The effect is heterogeneous across groups: the early-treated group experiences a negative impact, while the late-treated group experiences a positive impact.

To find the overall treatment effect, you aggregate these effects from different groups (i.e, sub-experiments). At first glance, the treatment effect appears to fade out over time. However, this is not due to the actual treatment but rather a result of *compositional imbalance*. Three years after the treatment (at event time = 3), the aggregated coefficient only includes the *early-treated group* (treated in 2020), because the effect on the *late-treated group* (treated in 2023) has not yet been observed!

{{% /example %}}

{{% tip %}}

*Event time*

Event time refers to the specific point at which a unit is exposed to treatment within a study. This concept differs from the usual "calendar time" (e.g., the years 2020, 2021, 2022) and helps standardize comparisons across units treated at different times. 

For instance, *event time = 0* marks the moment a unit receives treatment, *event time = 1* indicates one year after treatment, and *event time = -1* refers to one year before treatment. 

{{% /tip %}}

The potential bias caused by compositional imbalance is known, as it is a function of the sample sizes of each sub-experiment. The next section introduces a new weighted approach to address the bias.

## The Weighted stacked DiD Framework

[Wing et al. (2024)](https://www.nber.org/papers/w32054) propose a *weighted stacked DiD design* to correct imbalances using sample weights. The framework consists of three main steps:

1. Trimming the dataset
2. Aggregating sub-experiments 
3. Estimating the Stacked DiD

### 1. Trimming the dataset

To address the imbalance, the dataset is trimmed to ensure that sub-experiments are balanced over a fixed event time window. This involves removing sub-experiments that do not have enough follow-up years. 

Two criteria are used to trim the sample of treatment adoption events:

1. *Adoption event window*: Treatment adoption must occur within the chosen *k* event window. The choice of *k* is a research design choice. 

2. *Existence of clean controls*: There must be one or more "clean control" units to serve as comparisons in the dataset. A "clean control" is defined based on the study context. For example, it should not be exposed to the treatment at any time during the *k* event period but may be treated at a future date (*not-yet treated*), or it should not be exposed to treatment at all (*never treated*). 

### 2. Aggregating sub-experiments

Once the dataset is trimmed to avoid imbalances, you can calculate the group-time ATT (*Average Treatment Effect on the Treated*) parameters for each sub-experiment. To obtain a summary average of these estimates, aggregate the results from all sub-experiments. 

One approach to aggregate the group-specific ATT values is the *trimmed aggregate ATT*,  denoted as $\theta_\kappa ^\epsilon$. This method weighs the group-time ATT by its share of the trimmed treated sample. Specifically:

{{<katex>}}
{{</katex>}}

$$\theta_\kappa ^\epsilon = \sum_{\substack{a \in \Omega_\kappa }} ATT(a,a+e) * \frac{N_a ^D}{N_\Omega ^D} $$

Where:
- The first part, $ATT(a,a+e)$, represents the group-specific ATT within the fixed event time window $e$, where $a$ is the sub-experiment. 
- The second part assigns a weight to these ATT values by multiplying by their fraction of the total treatment group:
  - $N_a^D$ is the number of treated units in sub-experiment $a$ 
  - $N_\Omega^D$ = total number of treated units in the trimmed set

{{% tip %}}

Other approaches to aggregating ATT values include: 

- *Population-weighted ATT*: Weights the group-time ATT by its share of the treated population (instead of the treated sample) 

- *The sample share weighted ATT*: Weights the group-time ATT by its overall share of the stacked analytic sample, including both treated and control units in each sub-experiment.

The best weighting method depends on the specific application and study context. For more information on these alternative approaches, refer to [Section 4 of the paper](https://www.nber.org/papers/w32054).

{{% /tip %}}


### 3. Stacked DiD Estimation 

The final step in this framework is model estimation. As discussed earlier, simple stacked regression can introduce bias by weighting treatment and control group trends differently. To address this bias, sample weights are used to correct the imbalance. The *weighted stacked DiD* employs these sample weights to provide an accurate estimate of the ATT. 

Implementing these weighted regressions is straightforward with tools like linear regression models. Let's explore the application of this method and its estimation in the next section!


## Practical application


The authors provide functions to apply their framework easily in both Stata and R. For detailed guidance, you can refer to [their tutorial with code examples](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#load-the-data). As an example, they analyze the impact of the ACA (*Affordable Care Act*) Medicaid expansion on uninsurance rates in the United States, leveraging the staggered adoption of the treatment by states over different years.

In this section, we will guide you through the key steps of the analysis, replicating [the tutorial](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#load-the-data) and providing some additional tips.

1. Load the data

First, download the CSV dataset from [Alex Hollingworth's GitHub page](https://github.com/hollina/stacked-did-weights/tree/main/data) and save it to your computer. You can then load the data locally as shown in the [tutorial code](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#load-the-data), adjusting the code to your local path.

Here are the first 5 rows of the `dtc` dataset:

{{% codeblock %}}
```R
head(dtc)
```
{{% /codeblock %}}

```R
 st statefip year adopt_year     unins
1 AL        1 2008         NA 0.1964095
2 AL        1 2009         NA 0.2141095
3 AL        1 2010         NA 0.2300015
4 AL        1 2011         NA 0.2250678
5 AL        1 2012         NA 0.2159348
6 AL        1 2013         NA 0.2218695
```

 
- Dependent variable: `unins` (uninsurance rate)
- Treatment variable: `adopt_year` (the first year ACA Medicaid expansion was adopted in a state, or `NA` if never adopted)

2. Construct the stacked dataset

Start with a long-form panel dataset where each row represents a unit by calendar time observation. Use the `create_sub_exp()` function in R (define this function first with [the tutorial code](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#the-create_sub_exp-function)) to create a sub-experimental dataset for each specific adoption year. Then, run a loop to apply the function to each adoption year, making multiple sub-experiments. With `kappa_pre` and `kappa_post`, defining how many years before and after the treatment are included (inclusion criteria 1). Finally, combine all individual sub-experiments into a single [stacked dataset](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#the-create_sub_exp-function):

{{% codeblock %}}
```R

# create the sub-experimental data sets
events = dtc[is.na(adopt_year) == FALSE, funique(adopt_year)]

# make a list to store the sub experiments in.
sub_experiments = list()

# Loop over the events and make a data set for each one
for (j in events) {
  sub_name = paste0("sub_",j) 
  sub_experiments[[sub_name]] = create_sub_exp(
    dataset = dtc,
    timeID = "year",
    groupID = "statefips", 
    adoptionTime = "adopt_year", 
    focalAdoptionTime = j,
    kappa_pre = 3,
    kappa_post = 2)
}

# Vertically concatenate the sub-experiments
stackfull = rbindlist(sub_experiments)

# Remove the sub-experiments that are not feasible
stacked_dtc = stackfull[feasible == 1]

```
{{% /codeblock %}}


3. Compute the weights 

Simple stacked regression can be biased because it weights treatment and control group trends differently. To correct this bias, a sample weight can be defined.  

Use the `compute_weights()` function to assign weights to each sub-experiment in the `stacked_dtc` dataset, following the trimmed aggregate ATT weighting method. You must [define this function first](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#the-compute_weights-function). Here's how you apply it:

{{% codeblock %}}
```R
stacked_dtc2 = compute_weights(
  dataset = stacked_dtc,
  treatedVar = "treat",
  eventTimeVar = "event_time",
  subexpVar = "sub_exp")
```
{{% /codeblock %}}


4. Estimate the stacked regression

To analyze the aggregate impact of the treatment, run the regression using the `feols()` function from the `fixest` package in R. This function allows you to account for weights and clustering:

{{% codeblock %}}
```R

# Fit the event study model, using the weights, clustering at the state level.
weight_stack = feols(unins ~ i(event_time, treat, ref = -1) | treat + event_time, 
                     data = stacked_dtc2, 
                     cluster = stacked_dtc2$statefip,
                     weights = stacked_dtc2$stack_weight)

# display results
etable(weight_stack)
```
{{% /codeblock %}}

```R
                               weight_stack
Dependent Var.:                       unins
                                           
treat x event_time = -3    -0.0010 (0.0037)
treat x event_time = -2    -0.0030 (0.0030)
treat x event_time = 0  -0.0163*** (0.0039)
treat x event_time = 1  -0.0239*** (0.0065)
treat x event_time = 2  -0.0255*** (0.0071)
Fixed-Effects:          -------------------
treat                                   Yes
event_time                              Yes
_______________________ ___________________
S.E.: Clustered                 by: cluster
Observations                            600
R2                                  0.42775
Within R2                           0.01288
---
Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1


``` 
The analysis reveals a negative effect of the ACA Medicaid expansion on insurance rates. This is indicated by the negative significant coefficients observed in the year of the expansion (`-0.0163`), as well as one and two years (`-0.0239` and `-0.0255`) following the expansion. 

{{% tip %}}

Useful resources:

- Learn more about [the R package `fixest`](/fixest), which is ideal for analyzing panel data and fixed effects models. 
- Get a comprehensive overview of [linear regression analysis](/analyze/regression)
- Dive deeper into [Fixed Effects models](/within).
- Learn how to interpret [linear regression output in R](/regressionoutput)

{{% /tip %}}


{{% summary %}}

- The basic *Stacked DiD* approach involves aggregating data from various treatment adoption events to evaluate overall treatment effects in staggered settings. 
- The [*Weighted Stacked DiD* framework](https://www.nber.org/papers/w32054) addresses a potential bias in the basic Stacked DiD approach caused by imbalances in treatment and control trends. It involves trimming the dataset to ensure balance and aggregating estimates using weighted methods. 
- [A straightforward guide]((https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html)) is available for implementing weighted regressions to obtain accurate ATT estimates, with code examples in R and Stata.
{{% /summary %}}



## References

- [Working paper of Wing et al. (2024) - Stacked Difference-in-Differences](https://www.nber.org/papers/w32054), introducing the weighted Stacked DiD framework 

- [Tutorial including functions to implement the stacked DID estimator in R and Stata](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html)

