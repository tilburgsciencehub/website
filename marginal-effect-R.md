---
title: "Find marginal effects in R"
description: "Find marginal effects in R through margins package. Examples using probit and logit models"
keywords: "logit, probit, marginal effects, binary model, AME, MEM, average marginal effects"
weight: 3
#date: 2022-05-16T22:02:51+05:30
draft: TRUE
aliases:
  - /run/margR/
  - /run/margR
---
# Find marginal effects in R

## Loading the data and setting up the models

In many cases when analyzing a model, for example one with a dependent variable that is binary , we are interested in the marginal effects that the regressors have on the outcome variable, rather than the headline estimated coefficients. 

Consider the case examined in Wooldridge's Introductory Econometrics textbook where a binary variable such as female's labor participation is analyzed as depending on education, partner's income, age and number of children. A standard way to estimate this is using either a logit or a probit model. 

{{% codeblock %}}
```R
# Load necessary packages
#install.packages("margins")
library(foreign)
library(margins)
	
# Open the dataset
datab = read.dta("http://fmwww.bc.edu/ec-p/data/wooldridge/mroz.dta")

# Run Probit and Logit Model. OLS as well, for reference

probit_model = glm(inlf ~ nwifeinc + educ + exper + expersq + age + kidslt6 + kidsge6,data=datab, family = binomial(link = "probit"))

logit_model = glm(inlf ~ nwifeinc + educ + exper + expersq + age + kidslt6 + kidsge6,data=datab, family = binomial(link = "logit"))

ols_model = lm(inlf ~ nwifeinc + educ + exper + expersq + age + kidslt6 + kidsge6,data=datab)
```

```
-Stata-
* Open the dataset
use http://fmwww.bc.edu/ec-p/data/wooldridge/mroz, clear

probit inlf nwifeinc educ exper expersq age kidslt6 kidsge6
estimates store probit_model

logit inlf nwifeinc educ exper expersq age kidslt6 kidsge6
estimates store logit_model

```
{{% /codeblock %}}

## Calculating the Average Marginal Effect (AME)

In either model, the estimated effect of the explanatory variables on the outcome variable (i.e.: the increase or decrease in probability of being in the labor force) is not constant, but depends on the specific value of the explanatory variable. One standard way to report marginal effects in this situation is to calculate the Average Marginal Effect (AME), that is computing the marginal effect at the regressors value for each observation and then averaging out for the whole sample.

{{% codeblock %}}
```R

# AME is the default option for the margins package in R

probit_AME = margins(probit_model)
logit_AME = margins(logit_model)

# To obtain a table reporting the values use:
summary(probit_AME)
# or equivalently
margins_summary(probit_model)

# Comparing AME for Probit and Logit against the OLS coefficients:

# Probit AME
plot(probit_AME)
# Add Logit AME
points(1:length(summary(logit_AME)$AME)+0.1,summary(logit_AME)$AME,col="blue",pch=16)
invisible(sapply(1:length(summary(logit_AME)$AME),FUN=function(x) lines(c(x+0.1,x+0.1),c(summary(logit_AME)$lower[x],summary(logit_AME)$upper[x]),col="blue")))
# OLS average marginal effects are equal to the estimated coefficients
ols_AME = margins(ols_model)
points(1:length(summary(ols_AME)$AME)+0.2,summary(ols_AME)$AME,col="red",pch=16)
invisible(sapply(1:length(summary(ols_AME)$AME),FUN=function(x) lines(c(x+0.2,x+0.2),c(summary(ols_AME)$lower[x],summary(ols_AME)$upper[x]),col="red")))

legend("bottomleft",legend=c("Probit","Logit","OLS"),col=c("black","blue", "red"),lty=1,box.lty=0)
```

```
* To refer to the models above use estimates restore
* alternatively, you could run the probit or logit models again
* and then the margins postestimation command

estimates restore probit_model
margins, dydx(*)

estimates restore logit_model
margins, dydx(*)

```
{{% /codeblock %}}

## Marginal Effect at different value of the regressors

Alternatively, marginal effects can also be reported at given values of the regressors, which are of particular interest. For example the Marginal Effect at the Mean (MEM) gives the marginal effects at the mean values for all regressors. 

{{% warning %}}
Analyzing the effect at the mean is not always desirable:
- If an explanatory variable has very skewed values, the average can be not very representative of the whole sample.
- If the explanatory variable is in itself binary, for example a dummy detailing if there is any children in the household, it is not easy to interpet what the marginal effect at the mean represents.
{{% /warning %}}


