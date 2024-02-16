---
title: "Matching"
description: "Matching is used to create comparable groups in observational studies, helping to mitigate the effects of confounding variables and estimate causal effects."
keywords: "matching, causal, inference, effect,regression, R, exact, approximate"
draft: false
weight: 1
author: "Valerie Vossen"
aliases:
  - /exact-matching
  - /matching
---

# Overview

Randomization is a fundamental principle in experimental design, aiming to have a good counterfactual and ensuring treatment and control group are similar except for being treated. However, in certain cases, treatment is not randomly assigned and confounders can bias the estimated causal effect.

Matching is an alternative approach, which involves pairing individuals or units based on specific characteristics to create comparable groups. This article provides a comprehensive introduction of matching methods, focusing on both theory and practical applications.

## Exact and approximate matching

Exact matching involves pairing individuals who share **identical characteristics**. This requires the observable characteristic on which pairing happens to be a binary variable. Also the sample should contain observations in the control group for each binary variable in the treatment group to be able to get matched.

In contrast, [approximate matching](/approximate-matching) allows for some degree of flexibility and pairs on similar but not identical characteristics. 


## Identifying assumptions

{{% summary %}}
1. Conditional Independence Assumption:
2. Conditional on X, there are treated and untreated units (common assumption)

{{% /summary %}}



### Conditional Independence Assumption (CIA)

The most important assumption underlying matching is the Conditional Independence Assumption.

It states that once observable characteristics (the covariates) are taken into account, the assignment of treatment becomes independent of potential outcomes. 

In other words, **given a set of observed characteristics, there should be no systematic differences in potential outcomes between the treatment and control groups** (respectively Y0 and Y1). 

This is expressed as follows:

(Y0, Y1) ⊥ T|X

which states that potential outcomes in the treatment and control group (expected values for Y0 and Y1) are independent of treatment assignment T, for each value of X. The X is the binary variable on which the groups are based.

{{% warning %}}
Assumes that there are no unobservable characteristics that differ across these groups and significantly affect treatment probability and effect; this is an assumption that can not be tested and you are willing to make to establish causality.
{{% /warning %}}



### Assumption 2 

---


## Exact matching estimator


If these two assumptions are true, the following identity follows:

\begin{align*}
E[Y_1 - Y_0 | X] &= E[Y_1 - Y_0 | X, D = 1] - E[Y_0 | X, D = 0] \\
&= E[Y | X, D=1] - E[Y | X, D=0]
\end{align*}

The average effect of the treatment on the treated (ATT) is estimated by taking the expected outcome of the treatment group minus the expected outcome of the matched controls, averaged out over the treatment group. 

The expression can be written as follows:

\hat{d}_{\text{ATT}} = \frac{1}{N_T} \sum_{D = 1} (Y_i - Y_{j(i)})

where:
- *\hat{d}_{\text{ATT}}* is the estimated average treatment effect on the treated
- *N_{T}* is the total number of units in the treatment group
- *D* is the indicator variable for being treated (1 = treated, 0 = control)
- *Y_{i}* is the outcome variable of the treated unit i
- *Y_{j(i)}* is the outcome variable of the control unit matched to unit i


{{% tip %}}
The counterfactual is the mean outcome in control group for observations with the exact same characteristics. 
{{% /tip %}}


## Practical example exact matching

A simple practical example of exact matching will be shown with a data set that is generated for the purpose of this example. The goal is to find the effect of a graduate traineeship programme on earnings. The data set contains data of 100 employees, of which 50 completed a traineeship at the start of their career (the treatment group) and 50 did not (the control group).


First, load packages and data.

{{% codeblock %}}
```R
library(MatchIt)

# Load data
data_url <- "https://raw.githubusercontent.com/tilburgsciencehub/website/master/content/topics/Analyze/causal-inference/matching/jobtraining.Rda"
load(url(data_url))

View(jobtraining)
```
{{% /codeblock %}}

However, when observing the data, you notice the treatment and control group are not similar. People who followed the traineeship are on average younger (26 years) than people who did not follow the traineeship (39 years). 

{{% codeblock %}}
```R
# Average age for the treatment group
mean(jobtraining$Age[jobtraining$Treatment == 1])

# Average age for the control group
mean(jobtraining$Age[jobtraining$Treatment == 0])
```
{{% /codeblock %}}

If younger people have lower earnings on average, the effect of the traineeship is likely to underestimated. 


First, we calculate the treatment effect without taking this age difference into account.

{{% codeblock %}}
```R
ATT_original <-  mean(jobtraining$Earnings[jobtraining$Treatment == 1] - mean(jobtraining$Earnings[jobtraining$Treatment == 0]))

print(ATT_original)

```
{{% /codeblock %}}

The ATT is -998.26. If you don't take the age difference into account, you find a negative effect of the traineeship programme on earnings...

The solution is to match a treated employee to an untreated employee on age, and compare their earnings instead!

You can do this with the matchit() function, to match observations, specifying Treatment and Age. 

{{% codeblock %}}
```R
matched_jobtraining <- matchit(Treatment ~ Age, data = jobtraining, method = "exact")

# Extract the matched dataset
matched_jobtraining <- match.data(matched_jobtraining)

```
{{% /codeblock %}}


Calculate the ATT, but now on the matched sample.

{{% codeblock %}}
```R
ATT_matching <- mean(matched_jobtraining$Earnings[matched_jobtraining$Treatment == 1] - matched_jobtraining$Earnings[matched_jobtraining$Treatment == 0])

print(ATT_matching)

```
{{% /codeblock %}}

The ATT is 7968.828, suggesting a positive effect of the traineeship programme.


{{% summary %}}


{{% /summary %}}






