---
title: "Regression in Machine Learning"
description: "An introduction to regression pipeline in Python"
keywords: "regression, machine learning, ML, Linear, Regression, Python"
draft: false
weight: 4
author: "Kheiry Sohooli"
authorlink: "https://tilburgsciencehub.com/contributors/kheirysohooli/" 
---

## What is Regression in Machine Learning
Regression is a technique used in supervised machine learning and statistics when the goal is to predict a **continuous dependent variable** (or target) based on one or more independent variables (or features). Think of it as trying to fit a line (or a curve in some cases) through data points to establish a relationship between the independent and dependent variables. By understanding this relationship, we can make predictions about the target variable for new data points.

For instance, consider the example of predicting a house's price (dependent variable) based on several predictors like its size in square feet (independent variable). Using regression, we can fit a line through the historical data of houses sold and their properties. Once this line is established, if we have a new house of a specific characteristics, we can predict its approximate price by looking at where it falls on the line.

There are several regression techniques, such as linear regression, Lasso, and Ridge, each designed to handle specific data characteristics and relationships between variables. 

For this tutorial the [dataset]( https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market) on housing prices from kaggle will be used. 

## Machine learning Pipeline in Regression Problems 
In regression, we have a set of steps to follow, but not all of them are needed for every project. It depends on the data, the type of regression used, and the specific problem. However, there are some steps that are vital for every regression project like the train-test split.

### Get the Data
A common way to store data is in a CSV file. In Pandas, if you want to read a CSV file, you typically use the `read_csv` function. You can do this by using a file path or by providing a URL if the file is online.
These methods are versatile and can handle various scenarios for importing CSV data into Pandas. Additionally, the `read_csv` function provides a wide range of optional parameters that allow you to customize the import process based on your specific requirements (e.g., specifying column names, handling missing values, setting data types).

In following code block you learn how to read data from kaggle using URL. For more details on reading data from kaggle click [here](https://ravi-chan.medium.com/how-to-download-any-data-set-from-kaggle-7e2adc152d7f)


{{% codeblock %}}

```Python
# install required library to load data from kaggle 
!pip install opendatasets --upgrade --quiet

# Import the necessary libraries for data import in Pandas
import pandas as pd
import os
import opendatasets as od

# Assign the data set URL into a variable
dataset = 'https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market'

# download the data sets from melbourne-housing-market
od.download(dataset)

data_directory = './melbourne-housing-market'

# list the datasets in melbourne-housing-market
os.listdir(data_dir_h)

# define a dataframe using the desired dataset
df = pd.read_csv('./melbourne-housing-market/Melbourne_housing_FULL.csv')
```
{{% /codeblock %}}

{{% tip %}}
The alternative way of reading the data is that simply download the data on your computer and load it using Pandas library. 
{{% /tip %}}

### Discover and Visualize the Data to Gain Insights
Before starting modeling every data scientists need to get enough knowledge from the data. There are plenty of ways to disover and explore data which can be used according to the dataset in hand. However, some methods are commonly used. Here are a few of them.

#### Take a Quick Look at the Data Structure
The `head()` method shows you the first 5 rows of your data along with the column names. When you use it, you can see what features are in your dataset and get a quick overview of the values in each column. It's a handy way to get a glimpse of your data.

{{% codeblock %}}

```Python
# get the first 5 rows
df.head()
```
{{% /codeblock %}}


Additionally, the `info()` functions shows useful informations about the total number of samples(rows), and type of each feature(float64, object, etc.) and number of non-null values in each column.

{{% codeblock %}}

```Python
# get the first 5 rows
df.info()
```
{{% /codeblock %}}

Another helpful method is `describe()`, and it provides a summary of numerical features in your data. By running the following code, you can see the statistical information you can obtain using this method.

{{% codeblock %}}

```Python
# get the first 5 rows
df.describe()
```
{{% /codeblock %}}

You can understand your data better by looking at it visually. The code below helps you create a histogram, which shows the distribution of variables in your dataset. While there are various ways to visualize data, this is a good starting point.

{{% codeblock %}}

```Python
# import matplotlib.pyplot. Note that if you haven't install it yet, you need install it before importing. 
import matplotlib.pyplot as plt 

# histogram of all variables in dataframe
df.hist(bins=50, figsize=(20,15))
plt.show()
```
{{% /codeblock %}}


#### Looking for Correlations

In regression tasks, you're trying to estimate the objective variable by using predictor variables. If you have a lot of variables to consider, it's smart to only pick the most important ones. This makes your prediction more accurate and your model less complicated.
there are several ways to find which variables must be included but the simplest while effective way is to find the predictor variables which have higher correlation with the outcome variable(here is price) and include it in the model. You can use the following code to arrange the variables based on how much they're correlated to price.

{{% codeblock %}}

```Python
# create correlation matrix in which the correlation of every variable with all other variables computed. 
corr_matrix = df.corr()
# sort the variables based on the correlation with "price"
corr_matrix["Price"].sort_values(ascending=False)
```
{{% /codeblock %}}

{{% tip %}}

Correlation coefficient ranges from 1 to -1. correlation coefficient 1 indicates high positive correlation and -1 high negative correlation. while zero coefficient shows no linear coefficient. 

{{% /tip %}}

<p align = "center">
<img src = "../img/correlation .png" width="400">
<p align = "center">
Standard correlation coefficient of various datasets (source: Wikipedia)
</p>
                     
{{% tip %}}

To prevent issues with colinearity, don't use predictor variables that are strongly correlated with each other.

{{% /tip %}}



### Preprocessing the Data for Machine Learning Algorithms

#### Data Cleaning

Cleaning data involves different steps, and what you do depends on the dataset. here you see the explanation of only two steps.
1. **Removing Duplicates:**
   If there are identical rows in your dataset, it's a good idea to get rid of them.

{{% codeblock %}}

```Python
# check for duplicates
print("number of duplicated rows:" , sum(df.duplicated()))

# drop duplicate rows
df = df.drop_duplicates()
```
{{% /codeblock %}}

2. **Handling Missing Data:**
   There are a few ways to deal with missing information:
   - Delete rows with missing data.
   - Exclude columns with missing values.
   - Fill in missing values with a specific value like the average, median, zero, etc.

For this particular case, we choose to drop the rows with missing values.

{{% codeblock %}}

```Python
# drop the samples without price
df.dropna(subset=["Price"], inplace= True)

# or you can drop all NA by following codes 
df.dropna( inplace= True)
```
{{% /codeblock %}}

To get a cleaner dataset, you have to do some cleaning steps after checking and analyzing the data. This means you need to look at the data more closely and understand it as well as you can.

#### Handling Categorical Attributes
Many machine learning algorithms use only the numbers, so we have to change categorical data into numbers to use it in the model. One way to do this is by using a method called `LabelEncoder` from scikit-learn. It helps transform categorical values into numerical ones.

{{% codeblock %}}

```Python
# importing LabelEncoder method
from sklearn.preprocessing import LabelEncoder
# create encoder 
encoder = LabelEncoder()

# Transform the categories to numbers
df_cat = df["Type"]
df_cat_encoded = encoder.fit_transform(df_cat)
df_cat_encoded
```
{{% /codeblock %}}

Another way is to use OneHotEncoder. This method turns categories into numbers, creating a new column for each category. However, it's not recommended for variables with many categories due to the potential for a large number of columns.

{{% codeblock %}}

```Python
# import OneHotEncoder 
from sklearn.preprocessing import OneHotEncoder

# create encoder
encoder = OneHotEncoder()

# transform categories to numbers 
df_cat_1hot = encoder.fit_transform(df_cat_encoded.reshape(-1,1))
```
{{% /codeblock %}}

#### Splitting data into train and test sets
Before you start training your model on the data, set aside a part of it to test and evaluate the model afterward. This process is known as train-test-split. The easiest way to do this is by using the train_test_split function from the sklearn library.

{{% codeblock %}}

```Python
# define X and y
X = df[['Rooms','Bedroom2','Bathroom', 'YearBuilt']] #let's select the variables with high positive and negative correlation with price as X 
y = df['Price']

# import train_test_split from sklearn . Note that if you haven't install sklearn yet, you need install it before importing. 
from sklearn.model_selection import train_test_split 

# create train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size = .75)
```
{{% /codeblock %}}

In the code above, pay attention to the "test_size" parameter. It decides how much of the dataset is kept for testing. In our case, we've reserved 20% of the dataset for testing. Also, we set a random seed to make sure the dataset doesn't change every time we run the code.

#### Feature Scaling
This transformation is important when variables have different ranges. For instance, if you compare "rooms" (ranging from 1 to 7) with "yearbuilt" (ranging from 1196 to 2106), you'll notice a big difference. Many machine learning algorithms don't work well when features are in different scales.

{{% tip %}}

Note that scaling the target variable is not necessary.

{{% /tip %}}

There are two main ways to scale features: min-max scaling and standardization. Min-max scaling makes all values fall between 0 and 1. On the other hand, standardization gives a data distribution with a standard deviation of 1.

It's worth noting that standardization is less influenced by outliers.

{{% codeblock %}}

```Python
# import StandardScaler
from sklearn.preprocessing import StandardScaler

# define scaler
scaler = StandardScaler()

# fit scaler on train data 
scaler.fit(X_train)

# transform scaler on train data 
scaler.transform(X_train)

# transfor scaler on test data 
scaler.transform(X_test)
```
{{% /codeblock %}}

{{% tip %}}

It is very important to fit scaler on train data. Then transform on train and test data to avoid information leakage.

{{% /tip %}}

### Select and Train a Model

Finally! You've defined the problem, explored the data, selected samples for training and testing, and cleaned up the data for ML. Now, it's time to choose and train a ML model.

{{% codeblock %}}

```Python
# Import LinearRegression 
from sklearn.linear_model import LinearRegression 

# define regressor 
lin_reg = LinearRegression()

# train the regressor on the train data
lin_reg.fit(X_train, y_train)

# prediction on test data
predictions = lin_reg.predict(X_test)
```
{{% /codeblock %}}

Note that you can train your data using any other regressors but here we just work with one. Feel free to explore other regressors and compare the results with one another. 

### Select a Performance Measure

The most common evaluation metrics for regressions are R-squared (R2), Mean squared error(MSE), and Mean absolute error (MEA). In the next paragraph these metrics will be shortly explained. 

#### R2

R2, measures the proportion of the variance in the dependent variable that is predicable from the independent variable(s). It provides a sense of how well the predictions fit with the actual data. An advantage of R2 is that it indicates how well the data fits the model, and that it is easy to interpret. A disadvantage of R2 is that it does not indicate whether a regression model is adequate, as you could have a low R2 and a good model or a high R2 for a poor model (overfitting).

<br>
<div style="text-align: center;">
{{<katex>}}

R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} 

{{</katex>}}
</div>

#### MAE 

MAE evaluates the absolute distance of the predictions of the regression to the actual entries in the datset. The absolute value between the two values is used, so that negative errors are accounted for properly. The advantage of this is that MAE is easy to understand as it represents average error, and it is not sensitive to outliers. A disadvantage is that MAE is not differentiable, while MSE is (which helps algorithms as it can act as a loss function)

<br>
<div style="text-align: center;">
{{<katex>}}
   \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i| 
{{</katex>}}
</div>


#### MSE 

MSE, or Mean Squared Error, is similar to MAE, but squares the errors before averaging them. This means that larger errors are emphasized more than smaller errors, and that MSE is more sensitive to outliers than MAE. The advantage of this is that it makes MSE more applicable to real world situations, as some mistakes might be more acceptable than others. A disadvantage is that MSE heavily weights outliers, skewing the error metric which might lead to a misleading representation of the model's performance. 
<br>
<div style="text-align: center;">
{{<katex>}}
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 
{{</katex>}}
</div>


{{% codeblock %}}

```Python
from sklearn import metrics

print("mean_absolute_error:", metrics.mean_absolute_error(y_test, predictions))
print("mean_squared_error", metrics.mean_squared_error(y_test, predictions))
import numpy as np
print("root_squared error", np.sqrt(metrics.mean_squared_error(y_test, predictions)))
```
{{% /codeblock %}}

### Fine-Tune Your Model

Imagine you have a list of models that seem promising. Now, it's time to make them even better and select the best among them. Let's explore some ways you can do that. You can try adjusting the hyperparameters by hand, but it can be a lot of work and take up too much time. There are two practical ways do it; **Grid search** and **Random search**. 
In a simple way, you just have to let it know which settings you want it to test and the values to try. The Grid search will then explore all possible combinations of these settings, using cross-validation to assess their performance.
While the Randomized search checks various combinations by picking random values for different settings, and it does this a certain number of times during each trial.

For more details on regresion in ML refer to the second chapter from book [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/). You can also find the relevant codes on its [GitHub repository](https://github.com/ageron/handson-ml2).

## Types of Regression 

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



{{% summary %}} 

In this building block you learned the fundamentals of regression in python. after having a brief introduction on Regression, the steps that we need to take to do prediction 
   * reading data in python 
   * Exploring dataset by visualizing and get the summary of data, correlation level of predictors with the target variable 
   * Preprocessing the data including removing duplicates and get rid of missing values, handling categorical values, splitting data into train and test sets, and feature scaling   
   * Selecting and training a model 
   * explanation over performance measures 
   * a brief explanation on fine tuning the model

{{% /summary %}} 






