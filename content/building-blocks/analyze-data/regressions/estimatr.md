---
title: "Standard Error Adjustments using Estimatr"
description: "Adjust standard errors efficiently and get fast estimators for design-based inference"
keywords: "estimatr, robust standard errors, linear models, IV regression, R, regression, model "
draft: false
weight: 2
aliases:
  - /estimatr
---
# Overview
The `estimatr` package is a specialized tool in R that offers quick and efficient estimators for commonly used research designs. Several of the estimators available in the R or other popular packages are sluggish and can produce inappropriate estimates due to their default settings. Moreover, some of the latest and most advanced estimators have not yet been conveniently incorporated into R packages. `estimatr` aims to address these issues by offering estimators that are optimized for design-based inference, resulting in more accurate and reliable estimates.

Using the `wage2` [data set](https://rdrr.io/cran/wooldridge/man/wage2.html), we will walk you through the process of estimating regression coefficients while accounting for potential sources of bias and violations of statistical assumptions using two of the most commonly used functions in estimatr: `lm_robust()` and `iv_robust()`.

The dataset has 935 observations on 17 variables. We will use the following variables in this example:

| **Variable** | **Description**            |
| :------  | :---------             |
| `wage`     | monthly earnings       |
| `educ`     | years of education     |
| `IQ`       | IQ score               |

## Load packages


{{% codeblock %}}
```R
install.packages("estimatr")
install.packages("wooldridge")

library(estimatr)
library(wooldridge)

data(wage2)
```
{{% /codeblock %}}  


In this example, we are interested in examining how the education level of employees relates to their wages. Let's first use the built-in `lm()` function to estimate this linear model.


{{<katex>}}
Wage_{i}  =  \beta_{0} + \beta_{1} Educ_{i} + \mu
{{</katex>}}



{{% codeblock %}}
```R
reg <- lm(data=wage2, wage~educ)
summary(reg)
```
{{% /codeblock %}}  

The `lm()` function is specifically designed to fit linear models that assume homoscedasticity, which means that the variance of the error terms is constant across all independent variables. However, if this assumption is violated, the regression estimates will still be unbiased and consistent, but they will not be as efficient. In addition, the covariance matrix of the estimated regression coefficients will be inconsistent, rendering tests of hypotheses invalid. If the homoscedasticity assumption is violated, the `estimatr` package offers quick and easy ways to adjust standard errors, allowing for robust and clustered standard errors.

## Estimate Linear Models Using lm_robust

The `lm_robust()` function is used to get the robust standard errors from a linear regression model. Now, let's re-estimate the model using robust standard errors.

{{% codeblock %}}
```R
lm_robust(data=wage2, wage~educ, se_type = "HC2")
```
{{% /codeblock %}}  


## Heteroskedasticity-Robust Standard Errors

The lm_robust() function in the estimatr package provides several options for calculating standard errors of regression coefficients using the `se_type` argument. The available options are:

- `classical`: This is the default option, which uses the classical or ordinary least squares (OLS) estimator to calculate standard errors. It assumes that the error terms are homoscedastic and uncorrelated with the independent variables.

- `HC0`: This option uses the heteroscedasticity-consistent estimator to calculate standard errors. It allows for heteroscedasticity in the error terms, but does not correct for small sample bias.

- `HC1`: This option uses the HC1 estimator to calculate standard errors. It is similar to the HC0 estimator, but includes a small sample correction to improve the accuracy of standard errors.

- `HC2`: This option uses the HC2 estimator to calculate standard errors. It is similar to the HC1 estimator, but includes a different small sample correction.

- `HC3`: This option uses the HC3 estimator to calculate standard errors. It is similar to the HC2 estimator, but includes a more robust small sample correction that is less sensitive to outliers.

In summary, these options allow the user to choose between different types of standard errors that are appropriate for different assumptions about the error terms and sample size. The HC estimators are particularly useful when there is heteroscedasticity in the error terms, which violates the assumptions of the classical estimator.

## Cluster-Robust Standard Errors
Data is considered to be clustered when there are subsamples within the data that are related to each other. When error terms are correlated within clusters but independent across clusters, then regular standard errors, which assume independence between all observations, will be incorrect. Cluster-robust standard errors are designed to allow for correlation between observations within cluster.
For cluster-robust inference, this package provides several estimators that are essentially analogs of the heteroskedastic-consistent variance estimators for the clustered case: `CR0` and `CR2`. The default is the `CR2` variance estimator, analogous to `HC2` standard errors, and perform quite well in small samples without sacrificing much in the way of efficiency in larger samples.

{{% tip %}}
Check out the [mathematical notes](https://declaredesign.org/r/estimatr/articles/mathematical-notes.html) for each of the estimators to better understand the formulas used to compute these standard errors to have a more granular understanding of the different use-cases of the different types.
{{% /tip %}}  

## Estimate Instrumental Variable (IV) Regressions Using iv_robust
The `iv_robust` function is used to estimate Instrumental Variable (IV) regressions. An instrumental variable, denoted as Z, is used in regression analysis when there are endogenous variables, which are variables that are influenced by other variables in the model. The IV regression controls for threats to internal validity, such as confounding variables, measurement error, omitted variable bias (spuriousness), simultaneity, and reverse causality. A good instrument is one that is correlated with the independent variable, X, but not with the error term. In other words, it affects the outcome variable, Y, only through X.

For instance, in our example  on the effect of education on employee wage, the IQ of the employee may be a potential confounding variable, as it may affect both education and wage. Ignoring IQ in the analysis may lead to omitted variable bias. Therefore, including IQ as an instrument variable in a 2-Stage Least Squares (2SLS) analysis of the relationship between wage and education can address the endogeneity issue and produce unbiased estimates.

Let's estimate this IV regression.

First stage regression:
$$
Educ_{i} = \gamma_{0} + \gamma_{1} IQ_{i} + \mu
$$


Second stage regression:
$$
Wage_{i} = \beta_{0} + \beta_{1} \hat{Educ_{i}} + \epsilon
$$

{{% codeblock %}}
```R
iv_robust(data=wage2, wage~educ|IQ, se_type = "HC2")
```
{{% /codeblock %}}  

{{% summary %}}

- `estimatr` is an R package for linear estimators designed for speed and ease-of-use.

- Users can easily recover robust, cluster-robust, and other design-appropriate estimates, and options are provided to obtain standard errors that reflect heteroscedasticity.

- The package includes among others, linear regression estimators like `lm_robust()` and `iv_robust()`.

- The standard errors can be adjusted using the `se_type` argument.

{{% /summary %}}
