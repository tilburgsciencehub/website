---
title: "Testing for Serial Correlation"
description: "Learn how to identify and address serial correlation through visual inspection, statistical tests, and adjustments to standard errors."
keywords: "serial correlation, serial, correlation, autocorrelation, statistical, test, testing, R, OLS, assumptions, standard, error, errors, Durbin-Watson, Breusch-Godfrey, Wooldridge"
draft: false
weight: 1
author: "Valerie Vossen"
aliases:
  - /serial-correlation
  - /autocorrelation
---

## Overview

In time series or [panel data analysis](/paneldata), data covers various time periods, typically years, providing vakyabke insights into changing trends and patterns. However, a common challenge within this framework is serial correlation, also known as autocorrelation. This occurs when the error terms in a regression model are correlated across consecutive time periods in the data. 

{{% example %}}

Consider a regression model equation where $\epsilon_{it}$ represents the error term for each observation (entity `i` in time period `t`):

{{<katex>}}
Y_{it} = \beta_0 + \beta_1 X_{it} + \epsilon_{it}
{{</katex>}}

{{% /example %}}

Adressing serial correlation is crucial as it can affect model outcomes, potentially resulting in misleading standard errors estimated for the OLS coefficients. In this article, we will explore various methods for testing serial correlation in your data using simple R code examples. Additionally, we will discuss potential solutions to mitigate the impact of serial correlation.


## What is serial correlation? 

One of the fundamental Gauss-Markov assumptions for achieving the Best Linear Unbiased Estimators (BLUE) the OLS estimates to be BLUE (*best linear unbiased estimate*) pertains to the error terms. In mathematical terms, it is expressed as:

$Corr(u_t, u_s | X) = 0 $  for all $t ≠ s$

This assumption states that, given the covariates X, errors in different time periods should be uncorrelated. When errors exhibit serial correlation, this assumption is violated.

{{% tip %}}

Serial correlation can appear in either *positive* or *negative* patterns. 

*Positive serial correlation* occurs when an unexpected high (low) value in the dependent variable is followed by similar high (low) values in subsequent periods. Above-average errors in one period are mirrored in the next period, leading to an underestimation of the true uncertainty around the OLS estimates.

Conversely, *negative serial correlation* happens when deviations from the mean in one period are followed by opposite deviations in subsequent periods. This leads to an overestimation of the true uncertainty around the estimates.

{{% /tip %}}


## Example with `Grunfeld` data

Let's explore a regression analysis using the `Grunfeld` dataset in R. Our goal is to evaluate how market value influences firm gross investment. For an introduction to this analysis and the `Grunfeld` data, please refer to the [Panel data topic](/paneldata). The regression model is estimated in R using the `plm()` function from the `plm` package:

{{% codeblock %}}
```R
# Load data and required packages
library(AER)
data(Grunfeld)
library(plm)

# Define and estimate the regression model
model_plm <- plm(invest ~ value + capital, 
           data = Grunfeld, 
           index = c("firm", "year"), 
           model = "within", 
           effect = "twoways")

summary(model_plm)
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/summary-plm.png" width="400">
</p> 

In this data, positive serial correlation would be present if, following an unexpected increase in the interest rate (the dependent variable, `invest`) in one period, it remains above average in the year after, given the levels of market value (`market`) and stock value (`capital`).


## Visually inspecting serial correlation

First, we create an autocorrelation plot to visually inspect whether the data shows serial correlation. The `acf()` function in R automatically computes the serial correlation and produces a plot when `plot = TRUE` is specified. 

{{% codeblock %}}
```R
# Extract error terms from the regression model
e <- model_plm$residuals

# Calculate autocorrelation and generate plot
acf_residuals <- acf(e, 
                    plot = TRUE,
                    main = "Autocorrelation plot" # Set title
                    )
                    
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/autocorrelation-plot.png" width="400">
</p> 

The x-axis represents the *Lag* , indicating the time interval between each observation and its correlated observations. On the y-axis, the autocorrelation coefficients range from -1 to 1, where 0 indicates no correlation. The blue dashed lines around the zero line represent the 95% confidence interval. The plot displays significant positive autocorrelation at lag-1, 2, and 3, with spikes exceeding the 95% confidence interval. Additionally, the decreasing spikes as the lag increases tell us that the observations become less correlated as they are further apart in time. 

{{% tip %}}
You can set the maximum lag for calculating autocorrelation with the `lag.max` argument in the `acf()` function. By default, it is set to one less than the number of observations in the series.
{{% /tip %}}

## Testing for serial correlation in `plm` models

Various tests are available for quantitatively evaluating serial correlation in the error term. However, a drawback of these functions is that they only accept `plm` models as arguments. Consequently, you cannot directly apply them to a model estimated with the `fixest` package. If you are using `fixest` and would rather not re-estimate your model with `plm` first, the next section offers an alternative test approach that doesn't depend on these functions.

### 1. Durbin-Watson test

The Durbin Watson test is a commonly used method to check for first-order serial correlation (correlation from one period to the other). This test assumes strictly exogenous regressors. 

{{% codeblock %}}
```R
# Perform the Durbin-Watson test
pdwtest(model_plm)         
```
{{% /codeblock %}}

*Output:*

```R

Durbin-Watson test for serial correlation in panel models

data:  invest ~ value + capital
DW = 0.98848, p-value = 2.547e-14
alternative hypothesis: serial correlation in idiosyncratic errors

```

Interpreting the output, a test statistic (`DW`) close to 1 and a low p-value indicate strong positive serial correlation in the error terms.

{{% tip %}}

For different types of models, consider these alternatives of the Durbin-Watson test:

- For pooling models: `pbsytest()`.
- For random effects models: `pbltest()`.
- For unbalanced or non-consecutive panels: `pbnftest()` with `test = "lbi"` specified. 

{{% /tip %}}


### 2. Breusch-Godfrey test

To assess serial correlation at higher orders, the Breusch-Godfrey test serves as a suitable option. You can specify the maximal order of serial correlation to be tested using the `order` argument.

{{% codeblock %}}
```R
# Perform the Breusch-Godfrey test
bgtest(model_plm, type = "Chisq", data = Grunfeld, order = 4)

```
{{% /codeblock %}}

*Output:*

```R

Breusch-Godfrey test for serial correlation of order up to 4

data:  model_plm
LM test = 149.3, df = 4, p-value < 2.2e-16

```

The output includes the LM (Lagrange Multiplier) test statistic of `149.3` and a very small p-value, indicating the presence of serial correlation.

### 3. Wooldridge test 

The Wooldridge test examines serial correlation by regressing the residuals in first-differences on their lags. It then tests whether the coefficient on the lagged residuals equals -0.5. 

{{% codeblock %}}
```R
# Perform the Wooldridge test
pwartest(model_plm)
```
{{% /codeblock %}}

*Output:*

```R

Wooldridge's test for serial correlation in FE panels

data:  model_plm
F = 162.2, df1 = 1, df2 = 207, p-value < 2.2e-16
alternative hypothesis: serial correlation

```
The output provides the test statistic (F) of `162.2` and a very small p-value, which confirms the presence of serial correlation again.

{{% tip %}}
For Stata users, the `xtserial` function can be used. Refer to [this article of Drukker (2003)](https://journals.sagepub.com/doi/pdf/10.1177/1536867X0300300206) for an example.

{{% /tip %}}



## Alternative test approach for `fixest` users

An alternative approach that does not rely on a test function involves regressing the OLS residuals on lagged residuals. A statistically significant coefficient suggests the presence of first-order serial correlation. 

First, estimate the regression model using `feols()` from the `fixest` package. 

{{% codeblock %}}
```R
# Load the library
library(fixest)

# Estimate the regression model
model_feols <- feols(invest ~ value + capital | firm + year , data = Grunfeld)

summary(model_feols) 
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/summary-feols.png" width="400">
</p> 

Note that without specifiying `vcov`, the standard errors are clustered at `firm` level. Next, compute the residuals and their lagged values:

{{% codeblock %}}
```R
# Obtain the error terms (the residuals)
e <- model_feols$residuals

# Store lagged residuals in another vector
e_lag <- c(e[-1], 0)

# Perform the regression of residuals on their lags
residual_model <- lm(e ~ e_lag)
summary(residual_model)
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/summary-residuals.png" width="400">
</p> 

The estimate of `0.50` is statistically significant, suggesting a moderate positive correlation between the residuals and their lagged values.

## How to address serial correlation?

When serial correlation is present, standard errors estimated by OLS may be misleading. You can adjust the standard errors to account for this. We can apply the Newey-West method to adjust the standard errors by including `vcov = vcovNW` in the summary of the `plm` model.

{{% codeblock %}}
```R
# Include Newey-West standard errors in plm model
summary(model_plm, vcov = vcovNW)
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/summary-plm-neweywest.png" width="400">
</p> 

To implement Newey-West standard errors in the `fixest` model, specify the panel identifier like shown in the code snippet below. 

{{% codeblock %}}
```R
# Include Newey-West standard errors in fixest model
summary(reg_feols, newey ~ firm + year)
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/summary-feols-neweywest.png" width="400">
</p> 

When comparing the adjusted standard errors with the unadjusted ones, you'll notice that they are larger after the correction for serial correlation!

Alternatively, consider exploring other estimation methods that do not assume independent observations and allow for temporal dependencies within the data. For instance, dynamic panel models incorporate lagged dependent variables, capturing the dynamic nature of the data and potentially mitigating the impact of serial correlation. 

{{% summary %}}

Serial correlation poses a challenge in panel data analysis, and can result in misleading standard errors. To identify whether serial correlation is present in your data, visual inspection with the `acf()` function and statistical tests can be used. For `plm` models, the following methods were discussed with each having their own advantages:

1. *The Durbin-Watson test:* Assumes strictly exogenous regrssors, and is designed for detecting first-order correlation. Alternative functions are provided for pooling, random effects, or unbalanced models.
2. *The Breusch-Godfrey test:* Particularly useful for identifying higher-order correlation
3. *The Wooldridge test*: Relies on fewer assumptions, and therefore has good size and power properties

For `fixest` models, an alternative approach is given that involves regresing model residuals on their lags. To address serial correlation, you can adjust standard errors with the Newey-West method or explore alternative models beyond OLS that allow for temporal dependencies in your data.

{{% /summary %}}
