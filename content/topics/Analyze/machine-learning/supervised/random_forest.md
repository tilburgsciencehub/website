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

The goal of this article is to provide a theoretical and practical guide to [Random Forests](https://link.springer.com/article/10.1023/a:1010933404324). The article is divided as follows:

1. Introduction to Random Forests (**Theoretical Background**).
2. Practical application in Python (**Python Application**).

The primary objective of machine learning (ML) is to employ *statistical learning methods*, such as supervised learning, unsupervised learning, and reinforcement learning, to analyse a dataset of interest. ML is primarily concerned with outcome prediction. Therefore, the emphasis lies in utilising techniques that enable the estimation of a function, denoted as f', which closely approximates the real function f. This approximation ensures that the model, once trained, can accurately predict future and unknown values of f based on the acquired knowledge from the dataset.

In the context of *supervised learning*, where both predictors and responses are known, one of the most widely employed methods is the random forest. This ensemble learning technique leverages the power of multiple [Decision Trees](https://www.taylorfrancis.com/books/mono/10.1201/9781315139470/classification-regression-trees-leo-breiman), thereby enhancing accuracy and facilitating the generalization of results to previously unseen data. Practically, random forests average many decision trees to reduce their inherent high variance and prevent overfitting.

Among the properties that make decision trees, and hence random forests, outperform less flexible methods such as subset selection techniques or OLS are the facts that they are:

- **non-parametric**: no assumption is made about the functional form of f;
- **flexible**: f' better approximates the real function f;
- **robust** to non-linear relationships between variables;
- **allow for missing values**;
- **intuitive and computationally efficient**.


In addition, random forests can be used not only for exploratory data anlaysis and predictive modelling, but also for variable selection and dimensionality reduction. Finally, they are employed in both regression and classification tasks and can handle large datasets with high dimensionality. 


## Theoretical Background

In order to explain how random forests make predicitions, it is necessary to start from basic decision trees. Decision trees divide the predictor space into R distinct regions. In a **regression problem**, every training observation that is part of the same region (Rj) is predicted as the mean of the response values that are part of that region. Instead, in a **classification problem**, the most occurring class within each region is then defined as the class to which each training observation of the region belongs. Therefore, within the same region Rj, we make the same predictions. 

The predictor space is divided by following a *top-down* and *greedy* approach called *recursive binary splitting*. It is top-down because it starts from the top of the tree and greedy because each split is chosen based on a criterion that maximises the information gain at that specific point, rather than choosing a split that would lead to an overall greater information gain.

{{% warning %}} 
Decision trees represent a great alternative to other supervised learning methods when it comes to interpretability. However, due to their **high variance**, they tend to perform worse in terms of predictability.
{{% /warning %}}

The solution is to employ tree-based methods (e.g., random forests) that rely on multiple decision trees that are combined together to give a single consensus prediction.  

{{% tip %}}
This is accomplished by exploiting the principle that, in a **sequence** of **n independent observations**, each with its own variance, the **variance of the mean goes to zero** as n becomes sufficiently large. As a result, it becomes possible to decrease the inherent high variance of decision trees and enhance test set accuracy by iteratively sampling from the training set to estimate the sampling distribution of the relevant statistic.
{{% /tip %}}



## Python Application

The following section provides a step-by-step guide on implementing the [Random Forest](https://scikit-learn.org/stable/modules/ensemble#random-forests-and-other-randomized-tree-ensembles) method in Python using the `scikit-learn` library.


### Loading Dataset

In this practical application, we will be using the sklearn Iris Dataset. 

{{% codeblock %}} 
```python
import pandas as pd
import numpy as np
import sklearn
from sklearn import datasets

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

Exploratory data analysis allows one to identify *patterns* and *relationships* (i.e., missing values, distribution of variables, balanced/imbalanced datsets etc..) within the data. This is relevant to gain insights which can then guide further analysis or hypothesis generation. Three examples of possible ways to proceed are provided below.

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


**Plotting** a **histogram** for each variable, grouped by the target variable, using `matplotlib` to gain insights into the distribution of the data:

{{% codeblock %}} 
```python
import matplotlib.pyplot as plt

cols = iris.feature_names

for label in cols:
    plt.hist(iris_df[iris_df["target"]==0][label], color='green', label = '0', alpha=0.7)
    plt.hist(iris_df[iris_df["target"]==1][label], color='blue', label = '1', alpha=0.7)
    plt.hist(iris_df[iris_df["target"]==2][label], color='red', label = '2', alpha=0.7)
    plt.title(label)
    plt.ylabel("Count")
    plt.xlabel(label)
    plt.legend()
    plt.show()
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/sepal_length.png" width="500">
</p>

<p align = "center">
<img src = "../images/sepal_width.png" width="500">
</p>

<p align = "center">
<img src = "../images/petal_length.png" width="500">
</p>

<p align = "center">
<img src = "../images/petal_width.png" width="500">
</p>

From the four graphical representations above, it is clear that both **petal length** and **petal width** exhibit a **bimodal distribution**, implying that the data can be partitioned into two distinct clusters.


### Data Preprocessing

Once we have a clearer picture of the dataset we are dealing with, we can proceed with the necessary transformations (i.e., standardisation, normalisation, encoding categorical features, imputing missing values, and/or splitting the dataset into training and testing set) required for model fitting and hypothesis testing. Two examples of possible ways to proceed are provided below.

**Feature scaling** ensures that features with different scales contribute equally to the model's performance. This is achieved by standardising the features to have zero mean and unit variance.

{{% codeblock %}} 
```python
from sklearn.preprocessing import StandardScaler

# Standardisation
scaler = StandardScaler()
iris_df[iris.feature_names] = scaler.fit_transform(iris_df[iris.feature_names])

# Summary statistics
iris_df.describe()

```
{{% /codeblock %}}

Splitting a dataset into **training** and **testing** sets is a fundamental step in every machine learning workflow. The purpose of the training set is to teach a model how to make predictions based on a certain set of inputs. Once the model has been trained, the testing set is used to evaluate the performance of the model on unseen data.


{{% codeblock %}} 
```python
from sklearn.model_selection import train_test_split

# Splitting the dataset into two parts to represent dependent and independent variables
X, y = iris_df.iloc[:, :2], iris_df.target

# Generation of training and testing datasets for both dependent and independent variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 21)

```
{{% /codeblock %}}



### Model Fitting

**Training** the model:

{{% codeblock %}} 
```python
from sklearn.ensemble import RandomForestClassifier

# Random forest model
r_forest = RandomForestClassifier(n_estimators = 500, # number of trees in the forest
                               random_state = 17,
                               criterion = 'gini', # splitting criterion
                               max_depth = 4,
                               max_features = 'sqrt') # maximum number of end-nodes of the tree

# Fitting the model
r_forest.fit(X_train, y_train)

```
{{% /codeblock %}}

In the code snippet above, the *random_state* parameter is utilised to consistently produce the same set of random decisions during the training process, ensuring **reproducibility**. In addition, the *max_depth* parameter controls the maximum depth of each individual decision tree. You may want to set a maximum depth to **avoid overfitting** and **enhance interpretability** while being aware that it may come at the expense of predicition accuracy within the training set.

{{% tip %}} 

When implementing the [RandomForestClassifier()](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier), two sources of **randomness** are introduced. **First**, every tree is built from a sample drawn with replacement from the training set. **Second**, each split needed to construct a tree can be made either from all available inputs or from a subset of those inputs (normally, the subset is equal to the square root of the total number of input features). 

**What is the purpose of such randomness?**

As mentioned in the *Theoretical Background* section, the objective is to reduce the high variance of decision trees. Introducing randomness allows us to create decision trees with less correlated prediction errors. Consequently, when averaging multiple trees, some of the errors may cancel out, resulting in an overall improved model.


{{% /tip %}}


### Model Evaluation
Given the prediction-oriented focus of machine learning, the goal is to **minimise the overall prediction error**, which is made up of three components, namely, **bias**, **variance**, and **irreducible error**. The bias decreases with flexibility, the variance increases with flexibility, and the irreducible component is a consequence of data noise and cannot really be dealt with. To determine the model with the optimal variance-bias trade-off, various **evaluation techniques** can be employed.

Use the previously trained model to **make predictions**:

{{% codeblock %}} 
```python
y_pred = r_forest.predict(X_test)

```
{{% /codeblock %}}

Employ **evaluation techniques** such as accuracy, precision, and recall to **assess model performance**:

{{% codeblock %}} 
```python
from sklearn import metrics
```
{{% /codeblock %}}


**Accuracy**

Accuracy measures the overall performance of a model by identifying how many observations, whether positive or negative, are correctly classified. The higher the accuracy, the better the performance.

{{% codeblock %}} 
```python
accuracy = metrics.accuracy_score(y_test, y_pred)
accuracy
```
{{% /codeblock %}}


{{% warning %}}
Accuracy is not suitable for imbalanced datasets because it does not account for the class distribution of the data.
{{% /warning %}}


**Precision**

Precision provides the proportion of the truly positive predictions out of all the positive predictions (both true positives and false positives) made by the model. Unlike accuracy, precision can be used with imbalanced datasets and allows to assess the model's ability to minimise false positives. The higher the precision, the better the performance.

{{% codeblock %}} 
```python
precision = metrics.precision_score(y_test, y_pred, average = 'micro')
precision

```
{{% /codeblock %}}


**Recall**

Recall, also known as sensitivity, indicates the ratio of the model's correctly identified positive predictions to all the actual positive predictions. A higher recall value indicates that the model performs well at identifying positive instances. Hence, recall focuses on minimising false negatives.

{{% codeblock %}} 
```python
recall = metrics.recall_score(y_test, y_pred, average = 'micro')
recall

```
{{% /codeblock %}}


The *average* parameter (see precision and recall code snippets) is used in multiclass classification problems to aggregate the precision/recall score for different classes into a single score. If set to *micro*, precision is calculated globally by counting true positives and false positives and then aggregating these values.


{{% tip %}}
**Faster alternative to calculate all evaluation metrics simultaneously:**

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
{{% /tip %}}

### Model Tuning

When employing a model, there can be parameters that are not directly estimated within the model (hyperparameters) and whose values need to be set beforehand. Depending on the parameters chosen, the performance of the model can vary, leading to more or less accurate predictions. Tuning a model (or hyperparameters tuning) requires inputting different combinations of such parameters to identify the combination for which the model's loss is minimised. 

[GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV) allows to search the hyperparameter space to find the optimal combination of hyperparameters.

Using the random forest model employed earlier, the code snippet below shows how to find the best combination of the *n_estimators* and *max_depth* hyperparameters from a pre-set grid.

{{% codeblock %}} 
```python
from sklearn.model_selection import GridSearchCV

# Creating grid with different parameters
params = {'n_estimators': [100, 200, 300, 400, 500],
          'max_depth': np.arange(1, 20)}

# Identifying best parameters
grid = GridSearchCV(estimator = r_forest,
                    param_grid = params,
                    scoring='accuracy')

# Fitting the model 
grid.fit(X_train, y_train)

# Accuracy
print(grid.best_score_)

# Parameters combination that minimises loss
print(grid.best_params_)
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
# Extracting best parameters from grid search
best_max_depth = grid.best_params_['max_depth']
best_n_estimators = grid.best_params_['n_estimators']

# Random forest model with extracted parameters
r_forest = RandomForestClassifier(n_estimators = best_n_estimators, 
                               random_state = 17,
                               oob_score = True,
                               criterion = 'gini',
                               max_depth = best_max_depth,
                               max_features = 'sqrt')

# Fitting the model
r_forest.fit(X_train, y_train)

```
{{% /codeblock %}}


{{% codeblock %}} 
```python
y_pred = r_forest.predict(X_test)
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```
{{% /codeblock %}}


{{% summary %}}
This article introduces Random Forests in Python by providing:

- a simple explanation of the theoretical background behind Random Forests;
- a practical workflow for implementing Random Forests in Python.
{{% /summary %}}