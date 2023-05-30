---
title: "Simple Difference-in-Difference Estimation in R"
description: "Estimate the simple 2 x 2 DiD design in R using the fixest package "
keywords: "causal inference, difference-in-difference, DID, R, regression, model, fixest"
draft: false
weight: 2
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /canonical-DiD
---
# Overview
Causal inference aims to uncover the causal impact of a treatment, intervention, or policy change by carefully analyzing observational data. While randomized controlled experiments are considered the gold standard for establishing causality, they may not always be feasible, practical, or ethical sometimes. In such cases, quasi-experimental methods come handy, which leverage naturally occuring variations in treatment or exposure to approximate the conditions of a controlled experiment.

One prominent quasi-experimental method is the Difference-in-Difference (DiD). This is a powerful statistical method widely used to evaluate the causal impact of a treatment or intervention. It allows one to estimate the treatment effect by comparing the changes in outcomes between a treatment group and a control group before and after the treatment is implemented.
## DiD: Theoretical Background

### Potential Outcomes Framework

{{<katex>}}
{{</katex>}}

Prior to exploring the DiD (Difference-in-Differences) design, it is essential to grasp the significance of the **potential outcomes** framework, which serves as the lingua franca of causal inference.
Consider a binary variable that takes the value of 1 if a particular unit $i$ receives *treatment* and 0 if not. Each unit will have *two potential outcomes*, but only one of them is observed. The aforementioned potential outcomes are defined as $Y_i^1$ if unit $i$ received the treatment and as $Y_i^0$ if not. This state of the world where no treatment occurs is called the *control* state.
A unit's "actual" outcome that is observable is a function of its potential outcomes and is denoted by a so-called *switching equation*:

<div style="text-align: center;">
{{<katex>}}
Y_i = D_iY_i^1+(1-D_i)Y_i^0
{{</katex>}}
</div>

where $D_i = 1$ if the unit is treated and 0 if not. When $D_i = 1$, $Y_i = Y_i^1$, likewise when $D_i = 0$, $Y_i = Y_i^0$.

The treatment effect (aka causal effect) is denoted as the difference between the two states of the world (treatment and control):

<div style="text-align: center;">
{{<katex>}}
\delta_i=Y_i^1-Y_i^0
{{</katex>}}
</div>

### Average Treatment Effect

While we have previously defined *individual* treatment effect,researchers are often interested in the *average treatment effect:*

<div style="text-align: center;">
{{<katex>}}
ATE = E[\delta_i]
{{</katex>}}
</div>

Again, since ATE requires one to know BOTH potential outcomes but we observe only one it is unobserved but can be estimated. Now, let’s consider the event that individuals might self-select into the treatment which allows us to estimate the average treatment effect on the treated units (ATT):

<div style="text-align: center;">
{{<katex>}}
ATT = E[\delta_i|D_i=1]
{{</katex>}}
</div>

Similarly, the average treatment effect for the untreated/control group is called ATU(Average Treatment for the Untreated):

<div style="text-align: center;">
{{<katex>}}
ATU = E[\delta_i|D_i=0]
{{</katex>}}
</div>

Having established key theoretical definitions, let's now delve into an example to bridge the gap and illustrate how these concepts are applied in practice.
## An Illustrative Example: The Canonical 2x2 DiD

On May 21, 2014, Goodreads, a social cataloging website for books, introduced the Q&A feature, enabling users to post questions to authors and fellow readers. It is intriguing to explore the potential impact of this feature on subsequent book ratings. For example, users now have the opportunity to proactively inquire about a book before making a purchase. This interaction may help alleviate uncertainties regarding the book's suitability, potentially reducing customer dissatisfaction and mitigating the likelihood of negative reviews.

The dataset used in this example includes information on book ratings and their corresponding dates from both Goodreads and Amazon. In this analysis, we will treat the implementation date of the Q&A policy as the treatment and assess its impact on subsequent book ratings through the employment of the DiD approach. As Amazon lacks the Q&A feature specifically for the book category but still permits consumers to rate and review books akin to Goodreads, it serves as a suitable control group for comparison. You can find all the analysis code in [this Gist](https://gist.github.com/srosh2000/f52600b76999e88f0fe316e8f23b419e).

Since we have 2 groups (Amazon vs Goodreads) and 2 time periods (pre Q&A and post Q&A), we use the canonical 2 x 2 DiD design. This can be estimated with the following regression equation:

<div style="text-align: center;">
{{<katex>}}
rating_{ijt} = \alpha+ \lambda POST_{ijt}+\gamma Goodreads+\delta (POST_{ijt}* Goodreads_{ij})+\eta_j +\tau_t+\epsilon_{ijt}
{{</katex>}}
</div>

where,

$POST$: is a dummy that equals 1 if the observation is after Q&A launch

$Goodreads$: is a dummy equal to 1 if the observation is from the Goodreads platform and 0 if from Amazon

$\eta$: book fixed effects

$\tau$: time fixed effects

- Amazon Pre: $\alpha$
- Amazon Post: $\alpha + \lambda$
- Goodreads Pre: $\alpha + \gamma$
- Goodreads Post: $\alpha+\gamma+\lambda+\delta$

<p align = "center">
<img src = "../images/PT-graph.png" width="700">
<figcaption> Visualisation of the parallel trends assumption </figcaption>
</p>

 $\delta$ is the treatment effect parameter of interest. It is the difference between a counterfactual level of rating and the actual level of rating for Goodreads.

 <div style="text-align: center;">
 {{<katex>}}

 \delta = E[Y_{G,Post}^1]-E[Y_{G,Post}^0]

 {{</katex>}}
 </div>

 while the first term is observed, the second one is a counterfactual which is unobserved. It is the scenario that depicts what would have happened if the treatment group hadn’t received the treatment which is unobservable. This is where the crucial **parallel trends assumption** comes in. We get the true estimate of the causal effect only when the counterfactual trend of Goodreads is in parallel to the observed trend of Amazon. The intuition here relies on the fact that we have a control group (here: Amazon) approximates the trend of the treatment group had it not undergone the treatment and that the treatment is not endogenous. In case it is endogenous, then the parallel trends assumption is violated as the counterfactual trend of the treatment group would have diverged away, regardless of the treatment.

### Estimation

As a first step, it is important to assess whether the **parallel trends assumption** holds before estimation. This can be visually inspected by plotting the average ratings for Goodreads and Amazon over time.

<p align = "center">
<img src = "../images/PL.png" width="700">
<figcaption> Parallel trends assumption check </figcaption>
</p>

We see that pre Q&A, there seems to be similarity in the trends which seems to suggest that the assumption holds in this case.

Now, we are good to go to estimate the treatment effects. We include time and book fixed effects and cluster the standard errors at the book level.

{{% codeblock %}}
```R
# library(fixest) # load the necessary library
model_3<- feols(rating ~ goodr*qa
                  |
                  t + asin,
                data = GoodAma,
                cluster = ~ asin
)
summary(model_3)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/did-result.png" width="700">
<figcaption> Estimation result </figcaption>
</p>

The interaction term `goodr:qa` is the parameter of interest($\delta$), the treatment effect which suggests that the Q&A feature results in lower ratings.

Lastly, there is a growing literature highlighting an important caveat to keep in mind regarding this canonical DiD setup. This simple canonical setup might yield misleading estimates when there might be multiple time periods, groups and variations in the treatment timing.


{{% summary %}}

- Difference-in-Difference (DiD) is a powerful statistical method for evaluating the causal impact of a treatment or intervention.

- DiD compares changes in outcomes between a treatment group and a control group before and after the treatment is implemented.

- Average Treatment Effect (ATE) represents the average effect of treatment on all units.

- Average Treatment Effect on the Treated (ATT) focuses on the treated units, while Average Treatment Effect for the Untreated (ATU) focuses on the control group.

- The parallel trends assumption is crucial for obtaining unbiased estimates in DiD analysis. It requires that in the absence of treatment, the difference between the treatment and control group is constant over time.

- The canonical 2x2 DiD design is used in an illustrative example of the impact of a Q&A feature on book ratings.

- The treatment effects can be estimated in R using the `fixest` package using the `feols()` function.

- The canonical DiD setup involves some limitations when dealing with multiple time periods, groups, and variations in treatment timing.

{{% /summary %}}

# References
- [Cunningham, S. (2021). Causal inference: The mixtape. Yale university press.](https://mixtape.scunning.com/)
