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

## What Is XGBoost and HOW It Works
XGBoost, an open-source software library, uses optimized distributed gradient boosting machine learning algorithms within the Gradient Boosting framework.

XGBoost, short for Extreme Gradient Boosting, represents a scalable and distributed gradient-boosted decision tree (GBDT) machine learning library. It offers parallel tree boosting and holds a prominent position as a machine learning library for addressing regression, classification, and ranking challenges.

XGBoost builds upon supervised ML, decision trees algorithm(DT), ensemble learning, and gradient boosting. To deeply understand XGBoost, understanding mentioned concepts are necessary.

#### Supervised Machine Learning

Supervised machine learning involves training algorithms by presenting labeled datasets, where input variables are associated with corresponding output labels. Through this method, the algorithm learns to generalize patterns from the provided examples, enabling it to make accurate predictions or decisions when confronted with new, analogous data. The supervision aspect involves guiding the algorithm to align its predictions with the correct outcomes by leveraging labeled training instances.
for more details read the tutorial [In-depth Introduction to Machine Learning and R](https://tilburgsciencehub.com/topics/analyze/machine-learning/ml-intro/introduction-to-machine-learning/) .

#### Decision Tree 

Decision Trees (DTs) constitute a non-parametric supervised learning method applied for both classification and regression. These trees create a model that predicts the label by assessing a hierarchy of if-then-else true/false feature questions. The objective is to derive simple decision rules from the data features, estimating the minimum number of questions required to gauge the probability of making accurate predictions.

In practical terms, decision trees serve versatile purposes. They can be utilized for classification, where the goal is to predict a category, or for regression, where the aim is to predict a continuous numeric value. 

Go through Decision Tree BB for more details about it.  

#### Ensemble Learning 

Ensemble learning is a flexible approach in machine learning that improves predictive performance through the combination of predictions from multiple models. It consists of three main categories of ensemble learning methods: bagging, stacking, and boosting.

#### Gradient Boosting 

Boosting, a member of ensembel learning techniques, consists of sequentially introducing ensemble members to correct predictions from prior models, resulting in a weighted average of predictions. Gradient Boosting Decision Trees (GBDT) stands as a distinct ensemble learning algorithm, similar to random forests, applied in both classification and regression. 

Both random forests and GBDT develop models featuring multiple decision trees. However, their differentiation lies in the method of constructing and combining these trees. Random forests utilize bagging, concurrently constructing complete decision trees from random bootstrap samples of the dataset, with the final prediction being an average of all decision tree predictions.

Conversely, Gradient boosting, a type of boosting, makes a weak model better by combining it with other weak models through a step-by-step process. It employs a [gradient descent algorithm](http://tilburgsciencehub.com/topics/analyze-data/machine-learning/gradient_descent_variants/) over an objective function, determining targeted outcomes for the subsequent model to minimize errors. These outcomes are based on the gradient of the error, giving rise to the term "gradient boosting."

XGBoost represents a scalable and exceptionally precise implementation of gradient boosting, designed to maximize the potential of computing power in boosted tree algorithms. It is primarily engineered to enhance the performance and computational speed of machine learning models. In contrast to GBDT, XGBoost constructs trees in parallel, adopting a level-wise strategy. This involves scanning gradient values and utilizing partial sums to assess the viability of splits at each potential split within the training set.

For more details over the XGBoost concepts and how it works go to the [Extreme gradient boosting with XGBoost in R](https://tilburgsciencehub.com/topics/analyze/machine-learning/supervised/xgboost/) building block 

### Advantages of XGBoost

This algorithm has several advantages that makes it a favorite algorithm for data scientists. Parallel processing capability of XGBoost makes it fast and efficient. This results in faster training times, making it suitable for large datasets and complex models. It also support implementation on Hadoop. 

XGBoost incorporates regularization techniques, such as L1 and L2 regularization, which help prevent overfitting. This allows the model to generalize well to new, unseen data.

Users can define their own objective functions and evaluation criteria, providing flexibility to tailor the algorithm to specific needs. This is particularly useful when dealing with non-standard or domain-specific objectives.

XGBoost can effectively handle missing data during the training process. It has built-in mechanisms to address missing values in a dataset, reducing the need for extensive data preprocessing.

Finally, XGBoost is built on the gradient boosting framework, which is inherently flexible and allows for the sequential improvement of model predictions. It combines the strengths of multiple weak learners to create a robust and accurate ensemble model.



## Using XGBoost in Python 

To use XGBoost for classification or regression tasks in Python, you'll need to install and import the `xgboost` package. 


{{% codeblock %}}

```Python
# install XGBoost 
pip install xgboost 

# import XGBoost
import xgboost as xgb
```
{{% /codeblock %}}

You can load Diamond dataset from Seaborn package to implement XGBoost with the following codes:

{{% codeblock %}}

```Python
# import Seaborn 
import seaborn as sns

# loading dataset
diamonds = sns.load_dataset("diamonds")
```
{{% /codeblock %}}

After loading and inspecting your data, you should define your X and y variables. In this case, for example, if you're predicting the price of a diamond based on its various characteristics, you would set "price" as your y variable and the diamond's characteristics as your predictors (X).

{{% codeblock %}}

```Python
# selecting all column except 'price' as predictors
X= diamonds.loc[:, diamonds.columns != 'price']

# specify 'price' column to 'y'
y = diamonds[['price']]
```
{{% /codeblock %}}

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

Before training the dataset using the XGBoost algorithm, we need to complete two essential steps: storing the dataset in a `DMatrix` and setting the algorithm's parameters. 
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

{{% tip %}}
You can also import XGBoost from Scikit-learn but native API of XGBoost has more capabilities.
{{% /tip %}}

Use dictionary or list of tuples to specify both `Booster parameters` and `evaluation parameter`. 

{{% codeblock %}}

```Python
# Define Parameters
param = {"objective": "reg:squarederror"}

# set evaluation 
evallist = [(train, 'train'), (test, 'eval')]
```
{{% /codeblock %}}
 
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


### Visualization in Python 

Use the following code to visualize the feature importance when using the XGBoost algorithm to predict the outcome variable. Furthermore, you can also see the trees that have been created.

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

{{% summary %}}

- **Understanding XGBoost:**
  - Explaining in summary the concepts involves in the XGBoost's functionality.
  	* Supervised machine learning 
  	* Decision trees algorithm 
  	* Ensemble learning 
  	* Gradient Boosting 
  - Explore the advantages of XGBoost.
- **Using XGBoost in Python:** 
	- Implementig XGBoost in Python
	- Training the model and evaluation 
	- Hyperparameter tuning
	- Visualizing in Python
  

{{% /summary %}}
