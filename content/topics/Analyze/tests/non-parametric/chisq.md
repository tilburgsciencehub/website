---
title: "Chi-Squared Test"
description: "Short guide to understanding the workings of the Chi-Squared test for independence and goodness of fit, and how to use it in R"
keywords: "chi, goodness, indep, test, nominal, binary, disc, R "
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
The Chi-Squared test can be used when you are dealing with a **nominal** measurement scale with a **single** sample (**binary** data) or **two independent** samples with **discrete** data. With binary data, you use **Chi-squared test of goodness of fit**. It tests whether a significant difference exists between an observed number of outcomes falling in each category and an expected number based on the null hypothesis (goodness of fit). With two independent samples, you use the **Chi-squared test of independence**. It tests whether the two groups differ concerning the relative frequency with which group members fall into several categories. For both these tests, R offers an inbuilt test called the `chisq.test()`.

In this building block, we will describe how this code works for both these tests.

## Understanding chisq.test ()
In R, `chisq.test()` performs the chi-squared test of goodness of fit and chi-squared test of independence. The syntax of the test is as follows:

{{% codeblock %}}
```r
chisq.test( x, y = NULL,
            correct = TRUE,
            p = rep(1/length(x), length(x)),
            rescale.p = FALSE)
{{% /codeblock %}}

Where:
- *x* is a numeric vector or matrix that provides the observed frequencies.
- *y* describes another numeric vector with the same length as x. It is ignored for the test of goodness of fit or when *x* is a matrix.
- *correct* is a boolean that indicates whether to apply continuity correction when computing the test statistic for a 2x2 table. The default is set to be TRUE.
- *p* is a vector of probabilities of the same length of x.
- *rescale.p* is a boolean; if TRUE p is rescaled (if necessary) to sum to 1.
 It is set to FALSE by default.


## Test of goodness of fit
The chi-squared goodness of fit test is used to compare the observed distribution (Oi) to an expected distribution (Ei), in a situation where there are two or more categories in discrete data. The hypothesis is set as:
- H0: Oi = Ei
- H1: Oi ≠ Ei

As an example, suppose you gathered 40 wild tulips and observed that 20 were red, 15 were yellow and 5 were white, you can use the goodness of fit test to analyse if these three colours were equally common, i.e. the expected proportion of each colour was 1/3.

In this case, for the R code, you only need two arguments: *x* and *p*.

{{% codeblock %}}
```R
# Create a vector for the observed frequencies
tulip <- c(20,15,5)

# Run the test
chisq.test(tulip, p = c(1/3, 1/3, 1/3))

{{% /codeblock %}}


The output of this code gives the value of the chi-square statistic which is equal to **8.75** and the degrees of freedom (df) which equals one less than the number of categories. Since we have three colours, the df is **2**.

You need the df to look up the critical chi-square value for a certain significance level (alpha) using a distribution table or an online calculator. This is approximately equal to **6** if you take alpha equal to **0.05**.

Since the critical value (6) is smaller than the chi-square statistic (8.75), you can **reject** the null hypothesis and conclude that there is a **significant** difference between the observed and expected frequencies at a 5% significance level. Therefore, the colours are significantly not commonly distributed.

The R output also gives the p-value which you can compare with alpha to make the conclusion. If the p-value is **less than or equal** to the chosen alpha, you **reject** the null hypothesis. In our case, the **p-value is 0.013**  which is less than 0.05, verifying our previous analysis.


## Test of independence
The chi-squared test of independence is used to determine if two categorical variables have a significant correlation between them. A common example is checking the effectiveness of a new drug. Suppose you have 105 patients in a study out of which 50 were treated with the new drug and 55 were not. You record if these patients observed an improvement and obtain the following contingency table, let us call it 'drug_effectiveness':

|         |           | **Improvement** |     |
|:-----| :------  | :---------  |  :---------|
|      |           | **Yes** | **No** |
|Treatment|  **No**   |  26 | 29      |
|          |  **Yes**   |  35 | 15    |

You can read the dataset yourself by running the following code:

{{% codeblock %}}
```R
data_frame <- read.csv("https://goo.gl/j6lRXD") #Reading CSV
drug_effectiveness <- table(data_frame$treatment, data_frame$improvement)

{{% /codeblock %}}


The hypothesis will be set as:

- H0: The drug treatment and improvement are independent
- H1: Treatment and improvement are not independent; the drug is effective.

To run this test on R, you additionally need two other arguments: *y* and *correct*. *x* and *y* indicate the variables that you are comparing which in our case are 'Treatment' and 'Improvement' respectively, and *correct* is set `FALSE` to turn off Yates’ continuity correction.

{{% codeblock %}}
```R
chisq.test(data_frame$treatment, data_frame$improvement, correct=FALSE)

{{% /codeblock %}}

Another way of running this test is to assign the contingency table matrix, 'drug_effectiveness' to *x*, as follows:

{{% codeblock %}}
```R
chisq.test(drug_effectiveness, correct=FALSE)

{{% /codeblock %}}

The output of these codes gives the value of the chi-square statistic which is equal to **5.56** and the df equal to **1**. The critical chi-square value at alpha equal to 0.05 is **0.02**.

Since the p-value is smaller than 0.05, you can **reject** the null hypothesis. Thus, there is **sufficient evidence** to conclude a significant dependence of the drug treatment on the improvement implying that the drug is effective at a 5% significance level.



{{% summary %}}

- The chi-squared goodness of fit is apt for binary and nominal data.

- The chi-squared test of independence is used when you have two independent samples.

- These tests can be performed on R using its inbuilt test `chisq.test()`


{{% /summary %}}
