---
title: "Models analysing panel data: pooled OLS"
description: "A building block about models used to analyze panel data, starting with pooled OLS"
keywords: "paneldata, panel, data, R, regression, model, random, fixed, pooled, OLS, within, between"
draft: false
weight: 10
author: "Valerie Vossen"
authorlink: "https://nl.linkedin.com/in/valerie-vossen"
aliases:
  - /fixedeffects
  - /run/fixedeffects/
  - /run/fixedeffects
  - /fixedeffectsmodels
  - /pooledOLS
  - /run/pooledOLS
---

# Overview

The next building blocks will explain various models commonly used to analyze panel data. Panel data refers to a type of data set that contains observations on multiple entities (such as individuals, firms, or countries) over a specified period of time. By combining cross-sectional and time-series variations, it is very useful in causal inference analysis. For a refresher on panel data, please refer to the [panel data building block]().

Each of these models have their own strengths and assumptions and the choice of an appropriate model depends on the specific research question and the underlying assumptions that hold for the panel data set at hand. This series of building blocks aims to provide guidance in choosing the most suitable model for your analysis!

The following models will be discussed: 
- Pooled OLS
- Within estimator (Fixed effects)
- Between estimator
- Random effects

To illustrate the models with a practical example, we apply them to the analysis on `Grunfeld` data from the [panel data]() building block.  The analysis is about exploring the relationship between market value (`value`) and gross investment (`invest`) of firms. This is the derived model:

{{<katex>}}
invest_{it} = \beta_0 + \beta_1 value_{it} + \beta_2 capital_{it} + \alpha_i + \epsilon_{it}
{{</katex>}}

where,
- $invest_{it}$ is the gross investment of firm `i` in year `t`
- $value_{it}$ is the market value of assets of firm `i` in year `t`
- $capital_{it}$ is the stock value of plant and equipment of firm `i` in year `t`
- $\alpha_i$ is the fixed effect for firm `i`
- $\epsilon_{it}$ is the error term, which includes all other unobserved factors that affect investment but are not accounted for by the independent variables or the fixed effects.

## Pooled OLS Model

The Pooled OLS model applies the Ordinary Least Squares (OLS) methodology to panel data. This model assumes that there are no unobservable entity-specific effects, meaning that all entities in the data set are considered to have the same underlying characteristics. Consequently, $\alpha_i$ is assumed to be constant across individuals and there is no dependence within individual groups (firms). 

The model can be represented as follows:

{{<katex>}}
invest_{it} = \beta_0 + \beta_1 value_{it} + \beta_2 capital_{it} + \epsilon_{it}
{{</katex>}}

The model *pools* observations together from different time periods, ignoring they belong to specific groups (firms). As a result, all observations are treated as if they come from a single group, effectively combining the panel data into a cross-sectional data set. The model coefficients can then be estimated using OLS. 

## Estimation in R
The `plm` function in R is specifically designed for panel data analysis. To estimate a Pooled OLS model using the `plm` function, specify the model type as "pooling" within the function. 

The `index` argument specifies the index variables that define the panel structure of your data. Including this is not strictly necessary when the data is already in a default panel data format and the `plm` function will automatically detect the first column as the entity index and the second column as time index. 

{{% codeblock %}}
```R
model <- plm(invest ~ value + capital, 
              data = Grunfeld, 
              index = c("firm", "year"), 
              model = "pooling")

summary(model)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summarypooledols.png" width="700">
</p>

Since the Pooled OLS model effectively treats the panel data as cross-sectional data by ignoring entity-specific effects, you can also use the function `lm` and obtain the same results.

{{% codeblock %}}
```R
model <- lm(invest ~ value + capital, 
              data = Grunfeld)
summary(model)
```
{{% /codeblock %}}

{{% summary %}}
Pooled OLS is the simplest model to estimate and interpret. However, be careful using it. Panel data without entity-specific effects is very unlikely and the assumption of independence within groups is unrealistic in many cases. 

Using pooled OLS in the presence of unobserved entity-specific factors can lead to omitted variable bias and produce biased results. 
{{% /summary %}}