---
title: "Fixed Effects Models: Within estimator"
description: "A building block about the FE model (Within estimator)"
keywords: "paneldata, panel, data, R, regression, model, random, fixed, pooled, OLS, within, between"
draft: false
weight: 11
author: "Valerie Vossen"
authorlink: "https://nl.linkedin.com/in/valerie-vossen"
aliases:
  - /fixedeffects
  - /run/fixedeffects/
  - /run/fixedeffects
  - /fixedeffectsmodels
  - /withinestimator
  - /within
  - /run/withinestimator
---

# Overview

The fixed effects (FE) model, also known as the "Within estimator", captures changes *within groups*. This model is useful when there are unobserved entity-specific fixed effects in your analysis, due to the heterogeneity across groups. By focusing on within-group variations, the FE model controls for these unobserved effects. 

Examples of unobserved entity-specific fixed effects in our model include factors like managerial quality, level of risk aversion, or technological advancements within firms. 

Standard OLS regression fails to account for these unobserved effects, leading to an omitted variable bias. This bias arises when relevant independent variables are excluded from the regression. Hence, it is crucial to control for these unobserved effects to obtain reliable estimates!

{{% warning %}}
Note that a FE model cannot examine the influence of time-invariant variables on the dependent variable, as these variables are already captured in the fixed effects. 

Also, a FE model may not work well with variables that change little over time due to the issue of collinearity.
Collinearity occurs when independent variables are highly correlated, and when a variable changes very little over time, it becomes highly correlated with the fixed effects in the model. This high collinearity makes it hard to disentangle individual effects of this variable on the dependent variable, potentially leading to unreliable estimates. 
{{% /warning %}}

## Estimation in R
While the `plm()` function can also be used to estimate a FE model, we recommend using the `fixest` package. Refer to the [`fixest` building block]() for a comprehensive explanation of this package and its functions. 

To estimate a FE model using `fixest`, use the `feols()` function and specify the fixed effects variable (`firm`) within the model formula. 

{{% codeblock %}}
```R
# Load packages & data
library(fixest)
library(AER) 
data(Grunfeld) 

# Model estimation
model_within <- feols(inv ~ value + capital | firm, 
                      data = Grunfeld)
summary(model_within)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summarywithin.png" width="700">
</p>

## Time fixed effects

Including time fixed effects controls for time trends that are constant across all groups in the panel data and potentially influence the dependent variable. In our analysis with the `Grunfeld` data set, examples of time trends could be economic cycles, policy changes or market trends impacting firms' investment decisions. 

The model that incorporates both entity-specific and time fixed effects is called a **Two-way Fixed Effects model**. This model is very commonly used in causal inference analysis. 

To include time fixed effects in your model in R, add the variable `year` to the fixed effects specification:

{{% codeblock %}}
```R
model_twoway <- feols(inv ~ value + capital | firm + year, 
                      data = Grunfeld)
summary(model_twoway)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summarytwoway.png" width="700">
</p>

## The Least Square Dummy Variable (LSDV) model
Another approach to estimate fixed effects is the *Least Square Dummy Variable* model. In this model, dummy variables are added for each entity and/or time period to capture the fixed effects. In R, the LSDV model can be implemented using the `lm()` function and creating dummy variables for the entities and/or time periods. 

However, it is important to note that the LSDV approach is not practical for larger panel data sets. When there are many observations (entities and/or time periods), creating dummy variables for each of them can result in a substantial number of variables, leading to computational challenges. Therefore, when dealing with larger data sets, the FE model is preferred as it is a more efficient approach to control for unobserved fixed effects.

{{% summary %}}
The FE model, also known as the Within estimator allows us to estimate changes within groups and control for unobserved entity-specific fixed effects. Additionally, the inclusion of time fixed effects accounts for common time trends in the data across groups. The resulting model with both types of fixed effects is called a **Two-way fixed effects model** and is a widely used approach in causal inference analysis.

In R, the `fixest` package, specifically the `feols()` function, can be used to estimate the FE model.
{{% /summary %}}