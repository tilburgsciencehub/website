---
title: "Introduction to Synthetic Control Methods"
description: "This article provides an introduction to synthetic control methods and an illustration on how to implement them in R"
keywords: "causal, inference, econometrics, model, treatment, effect, control, synthetic"
draft: false
weight: 1
author: "Virginia Mirabile"
---

## Overview 

Synthetic control methods are statistical techniques used in the field of econometrics and causal inference to estimate the effect of an intervention or treatment in comparative case studies (research approach that involves the systematic comparison of two or more subjects). The method creates a synthetic version of the treatment group from a weighted combination of units in a control group, aiming to mimic what would have happened to the treated unit if the intervention had not occurred. 
This empirical method has gained popularity and is widely applied in empirical research in economics and the social sciences due to it's transparency and flexibility. Specifically, the method clearly shows how the synthetic control is constructed, making the results interpretable and can handle complex scenarios where traditional methods may fail. 

In this article we will delve into the fundamental concepts, implementation steps, and applications of synthetic control methods.

## Theoretical Foundations

This section will cover the explanation of the basic econometric principles behind synthetic control methods.

{{<katex>}}
{{</katex>}}

Setting: (notation follows professor [Alberto Abadie](https://conference.nber.org/confer/2021/SI2021/ML/AbadieSlides.pdf))

In the synthetic control method, the comparison unit is chosen as the weighted average of all potential control units to most closely match the characteristics of the treated unit(s).

The idea is to construct a combination of similar untreated units (often referred to as the “donor pool”) to create a synthetic control that closely resembles the treatment subject and conduct counterfactual analysis with it.

- Suppose that we observe $J + 1$ units in periods $1, 2, \ldots, T$.
- Unit "one" is treated during periods $T_0 + 1, \ldots, T$.
- The remaining $ J $ units are an untreated reserve of potential controls (a "donor pool").
- Let $Y_{it}^I$ be the outcome that would be observed for unit $ i $ at time $ t $ if unit $ i $ is exposed to treatment in periods $T_0 + 1$ to $T$.
- Let $Y_{it}^N$ be the outcome that would be observed for unit $ i $ at time $ t $ in the absence of the intervention. This variable is going to be constructed synthetically. 

We aim to estimate the effect of treatment on the treated unit: 

$
\tau_{1t} = Y_{1t}^I - Y_{1t}^N = Y_{1t} - Y_{1t}^N
$

for $t > T_0$, where $Y_{1t}$ is the observed outcome for treated unit. 

In order to create the synthetic control unit, we have to find appropriate weight for each donor in the donor pool by finding: 

- $\mathbf{W}' = (w_2, \ldots, w_{J+1})'$ with $w_j \geq 0$ for $j = 2, \ldots, J + 1$
- And $w_2 + \cdots + w_{J+1} = 1$. 
- Each value of $\mathbf{W}'$ represents a potential synthetic control.

The synthetic control has to be as similar as possible to the treatment unit before intervention, hence, the optimal synthetic control units have to be chosen to satisfy the following condition: 

- The vector $\mathbf{W'} = (w_2', \ldots, w_{J+1}')$ is chosen to minimize $||\mathbf{X}_1 - \mathbf{X}_0 \mathbf{W}||$, subject to our weight constraints.
- Where $\mathbf{X}_1$ be a $(k \times 1)$ vector of pre-intervention characteristics for the treated unit. 
- Similarly, let $\mathbf{X}_0$ be a $(k \times J)$ matrix of pre-intervention characteristics for the untreated units.

Let $Y_{jt}$ be the value of the outcome for unit $j$ at time $t$. 

For a post-intervention period $t$ (with $t \geq T_0$) the treatment effect with the synthetic control estimator is:

$
\hat\tau_{1t} = Y_{1t} - \sum_{j=2}^{J+1} w_j^{'} Y_{jt}
$

Now that we have set a basis for the theoretical aspect of synthetic control methods, let's dive into the implementation in R. 

## Implementation in R 

The implementation steps follow [this](https://github.com/edunford/tidysynth/blob/master/README.md). 

The package we are going to be using is called *tidysynth*, with functionalities specific for the implementation of this method. 

Let's start with installing and loading the package. 

{{% codeblock %}}
```R
install.packages('tidysynth')
library(tidysynth)
```
{{% /codeblock %}}

The dataset we are going to use in this tutorial is the *smoking* dataset, based on the paper by Abadie et al. (2010), which evaluates the impact of tobacco control program on cigarette consumption in California.

{{% codeblock %}}
```R
require(tidysynth)
data("smoking")
View(smoking)
```
{{% /codeblock %}}

The method aims to generate a synthetic California using information from a subset of control states (the “donor pool”) where a similar law was not implemented. The donor pool is the subset of case comparisons from which information is borrowed to generate a synthetic version of the treated unit (“California”). 

{{% codeblock %}}
```R
smoking_out <-
  
  smoking %>%
  
  # initiate the synthetic control object
  synthetic_control(outcome = cigsale, # outcome
                    unit = state, # unit index in the panel data
                    time = year, # time index in the panel data
                    i_unit = "California", # unit where the intervention occurred
                    i_time = 1988, # time period when the intervention occurred
                    generate_placebos=T # generate placebo synthetic controls (for inference)
                    ) %>%
  # Generate the aggregate predictors used to fit the weights (in our example referred to as W')
  
  # average log income, retail price of cigarettes, and proportion of the
  # population between 15 and 24 years of age from 1980 - 1988
  generate_predictor(time_window = 1980:1988,
                     ln_income = mean(lnincome, na.rm = T),
                     ret_price = mean(retprice, na.rm = T),
                     youth = mean(age15to24, na.rm = T)) %>%
  # average beer consumption in the donor pool from 1984 - 1988
  generate_predictor(time_window = 1984:1988,
                     beer_sales = mean(beer, na.rm = T)) %>%
  
  # Lagged cigarette sales 
  generate_predictor(time_window = 1975,
                     cigsale_1975 = cigsale) %>%
  generate_predictor(time_window = 1980,
                     cigsale_1980 = cigsale) %>%
  generate_predictor(time_window = 1988,
                     cigsale_1988 = cigsale) %>%
  
   # Generate the fitted weights for the synthetic control
  generate_weights(optimization_window = 1970:1988, # time to use in the optimization task
                   margin_ipop = .02,sigf_ipop = 7,bound_ipop = 6 # optimizer options
  ) %>%
  
  # Generate the synthetic control
  generate_control()
```
{{% /codeblock %}}

Once the synthetic control is generated, one can easily assess the fit by comparing the trends of the synthetic and observed time series. The idea is that the trends in the pre-intervention period should map closely onto one another. Let's verify that with a graph: 

{{% codeblock %}}
```R
smoking_out %>% plot_trends()
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/1_synthetic.png" width="700">
</p>

As you can see, the pre-intervention trend between synthetic and observed cigarette sales is the same. 

To capture the causal quantity (i.e. the difference between the observed and counterfactual), one can plot the differences using plot_differences(): 

{{% codeblock %}}
```R
smoking_out %>% plot_differences()
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/2_synthetic.png" width="700">
</p>

Another useful way of evaluating the synthetic control is to look at how comparable the synthetic control is to the observed covariates of the treated unit by means of the following code: 

{{% codeblock %}}
```R
smoking_out %>% grab_balance_table()
```
{{% /codeblock %}}
 
## Advantages and limitations 

According to Abadie (2021), the advantages of synthetic control methods are: 

- SCMs provide a systematic way to estimate the effects of interventions when randomized controlled trials are not feasible. 
- SCMs offer a transparent and data-driven method to construct the control group, which is based on observable characteristics and pre-treatment outcomes.
- SCMs are flexible and can be applied in a wide range of contexts. 

Possible disadvantages include: 

- SCMs require extensive data on pre-treatment characteristics and outcomes for both treated and potential control units. 
- The results of SCMs can be sensitive to the choice of predictor variables and the weighting scheme.
There can be considerable variability in estimates depending on the specification of the synthetic control model.
- Constructing synthetic controls can be computationally intensive, especially with large datasets or complex models.

## Summary 

{{% summary %}}

- Synthetic control methods (SCMs) are statistical techniques used to estimate the effect of interventions by creating a synthetic version of the treatment group from a weighted combination of control units.
- SCMs provide a transparent, data-driven approach for constructing control groups, making them suitable for contexts where randomized controlled trials are not feasible.
- While SCMs offer flexibility and systematic estimation, they require extensive pre-treatment data and can be sensitive to model specifications and computationally intensive.

{{% /summary %}}


### References 

Abadie, Alberto. 2021. "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects." Journal of Economic Literature, 59 (2): 391-425. https://www.aeaweb.org/articles?id=10.1257/jel.20191450
DOI: 10.1257/jel.20191450

Alberto Abadie, Alexis Diamond & Jens Hainmueller (2010) Synthetic
Control Methods for Comparative Case Studies: Estimating the Effect of California’s Tobacco
Control Program, Journal of the American Statistical Association, 105:490, 493-505, DOI:
10.1198/jasa.2009.ap08746

Code snippets from: https://github.com/edunford/tidysynth/blob/master/README.md
