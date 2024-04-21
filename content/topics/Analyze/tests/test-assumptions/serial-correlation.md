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

In analysis using time series or panel data, the errors included in the regression model are quite likely to suffer from serial correlation, also known as autocorrelation. This means the errors from subsequent time periods depend on each other. It can be either positive or negative. E.g. positive correlation would mean that when the dependent variable is unexpectedly high for one period, they are likely to also be above average (given the covariates) for the next period. Negative correlation is when the investment rate fell in this period, it is likely to rise in the next period.

It is important to address serial correlation as it has consequences for the outcomes of the model, as one of the model assumptions about independence among observations is violated. Since the OLS standard errors are based on this assumption, the resulting ones can be misleading when this correlation is ignored. The uncertainty around the estimates are is larger than is estimated by OLS. In some cases, estimates can also be biased. In this topic, we will dive into different ways to test for serial correlation with practical code examples, and then discuss solutions for when serial correlation is present in your data. 

## Serial correlation 

As a benchmark for time series or panel data analysis, there are five Gauss Markove assumptions that should hold for the OLS estimates to be BLUE (*best linear unbiased estimate*). The fifth one is about the error terms and :  

{{<katex>}}
Corr(u_t, u_s | X) = 0 for all t =/ s
{{</katex>}}

Conditional on the covariates `X`, the errors in two different time periods are uncorrelated. Or to put it even more simply: 

Corr(u_t, u_s) = 0 for all t =/ s

When this assumption doesn't hold, error terms are correlated across time, i.e. they suffer from serial correlation. Order 1 (AR(1)) means each error term is linearly related to the error term in the previous period. And higher orders, .... 


## Example with `Grunfeld` data

Let's take a simple example analysis with the `Grunfeld` dataset, which has a panel data structure consisting of 11 firms over 20 years. We are interested in the relationship between market value and gross investment of firms, which we can estimate with the following regression equation:

{{<katex>}}
invest_{it} = \beta_0 + \beta_1 value_{it} + \beta_2 capital_{it} + \alpha_i +  \delta_t + \epsilon_{it}
{{</katex>}}  

where:
- $invest_{it}$ is the gross investment of firm `i` in year `t`
- $value_{it}$ is the market value of assets of firm `i` in year `t`
- $capital_{it}$ is the stock value of plant and equipment of firm `i` in year `t`
- $\alpha_i$ is the fixed effect for firm `i`
- $\delta_t$ is the fixed effect for year `t`
- $u_{it}$ is the error term, which includes all other unobserved factors that affect investment but are not accounted for by the independent variables or the fixed effects.

The regression model is estimated in R with `plm()` function the `plm` package. 

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

Serial correlation in the error terms would be present if the investment rates (the dependent variable in the model) are unexpectedly high for one period, they are likely to be above average (for the given levels of c)
E.g. if interest rates (dependent var) are unexpectedly high for this period, they are likely to be above average (for the given levels of market value `market` and stock value `capital`) for the next period. This is reasonable to expect. 

## Autocorrelation plot

Before checking quantitatively, we can visually inspect the potential serial correlation between the error terms. To do this, you can easily make an autocorrelation plot with `acf()` (the *autocorrelation function*) . This function calculates the autocorrelation and plots it automatically when you set the argument `plot` to `TRUE`. The argument `main` sets the main title of the plot. 


{{% codeblock %}}
```R
# Obtain error terms from regression model
e <- reg$residuals

# Calculate autocorrelation + make plot
acf_residuals <- acf(e, 
                    plot = TRUE, 
                    main = "Autocorrelation plot")
                    
```
{{% /codeblock %}}

screenshot 

The x-axis represents the lag, i.e. the time interval between each observation and its correlated observations. Lag 1 represents the first-order correlation with the previous observation, and so on. The y-axis shows the autocorrelation coeffcients, which measure the strength and direction fo the linear relationship between observations at different lags. It ranges from -1 to 1, where 0 indicates no correlation. The blue dashed lines are the lower and upper bound of the 95% confidence interval around the zero line. Interpreting our plot, significant positive autocorrelation is found at lag-1, 2 and 3 as these spikes reach above the confidence interval,
As the spikes become smaller as lag increases, it suggests observations become less correlated as they become further apart in time. 

{{% tip %}}
With the `lag.max` argument you can set the maximum lag at which to calculate the acf, e.g set to 3 as a max with `lag.max = 3`. Default when not included is a limited to one less than the number of observations in the series.
{{% /tip %}}


## Durbin Watson test

(Chapter 12 Wooldridge) 

The first way to check for first order serial correlation in the error term is the Durbin Watson test. Note that this test is specifically for 
- first order correlation only (from one period to the other)
- assuming strictly exogenous regressors. 


The null hypothesis, $H_0$, that will be tested is: Serial correlation does not exist. If $H_0$ can be rejected, serial correlation is present. The test statistic ranges from 0 to 4, with value close to 2 indicating no serial correlation, less than 2: positive serial correlation, more than 2: negative serial correlation. 


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


Alternative approach: regress OLS residual on lagged residual and then conduct t test on the coefficient of the lagged residual. If coefficient is statistically significant it suggests presence of serial correlation first order.


## Breusch-Godfrey test

To test for serial correlation at higher orders, you can use the Breusch-Godfrey test. With the argument `order`, you can set the maximal order of serial correlation to be tested.

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

The LM (*Lagrange Multiplier*) test statistitc of `149.3` and a very small p-value, the null hypothesis that there is no serial correlation is rejected. 


## Wooldridge test 

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
The test statistic (F) of `162.2`, and a very small p-value indicate again evidence against the null hypothesis of no serial correlation. In other words, evidence for serial correlation formulated as the alternative hypothesis is found.

https://www.princeton.edu/~otorres/Panel101R.pdf


(Stata article)
based on few assumptions only
good size and power properties under these weaker assumptions
uses the residuals from a regression in first-differences

regress residuals from regression with first-differenced variables on their lags and tests that the coefficient on the lagged residuals is equal to -0.5
to account for within-panel correlation, VCE adjusted for clustering at panel level

Stata xtserial function
example: NLS, log wages as function of age etc.
null hypothesis: no serial correlation

## Potential solution 

adjust standard errors to account for correlation structure in the errors. Robust standard error - pag 401 pdf file Wooldridge.

Find other estimation method that does not rely on independent observations, and doesn't require this assumption?


## Comparing the tests

table
- first column: which function to use
- orders
- tests possible with plm not with fixest (find way to do it with fixest estimated model)
