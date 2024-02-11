---
title: "Introduction to non parametric tests"
description: "Describing the types of non parametric tests and their usage"
keywords: "non, para, test, binom, chi, wilcoxon, mcnemar, fisher, median, mann, whitney, in, dep, dist"
weight: 1
draft: false
author: "Aakriti Gupta"
authorlink: "https://nl.linkedin.com/in/aakriti-gupta-91450821b"

aliases:
  - /non-para-intro
---

## Overview

Performing statistical tests like t-tests and f-tests is imperative in any empirical study to help test the hypotheses about population parameters. However, parametric tests like these make certain assumptions about the underlying population distribution that are not always reasonable to make.

Imagine you're comparing the heights of two groups of people: Group A and Group B. You want to know if Group A is taller, on average, than Group B.

In a perfect world, where everything follows a bell-shaped curve (a normal distribution), you could use a parametric test like the t-test. This test assumes that the data is normally distributed and that the variances of the two groups are equal.

<p align = "center">
<img src = "../images/bell-shape-curve.png" width="400">
<figcaption> Bell-shaped curve of a normal distribution</figcaption>
</p>

Now, let's say you measure the heights of both groups, but your data doesn't look like a nice, symmetric bell curve as above. Instead, the data is kind of all over the place, and you're not sure if the variances are equal. Hence, in such a case, one should use a non-parametric test instead.

{{% tip %}}
In situations where the distribution of the sample is unknown, using a parametric test like the t-test might not be appropriate because it relies on those assumptions.
So, you should instead turn to non-parametric tests. These tests don't make as many assumptions about the shape of the data. They work by ranking the data points and comparing those ranks, rather than looking at the raw data values.

{{% /tip %}}  


In this building block, we will describe the various non-parametric tests that you can use according to the data sample you have.


## Which test to use?
Determining which statistical test is most appropriate depends on three characteristics of your data:

- Measurement scale
  - Nominal / Categorical scale
      - Categorizes data into distinct groups or categories without any inherent order or numerical value.
      - Example: Gender, colour
  - Ordinal / Ranking scale
      - Orders or ranks data based on their relative position or preference without making precise statements about the magnitude of the differences between them.      
      - Example: Grades, Valuations        
  - Interval (Cardinal) scale
      - Categorises data into distinct groups or levels, and the differences between these categories are meaningful and consistent
      - Example: Temperature, Calendar dates
  - Ratio scale
      - This is the highest level of measurement scale that possesses all the characteristics of nominal, ordinal, and interval scales, and in addition, it has a true zero point that represents the absence of the measured attribute.

- Type of data
  - Binary
  - Discrete
  - Continuous

- Data structure
  - **One sample**: Single observation from a single subject group
  - **Two (or more) dependent samples**: Multiple observations from a single subject group
  - **Two (or more) independent samples**: Multiple observations from several independent subject groups

## Types of non-parametric tests
Now that you know the characteristics of your sample, you can accordingly choose the most appropriate non-parametric test

### Binomial Test
If you are dealing with **binary data** with a **nominal** measurement scale, the binomial test is the most appropriate. It answers the question: "Is the observed outcome significantly different from what we would expect by a random chance?"; such as testing if a coin is fair, testing if an election outcome favours the Republicans or the Democrats, etc.

Check out the building block on the [Binomial test](https://tilburgsciencehub.com/topics/analyze/Non-parametric-tests/tests/binomial) to learn how to use this test on R.

### Chi-Squared Goodness of Fit
Another test you can use with **binary** and **nominal** data is the Chi-Squared Goodness of Fit. It tests whether a significant difference exists between an observed number of outcomes falling in each category and an expected number based on the null hypothesis (which we call the goodness-of-fit).

Check out the building block on the [Chi-squared test](https://tilburgsciencehub.com/topics/analyze/Non-parametric-tests/tests/chisq) to learn how to use this test on R.

{{% warning %}}
The two tests discussed above are useful when you only have **one sample** of data. However, when there are multiple samples of data, it is important to be mindful if those data samples are independent or if they are related to each other. You should accordingly choose the most apt test.

{{% /warning %}}

## Two dependent samples

### Wilcoxon Matched-Pairs Signed Ranks Test
This test is suitable for **ordinal** data of either **discrete** or **continuous** type.
Before going over the Wilcoxon matched-pairs test, let's first discuss another non-parametric test called the *Sign Test*. This test can be interpreted as an application of the [Binomial test](https://tilburgsciencehub.com/topics/analyze/Non-parametric-tests/tests/binomial) in the case of two dependent samples (generally a case of 'before' and 'after' treatment), with n observations. Each pair of observations can be put into three classes:

**+** = 'before' measurement is **greater/better** than the 'after' treatment

**0** = 'before' measurement is **equal/same** as 'after' treatment

**-** = 'before' measurement is **smaller/worse** than the 'after' treatment

The Sign Test, however, only accounts for the sign of the differences between the two dependent samples and not for the magnitude of the difference. Hence, the **Wilcoxon matched-pairs test** serves as a **powerful extension** of the Sign test as it uses both the sign and relative magnitude (ranks) of the differences. Check out the building block on the [Wilcoxon test](https://tilburgsciencehub.com/topics/analyze/Non-parametric-tests/tests/wilcoxon) to learn how to use this test on R.

### McNemar's test
The final test suitable for two dependent samples is McNemar's Test. It is suitable for **nominal** and **discrete** data. It's often used in situations where you have two sets of observations, like before and after measurements or two different treatments on the same group.

Let's say you're testing a new drug to see if it's effective in treating a medical condition. You have a group of 100 patients who are all currently using an existing treatment (Treatment A). You administer the new drug (Treatment B) to these patients and observe the outcomes after some time. You record the results in a 2x2 table like this:


|             |               | **Treatment B** |               |
|-------------|---------------|--------------|---------------|
|             |               | Improved| Not improved    |     
| **Treatment A** | Improved | 20      | 15            |
|             | Not improved | 10        | 55        |


In this case, each patient serves as their own control because they receive both treatments, A and B. Their responses are paired directly with themselves, making the observations dependent.

McNemar's test helps answer the question: "Is there a significant difference in improvement rates between the two treatments?"


{{% warning %}}
The tests above deal with a **within-subject** design in which all participants take part in every condition (treatment), making the observations dependent on each other. However, many experiments tend to have a **between-subject** design where each participant experiences only one of the treatments. As a result, the decisions made in the two (or more) treatments are **independent** of each other.

{{% /warning %}}

Let's discuss the tests suitable for this setting:

## Two independent samples

### Fisher's Exact test
This test is suitable for analysing **discrete** and **nominal** data, with two independent samples that fall into two distinct classes.
Hence, the data can be expressed as a 2x2 as such,

|             |      **Class 1**         | **Class 2** |               |
|-------------|---------------|--------------|---------------|
| **Sample 1**|     A          |     B        | A + B    |
| **Sample 2**  | C       | D          |  C + D    |
|              | A + C          | B + D      |    N = A + B + C + D    |


The Fisher's Exact test tries to determine whether there is a statistically significant relationship between the **'Sample'** (such as gender: male or female) and **'Class'** (such as preference of colour: blue or pink ). In other words, you can check if gender has any influence on whether someone prefers the colour blue or pink.  

### Median test
The Median test can be interpreted as an application of Fisher’s Exact test in a case where each observation is compared to the median of all the observations. Therefore, the Fisher's Exact test is applied to the following 2x2 contingency table with the *'Class'* constructed by comparison of each observation to the median of both independent samples.

|             |      **≤ Median**         | **> Median** |               |
|-------------|---------------|--------------|---------------|
| **Sample 1**|     A          |     B        | A + B    |
| **Sample 2**  | C       | D          |  C + D    |
|              | A + C          | B + D      |    N = A + B + C + D    |


Because an ordering of data is required to accurately define the median, it is important to have **ordinal** data to use this test.


### Mann-Whitney U test
Another test that is suitable for **ordinal** and **continuous** data is the Mann-Whitney U test (also known as the Wilcoxon rank-sum test). This is the most widely used non-parametric test and the non-parametric alternative to Student's t-test.
You can use this test when you want to know if there is a significant difference in the distribution or median of a variable between two independent groups. For example: Are the median test scores of students who received Tutoring Group A significantly different from those who received Tutoring Group B?

Check out the building block on the [Wilcoxon test](https://tilburgsciencehub.com/topics/analyze/Non-parametric-tests/tests/wilcoxon) to learn how to use this test on R.


{{% summary %}}

- Non-parametric tests are generally better than parametric tests as they do not make any assumptions about the underlying population distribution.

- There are several non-parametric tests that one can use depending on the kind of data they have:
|     **Test**        |      **Data Structure**         | **Measurement Scale** |   **Data Type**         |
|-------------|---------------|--------------|---------------|
| **Binomial test**|     One sample          |     Nominal        | Binary    |
| **Chi-squared GoF**|     One sample      |     Nominal        | Binary    |
| **Wilcoxon matched-pairs**|    Two dependent samples          |     Ordinal        | Discrete/Continuous    |
| **McNemar's test**|     Two dependent samples         |     Nominal        | Discrete    |
| **Fisher's Exact test**|     Two independent samples       |     Nominal        | Discrete   |
| **Median test**|      Two independent samples       |     Ordinal        | Discrete   |
| **Mann-Whitney U test**|      Two independent samples       |     Ordinal        | Continuous   |

{{% /summary %}}
