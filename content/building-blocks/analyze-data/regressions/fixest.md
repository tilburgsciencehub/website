---
title: "Fixed-Effects Estimation in R with the fixest Package"
description: "Efficient  and fast fixed-effects estimation in R with the fixest package"
keywords: "fixest, causal inference, difference-in-difference, DID, fixed-effects, R, regression, model "
draft: false
weight: 2
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /fixest
---
# Overview

The `fixest` package is a powerful and versatile tool for analysing panel data in R. It is fast, memory-efficient, and offers a wide range of options for controlling the estimation process. Its main strength is the ability to estimate fixed effects models, which are commonly used in panel data analysis to control for unobserved heterogeneity at the individual or group level. In addition to fixed effects models, the `fixest` package includes functions for estimating other (non-)linear models such as Poisson models, and negative binomial models.

Using a stylised example, we illustrate how you can use various functions in the `fixest` package for fixed-effect estimation and also perform a difference-in-difference analysis.


For illustration purposes, we will use the [Grunfeld dataset](https://www.statsmodels.org/dev/datasets/generated/grunfeld.html) which contains investment data for 11 U.S. Firms. It contains information on the following variables:

| **Variables** 	| **Description** 	|
|---	|---	|
| `invest` 	| Gross investment in 1947 dollars 	|
| `value` 	| Market value as of Dec 31 in 1947 dollars 	|
| `capital` 	| Stock of plant and equipment in 1947 dollars  	|
| `firm` 	| - General Motors <br>- US Steel <br>- General Electric <br>- Chrysler <br>- Atlantic Refining <br>- IBM <br>- Union Oil  <br>- Westinghouse <br>- Goodyear <br>- Diamond Match <br>- American Steel  	|
| `year`  	| 1935-1954 	|      

## Install and load packages  


{{% codeblock %}}
```R
# install packages
library(fixest)
library(AER)

data(Grunfeld) # load data
```
{{% /codeblock %}}  

## Estimation with feols()

In this example, we can estimate a fixed-effects model with investment as the dependent variable and value as the independent variable, controlling for unobserved firm-level and year-level heterogeneity using the `feols()` function, which can be used to estimate linear fixed-effects models.    

{{% codeblock %}}
```R
feols_model<- feols(invest ~ value + capital | firm + year , data = Grunfeld, cluster = c("year","firm"))
```
{{% /codeblock %}}     

We use the “cluster” argument to apply clustered standard errors at the year and firm level.

### Export results

We can print a summary of the model using the `summary` function. Alternatively, one could also use the `etable` function and export the results to Latex by passing an additional argument: ‘tex = TRUE’.

{{% codeblock %}}
```R
summary(feols_model)
# Alternatively, use etable:
etable(feols_model, tex = TRUE)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summary_feols.png" width="700">
<figcaption> Fixed Effects Estimation using feols() function </figcaption>
</p>

### Extract the fixed-effect coefficients

Use the `fixef()` function to obtain the fixed-effects of the estimation. The `summary()` method helps to get a quick overview:

<p align = "center">
<img src = "../images/fixed_coef.png" width="700">
<figcaption> Extracting the fixed-effects coefficients </figcaption>
</p>

Note that the mean values are meaningless per se, but give a reference point to which to compare the fixed-effects within a dimension

Finally, the `plot` function helps to distinguish the most notable fixed-effects with the highest and lowest values for each of the fixed-effect dimensions.

{{% codeblock %}}
```R
fixedEffects = fixef(feols_model)
plot(fixedEffects)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/plot_fixed_coef.png" width="700">
<figcaption> Plot of fixed-effect coefficients </figcaption>
</p>

## Simple difference-in-difference (TWFE)

For example, let’s suppose that we want to assess the effectiveness of some policy that was implemented in the US Steel firm in 1946 and we assume the remaining firms as control groups.

For this purpose, a binary variable **`treated`** is created with a value of 1 for the "US Steel" firm and 0 for all other firms in the dataset.

Next, a new variable **`period`** is created by dividing the difference between each year and 1946 by 1 and rounding down. This creates a series of period bins with a width of one year, starting from 0 for the years 1946-1947, 1 for the years 1948-1949, and so on.

{{% codeblock %}}
```R
# set up the data
## create treatment variable
Grunfeld$treated <- ifelse(Grunfeld$firm == "US Steel", 1, 0)
## create periods bins
Grunfeld$period<- floor((Grunfeld$year - 1946)/1)
```
{{% /codeblock %}}

The DID analysis is performed using the `feols()` function from the fixest package. The dependent variable is invest, and the independent variables are value, capital, and `i(period, treated, 0)`, which creates a set of interaction variables between period and treated where period 0 is specified as the reference point. The `| firm + year` syntax specifies that fixed effects should be included for both firm and year, and the `cluster = c("firm")` argument specifies that standard errors should be clustered at the firm level.

{{% codeblock %}}
```R
# estimate the equation
est_did<- feols(invest ~ value + capital + i(period, treated, 0)| firm + year, cluster = c("firm"), Grunfeld)
summary(est_did)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/did.png" width="500">
<figcaption> Difference-in-difference estimation output </figcaption>
</p>

Finally, the **`summary()`**, **`iplot()`**, and **`coefplot()`** functions are used to obtain a summary of the regression results, an interactive plot of the coefficients, and a plot of the coefficient estimates, respectively.

The `iplot()` function helps to visualize the data and quickly identify any divergent trends between the treatment and control groups before the intervention is introduced. This would suggest that the parallel trends assumption is violated, which is a necessary prerequisite for DID estimation.

{{% codeblock %}}
```R
iplot(est_did)
coefplot(est_did)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/iplot.png" width="700">
<figcaption> Check for parallel trends assumption </figcaption>
</p>

## Other functions for estimation

Aside from `feols()`, here are additional functions useful for estimation based on the model requirements:

| **Function** 	| **Description** 	| **Use** 	|
|---	|---	|---	|
| `feglm` 	| Generalized linear models 	| This function estimates fixed-effects generalized linear models, <br> which can handle non-linear outcome <br> variables and non-normal error distributions.  	|
| `femlm` 	| Maximum likelihood estimation 	| This function estimates fixed-effects <br> maximum likelihood models, which can <br> handle a wide range of distributions and can include <br> both continuous and categorical variables. 	|
| `feNmlm` 	| Non-linear in RHS parameters 	| This function estimates fixed-effects <br> non-linear models where the <br> non-linearity is in the <br> right-hand side parameters.  	|
| `fepois` 	| Poisson fixed-effect 	| This function estimates fixed-effects <br> Poisson models, which are commonly <br> used for count data that <br> follow a Poisson distribution. 	|
| `fenegbin` 	| Negative binomial fixed-effect 	| This function estimates fixed-effects <br> negative binomial models, which are <br> commonly used for count data that <br> exhibit over dispersion relative <br> to the Poisson distribution.  	|

{{% summary %}}
Here are the key takeaways from this building block:

- Use the `feols()` function to estimate linear fixed-effect models with clustered standard errors using the `cluster` option.
- Export the estimation results using the  `summary()` or `etable()` function.
- Extract the fixed-effect coefficients using the `fixef()` function.
- Create interactions using the `i()` syntax in DID analysis.
- Visualize parallel trends assumption using the `iplot()` function
- More info on other functions you can use depending on the research question and model requirements.

{{% /summary %}}
