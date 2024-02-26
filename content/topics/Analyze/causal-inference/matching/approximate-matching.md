---
title: "Propensity Score Matching"
description: "Matching is used to create comparable groups in observational studies, helping to mitigate the effects of confounding variables and estimate causal effects."
keywords: "matching, propensity, score, causal, inference, effect,regression, R, exact, approximate"
draft: false
weight: 2
author: "Valerie Vossen"
aliases:
  - /approximate-matching
  - /propensity-score-matching
---

# Overview

[The previous topic](/matching) introduced matching and specifically focused on exact matching, where individuals are paired on an identical characteristic. Here, we will go further with approximate matching, where pairs are made on similar but not identical characteristics. Then we will continue with an example on Propensity score matching.

It is again a way to adjust for differences when treatment is non-random. Important is that this method is only relevant for selection on observables, which means you should be able to identify the confounders (and have data on them!) that are biasing the causal effect you are trying to find. 


## Curse of dimensionality

[Exact matching](/matching) requires an untreated unit with the precise similar value on each the observed characteristics to be a good counterfactual for the treated units. This is only possible with lots of data and few covariates to match on. 

The curse of dimensionality means that, when there is a large number of variables you are matching treated and untreated units, or when some variables are continuous, there might be no appropriate counterfactual left (that has all the same values on all these covariates). This can be an issue in finite samples. 

Approximate matching offers a solution; it reduces the dimensionality by defining a distance metric on characteristic X an then matching using the distance rather than the value of X. As the sample get larger, approximate matching method results will all tend towards exact matching. 

## Methods

Other methods; sources 

- Nearest-neighbour matching: Each treated units is matched next to the "nearest" untreated unit. 

- Kernel matching: counterfactual calculated by taking the local averages of the control group unit near each treated unit. 

## Propensity score matching

Propensity score matching is one of the methods to generate inexact matches, and deal with the curse of dimensionality. 

It generates a "propensity score", which is the probability of being assigned to the treament group, conditional  on the particular covariates $X$: $P(X_i)$. 


By controlling for the propensity score, the selection bias is then eliminated. You compare units who, based solely on their observables, had similar probabilities of getting the treatment. 


This makes it possible to compare them, and the remaining variation in the outcome variable can then be assigned as being due to the treatment only.

### Propensity score calculation

Parametric model, such as logit or probit. Important to adopt a flexible specification for the parametric propensity score in practice and select that specification via balancing tests. 


1. Estimate propensity score

Prob(D=1 | X) = gamma*X + w


Using estimated coefficients, calculate;

rho bar _ i = gamma * X_bar_i

Propensity score is just the predicted conditional probability of treatment for each units. 


Then sort your data by the propensity score and divide into blocks (groups) of observations with similar propensity scores.

Within each block, test (using a t-test), whether the means of the covariates are equal in the treatment and control group. Good if yes!

If a particular block has one or more unbalanced covariates, divide into finer blocks and test again. If a particular covariate is unbalanced for multiple blocks, modify initial equation by including higher order terms and/or interaction with that covariate and test again.


2. Effect of treatment on outcome

- stratifying on the propenvity score: regression within each block. Calculate weighted mean of the within-block estimates to get the average treatment effect.

- Matching on propensity score: match each treatment observation with one or more control observations, based on similar propensity scores. Include dummy for each matched group which controls for everything that is common within that group.

warning
The	propensity	score	approac h doesn’t correct	for	
unobservable	variables	that	affect	whether	observations
receive	treatment.
warning



Tradeoff of which matching method to choose depends on your own data.



# Practical example

## setting
We will give an example of matching using the second example of [Imbens (2015)](). Context on our example can be found in part B section 6.2. The authors examine the effect of participation in a job training program on earnings. specifically, it is the Nsw program, which is in place to help disadvantaged workers.

studying this question isn't straightforward, because individuals who enroll in the training program can differ from those who don't. To tackle this challenge, they conduct a field experiment where qualified participants are randomly assigned to training positions. The Lalonde dataset is collected from this field experiment.

However, Imbens (2015) finds evidence of selective attrition in this dataset: individuals are more likely to drop out of the experiment in a manner where the likelihood of dropping out depends on treatment assignment. Hence, we cannot assume treatment holds in our dataset. Nonetheless, we can still utilize the matching estimator instead of the difference-in-means estimator if the rate of attrition remains the same when we control for the observed covariates.

## Load packages and data

You can load the data by copying the following code into R.

{{% codeblock %}}
```R
data_url <- "https://raw.githubusercontent.com/tilburgsciencehub/website/topic/interpret-summary-regression/content/topics/Analyze/causal-inference/matching/nsw_dw.dta"

load(url(data_url)) # is the cleaned data set

```
{{% /codeblock %}}

Load the following packages, and install them first using `install.packages()` if you don't have them yet:

{{% codeblock %}}
```R
library(knitr)
library(haven)
library(MatchIt)
```
{{% /codeblock %}}


## Difference-in-means estimate

The outcome variable is the income of participant $i$ in 1978 (`re78`). The treatment variable is a binary variable that denotes 1 if the participant took part in the training program and 0 if not (`treat`).

First, we calculate the ATT by using the difference-in-means estimate, without solving the potential bias coming from selective attrition. 

The following R code calculates the mean of `re78` for each treatment group, storing it in a new data frame called `meanre78`. Then, the difference-in-means estimate is calculated by subtracting the mean of the control group of the mean of the treatment group.

{{% codeblock %}}
```R
meanre78 <- aggregate(re78~treat, data=data, FUN=mean)
estimate_diffmean <- meanre78[2,2] - meanre78[1,2]
estimate_diffmean 

```
{{% /codeblock %}}

`1794.342` is returned. Additionally, a two sample t-test compares the `re78` values between the treatment and control group and tests the null hypothesis that the means of the two groups are equal.

{{% codeblock %}}
```R
t.test(data$re78[data$treat==1],
       data$re78[data$treat==0]
       )
```
{{% /codeblock %}}

- screenshot

A p-value lower than 0.05 indicates the means are statistically signicant different from eachother. Thus, interpreting the p-value of `0.007`, individuals who received the treatment have higher average earnings than individuals who did not. The difference-in-means suggest an ATT (*Average Treatment Effect on the Treated)* of approximately `1800`. 

## Balance test

To check whether randomization went right and the treatment and control group are balanced, we compare the observed covariates with a summary statistics table. The covariates of interest which are defined by the `columns_of_interest` list. Then, the mean and standard deviation of each variable are calculated for both treatment and control group, and t-test are conducted to compare these means. The results are extracted and stored in vectors. 

{{% codeblock %}}
```R
# Generate binary variable for unemployment
data$u74 = data$re74<0.0001
data$u75 = data$re75<0.0001

# Defining the covariates (columns) of interest
columns_of_interest = c("black","hispanic","age","married","nodegree","education","re74","re75")

# Calculate means and standard deviations
treatment_means = colMeans(data[data$treat==1,columns_of_interest])
control_means = colMeans(data[data$treat==0,columns_of_interest])
treatment_std = colSd(data[data$treat==1,columns_of_interest])
control_std = colSd(data[data$treat==0,columns_of_interest])

# Perform t-tests and extract results
t_test_results = sapply(columns_of_interest, function(x) {
  t.test(data[[x]][data$treat==1],data[[x]][data$treat==0])$statistic
})

t_test_pvalue = sapply(columns_of_interest, function(x) {
  t.test(data[[x]][data$treat==1],data[[x]][data$treat==0])$p.value
})

# Create summary table
df <- data.frame(
  Covariate = columns_of_interest,
  mean_control = round(control_means, digits = 2),
  sd_control = round(control_std, digits = 2),
  mean_treated = round(treatment_means, digits = 2),
  sd_treated = round(treatment_std, digits = 2),
  t_stat = round(t_test_results, digits = 1),
  p_value = round(t_test_pvalue, digits = 3)
)

kable(df)

```
{{% /codeblock %}}


- screenshot

The summary table above compares the observed characteristics between the treatment and control group. 
The first two columns present results of the control group, the third and fourth the results of the treatment group. 

Significant differences in some characteristics (p-values lower than 0.05) suggest imbalance between the two groups. For example, since people with no degree are more likely to drop out of the treatment group, the amount of people with nodegree differs between treatment and control group. If people with no degree have lower earnings independent of whether they received a program, the treatment effect is likely to be overestimated. 

Matching comes into play now, where we can control for covariates like `nodegree`.

## Calculate the propensity score

To avoid the curse of dimensionality, since we have multiple observed covariates and relatively few observations, propensity score matching is done. 

Calculate the propensity score by estimating a logistic regression with the `glm()` function. The dependent variable is the treatment indicator, the independent variables include the covariates and interaction terms. 

{{% codeblock %}}
```R
# Create interaction terms
data$re74nodegree = data$re74*data$nodegree
data$nodegreeeducation = data$nodegree*data$education
data$u75education = data$education*data$u75

# Run the logistic regression
propreg = glm(treat ~ re74 + u74 + re75 + u75 + nodegree + hispanic + education + nodegreeeducation + re74nodegree + u75education, family = binomial(link = "logit"),data=data)
summary(propreg)

```
{{% /codeblock %}}

- screenshot

This logistic regression model estimates the propensity score, the probability of receiving the treatment given on the observed covariates ($\hat{P}_{\text{X_i}}$).

## Nearest neighbor propensity score matching

We now use the propensity scores to conduct nearest neighbor matching, ensuring balance between treatment and control groups. This helps ensure that the difference in outcomes is due to the treatment rather than pre-existing differences in characteristics.

The `matchit()` function is used, in which the formula for the logistic regression model used to estimate the propensity scores is specified. The method argument specifies the matching method (here, `nearest`). The distance metric used to measure the similarity between individual; the distance is calculated as the log odds ratio of the propensity score. 

{{% codeblock %}}
```R
# Generate the matched data
match_prop <- matchit(treat ~ re74 +u74 + re75 +u75  + nodegree + hispanic + education + nodegreeeducation + re74nodegree + u75education,  method = "nearest",  distance = "glm", link = "logit", data=data )

# Data containing treated observations and their matched equivalence in the control group

data_match_prop <- match.data(match_prop)
```
{{% /codeblock %}}


{{% codeblock %}}
```R
# Estimate the ATT
mean_re78_match_prop <- aggregate(re78~treat,   data=data_match_prop,    FUN=mean)
estimate_matching <- mean_re78_match_prop$re78[2]    -  mean_re78_match_prop$re78[1]
estimate_matching

```
{{% /codeblock %}}

- screenshot 

The difference between income is 1500, which is lower than the estimated ATT before matching. This is in line with our reasoning of underestimating the treatment effect if the treatment group is on average higher educated due to selective attrition. 


## Flexible ols? for exact matching bb?

