---
title: "Wilcoxon test"
description: "Short guide to understanding the workings of the One-sample Wilcoxon signed-rank test, Wilcoxon matched pairs test and Wilcoxon rank-sum test on R."
keywords: "Wilcox, Mann, Whitney, signed, rank, sum, test, ordinal, discrete, continuous, R "
weight: 4
date:
draft: false
author: "Aakriti Gupta"
authorlink: "https://nl.linkedin.com/in/aakriti-gupta-91450821b"
aliases:
  - /Wilcoxon Test
  - /Wilcoxon Signed-Rank Test
  - /Wilcoxon Matched-Pairs Signed Ranks Test
  - /Wilcoxon Rank-Sum Test
  - /Mann-Whitney-U test
  - /One-sample Wilcoxon signed-rank test
---

## Overview
The Wilcoxon test is a non-parametric alternative to the t-test for comparing averages in one or two (dependent or independent) samples. In this building block, you will learn how to compute the different types of Wilcoxon tests: One-sample Wilcoxon signed rank test, Wilcoxon matched-pairs test and Wilcoxon rank sum test (Mann-Whitney U test) on R using `wilcox.test()`.

## One-sample Wilcoxon signed-rank test
The one-sample Wilcoxon signed-rank test is used to assess whether the median of the sample is equal to a known standard or theoretical value. It is a non-parametric test equivalent to a one-sample t-test and is appropriate for continuous and ordinal data. To perform this test on R, you can use the inbuilt function `wilcox.test()`, in the following way:

{{% codeblock %}}
```R
wilcox.test(x, mu = 0,
  alternative = “two.sided”,
  exact = NULL,
  correct = TRUE)
```
{{% /codeblock %}}

where:
- *x* denotes a numeric vector containing your data values.
- *mu* is the theoretical mean/median value. The default is 0 but you can change it.
- *alternative* defines the alternative hypothesis. It can be “two.sided” (default), “greater” or “less”.
- *exact* determines whether to compute an exact p-value for small sample sizes. When *exact = TRUE*, R will compute an exact p-value using the exact distribution of the test statistic rather than relying on an asymptotic approximation.
- *correct* is a boolean that indicates whether to apply continuity correction in the normal approximation for the p-value. It is *TRUE* by default.

Let's say you want to analyse the data set `trees` on R which provides measurements of the diameter, height and volume of timber in 31 felled black cherry trees. Specifically, you want to check if the median height of the trees is less than 80ft, so you run the `wilcox.test()` on R by setting *mu = 80* and *alternative = "less"*.

{{% codeblock %}}
```R
wilcox.test(trees$Height, mu = 80
          alternative = "less",
          exact = FALSE)
```
{{% /codeblock %}}

The hypothesis for this test will be set as:
- H0: Median height = 80
- H1: Median height < 80

The output of the code gives a p-value of **0.002** which is less than 0.01. Thus, you can reject the null hypothesis at a 1% significance level which is highly suggestive of the median height of the trees being less than 80ft.

{{% tip %}}
If your sample size is large, an asymptotic approximation is often used because otherwise, the exact calculation might be computationally expensive. Thus, given the large sample size of the dataset in this example, we set `exact = FALSE`.
{{% /tip %}}


## Wilcoxon matched-pairs test
The  Wilcoxon matched-pairs signed-rank test (or simply the Wilcoxon matched-pairs test) is a nonparametric method to compare before-after or matched subjects. For performing this test, `wilcox.test()` has the following syntax:

{{% codeblock %}}
```R
wilcox.test(x, y,
          paired = FALSE,
          alternative = “two.sided”,
          exact = NULL,
          correct = TRUE)
```
{{% /codeblock %}}

where:
- *y* is another (optional) numeric vector with data values.
- *paired* is a logical value specifying whether you want a paired test. It is *FALSE* by default, so you need to set it to *TRUE* for performing the Wilcoxon matched-pairs test.

To understand how to use this test, let us look at the dataset `mice2` from the package `datarium`. It contains the weights of ten mice before and after a treatment. Suppose you want to assess if there is a significant difference between the weights of the mice before and after the treatment (paired samples) you can use the Wilcoxon matched-pairs test. The hypothesis will be set as:
- H0: Weights before = Weights after
- H1: Weights before ≠ Weights after

{{% codeblock %}}
```R
library(datarium)

wilcox.test(mice2$before, mice2$after,
          paired = TRUE,
          alternative = “two.sided”,
          exact = TRUE)
```
{{% /codeblock %}}

The output of this test gives a p-value equal to **0.002** which is less than 0.01. This suggests that at a 1% significance level, the difference in the weights of the mice before and after the treatment is highly significant.

{{% tip %}}
If your dataset does not have the 'Before' and 'After' values in separate columns like so:  
| **id** | **before**  | **after**
| :------  | :---------             | :----- |
| 1     |  187.2      | 429.5 |

but instead in the form of, say
| **id** | **group**  | **weight**
| :------  | :---------             | :----- |
| 1     |  before     | 187.2 |
|  1  | after   | 429.5  |

you can specify your data values as


`wilcox.test(weight ~ group)`


{{% /tip %}}


## Wilcoxon rank sum test
The Wilcoxon rank sum test is a nonparametric test to compare two unmatched (independent) groups. It is also known as the Mann-Whitney U test. The syntax of `wilcox.test()` for performing this test is the same as that for the matched-pairs test.

{{% warning %}}
There is no need to explicitly specify the *exact* argument for this test. That argument is more relevant when you are dealing with paired samples.
For the Mann-Whitney U test (which is essentially a Wilcoxon rank-sum test for independent samples), the default behaviour is to use an asymptotic approximation.
{{% /warning %}}

For this let us look at another dataset from the `datarium` package, called `genderweight`. It contains the weights by sex (M for male; F for female). The genders are specified under the column 'group'. Suppose you want to answer the question of whether the average woman’s weight significantly differs from the average man’s weight you can use the Mann-Whitney U test. The hypothesis will be set as:
- H0: Female weight = Male weight
- H1: Female weight ≠ Male weight

{{% codeblock %}}
```R
library(datarium)

wilcox.test(genderweight$weight ~ genderweight$group)
```
{{% /codeblock %}}

The output of this test gives a p-value less than 0.0001 so you can reject the null hypothesis. This suggests that the difference in the average weights of the two genders is significant.

{{% summary %}}
- The Wilcoxon test family provides versatile options for comparing samples without making strong assumptions about the underlying distribution.
  - One-sample Wilcoxon Signed-Rank test is used when you have one sample and want to test if its distribution is symmetrically centred around a hypothesized median.
  - Wilcoxon matched-pairs test is used when you want to compare averages of two paired (dependent) samples.
  -  Wilcoxon rank sum test is used when you have two independent samples.


- These tests can be performed on R using its inbuilt test `wilcox.test()`


{{% /summary %}}
