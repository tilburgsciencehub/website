---
title: "Event Studies for Causal Inference"
description: "A building block on the implementation of event studies in R"
keywords: "event studies, causal inference, panel data, staggered treatment, time, dynamic treatment"
draft: false
weight: 1
author: "Virginia Mirabile"
aliases:
- /event-studies
- /event-study
---

# Overview 

Event studies are a powerful tool in the field of causal inference, allowing researchers to examine the impact of specific events on outcomes of interest and providing a quasi-experimental setting to evaluate causal relationships. This building block will delve into the concept of event studies, explore why they are essential for causal inference, and provide examples of how they have been employed in the context of staggered treatment designs.


## Why event study? 

Event studies offer several advantages for causal inference compared to traditional observational studies or experimental designs. First, they allow researchers to isolate the effect of a specific event from other confounding factors by focusing on the immediate changes in the outcome variable before and after the event. This temporal comparison provides a clear before-and-after picture, making it easier to attribute changes in the outcome to the event itself.

Second, event studies are particularly useful when randomized controlled trials (RCTs) are not feasible or ethical. In situations where it is impossible to manipulate the treatment variable, researchers can leverage naturally occurring events as quasi-experiments to estimate causal effects.

Finally, event studies provide a transparent and replicable framework for causal inference. The methodology is well-established, making it easier for other researchers to validate the findings and build upon existing research.

## Example case: Dynamic Treatment Effects in Staggered Design

Event studies are a powerful tool in the field of causal inference, offering a robust framework to examine the impact of specific events on outcomes of interest. While traditionally used to assess the immediate effects of events, such as policy changes, event studies can also be adapted to analyze dynamic treatment effects, particularly in the context of staggered treatment timing designs.

In staggered treatment timing designs, treatments or interventions are rolled out sequentially over time to different units, such as individuals, firms, or regions. This design allows researchers to study the dynamic effects of the treatment and to assess how the impact evolves over time as more units are treated. Event studies provide a formalized approach to analyze these dynamic treatment effects by focusing on the timing of the treatment as the "event" of interest and examining its immediate and longer-term impact on the outcome variable.

In this building block, we will delve into the concept of dynamic treatment effects in staggered treatment timing designs, explore how event studies can be used to formalize the analysis of these effects, and provide examples to illustrate their application. 

# Implementation 

In this building block, we will be dealing with a situation in which we have a **staggered treatment design**, meaning that all subjects of the study are eventually treated, and the only difference is the timing of treatment, administered randomly.

Estimation of the treatment effect can be done by means of **event study analysis**, which analyzes how the outcome changes around the time of treatment (first difference) for a specific unit *i* being treated, while units not undergoing treatment serve as controls (second difference).

## Context and background 

Throughout this example we will be using panel data from a field experiment conducted in Tilburg between 2014-2015, with the objective of encouraging households to separate their waste effectively. For more details, refer to the related paper by Ben Vollaard and Daan van Soest, 2023 titled ["Punishment to promote prosocial behavior: a field experiment"](https://www.sciencedirect.com/science/article/pii/S0095069623001171?dgcid=SSRN_redirect_SD&ssrnid=4569587). 

In this experiment, households used a dual-compartment garbage container, and the treatment involved a one-month crackdown by inspectors. Prior to the crackdown, a letter was sent to all households on a designated route announcing the enforcement action. During this period, inspectors checked the contents of each garbage container. If violations were detected, warnings were issued, and fines were imposed. 

The treatment was announced in a letter that was sent out three weeks before the start of the intervention. The treatment itself ran for four weeks. 

The study is based on a staggered treatment design. The timing of the treatment was randomized at the level of 5 or 10 garbage collection routes. Each of the routes counts some 1,000 households.

Now that the context we will be working with is clear, let's dive into some coding!

## Application in R 

In this building block, you learn how to set up a time-to-event analysis step by step in R. This should prepare you to do the same thing on your own.

Let's start with the usual cleaning operation: 

{{% codeblock %}}
```R
# Remove all objects from the global environment, without removing the loaded packages
if(!is.null(dev.list())) dev.off() 
# Clear the console
cat("\014")
# Remove all objects from the global environment
rm(list = ls())
```
{{% /codeblock %}}


{{% codeblock %}}
```R
# Install the fixest package for fixed-effects models
install.packages("fixest")
```
{{% /codeblock %}}

{{% codeblock %}}
```R
# Load necessary libraries
library(tidyverse)
library(dplyr)
library(ggplot2) 
library(fixest)
library(foreign)
```
{{% /codeblock %}}

{{% tip %}}
If not previously downloaded, perform the command install.packages("") on the above libraries. 
{{% /tip %}}

### Data 

The dataset is available for download in STATA 11/12 format, follow the command below:

{{% codeblock %}}
```R
theUrl_event_studies <- "https://surfdrive.surf.nl/files/index.php/s/ZphgKxImtwFawv9/download"
waste <- read.dta (file = theUrl_event_studies)
```
{{% /codeblock %}}

The main outcome variable is the weight of residual waste collected per garbage collection route per calendar week, *residual_weight*. The variable treatment is 1 as of the week that the announcement was sent out, and remains 1 for the rest of the time.

Before running any further code, let's write down the event time regression that we will use to estimate treatment effect:


$$Y_{it} = \beta_0 + \sum_{\tau = -T}^{-1} \alpha_\tau W_{i\tau} + \sum_{\tau = 1}^{T} \alpha_\tau W_{i\tau} + \lambda_i + \mu_t + \epsilon_{it}$$

Let's break down the equation and give some interpretation: 

- $Y_{it}$: Outcome variable, weight of residual waste per household $i$ in week $t$.
- $\tau$: Event time, indicating time relative to the start of the treatment ($\tau$ = 1 treatment starts).
- $\sum_{\tau = -T}^{-1} \alpha_\tau W_{i\tau}$: Sum of the pre-event window effects. It helps to control for any existing trends in the outcome variable before the event occurs.
- $\sum_{\tau = 1}^{T} \alpha_\tau W_{i\tau}$: Sum of the post-event window effects. It helps to capture the impact of the event on the outcome variable over a window of time after the event occurs. 
- $ W_{i\tau}$ is 1 for event time $\tau$ = 1 and 0 otherwise. 
- $\lambda_i + \mu_t$: Individual and time fixed-effects.

Once the theory is clear, let's move on to estimating this equation in R. 

The following code shows how to find out, for every route, in which calendar week the treatment started and defines the variable *event time*, indicating the treatment time span. 

{{% codeblock %}}
```R
waste <- waste %>% 

  # Group the data by 'route'
  group_by(route) %>%
  
  # Create a new column 'weekstart':
  # If 'treatment' is 1, use 'calendar_week', otherwise use infinity
  mutate(weekstart = ifelse(treatment == 1, calendar_week, Inf), 
  
  # Create a new column 'weekstart2' to store the minimum value of 'weekstart' for each group
  weekstart2 = min(weekstart),
  
  # Create a new column 'eventtime': with event time 0 being the last week before the start of the treatment, 1 in the first week of the treatment etc.
  # Calculate the difference between 'calendar_week' and 'weekstart2' plus 1
  eventtime = calendar_week - weekstart2 + 1) %>% 
  
  # Remove the temporary columns 'weekstart' and 'weekstart2'
  select(-weekstart, -weekstart2) %>%
  
  # Ungroup the data: tell R to no longer do everything by route
  ungroup()

```
{{% /codeblock %}}

To see how event time is distributed, make a histogram:

{{% codeblock %}}
```R
ggplot(waste, aes(x=eventtime, fill = "blue")) + 
  geom_bar(stat="count") + 
  labs(x='event time', y='count', title='Time since start of treatment') +
  scale_fill_identity()
```
{{% /codeblock %}}

As you can see, at the tails of event time we are dealing with very few observations (as low as 5). 

<p align = "center">
<img src = "../images/event_hist.png" width="500">
</p>

This could impose a problem as event time dummies with few observations cannot be estimated. 
To deal with the low number of observations in the tails, we can resort to the technique of **binning**. 
The solution is creating bins with multiple event times at the tails. In this case we create two bins containing the extreme values of 'eventtime':

{{% codeblock %}}
```R
# Update the 'waste' dataframe by adding a new column 'eventtime_bin'
waste <- waste %>%
  
  # Create a new column 'eventtime_bin':
  # If 'eventtime' is less than or equal to -37, set 'eventtime_bin' to -37.
  # If 'eventtime' is greater than or equal to 28, set 'eventtime_bin' to 28.
  # Otherwise, set 'eventtime_bin' to 'eventtime' itself.
  mutate(eventtime_bin = ifelse(eventtime <= -37, -37,
                                ifelse(eventtime >= 28, 28, eventtime)))

```
{{% /codeblock %}}


Let's now estimate the model using the function *feols* from the *fixest* package. 

{{% codeblock %}}
```R
#first, define a variable named "allones" that contains only ones. This indicates that all routes in the data are eventually treated. 
waste$allones <- 1
```
{{% /codeblock %}}

{{% codeblock %}}
```R
#Include residual_weight as outcome variable, the i() allows for interaction terms between event time and treated groups, include route and time fixed effects
mod_twfe = feols(residual_weight ~ i(eventtime_bin, allones, ref=0) | route + calendar_week, data=waste)
etable(mod_twfe)
```
{{% /codeblock %}}

The argument ref is the value of event-time taken as a reference. We take it to be 0, i.e. the last ‘normal’ period, the last period before the start of the treatment.

You can now see a long list of coefficients $\alpha_\tau$ which can be pretty confusing to go through, let's plot them with respect to time to have a straightforward picture of treatment effect. 

{{% codeblock %}}
```R
iplot(mod_twfe,
      xlab = 'Time to treatment',
      main = 'Event study: Staggered treatment (TWFE)', 
      type = "l", 
      col = "blue", 
      grid = TRUE,
      pch = 1, 
      legend = TRUE,
      legend.text = c("Treatment Effect", "95% CI"),
      ylab = "Treatment Effect",
      lty = 2, 
      lwd = 1)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/event_timeplot.png" width="500">
</p>

In this specific case, we assume that treatment effects are homogeneous across both time and groups. The estimated event time coefficients are derived from comparing newly treated groups (routes) to those that have not yet been treated, as well as to those that have already been treated. If treatment effects are, in fact, heterogeneous, comparing newly treated groups with already treated ones (known as "forbidden comparisons") can introduce bias into the estimated treatment effect.

# Summary 

{{% summary %}}

1. Event studies are crucial for causal inference, allowing examination of the impact of specific events on outcomes, especially in staggered treatment designs.
2. Advantages of Event Studies: They isolate the effect of an event from confounding factors and offer a transparent and replicable framework for causal inference.
3. Implementation in R: A step-by-step guide is provided for setting up a time-to-event analysis in R, focusing on a staggered treatment design.

{{% /summary %}}


## References 

Ben Vollaard, Daan van Soest,Punishment to promote prosocial behavior: a field experiment, Journal of Environmental Economics and Management, Volume 124, 2024, 102899, ISSN 0095-0696,
https://doi.org/10.1016/j.jeem.2023.102899.
(https://www.sciencedirect.com/science/article/pii/S0095069623001171)

Vollaard, Ben; Soest, Daan van, 2024, "Replication Data for: Collected household waste 2014-2015 – Tilburg’; ‘Household survey waste separation and warnings issued 2014-2015 – Tilburg", https://doi.org/10.34894/R7TRVB, DataverseNL, V1

