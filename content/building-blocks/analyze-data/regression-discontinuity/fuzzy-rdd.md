---
title: "Fuzzy RD Designs"
description: "Foundations of regression discontinuity - the fuzzy design"
keywords: "regression, discontinuity, fuzzy, designs"
date: 2023-06-21
weight: 4
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /fuzzy/designs
  - /regression/discontinuity
---

## Introduction

In all regression discontinuity designs, the treatment assignment takes place according to the rule $T\_{i} = \mathbb{1}(X_{i} >= c)$. Unlike the [Sharp RDD](https://tilburgsciencehub.com/building-blocks/analyze-data/regression-discontinuity/sharp-rdd/) where the treatment compliance is perfect (all units assigned to the treatment actually receive the treatment, while no units assigned to the control take the treatment), for Fuzzy RD designs, the treatment has **imperfect compliance**. This means that some units that have a score higher than the cutoff fail to receive the treatment or some units with score lower than the cutoff receive the treatment. 

For Fuzzy RD the same treatment assignment rule applies and the probability of receiving treatment still jumps abruptly at the cutoff, it doesn't change from 0 to 1 as it did for Sharp RD. 

## Assigned Treatment vs. Received Treatment

Since the treatment assigned is not always the same as the actual treatment received, we need different notation to distinguish between them. If the treatment assignment is noted with $T\_{i}$, we define the treatment received with $D\_{i}$, also known as **treatment take-up**. Therefore the main characteristic of Fuzzy RDD is that there are some units for which $T_{i} \neq D\_{i}$.

## Fuzzy vs. Sharp RDD

To visualize the difference between fuzzy and sharp RD, we plot {{<katex>}} \mathbb{P}(D_{i} = 1 | X_{i} = x) {{</katex>}} which is the conditional probability of receiving treatment.

<p align = "center">
<img src = "../images/fuzzy-sharp.png" width="550">
<figcaption> Conditional probability of receiving treatment in Sharp vs. Fuzzy RDD </figcaption>
</p>

As seen in the graphs, for sharp RD the probability changes exactly from 0 to 1 at the cutoff, while for fuzzy RD the probability is always less than 1.

$D_{i}$ has two values:
- $D_{i}(1)$: treatment received by $i$ when it is assigned to the treatment condition
- $D_{i}(0)$: treatment received by $i$ when it is assigned to the control condition

For instance, if unit $i$ receives treatment when assigned to the control condition, we then have $D_{i}(0) = 1$. 


The **fundamental problem of causal inference** is now that for each unit we either observe $D_{i}(1)$ or $D_{i}(0)$, but never both. 

## Estimation and Inference Methods

Non-compliance with treatment could occur because some units may decide to take or refuse the treatment, which introduces confounding between potential outcomes and compliance decisions. This can affect learning causal treatment effects for all units, in the absence of additional assumptions. Therefore, we need additional parameters, besides the average treatment effect, that can help with cases on non-compliance.

By applying the Sharp RD estimation strategy to the observed outcome in a Fuzzy RDD we estimate two parameters: $\tau_{Y}$ and $\theta_{Y}$.

$\tau_{Y}$ is estimated by comparing the average outcome of observations just below cutoff to the average outcome of observations just above cutoff, then by taking the limit of the two averages as the score approaches the cutoff. 

$\theta_{Y}$ is obtained by applying a local randomization approach that compares observations in a small window $W$.

There are two strategies using these parameters:
- focus on assumptions that allow for the interpretation of $\tau_{Y}$ and $\theta_{Y}$ as the effect of assigning the treatment on the outcome
- focus on assumptions that allow learning about the effect of receiving the treatment on the outcome

### Intention-to-treat Effects

The focus of the first strategy is to learn about the effects of **the treatment assignment**. The effects of assigning the treatment on any outcome is called *intention-to-treat effects* (ITT). There are two assumptions/approaches that can help obtain the ITT parameters: the continuity-based approach and the local randomization approach. After applying the two, the ITT parameters become:
- $\tau_{Y} = \mathbb{E}[Y_{i}(1) - Y_{i}(0) | X_{i} = c]$ 
- {{<katex>}}\theta_{Y} = \mathbb{E}_{W}[Y_{i}(1) - Y_{i}(0) | X_{i} \in W]{{</katex>}} 

As for the second strategy, the focus is on studying the effects of **receiving the treatment**. The same two parameters are defined, but the outcome variable is now $D$ instead of $Y$. Therefore, the parameters become:

- $\tau_{D} = \mathbb{E}[D_{i}(1) - D_{i}(0) | X_{i} = c]$ 
- {{<katex>}}\theta_{D} = \mathbb{E}_{W}[D_{i}(1) - D_{i}(0) | X_{i} \in W]{{</katex>}} 

### Treatment Effects for Subpopulations

If the goal is to study the effect of the treatment received, the focus is then on the **Fuzzy RD parameters**: 
- $\tau_{FRD} = \tau_{Y}/\tau_{D}$
- $\theta_{FRD} = \theta_{Y}/\theta_{D}$

We can define four groups of units according to the compliance decisions:
- *compliers*: units whose treatments received coincides with their treatment assigned
- *never-takers*: units who always refuse the treatment regardless of their assignment
- *always-takers*: units who always take the treatment no matter their assignment
- *defiers*: units who receive the other treatment to the one they are assigned

**Monotonicity** is the assumption that there are no *defiers* inside $W$ or at or around the cutoff.

### Bandwidth and Window Selection

The bandwidth and window selection procedure for the ITT parameters is the same as described in the [Sharp RDD](https://tilburgsciencehub.com/building-blocks/analyze-data/regression-discontinuity/sharp-rdd/). However, for $\tau_{FRD}$, since it is a ratio, there is the question of whether the bandwidths should be the same for the denominator and numerator or not. If the focus is on the ITT effects ($\tau_{Y}$), then it is better to have different bandwidths for the denominator and numerator. On the other hand, if the focus is on the ratio $\tau_{FRD}$, then the bandwidths should be the same as it adds transparency to the analysis.

## See also
[A Practical Introduction to Regression Discontinuity Designs: Extensions - Cattaneo, Idrobo & Titiunik (2023)](https://rdpackages.github.io/references/Cattaneo-Idrobo-Titiunik_2023_CUP.pdf)