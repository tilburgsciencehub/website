---
title: "In-depth Introduction to Supervised Machine Learning"
description: "Get introduced to Unsupervised Learning, a core branch of machine learning where the model learns \\\ to make predictions or decisions. This article explores unsupervised learning, its algorithms, and walks you through a simple example in R."
keywords: "machine learning, unsupervised learning, algorithms, regression, classification, R"
date: 05/04/2024
weight: #1
author: "Lisa Holling"
authorlink: "https://tilburgsciencehub.com/contributors/lisaholling/"
aliases:
  - /unsupervised

---

## Overview
This article is a follow-up to [Get Introduced to Machine Learning](/introduction), which covered the basics of different machine learning types. In this article, we will dive deeper into one of the types of machine learning: Unsupervised Learning.

This in-depth introduction to unsupervised learning will cover its key concepts, algorithms and provide hands-on examples in R to illustrate how you can use these concepts in practice. Whether you are new to this topic, only have basic coding skills or just curious about unsupervised learning - this article will equip you with the tools to start your first unsupervised learning model.

The article covers several topics:
1. What is Unsupervised Learning?
2. Unsupervised Learning Algorithms
3. A Regression Example
4. A Classification Example

## What is Unsupervised Learning?

This type of machine learning learns from data without human supervision. These models can detect patterns in data without specified labels or outcomes. It uses self-learning algorithms to structure information based on similarities, differences, and patterns in data. Unsupervised learning approaches are often used to find structure in large datasets, and create a more compact representation of data.

Different approaches are clustering, generalization and association: 
* Clustering 
* Association 
* Dimensionality Reduction

**Clustering**
Clustering involves grouping similar data points together. Because members of the same group tend to have similar characteristics, clustering algorithms can group unlabeled data based on their similarities and differences. The goal is to have data points in the same cluster to be similar to each other. It is widely used in market research, customer segmentation, fraud detection, and image analysis.

**Association**
Association rule mining can be used to identify patterns and discover relationships between features in the dataset. It finds rules that represent large parts of the data, to discover correlations, connections, and co-occurences within the data. It is often used to track purchases that are frequently bought together.

**Dimensionality Reduction**
Dimensionality reduction techniques are used to reduce the number of input variables in a dataset. It reduces the number of irrelevant or random features while maintaining as much of the important information of the original data as possible. This can help to increase the efficiency of future analyses, reduce computational costs, and help with the visualization and interpretability of the data. In other words, it is a process of transforming high-dimensional data into a lower-dimensional space that still preserves the essence of the original data. Dimensionality reduction algorithms are usually used as a pre-processing step in modeling, before the actual model training. 

### Key Concepts

## Unsupervised Learning Algorithms
<!-- clustering -->
- K-Means Clustering
  - This algorithm segments data into clusters based on similarity, a common approach for market segmentation by grouping customers according to purchasing habits.

- Hierarchical Clustering

- Anomaly Detection

<!-- association -->
- Apriori Algorithm
  - This association rule algorithm is great for discovering relationships between variables in large databases. It identifies frequent individual items in the database and larger item sets that often appear together, such as identifying products that frequently get bought together. 

- Eclat Algorithm

- Frequent Pattern Growth (FP-Growth)

<!-- Dimensionality -->
<!-- https://www.geeksforgeeks.org/dimensionality-reduction/ -->
- Principal Component Analysis (PCA)
  - PCA is a technique for dimensionality reduction, helping to simplify data without losing its core information, useful in visualizing high-dimensional data.

- Linear Discriminant Analysis (LDA)

- Generalized Discriminant Analysis (GDA)

## A Clustering Example: K-Means Clustering

In this example of clustering in unsupervised learning we will use the `iris` dataset. This dataset consists of measurements for iris flowers from three different species. We will train a model that can 


## An Association Example

<!-- 
Media platforms use clustering to categorize articles on the same topics 
Defining customer personas
Recommendation engines; discover data trends to develop more effective cross-selling strategies
-->