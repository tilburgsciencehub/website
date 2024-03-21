---
title: "The Concept and Motivation of Causal Inference"
description: "This building block motivates causal inference and provides theoretical background for all the practical methods you can find in this section."
keywords: "causal, inference, econometrics, regression, model, potential, outcomes, framework, treatment, effect, control, ATE, ATT"
draft: false
weight: 1
author: "Valerie Vossen"
aliases:
  - /causal-inference
  - /causal-inference-introduction
  - /causal-inference-intro
---

## Overview

Causal inference became a very important topic in quantitative social sciences, and means to estimate the impact of something on a specific outcome, by understanding the causal relationship. 
Unlike correlation, which only indicates a statistical relationship between variables, causal inference aims to determine if one variable directly influences another. It's essential to recognize that correlation does not imply causation; just because two variables are correlated does not mean that one causes the other. Note that causal relationships can also exist without observable correlation. 

{{% summary %}}
Causal inference methods are crucial for identifying and understanding causal effects in data. This topic introduces causal inference, navigate to the "Causal Inference" section for extensive content on the following methods:

- Regression Discontuinity Designs (RDD)
- Difference in Difference
- Panel Data
- Instrumental Variables
{{% /summary %}}


<p align = "center">
<img src = "../images/corr_cause.png" width="700">
<figcaption> Source: xkcd (https://xkcd.com/552/) </figcaption>
</p>

## Potential Outcomes Framework

{{<katex>}}
{{</katex>}}

The **potential outcomes** framework is central to understanding causal inference and the role of randomization. In this framework, each unit has two potential outcomes: 
- $Y_i^1$ if the unit receives treatment and
- $Y_i^0$ if it did not

The observable outcome $Y_i$ is determined by a switching equation:

$$
Y_i = D_i Y_i^1 +(1-D_i) Y_i^0
$$

Here, $D_i$ is the treatment indicator, taking the value 1 if the unit is treated and $0$ if not. This equation indicates that:
- When $D_i = 1$, the observable outcome $Y_i$ is $Y_i^1$ and
- when $D_i = 0$, the observable outcome $Y_i$ is $Y_i^0$.

The core of causal inference lies in comparing these potential outcomes. 

To know the individual treatment effect, you would want to take the difference $Y_i^1$ - $Y_i^0$. However, this is not possible since only one of these outcomes is observed. This challenge arises from the unobserved counterfactual: we cannot see what would have happened under the alternative scenario.


### Average Treatment Effect

From individual to *Average Treatment Effect (ATE)*, the same intuition stays. The ATE is the difference between the potential outcomes if all unit receive treatment and the potential outcomes when no units receive treatment. 
In mathematical terms:

<div style="text-align: center;">
{{<katex>}}
ATE = E[\delta_i] \\
= E[Y_i^1- Y_i^0]\\
= E[Y_i^1]-E[Y_i^0]\\
{{</katex>}}
</div>

However, the ATE cannot be calculated since you can only observe one both potential outcomes. The counterfactual can only be estimated!

tip?
- Average Treatment Effect on the Treated
- Average Treatment Effect for the Untreated
tip


## Randomization

Randomization is key to isolating causal effects.

...

By randomly assigning some units to treatment and some units to control, and the mean of a random sample from the population of units is then an unbiased estimator for the mean of the population. The *counterfactual* is based on random selection into treatment. 

## Selection bias

If a treatment group is NOT randomly selected, selection bias (omitted variable bias) arises. This means the treatment group would have a different outcome than the control group even if they did not receive treatment. As a consequence, the estimated effect is over-or underestimated. 

|                 | Untreated (\$Y_i^0\$)     | Treated (\$Y_i^1\$)     |
| --------------- | ---------------------- | ---------------------- |
| Control group (\$D_i = 0\$)    | \$E(Y_i^0\|D_i = 0)\$   | \$E(Y_i^1\|D_i = 0)\$   |
| Treatment group (\$D_i=1\$)    | \$E(Y_i^0\|D_i = 1)\$   | \$E(Y_i^1\|D_i = 1)\$   |


The Untreated Outcome of the Treatment Group and the Treated outcome of the Control group are unknown. 


Unit causal effect + selection bias = 

\$E(Y_i^1\|D_i = 1)\$  - \$E(Y_i^0\|D_i = 1)\$ + ( \$E(Y_i^0\|D_i = 1)\$ - \$E(Y_i^0\|D_i = 0)\$)


In words:
1. Unit causal effect: Difference in outcome for treated units treated - not treated
2. selection bias: Difference in treatment and control group while both not treated.


## Example with numbers












