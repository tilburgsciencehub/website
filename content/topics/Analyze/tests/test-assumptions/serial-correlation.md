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

In time series or [panel data analysis](/paneldata), data spans across different time periods, typically years, providing insights into evolving trends and patterns. Within this temporal framework lies a challenge of serial correlation, also known as autocorrelation. This occurs when the error terms in a regression model exhibit dependence across consecutive time periods, indicating a correlation among these errors. 

{{% example %}}

Consider a regression model equation where $\epsilon_{it}$ represents the error term for each observation (entity `i` in time period `t`):

{{<katex>}}
Y_{it} = \beta_0 + \beta_1 X_{it} + \epsilon_{it}
{{</katex>}}

{{% /example %}}

Adressing serial correlation is crucial due to its implications for model outcomes, as it can lead to misleading standard errors estimated for the OLS coefficients. In this article, we will explore various methods for testing serial correlation using straighforward R code examples. Additionally, potential solutions to mitigate the impact of serial correlation will be proposed.


## What is serial correlation? 

One of the fundamental Gauss-Markov assumptions for achieving the Best Linear Unbiased Estimators (BLUE) the OLS estimates to be BLUE (*best linear unbiased estimate*) pertains to the error terms. Mathematically, it is expressed as:

$Corr(u_t, u_s | X) = 0 $  for all $t ≠ s$

This assumption states that, given the covariates X, errors in different time periods should be uncorrelated. When errors exhibit serial correlation, this assumption is violated.

{{% tip %}}

Serial correlation manifests as either *positive* or *negative* correlation patterns.

*Positive serial correlation* describes a trend where an unexpected high value in the dependent variable is followed by similar high values in subsequent periods. As a result, an above-average error in one period tends to be mirrored in the next, leading to an underestimation of the true uncertainty around the OLS estimates.

Conversely, *negative serial correlation* occurs when deviations from the mean in one period are followed by opposite deviations in subsequent periods. This leads to overestimation of the true uncertainty around the estimates.

{{% /tip %}}


## Example with `Grunfeld` data

Let's consider a regression analysis using the `Grunfeld` dataset in R. Our aim is to examine the impact of market value on firm gross investment. You can refer to the [Panel data topic](/paneldata) for an introduction to the `Grunfeld` data and the regression equation. The regression model is estimated in R using the `plm()` function from the `plm` package:

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

- summary with screenshot

Positive serial correlation is a reasonable expectation in this context. This would imply that when the interest rate (the dependent variable, `invest`) unexpectedly increases in one period, it is likely to remain above average in the subsequent year, given the levels of market value (`market`) and stock value (`capital`).


## Autocorrelation plot

To visually inspect serial correlation, we will create an autocorrelation plot using the `acf()` function in R. This function automatically calculates the serial correlation and generates a plot when `plot = TRUE` is included. You can also specify the title of the plot using the `main` argument.  

{{% codeblock %}}
```R
# Extract error terms from the regression model
e <- model_plm$residuals

# Calculate autocorrelation and generate plot
acf_residuals <- acf(e, 
                    plot = TRUE, 
                    main = "Autocorrelation plot")
                    
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/autocorrelation-plot.png" width="400">
</p> 

The x-axis represents the lag, indicating the time interval between each observation and its correlated observations. For instance, Lag 1 signifies the first-order correlation with the previous observation, and so on. The y-axis shows the autocorrelation coefficients, reflecting the linear relationship between observations at different lags.

The autocorrelation coefficients range from -1 to 1, where 0 indicates no correlation. The blue dashed lines indicate the lower and upper bounds of the 95% confidence interval around the zero line. 

In our plot, significant positive autocorrelation is evident at lag-1, 2, and 3, as indicated by spikes exceeding the confidence interval. Additionally, the diminishing spikes with increasing lag suggests the observations become less correlated as they are further apart in time. 

{{% tip %}}
You can specify the maximum lag for calculating autocorrelation using the `lag.max` argument in the `acf()` function. By default, it is set to one less than the number of observations in the series.

{{% /tip %}}

## Testing for serial correlation with `plm`

Serial correlation in the error term can be assessed using various tests. 

Note that these tests are specifically designed for panel data regressions using the `plm` package as they rely on the "panelmodel" class to function correctly. You can verify the class yourself by running `class(model_plm)`. If your regressions are conducted with the `fixest` package, an alternative approach is provided in the next section. 

### 1. Durbin-Watson test

The Durbin Watson test is commonly used to check for first-order serial correlation (correlation from one period to the other). This test asssumes strictly exogenous regressors. 

{{% codeblock %}}
```R
# Perform the Durbin-Watson test
pdwtest(model_plm)         
```
{{% /codeblock %}}

```R

Durbin-Watson test for serial correlation in panel models

data:  invest ~ value + capital
DW = 0.98848, p-value = 2.547e-14
alternative hypothesis: serial correlation in idiosyncratic errors

```

Inspecting the output, we observe that the test statistic (`DW`) close to 1 and a low p-value indicate strong positive serial correlation in the error terms.

{{% tip %}}

For various types of models, explore these alternatives of the Durbin-Watson test:

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

```R

Breusch-Godfrey test for serial correlation of order up to 4

data:  model_plm
LM test = 149.3, df = 4, p-value < 2.2e-16

```

The output includes the LM (Lagrange Multiplier) test statistic of `149.3` and a very small p-value, indicating the presence of serial correlation.

### 3. Wooldridge test 

The Wooldridge test examines serial correlation by regressing the residuals in first-differences on their lags. It then tests whether the coefficient on the lagged residuals equals -0.5. To conduct the Wooldridge test in R, you can use the following command:

{{% codeblock %}}
```R
# Perform the Wooldridge test
pwartest(model_plm)
```
{{% /codeblock %}}

```R

Wooldridge's test for serial correlation in FE panels

data:  model_plm
F = 162.2, df1 = 1, df2 = 207, p-value < 2.2e-16
alternative hypothesis: serial correlation

```
The output provides the test statistic (F) of `162.2`, along with a very small p-value. Thus, evidence supporting serial correlation is found again.

{{% tip %}}
For Stata users, the `xtserial` function can be used. Refer to [this article of Drukker (2003)](https://journals.sagepub.com/doi/pdf/10.1177/1536867X0300300206) for an example.

{{% /tip %}}



## An alternative test approach for `fixest`

Another approach involves regressing the OLS residuals on lagged residuals. A statistically significant coefficient suggests the presence of first-order serial correlation. 

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

Note that without specifiying `vcov`, the standard errors are clustered at `firm` level. 

- summary screenshot

Next, compute the residuals and their lagged values. 

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

- screenshot

The estimate of `0.50` is statistically significant, suggesting a moderate positive correlation between the residuals and their lagged values.

## How to address serial correlation?

When serial correlation is present, standard errors estimated by OLS may be misleading. Luckily, you can adjust the standard errors to account for this.
Contuining with the example of the `plm` model, we apply the Newey-West method to adjust the standard errors, specifying `vcov = vcovNW`.

{{% codeblock %}}
```R
summary(model_plm, vcov = vcovNW)
```
{{% /codeblock %}}

- screenshpt

To implement Newey-West standard errors in the `fixest` model, specify the panel identifier as shown in the code snippet below. 

{{% codeblock %}}
```R
summary(reg_feols, newey ~ firm + year)
```
{{% /codeblock %}}

- screenshot 

When comparing the adjusted standard errors with the unadjusted ones, you will notice that they are larger after the correction for serial correlation!

Alternatively, consider exploring other estimation methods that do not assume independent observations and allow for temporal dependencies within the data. For instance, dynamic panel models incorporate lagged dependent variables, capturing the dynamic nature of the data and potentially mitigating the impact of serial correlation. 

{{% summary %}}

Test for serial correlation using an autocorrelation plot and various statistical tests that are applicable to `plm` regression models:

1. The Durbin-Watson test
2. The Breusch-Godfrey test
3. The Wooldridge test

For `fixest` regressions, an alternative approach is to regress the model residuals on their lags. 

To address serial correlation, adjust standard errors with the Newey-West method or use an alternative model to OLS that allows for temporal dependencies.

{{% /summary %}}
