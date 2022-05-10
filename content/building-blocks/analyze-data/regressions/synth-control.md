---
title: "Synthetic control for impact evaluation"
description: "Use Synthetic control to evaluate impacts of quasi-experiments"
keywords: "model, Synthetic Control, RD, impact evaluation, inference, quasi-experiment, abadie"
weight: 3
#date: 2022-05-09T22:02:51+05:30
draft: true
aliases:
  - /impact/syntCont
  - /run/syntCont/
  - /run/syntCont
---
# Synthetic Control?

## What is Synthetic Control

Synthetic Control is a tool developed by Abadie and Gardeazabal (2003) used widely in applied econometrics and particularly in impact evaluation. Synthetic control is best used in a framework in which we are interested in measuring effects to some outcome in units at an aggregate level, for example countries or states. As opposed to other techniques like [Difference in Difference](https://tilburgsciencehub.com/building-blocks/analyze-data/regressions/impact-evaluation/) that give clear-cut definition of what is a control unit, Synthetic Control uses a data-driven approach to construct a control measure.

{{% tip %}}
Some useful vocabulary:

 - **Treatment** is an intervention that occurs at some point in time to treated units but not to the donor pool.

 - **Treated** unit is a unit that receives treatment, for example a country in which certain policy intervention takes place.

 - **Donor** units are units that do not receive treatment. For it to constitute a Synthetic Control application, the donor pool must contain at least two units, and generally many more.
 
 - **Outcome** is the variable we are interested in measuring the effect of the treatment.
 
 - **Covariates** are variables, other than the treatment variable, that are useful to predict the level of the outcome and that will be used for defining the synthetic control.
 
{{% /tip %}}

## Constructing the synthetic control

The control unit in Synthetic Control is built as a weighted average of the units of the donor pool. To define what weights to assign to each unit in the donor pool Synthetic Control method proposes an algorithm based on the similarity of covariates of the donor unit to those of the treatment unit in the pre-treatment period.


{{% tip %}}

 - Limiting weights to be non-negative allow for better extrapolation and give a more intuitive interpretation of the synthetic control, as it can be thought of an addition of pieces of different donor units.

 - No limits to weights on the other hand give more flexibility to the procedure and may results in more efficient estimations.
 
 - With non-negative weights it is common to have lots of donor units with weight 0 and only a few units with positive weights.
 
{{% /tip %}}

Treatment effect is then estimated as the difference in the outcome of the treated unit and the synthetic control in the post-treatment period.

{{% example %}}

Some situations in which Synthetic Control has been applied:

 - 


{{% /example %}}

## Running a Synthetic Control

### Preparing the data

{{% codeblock %}}

```R
# Load necessary packages
	#install.packages("Synth")
	library(Synth)

# Open the dataset
  synth_smoking <- load(url("https://github.com/tilburgsciencehub/website/blob/9a0409c87948eb2cc523f9233b8e622574f55cac/content/building-blocks/analyze-data/regressions/synth_smoking.Rdata?raw=true"))


```

```
-Stata-
* install necessary packages
	ssc install synth

* Open the dataset
	use synth_smoking, clear


```
{{% /codeblock %}}


### Estimation

### Some interesting graphical output



