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

In this article, we explore how the *Stacked DiD* method for analyzing staggered treatment designs. We focus on the *Weighted Stacked DiD* by [Wing et al. (2024)](https://www.nber.org/papers/w32054), which addresses the imbalances in treatment and control trends inherent in the basic Stacked DiD approach.

## Basic Stacked DiD

The *Stacked DiD* method analyzes staggered designs by creating separate datasets for each valid subexperiment, excluding problematic late-early comparisons. These datasets are then combined, or "stacked", to analyze overall trends. 

{{% tip %}}

For more intuition on these problematic late-early comparisons, read [this topic](/goodman-bacon).

{{% /tip %}}

An important shortcoming of the basic stacked DiD design is *the imbalance in treatment and control trends* across different subexperiments, which can lead to a biased causal parameter. 

## Imbalance in trends

Each subexperiment has different lenghts of pre-and post-treatment periods because some groups are treated earlier than others. When aggregating across different subexperiments, and averaging all the group-specific effects of the treated groups, the composition of the treatment group changes. As a result, the regression essentially weights treatment and control trends differently across subexperiments.

{{% example %}}

Suppose you are measuring the treatment effect over four time periods, from 2020 to 2024. There is an *early-treated* group (treated in 2020) and a *late treated group* (treated in 2023). The effect is heterogeneous across groups: The early-treated group experiences a negative effect, while the late-treated group experiences a positive effect.

To find the overall treatment effect, you aggregate these effects from the different groups (i.e, sub-experiments). At first glance, the treatment effect appears to fade out over time. However, this is not due to the actual treatment but rather a result of *compositional imbalance*. Three years after the treatment (event time = 3), the aggregated coefficient only includes the *early-treated group* (treated in 2020), because the effect on the *late-treated group* (treated in 2023) is not observed yet!

{{% /example %}}

{{% tip %}}

*Event time*

Event time refers to the specific point at which a unit, is exposed to treatment within a study. This concept differs from the usual "calendar time" (e.g., the years 2020, 2021, 2022), and it helps standardize comparisons across units that are treated at different times. 

For instance, *event time = 0* marks the moment a unit receives treatment, *event time = 1* indicates one year after treatment, *event time = 2* refers to two years after treatment, and *event time = -1* represents one year before treatment. 

{{% /tip %}}

The potential bias caused by compositional imbalance is known, as it is a function of the sample sizes of each subexperiment. The next section introduces a new weighted approach to address the bias.

## Weighted stacked DiD

[Wing et al. (2024)](https://www.nber.org/papers/w32054) propose a *weighted stacked DiD design* that corrects for this imbalance, using sample weights. Summarizing their framework, it consists of three steps.

1. Trimming the dataset
2. Aggregation of subexperiments 
3. Stacked DiD estimation


### 1. Trimming the dataset

They offer a solution for this compositional imbalance that biases the parameter, by trimming the dataset (i.e, the subexperiments) to make them balanced over a fixed event time window. In other words, you take out the subexperiments that do not have enough follow-up years. 

Two inclusion criteria are used to trim the sample:

1. *Adoption event window*: The treatment adoption took place inside the *k* event window. (The *k* window, with is a research design choice.)


2. *Existence of clean controls*: There must be one or more "clean control" units that can serve as the comparison group for a treatment adoption event in this dataset. The exact "clean control" definition is a choice and depends on the study context. For example, it should not be exposed to the treatment at any time during the *k* event time period but at some future date (*not-yet treated*), or not be exposed to treatment at all (*never treated*). 


### 2. Aggregation of subexperiments

After trimming the dataset to avoid imbalances, you can calculate group-time ATT (*Average Treatment Effect on the Treated*) parameters for each subexperiment. To obtain a summary average of these estimates, you then aggregate the results from all subexperiments. 

One approach to aggregate the group-specific ATT values is the *trimmed aggregate ATT*,  denoted as $\theta_\kappa ^\epsilon$. It weighs the group-time ATT by its share of the trimmed treated sample. Specifically:

{{<katex>}}
{{</katex>}}

$$\theta_\kappa ^\epsilon = \sum_{\substack{a \in \Omega_\kappa }} ATT(a,a+e) * \frac{N_a ^D}{N_\Omega ^D} $$

Where:
- The first part consists of the group-specific ATT within the fixed event time window ($e$), where $a$ represents the subexperiment or treatment adoption event. 

- The second part assigns a weight to these ATT values by multiplying by its fraction of the total treatment group:
  - $N_a^D$ is the number of treated units in sub-experiment a 
  - $N_\Omega^D$ = total number of treated units in the trimmed set

{{% tip %}}

Other approaches, other than the *trimmed aggregate ATT*, include:

- *Population-weighted ATT*: This method weights the group-time ATT by its share of the treated population (instead of the treated sample) 

- *The sample share weighted ATT*: This method weighs the group-time ATT by its overall share of the stacked analytic sample (including both treated and control units in each subexperiment).

The best weighting scheme ultimately depends on the specific application and study context. Refer to [Section 4 of the paper](https://www.nber.org/papers/w32054) for more information on these alternative approaches.

{{% /tip %}}


### 3. Stacked DiD Estimation 

In this section, we demonstrate how to apply the *Stacked DiD* method to a staggered design. This approach allows you to estimate the aggregate treatment effect efficiently using a linear regression model. 

The authors have developed functions to apply their framework easily in both Stata and R. Their [tutorial with code example](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#load-the-data) provides detailed guidance. As a case study, they examine the impact of the ACA (*Affordable Care Act*) Medicaid expansion, a health insurance program for low-income groups, on uninsurance rates. This analysis takes advantage of the staggered adoption of the treatment by states in different years.

In this section, we guide you through the most important steps of the analysis, providing some extra tips.

- Load the data

You can download the CSV dataset from [Alex Hollingworth's GitHub page](https://github.com/hollina/stacked-did-weights/tree/main/data). Save this to your comptuer to load it locally as done in [the tutorial](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#load-the-data). Or, the following code snippet allows you to load the data directly:

{{% codeblock %}}
```R

# specify URL to CSV file on GitHub page
data_url <- "https://raw.githubusercontent.com/hollina/stacked-did-weights/main/data/acs1860_unins_2008_2021.csv"

# load CSV file from URL
dtc <- read.csv(url(data_url))
```
{{% /codeblock %}}

This is what the first 5 rows look like of the example dataset `dtc`:

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

 
- The dependent variable is `unins` (uninsurance rate)
- The treatment variable is `adopt_year` (the first year ACA Medicaid expansion was adopted in a state, or `NA` if never adopted)

- Construct the stacked dataset

You start with a long-form panel dataset where each row represents a unit by calendar time observation. 

You can use the `create_sub_exp()` function in R (define function first with code in [this section](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#the-create_sub_exp-function)) to construct a sub-experimental dataset for each specific adoption year. Then, run a loop to apply the function to each adoption year, creating multiple sub-experiment. Lastly, combine all individual sub-experiments into a single large [stacked dataset](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#the-create_sub_exp-function):

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


- Compute the weights 

The simple stacked regression is biased because it weights treatment and control group trends different. To correct for the bias, define a sample weight.  

Use the [`compute_weights()` function](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html#the-compute_weights-function) to the `stacked_dtc` dataset to assign a weight to each sub-experiment:

{{% codeblock %}}
```R
stacked_dtc2 = compute_weights(
  dataset = stacked_dtc,
  treatedVar = "treat",
  eventTimeVar = "event_time",
  subexpVar = "sub_exp")
```
{{% /codeblock %}}


- Estimate the stacked regression

To analyze the aggregate impact of the treatment, run the regression with the `feols()` function from the `fixest` package in R.


{{% tip %}}
Refer to [this topic](\fixest) to learn more about the functionalities of `fixest`, the R package ideal for analyzing panel data. 

{{% /tip %}}


{{% codeblock %}}
```R

# Fit the event study model, using the weights, clustering at the state level.
weight_stack = feols(unins ~ i(event_time, treat, ref = -1) | treat + event_time, 
                     data = stacked_dtc2, 
                     cluster = stacked_dtc2$statefip,
                     weights = stacked_dtc2$stack_weight)
```
{{% /codeblock %}}



{{% summary %}}


{{% /summary %}}



## See also




- [Example code](https://rawcdn.githack.com/hollina/stacked-did-weights/18a5e1155506cbd754b78f9cef549ac96aef888b/stacked-example-r-and-stata.html)

