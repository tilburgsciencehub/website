---
title: "Support Vector Machines in Python"
description: "Support Vector Machines (SVM) stand out as one of the most popular and effective machine learning classifiers which allow to accomodate for non-linear class boundaries."

keywords: "SVM, machine learning, Python"
date: 17/02/2024
weight: #1
author: "Matteo Zicari"
authorlink: "https://tilburgsciencehub.com/contributors/matteozicari/"
aliases:
  - /supportvectormachine
  - /machinelearning
  - /Python

---


## Overview

The objective of this article is to provide a practical guide to [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm) (SVM) in Python. SVMs are supervised machine learning models that can handle both linear and non-linear class boundaries by selecting the best line (or plane, if not two-diensional) that divides the prediction space to maximize the margin between the classes we are trying to classify.


## Python Application

### Loading Dataset

In this application, we will be using the sklearn Iris dataset. The dataset contains three different target variables corresponding to three different species of iris: *setosa* (0), *versicolor* (1), and *virginica* (2). The goal is to use the sepal length and width of each iris to predict its species.

{{% codeblock %}} 
```python
# Importing libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import datasets
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
iris = datasets.load_iris()

# Transforming 'iris' from an array to a dataframe
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)

# Adding a target variable (dependent variable of our model) to the dataframe
iris_df['target'] = iris.target
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
# Creation of dataset with only sepal features as dependent variables
iris_df = iris_df.drop(['petal length (cm)', 'petal width (cm)'], axis=1)
iris_df.sample(10)
```
{{% /codeblock %}}

Creation of a scatter plot to compare the sepal length and width of different species.

{{% codeblock %}} 
```python
# Creation of dataframes by species
setosa = iris_df[iris_df['target'] == 0]
versicolor = iris_df[iris_df['target'] == 1]
virginica = iris_df[iris_df['target'] == 2]

# Setting figure size
plt.rcParams['figure.figsize'] = (6, 4)

# Plotting each dataframe
plt.scatter(setosa['sepal length (cm)'], setosa['sepal width (cm)'], color='#003f5c', label='Setosa')
plt.scatter(versicolor['sepal length (cm)'], versicolor['sepal width (cm)'], color='#ffa600', label='Versicolor')
plt.scatter(virginica['sepal length (cm)'], virginica['sepal width (cm)'], color='green', label='Virginica')

# Scatter plot settings
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width (by species)')
plt.legend()

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/scatter_iris.png" width="500">
</p>


From the graph above, it's evident that iris setosa can be easily distinguished based on its sepal length and width. However, for the other two species, the division boundary appears to be far from linear, indicating the need for further analysis.


### Training and Test Data

{{% codeblock %}} 
```python
from sklearn.model_selection import train_test_split

X, y = iris_df.iloc[:, :2], iris_df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 21)

X_train.shape, y_train.shape, X_test.shape, y_test.shape

```
{{% /codeblock %}}



### Model Fitting

**EXPLAIN WHY 'RBF' OR 'POLY' MIGHT BE THE MOST APPROPRIATE MODELS GIVEN THE SCATTERPLOT ABOVE**

{{% codeblock %}} 
```python
from sklearn.svm import SVC

svm_model = SVC(kernel='rbf', C=1, random_state=42)
svm_model.fit(X_train, y_train)
```
{{% /codeblock %}}


{{% tip %}} 
Explain that one can also use 'poly' here
{{% /tip %}}



{{% codeblock %}} 
```python
y_pred = svm_model.predict(X_test)
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```
{{% /codeblock %}}


### Hyperparameters Tuning

*RBF Kernel*

{{% codeblock %}} 
```python
from sklearn.metrics import accuracy_score

sigma = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]
C = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]

accuracy = list()
sigma_c = list()

for each_s in sigma:
    for each_c in C:
        svm_model = SVC(kernel='rbf', gamma=1/(2*(each_s**2)), C=each_c, random_state=42)
        svm_model.fit(X_train, y_train)
        y_pred = svm_model.predict(X_test)
        accuracy.append(accuracy_score(y_test, y_pred))
        sigma_c.append((each_s, each_c))
```
{{% /codeblock %}}



{{% codeblock %}} 
```python
index = np.argmax(accuracy)

sigma_max, c_max = sigma_c[index]

print(f'Optimal sigma: {sigma_max}')
print(f'Optimal C: {c_max}')
```
{{% /codeblock %}}



{{% codeblock %}} 
```python

sigma = 0.3
gamma = 1/(2*sigma**2)
C = 10

optimal_svm_model = SVC(kernel='rbf', gamma=gamma, C=C, random_state=42)
optimal_svm_model.fit(X_train, y_train)


y_pred_train = optimal_svm_model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_pred_train)

y_pred_test = optimal_svm_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred_test)

print(f'Training Accuracy: {round(train_accuracy, 3)}')
print(f'Test Accuracy: {round(test_accuracy, 3)}')

```
{{% /codeblock %}}



*Poly Kernel*


{{% codeblock %}} 
```python
degree = [1, 2, 3, 4, 5]
C = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]

accuracy = list()
d_c = list()

for each_d in degree:
    for each_c in C:
        svm_model = SVC(kernel='poly', degree = each_d, C=each_c, random_state=42)
        svm_model.fit(X_train, y_train)
        y_pred = svm_model.predict(X_test)
        accuracy.append(accuracy_score(y_test, y_pred))
        d_c.append((each_d, each_c))
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
index = np.argmax(accuracy)

d_max, c_max = d_c[index]

print(f'Optimal degree: {d_max}')
print(f'Optimal C : {c_max}')
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
degree = 2
C = 0.03

optimal_svm_model = SVC(kernel='poly', degree=degree, C=C, random_state=42)
optimal_svm_model.fit(X_train, y_train)


y_pred_train = optimal_svm_model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_pred_train)

y_pred_test = optimal_svm_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred_test)

print(f'Training Accuracy: {round(train_accuracy, 3)}')
print(f'Test Accuracy: {round(test_accuracy, 3)}')
```
{{% /codeblock %}}


{{% codeblock %}} 
```python

from matplotlib.colors import ListedColormap

# Settings
x_min, x_max = X.iloc[:, 0].min() - 1, X.iloc[:, 0].max() + 1
y_min, y_max = X.iloc[:, 1].min() - 1, X.iloc[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = optimal_svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(6, 4))

# Define colours for each class
setosa_color = '#003f5c'  # Light blue for Setosa
versicolor_color = '#ffa600'  # Light yellow for Versicolor
virginica_color = 'green'  # Light green for Virginica

colors = [setosa_color, versicolor_color, virginica_color]
cmap = ListedColormap(colors)

# Plot decision boundary and color zones using custom colormap
plt.contourf(xx, yy, Z, alpha=0.2, cmap=cmap)

# Scatter plot for each class
setosa = iris_df[iris_df['target'] == 0]
versicolor = iris_df[iris_df['target'] == 1]
virginica = iris_df[iris_df['target'] == 2]

plt.scatter(setosa['sepal length (cm)'], setosa['sepal width (cm)'], color='#003f5c', label='Setosa')
plt.scatter(versicolor['sepal length (cm)'], versicolor['sepal width (cm)'], color='#ffa600', label='Versicolor')
plt.scatter(virginica['sepal length (cm)'], virginica['sepal width (cm)'], color='green', label='Virginica')

# Plot decision boundary lines
plt.contour(xx, yy, Z, colors='k', linewidths=1, alpha=0.5)

# Add labels, title, and legend
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.suptitle('Decision boundary of poly kernel')
plt.title('degree = 2, C = 0.03', fontsize=8)
plt.legend()

# Show the plot
plt.show()

```
{{% /codeblock %}}




{{% summary %}}

{{% /summary %}}


## References

https://www.youtube.com/watch?v=XU5pw3QRYjQ&t=5095s

