---
title: "Impact evaluation with Difference-in-Differences and Regression Discontinuity"
description: "Use Difference-in-Differences and Regression Discontinuity Design to evaluate impacts of quasi-experiments"
keywords: "regression, model, DiD, RD, impact evaluation, inference, quasi-experiment"
weight: 8
date: 2023-10-01T01:00:00+01:00
draft: false
aliases:
  - /impact/evaluation
  - /run/DiD/
  - /run/RD
  - /regression/discontinuity
---
# Impact Evaluation

## Why?

Many programs are designed to improve outcomes such as learning, health or productivity. Have resources been spent wisely on the program? Did the program/policy work? These are the questions that impact evaluation answers, based on evidence.

In this building block we discuss two of the most commonly used impact evaluation methods, Difference-in-Differences (DiD) and Regression Discontinuity (RD).

## Difference-in-Differences

{{% summary %}}
DiD **compares the changes in outcomes** (e.g. productivity) **over time** between a population that is enrolled in a program (the **treatment group**, e.g. employees who take an IT training) and a population that is not (the **comparison group**, e.g. employees who do not take the IT training).
{{% /summary %}}

### When should I apply DiD?

The DiD framework is used in a wide range of settings, from evaluating the impact of a rise in the [minimum wage](https://econpapers.repec.org/article/aeaaecrev/v_3a84_3ay_3a1994_3ai_3a4_3ap_3a772-93.htm) to assessing how the [adoption of online streaming affects music consumption and discovery](https://tiu.nu/spotify).

{{% tip %}}
DiD works well whenever:

 - There is a sudden specific intervention, treatment or even a date that clearly defines a before and an after. For instance, a passing of a law (e.g. lockdown).

 - There are well defined treatment and control groups.

 - The outcome of interest was measured before and after the treatment or intervention. That is, there is a baseline outcome to which to compare with the outcomes posterior to the intervention.

 - The intervention is unrelated to the outcome at baseline.

{{% /tip %}}

### Run a DiD regression
The following example comes from [Gertler, Martinez, Premand, Rawlings, and Vermeersch (2016)](https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice). From this example, we compare the change in health expenditures over time between enrolled and nonenrolled households in the treatment localities to find out whether the program actually lead to higher health expenditures among the treated.




{{% codeblock %}}

```R
# Data available at https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice

# Open the data
  library(haven)
  impact <- read_dta(".../evaluation.dta")

# Perform the DiD regression
  impact_did <- lm(health_expenditures ~ round + eligible + eligible*round, data= impact %>%
                   filter(treatment_locality == 1))

```

```
-Stata-
* Data available at https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice

* Open the data
  use "evaluation.dta"
  keep if treatment_locality == 1

* Perform the DiD regression to compare the change in health expenditures over time
* between enrolled and non-enrolled households in the treatment localities.
* (The double # tells Stata to include both binary variables and the interaction term)

  reg health_expenditures enrolled##round


```
{{% /codeblock %}}


## Regression Discontinuity

{{% summary %}}
RD is used to estimate the effect of a program or treatment in which candidates are selected for treatment based on whether their value for a numeric index is above or below a certain cutoff point.

  - This method is broadly used in social programs. For instance, antipoverty programs where individuals under a certain poverty index receive help from the government or for scholarships targeted at students that obtain at least a certain grade.
{{% /summary %}}


### When should I apply RD?

RD answers questions such as "should the program be cut or expanded at the margin?" For the scholarships example, we could aim to answer: Should we lower the required grade to expand it to more students or is it not working well enough?

{{% tip %}}
RD works well whenever:

 - There is a clear value or cutoff (e.g. poverty index, academic record) that divides those eligible from those who are not.

 - Such cutoff is based on a continuous variable, rather than categorical.

 - The cutoff score is unique to the program of interest (e.g. driving given that only over 18 year olds can).

 - Control variables/covariates are also continuous at the cutoff point.

 - We are interested in evaluating the impact on individuals around the cutoff rather than the general population.  

{{% /tip %}}


### Run a RD regression

We use the same example as before but we now assess whether the program has managed to significantly decrease health expenditures by comparing individuals just below the cutoff (eligible) to those just above the cutoff (non-eligible).

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

# Perform the RD regression
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

* Perform the RD regression
  reg health_expenditures eligible poverty_index_left poverty_index_right $covariates if round ==1

```
{{% /codeblock %}}


### Check Assumptions

{{% codeblock %}}

```R
# Check whether the poverty index is continuous at the cutoff point
  plot(density(impact$poverty_index))
  abline(v = 58, col = "red")

# Are covariates continuous at the cutoff point?
  plot(impact$poverty_index, impact$covariate1)
  abline(v = 58, col = "red")

# Check for Fuzzy or Sharp RD. If fuzzy, need to find Instrumental Variables.
  rdplot(impact$enrolled, impact$poverty_index, p = 1, c = 58, nbins = c(58, 42))
```

```
-Stata-
* Check whether the poverty index is continuous at the cutoff point
  kdensity poverty_index, xline(58)

* Are covariates continuous at the cutoff point?
  graph twoway scatter covariate1 poverty_index if round==1 & treatment_locality==1, xline(58)

* Check for Fuzzy or Sharp RD. If fuzzy, need to find Instrumental Variables.
  rdplot enrolled poverty_index if treatment_locality==1, c(58) p(1) numbinl(58) numbinr(42)
```
{{% /codeblock %}}



## Additional resources

- Want to learn other widely used impact evaluation methods? The [book](https://www.worldbank.org/en/programs/sief-trust-fund/publication/impact-evaluation-in-practice) from which examples are taken, also delves into many more methods.

- Want to learn more on how to implement these methods and others in R? Check out this [website](https://bookdown.org/aschmi11/causal_inf/regression-discontinuity.html) or [this one](https://bookdown.org/ccolonescu/RPoE4/).

*Gertler, Paul J., Sebastian Martinez, Patrick Premand, Laura B. Rawlings, and Christel M. J. Vermeersch. 2016. Impact Evaluation in Practice, second edition. Washington, DC: Inter-American Development Bank and World Bank. doi:10.1596/978-1-4648-0779-4.*
