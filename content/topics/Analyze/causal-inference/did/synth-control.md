---
title: "Synthetic Control for Impact Evaluation"
description: "Use Synthetic control to evaluate impacts of quasi-experiments"
keywords: "model, Synthetic Control, RD, impact evaluation, inference, quasi-experiment, abadie"
weight: 4
date: 2023-10-01T01:00:00+01:00
draft: false
aliases:
  - /impact/syntCont
  - /run/syntCont/
  - /run/syntCont
---
# Synthetic Control?

## What is Synthetic Control

Synthetic Control is a tool developed by Abadie and Gardeazabal (2003) used widely in applied econometrics and particularly in impact evaluation. Synthetic control is best used in a framework in which we are interested in measuring effects to some outcome in units at an aggregate level, for example countries or states. As opposed to other techniques like [Difference in Difference](/impact/evaluation) that give clear-cut definition of what is a control unit, Synthetic Control uses a data-driven approach to construct a control measure.

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

Because the analysis may include many covariates, it is necessary to also assign a weight to the importance in each covariates when measuring the difference between the treated unit and the donors.

The standard approach involves a two-step procedure, in which the donor weights are calculated for any given weight in the covariates, and then the optimal weight of the covariates is determined by minimizing the distance in the outcome variable for the pre-treatment period. Other approaches include using the inverse of variance to calculate the covariates weight or out-of-sample validation.

{{% tip %}}

 - Limiting weights to be non-negative allows for better extrapolation and gives a more intuitive interpretation of the synthetic control, as it can be thought of an addition of pieces of different donor units.
 
  - With non-negative weights it is common to have lots of donor units with weight 0 and only a few units with positive weights.

 - No limits to weights on the other hand give more flexibility to the procedure and may results in more efficient estimations.
 
{{% /tip %}}

Treatment effect is then estimated as the difference in the outcome of the treated unit and the synthetic control in the post-treatment period.

{{% example %}}

Some situations in which Synthetic Control has been applied:

 - Abadie and Gardeazabal (2003) is the founding paper of this literature. They measure the impact of terrorism in the Basque country, using other regions of Spain as the donor units.
 
 - Abadie, Diamond and Hainmueller (2010) measures the effect of a Tobacco Control Program in California, using other states of US as controls.
 
 - Abadie, Diamond and Hainmueller (2015) analyses the impact of 1990's reunification to West Germany's economy, taking other OECD countries as the donor pool.

 - Acemoglu, Johnson, Kermani, Kwak and Mitton (2016) study the value of political connections for firms during financial turmoil in 2008 financial crisis. In this setting there are many treated units, consisting of well-connected firms and the donor pools consists of non-connected firms.

{{% /example %}}

## Running a Synthetic Control analysis

The code uses data from [Abadie, Diamond and Hainmueller](https://www.nber.org/papers/w12831). The paper studies the effect of the introduction of a Tobacco Control Program in the state of California using other US states as controls for the donor pool. 

### Preparing the data

{{% codeblock %}}

```R
# Load necessary packages
#install.packages("Synth")
library(Synth)
	
# Open the dataset
url_synth=url("https://github.com/tilburgsciencehub/website/blob/9a0409c87948eb2cc523f9233b8e622574f55cac/content/topics/analyze-data/regressions-paneldata/synth_smoking.Rdata?raw=true")
load(url_synth)

# Data Preparation to pass the dataset to the correct format
# Predictors are averaged in the pre-treatment period
# Special predictors only use the years that are selected
# Treatment identifier gives the numeric identifier for California
# Control identifier lists the other 38 states used as controls


dataprep_smoking<- dataprep(foo = synth_smoking,
predictors = c("beer", "retprice"),
predictors.op = "mean",
dependent = "cigsale",
unit.variable = "state_num",
time.variable = "year",
special.predictors = list(
list("lnincome",c(1980,1985),"mean"),
list("cigsale", 1988, "mean"),
list("cigsale", 1980, "mean"),
list("cigsale", 1975, "mean")
),
controls.identifier = c(1:2,4:39),
time.predictors.prior = c(1970:1988),
time.optimize.ssr = c(1970:1988),
treatment.identifier = 3,
unit.names.variable = "state",
time.plot=c(1970:2000))


```

```
-Stata-
* install necessary packages
	ssc install synth

* Open the dataset
	use synth_smoking, clear

* Pass panel data format to the dataset

tsset state year


```
{{% /codeblock %}}


### Estimation and Graphical Output


{{% codeblock %}}

```R

# The comand takes the data structure from dataprep function above, with the defined dependent variable and regressors

synth_res=synth(dataprep_smoking,optimxmethod="All")

# To obtain the results, which give the donor units and covariates weights

print(synth.tab(synth_res,dataprep_smoking))

# Produce graphical output with treated unit and synthetic control

path.plot(synth_res,dataprep_smoking)
abline(v=1988.5,col=2,lty=2)

gaps.plot(synth_res,dataprep_smoking)
abline(v=1988.5,col=2,lty=2)


```

```
-Stata-

* Run command and obtain graphical output
* Results show the weights of donor units

synth cigsale beer retprice lnincome(1980&1985) cigsale(1988)  cigsale(1980) cigsale(1975), trunit(3) trperiod(1989) fig


```
{{% /codeblock %}}


