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
<!-- 3. Evaluation of a model's results (**Model Evaluation**). -->

The primary objective of machine learning (ML) is to employ `statistical` `learning` `methods`, such as supervised learning, unsupervised learning, and reinforcement learning, to analyse a dataset of interest. ML is primarily concerned with outcome prediction. Therefore, the emphasis lies in utilising techniques that enable the estimation of a function, denoted as f', which closely approximates the real function f. This approximation ensures that the model, once trained, can accurately predict future and unknown values of f based on the acquired knowledge from the dataset.

In the context of supervised learning, where both predictors and responses are known, one of the most widely employed methods is the random forest. This ensemble learning technique leverages the power of multiple [decision trees](https://www.taylorfrancis.com/books/mono/10.1201/9781315139470/classification-regression-trees-leo-breiman), thereby enhancing accuracy and facilitating the generalization of results to previously unseen data. Practically, random forests average many decision trees to reduce their inherent high variance and prevent overfitting.

Among the properties that make decision trees, and hence random forests, outperform less flexible methods such as subset selection techniques or OLS are the facts that they are:

- **non-parametric**: no assumption is made about the functional form of f;
- **flexible**: f' better approximates the real function f;
- **robust** to non-linear relationships between variables;
- **allow for missing values**;
- **intuitive and computationally efficient**.


In addition, random forests can be used not only for exploratory data anlaysis and predictive modelling, but also for variable selection and dimensionality reduction. Finally, they are used to perform both regression and classification tasks and can handle large datasets with high dimensionality. 


## Theoretical Background

In order to explain how random forests make predicitions, it is necessary to start from basic decision trees. Decision trees divide the predictor space into R distinct regions. In a regression problem, every training observation that is part of the same region (Rj) is predicted as the mean of the response values that are part of that region. Instead, in a classification problem, the most occurring class within each region is then defined as the class to which each training observation of the region belongs. Therefore, within the same region Rj, we make the same predictions. 

The predictor space is divided by following a *top-down* and *greedy* approach called `recursive` `binary` `splitting`. It is top-down because it starts from the top of the tree and greedy because each split is chosen based on a criterion that maximises the information gain at that specific point, rather than choosing a split that would lead to an overall greater information gain.

{{% warning %}} 
Decision trees represent a great alternative to other supervised learning methods when it comes to interpretability. However, due to their **high variance**, they tend to perform worse in terms of predictability.
{{% /warning %}}

The `solution` is to employ tree-based methods (e.g., **random forests**) that rely on multiple decision trees that are combined together to give a single consensus prediction.  

{{% tip %}}
This is accomplished by exploiting the principle that, in a **sequence** of **n independent observations**, each with its own variance, the **variance of the mean goes to zero** as n becomes sufficiently large. As a result, it becomes possible to decrease the inherent high variance of decision trees and enhance test set accuracy by iteratively sampling from the training set to estimate the sampling distribution of the relevant statistic.
{{% /tip %}}






## Python Application

The following section provides a step-by-step guide on implementing the [Random Forest](https://scikit-learn.org/stable/modules/ensemble#random-forests-and-other-randomized-tree-ensembles) method in Python using the `scikit-learn` library.

### Importing Libraries

{{% codeblock %}} 
```python

import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

ADD MORE IF NEEDED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

```
{{% /codeblock %}}


### Loading Dataset

In this practical application, we will be using the sklearn Iris Dataset. 

{{% codeblock %}} 
```python

# Loading dataset
iris = datasets.load_iris()

# Transforming 'iris' from an array to a dataframe
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)

# Adding a target variable (dependent variable of our model) to the dataframe
iris_df['target'] = iris.target

# Summary statistics
iris_df.describe()

```
{{% /codeblock %}}



### Exploratory Data Analysis

Exploratory data analysis allows one to identify `patterns` and `relationships` (i.e., missing values, distribution of variables, balanced/imbalanced datsets etc..) within the data. This is relevant to gain insights which can then guide further analysis or hypothesis generation. Three examples of possible ways to proceed are provided below.

Checking if the dependent variable is **balanced**:
{{% codeblock %}} 
```python

value_counts = iris_df['target'].value_counts()
print(value_counts)

```
{{% /codeblock %}}

Checking for **missing values**:

{{% codeblock %}} 
```python

missing_values = iris_df.isnull().sum()
print(missing_values)

```
{{% /codeblock %}}


**Plotting histograms** with `matplotlib` to gain insights into the distribution of the data:

{{% codeblock %}} 
```python

# SEPAL LENGTH
petal_length_counts = iris_df['sepal length (cm)'].value_counts().reset_index()
petal_length_counts.columns = ['Sepal Length (cm)', 'Count']
petal_length_counts = petal_length_counts.sort_values(by = 'Sepal Length (cm)')

plt.bar(petal_length_counts['Sepal Length (cm)'], petal_length_counts['Count'], align = 'center', alpha = 0.7)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Number of Instances')
plt.title('Number of Instances by Sepal Length')
plt.show()

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/sepal_length.png" width="500">
</p>

{{% codeblock %}} 
```python

# PETAL LENGTH
petal_length_counts = iris_df['petal length (cm)'].value_counts().reset_index()
petal_length_counts.columns = ['Petal Length (cm)', 'Count']
petal_length_counts = petal_length_counts.sort_values(by = 'Petal Length (cm)')

plt.bar(petal_length_counts['Petal Length (cm)'], petal_length_counts['Count'], align = 'center', alpha = 0.7, color = 'green')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Number of Instances')
plt.title('Number of Instances by Petal Length')
plt.show()

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/petal_length.png" width="500">
</p>

From the two graphical representations above, it is clear that **petal length** has a **bimodal distribution**, which suggests that the data can be grouped into two separate clusters.


### Data Preprocessing

Once we have a clearer picture of the dataset we are dealing with, we can proceed with the necessary transformations (i.e., standardisation, normalisation, encoding categorical features, imputing missing values, and/or splitting the dataset into training and testing set) required for model fitting and hypothesis testing. Two examples of possible ways to proceed are provided below.

**Feature scaling** ensures that features with different scales contribute equally to the model's performance. This is achieved by standardising the features to have zero mean and unit variance.

{{% codeblock %}} 
```python

# Standardisation
scaler = StandardScaler()
iris_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']] = scaler.fit_transform(iris_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']])

# Summary statistics
iris_df.describe()

```
{{% /codeblock %}}

Splitting a dataset into **training** and **testing** sets is a fundamental step in every machine learning workflow. The purpose of the training set is to teach a model how to make predictions based on a certain set of inputs. Once the model has been trained, the testing set is used to evaluate the performance of the model on unseen data.


{{% codeblock %}} 
```python

# Splitting the dataset into two parts to represent dependent and independent variables
X, y = iris_df.iloc[:, :2], iris_df.target

# Generation of training and testing datasets for both dependent and independent variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 21)

```
{{% /codeblock %}}



### Model Fitting

**Training the Model**

{{% codeblock %}} 
```python

r_forest = RandomForestClassifier(n_estimators = 500, 
                               random_state = 17,
                               oob_score = True,
                               criterion = "gini",
                               max_depth = 4)

r_forest.fit(X_train, y_train)
r_forest.score(X_test, y_test)
```
{{% /codeblock %}}






{{% codeblock %}} 
```python


```
{{% /codeblock %}}


### Model Evaluation











{{% summary %}}

{{% /summary %}}