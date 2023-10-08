---
title: "Supervised machine learning"
description: "An introduction to Supervised Machine learning"
keywords: "machine learning, ML, supervised, training, testing"
draft: false
weight: 1
author: "Niels Rahder"
authorlink: "https://www.linkedin.com/in/nielsrahder" 
---
  ## What is supervised machine learning? 

Supervised learning is the process of learning with "training labels". These labels, also referred to as `targets`, act as the guiding hand for the algorithm, steering it towards understanding the underlying relationships in the data. Through a process of learning, the algorithm refines its parameters to make more accurate predictions or classifications based on the input variables or `features`. The strength of supervised learning lies in its ability to map this input data (features) to the desired output (targets), allowing it to make informed decisions about new, unseen data. Based on the nature of the target variable supervised machine learning can be classified into two broad categories:

  - Classification 
In classification problems the `target` variable are categories. The main goal in classification problems is to categorize an data entry into the correct category (e.g., predicting if someone is going to default on their loan). 
  - Regression
In regression problems the `target` variable is continuous, and the main goal is to predict the numerical value (e.g., predicting home prices based on multiple features).

  ## training and testing data

In order to train a model you divide your data set up in two parts: a training part (usually 80% of the data), and a testing part (the remaining 20%.) This division allows us to evaluate the model and prevent overfitting. Overfitting occurs when a model is too complex and captures noise in the training data, making it perform poorly on new, unseen data. It essentially 'memorizes' the training data rather than 'learning' from it. 

  - Training data. 
This part of the data is used to train (or teach) the model. Essentially, the algorithm tries to learn the underling patters from the data. For example, if we are trying to predict the probability that a lender defaults on his/her loan, the training data will provide the model with features of lenders (e.g., age, education, income)

  - Testing data 
When the model has been trained, it is evaluated on its performance on data it has never seen before. This is done by using the testing data. By using this data, it is possible to asses the model and see if it is over fitting. 

To illustrate this concept further, let's consider the example of loan defaults. In the following table we have a small data set of six lenders with their respective features, and our interest variable if they defaulted on a loan. Suppose we use four of these entries as training data (Alice, Bob, Carol and Dave). The model will then attempt to learn patterns between the features of Age, Annual Income, level of education, job stability and whether they defaulted on their loan. 

After training the data, we use the remaining two entries (Eve and Frank) as our testing data. 


| Name  | Age | Annual Income ($) | Education Level | Job Stability (Years) | Defaulted on Loan (Y/N) |
|-------|-----|-------------------|-----------------|-----------------------|--------------------------|
| Alice | 28  | 40,000            | Bachelor's     | 3                     | N                        |
| Bob   | 35  | 75,000            | Master's       | 5                     | N                        |
| Carol | 45  | 50,000            | High School    | 20                    | Y                        |
| Dave  | 30  | 65,000            | Associate's    | 2                     | Y                        |
| Eve   | 40  | 90,000            | PhD            | 10                    | N                        |
| Frank | 55  | 30,000            | None           | 1                     | Y                        |
