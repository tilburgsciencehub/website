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

[Panel data analysis](/paneldata) involves studying observations on individuals over multiple time periods, offering valuable insights into changing trends and patterns. However, a common challenge in panel data analysis is serial correlation, also known as autocorrelation, where the error terms in regression models are correlated across different periods. Addressing serial correlation is crucial as it bias the standard estimated for the OLS coefficients. In this article, we will explore methods for testing serial correlation in panel data using R code examples. Additionally, we will discuss how to address serial correlation.

## What is serial correlation? 

The Gauss-Markov assumption for OLS estimators states that error terms should be uncorrelated across different time periods given the covariates X. This is expressed as follows:

$Corr(u_t, u_s | X) = 0 $  for all $t ≠ s$

This assumption is violated when the errors exhibit serial correlation. 

Serial correlation can appear in either *positive* or *negative* patterns. *Positive serial correlation* occurs when an unexpected high (low) value in the dependent variable is followed by similar high (low) values in subsequent periods. Above-average errors in one period are mirrored in the next period, leading to an underestimation of the true uncertainty around the OLS estimates. 

Conversely, *negative serial correlation* happens when deviations from the mean in one period are followed by opposite deviations in subsequent periods. This leads to an overestimation of the true uncertainty around the estimates.

{{% /tip %}}


## Example with `Grunfeld` data

Using the `Grunfeld` dataset in R, we will examine how market value influences firm gross investment. For an introduction to this analysis and the `Grunfeld` data, please refer to the [Panel data topic](/paneldata). The regression model is estimated in R using the `plm()` function from the `plm` package, including standard errors robust to heteroskedasticity using the White method. 

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

coeftest(model_plm, 
         vcov. = vcovHC(model_plm, method = "white1",type = "HC3"))

```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/summary-plm.png" width="400">
</p> 

The `firm` fixed effects are assumed to remain constant over time. However, if this assumption is too strong and the `firm` fixed effects vary substantially over time, they do not sufficiently capture the within-cluster dependence. Consequently, serial correlation becomes a concern in the data.  

## Visually inspecting serial correlation

We will start by creating an autocorrelation plot using the `acf()` function in R.

{{% codeblock %}}
```R
# Extract error terms from the regression model
e <- model_plm$residuals

# Calculate autocorrelation and generate a plot
acf_residuals <- acf(e, 
                    plot = TRUE,
                    main = "Autocorrelation plot" # Set title
                    )
                    
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/autocorrelation-plot.png" width="400">
</p> 

The x-axis represents the *Lag*, indicating the time interval between each observation and its correlated observations. On the y-axis, the autocorrelation coefficients range from -1 to 1, where 0 indicates no correlation. The blue dashed lines around the zero line represent the 95% confidence interval. The plot displays significant positive autocorrelation at lag-1, 2, and 3, with spikes exceeding the 95% confidence interval. Additionally, the decreasing spikes as the lag increases tell us that the observations become less correlated as they are further apart in time. 

{{% tip %}}
You can set the maximum lag for calculating autocorrelation with the `lag.max` argument in the `acf()` function. By default, it is set to one less than the number of observations in the series.
{{% /tip %}}

## Testing for serial correlation in `plm` models

Various tests are available for detecting serial correlation in panel data. A drawback of these functions is that they only accept `plm` models as arguments. Consequently, you cannot directly apply them to a model estimated with the `fixest` package. If you are using `fixest` and would rather not re-estimate your model with `plm` first, the next section offers an alternative test approach that doesn't depend on these functions.

### 1. Durbin-Watson test

The Durbin-Watson test is a commonly used method to check for first-order serial correlation (correlation from one period to the other). This test assumes strictly exogenous regressors. 

{{% codeblock %}}
```R
# Perform the Durbin-Watson test for panel models
pbnftest(model_plm)         
```
{{% /codeblock %}}

*Output:*

```R
Bhargava/Franzini/Narendranathan Panel Durbin-Watson Test

data:  invest ~ value + capital
DW = 0.68497
alternative hypothesis: serial correlation in idiosyncratic errors
```

Interpreting the output, a test statistic (`DW`) close to 1 and a low p-value indicate a positive serial correlation in the error terms.

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

The Wooldridge test examines serial correlation by regressing the residuals in first differences on their lags. It then tests whether the coefficient on the lagged residuals equals -0.5. 

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
The output provides the test statistic (F) of `162.2` and a very small p-value, which suggests the presence of serial correlation again.

{{% tip %}}
For Stata users, the `xtserial` function can be used. Refer to [this article by Drukker (2003)](https://journals.sagepub.com/doi/pdf/10.1177/1536867X0300300206) for an example.

{{% /tip %}}

## Alternative test approach for `fixest` users

For `fixest` models, an alternative approach that does not rely on a test function involves regressing the OLS residuals on lagged residuals. 

First, estimate the regression model using `feols()` from the `fixest` package. 

{{% codeblock %}}
```R
# Load the library
library(fixest)

# Estimate the regression model
model_feols <- feols(invest ~ value + capital | firm + year , data = Grunfeld)

summary(model_feols, vcov = "hetero") 
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summary-feols.png" width="400">
</p> 

Note that the standard errors are clustered at the individual (`firm`) level by default. To calculate heteroskedasticity-robust standard errors, specify this with the `vcov` argument. Next, compute the residuals and their lagged values:

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

A statistically significant coefficient suggests a moderate positive correlation between the residuals and their lagged values.

## How to address serial correlation?

When serial correlation is present, standard errors estimated by OLS may be biased. To mitigate this bias, you can cluster the standard errors at the individual level. 

{{% tip %}}
Clustered standard errors can also be beneficial when you want to include two levels of fixed effects. Including both types as dummies simultaneously is not feasible, as one would absorb the other. For instance, `firm` fixed effects absorb the specific `industry` this firm belongs to. Instead, you can include `firm` fixed effects while clustering the standard errors at the `industry` level.
{{% /tip %}}

For the `plm` model, you can calculate the clustered standard erors by including `cluster = "group"`.

{{% codeblock %}}
```R
# Include clustered standard errors in the plm model
coeftest(plm_model, vcov. = vcovHC(plm_model, cluster = "group"))
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/summary-plm-neweywest.png" width="400">
</p> 

In `fixest` regressions, you can specify `vcov = "cluster"`, but note that the default will already calculate standard errors at the group level.

{{% codeblock %}}
```R
# Include clustered standard errors in the fixest model
summary(reg_feols, vcov = "cluster")
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summary-feols-neweywest.png" width="400">
</p> 

If clustered standard errors are much larger than White standard errors, it suggests the presence of autocorrelation. [Petersen (2008)](https://www.nber.org/papers/w11280) recommends considering clusterd standard errors that are 3-5 times larger than heteroskedasticity-robust ones as indicative of serial correlation. 

In our case, clustering standard errors at the individual `firm` level has not increased them. This suggests serial correlation likely did not impact the standard errors in our model. This underscores the nuance of test outcomes, as they may offer conflicting suggestions. It is crucial to critically think about your data structure, avoiding to rely solely on the statistical tests. Despite standard errors have not changed much, clustering them is still a good idea. 

Alternatively, consider exploring other estimation methods that do not assume independent observations and allow for temporal dependencies within the data. For instance, dynamic panel models incorporate lagged dependent variables, capturing the dynamic nature of the data and potentially mitigating the impact of serial correlation. 

{{% summary %}}

Serial correlation poses a challenge in panel data analysis and can result in misleading standard errors. To identify whether serial correlation is present in your data, you can visually inspect your data with the `acf()` function or use the following statistical tests for `plm` models:

1. *The Durbin-Watson test:* Assumes strictly exogenous regressors, and is designed for detecting first-order correlation. Alternative functions are provided for pooling, random effects, or unbalanced models.
2. *The Breusch-Godfrey test:* Particularly useful for identifying higher-order correlation
3. *The Wooldridge test*: Relies on fewer assumptions, and therefore has good size and power properties

For `fixest` models, an alternative test approach is given that involves regressing model residuals on their lags. It is important to consider your data structure, instead of solely relying on statistical test outcomes. Clustered standard errors are a solution serial correlation, as they ... Additionally, you can explore alternative models beyond OLS that allow for temporal dependencies in your data.

{{% /summary %}}
