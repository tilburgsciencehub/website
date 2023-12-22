---
title: "The Shift-Share Instrumental Variable"
description: "The Shift-share IV is an innovative approach to address endogeneity and selection challenges in regression analysis."
keywords: "instrumental, variable, iv, shift-share, shiftshare, regression, causal, inference, effect, regressions, analysis"
draft: false
weight: 3
author: "Valerie Vossen"
aliases:
  - /shiftshare
---

# Overview

- Motivation
- The shift-share instrument
- Assumptions
- A practical application: migration case
- Other examples from literature
- Application in R


## Motivation

Analyzing the causal impact of exogenous shocks within regional economic studies will come with challenges. It is often difficult to isolate the true relationships between the variables of interest with normal OLS. Then, endogeneity problems can arise, where the independent variable is correlated with the error term and the coefficients, estimating the relationship you are interested in, are biased. 

### Effect of immigration on unemployment
To illustrate with an example, the following analysis will be us throughout this article:

A typical question asked in economics is the impact of immigration on unemployment. If immigrants are substitutes to natives, immigration inflow is expected to rise unemployment. It might seem straightforward to estimate this effect when you have national panel data on immigration and unemployment rates. You can run the following regression: 

{{<katex>}}
UR_{i,t} = \beta_0 + \beta_1 IM_{i,t} + \beta_2 X_{i,t} + \epsilon_{i,t}
{{</katex>}}
<br>
<br>
where
- $UR_{i,t}$ is the unemployment rate in region $i$, at time $t$
- $IM_{i,t}$ is the immigration inflow (from a specific origin country, or total immigration depending on your research question) to region $i$ in the destination country, at time $t$
- $X_{i,t}$ is a vector of controls, like variables for GDP growth or educational level in each region $i$, at time $t$
- $\epsilon_{i,t}$ is the error term


### Problem: Endogeneity of the independent variable
However, there is a concern with this specification. Endogeneity arises if immigration to each region is itself driven by regional unemployment rates. This reasoning makes sense: immigrants, seeking opportunities, are likely to grativate towards regions which lower unemployment rates. If this is true, there is reverse causality (unemployment affects immigration which is the other way around). The estimated effect of immigration on the unemployment rate will be biased. 

A shift-share instrument (also called Bartik instrument) can be used to help solve this issue. In short, the shift-share IV decomposes changes in economic variables within regions into two components which are both assumed to be **exogenous**: the shift and the share. Together, the shift and the share can exogenously predict immigration inflows.

## The shift-share instrument

The essence of the shift-share instrument is that it deconstructs changes in economic variables within regions into two distinct components: the shift and the share. 

The predicted inflow of migrants into a destination country is a weighted average of the national inflow rates from each country (*shifts*), with weights depending on the initial distribution of immigrants (*shares*). In other words, the instrument combines the past settlement and national inflow.

{{<katex>}}
z_{i,t} = \sum_{i=1}^I s_{i,t-1} * m_{t}
{{</katex>}}  
<br>
Where:

- The share $s_{i,t-1}$: The lagged or "initial" distribution of the share of immigrants in region $i$.

- The shift $m_{j,t}$: The national immigration inflow. Note that the shifts vary at a "higher" level than the shares, namely the shifts are national and not varying at regional level $i$ like the shares. 

### The regression model

The shift-share instrument $z_{i,t}$ is used as to estimate $\beta_1$ in the following regression model:
<br>
<br>
{{<katex>}}
UR_{i,t} = \beta_0 + \beta_1 z_{i,t} + \beta_2 X_{i,t} + \epsilon_{i,t}
{{</katex>}}
<br>

The shift-share instrument exogenously predicts the endogenous shift (the immigration inflow into each region).

## Instrument validity
For the shift-share instrumental approach to work, instrument exogeneity should hold. On average, the product of the instrument, $z_{i,t}$, and the error term $\epsilon_{i,t}$ balance out to zero. This is the following condition in mathematical terms:

{{<katex>}}
E[\frac{1}{I} \sum_{i} z_{i,t} \epsilon_{i,t}] = 0
{{</katex>}}

## Identifying assumptions

There are two recent views in literature about which assumptions should hold for the shift-share IV to be valid: the share- and the shift-view. 

### Share-view 

[Goldsmith-Pinkham et al. (2020)]() show that the shift-share instrument is equivalent to using the shares as instruments, and so identification is based on **exogeneity of the shares**. The shares measure the differential exogenous exposure to the common shock ("shift"). The shifts only provide the weights and do not affect the instrument endogeneity.

The identifying assumption is: shares $s_{i,t}$ are exogenous, which is the following condition in mathematical terms:

$E[\epsilon_{t} | s_{i,t} ] = 0$ for each $t$

In our migration example, this implies arguing whether the past settlement (initial distribution) of migrants can assumed to be uncorrelated with the local unemployment rates (the dependent variable).

{{% tip %}}
Some strategies to explore the validity of this share exogeneity assumption:

- A balance test: Identify the correlation between the *shares* and potential confounders. In the migration example, you could for example examine whether areas with higher initial immigrant shares also display distinct characteristics (such as higher education levels) that might affect the unemployment rate.
- A pre-trend test: If you have a pre-period, test for parallel pre-trends.
- Overidentification test
{{% /tip %}}

### Other assumptions

- **Absence of spatial spillover effects**

Absence of spatial spillovers and interdependencies between locations means that the outcomes in one location are not influenced by the outcomes in neighboring regions, ensuring the independence of observations. This assumption is not straightforward: If local workers respond to immigration inflow by moving to other regions, domestic migration is likely to overestimate the negative effect of immigration on unemployment rates in each region. 

- **Independent data periods**

The instrument's validity assumes that the data represent distinct periods without significant intertemporal correlations that might confound the estimation. This  assumption of steady-state is important, especially in considering adjustment dynamics.

### Shift (Shock) view

Another approach is introduced by [Borusyak, Hull, and Jaravel (2022)]() in which identification follows from the quasi-random assignment of shocks, while exposure shares are allowed to be endogenous. The two baseline assumptions are

- **Quasi-random shift assignment**

$E[m_{t} | \bar{\epsilon}, s] = \mu$ for all $t$

Each shift has the same expected value, conditional on the shift-level unobservables $\bar{e_{t}}$, and average
exposure $s_{t}$. 

-  **Many uncorrelated shifts**

This assumption implies that when there are many regions, the shifts are becoming increasingly uncorrelated to each other. Mathematically, this is represented as the covariance between the shifts in one region and the shifts in another region becoming close to zero when comparing different regions.

$Cov(m_t, m_t' | \bar{\epsilon}, s) = 0$ for all $m' \neq m$


## Other practical examples in literature

Note: the instrument is $z_{l} = \sum_{n} s_{l,n} * m_{n}$ where shifts (shocks) vary at another level (`n`) than the shares (`l`), and outcome and treatment are observed at level `l`.

| Context                                        | Shift-Share Instrument                                | Authors                                    |
|-------------------------------------------|----------------------------------------------------|--------------------------------------------------|
| Employment's impact <br> on wage growth <br> in region `l` | *Predicted employment due to <br> national industry trends* <br><br> **Shifts:** National growth of industry `n` <br> **Shares:** Lagged employment <br> shares of industry in region `l` | [Bartik (1991)](); <br> [Blanchard & <br> Katz (1992)]()  |
| Local labor market effects <br> of rising Chinese import <br> competition in the US | *Predicted growth of <br> import competition* <br><br> **Shifts:** Growth of China exports <br> in manufacturing industry `n` <br> **Shares:** 10-year lagged <br> employment shares over total <br> employment in region `l` | [Autor, Dorn, <br> and Hanson <br> (2013)](https://www.aeaweb.org/articles?id=10.1257/aer.103.6.2121)  |
| Import impact by <br> Danish firm on wages  | *Predicted change in firm inputs <br> via transport costs*<br><br> **Shifts:** Changes in transport <br> costs by `n` = (product, country) <br> **Shares:** Lagged import shares  | [Hummels <br> et al. (2014)]()  |


## Practical example in R

The code block illustrates an estimation of the second literature example in the table above (Autor, Dorn, and Hanson, 2013), with use of the [`ShiftShareSE` package](https://cran.r-project.org/web/packages/ShiftShareSE/ShiftShareSE.pdf). The data set (`ADH`) is already included in the package. The `ivreg_ss()` function is used to estimate a regression model with the shift-share instrument.

{{% codeblock %}}
```R
# Install and load the ShiftShareSE package
install.packages("ShiftShareSE")
library(ShiftShareSE)

# Estimate the shift-share instrumental variable regression
ivreg_ss(d_sh_empl ~ 1 | shock, 
          X=IV, 
          data=ADH$reg, 
          W=ADH$W,
          method=c("ehw", "akm", "akm0")
          )

```
{{% /codeblock %}}

The first part represents the formula:
  - `d_sh_empl`, the dependent variable; the change in the share of the working-age population
  - No controls are added, thus the `controls` term equals `1`.
  - `shock` is the endogenous regressor and represents the local China imports. 
  - The instrument used to replace `shock` is `IV`: This is the shift-share vector, with length N of sectoral shocks, aggregated to regional level using the share matrix W
- `W` is a matrix of sector shares (the weights)
- `method` specifies which inference methods to use

<p align = "center">
<img src = "../images/shiftshare_r.png" width="400">
<figcaption> Regression output </figcaption>
</p>

# References
- shiftshare mixtape
- any papers?
- https://blogs.worldbank.org/impactevaluations/rethinking-identification-under-bartik-shift-share-instrument


