---
title: "Understanding the binomial test"
description: "Short guide to understanding the workings of the binomial test and how to use it in R"
keywords: ""
weight: 1
date:
draft: false
aliases:
  - /binomial-test
---


## Overview
Binomial test is very handy when dealing with a **binary data** with a **nominal** measurement scale. It answers the question: "Is the observed outcome significantly different from what we would expect by a random chance?"; such as: Testing if a coin is fair, testing if a an election outcome favours the Republican or the Democrats, etc.

In this building block we will describe how the formula works mathematically and how to use it in R. Let's look at an example.

## Is you coin fair?
Suppose you are wondering whether a coin is fair, in particular, you are testing if tails does not come up as expected. You flip the coin, say 5 times and record the only 2 possible outcomes: Heads or tails. Clearly, these outcomes require no inherent order, so the data is indeed binary and nominal.

### Hypothesis testing
To conduct a hypothesis test, it is important to know the probability, p of getting tails with a fair coin, that is 1/2. Thus, your null hypothesis and alternative hypothesis will be as follows:

H0: p = 1/2

H1: p ≠ 1/2

### Formula for the Binomial Test
The Binomial Test formula calculates the probability of observing the actual number of successes (x) in a given number of trials (n) under the assumption of a specific probability of success (p) according to the null hypothesis.

The formula is:

{{<katex>}}
P(X = x) = \binom{n}{x} \cdot p^x \cdot (1 - p)^{n - x}
{{</katex>}}


Where:
- P(X = x) is the probability of observing x successes.
- {{<katex>}}\binom{n}{x} {{</katex>}} represents the binomial coefficient.
- p is the probability of success (i.e. 0.5 in this case).
- n is the total number of trials.

{{% tip %}}

{{<katex>}}\binom{n}{x} = \frac{n!}{x!(n-x)!} {{</katex>}}

{{% /tip %}}

Now, suppose when you flip the coin 5 times and tails comes up 3 times, with n = 5 and x = 3, the probability of observing exactly 3 successes will be

{{<katex>}}
P(X = 3) = \binom{5}{3} \cdot 0.5^3 \cdot (1 - 0.5)^{5 - 3} = 0.3125.

{{</katex>}}

<br>
<br>


This type of a hypothesis is called a **two-sided test** because you cannot identify in which direction this inequality occurs. Sometimes you might not be interested in such extreme cases but instead, want to check the probability of observing less than or more than 3 successes.

The probability of exactly, or fewer than 3 successes will be:

{{<katex>}}
P(X ≤ 3) = \sum_{i=0}^3\binom{5}{i} \cdot 0.5^i \cdot (1 - 0.5)^{5 - i}
        = 0.8125
{{</katex>}}
<br>
<br>
with the following hypothesis:

H0: p = 1/2

H1: p ≤ 1/2


Similarly, the probability of exactly, or more than 3 successes will be:

{{<katex>}}
P(X ≥ 3) = \sum_{i=3}^5\binom{5}{i} \cdot 0.5^i \cdot (1 - 0.5)^{5 - i}
        = 0.5
{{</katex>}}
<br>
<br>
with the following hypothesis:

H0: p = 1/2

H1: p ≥ 1/2

<br>

### Reject or accept?
In order to reject or accept a hypothesis, you should first choose a significance level (alpha) in advance. Typically, it is set to 5% (i.e. alpha = 0.05). This acts as a threshold for determining statistical significance.

If the calculated probability (p) is **less than or equal to alpha**, you would typically **reject the null hypothesis** that the coin is fair. On the other hand, if the p is **greater** than alpha, you would **fail to reject** the null hypothesis.

In our first example, we calculate **p = 0.3125**. This means that with the results we observed ( 3 tails in 5 flips), we do not have enough evidence to conclude at 5% confidence level that the coin is not fair.

{{% warning %}}
In this example, we focused on a case where the alternative hypothesis was **two-sided**, i.e. H1: p ≠ 1/2. However, if you are dealing with a one-sided hypothesis, for example H1: p < 1/2, you should compare the p-value with half of the alpha value (0.05/2 = 0.025) and accordingly make a conclusion for your hypothesis.


{{% /warning %}}

### Testing this in R
In the previous examples, we worked with relatively small datasets, simplifying the calculations. However, in practice, you may frequently encounter larger datasets. Handling these manually not only consumes time but also increases the risk of mathematical errors, especially for a one-tailed test. That's where R comes to the rescue. R offers a built-in function called `binom.test()`, which efficiently performs binomial tests, making it a reliable and time-saving tool for such scenarios.

Let's have a quick look at how it works.

{{% codeblock %}}
```R
binom.test(x=3, n=5, p=0.5,
  alternative = "two.sided",
   conf.level=0.95)

{{% /codeblock %}}

- Here, as discussed before, *x* refers to the number of successes, *n* is the total number of trials and *p* is the probability defined in the hypothesis.
- The argument, *alternative* indicates the alternative hypothesis and must be one of "two.sided", "greater" or "less". You can specify just the initial letter. By default it is set to "two.sided".
- Lastly, the *conf.level* argument is for the confidence level for the returned confidence interval which is 0.95 by default.  


{{% summary %}}

-



{{% /summary %}}
