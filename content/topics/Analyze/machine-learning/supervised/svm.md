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

[SVC](https://scikit-learn.org/stable/modules/svm.html#svc)

https://www.youtube.com/watch?v=XU5pw3QRYjQ&t=5095s



## Python Application




### Importing Packages

{{% codeblock %}} 
```python
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import datasets
```
{{% /codeblock %}}


### Loading Dataset
{{% codeblock %}} 
```python
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
iris_df['target'] = iris.target
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
iris_df = iris_df.drop(['petal length (cm)', 'petal width (cm)'], axis=1)
iris_df.sample(10)
```
{{% /codeblock %}}


{{% codeblock %}} 
```python
# Scatter plot for each class
setosa = iris_df[iris_df['target'] == 0]
versicolor = iris_df[iris_df['target'] == 1]
virginica = iris_df[iris_df['target'] == 2]

plt.rcParams['figure.figsize'] = (6, 4)

plt.scatter(setosa['sepal length (cm)'], setosa['sepal width (cm)'], color='#003f5c', label='Setosa')
plt.scatter(versicolor['sepal length (cm)'], versicolor['sepal width (cm)'], color='#ffa600', label='Versicolor')
plt.scatter(virginica['sepal length (cm)'], virginica['sepal width (cm)'], color='green', label='Virginica')

# Add labels, title, and legend
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width (by species)')
plt.legend()

```
{{% /codeblock %}}

**ADD GRAPH HERE!!!!!!**

<p align = "center">
<img src = "../images/....png" width="500">
</p>


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







{{% summary %}}

{{% /summary %}}


## References

https://www.youtube.com/watch?v=XU5pw3QRYjQ&t=5095s

