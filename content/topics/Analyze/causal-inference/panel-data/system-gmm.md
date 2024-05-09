---
title: "Dynamic Panel Data Estimation with System-GMM"
description: " "
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

[Panel data](\paneldata) tracks observations of individuals over multiple time periods, enabling researchers to uncover dynamic patterns that can't be observed in cross-sectional or time-series data alone. While traditional static panel data models assume that idiosyncratic errors are uncorrelated across time periods, dynamic panel models account for temporal depencies in the data, often providing a more accurate representation of economic relationships. By including the lagged dependent variable as a regressor, dynamic panel models account for adjustment dynamics and persistence in the data. 

This topic introduces the dynamic panel model and demonstrates how to estimate it, given that the estimation methods for panel data (e.g. Fixed Effects) are likely to produce biased results. Furthermore, an example with R code is provided.


{{% example %}}

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

While including the lagged dependent variable provides a more accurate representation of the dynamic nature of the data, endogeneity arises which is known as the Nickell bias.

## Nickell bias

The lagged dependent variable is correlated with the error term, introducing endogeneity in the model which can be expressed as:

$E(v_{it} | Y_{i,t-1}) ≠ 0$. 

As a result, standard panel data estimators like [Fixed Effects](\within), [Random Effects](\random), and [First-Difference](\firstdifference) become biased and inconsistent. Both the coefficients of the lagged dependent variable ($\beta_1$) and coefficients of interest ($\beta_2$) are potentially biased.

The size of the bias depends on the length of the time period (T), as well as the persistence of the correlation, making the bias particularly significant in panels with a short T and a large number of individuals (N).

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

System GMM, introduced by [Blundell and Bond (1998)](https://www.sciencedirect.com/science/article/pii/S0304407698000098?casa_token=dYWIhT8f8OMAAAAA:ABPXjapGCr7BAZKtJVamMFPhU2yvYbgDcnAd7Usvp6H2QqyxhJftVQQ9i-KXcfAg_qH8BbAs), is a Generalized Method of Moments (GMM) approach that corrects for the Nickell bias by using lagged variables as instruments. 

It exploits the so-called orthogonality conditions (where instruments are uncorrelated with the error terms) to construct valid instruments from both lagged levels and lagged differences of the endogenous variables. A system of equations is estimated, one for each time period, and the instruments vary across equations. For instance, in later time periods, additional lags of the instruments are available and can be used. 

{{% tip %}}
*Difference GMM vs. System GMM* 

Difference GMM is the original estimator which uses only lagged levels of the dependent variable as instruments, while System GMM combines lagged levels and differences as instruments.

{{% /tip %}}

### Two-step System GMM

The two-step system GMM estimation process involves:
1. *First-differencing* the variables to eliminate individual fixed effects
2. *Instrumenting* the differenced equations using lagged levels and differences of the variables. 

## Instrument validity
Instrument validity is crucial in System GMM estimation. Instruments must be:
- Relevant: Highly correlated with the endogenous variables they instrument. 
- Exogenous: Uncorrelated with the composite error term. 

If error term is i.i.d., those lags of y will be highly correlated with the lagged dependent variable (and its difference) but uncorrelated with the composite error process, which is required for an instrument to be valid!

[Bastardoz et al. (2023)](https://www.sciencedirect.com/science/article/abs/pii/S1048984322000765)

## Example in R

- Adapt example from here: https://rdrr.io/cran/plm/man/pgmm.html
- Interpretation of output
- Tests and diagnostics: Sargan test, AR test for autocorrelation of residuals

Inequality

tip
OLS: lagged dep. var positively correlated with the error, biasing its coefficient upward
FE: coefficient biased downward due to negative sign on v_t-1 in the transformed error.

Consistent estimates should lie between these two values, which might be a useful check.
Check whether coefficient of lag dependent variable is sensitive to lag length.
tip

## Tests or diagnostics
- Sargan-Hansen test
- Sargan; instrument validity
- AR test for autocorrelation of the residuals. 

By construction, the residuals of the differenced equation should possess serial correlation, but if the assumption of serial independence in the original errors is warranted, the differenced residuals should not exhibit significant AR(2) behavior. If a significant AR(2) statistic is encountered, the second lags of the endogenous varialbes will not be appropriate instruments for their current values. 

Only use 2-5 lags in constructing the GMM instruments, otherwise possible loss of efficiency

- While DPD estimator are linear estimators, highly sensitive to the particular specification of the model and its instruments. 



{{% summary %}}

A Nickell bias arises as a consequence of correlation of the lagged dependent variable with the error term by construction. Standard panel data estimators (FE, RE, FD) will be inconsistent, especially in analysis with short time series (T) and large number of individuals (N). 

{{% /summary %}}

References
- Econometric analysis of panel data - Baltagi fourth edition.

- https://web.sgh.waw.pl/~jmuck/EoPD/Meeting8.pdf
- http://fmwww.bc.edu/EC-C/S2013/823/EC823.S2013.nn05.slides.pdf

cannot open, so not sure : https://www.sciencedirect.com/science/article/abs/pii/S0169716119300021

