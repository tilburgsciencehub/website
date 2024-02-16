---
title: "Matching"
description: ""
keywords: "matching, causal, inference, regression, R"
draft: false
weight: 1
author: "Valerie Vossen"
aliases:
  - /exact-matching
  - /matching
---

# Overview

Randomization is a fundamental principle in experimental design, aiming to have a good counterfactual and ensuring treatment and control group are similar except for being treated. However, in certain cases, treatment is not randomly assigned and confounders can bias the estimated causal effect.

Matching is an alternative approach, which involves pairing individuals or units based on specific characteristics to create comparable groups. 

This article provides a comprehensive introduction of matching methods, focusing on both theory and practical applications.

## Exact and approximate matching

The focus lays on exact matching, which involves pairing individuals who share **identical characteristics**. This requires the variable on which pairing happens to be a binary variable. In contrast [approximate matching](/approximate-matching) allows for some degree of flexibility and pairs on similar but not identical characteristics. 

## Identifying assumptions

summary
1. Conditional Independence Assumption
2. Conditional on X, there are treated and untreated units. 
summary


### Conditional Independence Assumption (CIA)

The identifying assumption is the Conditional Independence Assumption.

It states that once observable characteristics (the covariates) are taken into account, the assignment of treatmetn becomes independent of potional outcomes. In other words, given a set of observed characteristics, there should be no systematic differences in potential outcomes between the treatment and control groups (respectively Y0 and Y1). 

This is expressed as follows:

(Y0, Y1) ⊥ T|X

which states that potential outcomes in the treatment and control group (expected values for Y0 and Y1) are independent of treatment assignment T, for each value of X. The X is the binary variable on which the groups are based.

### Assumption 2 


If these two assumptions are true, the followig identity is valid:

E[Y1 - Y0 | X] 
= E[Y1 - Y0 | X, D = 1] - E[Y0 | X, D = 0]
= E[ Y | X, D=1] - E[Y | X, D=0]

We can estimate ...


## Exact matching

Counterfactual is mean outcome in control group for observations with the exact same characteristics.
Example: we have unit in 


## Practical example

Imbens (2015) gives three practical examples.


table





