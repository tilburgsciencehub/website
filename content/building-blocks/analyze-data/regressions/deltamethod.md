---
title: "Doing Calculations with Regression Coefficients Using deltaMethod"
description: "How to calculate the combined effects of regression coefficients using the deltaMethod package"
keywords: "regression, coefficients, calculations, deltaMethod"
date: 2023-06-05
weight: 5
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /calculate/effects
  - /regression/analysis
  - /deltaMethod/package
---

## Overview 

Having the regression coefficients might not be enough if we want to interpret some combined effects between them. Merely summing the coefficients does not ensure that the resulting effect is significant and it also does not offer any information on the resulting standard error. 

To obtain the combined effects of coefficients we can use the `deltaMethod` function of the R `car` package. To illustrate it we use the "Boston Housing" dataset available in the `MASS` package of R. 

## Implementation

Let's first load the dataset and required packages. 


{{% codeblock %}}

```R
#load libraries
library(MASS)
library(car)

#load dataset
data(Boston)

#dataset description
?Boston
```
{{% /codeblock %}}

Next, we perform a simple linear regression analysis. We regress the `medv` variable, which is the median value of owner-occupied homes in $1000s, on all other variables.

{{% codeblock %}}

```R
#linear model
reg <- lm(medv~., data = Boston)
summary(reg)
```
{{% /codeblock %}}

_Output:_
<p align = "center">
<img src = "../images/deltamethod.png" width=350">
<figcaption> Regression output </figcaption>
</p>

Now let's calculate the combined effect of the lower status of the population (`lstat`) with the crime rate per capita (`crim`). The `deltaMethod` function takes as first argument the regression object, followed by the names of the coefficients between quotes:  

{{% codeblock %}}

```R
deltaMethod(reg, 'crim+lstat')
```
{{% /codeblock %}}

_Output:_
<p align = "center">
<img src = "../images/deltamethod1.png" width=350">
<figcaption> deltaMethod output </figcaption>
</p>

We see that the combined effect of the two coefficients is -0.632, with a standard error of 0.056 and a 95% confidence interval between -0.742 and -0.522, denoting that the resulting coefficient is significant at a 5% level.

Alternatively, we can calculate the effect between the intercept and the weighted mean of distances to five Boston employment centers (`dis`).

{{% codeblock %}}

```R
deltaMethod(reg, '(Intercept)+dis')
```
{{% /codeblock %}}

_Output:_
<p align = "center">
<img src = "../images/deltamethod2.png" width=350">
<figcaption> deltaMethod output </figcaption>
</p>

The output shows that the combined coefficient is 34.983, but with a high standard error of 5.035.

## See also
[deltaMethod documentation](https://www.rdocumentation.org/packages/car/versions/3.1-2/topics/deltaMethod)