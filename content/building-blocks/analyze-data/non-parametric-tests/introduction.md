---
title: "Intro to non parametric tests"
description: "Describing the types of non parametric tests and their usage"
keywords: "non, para, test, binom, chi, wilcoxon, mcnemar, fisher, median, mann, whitney, kruskal, wallis"
weight: 1
date:
draft: false
aliases:
  - /non-para-intro
---

## Overview

Performing statistical tests like t-test and f-test are imperative in any empirical study to help test the hypotheses about population parameters. However, parametric tests like these make certain assumptions about the underlying population distribution which are not always reasonable to make. Hence, in such a case, one should use a non-parametric test instead.
In this building block, we will describe the various non-parametric test that you can use according to the data sample you have.

## Which test to use?
Determining which statistical test is most appropriate depends on 3 characteristics of your data:

- Measurement scale
  1) Nominal / Categorical scale
      - Categorizes data into distinct groups or categories without any inherent order or numerical value.
      - Example: Gender, colour
  2) Ordinal / Ranking scale
      - Orders or ranks data based on their relative position or preference without making precise statements about the magnitude of the differences between them.      
      - Example: Grades, Valuations        
  3) Interval (Cardinal) scale
      - Categorizes data into distinct groups or levels, and the differences between these categories are meaningful and consistent
      - Example: Temperature, Calendar dates
  4) Ratio scale
      - This is the highest level of measurement scale that possesses all the characteristics of nominal, ordinal, and interval scales, and in addition, it has a true zero point that represents the absence of the measured attribute.

- Type of data
  - Binary
  - Discrete
  - Continuous

- Data structure
  - One sample
      - Single observation from a single subject group
  - Two (or more) related / dependent samples
      - Multiple observations from a single subject group
  - Two (or more) independent samples
      - Multiple observations from several independent subject groups

## Types of non parametric tests
Now that you know the characteristics of your sample, you can accordingly choose the most appropriate non parametric test

### Binomial Test
If you are dealing with a `binary data` with a `nominal` measurement scale, binomial test is the most appropriate test. It answers the question: "Is the observed outcome significantly different from what we would expect by a random chance?"; such as: Testing if a coin is fair, testing if a an election outcome favours the Republican or the Democrats, etc.

Check out the building block on the binomial test [# I'll add link here] to learn how to use this test on R and how the formula works mathematically.

### Chi-Squared Goodness of Fit
Another test you can use with a `binary` and `nominal` data is the Chi-Squared Goodness of Fit. It tests whether a significant difference exists between an observed number of outcomes falling in each category and an expected number based on the null hypothesis (which we call the goodness-of-fit)

Check out the building block on the chi-squared goodness of fit [# I'll add link here] to learn how to use this test on R and how the formula works mathematically.

These 2 tests are useful when you only have 1 sample of data. However, when there are multiple samples of data, it is important to be mindful if those data samples are independent or if they are related to each other. Accordingly you can choose among the following tests:

## Non parametric test for 2 dependent samples

### Wilcoxon Matched-Pairs Signed Ranks Test
Before going over the Wilcoxon Matched-Pairs Sign Test, let's first discuss another non-parametric test called the `Sign Test`. This test can be interpreted as an application of the Binomial Test in case of 2 dependent samples (generally a case of 'before' and 'after' treatment), with n observations. Each pair of the observation can be put into 3 classes:

`+` = 'before' measurement is `greater/better` than the 'after' treatment

`0` = 'before' measurement is `equal/same` as 'after' treatment

`-` = 'before' measurement is `smaller/worse` than the 'after' treatment

The Sign Test, however, only accounts for the sign of the differences between the 2 dependent samples and not for the magnitude of the difference. Hence, the **Wilcoxon Signed-Ranks Test** serves as a **powerful extension** of the Sign test as it uses both the sign and relative magnitude (ranks) of the differences. Check out how to use this test on the building block [#Add link here]

### McNemar's test
The final test suitable for 2 dependent samples is the McNemar's Test. It is suitable for `nominal data` and when the 2 decisions are made by the same subjects. Consider the contingency table given below:

|             |               | `Decision 1` |               |    |
|-------------|---------------|--------------|---------------| ----- |
|             |               | Option A| Option B    |       |
| `Decision 2` | Option A | a      | b              | **a + b** |
|             | Option B | c        | d               | c + d |
|             |          | **a + c**    | b + d           | N      |



The test examines whether the 2 proportions, P1 = (a+b)/N and P2 = (a+c)/N are significantly different from each other.
To know how to use this test, check out the building block [#Add link here]. 

## Non parametric test for 2 independent samples

### Fisher's exact test

### Median test

### Mann-Whitney U test (Kruskal Wallis)
