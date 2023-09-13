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

### Binomial test
If you are dealing with a binary data with a nominal measurement scale, binomial test is the most appropriate test. It answers the question: "Is the observed outcome significantly different from what we would expect by a random chance?"; such as: Testing if a coin is fair, testing if a an election outcome favours the Republican or the Democrats, etc.

Check out the building block on the binomial test [# I'll add link here] to learn how to use this test on R and how the formula works mathematically.

### Chi-squared goodness of fit
Another test you can use with a binary and nominal data is the chi-squared goodness of fit. It tests whether a significant difference exists between an observed number of outcomes falling in each category and an expected number based on the null hypothesis (which we call the goodness-of-fit)

Check out the building block on the chi-squared goodness of fit [# I'll add link here] to learn how to use this test on R and how the formula works mathematically.

These 2 tests are useful when you only have 1 sample of data. However, when there are multiple samples of data, it is important to be mindful if those data samples are independent or if they are related to each other. Accordingly you can choose among the following tests:

## Non parametric test for 2 dependent samples

### Wilcoxon matched-pairs signed ranks test
