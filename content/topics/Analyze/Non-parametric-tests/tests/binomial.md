---
title: "Understanding the binomial test"
description: "Short guide to understanding the workings of the binomial test and how to use it in R"
keywords: "bin, nominal, sample, one, test, hypothesis, trial, success, "
weight: 1
draft: false
author: "Aakriti Gupta"
authorlink: "https://nl.linkedin.com/in/aakriti-gupta-91450821b"
aliases:
  - /binomial-test
---

## Overview
The Binomial test is applied to **binary data** with a **nominal** measurement scale. It answers the question: "Is the observed outcome significantly different from what we would expect by a random chance?"; such as testing if a coin is fair, testing if an election outcome favours the Republicans or the Democrats, etc. For performing this test, R offers an inbuilt function called `binom.test()` which we will describe in this building block.

## Understanding binom.test()
In R, the binomial test is performed by `binom.test()` which can be applied using the following syntax:

{{% codeblock %}}
```R
binom.test(x, n, p = 0.5,
           alternative = c("two.sided", "less", "greater"),
           conf.level = 0.95)

{{% /codeblock %}}

where:
- *x*	denotes the number of successes, or a vector of length 2 giving the numbers of successes and failures, respectively.

- *n* is the number of trials; ignored if x has length 2.

- *p* hypothesizes the probability of success. It takes the value of 0.5 by default.

- *alternative* indicates the alternative hypothesis and must be one of "two.sided", "greater" or "less". You can specify just the initial letter. By default, it is set to "two.sided".

- *conf.level* indicates the confidence level for the returned confidence interval. It takes the value of 95% by default.

The binomial test compares a sample proportion to a hypothesized proportion. The test can be performed with a two-tailed alternative that the true population is unequal to the hypothesized one or with a one-tailed alternative that the true population proportion is less (left-tailed) or greater (right-tailed) than some value p. Let us look at how `binom.test` works for these three cases.

### Example 1: Two-tailed Binomial test
Imagine you are investigating the fairness of a die. To assess this, you roll the die 24 times (n) and observe that the number 4 appears 9 times (x). You can use `binom.test()` to test whether the observed number of successes (rolling a 4) is significantly different from what you would expect under the assumption of fairness. Because the probability (p) of obtaining each number on the die is 1/6, the hypothesis can be set in the following way:
- H0: p = 1/6
- H1: p ≠ 1/6

Here is the code:

{{% codeblock %}}
```R
binom.test(9, 24, 1/6)

{{% /codeblock %}}

This function gives the p-value for the test which is **0.012**. Since this is less than 0.05 (assuming a 5% significance level), we can reject the null hypothesis and conclude that there is evidence that the die does not land on the number “4” during 1/6 of the rolls, indicating that the die is not fair.

### Example 2: Left-tailed Binomial test
Suppose you want to determine the fairness of a coin, specifically if the coin is less likely to land on tails compared to heads. You flip the coin 30 times (n) and find that it lands on tails just 11 times (x). Because the probability (p) of getting tails is 1/2, the hypothesis is set as:
- H0: p = 1/2
- H1: p < 1/2

Here is the code:
{{% codeblock %}}
```R
binom.test(11, 30, 1/2,
        alternative = "less")
## you can also use alternative = "l"

{{% /codeblock %}}

The p-value in this case is **0.1**. Since this is not less than 0.05, we fail to reject the null hypothesis and thus there is not enough evidence to suggest that the coin tends to favour heads over tails.

### Example 3: Right-tailed Binomial test
Now, to confirm if the coin is fair you should also check if the coin is instead more likely to land on tails compared to heads. To do this, the hypothesis is set as:
- H0: p = 1/2
- H1: p > 1/2

Here is the code:
{{% codeblock %}}
```R
binom.test(11, 30, 1/2,
        alternative = "greater")
## you can also use alternative = "g"

{{% /codeblock %}}

The p-value in this case is **0.95**. Since this is also not less than 0.05, we fail to reject the null hypothesis and thus there is not enough evidence to suggest that the coin is against heads.

{{% summary %}}

- The Binomial test is used for binary data with a nominal measurement scale.

- It can be performed on R using its in-built function `binom.test()`


{{% /summary %}}
