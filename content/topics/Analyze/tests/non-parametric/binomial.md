---
title: "Understanding the Binomial Test"
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
```
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
```
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
```
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
```
{{% /codeblock %}}

The p-value in this case is **0.95**. Since this is also not less than 0.05, we fail to reject the null hypothesis and thus there is not enough evidence to suggest that the coin is against heads.

{{% tip %}}
The result of `binom.test()` is an object of class "htest". It includes various elements such as the p-value of the test (p.value), number of successes (statistic), number of trials (parameter), etc. If you are only interested in say, obtaining the p-value of the test, you can access it by using `$` in the code as so:

`binom.test(x,n,p)$p.value`

{{% /tip %}}

The three examples we discussed earlier involve small samples where it is easy to count the number of successes (x). However, this is not always feasible when you have large amounts of data. Let's explore an example with more data to better understand how to use the `binom.test()` function in such cases.

### Assessing election results using binom.test()
Suppose you are interested in finding the results of an election in a hypothetical land with two political parties: Party A and Party B. You survey the population of the land and create a data set called 'Election_data' with 100 observations. It looks like this:

| **Voter Id** | **Party** |
| :-----      | :-----        |
| 001    |   Party A     |
| 002    |   Party B     |
| 003    |   Party B     |
| 004    |   Party A     |

Let's say a political party considers a win if it receives more than 50% of the votes. To check if they indeed achieved this, you can use a right-tailed binomial test with a probability (p) set to 1/2. Here's how you can implement the code for Party A:

{{% codeblock %}}
```R
# Set n
num_voters = 100

# Calculate the number of successes
party_A_wins <- sum(Election_data$Party == "Party A")

# Apply the test
result <- binom.test(party_A_wins,
                     num_voters,
                     p = 0.5, alternative = "greater")
# Obtain the p-value
result$p.value
```
{{% /codeblock %}}

If this p-value is less than your chosen significance level, it suggests that more than 50% of the population voted for party A leading to its victory.

## Understanding binom.confint()
We use `binom.test()` when we want to make a hypothesis about a proportion and need a p-value to decide on the null hypothesis. However, if you are more interested in estimating the range within which the true proportion might fall, you need to estimate the confidence intervals. The R package `binom` offers a function called `binom.confint()` which is used for constructing confidence intervals for binomial proportions. It provides a range of values within which the true proportion is likely to lie. It does not perform a hypothesis test but gives you a sense of the precision of your estimate.

The syntax of this function is fairly straightforward.
{{% codeblock %}}
```R
binom.confint(x, n,
              conf.level = 0.95,
              methods = c("exact", "ac", "asymptotic",
              "wilson", "prop.test", "bayes", "logit",
              "cloglog", "probit")
               # Default for method is "all"

```
{{% /codeblock %}}

 In addition to *x* and *n*, it requires an argument called *method* which specifies the method of constructing the intervals. It is suggested to use the [Agresti-Coull method](https://statisticaloddsandends.wordpress.com/2019/06/09/wilson-score-and-agresti-coull-intervals-for-binomial-proportions/) to calculate a confidence interval for an estimate of a proportion as it provides a good compromise between accuracy and computational efficiency for larger samples.

Let's consider the example in the previous subsection about assessing election results. If you want to construct the confidence interval for Party A, you can use the `binom.confint()` as follows:

{{% codeblock %}}
```R
install.packages("binom", dependencies = TRUE)
library(binom)

binom.confint(party_A_wins,
              num_voters,
              method = "ac") # ac stands for Agresti-Coull
```
{{% /codeblock %}}

The result of this code gives a lower limit and an upper limit which forms the confidence interval. It suggests that, based on your sample data, you can be 95% confident that the true proportion of people voting for Party A in the entire population falls within this range.

{{% warning %}}
If you are unsure about which method to choose, you could try different methods and see which one aligns better with your assumptions and preferences. Alternatively, you might conduct a sensitivity analysis to see how results change under different methods.

Remember that the "best" method can depend on the characteristics of your specific data, and there is not a one-size-fits-all answer.
{{% /warning %}}

## Extension to binomial - Exact multinomial test
The exact [multinomial test](https://rinterested.github.io/statistics/multinomial_exact.html) is a statistical test used to determine if the observed frequencies of categorical data differ significantly from the expected frequencies. It is an extension of the binomial test to the case where there are more than two categories. This test can be performed on R with the [`multinom_test()`](https://search.r-project.org/CRAN/refmans/rstatix/html/multinom_test.html) which is offered by the `rstatix` package. Another function called [`multinomial.test()`](https://search.r-project.org/CRAN/refmans/EMT/html/multinomial.test.html) also performs this test on R for discrete multivariate data. You can choose the test which is more tailored to your requirements.

{{% summary %}}

- The Binomial test is used for binary data with a nominal measurement scale.

- It can be performed on R using its in-built function `binom.test()`.

- `binom.confint()`  is used for estimating confidence intervals for binomial proportions.

- The exact multinomial test which is a generalisation for the binomial test when there are more than two categories, can be performed on R using `multinom_test{rstatix}` and `multinomial.test{EMT}`.

{{% /summary %}}
