---
title: "Interaction in Regression Analysis"
description: "Interpreting and coding interaction terms in R. Various scenarios will be discussed involving continuous and discrete independent variables, continuous and discrete dependent variables, with and without control variables. Specifically for the discrete variables, binary and multilevel interaction terms are explained."
keywords: "R, regression, interpretation, interaction, discrete, continuous, multilevel, binary"
draft: false 
weight: 11
author: "Matthijs ten Tije"
authorlink: "https://tilburgsciencehub.com/contributors/matthijstentije/"
aliases:
  - /regression
  - /Interpretation
  - /regressioninterpretation
  - /interaction terms
  - /r
  - /logistic
  - /dummyvariable
---

## Overview 

### What are Interaction Terms
In a standard regression analysis, you use an explanatory variable (X) to understand how it influences the dependent variable (Y).   
However, when you introduce an `interaction term` into the regression, you are adding an extra layer to this relationship. The main idea is that the relationship between X and Y is not solely determined by X; it also varies with another variable, which we'll call Z. An interaction term is included in the regression when you multiply together two different variables and include their product in the regression. The model is now called a `fully interacted model`.


{{<katex>}}
 Y = \beta_0 + \beta_1 X + \beta_2 Z + \beta_3 X Z + \epsilon
 {{</katex>}}


### Interpretation
The concept of `interaction terms` can be best explained with calculus. It answers the question: "What is the impact of X when it interacts with another variable, Z?" 
The answer can be found by taking the `derivative` of the main formula. We take out of the regression equation, the derivative with respect to X. That's it!  

So, The `fully interacted model`:

{{<katex>}}
 Y = \beta_0 + \beta_1 X + \beta_2 Z + \beta_3 X Z + \epsilon
 
{{</katex>}} 

and its derivative: 

{{<katex>}}
 \frac{\partial Y}{\partial X} = \beta_1 + \beta_3 Z 
{{</katex>}}


This represents the effect of X on Y, which is now conditional on Z! For those unfamiliar with calculus, look how we just took the terms with an X including $\beta_1 X$ and $\beta_3 X Z$ and took out the X, leaving us with the expression above. 

Notice how the effect of X is contingent on Z. There is not a single effect of X on Y. Rather, we state the effect of X at a given value of Z.  
Consequently, individual coefficients like $\beta_1$ no longer convey "the effect of X." When examining `effect size`, we must account for the complete influence.

The interpretation of the interaction term, which is $\beta_3$, is as follows: 
In the derivative we discussed earlier, where we explained the effect of X on Y, the interaction term simplifies to $\beta_3 Z$.  Now, the coefficient $\beta_3$ tells us how our prediction of $\frac{\partial Y}{\partial X}$ changes when Z increases by one unit.  
In other words, $\beta_3$ quantifies how much stronger the effect of X on Y becomes when Z increases by one unit. 

### Word of caution 
Using interaction terms can increase the likelihood of detecting significant effects, but it can also lead to a random significance, especially with numerous covariates. To maintain research credibility, avoid a "`fishing expedition`" approach. Recognize the exploratory nature of interaction effects and document all analyses. Consider machine learning techniques like `causal forests` or use a `factorial design` with limited comparisons. 

## Scenario Analyses 
In this section, we will perform multiple regression analyses, each illustrating a different scenario. We will explore scenarios involving `continuous` and `discrete` `independent variables`, `continuous` and `discrete` `dependent variables`, and models with and without control variables. Additionally, when examining discrete variables, we will explore interactions in both `binary` and `multi-level` contexts.

The scenario analysis will use a public dataset CPS1988, which is open source and can be downloaded using the AER package in R. It contains cross-section data originating from the March 1988 Current Population Survey by the US Census Bureau.

It contains the following variables: 
- Wage: Dollars per week.
- Education: Number of years of education.
- Experience: Number of years of potential work experience.
- Ethnicity: Factor with levels "cauc" and "afam" (African-American).
- Smsa: Factor. Does the individual reside in a Standard Metropolitan Statistical Area (SMSA)?
- Region: Factor with levels "northeast", "midwest", "south", "west".
- Parttime: Factor. Does the individual work part-time?

**Short remark**: CPS data lacks direct work experience information, so a common workaround is to estimate potential experience as age minus education minus 6. This method can result in negative experience values for some respondents.

{{% codeblock %}} 
```R 
# Loading in the dataset
data("CPS1988", package = "AER") 
```
{{% /codeblock %}} 

### 1. Discrete Binary Independent variable without controls
To construct a regression model with interaction effects in R, we must incorporate interaction terms into our model. 
We use an asterisk "*" to denote the interaction term, and R will automatically include both separate variables involved in the interaction in the regression model.

Here, we're studying a model that tries to understand how a person's wage (Y) is affected by their level of education (X). We're also looking into whether a person's ethnicity (Z) plays a role in mediating or influencing this relationship. 
 Notice that ethnicity is a binary indicator, separating the data into two groups. 

{{% codeblock %}} 

```R
# Create discrete binary independent variables
CPS1988$ethnicity <- ifelse(CPS1988$ethnicity == "afam", 1, 0)
CPS1988$parttime <- ifelse(CPS1988$parttime == "yes", 1, 0)
CPS1988$smsa <- ifelse(CPS1988$smsa == "yes", 1, 0)

# Regression 1
reg1_Short <- lm(wage ~ education * ethnicity, data = CPS1988)
summary(reg1_Short)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/regression-3-intr.png" width="400">
</p>

The interpretation of the regression output is as follows:
Based on this specific dataset and model, we observe that a one-year increase in education is associated with an expected wage increase of 47.366 dollars ($\beta_1$).

However, it's important to note that this relationship is influenced by a person's ethnicity, look at the significance level of the interaction term. For African Americans, each additional year of education leads to an expected wage increase of 32.001 dollars ($\beta_1 + \beta_3$). which is calculated as 47.366 (the effect of education for the general population) plus -15.365 (the interaction effect for African Americans).



{{% tip %}} 

A common method for visualizing how variable Z affects the relationship between X and Y is by creating a marginal effect plot. You can find a brief introduction to this concept here: [building block](https://tilburgsciencehub.com/building-blocks/analyze-data/regressions/marginal-effect-r/). In this discussion, I will utilize the R package called "interflex," which enables us to generate marginal effect plots.

{{% /tip %}} 

{{% codeblock %}} 
```R
install.packages('devtools', repos = 'http://cran.us.r-project.org') 
devtools::install_github('xuyiqing/interflex')
marginal_effect_plot <- interflex(Y = "wage", D = "education", X = "ethnicity", bin.labs = F, data = CPS1988, estimator = "linear")
plot(marginal_effect_plot)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/interflex-reg1-intr.png" width="400">
</p>

The command first estimates a model and then displays the marginal effect plot. 
In this instance, I utilized a linear estimator. Y represents the outcome variable, D represents the treatment variable, X stands for the moderator (our interaction variable), and Z represents the covariates in the model.  
Furthermore, interflex provides the option for fixed effects and clustering of standard errors. It's important to note that the model also displays the confidence interval and the distribution of the moderating variable. In this case, the moderating variable is binary, as expected. 

### 2. Discrete Multilevel Independent variable without controls
The independent variable doesn't have to be binary (0 or 1); it can also be multilevel, taking on various values or categories. For example, it could represent different levels of education, such as primary school, secondary school, or tertiary school.

To implement this kind of multilevel variable in R, it's essential to inform R that you're working with a factorial or categorical variable with distinct levels. Additionally, you should specify which level will serve as the reference or baseline group, against which the relationships with other levels will be compared.

In the case of a binary variable, like the one displayed above, the reference group is often the 0 value, and the regression output will provide information about the differences in relationships compared to this baseline group.

{{% codeblock %}}
 ```R
# Create a discrete multilevel independent variable "region"
CPS1988$region <- factor(CPS1988$region)
CPS1988$region <- relevel(CPS1988$region, ref = "south")
```

{{% /codeblock %}}



Here, we're studying a model that tries to understand how a person's wage (Y) is affected by their level of education (X). We're also looking into whether a person's living region (Z) plays a role in moderating or influencing this relationship. Notice that a person's region is a categorical variable, separating the data into different groups. 

{{% codeblock %}}

```R
reg2 <- lm(log(wage) ~ education * region, data = CPS1988)
summary(reg2)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/regression-2-intr.png" width="400">
</p>

The interpretation of the regression output is as follows, notice that we transformed the wage into a logarithmic scale. For how to interpret a Log-Linear model, see this building block: LINK.  
Based on this specific dataset and model, we observe that a one-year increase in education is associated with an expected wage increase of 7.98\% ($\beta_1$ * 100\%), at a 1 per cent significance level. 

However, it's important to note that this relationship is influenced by a person's region, look at the significance level of the interaction term of the north-east and mid-west. We observe different conditional average treatment effects for each region:

The estimated average treatment effect for individuals from the South is 7.98\% ($\beta_1$).
For individuals from the North-East, the estimated average treatment effect is 7.04\% (0.079842 - 0.009422).
Individuals from the Mid-West have an estimated average treatment effect of 6.55\% (0.079842 - 0.014336).
In the case of individuals from the West, the estimated average treatment effect is 7.85\% (0.079842 - 0.001337), and it's not statistically significant at the 5\% level, indicating no significant difference in the relationship between education and wage from people in the south and the west.


### 3. Continuous Independent Variable
Here, we're studying a model that tries to understand how a person's wage (Y) is affected by their level of education (X). We're also looking into whether being a more experienced worker (Z) plays a role in moderating or influencing this relationship. 

{{% codeblock %}}

```R
reg3 <- lm(log(wage) ~ education*experience, data = CPS1988)
summary(reg3)

marginal_effect_plot <- interflex(Y = "wage", D = "education", X = "experience" , data = CPS1988, estimator = "binning", bin.labs = T,  wald = TRUE)
print(marginal_effect_plot$tests$p.wald)
plot(marginal_effect_plot)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/regression-3-intr.png" width="400">
</p>

<p align = "center">
<img src = "../images/interflex-reg3-intr.png" width="400">
</p>

Here the marginal effect plot provides valuable insights into the model's accuracy.  
By using the "binning" argument in the estimator, we break down the interaction term into groups and calculate the interaction effect for each group. This reveals that the relationship seems to be non-linear. The marginal effect plot offers additional information that isn't available from the summary of the regression alone.  
To confirm the significance, you can use the Wald test within the interflex function. The Wald test compares the linear interaction model to the more flexible binning model. The null hypothesis is that the linear interaction model and the three-bin model are statistically equivalent. If the p-value of the Wald test is close to zero, you can confidently reject the null hypothesis.  For our example, this is the case!

### 4. Discrete Dependent Variable
When dealing with a discrete dependent variable like a count or binary variable (0 or 1), you can still calculate and interpret the effects of interaction terms. However, the approach for estimating and interpreting these effects may vary depending on the type of dependent variable. Let's explore how to compute the effects of interaction terms for binary dependent variables, as seen in logistic regression.

In this scenario, we are analyzing a logistic regression model that aims to determine whether a person's African American background (Y) can be predicted based on their wage (X). Additionally, we are investigating whether a person's residence in a metropolitan area moderates this relationship. We will run our logistic regression using glm with family=binomial.

{{% codeblock %}}

```R
reg4 <- glm(ethnicity ~ wage * smsa, family = binomial, data = CPS1988)
summary(reg4)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/regression-4-intr.png" width="400">
</p>

In our output, coefficients are initially in log odds. Think of log odds as a way to measure the odds of an event happening using natural logarithms, allowing for a linear connection with predictors. To draw meaningful conclusions, we often prefer odds ratios. These help us understand how much more or less likely an event becomes when one variable changes versus staying the same.
In logistic regression, odds ratios are essential. They quantify how a one-unit change in a predictor impacts the odds of our outcome variable falling into a specific category, making our statistical findings more practical.

{{% codeblock %}}

```R
log_odds <- coef(reg5)
exp(log_odds)
(exp(log_odds)[4]-1) * IQR(CPS1988$wage) #Coefficient of interaction terms multiplied by the IQR range of gap of the wage distribution
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/log-odds-regression-5-intr" width="400">
</p>


For an individual not residing in a metropolitan area, each one-unit increase in wage is associated with an expected decrease in the odds of being an African American by approximately 0.27463\%. However, living in a metropolitan area raises the odds of 0.14\% for a unit increase in wage. What does this mean in practical terms? Let's consider a person at the 75th percentile of the wage distribution. If this individual lives in a metropolitan area, they are approximately 8.59\% more likely to be African American compared to if they did not live in a metropolitan area.

### 5. Continuous Dependent Variable with controls
Let's examine a full regression model where we aim to explain wages (transformed logarithmically). We include several predictor variables: experience, experience squared (to account for diminishing returns), education, part-time status, ethnicity, metropolitan area, and region.

Additionally, we want to explore if higher education can help narrow the wage gap for African Americans. Specifically, we're interested in whether the impact of being African American on wages is less pronounced for individuals with higher levels of education.

{{% codeblock %}}

```R
# Regression 
CPS1988$experience2 <- CPS1988$experience^2 # Create a new variable 
full_model_interacted <- lm(log(wage) ~ education * ethnicity + experience +  experience2  + region +  smsa + parttime, data = CPS1988)
summary(full_model_interacted)

# Marginal effect plot 
marginal_effect_plot <- interflex(Y = "wage", D = "ethnicity", X = "education", Z = c("experience2", "smsa","parttime","region"),
                                  data = CPS1988, estimator = "linear")
plot(marginal_effect_plot)
```
{{% /codeblock %}} 

<p align = "center">
<img src = "../images/regression-5-intr.png" width="400">
</p>

<p align = "center">
<img src = "../images/interflex-reg5-intr.png" width="400">
</p>

By examining the p-value linked to the interaction term coefficient, which is 0.0254, we can conclude that the interaction term is statistically significant at the 5\% significance level. This suggests strong evidence supporting the existence of an interaction between education and ethnicity. However, we also need to determine whether this interaction is practically meaningful. To do so, we compare the variance explained, represented by R-squared, in the model with interaction terms to that in the model without interaction terms.

{{% codeblock %}}

```R
full_model_interacted <- lm(log(wage) ~ education * ethnicity + experience +  experience2  + region +  smsa + parttime, data = CPS1988)
summary(full_model_interacted)
full_model_without_interaction <- lm(log(wage) ~ education + ethnicity + experience +  experience2  + region +  smsa + parttime, data = CPS1988)
summary(full_model_without_interaction)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/regression-6-intr.png" width="400">
</p>

<p align = "center">
<img src = "../images/regression-7-intr.png" width="400">
</p>

In this instance, the model without interaction accounts for 45.72\% of the wage variance, while the model with interaction explains 45.73\% of the wage variance. This implies that the interaction only explains an additional 0.01\% of the wage variance, which is a negligible effect.


## Summary

{{% summary %}}
This building block explains `interaction terms` in regression analysis, their mathematical interpretation, and their practical applications in various scenarios. The key points covered include:

1. **Interaction Term Introduction**: Interaction terms add complexity to the relationship between an `independent variable` (X) and a `dependent variable` (Y) by considering how this relationship changes based on the value of another variable (Z).

2. **Scenario Analysis**: The article explores different scenarios involving `continuous` and `discrete` independent and dependent variables. It covers models with and without control variables and examines interactions in `binary` and `multi-level` contexts.

3. **Significance and Relevance**: The article emphasizes the importance of assessing both the `statistical significance` and practical relevance of interaction terms. 


{{% /summary %}}