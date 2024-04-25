---
title: "An Introduction to Difference-in-Difference Analysis"
description: "This building block motivates causal inference, provides theoretical background for the difference-in-difference method and an example that walks you through how to set up the data to compute difference in means table for the 2 x 2 case.  "
keywords: "causal inference, difference-in-difference, DID, R, regression, model, canonical DiD, difference in means table, potential outcomes framework, average treatment effect, ATE, ATT, ATU, treatment effects"
draft: false
weight: 9
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /canonical-DiD
---
# Overview
Having the ability to establish causality provides a strong foundation for using the term "because" when making claims about the relationship between certain variables. We are then able to say for instance, that the popularity of a song increased *because* it was featured in a movie or that the customer bought a given product *because* they saw an ad and so on. These relationships are not inherently causal, as the direction of cause and effect may be ambiguous, other variables can influence the relationship, or the observed outcome may be due to chance. While regression analysis provides some insight into the significance of associations, interpreting the results as causal relationships requires additional assumptions and thoughtful study designs.

<p align = "center">
<img src = "../images/corr_cause.png" width="700">
<figcaption> Source: xkcd (https://xkcd.com/552/) </figcaption>
</p>

While randomized controlled experiments are widely regarded as the gold standard for establishing causality, they may not always be practical, feasible, or ethically permissible. In such circumstances, quasi-experimental methods offer a valuable alternative by leveraging naturally occurring variations in treatment or exposure to approximate controlled experimental conditions. One such prominent quasi-experimental method is known as **Difference-in-Differences** (DiD). This robust statistical approach is extensively used to evaluate the causal impact of a treatment or intervention. It allows estimation of the treatment effect by comparing changes in outcomes between a treatment group and a control group before and after the implementation of the treatment.

## DiD: Theoretical Background

### Potential Outcomes Framework

Before delving into the Difference-in-Differences design, it is essential to grasp the significance of the **potential outcomes** framework, which serves as the lingua franca of causal inference. In this framework, each unit has two potential outcomes: $Y_i^1$ if the unit receives treatment and $Y_i^0$ if not. However, we can only observe one of these potential outcomes. The observable outcome, denoted by $Y_i$ is determined by a *switching equation*:

$$
Y_i = D_iY_i^1+(1-D_i)Y_i^0
$$

where $D_i = 1$ if the unit is treated and $0$ if not. When $D_i = 1$, $Y_i = Y_i^1$, likewise when $D_i = 0$, $Y_i = Y_i^0$.

### Average Treatment Effect

While we have previously defined *individual* treatment effect, researchers are often interested in the *average treatment effect:*

<div style="text-align: center;">
$$
ATE = E[\delta_i] \\
= E[Y_i^1 - Y_i^0]\\
= E[Y_i^1] - E[Y_i^0]\\
$$
</div>

Here, we compare potential outcomes when *all* units receive treatment with the potential outcomes when no units receive treatment.

Again, since ATE requires one to know BOTH potential outcomes but we observe only one it is unobserved but can be *estimated*. Now, let’s consider the event that individuals might self-select into the treatment which allows us to estimate the *Average Treatment effect on the Treated* units (ATT):

<div style="text-align: center;">
$$
ATT = E[\delta_i|D_i=1] \\
= E[Y_i^1|D_i=1] - E[Y_i^0|D_i=1]
$$
</div>

Similarly, the average treatment effect for the untreated/control group is called *Average Treatment for the Untreated* (ATU):


$$
ATU = E[\delta_i|D_i=0]
$$
In the DiD setup, we are mainly interested in comparing the outcomes before and after the treatment for the treated and control groups:

 {{% table %}}
|                 | Before ($Y_i^0$)     | After ($Y_i^1$)     |
| --------------- | ---------------------- | ---------------------- |
| Control ($D_i = 0$)    | $E(Y_i^0 \mid D_i = 0)$   | $E(Y_i^1 \mid D_i = 0)$   |
| Treatment ($D_i=1$)    | $E(Y_i^0 \mid D_i = 0)$   | $E(Y_i^1 \ mid D_i = 1)$    |
 {{% /table %}}

Part of the outcomes presented above are *counterfactual*. These outcomes represent what would have happened to the treated and control groups if their treatment statuses were reversed. Naturally, a single person cannot be both treated and not treated, that’s why we only observe one of the two values.

For more intuition, suppose we are studying the effectiveness of a new educational program (treatment) on students’ test scores. We have a control group of students who did not receive the program (when $D_i = 0$) and a treatment group of students who did receive the program (when $D_i = 1$).

The counterfactual outcomes help us understand what would have happened if the treatment status were reversed for each group:

- For the *control* group (when $D_i = 0$): The counterfactual outcome represents the expected test scores for the control group if they had received the treatment. This is denoted as $E(Y_i^1|D_i = 0)$. It provides an estimate of what their test scores would have been if they had been part of the treatment group.
- For the *treatment* group (when $D_i = 1$): The counterfactual outcome represents the expected test scores for the treatment group if they had not received the treatment. This is denoted as $E(Y_i^0|D_i = 1)$. It gives us an estimate of what their test scores would have been if they had been part of the control group instead.

Now imagine for a while we can move between alternative realities and can observe the same person’s outcome in both scenarios: when they are treated and when they are not.

At a first glance, one might think of simply taking the difference in the average outcome before and after for the treatment group ($Y_1^0-Y_1^1$). However, this approach fails because the occurrence of treatment and time are perfectly correlated, making it impossible to isolate the treatment effect from the temporal effects.

Similarly, taking the difference between the average outcomes of the treated and control groups in the after period ($Y_1^1-Y_0^1$) won’t work either. This is because the treatment group might naturally differ from the control group, leading to differences in outcomes that are not solely due to the treatment effect.

To address these issues, we combine both ideas and perform **double differencing**, which is why it is called *difference-in-difference.*
{{%table%}}

|  | Before | After | After - Before |
| --- | --- | --- | --- |
| **Control** | $\alpha$ | $\alpha + \lambda$ |  |
| **Treatment** | $\alpha + \gamma$ | $\alpha+\gamma+\lambda+\delta$ |  |
| **Treatment** - **Control**  | $\gamma$ | $\gamma+\delta$ | $\delta$ |
{{%/table%}}


By taking the difference between the treatment and control groups’ outcomes before treatment ($\gamma$) and the difference between their outcomes after treatment ($\gamma + \delta$), we can obtain the final treatment effect ($\delta$).
## Assumptions for Causality

To establish causality using the DiD design, two key assumptions are necessary:

1. **Parallel Trends Assumption**: The parallel trends assumption states that, in the absence of treatment, the treated and control groups would have followed similar trends over time. This assumption implies that any differences in outcomes between the two groups before treatment can be attributed to pre-existing differences, as the trends are assumed to be parallel. It ensures the existence of a valid counterfactual outcome to compare the treated group.
More formally, it assumes that the difference between the control group's counterfactual outcome ($E(Y_i^1|D_i = 0)$) and its observed outcome before treatment ($E(Y_i^0|D_i = 0)$) would remain constant over time. Similarly, it assumes that the difference between the treatment group's observed outcome after treatment ($E(Y_i^1|D_i = 1)$) and its counterfactual outcome ($E(Y_i^0|D_i = 1)$) would also remain constant over time.

<p align = "center">
<img src = "../images/parallel.png" width="700">
<figcaption> Parallel trends visualisation, image by the author </figcaption>
</p>

2. **Conditional Independence (Unconfoundedness) Assumption**: The conditional independence assumption states that, conditional on observed variables, the treatment assignment is independent of potential outcomes. This assumption ensures that there are no confounding factors that simultaneously affect both the treatment assignment and the potential outcomes. It implies that, after controlling for observable covariates, the treatment assignment is random with respect to potential outcomes. Controlling for observable covariates helps reduce the potential for bias due to omitted variables confounding.

Now that we have covered all the basics, let's jump to an example to put all this theory to practice!

## An Illustrative Example: The Canonical 2x2 DiD Table
On May 21, 2014, Goodreads, a social cataloging website for books, introduced the Q&A feature, enabling users to post questions to authors and fellow readers. It is intriguing to explore the potential impact of this feature on subsequent book ratings. For example, users now have the opportunity to proactively inquire about a book before making a purchase. This interaction may help alleviate uncertainties regarding the book's suitability, potentially reducing customer dissatisfaction and mitigating the likelihood of negative reviews.

The dataset used in this example includes information on book ratings and their corresponding dates from both Goodreads and Amazon. In this analysis, we will treat the implementation date of the Q&A policy as the treatment and assess its impact on subsequent book ratings through the employment of the DiD approach. As Amazon lacks the Q&A feature specifically for the book category but still permits consumers to rate and review books akin to Goodreads, it serves as a suitable control group for comparison. You can find the complete data preparation and analysis code in this [Gist](https://gist.github.com/srosh2000/f52600b76999e88f0fe316e8f23b419e) to follow along.

Since we have 2 groups (Amazon Vs Goodreads) and 2 time periods (pre Q&A and post Q&A), we use the canonical 2 x 2 DiD design.

{{% codeblock %}}
```R
# Compute the average rating for the treatment and control group, before and after the Q&A launch
means<- GoodAma %>%
  group_by(goodr, qa) %>%
  summarize(rating=mean(rating)) %>%
  ungroup()

# Modify the labels
means_modified <- means %>%
  mutate(
    goodr_label = case_when(
      goodr == 0 ~ "Amazon",
      goodr == 1 ~ "Goodreads"
    ),
    qa_label = case_when(
      qa == 0 ~ "Before",
      qa == 1 ~ "After"
    )
  )
print(means_modified)
```
{{% /codeblock %}}

Here, we compute the average rating for the treatment and control group both before and after the Q&A launch based on the `GoodAma` dataframe. The treatment dummy, `goodr = 1` indicates the *treatment* group (Goodreads), and otherwise the *control* group (Amazon). The time dummy, `qa = 1` indicates the *after* period and `0` for *before* period.

<p align = "center">
<img src = "../images/did-table.png" width="500">
<figcaption> Difference in means table (2 x 2 case) </figcaption>
</p>


Now, let’s compute the treatment effect by **double differencing**.

{{% codeblock %}}

```R
# before-after for untreated, has time effect only

bef_aft_untreated <- filter(means, goodr == 0, qa == 1)$rating - filter(means, goodr == 0, qa == 0)$rating

# before-after for treated, has time and treatment effect
bef_aft_treated<- filter(means, goodr == 1, qa == 1)$rating - filter(means, goodr == 1, qa == 0)$rating

# difference-in-difference: take time +treatment effect, and remove the time effect
did<- bef_aft_treated - bef_aft_untreated

print(paste("Diff in Diff Estimate: " , did))
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/treatment-effect.png" width="500">
<figcaption> Treatment effect value </figcaption>
</p>

The obtained results indicate that the presence of the Q&A feature is associated with lower ratings. However, it is crucial to acknowledge that the differences in means table presented above is merely suggestive and should be interpreted with caution. To obtain more accurate and reliable estimates, it is essential to conduct a regression analysis that allows us to control for other variables that may be related to the outcome and treatment, thereby providing a more comprehensive understanding of the relationship.

Utilising regression analysis not only enhances the precision of the estimates but also allows us to examine the statistical significance of the results. This helps determine the strength and reliability of the observed relationship between the Q&A feature and ratings. Additionally, regression analysis enables the exploration of potential interactions or nonlinear effects, providing further insights into the complex dynamics at play.


{{% summary %}}

- **Difference-in-Difference** (DiD) is a powerful statistical method for evaluating the causal impact of a treatment or intervention.

- DiD compares changes in outcomes between a treatment group and a control group before and after the treatment is implemented.

- **Average Treatment Effect** (ATE) represents the average effect of treatment on all units.

- **Average Treatment Effect on the Treated** (ATT) focuses on the treated units, while **Average Treatment Effect for the Untreated** (ATU) focuses on the control group.

- The **parallel trends** assumption and **conditional independence** assumption are crucial for a causal interpretation of the estimates.


{{% /summary %}}

# Reference
- [Cunningham, S. (2021). Causal inference: The mixtape. Yale university press.](https://mixtape.scunning.com/)
