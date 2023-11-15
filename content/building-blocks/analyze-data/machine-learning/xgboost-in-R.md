---
title: "Extreme gradient boosting with XGBoost in R"
description: "Explanation and usage of XGBoost in R"
keywords: "XGBoost, Extreme Gradient Boosting, Machine Learning, R, decision tree, model, Python "
draft: false
weight: 2
author: "Niels Rahder, Kheiry Sohooli"
---

## Overview

In this building block, you will delve deep into the inner workings of XGBoost, a top-tier machine learning algorithm known for its efficiency and effectiveness.

Navigating through this guide, you will gain hands-on experience and broaden your understanding of:

- The 'under the hood' process of how XGboost works.
- How to use XGBoost in `R`, what the hyperparameters are, and how to tune them using a grid search. 
- How to interpret and visualize the results. 

## What is XGBoost?

Extreme gradient boosting is an highly effective and widely used machine learning algorithm developed by [Chen and Guestrin 2016](https://dl.acm.org/doi/10.1145/2939672.2939785). The algorithm works by iteratively building a collection of decision trees, where newer trees are used to correct the errors made by previous trees (think of it as taking small steps in order to come closer to the "ultimate truth"). Additionally, the algorithm uses L1 (Lasso regression) and L2 (Ridge regression) regularization terms in its cost function, and a penalizing term to prevent overfitting and complexity of the model.

This method has proven to be effective in working with large and complex datasets. Also it is famous to handle sparse datasets. XGBoost provides a parallel tree boosting that solve many data science problems such as classification, regression, and recommendation in a fast and accurate way (for example, at the KDDCup in 2015, XGBoost was used by every team ranked in the top 10!).

## Using XGBoost in R

You can get started by using the [`xgboost` package in R](https://cran.r-project.org/web/packages/xgboost/xgboost.pdf). 

In what follows, we use [this dataset from Kaggle](https://www.kaggle.com/code/ekaterinadranitsyna/russian-housing-evaluation-model/input) for illustration. With this dataset we will try to predict the house price based on a number of features (e.g., number of bedrooms, stories, type of building etc).

In order to work with the algorithm you first need to install the `XGBoost` package, load the data and remove some columns via the following commands:

{{% codeblock %}}
```R
#install the xgboost package
install.packages("xgboost")

# Load necessary packages
library(xgboost)
library(tidyverse)
library(caret)

# Open the dataset 
data <- read.csv("../all_v2.csv", nrows = 2000)

#remove columns
data <- data %>%
  select(-date, -time, -geo_lat, -geo_lon, -region)
```
{{% /codeblock %}}

{{% warning %}}
Because XGBoost only works with numeric vectors, you need to convert the categorical values into numerical ones using one-hot encoding or any other approaches.
{{%/ warning %}}

Luckily, this is straightforward to do using the `dplyr` package. One-hot encoding is a process that transforms categorical data into a format that machine learning algorithms can understand. In the code below each category value in a column is transformed into its own column where the presence of the category is marked with a 1, and its absence is marked with a 0.

{{% codeblock %}}
```R

data <- data %>%
  mutate(building_type_1 = as.integer(building_type == 1),
        building_type_2 = as.integer(building_type == 2),
        building_type_3 = as.integer(building_type == 3),
        building_type_4 = as.integer(building_type == 4),
        building_type_5 = as.integer(building_type == 5)) %>%
  select(-building_type)
```
{{% /codeblock %}}

Now that we have one-hot encoded our data we separate the target variable `price` from the input variables. Subsequently, the data is divided into training and testing sets using an 80/20 split ratio. Finally the data is converted into separate data matrices in order for `XGBoost` to use it.

{{% codeblock %}}
```R
#separate target variable (price) from input variables
X <- data %>% select(-price)  
Y <- data$price 

set.seed(123) #set seed for reproducibility

train_indices <- sample(nrow(data), 0.8 * nrow(data)) #sample 80% for training set
X_train <- X[train_indices, ] #extract features for training set
y_train <- Y[train_indices] #extract target values for training set
X_test <- X[-train_indices, ] 
y_test <- Y[-train_indices]

#convert both sets to a DMatrix format, in order for xgboost to work with the data 
dtrain <- xgb.DMatrix(data = as.matrix(X_train), label = y_train)
dtest <- xgb.DMatrix(data = as.matrix(X_test), label = y_test)
```
{{% /codeblock %}}

### Setting Hyperparameters

Now that we have created our training data and test data we need to set up our hyperparameters (think of these as our knobs and handles for the algorithm). These hyperparameters for the XGBoost algorithm consist out of:

  - `max_depth`: Specifies the maximum depth of a tree.
  - `min_child_weight`: Minimum sum of instance weight needed in a child to further split it.
  - `gamma`: Regularization term. Specifies a penalty for each split in a tree.
  - `eta`: Learning rate, which controls the weights on different features to make the boosting process more conservative (or aggressive).
  - `colsample_bytree`: Fraction of features sampled for building each tree (to introduce randomness and variety).
  - `objective`: Specifies the object (regression, or classification).
  - `eval_metric`: Specifies the model performance (e.g. RMSE).
  - `nrounds`: Number of boosting rounds or trees to be built.

Let us now (arbitrarily) set up some hyperparameters:  

{{% codeblock %}}

```R
params <- list(
  max_depth = 4,
  min_child_weight = 1, 
  gamma = 1,
  eta = 0.1, 
  colsample_bytree = 0.8, 
  objective = "reg:squarederror", # Set the objective for regression
  eval_metric = "rmse", # Use RMSE for evaluation
  nrounds = 100 
)

```
{{% /codeblock %}}

{{% tip %}}
You can also use objective = `binary:logistic` for classification.
{{% /tip %}}


With the parameters specified we can now pass them to the `xgb.train` command in order to train the model on the `dtrain` data!
{{% codeblock %}}

```R
xgb_model <- xgb.train(
  params = params,
  data = dtrain,
  nrounds = params$nrounds, 
  early_stopping_rounds = 20, # stop iteration when there test set does not improve for 20 rounds
  watchlist = list(train = dtrain, test = dtest),
  verbose = 1 # print progress to screen
)

```
{{% /codeblock %}}

Finally, let us make some predictions on the new dataset, view the original prices and the predicted prices next to each other, and assess the Mean Absolute Error (MAE).

{{% codeblock %}}

```R
predictions <- predict(xgb_model, newdata = dtest)

results <- data.frame(
  Actual_Price = y_test,
  Predicted_Price = predictions
)

mae <- mean(abs(predictions - y_test))
mea

```
{{% /codeblock %}}

As can be seen the predictions of the algorithm and the original prices still differ significantly (MEA is almost 2 million). A possible reason for this could be that the hyperparameters were arbitrarily chosen. In order to perform a more structured way to choose our hyperparameter we can perform a grid search. 

### Hyperparameter Optimization using Grid Search 
Selecting the correct hyperparameters can prove to be quite a time-consuming task. Fortunately, there exists a technique in the form of grid search that can help alleviate this burden. 

Utilizing a grid search involves selecting a predefined range of potential hyperparameters for examination. The grid search systematically tests each specified combination, identifying the set of parameters that yield the highest level of optimization. Additionally, we make use of a 5-fold cross validation in order to robustly assess the models performance across different subsets of the data. 

{{% codeblock %}}
```R
ctrl <- trainControl(
  method = "cv", # Use cross-validation
  number = 5,  # 5-fold cross-validation
  verboseIter = TRUE, # print progress messages 
  allowParallel = TRUE # allow for prarallel processing (to speed up computations)
)
```
{{% /codeblock %}}

Following which we define the hyperparameter grid: 

{{% codeblock %}}

```R
hyper_grid <- expand.grid(
  nrounds = c(100, 200),
  max_depth = c(3, 6, 8),
  eta = c(0.001, 0.01, 0.1),
  gamma = c(0, 0.1, 0.5),
  colsample_bytree = c(0.6, 0.8, 1),
  min_child_weight = c(1, 3, 5),
  subsample = c(1)
)

```
{{% /codeblock %}}

In order to run the grid search we run the following code. With `X` and `Y` representing the input features and the target variable, respectively (this could take some time).
{{% codeblock %}}

```R
# Perform grid search
xgb_grid <- train(
  X, Y,
  method = "xgbTree", # specify that xgboost is used
  trControl = ctrl, # specify the 5-fold cross validation
  tuneGrid = hyper_grid, 
  metric = "RMSE" # specify the evaluation method
)

# Print the best model
print(xgb_grid$bestTune)
```
{{% /codeblock %}}

from which the output is: 

|            | **nrounds** | **max_depth** | **eta** | **gamma** | **colsample_bytree** | **min_child_weight** | **subsample** |
| --------- | ---------- | ------------- | ------- | --------- | -------------------- | ------------------- | -------------- |
| 445   | 100        | 8             | 0.1     | 0         | 1                    | 1                   | 1              |

indicating the following: 
- `nrounds ` = 100 means that the training process will involve 100 boosting rounds or iterations. 
- The value of 3 for `max_depth` means that the maximum depth of each decision tree in the ensemble was limited to 8 levels.
- `eta` = 0.1 indicates that a relatively small learning rate was applied making the model learn slow (but steady!)
- the value of 0 for `gamma` means that there was no minimum loss reduction required to make a further split. In other words, the algorithm could split nodes even if the split didn't lead to a reduction in the loss function. 
- `colsample_bytree` = 1 indicated that all available features are considered during training
- a new split in a tree node was required to have a minimum sum of instance weights of 1, as indicated by `min_child_weight`
- the full `subsample` was used

### Model Evaluation

For the full set of combinations, the command below can be used. This will also return all other indicators like RMSE, R2, MAE, R2SD, MAESD, allowing you to evaluate model performance.

{{% codeblock %}}

```R
print(xgb_grid$results)
```
{{% /codeblock %}}

Additionally, the importance of individual features can also be assessed. This can be done via the following code: 

{{% codeblock %}}

```R
importance_matrix <- xgb.importance(feature_names = colnames(X), model = xgb_model)
xgb.plot.importance(importance_matrix)

```
{{% /codeblock %}}

Which results in the following graph, from which it can be see that `kitchen_area` is the most important feature in predicting house prices. 

<p align = "center">
<img src = "../img/Features_XGB.png" width="500">
</p>

### Visualization

In order to visualize the created tree (using the hyperparameters found in the grid search), let's run the next line of code:
{{% codeblock %}}

```R
xgb.plot.multi.trees(feature_names = names(data), 
                     model = xgb_model) #the size of this plot can be adjusted by limiting the max_depth variable
```
{{% /codeblock %}}

<p align = "center">
<img src = "../img/tree_plot.png" width="400">
</p>



{{% summary %}}

- **Understanding XGBoost:**
  - Dive into the mechanics of XGBoost's functionality.
  - Explore its application within the `R`.

- **Setting Up and Tuning the Algorithm in R:**
  - Define and understand the hyperparameters.
  - Employ a systematic grid search for optimal model performance.

- **Interpreting and Visualizing Outcomes in R:**
  - Analyze model results for meaningful insights.
  - Visualize your algorithm's efficacy and decision process.

{{% /summary %}}

