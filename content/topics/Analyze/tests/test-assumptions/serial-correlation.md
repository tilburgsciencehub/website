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

[Panel data analysis](/paneldata) offers valuable insights into changing trends and patterns by studying observations on individuals over multiple time periods. However, a common challenge when working with panel data is serial correlation, also known as autocorrelation, where the error terms in regression models are correlated across different periods. Addressing serial correlation is crucial as it can bias the standard errors estimated for the OLS coefficients. This article explores methods for testing serial correlation in panel data using R code examples and discusses strategies for addressing it. 

## What is serial correlation? 

The Gauss-Markov assumption for OLS estimators states that error terms should be uncorrelated across different time periods given the covariates X. This is expressed as follows:

{{<katex>}}
{{</katex>}}

$Corr(u_t, u_s | X) = 0 $  for all $t ≠ s$

However, when errors exhibit serial correlation, this assumption is violated. 

Serial correlation can appear in either *positive* or *negative* patterns. *Positive serial correlation* occurs when an unexpected high (low) value in the dependent variable is followed by similar high (low) values in subsequent periods. this results in above-average errors in one period being mirrored in the next, leading to an underestimation of the true uncertainty around the OLS estimates. On the other hand, *negative serial correlation* arises when deviations from the mean in one period are followed by opposite deviations in subsequent periods. This leads to an overestimation of the true uncertainty around the estimates.


## Example with `Grunfeld` data

We will use the `Grunfeld` dataset in R to examine how market value influences firm gross investment. For an introduction to this analysis, you can refer to the [Panel data topic](/paneldata). The regression model is estimated using the `plm()` function from the `plm` package, with standard errors robust to heteroskedasticity using the White method. 

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
<img src = "../images/coeftest-plm-white.png" width="400">
</p> 

In [the Fixed Effects model](/within), we assume the unobserved `firm` effects to remain constant over time. If this assumption appears too strong and these effects vary substantially across periods, these terms might not sufficiently capture the within-cluster dependence, which can lead to serial correlation becoming an issue.

## Visual inspection of serial correlation

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

Various tests are available for detecting serial correlation in panel data. A drawback of these functions is that they only accept `plm` models as arguments and therefore you cannot directly apply them to a model estimated with the `fixest` package. If you are using `fixest` and would rather not re-estimate your model with `plm` first, the next section offers an alternative test approach that doesn't depend on these functions.

### 1. Durbin-Watson test

The Durbin-Watson test is commonly used to check for first-order serial correlation (correlation from one period to the other). This test assumes strictly exogenous regressors. 

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

The DW test statistic ranges between 0 and 4, with a value around 2 indicating no autocorrelation, values below 2 suggesting positive autocorrelation, and values above 2 suggesting negative autocorrelation. 

In the output, the DW statistic of `0.86` with a low p-value indicates there is positive autocorrelation in the regression model. 

{{% tip %}}

For different types of models, consider these alternatives of the Durbin-Watson test:

- For pooling models: `pbsytest()`.
- For random effects models: `pbltest()`.
- For unequally-spaced panels: `pbnftest()` with `test = "lbi"` specified. 

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
<img src = "../images/summary-feols-white.png" width="400">
</p> 

Note that the standard errors are clustered at the individual (`firm`) level by default. To calculate heteroskedasticity-robust standard errors, specify this with the `vcov` argument. Next, compute the residuals and their lagged values:

{{% codeblock %}}
```R
# Obtain residuals and their lagged values
e <- model_feols$residuals
e_lag <- c(e[-1], 0)

# Perform regression of residuals on their lags
residual_model <- lm(e ~ e_lag)
summary(residual_model)
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/summary-residuals.png" width="400">
</p> 

A statistically significant coefficient suggests a positive correlation between the residuals and their lagged values, indicating serial correlation.

## How to address serial correlation?

Clustered standard errors are a method to correct for the bias in the standard errors resulting from serial correlation, as they account for the dependence among observations within clusters, such as firms. 

For the `plm` model:

{{% codeblock %}}
```R
# Include clustered standard errors in the plm model
coeftest(plm_model, vcov. = vcovHC(plm_model, cluster = "group"))
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/coeftest-plm-cluster.png" width="400">
</p> 

For `fixest` regressions, clustered standard errors are the default. However, you can explicitly include them by specifying the `vcov` argument:  


{{% codeblock %}}
```R
# Include clustered standard errors in the fixest model
summary(model_feols, vcov = "cluster")
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summary-feols-cluster.png" width="400">
</p> 

{{% tip %}}
If clustered standard errors are much larger than White standard errors, it suggests that serial correlation is affecting the standard errors, as they are inflated when adjusting for this. According to [Petersen (2008)](https://www.nber.org/papers/w11280), clustered standard errors that are 3-5 times larger than heteroskedasticity-robust (White) ones can be indicative of serial correlation, serving as a rule of thumb.
{{% /tip %}}

In our case, clustering at the individual `firm` level has not inflated the standard errors. This suggests serial correlation might not have a large impact on the standard errors in our model, despite test outcomes telling otherwise. 


This highlights the complexity of testing for serial correlation, where there might not always be a definitive answer. It is crucial to critically assess your data structure rather than solely relying on statistical test outcomes. 

Alternatively, consider exploring other estimation methods that do not assume independent observations and allow for temporal dependencies within the data. For instance, dynamic panel models incorporate lagged dependent variables, capturing the dynamic nature of the data and potentially mitigating the impact of serial correlation. 

{{% summary %}}

Serial correlation poses a challenge in panel data analysis and can lead to biased standard errors. To identify whether serial correlation is present in your data, you can visually inspect your data with the `acf()` function or employ statistical tests for `plm` models, such as: 

1. *The Durbin-Watson test:* Assumes strictly exogenous regressors and is designed for detecting first-order correlation. Alternative functions are provided for pooling, random effects, or unbalanced models.
2. *The Breusch-Godfrey test:* Particularly useful for identifying higher-order correlation
3. *The Wooldridge test*: Relies on fewer assumptions, and therefore has good size and power properties

For `fixest` models, an alternative test approach involves regressing model residuals on their lags.

Clustered standard errors provide a solution by accounting for the dependence in error terms within clusters. When clustered standard errors are much larger than heteroskedasticity-robust ones, this suggests the presence of serial correlation.

{{% /summary %}}
