---
title: "Regression Analysis"
description: "Build linear models to draw inferences from your datasets"
keywords: "linear regression, model, regression, prediction, model evaluation, linear inferences"
weight: 1
date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /regression-analysis
---

## Overview
XXX


## Code

### Estimate Model
Linear regression (`lm`) is suitable for a response variable that is numeric. For logical values (e.g., did a customer churn: yes/no), you can estimate a logistic regression model (`glm`). The code sample below estimates a model, checks the model assumptions, and shows the regression coefficients.

* Model transformations can be incorporated into the formula, for example: `formula = log(y) ~ I(x^2)`.
* The coefficients (`coefficients(mdl)`), predictions for the original data set (`fitted(mdl)`), and residuals (`residuals(mdl)`) can be directly derived from the model object.
* A concrete example on how to evaluate model assumptions (mean residuals is 0, residuals are normally distributed, homskedascticiy) can be found [here](). 

{{% codeblock %}}
```R
library(broom)

# estimate linear regression model 
# to estimate a logistic regression model use:
# glm(formula = y ~ x, data = data, family = binomial)
mdl <- lm(formula = y ~ x, data = data)

# check model assumptions
autoplot(
  mdl,
  which = 1:3,
  nrow = 1,
  ncol = 3
)

# show regression coefficients
summary(mdl)
```
{{% /codeblock %}}

### Identify Outliers
Compute the leverage of your data records and influence on `mdl` to identify potential outliers.

{{% codeblock %}}
```R
library(dplyr)
leverage_influence <- mdl %>%
    augment() %>%
    select(y, x, leverage = .hat, cooks_dist = .cooksd) %>%
    arrange(desc(cooks_dist)) %>%
```
{{% /codeblock %}}

### Plot Trend Line
Plot a scatter plot of two numeric variables and add a linear trend line on top of it.

{{% codeblock %}}
```R
library(ggplot2)

ggplot(data = data, aes(x, y)) + 
geom_points() + 
geom_smooth(method = "lm", se = FALSE)

```
{{% /codeblock %}}


### Make predictions
Given a linear regression model (`mdl`), make predictions for unseen input data (`explanatory_data`). Note that for multiple linear regression models, you need to pass an `explanatory_data` object with multiple columns.

{{% codeblock %}}
```R
explanatory_data <- c(..., ..., ...)

prediction_data <- explanatory_data %>% 
  mutate(   
    y = predict(
      mdl, 
      explanatory_data, 
      type = "response"
    )
  )

# See the result
prediction_data
```
{{% /codeblock %}}




## Example

The [Shiny app](https://royklaassebos.shinyapps.io/dPrep_Demo_Google_Mobility/) below  visualizes Google’s COVID-19 Community Mobility Reports of the Netherlands. A step-by-step tutorial (incl. source code) can be found [here](https://dprep.hannesdatta.com/docs/building-blocks/deployment-reporting/).

![](../images/demo_app.png)

## See Also
* [Interactive Web Apps with shiny Cheat Sheet](https://shiny.rstudio.com/images/shiny-cheatsheet.pdf)
* [Shiny User Showcase](https://shiny.rstudio.com/gallery/)