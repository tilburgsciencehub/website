---
title: "Dynamic Panel Data Estimation with System-GMM"
description: " "
keywords: "generalized", "moments"
draft: false
weight: 1
author: "Valerie Vossen"
aliases:
  - /system-gmm
  - /gmm
  - /dynamic-panel-data
  - /dynamic
---

## Overview

- Introduce topic
- Motivation why dynamic panel models are relevant; e.g. many economic relationships are dynamic in nature
- include how they differ from "traditional" panel models and why that difference matters.


[Panel data](\paneldata) follows observations of individuals over multiple time period, enabling researchers to uncover dynamic patterns that cannot be observed in cross-sectional or time-series data alone. 


[Traditional static panel data models](\paneldata-assumptions) rely on the assumption that observations are independently .. over time. On the other hand, dynamic panel models are crucial in analyzing economic relationships that exhibit adjusment dynamics and persistence. Unlike traditional static panel models, dynamic panel analysis recognizes and incorporates the temporal interdepencies of variables by including the lagged dependent variable as a regressor. This often provides a more accurate representation. 

A new estimation method is suggested, as the OLS, FE and, RE method give bias. .. An R code example is given.

{{% example %}}
Example of relationship that is dynamic, e.g. inequality level. 
{{% /example %}}



## Dynamic panel data model

A general form of the dynamic panel data model is expressed as follows: 


{{<katex>}}
Y_{it} = \beta_1 Y_{i,t-1} + \beta_2 * x_{it} + \u_{it}
{{</katex>}}

where

- $Y_{it}$: Dependent variable for individual $i$ at time $t$
- $Y_{i,t-1}$: Lagged dependent variable
- $x_{it}$: Vector of independent variables
- $u_{it}$: Error term consisting of the unobserved individual specific effect ($\mu_{i}$) and the idiosyncratic error ($v_{i,t}$)

Dynamic panel models exhibit two primary sources of persistence over time:

1. Autocorrelation: Presence of a lagged dependent variable among the regressors
2. Individual effects: Unobserved heterogeneity among individuals 


## Nickell bias

Including the lagged dependent variable as a regressor introduces a problem of endogeneity due to correlation with the error term, i.e. $E(v_{it} | Y_{i,t-1}) ≠ 0$. This leads to the Nickell bias, which makes standard panel data estimators ([Fixed Effects](\within), [Random Effects](\random), [First-Difference](\firstdifference)) biased and inconsistent.  Both coefficients of the lagged dependent variable ($\beta_1$) and coefficients of interest will exhibit some bias ($beta_2$). 

The size of the bias depends on the length of the time period (T), as well as the correlation persistence, and this bias is thus particularly significant in panels with a short T and a large number of individuals (N).

Specifically it causes: 

- *Overestimation with OLS*

Since the dependent varaible $y_{it}$ is a function of the unobserved individual effects $\mu_{i}$, it follows that the lagged dependent variable $y_{i,t-1}$ is also a function of $\mu_{i}$. Therefore, the lagged dependent variable is positively correlated with the error, which biases the OLS estimator, even if the idiosyncratic error terms $v_{it}$ are not serially correlated.

- *Underestimation with Fixed Effects (FE)*

The [FE estimator](\within), also known as the within estimator, eliminates individual effects ($\mu_{i}$) through demeaning (within transformation). However, the transformation introduces a negative correlation between the transformed lagged dependent variable and the error term, resulting in downward bias. The coefficient $\beta_1$, measuring the persistence of the dependent variable, will be underestimated, and if other regressors are correlated with lagged dependent variable, their coefficients may be biased as well.

{{% tip %}}
*How does this bias exactly occur?*

The within transformation subtracts the individual mean from each observation:

$\tilde{Y_{it}} = Y_{it} - \bar{Y_{it}}

where $\bar{Y_it} is the mean of the dependent variable. The same transformation is applied to the lagged dependent variable and the error term. 

The transformed lagged dependent variable. $\tilde{Y_{i,t-1}}$, is still correlated with the transformed error term ($\tilde{v_{it}}$ because the mean ($\bar{v_i}$ contains a lagged error ($v_{i,t-1}$) that correlates with $Y_{i,t-1}$ by construction. 

And. the transformed error term $\tilde{v_i,t-1}$ is also correlated with the mean of the lagged dependent variable ($\bar{Y_{i,t-1}}) due to the inclusion of $v_{i,t}$ in the mean ($\bar{v_i$})
 
{{% /tip %}}

The Nickell bias does not diminish with an increase in the number of individuals (N), and only decreases with longer time series (T) increases. Therefore, as T gets large enough, the FE estimator becomes consistent. Even with T = 30, the bias may still be up to 20% of the true coefficient value (cite)


## How to correct for this bias?

Several suggestions to correct for the bias in the FE estimator have been proposed.

For first differencing; with individual FE swept out, a straightforward instrumental variable estimator is available. We may construct instruments for the lagged dependent variable from the second and third lags of y, either in the form of differences or lagged levels. If error term is i.i.d., those lags of y will be highly correlated with the lagged dependent variable (and its difference) but uncorrrelated with the composite error process.

A linear functional relationship
Dynamic left-hand variable
Right-hand variables that are not strictly exogenous: correlated with past and possibly current realisations of the error
Fixed individual effects, implying unobserved heterogeneity
heteroskedasticity and autocorrelation within individual units but not across them

## Estimation with System GMM 

System GMM, introduced by ...., is a GMM approach that estimates a system of equations, one for each time periods. Instruments used for the lagged dependent variable. 

Blundell and Bond (1998)

- Generalized method of moments in which the model is specified as a system of equations, one per time period, where the instruments applicable to each equation differ (for instance, in later time periods, additional lagged values of the instruments are available)

Simultaneously estimating the system of equations using both levels and differences of the variables. It utilizes moment conditions derived from the system of equations to construct efficient instruments and estimate the parameters consistently.

Lagged levels as well as lagged differences (= System GMM). Difference GMM is original estimator with only lagged levels. 

{{% tip %}}
GMM = 
Difference GMM uses lagged levels of the dependent variable as instruments, while System GMM combines lagged levels and differences as instruments
tip
{{% /tip %}}


### Two-step System GMM

The two-step system GMM estimation process involves first-differencing the variables to eliminate individual fixed effects and then instrumenting the differenced equations using lagged levels and differences of the variables. This approach addresses endogeneity concerns by using lagged variables as instruments, exploiting the orthogonality conditions provided by the system of equations. 

## Instrument validity


Instrument validity is crucial in System GMM estimation. Instruments must be:
- Relevant: Highly correlated with the endogenous variables they instrument. 
- Exogenous: Uncorrelated with the composite error term. 

https://www.sciencedirect.com/science/article/abs/pii/S1048984322000765


## Example in R


- Adapt example from here: https://rdrr.io/cran/plm/man/pgmm.html
- Interpretation of output
- Tests and diagnostics: Sargan test, AR test for autocorrelation of residuals

Inequality

OLS: lagged dep. var positively correlated with the error, biasing its coefficient upward
FE: coefficient biased downward due to negative sign on v_t-1 in the transformed error.

Consistent estimates should lie between these two values, which might be a useful check.
Check whether coefficient of lag dependent variable is sensitive to lag length.


## Tests or diagnostics
- Sargan-Hansen test
- Sargan; instrument validity
- AR test for autocorrelation of the residuals. 

By construction, the residuals of the differenced equation should possess serial correlation, but if the assumption of serial independence in the original errors is warranted, the differenced residuals should not exhibit significant AR(2) behavior. If a significant AR(2) statistic is encountered, the second lags of the endogenous varialbes will not be appropriate instruments for their current values. 

Only use 2-5 lags in constructing the GMM instruments, otherwise possible loss of efficiency

- While DPD estimator are linear estimators, highly sensitive to the particular specification of the model and its instruments. 


Link : 
http://fmwww.bc.edu/EC-C/S2013/823/EC823.S2013.nn05.slides.pdf

{{% summary %}}

A Nickell bias arises as a consequence of correlation of the lagged dependent varible with the error term by construction. Standard panel data estimators (FE, RE, FD) will be inconsistent, especially in analysis with short time series (T) and large number of individuals (N). 








{{% /summary %}}
