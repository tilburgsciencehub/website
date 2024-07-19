---
title: "Handling Categorical Variables in R"
description: "This article shows how to handle and analyze categorical variables in R."
keywords: "R, categorical variables, data analysis, regression, factors, relevel"
draft: false
weight: 3
author: "Matthijs ten Tije"
aliases:
  - /categorical/variables
  - /factor/r
---

## Overview
in data analysis, you often come across **categorical variables** that group data into specific categories. Properly handling these variables is important for accurate analysis and interpretation, but it does require some understanding of how to interpret and restructure them. This article will walk you through the process of working with categorical variables in `R`.

We will make use of the `PIAAC` dataset. With this dataset we can investigate the impact of education level, gender, and proficiency in the national language on hourly earnings. You can download the dataset using this link:

{{% codeblock %}}

```R
data_url <- https://raw.githubusercontent.com/content/topics/Manage-manipulate/manipulate-clean/numerical/PIAAC.csv
load(url(data_url))
```

{{% /codeblock %}}

## Interpreting Regression Coefficients for Categorical Variables
A common goal when analyzing categorical is to quantify differences in an outcome variable across various groups, represented by different levels of a categorical variable. For instance, for the `PIAAC` dataset we might want to know:

- What is the impact of education level on hourly earnings?
- Does gender influence hourly earnings?
- How does being a native speaker affect hourly earnings?

These questions focus on comparing a situation of interest against a baseline scenario. 

{{% example %}}

Let's say you are currently researching the effect of gender, education level, and proficiency in the national language on income. You have come across the following regression:

<p align = "center">
<img src = "../images/regression-categorical-data-1.png" width="400">
</p>

If you look at the estimates, you'll see that `EducationlevelLow` and `EducationlevelMedium` have negative coefficients. This means that individuals with low education, represented by `EducationlevelLow`, earn significantly less compared to... This cannot be inferred from the regression output.

When you open the data, you will see that the education level variable contains three levels, including High. 

{{% /example %}}

{{% codeblock %}}

```R
unique(data$Educationlevel) # Low - Medium - High
```

{{% /codeblock %}}

{{% example %}}

However, the value `High` of the variable `Educationlevel` is missing a coefficient. This indicates that it is the **baseline**, and all other coefficients should be interpreted relative to it. Therefore, `EducationlevelHigh` is the **reference level** for the response variable, meaning the coefficients are associated with predicting income relative to a person who is highly educated.

Similarly, `NativespeakerYes` indicates a positive coefficient for being a native speaker on income. However, wouldn't it make more sense to look at the effect on income when you are a non-native speaker? 

{{% /example %}}

### Refactoring Categorical Variables with Meaningful Reference Levels

To improve the interpretability of our regression model on hourly earnings, we can **refactor** variables to use more meaningful and intuitive reference levels. First, we'll need to explicitly convert our variables into the `factor` data type, and then we can use the `relevel()` command to define 'reference levels' that make more intuitive sense.

{{% codeblock %}}
```R
# Checking the data type of the variables of interest
class(data$Gender)  # Character
class(data$Nativespeaker)  # Character
class(data$Educationlevel)  # Character

# Conversion to a factor data type
data$Gender <- as.factor(data$Gender)
data$Nativespeaker <- as.factor(data$Nativespeaker)
data$Educationlevel <- as.factor(data$Educationlevel)

# Relevel the factor
data$Gender <- relevel(x = data$Gender, ref = "Male")
data$Nativespeaker <- relevel(x = data$Nativespeaker, ref = "Yes")
data$Educationlevel <- relevel(x = data$Educationlevel, ref = "Low")

# Or more efficiently using dplyr
data <- data %>%
  mutate(Gender = relevel(factor(Gender), ref = "Male"),
         Nativespeaker = relevel(factor(Nativespeaker), ref = "Yes"),
         Educationlevel = relevel(factor(Educationlevel), ref = "Low"))
```
{{% /codeblock %}}

In the background, R creates 'dummy variables' - each 'level' of a categorical variable, for example the `High`, `Medium` and `Low` categories of `Educationlevel` is turned into its own variable, which is either 0 or 1. These are then handled using a 'treatment contrasts scheme'; one level is designated the "baseline", and coefficients are computed for the rest.

If we run the same regression, these are our results now:

<p align = "center">
<img src = "../images/regression-categorical-data-2.png" width="400">
</p>

## Using the factor() Function in R
As discussed above, we use the `factor()` function to create factors, which are data structures used to categorize and store categorical data.

General Syntax:
`factor(x, levels, labels, ordered = FALSE)`
- _x_: A vector of data, usually a character vector.
- _levels_: A vector of unique values that x can take. If not provided, levels are determined from x.
- _ordered_: Logical flag indicating if the levels should be treated as ordered.

#### Structure of Factors
Factors have levels and can be ordered or unordered. The `str()` function can be used to inspect the structure of a factor:

{{% codeblock %}}
```R
str(data$Educationlevel)
# Output: Factor w/ 3 levels "Low","High","Medium": 2 2 2 2 2 2 2 2 2 3 ...
```
{{% /codeblock %}}

#### Ordering Levels
By default, `levels` are unordered. As you can see, `R` does not automatically understand that "`High`" education should be a higher category than "`Medium`" education. However, you can create ordered factors:

{{% codeblock %}}
```R
data$Educationlevel <- factor(data$Educationlevel, levels = c("Low", "Medium", "High"), ordered = TRUE)
str(data$Educationlevel)
# Output: Ord.factor w/ 3 levels "Low"<"Medium"<..: 3 3 3 3 3 3 3 3 3 2 ..
```
{{% /codeblock %}}

### Converting Continuous Variables to Categorical Variables
So far, we have only discussed **discrete variables** like `Gender`, `Nativespeaker`, and `Educationlevel`. However, the dataset contains the variable `age`, which is a **continuous variable**. We can adapt the above code to create a dichotomous variable indicating whether an individual is an adult or not.

{{% codeblock %}}
```R
data <- data %>% 
  mutate(adult = as.numeric(Age >= 21))

class(data$adult)  # numeric
unique(data$adult) # 1 or 0
```
{{% /codeblock %}}

A multiple-level categorical variable can be created with `case_when()`. Each argument within `case_when()` is **condition ~ value**, where if a condition is met, a value is assigned. Anything not covered by any of the conditions we provide is assigned a value of **NA**.

We can turn a continuous variable like experience into distinct categories:

{{% codeblock %}}
```R
data <- data %>% 
  mutate(experience_categories = case_when(experience < 0 ~ "Studying", 
                                           experience == 1 | experience == 2  ~ "Starter", 
                                           experience > 2  & experience <= 10 ~ "Average", 
                                           experience > 10 ~ "Experienced"))
```
{{% /codeblock %}}

We can use this `experience_categories` variable as a predictor in a statistical model or for creating histograms of income by work experience.

{{% summary %}}

In this article, we have demonstrated that R automatically creates reference levels in a regression model. We have explored how to interpret regression coefficients for `categorical variables` by comparing groups to a baseline level. Subsequently, we have used the `factor()` and `relevel()` functions to set specific reference levels for categorical variables. Additionally, we have revisited the `factor()` function to categorize and store categorical data, and we have focused on creating ordered factors using the `level` argument. Finally, we converted continuous variables into categorical variables using the `case_when()` function.

{{% /summary %}}