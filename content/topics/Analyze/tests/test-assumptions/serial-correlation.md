---
title: "Testing for Serial Correlation"
description: ""
keywords: "serial correlation, serial, correlation, autocorrelation, statistical, test, testing, R"
draft: false
weight: 1
author: "Valerie Vossen"
aliases:
  - /exact-matching
  - /matching
---

## Overview

In time series or panel data analysis, the errors included in the regression model are often subject to serial correlation, meaning that errors from subsequent time periods depend on each other.

{{% example %}}

Consider a regression model equation with $\epsilon_{it}$ representing the error term for each observation (entity `i` in time period `t`):

{{<katex>}}
Y_{it} = \beta_0 + \beta_1 X_{it} + \epsilon_{it}
{{</katex>}}

{{% /example %}}

Adressing serial correlation is crucial due to its implications for the model outcomes, as it can lead to misleading standard errors, resulting in larger estimated uncertainties around the coefficients. In some cases, estimates may also be biased. In this topic, we will explore various methods to test for serial correlation through straighforward R code examples. Also, potential solutions will be discussed when serial correlation is present in your data. 


## How does serial correlation arise? 

One of the Gauss-Markov assumptions for the OLS estimates to be BLUE (*best linear unbiased estimate*) concerns the error terms. It is expressed as follows:   

$Corr(u_t, u_s | X) = 0 $  for all $t ≠ s$

In words; given the covariates `X`, errors in different time periods should be uncorrelated. When errors exhibit serial correlation, this assumption is violated.

{{% tip %}}

Serial correlation can be either positive or negativ. Positive correlation could for example imply that when the dependent variable unexpectedly rises in one period (above-average errors), errors are likely to be above average in the subsequent period, given the covariates. Conversely, negative correlation occurs when above-average errors are followed by below-average errors in the next time period. 

{{% /tip %}}


## Example with `Grunfeld` data

Let's consider a regression analysis using the `Grunfeld` dataset in R. Our objective is to examine the impact of market value on firm gross investment. You can find an introduction to the `Grunfeld` data and the regression equation in the [Panel data topic](/paneldata). 

The regression model is estimated in R using the `plm()` function from the `plm` package. 

{{% codeblock %}}
```R
# Load data and packages
library(AER)
data(Grunfeld)
library(plm)

# Regression model
reg <- plm(invest ~ value + capital, 
           data = Grunfeld, 
           index = c("firm", "year"), 
           model = "within", 
           effect = "twoways")

summary(reg)
```
{{% /codeblock %}}

Positive serial correlation is indeed a reasonable expectation here. This implies that when the interest rate (the dependent variable, `invest`) unexpectedly increases in one period, it is likely to remain above average in the subsequent period, given the levels of market value `market` and stock value `capital`.


## Visual inspection: autocorrelation plot

We start by visually examining the serial correlation through an autocorrelation plot. This is very straightforward using the `acf()` function. This *autocorrelation function* automatically calculates the serial correlation and generates a plot when you include `plot = TRUE`. Additionally, the `main` argument allows you to specify the title of the plot. 

{{% codeblock %}}
```R
# Obtain error terms from regression model
e <- reg$residuals

# Calculate autocorrelation and generate plot
acf_residuals <- acf(e, 
                    plot = TRUE, 
                    main = "Autocorrelation plot")
                    
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/autocorrelation-plot.png" width="400">
</p> 

The x-axis depicts the lag, indicating the time interval between each observation and its correlated observations. For instance, Lag 1 represents the first-order correlation with the previous observation, and so forth. Meanwhile, the y-axis shows the autocorrelation coefficients, reflecting the linear observations at different lags.


Ranging from -1 to 1, where 0 indicates no correlation, the coefficients show both the direction and strength of the autocorrelation. The blue dashed lines denote the lower and upper bound of the 95% confidence interval around the zero line. 

In our plot, significant positive autocorrelation is found at lag-1, 2 and 3 as indicated by spikes exceeding the confidence interval. Furthermore, as the spikes become smaller as the lag increases, it suggests observations become less correlated as they are further apart in time. 

{{% tip %}}
You can specify the maximum lag for calculating the autocorrelation using the `lag.max` argument, e.g. setting it to 3 with `lag.max = 3`. By default, when not included, it is limited to one less than the number of observations in the series.
{{% /tip %}}

## Tests for serial correlation 

Serial correlation in the error term can be assessed using various tests. 


{{% warning %}}
The three tests discussed here are only applicable to regressions using `plm`, as this function is part of the `lm` baseline. Regressions using the `fixest` package are not supported for these tests. 

An alternative approach for `fixest` analysis involves regressing OLS residuals on lagged residuals and then conducting a t-test on the coefficient of the lagged residual. A statistically significant coefficient suggests the presence of first-order serial correlation. 
{{% /warning %}}


The null hypothesis, $H_0$, that will be tested is: Serial correlation does not exist. If $H_0$ can be rejected, serial correlation is present. The test statistic ranges from 0 to 4, with value close to 2 indicating no serial correlation, less than 2: positive serial correlation, more than 2: negative serial correlation. 

### 1. Durbin Watson test

(Chapter 12 Wooldridge) 

The first way to check for first order serial correlation in the error term is the Durbin Watson test. Note that this test is specifically for 
- first order correlation only (from one period to the other)

Order 1 (AR(1)) means each error term is linearly related to the error term in the previous period. And higher orders, .... 

- assuming strictly exogenous regressors. 




{{% codeblock %}}
```R
pdwtest(reg)         
```
{{% /codeblock %}}

The following output is returned:
```R

Durbin-Watson test for serial correlation in panel models

data:  invest ~ value + capital
DW = 0.98848, p-value = 2.547e-14
alternative hypothesis: serial correlation in idiosyncratic errors

```

This test statistic (`0.98848`) close to 1, with the low p-value (lower than `0.05`), suggests strong positive serial correlation in the errors.

{{% tip %}}

- `pbsytest()` for pooling models
- `pbltest()` for random effects models
- `pbnftest()` and specify `test = "lbi"` for unbalanced or non-consecutive panels. (The default panel bnf is with `test = "bnf"` designed for balanced panel data.)

{{% /tip %}}


### 2. Breusch-Godfrey test

For assessing serial correlation at higher orders, the Breusch-Godfrey test is a suitable option. By specifying the `order` argument `order`, you can set the maximal order of serial correlation to be tested.

{{% codeblock %}}
```R

bgtest(reg, type = "Chisq", data = Grunfeld, order = 4)

```
{{% /codeblock %}}

```R

Breusch-Godfrey test for serial correlation of order up to 4

data:  reg
LM test = 149.3, df = 4, p-value < 2.2e-16

```

The output includes the LM (*Lagrange Multiplier*) test statistitc of `149.3` and a very small p-value, indicating the presence of serial correlation.


### 3. Wooldridge test 

The Wooldridge test regresses the residuals from a regression in first-differences (ref) on its lags, and then tests that the coefficient on the lagged residuals equals -0.5 (H0: no serial correlation). To account for within-panel correlation, the variance-covariance matrix adjusted for clustering at the panel level. (Stata article). Since it is based on relatively few assumptions, the Wooldridge test exhibits good size and power properties.

To conduct the Wooldridge test in R, you can use the following command:

{{% codeblock %}}
```R
pwartest(reg)
```
{{% /codeblock %}}

```R

Wooldridge's test for serial correlation in FE panels

data:  reg
F = 162.2, df1 = 1, df2 = 207, p-value < 2.2e-16
alternative hypothesis: serial correlation

```
The output provides the test statistic (F) of `162.2`, along with a very small p-value. Thus, evidence supporting serial correlation is found again.

{{% tip %}}
For Stata users, the `xtserial` function can be used. Refer to this [article] for a nice example. 
{{% /tip %}}


https://www.princeton.edu/~otorres/Panel101R.pdf



## Potential solution 

Now, after testing, we want to address it.One potential solution to account for serial correlation is to adjust standard errors to account for this.
(Robust standard error - pag 401 pdf file Wooldridge).
- test this

Alternatively, explore other estimation methods that do not rely on the assumption of independent observations and allow for temporal dependencies within the data. For example, dynamic panel models allow for the incorporation of the lagged dependent variables, thus capturing the dynamic nature of the data and potentially mitigating the impact of serial correlation. 

## Comparing the tests

table
- first column: which function to use
- orders
- tests possible with plm not with fixest (find way to do it with fixest estimated model)


summary
- first visually inspect is important
