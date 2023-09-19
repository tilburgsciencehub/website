---
title: "Staggered Difference-in-Difference Estimation"
description: "Staggered difference-in-difference estimation in R using the `did` package"
keywords: "difference-in-difference, causal inference, did, DID, staggered treatment, regression, model "
draft: false
weight: 2
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /staggered-did
---

# Overview
Difference-in-Difference (DiD) analysis serves as a valuable tool for evaluating the causal impact of interventions in observational studies. It involves comparing changes in outcomes between a treatment group and a control group before and after the introduction of an intervention. While the traditional DiD framework typically revolves around two distinct groups and two specific time periods, real-world applications often present more intricate scenarios with multiple time intervals and varying treatment timings.

In such complex situations, where interventions are implemented at different times for different units or groups, we encounter what is known as a "staggered" treatment setup. For instance, consider the need to assess the effects of diverse promotional strategies rolled out across different stores or regions at various points in time, or the impact of healthcare reform policies implemented across distinct regions. In these cases, the conventional DiD framework may not be suitable.

[Recent research](https://www.sciencedirect.com/science/article/pii/S0304407621001445), as discussed in , has shed light on the limitations of the traditional approach in these staggered treatment scenarios. It has been revealed that using the standard method can lead to potentially misleading estimates of treatment effects, sometimes even indicating effects in the opposite direction of the actual impact.

In this building block, we delve into the intricacies of scenarios where the traditional DiD setup falls short—specifically, those involving staggered treatment timing and a multitude of time periods. You will gain insights into:

- The concept of staggered treatment within the context of Difference-in-Difference (DiD) analysis.
- The inherent challenges and issues associated with applying the conventional DiD approach to staggered treatment settings.
- The fundamental assumptions underpinning the staggered DiD methodology.
- The notable advantages offered by the staggered DiD approach.
- Practical implementation of staggered DiD estimation using the `did` package in the R programming language.


## Common Issues with the Conventional DiD Approach

Why is it problematic to apply the standard DiD setup in staggered treatment scenarios? The traditional DiD framework functions adequately when dealing with scenarios featuring only two time periods and a consistent treatment effect. However, in staggered treatment cases, this approach often falls short of capturing the intricacies of the real-world dynamics.

Several factors contribute to this limitation, including the potential for the treatment effect to fluctuate over time or among different groups due to factors such as learning curves, adaptation, or changing external conditions. Additionally, some units may exhibit immediate responses to treatment, while others might require more time to react. The conventional approach's one-size-fits-all methodology may not effectively account for these variations.

More specifically, the treatment effect estimate in the traditional DiD approach is essentially a weighted average of treatment effects. These weights can sometimes be negative, even if the overall treatment effect is positive. Consequently, this can lead to misleading estimates of the treatment effect, where the average effect appears negative, despite the actual positive impact of the intervention.

## An Illustrative Example: Steps for Staggered DiD Estimation

In this illustrative example, we investigate the impact of the Questions and Answers (Q&A) feature on ratings and reviews within online platforms. Specifically, we analyze data from two prominent platforms: Goodreads and Amazon. Goodreads serves as the treatment group, as it offers users the ability to rate and review books while also providing the Q&A feature. In contrast, Amazon serves as the control group because it enables users to rate and review products but lacks the Q&A feature for books.

This scenario presents a staggered treatment setup, where various books receive questions at different points in time. This staggered treatment timing introduces variations that would yield biased estimates when using the conventional DiD framework. To address this issue, we employ a modern DiD technique proposed by [Callaway and Sant Anna (2021)](https://www.sciencedirect.com/science/article/pii/S0304407620303948), implemented using the `did` [package](https://bcallaway11.github.io/did/articles/did-basics.html).

This technique offers two primary advantages:

1. **Enhanced Control Group Selection:** It provides greater flexibility in choosing control groups. Specifically, it allows us to utilize "not-yet treated units" as controls, in addition to "never-treated" units. In our context, this means that a book receiving its first question in July 2017 can serve as a control for a book that received its first question in May 2017. The "never-treated" units comprise books on Amazon that never receive questions.

2. **Covariate Incorporation:** This method accommodates the inclusion of covariates, thereby ensuring that the parallel conditions assumption holds conditionally on these covariates.


### Identifying Assumptions

To ensure the validity of staggered DiD estimation, we rely on several key assumptions:

- **Staggered treatment adoption:** This assumption posits that once units receive treatment, they remain treated throughout the observation period.
- **Parallel Trends Assumption with Never-Treated Units:** When we examine groups and time periods where treatment isn't applied $(C=1)$, we assume that the average potential outcomes for the group initially treated at time $g$ and the group that never received treatment would have followed similar trends in all post-treatment periods $t\geq g$.

Formally, for all $g=2,…, \mathcal{T}, t = 2,...,\mathcal{T} $ such that $t \geq g$,
{{<katex>}}
{{</katex>}}

$$\mathbb{E}[Y_t(0) - Y_{t-1}|G_g=g] = \mathbb{E}[Y_t(0)-Y_{t-1}(0)|C=1]$$



However, this assumption relies on two important conditions:

(i) There must be a sufficiently large group of units that have never received treatment in our data.

(ii) These never-treated units must be similar enough to the units that eventually receive treatment so that we can validly compare their outcomes.

In situations where these conditions are not met, we can use an alternative parallel trends assumption that involves the **not-yet treated units** as valid comparison groups.

- **Parallel Trends Assumption with Not-Yet Treated Units:** When we're studying groups treated first at time $g$, we assume that we can use the units that are not-yet treated by time $s$ (where $s \geq t$) as valid comparison groups for the group initially treated at time $g$.

Formally, for all $g=2,…,\mathcal{T},s,t=2,...,\mathcal{T}$ such that $t \geq g$ and $s \geq t$,

$$\mathbb{E}[Y_t(0) - Y_{t-1}|G_g=g] = \mathbb{E}[Y_t(0)-Y_{t-1}(0)|D_s = 0, G \neq g]$$


In certain scenarios, the credibility of the parallel trends assumption is enhanced when we consider pre-treatment characteristics (covariates). In such cases, the parallel trends assumptions take on a conditional nature, allowing for **covariate-specific trends** in outcomes across groups. This becomes particularly valuable when the distribution of covariates varies among groups.

For instance, when dealing with book-related data, various characteristics like popularity, genre, publication date, and more can vary across books. To apply the conditional parallel trends assumption in this context, you would condition the assumption on these relevant book-level characteristics. This means that, before the introduction of the Q&A feature, books with similar attributes, such as genre, author reputation, or publication date, should have exhibited comparable trends in ratings.

## Estimation

### Load Data

The dataset consists rating and question data for 5000 unique books on Goodreads and Amazon. The complete set of codes for data processing and estimation can be found in this [Gist](https://gist.github.com/srosh2000/13be23a4a37e16d21d2842e704b2c60d).

{{% codeblock %}}
```R
# Load packages
library(data.table)
library(dplyr)
library(tidyr)
library(zoo)
library(did)
library(lubridate)
library(googledrive)
library(ggplot2)

#### --- Load data ---###
# Download data from google drive

drive_deauth()

file_id<- "1e-VogI4zQPi_xbSydVLH7PrgkOlWpczl"

drive_download(as_id(file_id), overwrite = TRUE)

GoodAma_sample<- fread("GoodAma_sample.csv")
```
{{% /codeblock %}}   

### Data requirements

- The dataset should be in *long* format where each row corresponds to a particular unit of observation at a particular point in time.

<p align = "center">
<img src = "../images/dataset-overview.png" width="700">
<figcaption> Overview of the dataset </figcaption>
</p>

- There must be an identifier variable that is unit specific and does not vary over time. In this case `asin` is the book identifier.
- There must be a time variable - here it is `year_month`
- There must be a group variable, which is usually the time period when an individual first becomes treated. For units that are *never treated*, this variable should be set to 0! In our case, `period_question` is the group variable as it indicates the time period a given book receives its first question.
- The variables must be of numeric class.


### Effect of Q&A on book ratings using “not-yet treated” units as control

We use the `att_gt()` function to estimate group-time average treatment effect.

{{% codeblock %}}
```R
staggered_notyettreated <- att_gt(yname = "rating", # outcome variable
                                  tname = "period_review", # time variable
                                  idname = "asin", # id variable
                                  gname = "period_question", # first treatment period variable
                                  control_group = "notyettreated", # set the comparison group as either "never treated" or "not yet treated"
                                  data = goodreads_df, # data
                                  xformla = NULL, # add covariates here but it is set to default in this case
                                  allow_unbalanced_panel = TRUE # indicate whether or not the function should balance with respect to time and id
)

summary(staggered_notyettreated)
```
{{% /codeblock %}}


In cases where there are a large number of groups and time periods, it may be infeasible to interpret all of the group-time average treatment effect coefficients. Thus, we can aggregate group-time average treatment effects using the ``aggte()`` function.

{{% codeblock %}}
```R
# aggregate the group-time average treatment effects

staggered_notyettreated_aggregate<- aggte(staggered_notyettreated, type = "dynamic", na.rm = TRUE)
summary(staggered_notyettreated_aggregate)

# Plot group-time ATTs
staggered_notyettreated_plot<- ggdid(staggered_notyettreated_aggregate)+ labs(x = "Time Relative to Q&A Adoption (in 30-day bins)", y = "ATT")
print(staggered_notyettreated_plot)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/aggte-notyettreated.png" width="500">
<figcaption> Aggregated Group-Time Effects with Not-Yet Treated Units as the Control Group </figcaption>
</p>

We find that the Q&A feature leads to a decrease in star ratings by 0.13 stars (p < 0.1).
### Plotting Treatment Effects

Next, we can plot the dynamics of this effect over time using the `ggdid()` function. All of the data has been reframed in relative event/treatment time.

{{% codeblock %}}
```R
# Plot group-time ATTs
staggered_notyettreated_plot<- ggdid(staggered_notyettreated_aggregate)+ labs(x = "Time Relative to Q&A Adoption (in 30-day bins)", y = "ATT")
print(staggered_notyettreated_plot)
```
{{% /codeblock %}}

Notice how 12 months prior, there are essentially no differences between treatment and control group units which provides some support for the parallel trends assumption. But, post Q&A, the ratings go down.

<p align = "center">
<img src = "../images/ggdid-notyettreated.png" width="700">
<figcaption> Event Study Plot </figcaption>
</p>

{{% summary %}}
- Staggered treatment occurs when interventions vary in timing across units or groups.

- Traditional DiD approach works well for cases with two groups and time periods with constant treatment effects but falls short in scenarios with staggered treatments and multiple time periods due to heterogeneous treatment effects and negative weighting issue which can yield misleading estimates.

- Modern DiD techniques offer advantages such as flexible control group selection and the incorporation of covariates.

- Identifying assumptions for staggered DiD include the persistence of treated units and (conditional) parallel trends.

- Staggered DiD can be estimated in R using the `did` package.

- `att_gt()` is used to estimate group-time average treatment effect.

- `aggte()` is used to *aggregate* group-time average treatment effects.

- `ggdid()` is used to visualise the treatment effects.


{{% /summary %}}

# See Also

- [Two-Way Fixed Effects and Differences-in-Differences with Heterogeneous Treatment Effects: A Survey](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3980758)
- [Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects](https://www.aeaweb.org/articles?id=10.1257/aer.20181169)
- [Estimating dynamic treatment effects in event studies with heterogeneous treatment effects](https://www.sciencedirect.com/science/article/pii/S030440762030378X?via%3Dihub)
- [The Role of Parallel Trends in Event Study Settings: An Application to Environmental Economics](https://www.journals.uchicago.edu/doi/10.1086/711509)
