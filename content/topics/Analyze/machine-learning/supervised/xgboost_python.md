---
title: "Extreme Gradient Boosting with XGBoost in Python"
description: "Explanation and usage of XGBoost in Python"
keywords: "XGBoost, Extreme Gradient Boosting, Machine Learning, Python "
draft: false
weight: 5
author: "Kheiry Sohooli" 
authorlink: "https://tilburgsciencehub.com/contributors/kheirysohooli/" 
---

## Overview

This building block explains XGBoost, a leading machine learning algorithm renowned for its efficiency and effectiveness. As you progress through this guide, you will acquire practical experience and enhance your comprehension of:

* The inner workings of XGBoost.

* Using XGBoost in Python, understanding its hyperparameters, and learning how to fine-tune them.

* Visualizing the XGBoost results and feature importance 

## What Is XGBoost?
XGBoost, an open-source software library, uses optimized distributed gradient boosting machine learning algorithms within the Gradient Boosting framework.

XGBoost, short for Extreme Gradient Boosting, represents a scalable and distributed gradient-boosted decision tree (GBDT) machine learning library. It offers parallel tree boosting and holds a prominent position as a machine learning library for addressing regression, classification, and ranking challenges.

## Installing XGBoost in Python

To use XGBoost for classification or regression tasks in Python, you'll need to install and import the `xgboost` package. 

To install the package use `pip`:

{{% codeblock %}}

```Python
# install XGBoost 
pip install xgboost 
```
{{% /codeblock %}}

## Importing the Package into the Workspace

Import the package into your python script or notebook using the following convention:

{{% codeblock %}}
```Python
# import XGBoost
import xgboost as xgb
# we'll also need pandas
import pandas as pd
```
{{% /codeblock %}}

## Working Example: Predicting Diamond Prices

### Loading the Data

To see XGBoost in action we will build a model that predicts the price of diamonds based on their characteristics.
Let's load the `diamonds` dataset from Seaborn package as our example dataset:

{{% codeblock %}}

```Python
# import Seaborn 
import seaborn as sns

# loading dataset
diamonds = sns.load_dataset("diamonds")
```
{{% /codeblock %}}

### Configuring the Data

After loading and inspecting your data, you should define your `X` and `y` variables. 
In this example we want to  predict the price of a diamond based on its characteristics, so we set `price` as your `y` variable and the diamond's characteristics as your predictors, `X`.

{{% codeblock %}}

```Python
# selecting all column except 'price' as predictors
X= diamonds.loc[:, diamonds.columns != 'price']

# specify 'price' column to 'y'
y = diamonds[['price']]
```
{{% /codeblock %}}

### The test-train split

Now, let's divide the data into training and testing sets using the `sklearn.model_selection` module and then check the shape of the data.

{{% codeblock %}}

```Python
# importing train_test_split 
from sklearn.model_selection import train_test_split
# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# check the shapes
import os 
print('X-train shape:',X_train.shape,
     'X-test shape:' , X_test.shape,
     'y_train shape:' ,y_train.shape,
     'y_test shape:' ,y_test.shape,sep=os.linesep )
```
{{% /codeblock %}}


Before training the dataset using the XGBoost algorithm, we need to complete two essential steps: storing the dataset in a `DMatrix` . 
XGBoost uses the `DMatrix` class to efficiently store the dataset, enabling you to run XGBoost optimally.

{{% codeblock %}}

```Python
# import xgboost package
import xgboost as xgb

# train and test data which automaticaly create regression matrices
train = xgb.DMatrix(X_train, y_train, enable_categorical=True)
test= xgb.DMatrix(X_test, y_test, enable_categorical=True)
```
{{% /codeblock %}}

### Specifying Hyperparameters

Next, we set the algorithm's hyperparameters and specify which data stored in a `DMatrix` to use for training and testing.
A dictionary or list of tuples is used to specify both: 

{{% codeblock %}}

```Python
# Define Parameters
param = {"objective": "reg:squarederror"}

# set evaluation 
evallist = [(train, 'train'), (test, 'eval')]
```
{{% /codeblock %}}

### Training the Model

You also need to decide on the number of boosting rounds, which determines how many rounds the XGBoost algorithm will use to minimize the loss function. For now, let's set it to 10, but it's important to note that this is one of the parameters that should be tuned.

{{% codeblock %}}

```Python
# train the model 
num_round = 10
model = xgb.train(param, train, num_round, evallist)
```
{{% /codeblock %}}

The output displays the model's performance (RMSE) on both the training and validation sets. As mentioned earlier, the number of boosting rounds is a crucial tuning parameter. In fact, more rounds mean more attempts to minimize the loss. However, it's important to be careful to prevent overfitting. Sometimes, the model may stop improving after a certain number of rounds. To address this, you can use the following code. We increase the number of rounds to 1000 and introduce the `early_stopping_rounds` parameter to the code above. This ensures that training stops after 50 rounds if there is no improvement in the results. 

{{% codeblock %}}

```Python
# increase number of boosting rounds 
num_round = 1000
model = xgb.train(param, train, num_round, evallist,
   # enabeling early stopping
   early_stopping_rounds=50)
```
{{% /codeblock %}}

XGBoost offers a variety of regularization techniques for model refinement. For detailed information on tuning parameters, please refer to the provided [resource](https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/) .


### Visualizing the Results 

Once the model is trained, we can visualize the feature importance, i.e. which characteristics have the largest effect on price. We can also see the trees that have been created.

{{% codeblock %}}

```Python
import matplotlib.pyplot as plt 
# visualize the importance of predictors
xgb.plot_importance(model)
```
{{% /codeblock %}}

To visualize the trees:

{{% codeblock %}}

```Python

xgb.plot_tree(model)
plt.show()
```
{{% /codeblock %}}

{{% tip %}}
Note that to visualize the trees you need `graphviz`.
{{% /tip %}}

## Summary

{{% tip %}}
You can also import XGBoost from Scikit-learn but native API of XGBoost has more capabilities.
{{% /tip %}}

{{% summary %}}

We covered how to use XGBoost in Python. 
In particular, we covered:

- Implementing XGBoost in Python
- Training the model and evaluation 
- Hyperparameter specification
- Visualizing the trained model output


{{% /summary %}}