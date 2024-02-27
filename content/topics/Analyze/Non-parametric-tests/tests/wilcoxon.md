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
The Wilcoxon test is a non-parametric alternative to the t-test for comparing averages in one or two (dependent or independent) samples. There are different types of wilcoxon tests, depending on the type of sample: One-sample Wilcoxon signed rank test, Wilcoxon matched-pairs test for a dependent sample and Wilcoxon rank sum test (Mann-Whitney U test) for an independent sample. In this building block, you will learn how to perform these tests on R using `wilcox.test()`.

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

Suppose you recorded the heights of 100 trees in a dataset called `tree_heights` to check if the median height is less than 85ft.

{{% codeblock %}}
```R
tree_heights <- c(90.4, 93, 62.3, 72.9, 88.7, 81.2, 72.5, 67, 58, 66.8,
                  99.5, 95.6, 92.4, 62.7, 61.2, 103.7, 76.8, 78.2, 63.3, 84.2,
                  68.5, 66.5, 89.6, 69.1, 95.5, 59.7, 96.1, 76.4, 92.8, 88.1,
                  77.2, 86.4, 55, 65.9, 90.2, 65.8, 95.7, 70.4, 89.4, 101.6 )
```
{{% /codeblock %}}

Let's first check if this data set follows a normal distribution via a histogram and the [Shapiro-Wilk test.](https://www.geeksforgeeks.org/shapiro-wilk-test-in-r-programming/)

{{% codeblock %}}
```R
hist(tree_heights)

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/hist_trees.png" width="400">
<figcaption> </figcaption>
</p>

{{% codeblock %}}
```R
shapiro.test(tree_heights)

#Shapiro-Wilk normality test
#data:  tree_heights
#W = 0.94126, p-value = 0.03814
```
{{% /codeblock %}}

The shape of the histogram shows that the data does not follow a normal distribution and the p-value of the Shapiro-Wilk tests confirms it (since we reject the null hypothesis of normality for both distributions at the 5% significance level). Since the normality assumption is violated we cannot use parametric tests such as Student’s t-test and should instead utilise the Wilcoxon test.  

This test can be performed on R using `wilcox.test()`. Since you are interested in analysing if the median height is less than 85ft you should set *mu = 85* and *alternative = "less"*.

{{% codeblock %}}
```R
wilcox.test(tree_heights, mu=85,
            alternative = "less",
            exact=FALSE)
```
{{% /codeblock %}}

The hypothesis for this test will be set as:
- H0: Median height = 85
- H1: Median height < 85

The output of the code gives a p-value of **0.008** which is less than 0.01. Thus, you can reject the null hypothesis at a 1% significance level which is highly suggestive of the median height of the trees being less than 85ft.

{{% tip %}}
If your sample size is large, an asymptotic approximation is often used because otherwise, the exact calculation might be computationally expensive. Thus, given the large sample size of the dataset in this example, we set `exact = FALSE`.
{{% /tip %}}


It is important to note that in the case of large samples, normality is not required. By the [central limit theorem](https://www.scribbr.com/statistics/central-limit-theorem/#:~:text=The%20central%20limit%20theorem%20says,the%20mean%20will%20be%20normal.), sample means of large samples are often well-approximated by a normal distribution even if the data are not normally distributed. Therefore, we typically use the wilcoxon test for smaller samples where normality is unlikely to hold.

For the sake of this building block, in the following two examples, we will assume that normality does not hold even with a large sample.  

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

{{% warning %}}
For an independent sample, it is sufficient to check for normality **individually** on the two samples. However, for paired samples (when in the presence of a small sample), normality must be checked on the **differences** between the two paired samples.
{{% /warning %}}

## Wilcoxon rank sum test
The Wilcoxon rank sum test is a nonparametric test to compare two unmatched (independent) groups. It is also known as the Mann-Whitney U test. The syntax of `wilcox.test()` for performing this test is the same as that for the matched-pairs test.

{{% tip %}}
There is no need to explicitly specify the *exact* argument for this test. That argument is more relevant when you are dealing with paired samples.
For the Mann-Whitney U test (which is essentially a Wilcoxon rank-sum test for independent samples), the default behaviour is to use an asymptotic approximation.
{{% /tip %}}

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



{{% warning %}}
It is not always ideal to default to non-parametric tests to avoid normality checks. The reason is that non-parametric tests are usually less powerful than corresponding parametric tests when the normality assumption holds. This means that ceteris paribus, with a non-parametric test you are less likely to reject the null hypothesis when it is false if the data follows a normal distribution. It is thus preferred to use the parametric version of a statistical test when the assumptions are met.
{{% /warning %}}

{{% summary %}}
- The Wilcoxon test family provides versatile options for comparing samples without making strong assumptions about the underlying distribution.
  - One-sample Wilcoxon Signed-Rank test is used when you have one sample and want to test if its distribution is symmetrically centred around a hypothesized median.
  - Wilcoxon matched-pairs test is used when you want to compare averages of two paired (dependent) samples.
  -  Wilcoxon rank sum test is used when you have two independent samples.


- These tests can be performed on R using its inbuilt test `wilcox.test()`


{{% /summary %}}
