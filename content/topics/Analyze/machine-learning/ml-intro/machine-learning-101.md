---
title: "Machine Learning 101"
description: "nog invullen"
keywords: "machine learning, R, Python"
date: 26/02/2024
weight: #1
author: "Lisa Holling"
authorlink: "https://tilburgsciencehub.com/contributors/lisaholling/"
aliases:
  - /machinelearning
  - /supervised
  - /unsupervised
  - /reinforcement

---

## Overview
Are you intrigued by the concept of machine learning but find yourself daunted by complex theories and techniques?  No need to worry - this article has got you covered. It explains the basics of machine learning and provides a practical guide to set up your own machine modeling project. 

The article covers several topics, from basic theories to code blocks to get you started on your own project: 
1. What is Machine Learning?
2. Types of Machine Learning
4. Machine Learning Algorithm examples 
5. Tips and guidelines for setting up your machine learning project



## What is Machine Learning? 
Machine learning is a type of artificial intelligence that allows systems to learn and improve automatically from experience. Instead of relying on explicit programming, these systems use data to recognize patterns, make decisions, and improve their performance over time. 

Typically, the objective of machine learning is to develop algorithms that are capable of learning how to perform a task based on input data. For instance, a model can be trained on a specific data set to generate an output variable based on that input data. This classical approach is often used to forecast outcomes, such as customer churn or predicting sales.

[visualization]


## Types of Machine Learning
There are several types of machine learning, each suitable for different types and sizes of data, as well as goals. 
Classical machine learning (including supervised and unsupervised learning) splits data into a training and test set. They observe patterns on existing data and apply them to new data in the form of predictions.

With supervised learning, the model uses information from the training set to predict a given outcome variable. 

On the other hand, if you want to identify patterns and relationships in your data, without a given outcome variable, unsupervised learning is the right approach. 

It can also be the case that you don't have a specific data set as input. Then, you can use reinforcement learning, which interacts with an environment.


### 1. **Supervised Learning**

Supervised learning is a type of machine learning where the algorithm is trained on a labeled dataset, which means that the input data and corresponding output are provided. The model learns to map the input to the correct output, making predictions on unseen data. 

Two different approaches are classification and regression. 
Classification deals with predicting categorical outcomes, such as labeling the sentiment of course feedback from students as positive or negative. 
Regression deals with predicting continuous outcomes, such as the sales from a newly launched product.

Common supervised learning techniques include linear regression, decision trees, and random forests.

### 2. **Unsupervised Learning** 

Unsupervised learning, on the other hand, deals with unlabeled data. The algorithm explores the inherent structure within the data, identifying patterns and relationships without explicit guidance or output. Unsupervised learning is often used to group and cluster different objects based on various attributes, such as segmentating customers based on demographics and purchase history.

Different approaches are clustering, generalization and association. Clustering is used for grouping similar instances, generalization for finding general patterns, and association for discovering rules that describe large portions of the data. 

Common techniques include K-means clustering, Principal Component Analysis, and apriori algorithm.

### 3. **Reinforcement Learning**

Reinforcement learning involves training a model to make decisions by interacting with its environment. The algorithm receives feedback in the form of rewards or penalties, refining its actions to achieve a specific goal. It is a behavioral modeling technique where the model learns through a trial and error mechanism as it keeps interacting with the environment.
Types of reinforcement learning include model-based and model-free reinforcement learning, where the former anticipates the outcomes of actions, and the latter learns policies directly from trial and error. Common techniques include Q-learning and policy gradients.

If you'd like to learn more about each of these machine learning types, you can check out their corresponding articles, which cover more in-depth theory and examples:
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

##

## Machine Learning Algorithm examples 

linear regression
logistic regression
decision trees
random forests
k-means clustering
support vector machines


References:
https://vas3k.com/blog/machine_learning/?ref=hn
https://www.linkedin.com/pulse/machine-learning-101-understanding-fundamentals-ai-technology-batra/
https://medium.com/onfido-tech/machine-learning-101-be2e0a86c96a
https://www.datacamp.com/blog/top-machine-learning-use-cases-and-algorithms