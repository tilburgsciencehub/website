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

Causal inference is an important topic in quantitative social sciences, e.g. economics and data science, and refers to the practice of a causal question. Establishing causality, which refers to a cause-and-effect relationship between variables, where changes in one variable cause changes in another variable, requires more than just observing a correlation between two variables. 



However, these relationships are not inherently causal, as the direction of cause and effect may be ambiguous, other variables can influence the relationship, or the observed outcome may be due to chance. While regression analysis provides some insight into the significance of associations, interpreting the results as causal relationships requires additional assumptions and thoughtful study designs.

<p align = "center">
<img src = "../images/corr_cause.png" width="700">
<figcaption> Source: xkcd (https://xkcd.com/552/) </figcaption>
</p>


## Potential Outcomes Framework

{{<katex>}}
{{</katex>}}

The **potential outcomes** framework is the theoretical background of causal inference. In this framework, each unit has two potential outcomes: 
- $Y_i^1$ if the unit receives the treatment
-  $Y_i^0$ if the unit did not receive the treatment.


The observable outcome, denoted by $Y_i$ is determined by a *switching equation*:

$$
Y_i = D_i Y_i^1 +(1-D_i) Y_i^0
$$

$D_i$ is the treatment indicator: it equals $1$ if the unit is treated and $0$ if not. The equation expresses the following:
- When $D_i = 1$, the observable outcome $Y_i$ is $Y_i^1$.
- When $D_i = 0$, the observable outcome $Y_i$ is $Y_i^0$.

The challenge of causal inference lies in the unobserved counterfactual. We can only observe one of these potential outcomes, namely the observable outcome. 


### Average Treatment Effect

We are interested in the *Average Treatment Effect (ATE)*. This is the difference between the potential outcomes if all unit receive treatment and the potential outcomes when no units receive treatment. 

In mathematical terms:

<div style="text-align: center;">
{{<katex>}}
ATE = E[\delta_i] \\
= E[Y_i^1- Y_i^0]\\
= E[Y_i^1]-E[Y_i^0]\\
{{</katex>}}
</div>

## Random assignment of treatment

ATE requires us to know both potential outcomes, but we can only observe on. The counterfactual is unobserved but can be estimated. With randomization, you can estimate the average causal effect, which is the difference between treatment and control group. You randomly assign some units to treatment and some units to control, and the mean of a random sample from the population of units is then an unbiased estimator for the mean of the population. The *counterfactual* is based on random selection into treatment. 

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












