---
title: "Evaluate Model Assumptions of an OLS Regression in R"
description: "Check the validity of the OLS assumptions"
keywords: "linear regression, model, lm, prediction, model evaluation, linear inferences, assumptions"
weight: 1
draft: false
aliases:
  - /analyze/regression/model-assumptions
  - /run/model-assumptions
  - /model-assumptions
---

## Overview

The first step before estimating an OLS regression is to validate the model assumptions to ensure the estimates are reliable and the inference drawn is valid.

To illustrate how to check for model assumptions with an example, we use the built-in `cars` dataset which includes 50 data points of a car’s stop distance at a given speed. Since the dimensions are shown in miles per hour and foot, we first convert them into kilometers per hour and meters, respectively. Then, we estimate a linear model and evaluate its properties with the `autoplot` function from the `broom` package.

## Example code

{{% codeblock %}}
```R
library(ggplot2)
library(ggfortify)
library(broom)
library(dplyr)

data(cars) # import built-in car dataset
cars$speed_kmh <- cars$speed * 1.60934  # convert miles per hour to kilometer per hour
cars$dist_m <- cars$dist * 0.3048  # convert foot to meters

# estimate linear model
mdl_cars <- lm(dist_m ~ speed_kmh, data=cars)

# check linear model assumptions
autoplot(
  mdl_cars,
  which = 1:3,
  nrow = 1,
  ncol = 3
)
```
{{% /codeblock %}}


### Outputs

<p align = "center">
<img src = "../images/residual-fitted.png" width="400">
</p> 


- *Residuals vs Fitted*: Residuals indicate the difference between the predicted and the actual value. The residuals vs fitted plot shows the residuals and the data points should center around the horizontal axis (i.e., the mean of the residuals is 0). The equally spread residuals around the horizontal line without distinct patterns are a good indication of having linear relationships. Although the line goes slightly downward around the middle, it does not look worrisome at first sight. The linearity assumption seems to hold reasonably well.


<p align = "center">
<img src = "../images/normal-qq.png" width="400">
</p> 

- *Normal Q-Q*: Another requirement is that the residuals are approximately normally distributed. This means that if you plot the distribution of all residuals it would look like a bell-shaped distribution (also known as Gaussian distribution). This is the case if the data points in the QQ-Plot are close to the diagonal. Here, we find that record 23, 35, and 49 are somewhat higher than expected (the right tail).


<p align = "center">
<img src = "../images/scale-location.png" width="400">
</p> 



- *Scale-Location*: Finally, the scale-location plot shows the standardized residuals for all fitted values. The homoskedasticity assumption states that the error term should be the same across all values of the independent variables. Hence, we should check here if there is any pattern that stands out. In our case, this happens to be the case as the blue line stays rather flat. It would, however, be troublesome if the error value increases for higher speed values(i.e. if there is a “fanning out” pattern).
