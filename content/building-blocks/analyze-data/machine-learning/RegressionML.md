---
title: "Regression in machine learning"
description: "An introduction to different regression techniques with Python"
keywords: "regression, machine learning, ML, Linear, Regression, lasso, Python"
draft: false
weight: 4
author: "Niels Rahder"
authorlink: "https://www.linkedin.com/in/nielsrahder" 
---

## What is regression in machine learning

Regression is a technique used in supervised machine learning and statistics when the goal is to predict a continuous dependent variable (or target) based on one or more independent variables (or features). Think of it as trying to fit a line (or a curve in some cases) through data points to establish a relationship between the independent and dependent variables. By understanding this relationship, we can make predictions about the target variable for new data points.

For instance, consider the example of predicting a house's price (dependent variable) based on its size in square feet (independent variable). Using regression, we can fit a line through the historical data of houses sold and their sizes. Once this line is established, if we have a new house of a specific size, we can predict its approximate price by looking at where it falls on the line.

There are several regression techniques, such as linear regression, Lasso, and Ridge, each designed to handle specific data characteristics and relationships between variables. 
For this tutorial the following [dataset]( https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market) on housing prices will be used. 

## Types of regression 

### Linear 

Linear regression is a linear approach to model the relationship between a dependent variable `Y` and one or more independent variables `X`. The relationship for a regression with multiple (p) predictors (multiple linear regression) looks like this:

<br>
<div style="text-align: center;">
{{<katex>}}

y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_p x_p + \varepsilon

{{</katex>}}
</div>
<br>

A machine learning model (MLM) tries to optimize the above-mentioned equation by selecting the best weights ($\beta$) for each parameter ($x$). It does this trough a learning process, where it uses data where the outcomes are known to learn the patterns. The cost function is essential in this optimization process. For a regression model, this is typically the Mean Squared Error (MSE), which takes the following form:

<br>

<div style="text-align: center;">
{{<katex>}}
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
{{</katex>}}
</div>

<br>

Where:
- $n$ is the number of observations.
- $y_i$ are the actual values.
- $\hat{y}_i$ are the predicted values by the model.

During training, the model adjusts the $\beta$ coefficients to minimize the MSE. This adjustment continues until the model achieves the lowest possible MSE, meaning it has found the most reliable $\beta$ to predict `Y`. 

In practice linear regression is a starting point for regression analysis, as it is simple and interpretable. However, as relationships in the real world are often non-linear its applicability is limited. 

To work with linear regression in Python the following code block can be used:

{{% codeblock %}}
```Python
#import libraries
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#load dataset
df = pd.read_csv('Melbourne_housing_FULL.csv')

#select columns of interest
cols = ['Suburb', 'Rooms', 'Type', 'Method', 'SellerG', 
        'Regionname', 'Propertycount', 'Distance', 'CouncilArea', 
        'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'Price' ]
df = df[cols]

#replace NA's
cols_zero = ['Propertycount', 'Distance', 'Bedroom2', 'Bathroom' , 'Car']
df[cols_zero] = df[cols_zero].fillna(0)

df['Landsize'] = df['Landsize'].fillna(df.Landsize.mean())
df['BuildingArea'] = df['BuildingArea'].fillna(df.BuildingArea.mean())

df.dropna(inplace=True)
df = pd.get_dummies(df, drop_first= True)

#select Price as the Y variable
X = df.drop('Price', axis = 1)
Y = df['Price']

#create train and test sets
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size = 0.3, 
                                                    random_state= 2)

#fit the regression
reg = LinearRegression().fit(train_X, train_Y)

#Make predictions with linear regression
linear_pred = reg.predict(test_X)

#print metrics
print("Linear MAE:", mean_absolute_error(test_Y, linear_pred))
print("Linear MSE:", mean_squared_error(test_Y, linear_pred))
print("The difference between the test and training score for Linear is:", reg.score(test_X, test_Y) - reg.score(train_X, train_Y))

```
{{% /codeblock %}}

```
Linear MAE: 246805.6289080094
Linear MSE: 342275472103.38684
The difference between the test and training score for Linear is: -0.5442424079619764
```

From the output it can be seen that there is a significant difference in the R2 measure between the training and testing data, which is an indicator of overfitting (non-generalizability). Furthermore, the high Mean Absolute Error (MAE) and Mean Squared Error (MSE) in the linear regression model indicate large average errors and inconsistencies in predictions, respectively. These metrics further indicate that the model's predictions are not only imprecise on average (as shown by the MAE) but also suffer from extreme deviations in some cases (reflected in the high MSE).

To address this, we can make use of Lasso (L1) or Ridge (L2) regression. 

### Lasso Regression (L1 Regularization)

Lasso Regression, which stands for Least Absolute Shrinkage and Selection Operator, is a regression technique that involves penalizing the absolute size of the regression coefficients. By doing so, Lasso penalizes complex models, leading to simpler, more generalizable models (i.e., combating overfitting). Additionally, Lasso can also be used to distinguish important from unimportant features of a datset.

For linear regression, our objective was to minimize the MSE. Lasso also aims to minimize the MSE, but adds a penalty for non-zero coefficients. The cost function for Lasso can be formulated as:

<br>

<div style="text-align: center;">

{{<katex>}}
\text{Cost function (Lasso)} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} |w_j|
{{</katex>}}

</div>

Here, 
- $n$ is the number of observations,
- $y_i$ represents the actual values,
- $\hat{y}_i$ denotes the model's predictions,
- $w_j$ are the model's coefficients,
- $\lambda$ is the regularization parameter.

The $\lambda$ parameter plays a critical role in Lasso (and Ridge) regression, as it serves as the regulator to tune the model. When $\lambda$ is set to 0, there's no penalty on the coefficients, and the model follows that of a standard linear regression (using all the available variables). When $\lambda$ increases, large coefficients are penalized, and the model is forced to be more selective in its variables dropping less important variables. Automatically focusing on coefficients that make an important contribution, and disregarding coefficients that do not, thereby limiting the number of variables and combating overfitting. 

{{% warning %}}

When setting $\lambda$ to high the model becomes too 'tight', ignoring variables that are useful. This over-simplification of the model might lead to underfitting, making the model lose predicting accuracy. 

{{% /warning %}}


To work with lasso in Python the following code snippet can be used (after having ran the code snippet above).

{{% codeblock %}}

```Python 
#let's try Lasso
lasso_reg = linear_model.Lasso(alpha = 50, max_iter=100, tol=0.1) #Lamda is specified here as alpha 
lasso_reg.fit(train_X, train_Y)

# Make predictions with Lasso
lasso_pred_test = lasso_reg.predict(test_X)

# Calculate and print the metrics for Lasso
print("Lasso MAE:", mean_absolute_error(test_Y, lasso_pred_test))
print("Lasso MSE:", mean_squared_error(test_Y, lasso_pred_test))
print("The difference between the test and training score for Lasso is:", lasso_reg.score(test_X, test_Y) - lasso_reg.score(train_X, train_Y))
```

{{% /codeblock %}}

```
Lasso MAE: 236924.54916510652
Lasso MSE: 133653603705.64275
The difference between the test and training score for Lasso is: -0.01308742553623321
```

The Lasso regression results indicate a more stable model compared to the previous linear regression. The smaller difference in R2 scores between training and testing, along with lower MAE and MSE values, suggests improved generalizability and more accurate predictions. 

### Ridge Regression (L2 Regularization)

Ridge regression, an alternative to Lasso, is useful when dealing with multicollinearity in a dataset. Unlike Lasso, which can drive certain coefficients to zero, Ridge regression incorporates L2 regularization, imposing a penalty equivalent to the square of the magnitude of coefficients. This method shrinks the coefficients without being able to set them to exactly zero, ensuring all features remain within the model. This is important in models where every variable carries some form of importance. 

The cost function for Ridge regression takes the following form:

<br>
<div style="text-align: center;">
{{<katex>}}
\text{Cost function (Ridge)} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} w_j^2
{{</katex>}}
</div>
<br>

Here, 
- $n$ is the number of observations,
- $y_i$ represents the actual values,
- $\hat{y}_i$ denotes the model's predictions,
- $w_j$ are the model's coefficients,
- $\lambda$ is the regularization parameter.

Ridge regression can be used in Python by using the following snippet: 


{{% codeblock %}}
```Python 
#let's try Ridge
ridge_reg = linear_model.Ridge(alpha = 50, max_iter=100, tol=0.1) #lambda is specified here as alpha 
ridge_reg.fit(train_X, train_Y)

ridge_pred_test = ridge_reg.predict(test_X)

# Calculate and print the metrics for Ridge
print("Ridge MAE:", mean_absolute_error(test_Y, ridge_pred_test))
print("Ridge MSE:", mean_squared_error(test_Y, ridge_pred_test))

print("The difference between the test and training score for Ridge is:", ridge_reg.score(test_X, test_Y) - ridge_reg.score(train_X, train_Y))
```
{{% /codeblock %}}

The output of this code is: 

```
Ridge MAE: 236797.3711661221
Ridge MSE: 132273414674.95775
The difference between the test and training score for Ridge is: 0.004847220551063125

```

The Ridge regression's results are similar to those of the Lasso regression, showing it's also doing a good job of not overfitting. The very small change in R2 scores between training and testing, along with the lower MAE and MSE errors, means the model is not just memorizing the training data but learning patterns that also apply to new data.  

{{% tip %}}
It is common practice to use the simpler model (Lasso) when the outcomes are (very) similar. 
{{% /tip %}}


## Evaluation 

The most common evaluation metrics for regressions are R-squared (R2), Mean squared error(MSE), and Mean absolute error (MEA). In the next paragraph these metrics will be shortly explained. 

### R2

R2, measures the proportion of the variance in the dependent variable that is predicable from the independent variables(s). It provides a sense of well the predictions fit with the actual data. An advantage of R2 is that it indicates how well the data fits the model, and that it is easy to interpret. A disadvantage of R2 is that it does not indicate whether a regression model is adequate, as you could have a low R2 and a good model or a high R2 for a poor model (overfitting).

<br>
<div style="text-align: center;">
{{<katex>}}

R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} 

{{</katex>}}
</div>

### MAE 

MAE evaluates the absolute distance of the predictions of the regression to the actual entries in the datset. The absolute value between the two values is used, so that negative errors are accounted for properly. The advantage of this is that MAE is easy to understand as it represents average error, and it is not sensitive to outliers. A disadvantage is that MAE is not differentiable, while MSE is (which helps algorithms as it can act as a loss function)

<br>
<div style="text-align: center;">
{{<katex>}}
   \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| 
{{</katex>}}
</div>


### MSE 

MSE, or Mean Squared Error, is similar to MAE, but squares the errors before averaging them. This means that larger errors are emphasized more than smaller errors, and that MSE is more sensitive to outliers than MAE. The advantage of this is that it makes MSE more applicable to real world situations, as some mistakes might be more acceptable than others. A disadvantage is that MSE heavily weights outliers, skewing the error metric which might lead to a misleading representation of the model's performance. 
<br>
<div style="text-align: center;">
{{<katex>}}
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 
{{</katex>}}
</div>





