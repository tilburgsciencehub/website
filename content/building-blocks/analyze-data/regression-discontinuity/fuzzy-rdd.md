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

## Assigned treatment vs. received treatment

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

## See also
[A Practical Introduction to Regression Discontinuity Designs: Extensions - Cattaneo, Idrobo & Titiunik (2023)](https://rdpackages.github.io/references/Cattaneo-Idrobo-Titiunik_2023_CUP.pdf)