---
title: "Introduction to Random Forests in Python"
description: "Random Forests are one of the most widely used and effective machine learning (ML) algorithms. The balanced trade-off between flexibility of the model and interpretability of the results makes random forests a ML method worth analysing from both theoretical and practical perspectives."
keywords: "random forests, machine learning, Python"
date: 24/11/2023
weight: #1
author: "Matteo Zicari"
authorlink: "https://tilburgsciencehub.com/contributors/matteozicari/"
aliases:
  - /randomforest
  - /machinelearning
  - /Python

---


## Overview

The goal of this article is to provide a theoretical and practical guide to [random forests](https://link.springer.com/article/10.1023/a:1010933404324). The article is divided as follows:

1. Introduction to Random Forests (**Theoretical Background**).
2. Practical application in Python (**Python Application**).
3. Evaluation of the model's results (**Model Evaluation**).

The primary objective of machine learning (ML) is to employ `statistical` `learning` `methods`, such as supervised learning, unsupervised learning, and reinforcement learning, to analyse a dataset of interest. ML is primarily concerned with outcome prediction. Therefore, the emphasis lies in utilising techniques that enable the estimation of a function, denoted as f^, which closely approximates the real function f. This approximation ensures that the model, once trained, can accurately predict future and unknown values of f based on the acquired knowledge from the dataset.

In the context of supervised learning, where both predictors and responses are known, one of the most widely employed methods is the random forest. This ensemble learning technique leverages the power of multiple [decision trees](https://www.taylorfrancis.com/books/mono/10.1201/9781315139470/classification-regression-trees-leo-breiman), thereby enhancing accuracy and facilitating the generalization of results to previously unseen data.

Among the properties that make decision trees, and hence random forests, outperform less flexible methods such as subset selection  lasso or OLS, are the facts that they are:

- **non-parametric**: no assumption is made about the functional form of f;
- **flexible**: f^ better approximates the real function f;
- **robust**: to non-linear relationships between variables;
- **allow for missing values**;
- **intuitive and computationally efficient**.


Finally, random forests can be used not only for exploratory data anlaysis and predictive modelling, but also for variable selection and dimensionality reduction. 


## Theoretical Background

In order to explain how random forests make predicitions, it is necessary to start from basic decision trees. Decision trees divide the predictor space into R distinct regions. Every observation that is part of the same region (Rj) is predicted as the mean of the response values that are part of that region. Therefore, within the same region Rj, we make the same predictions. 

The predictor space is divided by following a *top-down* and *greedy* approach called `recursive` `binary` `splitting`. It is top-down because it starts from the top of the tree and greedy because each split is chosen based on a criterion that maximises the information gain at that specific point, rather than choosing a split that would lead to an overall greater information gain.

{{% warning %}} 
Decision trees represent a great alternative to other supervised learning methods when it comes to interpretability. However, due to their **high variance**, they tend to perform worse in terms of predictability.
{{% /warning %}}

The `solution` is to employ tree-based methods (e.g., **random forests**) that rely on multiple decision trees that are combined together to give a single consensus prediction.  

{{% tip %}}
This is accomplished by exploiting the principle that, in a *sequence* of *n independent observations*, each with its own variance, the *variance of the mean goes to zero* as n becomes sufficiently large. As a result, it becomes possible to decrease the inherent high variance of decision trees and enhance test set accuracy by iteratively sampling from the training set to estimate the sampling distribution of the relevant statistic.
{{% /tip %}}




## Python Application

{{% codeblock %}} 
```python


```
{{% /codeblock %}}


## Model Evaluation











{{% summary %}}

{{% /summary %}}