---
title: "Chi-Squared Test"
description: "Short guide to understanding the workings of the Chi-Squared test for independence and goodness of fit, and how to use it in R"
keywords: "chi, test, nominal, bin, disc, goodness, indep, R "
weight: 2
date:
draft: false
author: "Aakriti Gupta"
aliases:
  - /chi-squared test
  - /Chi-Squared Goodness of Fit test
  - /Chi-squared test of independence
---

## Overview
The Chi-Squared test can be used when you are dealing with **nominal** measurement scale with a **single** sample (**binary** data) or **two independent** samples with **discrete** data. With a binary data, you use **Chi-squared test of goodness of fit**. It tests whether a significant difference exists between an observed number of outcomes falling in each category and an expected number based on the null hypothesis (goodness of fit). With two independent samples you use **Chi-squared test of independence**. It tests whether the two groups differ with respect to the relative frequency with which group members fall into several categories. For both these tests, R offers an inbuilt test called the `chisq.test()`.

In this building block we will describe how this code works for both these tests. Let's first look at an example for goodness of fit test.

## Is your ice-cream preference same as the expected distribution?
Suppose you conduct a survey asking 200 people about their preferred ice-cream flavors. You want to test whether the distribution of preferred flavors in your sample matches a theoretical distribution based on industry standards, which is as follows:
- Chocolate: 40%
- Vanilla: 30%
- Strawberry: 15%
- Mint: 10%
- Other: 5%

Using this data we can compute the **expected distribution** for category i (Ei) as 200 times the expected percentage of preference for each ice-cream flavour. For example, for chocolate it will be 0.4*200 = 80.

|      |  Chocolate   | Vanilla | Strawberry | Mint | Other              |
|-------------|---------------|--------------|---------------| ------- | ----  |
|     Ei   |  80 |  60 |  30 |  20 |  10             |




Moreover, from the survey, you collect the following data:

|      |  Chocolate   | Vanilla | Strawberry | Mint | Other              |
|-------------|---------------|--------------|---------------| ------- | ----  |
|     Oi   |  70 |  60 |  30 |  20 |  20             |


We will refer to this as the **observed distribution** for category i (Oi).

### Hypothesis testing
To statistically test for this case, we first describe the hypotheses. The null hypothesis (H0) states that the observed distribution of ice-cream flavors in the sample matches the expected distribution and the alternative hypothesis (H1) states that the observed distribution in the sample is significantly different from the expected distribution. Hence, we have:

- H0: Oi = Ei
- H1: Oi ≠ Ei

### Testing this in R
R offers a built-in function called `chisq.test()`, which efficiently performs the chi-squared goodness of fit test, making it a reliable and time-saving tool.

Let's have a quick look at how it works for our given example.
{{% codeblock %}}
```r
# Create a data frame with observed counts
observed <- data.frame(
  Flavor = c("Chocolate", "Vanilla", "Strawberry", "Mint", "Other"),
  Count = c(70, 60, 30, 20, 20)
)


# Expected probabilities based on null hypothesis
expected_prob <- c(0.4, 0.3, 0.15, 0.1, 0.05)

# Total count
total <- sum(observed$Count)

# Calculate expected counts
expected <- total * expected_prob
print(expected)

# Perform chi-square test
chi_square_test <- chisq.test(observed$Count, p = expected_prob)

# Print the result
print(chi_square_test)

{{% /codeblock %}}


The output of this code, gives the value of the chi-sqaure statistic which is equal to **11.25** and the degrees of freedom (df) which equals one less than the number of categories. Since we have 5 ice-cream flavours, the df is **4**.


You need the df to lookup the critical chi-square value for a certain significance level (alpha) using a distribution table or an online calculator. This is approximately **9.49** if you take alpha equal to **0.05**.

Since, the critical value(9.49) is smaller than the chi-square statistic(11.25), you can **reject** the null hypothesis and conclude that there is a **significant** difference between the observed and expected ice-cream preferences at 5% significance level.

The R output also gives the p-value which you can compare with alpha to make the final conclusion. If the p-value is **less than or equal** to the chosen alpha, you **reject** the null hypothesis. In our case, the **p-value is 0.02**  which is less than 0.05, verifying our previous analysis.

### Understanding chisq.test ()

{{% codeblock %}}
```r
chisq.test( x,
            p = rep(1/length(x), length(x)),
            rescale.p = FALSE)
{{% /codeblock %}}

The syntax of the `chisq.test()` includes two important arguments:
- **x**: A numeric vector that provides the observed frequencies. In our case it is the variable, *Count*.
- **p**: A vector of probabilities of the same length of x.
- **rescale.p**: A logical scalar; if TRUE p is rescaled (if necessary) to sum to 1. It is set to FALSE by default.


## Chi-squared test with two independent samples
Suppose you are interested in studying the relationship between smoking status (smoker or non-smoker) and the occurrence of a respiratory condition (yes or no). Assuming that the observations of these categorical variables are independent, you can use the `chisq.test` to perform the **chi-sqaured test of independence**. This test is often referred to as the test of contingency or simply the contingency test. The term "contingency" in this context reflects the idea that the test is used to examine whether there is a contingency (association or dependence) between two categorical variables. So, this test is usually used when you have data in a form of a contingency table (matrix).

### Usage in R
When using `chisq.test()` for test of independence, you need two other arguments in addition to the ones mentioned before:
- **y**: It describes the other numeric vector with the same length as x.

{{% warning %}}
y should be ignored if x is a matrix.

{{% /warning %}}

- **correct**: A logical indicating whether to apply continuity correction when computing the test statistic for a 2x2 table. The default is set to TRUE.

Before we look at how this works on R, let us first create our hypothetical data set.

{{% codeblock %}}
```r
# Create a hypothetical dataset
set.seed(123)  # for reproducibility
n <- 200  # number of observations

smoking_status <- sample(c("Smoker", "Non-Smoker"), n, replace = TRUE)
respiratory_condition <- sample(c("Yes", "No"), n, replace = TRUE)

# Combine into a data frame
my_data <- data.frame(Smoking = smoking_status, RespiratoryCondition = respiratory_condition)

# Create a contingency table
contingency_table <- table(my_data$Smoking, my_data$RespiratoryCondition)

# Print the contingency table
print(contingency_table)

{{% /codeblock %}}

The contingency table will look like this:

|           | **No**     | **Yes** |
| :------  | :---------  |  :---------  |
|  **Non-smoker**   |  38 | 59      |
|  **Smoker**   |  54 | 49    |

and the hypothesis will be set as:


H0: Smoking status and respiratory condition are independent


H1: Smoking status and respiratory condition are not independent; there is an association.

Now let's see how to use the test in R.

{{% codeblock %}}
```r
# Perform a chi-squared test of independence
chi_square_result <- chisq.test(contingency_table)

# Print the result
print(chi_square_result)


{{% /codeblock %}}

The output of this code, gives the value of the chi-sqaure statistic which is equal to **3.0184** and the df is **1**. The critical chi-square value at alpha equal to **0.05** is **3.841**.

Since, the critical value is not smaller than the chi-square statistic, you cannot **reject** the null hypothesis. Thus, there is **not sufficient evidence** to conclude a significant dependence of smoking on a person's respiratory condition.



{{% summary %}}

- The chi-squared goodness of fit is apt for binary and nominal data.

- The chi-squared test of independence is used when you have two independent samples.

- These test can be performed on r using its inbuilt test `chisq.test()`


{{% /summary %}}
