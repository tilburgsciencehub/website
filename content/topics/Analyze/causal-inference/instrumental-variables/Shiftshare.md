---
title: "The Shift-Share Instrumental Variable"
description: "The Shift-share IV is an innovative approach to address endogeneity and selection challenges in regression analysis."
keywords: "instrumental, variable, iv, shift-share, shiftshare, regression, causal, inference, effect, regressions, analysis"
draft: false
weight: 1
author: "Valerie Vossen"
aliases:
  - /shiftshare
---

# Overview

- Motivation
- The shift-share instrument
- Assumptions
- A practical application: effect immigration on unemployment
- Other examples from literature
- Application in R


## Motivation

Analyzing the causal impact of exogenous shocks within regional economic studies, will come with challenges
Think of endogeneity, making it difficult to isolate the true relationships between the variables of interest with normal OLS. 

To illustrate this challenge, and the shift-share instrument, we will use the following analysis as an example throughout this article:

A typical question asked in economics is the impact of immigration on unemployment. It seems straightforward to estimate this effect when you have national panel data on immigration and unemployment rates. You can run the following regression: 

unemploymentrate_{i,t} = beta_0 + beta_1 * immigrationinflow_{i,t} + controls + e_{i,t}


### Problem: Endogeneity of the independent variable
However, there is a typical concern with this specification. Endogeneity arises if immigration might itself be driven by regional unemployment rates. This makes sense: immigrants, seeking opportunities, are likely to grativate towards regions which lower unemployment rates.

This is a reverse causality problem, and the estimated effect of immigration on the unemployment rate will be biased. 

A shift-share instrument can be used as an instrument, to help solve this issue. it decomposes changes in economic variables within regions into two components which are both assumed to be exogenous: the shift and the share. Together the shift and the share can exogenously predict immigration inflows.


## The shift-share instrument

The essence of the shift-share instrument is that it deconstructs changes in economic variables within regions into two distinct components: the shift and the share. 

The predicted inflow of migrants into a destination country is a weighted average of the national inflow rates from each country ("the shift"), with weights depending on the initial distribution of immigrants ("the shares"). 

{{<katex>}}
z_{i,t} = sum_i z_{i,j,t-1} m{j,t}
{{</katex>}}  

- z are the lagged or "initial" distribution of the share of immigrants from source country j in location i.

- m is the normalized change in immigration from country j into the country as a whole. 


The shocks vary at a different "level" j = 1,...,J than the shares i = 1,...,I, where we also observe an outcome y_i and treatment x_i

z_{i,t} is used as an estimator in the model y_{i,t} = beta*x_{i,j,t} + epsilon_{i,j,y}, where it exogenously predicts the endogenous shift. 

sum_n s_ln = 1 for all l. 

maths: until slide 45

## Assumptions

Properties of shocks and shares to make this condition hold. 

1. Exogeneity of initial shares

Initial shares of immigrants across locations are exogenous or independent from the outcomes being studied. 


## shift exogeneity

1. Quasi-random shock assignment

Each shift has the same expected value, conditional on the shift-level unobservables e_n, and average exposure s_n. 


 
2. Many uncorrelated shocks

Share exogeneity assumes that the shocks affecting one region are unrelated or uncorrelated with the shocks affecting other regions, given the unobservable factors

The aspect highlighted, where the expected Herfindahl index of average shock exposure converges to zero as the number of regions (N) approaches infinity, implies a situation where shocks become increasingly uncorrelated across regions

### Absence of spatial spillovers

The Bartik instrument's validity assumes that there are no spatial spillover effects or interdependencies among locations. This means that the outcomes in one location are not influenced by the outcomes in neighboring regions, ensuring the independence of observations. This is not straightforward in our example: If local workers respond to immigration inflow by moving to other regions, domestic migration is likely to overestimate the negative effect of immigration on unemployment rates in each region. 

### Independent data periods

The assumption of steady-state or independence among data periods is important, especially in considering adjustment dynamics. The instrument's validity assumes that the data represent distinct periods without significant intertemporal correlations that might confound the estimation.




## Immigration on unemployment example



y_l = beta x_l + gamma' x w_l + e_l

where:
- y_l = unemployment in region l
- x_l = immigration

- reverse causality
- need an IV to give a relative labor supply instrument 

instrument = share of migrants predicted from enclaves & recent growth (= past settlement and national inflow?)

chatgpt:
Share of Migrants Predicted from Enclaves: This part of the instrument captures the predicted share of migrants coming to a region based on the historical presence of enclaves (areas with a high concentration of migrants) and recent growth trends.

Recent Growth: Recent growth includes factors like past settlement patterns and national inflow of migrants. It accounts for the changes in the flow of migrants to a region due to factors unrelated to the treatment or policy being studied.

shift = national immigration growht from origin country n
share = lagged shares of migrants from origin n in region 

shift: the national inflow of immigrants
share: past settlement of immigrations in the different regions. Both assumed to have no direct effect on local unemployment rates = exogenous!


## Other practical examples in literature

- labour markets
employment (x) --> wage growth (y)

y_l = beta x_l + gamma' x w_l + e_l

IV = labor demand shifter
 - IV relevance = should be a strong enough predictor for employment
 - IV exogeneity = should not affect wage growth as a direct effect

instrument = predicted employment growth due to national industry trends

- shift (shocks): national growth of industry n
- shares = lagged employment shares (of industry in a region)


# Practical application in R

- package "ShiftShareSE"
ssaggregate? slide 67
- which data for example?

Thesis


# references
- shiftshare mixtape
- any papers?


