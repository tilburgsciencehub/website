---
title: "Exact Matching"
description: "Matching is used to create comparable groups in observational studies, helping to mitigate the effects of confounding variables and estimate causal effects."
keywords: "matching, causal, inference, effect,regression, R, exact, approximate"
draft: false
weight: 1
author: "Valerie Vossen"
aliases:
  - /exact-matching
  - /matching
---

## Overview

Randomization is a fundamental principle in experimental design, aiming to have a good counterfactual and ensuring treatment and control group are similar except for being treated. However, in cases where treatment is not randomly assigned, confounding variables can bias the estimated causal effect.

Matching offers an alternative approach by basically creating an artificial counterfactual. This is done by pairing individuals or units based on specific observable characteristics to create comparable groups. This article provides a comprehensive introduction to matching, focusing on both the theory behind the method and practical applications.

## Exact and approximate matching

Exact matching involves pairing individuals who share **identical characteristics**. This requires the observable characteristic on which pairing happens to be a binary variable. Also ideally, the control group has many observations at each distinct value of the binary variable the observations are matched on. 

In contrast, [approximate matching, discussed in the next topic](/approximate-matching), allows for some degree of flexibility and pairs on similar but not identical characteristics. 


## Identifying assumptions

{{% summary %}}

There are two identifying assumptions that should hold for exact matching to be valid:

1. *Conditional Independence Assumption:* Given observed covariates *X*, there are no systematic differences between treated and untreated units.
<br>
<br>

2. *Overlapping support*: Conditional on *X*, there are treated and untreated units.

{{% /summary %}}


### 1. Conditional Independence Assumption (CIA)

The Conditional Independence Assumption is the primary assumption underlying matching. It state that **once we account for the observed characteristics of units or individuals, there should be no systematic differences in potential outcomes between the treatment and control groups**. 

Mathematically, this assumption is expressed as follows:

{{<katex>}}
(Y_{0}, Y_{1}) \perp T \:|\: X
{{</katex>}}

<br>
<br>

Where $Y_{0}$ and $Y_{1}$ are the potential outcomes in respectively the control and treatment group, which are independent of treatment assignment $T$ for each value of the observed covariates $X$. The $X$ is the binary variable(s) which the observations are matched.

{{% warning %}}
You are also assuming that there are no *unobservable* characteristics that may differ between these groups and could influence both the likelihood of receiving treatment and its effects. This assumption cannot be tested empirically, but is a logical premise you are willing to accept in order to establish causality.
{{% /warning %}}


### 2. Overlapping support

The assumption of overlapping support states that, conditional on observed covariates $X$, there exist both treated and untreated units across the entire range of 
$X$. In other words, there should be enough overlap in the distribution between the treatment and control groups to enable meaningful comparisons. This ensures that the treatment and control groups are comparable across all observed covariates, allowing for valid causal inference.


## Exact matching estimator

If the above two assumptions are valid, the following identity follows:

{{<katex>}}
E[Y_1 - Y_0 | X] = \\

E[Y_1 - Y_0 | X, D = 1] - E[Y_0 | X, D = 0] = \\

E[Y | X, D=1] - E[Y | X, D=0]
{{</katex>}}

<br>
<br>

The average effect of the treatment on the treated (ATT) is estimated by taking the expected outcome of the treatment group minus the expected outcome of the matched controls, averaged out over the treatment group. 

The expression can be written as follows:

{{<katex>}}
\hat{d}_{\text{ATT}} = \frac{1}{N_T} \sum_{D = 1} (Y_i - Y_{j(i)})
{{</katex>}}

where:
- $\hat{d}_{\text{ATT}}$ is the estimated average treatment effect on the treated
- $N_{1}$ is the total number of units in the treatment group
- $D$ is the indicator variable for being treated (1 = treated, 0 = control)
- $Y_{i}$ is the outcome variable of the treated unit $i$
- $Y_{j(i)}$ is the outcome variable of the control unit matched to unit $i$

{{% tip %}}
The counterfactual is the mean outcome in control group for observations with the exact same characteristics. 
{{% /tip %}}


## Practical example

A simple practical example of exact matching will be shown with a data set that is generated for this purpose.We are interested in finding the effect of a graduate traineeship programme on earnings. The data set contains data of 100 employees, of which 50 completed a traineeship at the start of their career (the *treatment group*) and 50 did not (the *control group*).


First, load the packages we need, and the dataset:

{{% codeblock %}}
```R
library(MatchIt)
library(ggplot2)
library(dplyr)

# Load data
data_url <- "https://raw.githubusercontent.com/tilburgsciencehub/website/master/content/topics/Analyze/causal-inference/matching/jobtraining_data.Rda"

data <- load(url(data_url))

View(data)
```
{{% /codeblock %}}

When observing the data, you notice the treatment and control group are not similar. People who followed the traineeship are on average younger (26 years) than people who did not follow the traineeship (39 years). 

{{% codeblock %}}
```R
# Average age for the treatment group
mean(data$Age[data$Treatment == 1])

# Average age for the control group
mean(data$Age[data$Treatment == 0])
```
{{% /codeblock %}}

The following histogram confirms this unequal distribution:

{{% codeblock %}}
```R
# Create a combined data frame for treatment and control groups
data$Group <- ifelse(data$Treatment == 1, "Treatment", "Control")

# Create the histogram
ggplot(data, aes(x = Age, fill = Group)) +
  geom_histogram(position = "identity", 
                 alpha = 0.5, 
                 bin_width = 1) +
  labs(title = "Age Distribution: Treatment vs. Control Group",
       x = "Age",
       y = "Frequency") +
  scale_fill_manual(values = c("blue", "red")
  )

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/histogram_age.png" width="400">
</p>

If younger people have lower earnings on average (which is likely to be the case), the effect of the traineeship is underestimated due to this unequal distribution of treatment assignment. First, we calculate the treatment effect without taking this unequal distribution of age into account.

{{% codeblock %}}
```R
ATT_original <-  mean(data$Earnings[data$Treatment == 1] - mean(data$Earnings[data$Treatment == 0]))

print(ATT_original)

```
{{% /codeblock %}}

The ATT is -998.26. If you don't take the age difference into account, you find a negative effect of the traineeship programme on earnings. To overcome the bias, the solution is to match a treated employee to an untreated employee on age, and compare their earnings instead! You can do this with the `matchit` function from the `MatchIt` in R, to match observations, specifying `Treatment` and `Age`. 

{{% codeblock %}}
```R
matched_data <- matchit(Treatment ~ Age, data = data, method = "exact")

# Extract the matched dataset
matched_data <- match.data(matched_data)

```
{{% /codeblock %}}

Calculate the ATT, but now on the matched sample:

{{% codeblock %}}
```R
ATT_matching <- mean(matched_data$Earnings[matched_data$Treatment == 1] - matched_data$Earnings[matched_data$Treatment == 0])

print(ATT_matching)

```
{{% /codeblock %}}

The ATT is 7968.828, suggesting a positive effect of the traineeship programme.

## OLS as a matching estimator

Using Ordinary Least Squares (OLS) regression as a matching estimator involves regressing the outcome variable ($Y$) on the treatment indicator ($D$), and the covariates ($X$). This allows us to estimate the treatment effect while controlling for the effects of other variables. 

To understand how the treatment effect depends on observable characteristics $X$, we can include interaction terms between $D$ and $X$ in the regression model.

{{<katex>}}
Y = \beta_0 + \beta_1 D + \beta_2 * X + \beta_3 (D * X) + \epsilon_i
{{</katex>}}

Where
- $Y$ is the outcome variable
- $D$ is the treatment indicator: 1 for treated, 0 for control
- $X$ is a vector of covariates
- $(D * X)$ is the interaction effect between the treatment and covariate(s) *X*.

### Effect coding

One approach to include these interaction terms is through effect coding. This involves coding categorical variables such that the coefficients represent deviations from the overall mean, allowing us to interpret them more easily. It can help understand how the treatment effect varies across different levels of X.

Using the data from before as an example, the regression equation with interaction terms included would look like this:

{{<katex>}}
Y = \beta_0 + \beta_1 D + \beta_2 * X + \beta_3 D * (X_i - \bar{X}) + \epsilon_i
{{</katex>}}

where D * ($X_i - \bar{X}$) is the interaction between the treatment indicator D and the de-meaned covariate $X_{i} - \bar{X}$. It captures how the treatment effect varies with deviations of the covariate $X$ from its mean value ($\bar{X}$). 

Specifically, \beta_3 measures the dependence of the treatment effect on $X_i$; it indicates the additional effect of the treatment for each unit change in the covariate(s), compared to the average treatment effect. 

The ATT is now estimated as
<br>
{{<katex>}}
\hat{\beta}_2 + \frac{1}{N_1} \sum_{i=1}^{N_1} D_i \cdot (X_i - \bar{X})' \hat{\beta}_3
{{</katex>}}


In R, the following code creates a de-meaned variable for `Age` and runs the OLS regression with an interaction term between `Treatment` and `Age_demeaned`. 

{{% codeblock %}}
```R
# Create a de-meaned covariate
data$Age_demeaned = data$Age - mean(data$Age)

# OLS regression with interaction term
ols_model <- lm(Earnings ~ Treatment * Age_demeaned, data = data)

summary(ols_model)

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summary_matching.png" width="400">
</p>

The coefficient for treatment is 351.4, indicating a positive but statistically insignificant effect of the programme on earnings. 

The estimate for the interaction term measures the dependence of the treatment effect on covariate `Age`. While insignificant, the negative sign of indicates the effect of the programme on earnings is reduced for individuals with an age that is further away from the mean. 

{{% tip %}}

For full interpretation of the summary output of the regression model, refer to [this topic](/regressionoutput). 

{{% /tip %}}


{{% summary %}}

{{% /summary %}}






Approximate and propensity score matching

# Overview





## Practical example

Imbens (2015) gives three practical examples.


table

