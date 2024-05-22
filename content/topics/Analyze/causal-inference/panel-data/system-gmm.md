---
title: "Dynamic Panel Data Estimation with System-GMM"
description: "An introduction to dynamic panel models, and how to estimate them correctly using GMM."
keywords: "dynamic, panel, data, estimation, system, GMM, generalized, method, moments"
draft: false
weight: 8
author: "Valerie Vossen"
aliases:
  - /system-gmm
  - /gmm
  - /dynamic-panel-data
  - /dynamic
---

## Overview

[Panel data](\paneldata) tracks observations of individuals over multiple time periods, enabling researchers to uncover dynamic patterns that can't be observed in cross-sectional or time-series data alone. While traditional static panel data models assume that idiosyncratic errors are uncorrelated across time periods, dynamic panel models account for temporal depencies in the data by including the lagged dependent variable as a regressor, often providing a more accurate representation of economic relationships, by including the lagged dependent variable as a regressor.

This topic introduces the dynamic panel model and demonstrates how to estimate it, given that the estimation methods for panel data (e.g. Fixed Effects) are likely to produce biased results. After introducing the dynamic panel data model and System-GMM estimation, a simple example of estimation in R is provided.

{{% example %}}

Dynamic panel data models account for persistence or adjustment dynamics in the data. Think of ... 

{{% /example %}}

## Dynamic panel data model

A general form of the dynamic panel data model is expressed as follows: 

$Y_{it} = \beta_1 Y_{i,t-1} + \beta_2 x_{it} + u_{it}$
{{<katex>}}
{{</katex>}}

where

- $Y_{it}$: Dependent variable for individual $i$ at time $t$
- $Y_{i,t-1}$: Lagged dependent variable
- $x_{it}$: Vector of independent variables
- $u_{it}$: Error term consisting of the unobserved individual specific effect ($\mu_{i}$) and the idiosyncratic error ($v_{it}$)

{{% summary %}}
Key characteristics of the dynamic panel model: 

- *A linear functional relationship*
- *Dynamic dependent (left-hand) variable:* A lagged dependent variable is included among the regressors
- *Endogenous explanatory (right-hand) variables* that are correlated with past and possible current error terms
- *Fixed individual effects:* Unobserved heterogeneity among individuals, which is another source of persistence over time
- *Heteroskedasticity and autocorrelation* within individual units, but not across them
{{% /summary %}}

While including the lagged dependent variable provides a more accurate representation of the dynamic nature of the data, endogeneity is likely to arise in standard panel data estimation. This is known as the Nickell bias.

## Nickell bias

Discovered by [Nickell (1981)](https://www.jstor.org/stable/1911408), including the lagged dependent variable introducing endogeneity in the model due to its correlation with the error term in the model. This can be expressed as:

$E(v_{it} | Y_{i,t-1}) ≠ 0$. 

As a result, standard panel data estimators like [Fixed Effects](\within), [Random Effects](\random), and [First-Difference](\firstdifference) become biased and inconsistent. Both the coefficients of the lagged dependent variable ($\beta_1$) and coefficients of interest ($\beta_2$) are potentially biased. The size of the bias depends on the length of the time period (T), as well as the persistence of the correlation, making the bias particularly significant in data with a short T and a large number of individuals (N). Increasing N will not decrease the bias. 

Specifically, it leads to: 

- *Overestimation with OLS*

Since the dependent varaible ($Y_{it}$) is a function of the unobserved individual effects ($\mu_{i}$), the lagged dependent variable ($Y_{i,t-1}$) is also a function of $\mu_{i}$. Therefore, $Y_{i,t-1}$ is positively correlated with the error, which biases the OLS estimator, even if the idiosyncratic error terms $v_{it}$ are not serially correlated.

- *Underestimation with Fixed Effects (FE)*

The [FE estimator](\within) eliminates $\mu_{i}$ through demeaning (within transformation). However, this transformation introduces a negative correlation between the transformed lagged dependent variable and the error term, resulting in downward bias. The coefficient $\beta_1$, measuring the persistence of the dependent variable, will be underestimated, and if other regressors are correlated with lagged dependent variable, their coefficients may also be biased.

{{% tip %}}
*How does this bias exactly occur?*

The within transformation subtracts the individual mean from each observation:

$\tilde{Y_{it}} = Y_{it} - \bar{Y_{i}}$


where $\bar{Y_{it}}$ is the mean of the dependent variable for individual $i$. The same transformation is applied to the lagged dependent variable and the error term. 

The transformed lagged dependent variable. $\tilde{Y_{i,t-1}}$, is still correlated with the transformed error term ($\tilde{v_{it}}$), because the mean ($\bar{v_i}$) contains a lagged error ($v_{i,t-1}$) that correlates with $Y_{i,t-1}$ by construction. 

Also, the transformed error term $\tilde{v_{it}}$ is correlated with the transformed lagged dependent variable, as its mean ($\bar{Y_{i,t-1}}$) includes $Y_{it}$.
 
{{% /tip %}}


## Estimation with System GMM

System Generalized Method of Moments (GMM), introduced by [Blundell and Bond (1998)](https://www.sciencedirect.com/science/article/pii/S0304407698000098?casa_token=dYWIhT8f8OMAAAAA:ABPXjapGCr7BAZKtJVamMFPhU2yvYbgDcnAd7Usvp6H2QqyxhJftVQQ9i-KXcfAg_qH8BbAs), addresses endogeneity by using lagged variables as instruments. Specifically, it uses the so-called orthogonality conditions (where instruments are uncorrelated with the error terms) to construct valid instruments from both lagged levels and lagged differences of the endogenous variables. A system of equations is estimated, one for each time period, and the instruments vary across equations. For instance, in later time periods, additional lags of the instruments are available and can be used. 

{{% tip %}}
*Difference GMM vs. System GMM* 

Difference GMM is the original estimator which uses only lagged levels of the dependent variable as instruments, while System GMM combines lagged levels and differences as instruments.

{{% /tip %}}

The *two-step system GMM* estimation process involves:
1. *First-differencing* the variables to eliminate individual fixed effects
2. *Instrumenting* the differenced equations using lagged levels and differences of the variables. 


## Instrument validity

Instrument validity is crucial. The conditions for a valid instruments to satisfy are: 

1. *Relevance:* Instruments must be highly correlated with the endogenous variables they instrument. Using sufficient lags can help to maintain this condition. 

2. *Exclusion restriction:* The lagged instruments must be exogenous, meaning they are uncorrelated with the error term. The instruments should only affect the dependent variable through the endogenous predictor. This assumption generally requires theoretical justification, and if instruments are found to be endogenous, thye cannot simply be fixed.

3. *Independence assumption*: The instruments are independent of the error term. In System GMM, lagged levels and differences of the endogenous variables should be uncorrelated with future errors. Limiting the lag length can help avoid correlation with present errors to maintain this condition. 

In practice, it is important to balance the number of lags to ensure sufficient relevance without introducing bias or violating the exclusion and independence assumptions. 

To ensure instrument validity, the Sargan test (of overidentifying restrictions) can be used, when there are more instruments than the number of endogenous variables (i.e. the model is overidentified). It tests whether all the instruments used in the model are uncorrelated with the error term, i.e. whether they are exogenous. Furthermore, the Arrellano-Bond test for autocorrelation of order 2 can help to ensure whether the differenced residuals are not serially correlated at order 2. More on this in the R code example!

{{% tip %}}
For more background on Instrumental Variable Estimation: 
- [Intro to IV Estimation](\iv)
- [Bastardoz et al. (2023)](https://www.sciencedirect.com/science/article/abs/pii/S1048984322000765): A comprehensive review of IV Estimation discussing valid instruments. 
{{% /tip %}}


## Example in R

An example adjusted from [Blundell & Bond (1998)](https://www.sciencedirect.com/science/article/pii/S0304407698000098?casa_token=dYWIhT8f8OMAAAAA:ABPXjapGCr7BAZKtJVamMFPhU2yvYbgDcnAd7Usvp6H2QqyxhJftVQQ9i-KXcfAg_qH8BbAs), with unbalanced panel data of 140 firms in the UK over the years 1976-1984. The following model is estimated:


$Log(Empl)_{it} = \beta_1 Log(Empl)_{i,t-1} + \beta_2 Log(Wage)_{it} + \beta_3 Log(Wage)_{i,t-1} + \beta_4 Log(Cap)_{it} + \beta_5 Log(Cap)_{i,t-1} + \mu_{i} + v_{it}$

{{<katex>}}
{{</katex>}}

Where:
- $Log(Empl)_{it}$ is the log of employment in firm $i$ in year $t$, and its lag is included on the right-hand side
- The independent variables include both current and lag values of log wages and log capital
- $\mu_{i}$: The fixed effects per firm
- $v_{it}$: The idiosyncratic error term

The instruments used for the GMM estimation depend on the assumptions regarding the correlation between the independent variables and the erorr term. Here, we do not assume wages and capital to be strictly exogenous, so they are also instrumented. 

The dataset starts in 1976 because the data provider did not report employment data for earlier years. Consequently, the first observation for each firm in this sample is not special, supporting the validity of the initial conditions restriction. Outlined in Blundell and Bond (1998), this restriction assumes that the initial observations of the dependent variable are not correlated with the individual-specific effects and is crucial for the System-GMM estimation to be valid. 



{{% codeblock %}}
```R
# Load the package and data
library(plm)
data("EmplUK")

# Estimate the dynamic model with Two-step System GMM
dyn_model <- pgmm(log(emp) ~ lag(log(emp), 1) + 
                  lag(log(wage), 0:1) + lag(log(capital), 0:1) | 
                    lag(log(emp), 2:99) + lag(log(wage), 2:99) + 
                    lag(log(capital), 2:99),
                  data = EmplUK, 
                  effect = "twoways", 
                  model = "twosteps", 
                  transformation = "ld", 
                  collapse = TRUE
)
```
{{% /codeblock %}}


- Deeper lags of the endogenous variables are used as instruments, specified behind the `|`. Here, all lags from 2 of the endogenous varibles are used as GMM instruments. As wages and capital are expected to be endogenous in this model, they are instrumented as well.
- `effect = twoways` introduces both firm and time fixed effects. To only include firm fixed effects,  use `effect = individual`.
- `model = "twosteps"` uses the two-step GMM estimator
- `transformation = "ld"` applies the first-difference transformation and thus the use of a System GMM model instead of a Difference GMM.
- `collapse = TRUE` reduces the number of instruments to avoid overfitting the model

{{% tip %}}
- For further details, refer to the [pgmm documentation](https://rdrr.io/cran/plm/man/pgmm.html).
{{% /tip %}}

## Interpreting the output

{{% codeblock %}}
```R
# Print summary of the model with robust standard errors
summary(dyn_model, robust = TRUE)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/summary-gmm.png" width="700">
</p>


Refer to this [topic] for full interpretation of a summary output in R. 

Employment persistence is found to be very strong, indicated by the positive coefficient of past employment levels that is statistically significant at a 1% level. Furthermore, higher current wages seem to decrease employment, while higher past wages increase employment. And, current investment has a positive impact, whereas past capital investments appear to have a negative effect on employment. 


## Tests 
- The Sargan test of the over-identifying restrictions tests the validity of the instruments. A p-value of 0.449 is high enough to indicate that the instruments are valid. 

- Autocorrelation Tests: First-order serial correlation (1) is present indicated with a p-value < 0.05, which happens by construction and is as expected. There is no second-order serial correlation (2), indicated with a p-value > 0.05, which is consistent with the assumptions. If AR(@) was present, the second lags of the endogenous variables will not be appropriate instruments for their current values. 

- The Wald Tests assesses the joint significance of all the coefficients or time dummies in the model. The low p-value indicates that we reject the null hypothesis, suggesting the coefficients and time dummies have an effect on the dependent variable. 
 

All the test outcomes confirm the validity of the model. 

These dynamic panel data estimators are highly sensitive to the particular specification of the model and its instruments. Therefore, it is good practice to do several robustness checks and experiment with different model specifications the inclusion of different lag lenghts.


{{% tip %}}
As a useful check, consistent estimates should lie inbetween the OLS and the FE estimates. This is because the OLS coefficient is biased upwards and the FE biased downwards. 
{{% /tip %}}


{{% summary %}}

A Nickell bias arises as a consequence of correlation of the lagged dependent variable with the error term by construction. Standard panel data estimators (FE, RE, FD) will be inconsistent, especially in analysis with short time series (T) and large number of individuals (N). 

{{% /summary %}}

References
- Econometric analysis of panel data - Baltagi fourth edition.

- https://web.sgh.waw.pl/~jmuck/EoPD/Meeting8.pdf
- http://fmwww.bc.edu/EC-C/S2013/823/EC823.S2013.nn05.slides.pdf

cannot open, so not sure : https://www.sciencedirect.com/science/article/abs/pii/S0169716119300021

