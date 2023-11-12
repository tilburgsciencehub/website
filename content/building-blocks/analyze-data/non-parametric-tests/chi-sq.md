---
title: "Chi-Squared Goodness of Fit Test"
description: "Short guide to understanding the workings of the Chi-Squared Goodness of Fit test and how to use it in R"
keywords: ""
weight: 2
date:
draft: false
aliases:
  - /chi-squared test
  - /Chi-Squared Goodness of Fit test
---


## Overview
The Chi-Squared Goodness of Fit test is used when you are dealing with **binary** data with a **nominal** measurement scale. It tests whether a significant difference exists between an observed number of outcomes falling in each category and an expected number based on the null hypothesis (which we call the goodness-of-fit)

In this building block we will describe how the formula works mathematically and how to use it in R. Let's look at an example.

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

## Hypothesis testing
To statistically test for this case, we first describe the hypotheses. The null hypothesis (H0) states that the observed distribution of ice cream flavors in the sample matches the expected distribution and the alternative hypothesis (H1) states that the observed distribution in the sample is significantly different from the expected distribution. Hence, we have:

- H0: Oi = Ei
- H1: Oi ≠ Ei

## Reject or accept H0?
In order to conclude if you can reject the null hypothesis, it is important to compare the chi-square statistic with the critical value. According to the data available to us, this comparison can be made using the following steps:
### Step1: Calculate the chi-square statistic

{{<katex>}}
\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i}
{{</katex>}}

<br>
<br>

where k describes the number of categories, which in our case equals 5.

According to the data, the chi-square statistic will be as follows:

{{<katex>}}
\chi^2 = \frac{(70 - 80)^2}{80} + \frac{(60 - 60)^2}{60} + \frac{(30 - 30)^2}{30} + \frac{(20 - 20)^2}{20} + \frac{(20 - 10)^2}{10}
{{</katex>}}

= **11.25**

### Step2: Compute the degrees of freedom
An important step for computing the critical value is to know the degrees of freedom (df), which equals k-1. Therefore, in this case, df = 5 - 1 = **4**.

### Step3: Set the significance level
Similar to most hypothesis tests, it is necessary to set a significance level (alpha) to be able to make a statistical conclusion. Let us choose alpha = **0.05**.

### Step4: Note the chi-square critical value
Lookup the critical chi-square value for a significance level of 0.05 and df of 4 from a chi-square distribution table. This is approximately **9.49**.

### Step5: Make a comparison
From our calculations is the previous steps, we get the chi-square statistics equal to 11.25 and the critical value to be 9.49. Since the calculated chi-square statistic (11.25) is greater than the critical value (9.49), we **reject** the null hypothesis.

Thus, we have evidence to conclude that the observed distribution of ice cream flavors in the sample is **significantly different** from the expected distribution based on industry standards. In other words, there is a statistically significant difference, suggesting that the preferences in your sample **deviate** from what was expected.


## Testing this in R
In the previous examples, we worked with relatively small datasets, simplifying the calculations. However, in practice, you may frequently encounter larger datasets. Handling these manually not only consumes time but also increases the risk of mathematical errors, especially for a one-tailed test. That's where R comes to the rescue. R offers a built-in function called `chisq.test()`, which efficiently performs the chi-sqaured goodness of fit test, making it a reliable and time-saving tool for such scenarios.

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


The output of this code, gives the value of the chi-sqaure statistic and the df. You can use this information, to compare the statistic with the critical value and make the final conclusion as we did before. The output also gives the p-value which you compare with the alpha.

Here's the general interpretation:

If the p-value is **less than or equal** to the chosen significance level (e.g., 0.05), you **reject** the null hypothesis.

If the p-value is **greater** than the chosen significance level, you **fail to reject** the null hypothesis.

In our case, the **p-value is 0.02**  which is less than 0.05, so verifying our previous analysis, you would reject the null hypothesis.



{{% summary %}}

- The chi-squared goodness of fit is apt for binary and nominal data.

- The formula of the chi-square statistic is:

{{<katex>}}
\chi^2 = \sum_{i=1}^k \frac{(Oi - Ei)^2}{Ei}
{{</katex>}}

where k describes the number of categories, Oi is the observed data and Ei is the expected data.


- This test can be performed on r using its inbuilt test `chisq.test()`


{{% /summary %}}
