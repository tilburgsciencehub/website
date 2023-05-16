---
title: "Intro to IV Estimation"
description: "This is an intro to IV estimation"
keywords: "iv, causal inference, difference-in-difference, DID, R, regression, model, iv, instrumental variable "
draft: false
weight: 5
author: "Aakriti Gupta"
authorlink: ""
aliases:
  - /iv
---

---


## Overview

An instrumental variable is used in regression analysis when independent variable(s) are influenced by other independent variable(s) in the model. The existence of these endogenous variables violates the assumption of 'No perfect collinearity' which states that there is no linear relationship among the independent variables.

 In addition to this the IV regression also controls for threats to internal validity, such as confounding variables, measurement error, omitted variable bias (spuriousness), simultaneity, and reverse causality.

In this building block we will walk you through the process of using instrumental variables in your regression by introducing the `ivreg()` function from the `AER` package and also discuss which variables are considered to be valid instruments.

We analyse data from the`mroz` data set which is an in-built data set in R, provided by the `wooldridge` package. We are interested in examining how the education level of employees relates to their wages. Our simple regression model will be as follows:

{{<katex>}}
wage_{i}  =  \beta_{0} + \beta_{1} educ_{i} + \mu
{{</katex>}}

<br>
<br>
where,

| **Variable** | **Description**            |
| :------  | :---------             |
| `wage`     | earnings per hour      |
| `educ`     | years of schooling    |


## Loading the data

{{% codeblock %}}

```R
install.packages("wooldridge")
install.packages("AER")
library(wooldridge)
library(AER)
data(mroz)
```
{{% /codeblock %}}

## Estimating the simple regression model

{{% codeblock %}}
```R

ols <- lm(data=mroz, wage~educ) 
summary(ols)
```
{{% /codeblock %}}

This regression, however, is under-specified because some variables such as `fatheduc` (father's years of schooling) which can be relevant in our model, has been excluded, leading to an omitted variable bias. But, `fatheduc` can also not be added as a second independent variable because it influences the variable `educ` as is supported by the regression result below:

{{% codeblock %}}
```R
reg <- lm(data=mroz, educ~fatheduc)
summary(reg)
```
{{% /codeblock %}}

Thus, a possible solution is to use `fatheduc` as an instrument for `educ`.

## IV regression
A valid instrument, Z is one that fulfills the following 2 conditions:

1)It is correlated with the independent variable, X i.e. it is relevant.

2)It is not correlated with the error term, $\mu$ i.e. it is exogenous.

In other words, Z should affect the outcome variable, Y, only through X to be considered as a valid instrument.

Now in our model, we have seen in the previous section that `fatheduc` is indeed correlated with `educ` and hence satisfies the condition for instrument relevance. Instrument exogeneity, however, cannot be tested and needs to be justified from theory or common sense.  

Therefore, including `fatheduc` as an instrument variable in a 2-Stage Least Squares (2SLS) analysis of the relationship between `wage` and `educ` can address the endogeneity issue and produce unbiased estimates.

Let's estimate this IV regression.

First stage regression:


{{<katex>}}

educ_{i} = \gamma_{0} + \gamma_{1} fatheduc_{i} + \mu
{{</katex>}}
<br>

Second stage regression:


{{<katex>}}

wage_{i} = \beta_{0} + \beta_{1} \hat{educ_{i}} + \epsilon
{{</katex>}}  
<br>

Now let's try to run this regression. To do so, we use the `ivreg()` function which is offered by the `AER` package. It works similar to the `lm()` function but includes an additional argument for the instrument, separated from the regression equation by a vertical line, `|`.

{{% codeblock %}}
```R
iv <- ivreg(data=mroz, wage~educ|fatheduc)
summary(iv)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/ivreg.png" width="400">
<figcaption> Estimation results using ivreg()</figcaption>
</p>

## Test for instrument strength
Although `fatheduc` is a valid instrument, it could still not be a very strong one. This could be because it is not that significantly correlated with the independent variable.

To check the strength of the instrument in your model, you can use the `diagnostics = TRUE` argument in the `summary()` function as follows:
{{% codeblock %}}
```R
summary(iv, diagnostics = TRUE)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/iv_diagnostic.png" width="400">
<figcaption> Test for instrument strength</figcaption>
</p>


This gives you information about 3 tests:

1)Weak instrument:

A good instrumental variable is highly correlated with one or more of the explanatory variables while remaining uncorrelated with the errors. If an endogenous regressor is only weakly related to the instrumental variables, then its coefficient will be estimated imprecisely. We hope for a large test statistic and small p-value in the diagnostic test for weak instruments, as is the case in our example.

2)Wu-Hausman:

Applied to 2SLS regression, the Wu–Hausman test is a test of endogeneity. If all of the regressors are exogenous, then both the OLS and 2SLS estimators are consistent, and the OLS estimator is more efficient, but if one or more regressors are endogenous, then the OLS estimator is inconsistent. Again, we need a large test statistic and a small p-value for the OLS estimator is inconsistent. However, it is not true in our example and the 2SLS estimator is therefore not to be preferred.

3)Sargan:

 The Sargan test is a test of overidentification. That is, in an overidentified regression equation, where there are more instrumental variables than coefficients to estimate it is possible that the instrumental variables provide conflicting information about the values of the coefficients. A large test statistic and small p-value for the Sargan test suggest, therefore, that the model is misspecified.
 We obtain NA values for this test as it is inapplicable with an equal number of instrumental variables and coefficients.
