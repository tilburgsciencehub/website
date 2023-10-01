---
title: "Extreme gradient boosting with XGBoost in R"
description: "Explanation and usage of XGBoost in R"
keywords: "XGBoost, Extreme Gradient Boosting, Machine Learning, R, decision tree, model "
draft: false
weight: 2
author: "Niels Rahder"
authorlink: "https://www.linkedin.com/in/nielsrahder" 
---


## Overview

Extreme gradient boosting is an highly effective and widely used machine learning prediction model, developed by [Chen and Guestrin 2016](https://dl.acm.org/doi/10.1145/2939672.2939785). 

The method has proven to be effective in working with 
- large and complex datasets,  and 
- was used to address a wide range of problems (for example, at the KDDCup in 2015, XGBoost was used by every team ranked in the top 10!)

The algorithm works by 
- gradient boosting to build a collection of trees (i.e., iteratively adding new trees to the collection to correct the errors made by previous trees - think of it as taking very small steps towards the "ultimate truth"), and 
- regularization to prevent overfitting. 

## Using `XGBoost` in R

You can get started by using the [`xgboost` package in R](https://cran.r-project.org/web/packages/xgboost/xgboost.pdf). 

In what follows, we use [this dataset from Kaggle](https://www.kaggle.com/datasets/ashydv/housing-dataset) for illustration.

```r
# Load necessary packages
library(xgboost)
library(tidyverse)
library(caret)

# Open the dataset 
data <- read.csv("../all_v2.csv", nrows = 7500)

#remove columns
data <- data %>%
  select(-date, -time, -geo_lat, -geo_lon, -region)
```
{{% warning %}}
XGBoost only works with numeric vectors, so you need to one-hot encode you data.

{{% /warning %}}

```r

data <- data %>%
  mutate(building_type_1 = as.integer(building_type == 1),
        building_type_2 = as.integer(building_type == 2),
        building_type_3 = as.integer(building_type == 3),
        building_type_4 = as.integer(building_type == 4),
        building_type_5 = as.integer(building_type == 5)) %>%
  select(-building_type)
```

Next, we separate the target variable `price` from the input variables. Subsequently, the data is divided into training and testing sets using an 80/20 split ratio. Finally the data is converted into separate data matrices in order for `XGBoost` to use it.

```r
#separate target variable (price) from input variables
X <- data %>% select(-price)  
Y <- data$price 

set.seed(123)

train_indices <- sample(nrow(data), 0.8 * nrow(data))
X_train <- X[train_indices, ]
y_train <- Y[train_indices]
X_test <- X[-train_indices, ]
y_test <- Y[-train_indices]

dtrain <- xgb.DMatrix(data = as.matrix(X_train), label = y_train)
dtest <- xgb.DMatrix(data = as.matrix(X_test), label = y_test)
```

Let us now set up some hyperparameters. We are going to conduct a grid search later for optimizing them!

```r
params <- list(
  max_depth = 4,  # Limit the tree depth
  min_child_weight = 1, 
  gamma = 1,
  eta = 0.1, 
  colsample_bytree = 0.8, 
  objective = "reg:squarederror", # Set the objective for regression
  eval_metric = "rmse", # Use RMSE for evaluation
  nrounds = 100 
)

```

We can now pass the parameters to the command `xgb.train` to train the model on the `dtrain` data!

```r
xgb_model <- xgb.train(
  params = params,
  data = dtrain,
  nrounds = params$nrounds, 
  early_stopping_rounds = 20, # stop iteration when there test set does not improve for 20 rounds
  watchlist = list(train = dtrain, test = dtest),
  verbose = 1 #print progress to screen
)

```

Finally, let us make some predictions on the new data set.

```r
predictions <- predict(model, newdata = dtest)

```

{{% tip %}}
You can also use objective = `binary:logistic` for classification.
{{% /tip %}}

## Hyperparameter optimization using grid search 
Selecting the correct hyperparameter selection can prove to be quite a time-consuming task. Fortunately, there exists a technique in the form of grid search that can help alleviate this burden. 

Using a grid search entails the usage of a predefined range encompassing potential hyperparameters that are subject to exploration. Following this, the process systematically traverses through these specified options, resulting in the identification of the configuration that offers the highest degree of optimization. 

Next, we make use of a 5-fold cross validation in order to robustly assess the models performance across different subsets of the data. Moreover, to expedite the overall procedure, parallel processing is used, enabling (when possible) simultaneous computation and thus acceleration of the analysis. 

```r
ctrl <- trainControl(
  method = "cv",
  number = 5,  # 5-fold cross-validation
  verboseIter = TRUE, # print progress messages 
  allowParallel = TRUE 
)
```

Following which we define the hyperparameter grid 

```r
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
In order to run the grid search we run the following code. With `X` and `Y` representing the input features and the target variable, respectively. 

```r
# Perform grid search
xgb_grid <- train(
  X, Y,
  method = "xgbTree", # specify that xgboost is used
  trControl = ctrl, 
  tuneGrid = hyper_grid, 
  metric = "RMSE" # specify the evaluation method
)

# Print the best model
print(xgb_grid$bestTune)
```

from which the output is: 

|           | **nrounds** | **max_depth** | **eta** | **gamma** | **colsample_bytree** | **min_child_weight** | **subsample** |
| --------- | ---------- | ------------- | ------- | --------- | -------------------- | ------------------- | -------------- |
| 679   | 100        | 3             | 0.1     | 0         | 1                    | 3                   | 1              |

indicating the following: 
- `nrounds ` = 100 means that the training process will involve 100 boosting rounds or iterations. 
- The value of 3 for `max_depth` means that the maximum depth of each decision tree in the ensemble was limited to 3 levels.
- `eta` = 0.1 indicates that a relatively small learning rate was applied making the model learn slow (but steady!)
- the value of 0 for `gamma` means that there was no minimum loss reduction requred to make a further split. In other words, the algorithm could split nodes even if the split did't lead to a reduction in the loss function. 
- `colsample_bytree` = 1 indicated that all avalable features are considered during training
- a new split in a tree node was required to have a minimum sum of instance weights of 3, as indicated by `min_child_weight`
- the full `subsample` was used

for the full set of combinations the command below can be used. 
```r
print(xgb_grid$results)
```

This will also return all indicators like 
- RMSE
- Rsquared 
- MAE
- RMSESD
- RsquaredSD
- MAESD

## Visualization

In order to visualize the created tree (using the hyperparameters found in the grid search), let's run the next line of code:

```r
xgb.plot.multi.trees(feature_names = names(data), 
                     model = xgb_model) #the size of this plot can be adjusted by limiting the max_depth varibale
```

<p align = "center">
<img src = "../img/tree_plot.png" width="400">
</p>

{{% tip hint %}}
__Under the hood: How does XGboost work?__

The algorithm start by calculating the residual values for each data point, based on an initial estimate. For instance, given the variables `age` and `degree`, we compute the residual values relative to `salary`, for which the value `49` will serve as our initial estimation:

  | **Salary**  | **age** | **degree** | **Residual** |
  | --------- | ---------- | --------- | --------- |
  |     40   | 20   | yes |  -9   |
  |   46   |  28    | yes |  -3   |
  |   50   |  31    | no |  1   |
  |    54   |  34   | yes |  5   |
  |   61   |  38    | no |  12   |


Next, the algorithm calculates the similarity score for the entire tree and the individual splits, especially focusing on an arbitrarily chosen mean value of 24 (the mean between the first two age values) using the following formula:  
  
<div style="text-align: center;">
{{<katex>}}
\text{Similarity score} = \frac{{(\sum \text{Residual})^2}}{{\text{\# of Residual} + \lambda}}
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score root node} (\lambda = 1) = \frac{(-9 - 3 + 1 + 5 + 12)^2}{6} = \frac {36}{6} = 6 
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score left node} (\lambda = 1) = \frac{(-9 )^2}{2} = 40.5 
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score right node} (\lambda = 1) = \frac{(- 3 + 1 + 5 + 12 )^2}{5} = 112.5
{{</katex>}}
</div>

<br>

{{% warning %}}
λ is a regularization parameter which is used to prune the tree. For now, we set it to the default value of 1
{{% /warning %}}

Following the calculation of the individual similarity scores, the gain is calculated as:

<div style="text-align: center;">
{{<katex>}}
\text{Gain} = \text{sim(left node)} + \text{sim(right node)} - \text{sim(root node)}
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Gain} = 40.5 + 112.5 - 6 = 147
{{</katex>}}
</div>

<br>

The algorithm then compares this value to gain values generated by other split options within the dataset to determine which division optimally enhances the separation of classes. When (for example) we take the split value of 29.5 (the mean value between the second and the third age). The similarity score of the root node stays the same, while the similarity score of the left and right node changes to: 

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score left node} ( \lambda = 1) = \frac{(-9 -3)^2}{3} = 72
{{</katex>}}
</div>

<br> 

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score right node} ( \lambda = 1) = \frac{(1 + 5 + 12)^2}{4} = 162
{{</katex>}}
</div>

<br> 

The gain value therefore becomes:
<br> 

<div style="text-align: center;">
{{<katex>}}
\text{Gain} = {72 +  162 - 6 } =228
{{</katex>}}
</div>

<br> 

Which is a higher value than that of the split based on our initial values, and is therefore used as the more favorable option. The same process is then repeated for all possible split combinations in order to find the best option. After this process is completed for all possible split options the final tree (with the residual values) becomes:

<p align = "center">
<img src = "../img/tree_structure.png" width="400">
</p>

The ouput value is for each datapoint is then calculated via the following formula: 

<div style="text-align: center;">
{{<katex>}}
\text{Output value} = {\text{initial estimate} +  \alpha * \text{output of tree} } 
{{</katex>}}
</div>

{{% warning %}}
ɑ is the learning rate of the model, for now we set it to the default value of 0.3 
{{% /warning %}}

<br> 

<div style="text-align: center;">
{{<katex>}}
\text{Output value (age = 20)} = {49 +  0.3 * -6 } = 47.2
{{</katex>}}
</div>

<br> 

From this we can see that our output value for the average salary of a 20 year old has decreased from the initial prediction of 49 to our new prediction of 47.2, which is closer to the true value of 40. An overview of all output values can be found below, from these output values the new residual values `Res2` are constructed. From this it can be seen that the average residual has decreased! 

This process is then repeated until the model cannot improve anymore  


| **Salary**  | **age** | **degree** | **Residual** | **Output** | **Residual 2** |
| --------- | ---------- | --------- | --------- |  --------- | --------- |
|     40   | 20   | yes |  -9   | 47.2 | -7.2 |
|   46   |  28    | yes |  -3   | 47.2 | -7.2 |
|   50   |  31    | no |  1   | 50.95 | -0.95 |
|    54   |  34   | yes |  5   | 50.5 | 3.5 |
|   61   |  38    | no |  12   | 50.95 | 10.05 |

An additional factor we need to take into account is γ, which is an arbitrary regularization parameter that controls the complexity of individual trees in the boosting process. It is a measure of how much an additional split will need to reduce loss in order to be added to the ensemble. 
A higher gamma value encourages simpler trees with fewer splits, which helps to prevent overfitting and lead to a more generalized model. A lower gamma, on the other hand, allows for more splits and potentially more complex trees which may lead to better fit on the training data but could increase the risk of overfitting.  

The tree is pruned when the gain value - gamma < 0 (then the branch is removed). In other words the gain value always needs to be higher than gamma in order for a split to be used. 

<br> 

<div style="text-align: center;">
{{<katex>}}
\text{gain value - }\gamma < 0
{{</katex>}}
</div>

<br> 

{{% /tip %}}

