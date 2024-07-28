---
title: "The Goodman-Bacon Decomposition"
description: "The limitations of the TWFE estimator in staggered DiD settings and the use of the Goodman-Bacon decomposition as a diagnostic"
keywords: "difference-in-difference, causal inference, did, DID, staggered treatment, regression, model, DiD, R, event study, Goodman-Bacon decomposition, Bacon decomposition, TWFE, two-way fixed effects"
draft: false
weight: 6
author: "Victor Arutyunov"
aliases:
- /goodman-bacon
- /bacon-decomp
---

## Overview 

[Staggered difference-in-differences (DiD)](/staggered-did) and [event study designs](/event-studies) allow for causal inference in settings where units are treated at different times – for example, Covid-19 restrictions that were introduced on different days in different countries or states. In such cases, the conventional two-way fixed effects (TWFE) method designed for [classic DiD studies](/canonical-DiD) with just 2 groups and 2 periods may yield incorrect and biased results.  

The Goodman-Bacon decomposition is a descriptive tool which allows us to see how the staggered DiD estimator is actually constructed and to assess how likely it is to give biased results in our context. In this topic, we will discuss why TWFE may fail in staggered treatment settings, what the Goodman-Bacon decomposition is and why it’s useful, and explore an applied example in R.  

{{% tip %}} 

This topic deals with the reasons behind the shortcomings of TWFE in staggered DiD designs and how the Goodman-Bacon decomposition allows us to observe them. For ways to address the limitations of TWFE, see [this topic](/staggered-did), which introduces Callaway and Sant’Anna’s (2021) robust method.  

{{% /tip %}} 

## Staggered treatment and shortcomings of TWFE 

The [TWFE model](/within) is widely used for causal inference with [panel data](/paneldata) – that is, data which includes observations across both different cross-sectional groups and different time periods. It is estimated with two types of fixed effects:  

1. Group fixed effects: these capture group-specific unobservable characteristics that are constant across time.  

2. Time fixed effects: these capture time trends, or differences between time periods, that are common to all groups.  

This model works well when we only have two groups and two time periods (one before and one after treatment). When we have more than two groups or more than two time periods, our treatment estimate becomes a weighted average of all 2x2 TWFE comparisons – all instances where one group changes its treatment status while another’s treatment status remains unaltered.  

{{% example %}} 

Suppose that we are studying the effects of Covid-19 lockdowns on Covid-19 infections. Our unit of observation are wards across three cities – A, B, and C. City A introduces a Covid-19 lockdown in week 1, city B introduces a lockdown in week 2, and city C does not introduce any restrictions. This is a typical case of staggered treatment timing: city A is treated earlier, city B is treated later, and city C is never treated.  

Our TWFE estimate in this case would be a weighted average of all possible 2x2 comparisons between the cities. That is, city A vs city B for weeks 0 and 1, city A vs city B for weeks 1 and 2, city B vs city C for weeks 1 and 2, etc. The weights attached to each comparison would depend on the number of observations in the compared groups (in our case, the number of wards in the compared cities) and how much the treatment indicator varies within each comparison. 

| City/Week | 0 | 1 | 2 |
| -------- | ------- | ------- | ------- |
| A | Not Treated | Treated | Treated |
| B | Not Treated | Not Treated | Treated |
| C | Not Treated | Not Treated | Not Treated |

{{% /example %}} 

The weighted average of all 2x2 comparisons is problematic for two reasons: 

1. Forbidden comparisons/contrasts: in our example, one of the 2x2 comparisons that form part of the final TWFE estimate is as follows: 

| City/Week | 1 | 2 |
| -------- | ------- | ------- |
| A | Treated | Treated |
| B | Not Treated | Treated |

The group that changes its treatment status here (i.e., the treatment group) is city B, as it goes from being untreated in week 1 to being treated in week 2. City A therefore serves as the control group, even though it is actually treated in both weeks!  

This would not be a problem if the treatment effect were completely constant over time, as city A would not see any changes in the outcome from week 1 to week 2 _due to the treatment_. However, this is very rarely the case: treatment effects are often dynamic – they can vary over time due to adaptation or learning effects, for example. 

The implication of these forbidden comparisons is that our supposedly causal TWFE estimates are partly composed of non-causal, biased coefficients, which actually compare treatment to treatment, as opposed to treatment to control.  

2. Negative weights: each comparison is assigned a weight which is proportional to group size (the number of observations within the group) and variation in treatment exposure. The larger the group size and the smaller the variation in treatment exposure, the higher the attached weight. All weights sum to one, but they can also be negative – sometimes, the comparisons at the tails of the time period distribution (in very early or very late periods) can carry negative weights, as treatment variation is typically smaller there (as most groups are not yet treated in early stages or already treated in late stages).  

{{<katex>}}
{{</katex>}}

The problem with negative weights is that they can bias our final estimate by altering the direction (sign) of the effect. Let’s suppose we have three comparisons with coefficients of 0.5, 1, and 5 and weights of 0.8, 0.8, and –0.6, respectively. Our total effect is then: $0.5*0.8 + 1*0.8 + 5*(-0.6) = -1.8$. We therefore obtain a negative treatment effect estimate even though each of the individual comparisons yields a positive effect of the treatment! 

## The Goodman-Bacon decomposition 

The Goodman-Bacon decomposition is a diagnostic tool which allows us to see whether our TWFE estimator is reliant on forbidden comparisons or negative weights. The decomposition breaks down the estimator into three types of comparisons: 

1. Treated vs. never treated: this is equivalent to the classic 2x2 DiD comparison. We are only comparing treated to untreated units. 

2. Early treated vs. late control: we are comparing units that are treated early to units that will be treated later, but have not been treated yet. 

3. Late treated vs. early control: we are comparing units that are treated later to units that have _already been treated_ – this is a forbidden comparison! 

{{% tip %}} 

‘Early’ refers to the group that is treated earlier, ‘late’ refers to the group treated later. Therefore, a comparison called ‘early treated’ vs. ‘late control’ simply means that the comparison uses the early group as the treated group and the late group as the control group. In our example, an early treated vs. late control comparison would be city A vs. city B, with city A as the treatment group and city B as the control group. 

{{% /tip %}} 

The decomposition also allows us to see the weight attached to each type of comparison. This way, we are able to see how our overall TWFE estimate is constructed and whether it is prone to the limitations and biases discussed above. In practice, computing the Goodman-Bacon decomposition is very straightforward with the `bacondecomp` [package](https://github.com/evanjflack/bacondecomp) in R.  

## An example in R 

The `bacondecomp` package contains datasets from three papers using DiD/event study designs with staggered treatment timing. We will use the dataset from [Stevenson and Wolfers (2006)](https://academic.oup.com/qje/article/121/1/267/1849020), who study the effects of unilateral divorce laws on female suicide rates in the US, exploiting variation in the timing of the introduction of these laws across states.

First, we install and load the package:


{{% codeblock %}}
```R
install.packages("bacondecomp") #install the package
library(bacondecomp) #load the package
```
{{% codeblock %}}

Next, we load the data and prepare it for our analysis:

{{% codeblock %}}
```R
wolfers_df <- bacondecomp::divorce #load the Stevenson & Wolfers data
wolfers_df <- subset(wolfers_df, sex==2) #isolate female suicide rates
wolfers_df$ln_suicide <- log(wolfers_df$suicide) #create log of outcome variable
```
{{% /codeblock %}}

Finally, we are able to derive the Goodman-Bacon decomposition using the `bacon` function:

{{% codeblock %}}
```R
#changed is our treatment dummy
df_bacon <- bacon(ln_suicide ~ changed, #regression equation
                  data = wolfers_df,
                  id_var = "st", #group (state) fixed effects
                  time_var = "year") #time (year) fixed effects
df_bacon 
```
{{% /codeblock %}}
_Output_
<p align = "center">
<img src = "../images/bacondecomp.png" width="400">
</p>

{{% warning %}}
In this case, we actually have 4 types of comparisons, because the data also includes states which had introduced unilateral divorce laws (that is, were treated) before the years that are included in the dataset. Therefore, some units are 'always treated'. 
{{% /warning %}}

We see that a very large weight (around 2/3 in total) is attached to forbidden comparisons ('Later vs Always Treated') and ('Later vs Earlier Treated') - that is, to cases where our control group has been treated in the past. As previously discussed, this can be a source of bias if the treatment effect is not homogenous over time (which is very likely to be the case). Therefore, these results of the Goodman-Bacon decomposition tell us that it is advisable to re-run our study using one of the recently created robust methods for staggered DiD, such as those proposed by [Callaway and Sant’Anna (2021)](/staggered-did) and [Abraham and Sun (2021)](https://www.sciencedirect.com/science/article/pii/S030440762030378X).

## Summary 

{{% summary %}}
- Conventional TWFE models may fail when estimating treatment effects in a setting with staggered treatment timing. This can happen because of forbidden comparisons (where our control group is actually being treated) or negative weights attached to certain comparisons. 

- The Goodman-Bacon decomposition is a useful diagnostic for the performance of TWFE estimators in DiD and event study settings with staggered treatment timing.  

- It decomposes the overall TWFE treatment estimate into three distinct components – treated vs never treated comparisons, early treated vs late control comparisons, and late treated vs early control comparisons and shows us what weight each component has. 

- If we detect an important presence of forbidden comparisons or bias arising from negative weights, we can use recently developed robust staggered DiD, such as those proposed by [Callaway and Sant’Anna (2021)](/staggered-did) and [Abraham and Sun (2021)](https://www.sciencedirect.com/science/article/pii/S030440762030378X). 
{{% /summary %}}

## See Also

[Difference-in-differences with variation in treatment timing - Goodman-Bacon (2021)](https://www.sciencedirect.com/science/article/pii/S0304407621001445)

[Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects - de Chaisemartin & D'Haultfœuille (2020)](https://www.aeaweb.org/articles?id=10.1257/aer.20181169)