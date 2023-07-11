---
title: "Local Randomization Approach"
description: "The local randomization approach to regression discontinuity analysis: an introduction, example, estimation and inference"
keywords: "regression, discontinuity, local, randomization, approach, example, estimation, inference"
date: 2023-07-10
weight: 6
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /regression/discontinuity
  - /local/randomization
  - /estimation/inference
---

## Introduction
Local randomization approach introduces the idea that the RD design can be interpreted as a randomized experiment near the cutoff. This can be a complement and robustness check to the [continuity based analysis](https://tilburgsciencehub.com/building-blocks/analyze-data/regression-discontinuity/continuity-rd/). 

This approach imposes certain conditions so that units who are in a small window around the cutoff are comparable to each other and are studies as if they are randomly assigned to treatment or control.

Depending on the nature of the running variable, one can choose whether to use the continuity-based approach or the local randomization approach. If the variable is discrete, the local randomization approach does not impose strong assumptions and can be used for estimation and inference. However, if the variable is continuous, the local randomization requires stronger assumptions than the continuity-based approach, thus it is better to use the latter for the main RD analysis and the former as a robustness check.

The main assumption throughout the building block is that the RDD is sharp and the compliance is perfect. Another assumption we make is called *as if random assignment*. This means that there is a small window around the cutoff, $W = [c-w, c+w]$, such that for units with scores that fall in that interval, their placement above or below the cutoff is assigned as it would have been assigned in a random experiment.

The main feature of a randomized experiment is that due to the randomly generated number, the running variable is unrelated to the average potential outcomes. 

<p align = "center">
<img src = "../images/local-rand.png" width="500">
</p>

The above graphs compare a randomized experiment (left graph) with a continuity-based design (right graph). Due to the randomly generated number, {{<katex>}} \mu_{1}(x) = \mathbb{E}[Y_{i}(1)|X_{i}=x]  {{</katex>}} and $\mu_{0}(x) = \mathbb{E}[Y_{i}(0)|X_{i}=x]$ are constant for all $x$ values, as shown in graph (a). 

Therefore, another assumption that needs to be met is that the value of the score within the defined window is unrelated to the potential outcomes.

{{% summary %}}
The local randomization approach needs to fill two conditions:
- The joint probability distribution of scores within $W$ is known
- The potential outcomes are not affected by the score within $W$.
{{% /summary %}}

### Notations

The probability is defined as {{<katex>}}\mathbb{P}_{W}[.]{{</katex>}} for those units with $X_{i}\in W$. As such, the first condition requires that {{<katex>}}\mathbb{P}_{W}[X_{W} \leq x] = F(x){{</katex>}} for some known joint cumulative distribution function $F(x)$.

For the second condition, let $Y_{i}(0,x)$ and $Y_{i}(1,x)$ be the potential outcomes with explicit dependence on the score variable, so that $Y_{i}(0) = Y_{i}(0, X_{i})$ and $Y_{i}(1) = Y_{i}(1, X_{i})$. As such, if the potential outcomes are non-random, the second condition means that $Y_{i}(0,x') = Y_{i}(0, X_{i})$ and $Y_{i}(1,x') = Y_{i}(1, X_{i})$ for all $x$, $x' \in W$ and all units such that $X_{i} \in W$. If the potential outcomes are non-random, the condition becomes {{<katex>}}\mathbb{P}_{W}[Y_{i}(0,x') = Y_{i}(0,x)] = 1 {{</katex>}} and {{<katex>}}\mathbb{P}_{W}[Y_{i}(1,x') = Y_{i}(1,x)] = 1 {{</katex>}} for all $x$, $x' \in W$. 

## Estimation and Inference

### Fisherian Inference

Since in many RD cases a local randomization assumption is only plausible in a very small window around the cutoff, it means that this window will most likely contain few observations. For this case, a Fisherian inference approach is appropriate, as it is valid in any finite sample and leads to correct inferences even with small samples. 

With the Fisherian approach, the potential outcomes are fixed or non-stochastic. The null hypothesis, also called the *sharp null hypothesis* is:
{{<katex>}} H^F_{0}: Y_{i}(0) = Y_{i}(1) {{</katex>}} for all $i$.

The sharp null hypothesis with the non-stochastic potential outcomes lead to inferences that are (type I error) correct for any sample size, since under $H^F_{0}$ the observed outcome of each unit is equal to the unit's potential outcomes ($Y_{i} = Y_{i}(1) = Y_{i}(0)$) and there is no missing data.   

### Neyman and Super-population Estimation and Inference

Although the window around the cutoff is small, some RD applications can have many observations in these windows. The Fisherian inference method would still work well and be valid, but there are some large sample methods that provide consistent point estimators. 

Both the Neyman and Super-population are large sample methods, and they require that the number of observations within the window are large enough. 

An overview of the mentioned statistical methods is present below:

|  | Fisher | Neyman | Super-population |
| --- | --- | --- | --- |
|Sampling| None | Urn model | i.i.d. |
|Potential Outcomes | Non-random | Non-random | Random |
|Sample size| Fixed | Large | Large |
|Null hypothesis| Sharp | Non-sharp | Non-sharp |
|Inferences| Exact | Approximate | Approximate | 

In the Neyman method, the potential outcomes are non-stochastic, so all parameters are conditional on the potential outcomes. The "urn model" of assignment entails that there is one urn per treatment condition and each urn has the potential outcomes that correspond to that treatment condition for each unit.

In the Super-population method, units are assumed to be drawn from a larger population using independently and identically distributed sampling (i.i.d.). This results in the potential outcomes being random variables, not fixed quantities.

For all three methods, the parameter of interest is {{<katex>}} \mathbb{E}_{W}[.] {{</katex>}}, denoting the expectation computed with respect to the probability {{<katex>}}\mathbb{P}_{W} {{</katex>}}. 

In a Neyman framework, the average treatment effect is :
$$\theta_{SRD} = \frac{1}{N_{W}} \sum_{i:X_{i} \in W} [Y_{i}(1) - Y_{i}(0)]$$

In the Super-population framework, the average treatment effect is:
$$\theta_{SRD} = \mathbb{E}[Y_{i}(1) - Y_{i}(0)|X_{i} \in W]$$

$\theta_{SRD}$ is different from the continuity-based parameter $\tau_{SRD}$, because the former is an average effect inside the window, while the latter is an average at the cutoff point.

## Estimation and Inference in Practice

### Example

To illustrate the theory we use the example of US Senate elections. The example studies the effect of winning elections on future vote shares. There is a discontinuous relationship between the incumbency status of a political party and the vote share obtained in an election. This means that when there are two parties that compete for a seat, the party with just above 50% of the vote wins and becomes the incumbent, while the other loses. 

Here, the unit of analysis is the US state and the score is the Democratic party's margin of victory at election $t$ (the margin is the difference between the vote share of the Democratic party and the vote share of its strongest opponent).
The variables are defined as follows:
- $Y$ - vote share obtained by the Democratic party in the election in a given state
- $X$ - margin of victory of the Democratic party
- $T$ - electoral victory of the Democratic party, being equal to 1 if they won and 0 otherwise

### Coding

The R library for local randomization is `rdlocrand`, from which we use the function `rdrandinf`. The main parameters of the function are the outcome variable $Y$, the running variable $X$ and the bounds of the window: `wr` (right bound), `wl` (left bound). For now we set them to -2.5 and 2.5. 

{{% codeblock %}}

```R
out <- rdrandinf(Y, X, wl = -2.5, wr = 2.5, seed = 50)
summary(out)
```
{{% /codeblock %}}

_Output_:

<p align = "center">
<img src = "../images/output1.png" width="400">
</p>

The output shows that there are 1297 observations in total, with a default polynomial order of 0 and a uniform kernel. It also shows that there are 1000 simulations used, the null hypothesis tested (by default $\tau_{0} = 0$) and the randomization mechanism is by default fixed margins randomization. 

{{% tip %}}
Kernel type can be changed with the argument `kernel`.

Number of simulations can be changed with the `reps` argument.

{{% /tip %}}

The middle part of the output shows the distribution of the observations left and right of the cutoff. There are 595 control and 702 treated observations, but in the chosen window there are only 63 elections below the cutoff and 57 above.

The difference in means of 9.167 means that this is the difference between a Democratic vote share of 53.235% (mean of outcome above cutoff) in elections where this party barely wins, and 44.068% (mean of outcome below cutoff) in elections where the Democratic party barely loses.

The p-value shows that we can reject the null hypothesis.

### How to choose the window

Manually choosing the window lacks transparency and objectivity. The `rdlocrand` library contains the function `rdwinselect` which selects a window. It takes as argument the score variable $X$ and a matrix of predetermined covariates. We can also set the number of simulations to 1000 by using `reps`. Additionally, one can use `wstep` to increase the length of the windows in fixed steps, or `wobs` to increase the window length so that the observations number increases by a minimum fixed amount every step. `wobs` = 2 means that at least 2 observations are added on each side of the cutoff in every step.

{{% codeblock %}}

```R
out <- rdwinselect(X, Z, seed = 50, reps = 1000, wobs = 2)
summary(out)
```
{{% /codeblock %}}

_Output_:

<p align = "center">
<img src = "../images/output2.png" width="400">
</p>

The output shows that the optimum window is [-0.7652, 0.7652]. 

The function only shows the first 20 windows, but we can increase it by using the argument `nwindows`.

## See also
[A Practical Introduction to Regression Discontinuity Designs: Extensions - Cattaneo, Idrobo & Titiunik (2023)](https://rdpackages.github.io/references/Cattaneo-Idrobo-Titiunik_2023_CUP.pdf)