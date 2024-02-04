---
title: "Understand the Summary Statistics of Regression Output in R"
description: "Learn how to interpret the summary output of a linear regression model, e.g. coefficients, standard error, significance, R-squared etcetera."
keywords: "R, regression, interpretation, output, model, summary, linear, analysis, interpret, analyze"
draft: false 
weight: 7
author: "Valerie Vossen"
aliases:
  - /regressionoutput
  - /summary
---


# Overview

Regression analysis is a powerful tool to estimate relationships between variables. It is a way to quantify the impact of one variable on the other and make predictions for unseen data. [Check out this topic](/analyze/regression) for the basics of regression output, In this topic, we discuss the summary of a regression in R, i.e. all the components of a regression output. We provide step-by-step explanations with suggestions on how to interpret and present the results.

## Load packages and data

We will start by loading the necessary packages and our sample dataset. The dataset we'll use is manipulated before and contains data on immigration and unemployment rates in regions in the Netherlands. 

We investigate the relationship between 

{{% codeblock %}}

```R
library(readr)
data <- read.csv".csv")
```
{{% /codeblock %}}

Load the dataset yourself by copying the code into your Rscript. A preview of the dataset given by head() returns the first 5 rows.

{{% codeblock %}}

```R
# Preview the first few rows of the dataset
head(data)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/.png" width="400">
</p>

## Simple linear regression output

The simple linear regression is used to understand the relationship between the linear independent and dependent variable.

For interpreation of other different functional forms (e.g. one of the two variables is in log), or multivariate regression where more than one independent variable is added, check out [this topic on interpreting regressions of different functional forms](/regressioninterpretation). 
 
The function `lm()` is used for running a regression of X on Y, of the following model: `Y = a + bX`, where X is the independent and Y is the independent variable. a is the intercept and b is the coefficient that predicts the relationship between X and Y. 


{{% codeblock %}}

```R

# simple linear regression
regression <- lm(Y ~ X, data = data)

# summary of the regression model
summary(model)

```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/summary_output.png" width="400">
</p>

Now we walk through the output step by step:

## Call

<p align = "center">
<img src = "../images/call.png" width="400">
</p>

The call section shows the formula used for the regression analysis, indicating the dependent variable, independent variable, and dataset.

## Residuals

Residuals represent the difference between the observed and the predicted values of the dependent variable. 

The summary output provides:
- `Min`: The minimum residual value
- `1Q`: The first quartile, the value below which 25% of the residuals lie.
- `Median`: The median, the midpoint of the residual values, separating the lower 50% from the upper 50%.
- `3Q`: The third quartile, the value below which 75% of the residuals lie.
- `Max`: The maximum residual value

For a linear regression model to be unbiased, the residuals should be evenly distributed around zero, indicating that the model is equally likely to overestimate or underestimate the dependent variable's value.

While the summary output can provide an initial overview of the residuals, it is typically not the primary tool for directly assessing the assumption on residuals. [This topic](/analyze/regression/model-assumptions) elaborates on model assumptions and shows how you can plot model residuals to evaluate the assumption. 

## Coefficients

The coefficients section is probably the most familiar and important part of the summary regression output. It provides information about the estimated relationships between the independent and dependent variables in the model. 

### Estimate


The estimate column displays the coefficients for each predictor in the model. These coefficients represent the expected change in the dependent variable (Y) for a one-unit change in the predictor variable (X), holding all other variables constant.

- Intercept term

<p align = "center">
<img src = "../images/intercept.png" width="400">
</p>

The first estimate is of the intercept term.
It represents the predicted value of the dependent variable when all predictor variables are set to zero. 

{{% warning %}}
Note that interpretation of the intercept may not be meaningful if the independent variable(s) cannot realistically take on a value of zero in the dataset.
{{% /warning %}}

- Independent variables: 

<p align = "center">
<img src = "../images/estimates.png" width="400">
</p>

The estimates for the independent variables indicate the predicted effect of each predictor variable on the dependent variable. In our example, a one-unit increase in X is associated with ... increase in Y, all else being equal. For interpretation of this and other functional forms, check [this topic](/regressioninterpretation).


- The standard error

<p align = "center">
<img src = "../images/standarderror.png" width="400">
</p>


The standard error provides an estimate of the uncertainty associated with the coefficient estimates. In simple terms, it tells us how much we would expect the coefficient estimate to vary if we were to take multiple samples from the population. 


You can use the standard error to create confidence intervals, which help to quantify the uncertainty in our estimates and provide a range of plausible vlaues for the true population parameter


{{% tip %}}

Confidence intervals (CI) are a range of values constructed around the point estimate (such as the coefficient estimate) that are likely to contain the true population parameter with a certain level of confidence (e.g., 95%). In other words, it gives the range of most likely values of the coefficient. 
say you re-estimate the model, the range of values of coefficients that you will find in 95% of the cases is the CI. 


Reporting the 95% CI around the estimated effect is useful. Even when the estimate is significant, the uncertainty is still there. A CI shows this uncertainty. 

For large samples: β + - 1.96 SE(β) 

{{% /tip %}}


- t value

The t-value is the coefficient estimate divided by the standard error.

Essentially, a large t value indicates that our standard error is small relative to the size of the coefficient. The larger the t statistic, the more certain we are that the coefficient is not zero. 


- Pr(>|t|): p-value

The p-value of each estimate indicates the probability of observing a t-value as extreme as, or more extreme than, the one calculated from our sample data, assuming that the null hypothesis is true (i.e., the true population coefficient is zero).

In other words, the p-value represents the probability of finding an effect, when there is no effect. 

In practice, a small p-value indicates that the observed relationship between the predictor variable (X) and the dependent variable (Y) is unlikely to be due to random chance alone. Instead, it suggests that there is strong evidence supporting a true association between the predictor and the outcome.


When the p-value is sufficiently small, typically set to be lower than 0.05, the coefficient estimate is statistically significant (at a 5% level).


#### Two-sided test

Test whether there is a significant positive or negative effect of the predictor value on the outcome varialbe. 

For example, our regression coefficient of ... with a p-value of ...:

If X has no effect on Y, then there is a .. percent chance of obtaining the result that X leads to a 1.24 higher grade and a 1.24 lower grade. 


## significance

Interpretation of a stat. insignificant coefficient (P>0.05)

Non-significance does not imply absence of effect: A p-value greater than 0.05 does not necessarily mean that there is no effect of the predictor variable on the outcome. Instead, it indicates that the evidence against the null hypothesis (i.e., the absence of an effect) is not strong enough to reject it.

Report non-significant results by saying you don't find evidence for a relatipnship fo X and Y, not that there is no relationship. 



Tip

Also think about the magnitude of estimated effect. say you found a statistically significant effect between X and Y, it is important to think about how large this effect is. This is not just calculation, but requires your own judgement based on literature. 

A way how to do it is to put it in %; in linear models, the coefficient divided by the baseline mean of the outcome variable * 100%. 


tip




## Other information


- Residual standard error

How well the model fits the data
The average amount that the actual values of Y differ from the predictions in units of Y. With a smaller residual standard error, the model's prediction line is very close to the actual values, on average.


- Multiple and Adjusted R-squared

What percentage of variation is within our dependent variable is explained by the independent variable(s). 
With a R-squared of ..., ..% is explained.

The adjusted R-squared ...

A low R-squared does not necessarily mean that your model is bad and the other way around, so be careful drawing conclusions from this.

- F-statistic and p-value

Null hypothesis: no relationship betewen dependent and independent variable. Alternative hypothesis: there is a relationship. The F-statistic and p-value helps us determine the result of this test. However, better use the p-value to determine this. F-stat can be misleading. 

summary

How to present your result

Don't just say you find a statistically significant effect of the independent on the dependent variable. 

Important to understand your whole output with concluding anything on the relationship between the independent and dependent variable in your estimated model.
