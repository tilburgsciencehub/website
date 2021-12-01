---
title: "Impact evaluation with DiD and RDD"
description: "Use Difference-in-Differences and Regression Discontinuity Design to evaluate impacts of quasi-experiments"
keywords: "regression, model, DiD, RDD, impact evaluation, inference, quasi-experiment"
weight: 3
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /policy/evaluation
  - /run/DiD/
  - /run/RDD
---
# Impact Evaluation

## Why?

## How?
Hands-on book with many models.

In this building block we show two of the most commonly used, Difference-in-Differences and Regression Discontinuity Design.

## Difference-in-Differences

### When should I apply DiD?

{{% codeblock %}}

```R
# Open the Stata dataset
library(haven)
evaluation <- read_dta("..../evaluation.dta")



```

```
-Stata-
* Perform a DiD (Chapter 7)
* We compare the change in health expenditures over time
* between enrolled and non-enrolled households in the treatment localities.

  use "evaluation.dta"
  keep if treatment_locality == 1

* Perform the DiD regression:
  reg health_expenditures enrolled_round##round enrolled, cl(locality_identifier)

```
{{% /codeblock %}}

## Regression Discontinuity Design

RDD is used to estimate the effect of a program, intervention or treatment in which candidates are selected for treatment based on whether their value for a numeric index is above or below a certain cutoff point. This method is widely used in social programs. For instance, antipoverty programs where individuals under a certain poverty index receive help from the government or for scholarships targeted at students that obtain at least a certain grade.



### When should I apply RDD?

RD answers questions such as "should the program be cut or expanded at the margin? For the scholarships example, we could aim to answer: Should we lower the required grade to expand it to more students or is it not working well enough?

{{% warning %}}
For RD to work the following assumptions should be true:

 - There is a clear value or cutoff (e.g. poverty index, academic record) that divides those eligible from those who are not.

 - Such cutoff is based on a continuous variable, rather than categorical.

 - The cutoff score is unique to the program of interest
    - e.g. driving given that only over 18 year olds can.

 - Control variables/covariates are also continuous at the cutoff point.


{{% /warning %}}


### Run a RDD regression

{{% codeblock %}}

```R
# Load necessary packages
  library(haven)
  library(dplyr)
  library(rdrobust)

# Open the dataset
  impact <- read_dta(".../evaluation.dta") %>%
# Select relevant data (treated localities)
  filter(treatment_locality==1) %>%

# Generate above and below cutoff variables to normalize poverty index:
  mutate(poverty_index_left = ifelse(poverty_index<=58, poverty_index-58, 0),
         poverty_index_right = ifelse(poverty_index>58, poverty_index-58, 0))

# Perform the RDD regression
  impact_model <- lm(health_expenditures ~ poverty_index_left+ poverty_index_right
                          + eligible + covariates, data = impact %>% filter(round ==1))

```

```
-Stata-
* install necessary packages
  net install st0366.pkg, all replace force from(http://www.stata-journal.com/software/sj14-4/)
  net install sg65.pkg, all replace force from(http://www.stata.com/stb/stb35)
  net install sxd4.pkg, all replace force from(http://www.stata.com/stb/stb60)

* Open the dataset
  use ".../evaluation.dta"

* Select relevant data (treated localities)
  keep if treatment_locality == 1

* Generate above and below cutoff variables to normalize poverty index:
  gen poverty_index_left = poverty_index if poverty_index<=58
  replace poverty_index_left = 0 if poverty_index>58
  gen poverty_index_right = poverty_index if poverty_index>58
  replace poverty_index_right=0 if poverty_index<=58

* Perform the RDD regression
  reg health_expenditures eligible poverty_index_left poverty_index_right $covariates if round ==1

```
{{% /codeblock %}}


### Check Assumptions

{{% codeblock %}}

```R
# Check whether the poverty index is continuous at the cutoff point
  plot(density(impact$poverty_index))
  abline(v = 58, col = "red")

# Are covariates continuous at cutoff point?
  plot(impact$poverty_index, impact$covariate1)
  abline(v = 58, col = "red")

# Check for Fuzzy or Sharp RDD. If fuzzy, need to find Instrumental Variables.
  rdplot(impact$enrolled, impact$poverty_index, p = 1, c = 58, nbins = c(58, 42))
```

```
-Stata-
* Check whether the poverty index is continuous at the cutoff point
  kdensity poverty_index, xline(58)

* Are covariates continuous at cutoff point?
  graph twoway scatter covariate1 poverty_index if round==1 & treatment_locality==1, xline(58)

* Check for Fuzzy or Sharp RDD. If fuzzy, need to find Instrumental Variables.
  rdplot enrolled poverty_index if treatment_locality==1, c(58) p(1) numbinl(58) numbinr(42)
```
{{% /codeblock %}}

*Gertler, Paul J., Sebastian Martinez, Patrick Premand, Laura B. Rawlings, and Christel M. J. Vermeersch. 2016. Impact Evaluation in Practice, second edition. Washington, DC: Inter-American Development Bank and World Bank. doi:10.1596/978-1-4648-0779-4.*
