---
title: "Fixed Effects Models: Between estimator"
description: "A building block about the Between estimator"
keywords: "paneldata, panel, data, R, regression, model, random, fixed, pooled, OLS, within, between"
draft: false
weight: 13
author: "Valerie Vossen"
authorlink: "https://nl.linkedin.com/in/valerie-vossen"
aliases:
  - /fixedeffects
  - /run/fixedeffects/
  - /run/fixedeffects
  - /fixedeffectsmodels
  - /betweenestimator
  - /between
  - /run/betweenestimator
---

# Overview

The **Between estimator** is a method used to estimate the relationship between variables by taking averages across time for each entity. It uses only the *between-group variation* in the data by averaging out the time component of panel data. 

This results in a pooled cross-sectional data set. Consequently, important information about how variables change over time is ignored.

## Estimation of the Between estimator 
The Between estimator is obtained by regressing the averaged variables on each other using OLS regression.

It is important to note that that the error term should be uncorrelated with any of the averaged independent variables, for the estimated coefficients to be unbiased. And if the error term is assumed to be uncorrelated with the independent variables,the [Random Effects model]() is generally more appropriate. 

Nonetheless, the Between estimator can be suitable for research question that specifically address variation between different entities rather than changes within entities over time. 

## Estimation in R
To estimate the Between estimator in R, you can use the `plm()` function from the `plm` package. Specify the model type as "between". 

{{% codeblock %}}
```R
# Load packages & data
library(plm)
library(AER) 
data(Grunfeld) 

# Estimate Between estimator
model_between <- plm(inv ~ value + capital, 
                      data = Grunfeld,
                      model = "between")
```
{{% /codeblock %}}

{{% summary %}}
The Between estimator uses averaged variables across time to estimate the relationship between variables. By averaging out the time component of panel data, it effectively transforms the panel data into a pooled-cross sectional data set. This approach thus ignores information about how variables change over time. 

To obtain unbiased estimates, it is crucial to ensure the assumption of zero correlation between the error term and averaged independent variables holds. 
{{% /summary %}}
