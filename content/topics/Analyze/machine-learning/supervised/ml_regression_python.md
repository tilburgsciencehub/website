---
title: "Linear Regression for Prediction in Python"
description: "An introduction to linear regression based prediction in Python"
keywords: "regression, machine learning, ML, Linear, Regression, Python"
draft: false
weight: 10
author: "Kheiry Sohooli"
authorlink: "https://tilburgsciencehub.com/contributors/kheirysohooli/" 
---

## Overview
This article introduces how to use linear regression to predict a continuous outcome variable and the steps to implement it in Python. 

Regression is a technique used in supervised machine learning when the goal is to predict a **continuous dependent variable** (target) based on one or more independent variables (predictors). Think of it as trying to fit a line (or a curve in some cases) through data points to establish a relationship between the independent and dependent variables. By understanding this relationship, we can make predictions about the target variable for new data points.

For instance, consider the example of predicting a house's price (dependent variable) based on several predictors like its size in square feet (independent variable). Using regression, we can fit a line through the historical data of houses sold and their properties. Once this line is established, if we have a new house of a specific characteristics, we can predict its approximate price by looking at where it falls on the line.

There are several regression techniques, such as linear regression, Lasso, and Ridge, each designed to handle specific data characteristics and relationships between variables. 

For this tutorial the [dataset]( https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market) on housing prices from kaggle will be used. 

## Machine learning Linear Regression Pipeline 
### Get the Data
To import CSV data into Pandas, use the read_csv function, accepting file paths or URLs. This method offers customization options via various parameters. Explore reading data from Kaggle click [here](https://ravi-chan.medium.com/how-to-download-any-data-set-from-kaggle-7e2adc152d7f) .

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


### Take a Quick Look at the Data
The `head()` method shows you the first 5 rows of your data along with the column names. When you use it, you can see what features are in your dataset and get a quick overview of the values in each column. It's a handy way to get a glimpse of your data.

{{% codeblock %}}

```Python
# get the first 5 rows
df.head()
```
{{% /codeblock %}}


Additionally, the `info()` functions shows useful information about the total number of samples(rows), and type of each feature(float64, object, etc.) and number of non-null values in each column.

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

### Preprocessing the Data for Machine Learning Algorithms

#### Data Cleaning

Cleaning data involves different steps, and what you do depends on the dataset.
1. **Removing Duplicates:**  Easily eliminate repetitive samples for cleaner data.

{{% codeblock %}}

```Python
# check for duplicates
print("number of duplicated rows:" , sum(df.duplicated()))

# drop duplicate rows
df = df.drop_duplicates()
```
{{% /codeblock %}}

2. **Handling Missing Data:** For this particular case, we choose to drop the rows with missing values.

{{% codeblock %}}

```Python
# drop the samples without price
df.dropna(subset=["Price"], inplace= True)

# or you can drop all NA by following codes 
df.dropna( inplace= True)
```
{{% /codeblock %}}

#### Handling Categorical Attributes
Use `LabelEncoder` from scikit-learn to transform categorical values into numerical ones.

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


#### Splitting data into train and test sets
Before you start training your model on the data, set aside a part of it to test and evaluate the model afterwards. This process is known as train-test-split. The easiest way to do this is by using the `train_test_split()` function from the `sklearn` library.

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

In the code above, pay attention to the "test_size" parameter. It decides how much of the dataset is kept for testing. In our case, we've reserved 25% of the dataset for testing. 
Also, we set a random seed to make sure the split dataset doesn't change every time we run the code.

#### Feature Scaling
This transformation is important when variables have different ranges. For instance, if you compare "rooms" (ranging from 1 to 7) with "yearbuilt" (ranging from 1196 to 2106), you'll notice a big difference. Many machine learning algorithms don't work well when features are in different scales.

{{% tip %}}

Note that scaling the target variable is not necessary.

{{% /tip %}}


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

Note that you can train your data using any other regressors but here we just work with one. Feel free to explore other regressors and compare the results. 

### Evaluate the model 

The most common evaluation metrics for regressions are R-squared (R2), Mean squared error(MSE), and Mean absolute error (MEA).

{{% codeblock %}}

```Python
from sklearn import metrics

print("mean_absolute_error:", metrics.mean_absolute_error(y_test, predictions))
print("mean_squared_error", metrics.mean_squared_error(y_test, predictions))
import numpy as np
print("root_squared error", np.sqrt(metrics.mean_squared_error(y_test, predictions)))
```
{{% /codeblock %}}

<!---
### Fine-Tune Your Model

Imagine you have a list of models that seem promising. Now, it's time to make them even better and select the best among them. Let's explore some ways you can do that. You can try adjusting the hyperparameters by hand, but it can be a lot of work and take up too much time. There are two practical ways do it; **Grid search** and **Random search**. 
In a simple way, you just have to let it know which settings you want it to test and the values to try. The Grid search will then explore all possible combinations of these settings, using cross-validation to assess their performance.
While the Randomized search checks various combinations by picking random values for different settings, and it does this a certain number of times during each trial.

For more details on regresion in ML refer to the second chapter from book [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/). You can also find the relevant codes on its [GitHub repository](https://github.com/ageron/handson-ml2).
--->


{{% summary %}} 

In this article, you have explored the fundamentals of regression in Python. After an introduction to regression, we've outlined the essential steps for prediction:

- **Reading Data in Python**: Understanding how to import and access data within Python.

- **Exploring Dataset**: Describing the data via summary statistics to understand its structure.

- **Data Preprocessing**: Tasks include handling duplicates, addressing missing values, managing categorical variables, splitting data into training and testing sets, and feature scaling.

- **Selecting and Training a Model**: Choosing an appropriate regression model and training it using the prepared data.

- **Evaluating the Model**: Assessing the performance of the trained model using suitable evaluation metrics.

{{% /summary %}} 
