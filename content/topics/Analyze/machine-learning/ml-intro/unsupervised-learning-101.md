---
title: "In-depth Introduction to Unsupervised Machine Learning"
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
3. A Clustering Example
4. An Association Example
5. A Dimensionality Reduction Example

## What is Unsupervised Learning?

This type of machine learning learns from data without human supervision. These models can detect previously unknown patterns in datasets without specified labels or outcomes. It uses self-learning algorithms to structure information based on similarities, differences, and patterns in data. Unsupervised learning approaches are often used to find structure in large datasets, and create a more compact representation of the data that is easier to understand.

Different approaches are clustering, association, and dimensionality reduction: 
* Clustering 
* Association 
* Dimensionality Reduction

**Clustering**

Clustering organizes data by grouping similar data points together. Because members of the same group tend to have similar characteristics, clustering algorithms can group unlabeled data based on their similarities and differences. The goal is to have data points in the same cluster to be similar to each other. It is widely used in market research, customer segmentation, fraud detection, and image analysis. For example, on LinkedIn, clustering can be used to discover professional communities based on shared interests, job roles, or industry sectors, such as "technology innovators" or "digitial marketing professionals". 

**Association**

Association rule mining is used to uncover patterns and relationships in the data, by finding rules that represent large parts of the data. It discovers correlations, connections, and co-occurences, and is often used to track purchases or make recommendations to customers. For example, Netflix uses association algorithms to discover that people who watch certain genres like science fiction often also enjoy fantasy series, and they can recommend new shows based on viewing habits.

{{% tip %}}
In association rule mining, two important metrics to evaluate the strength and relevance of discovered rules are confidence and lift. Confidence measures how often items in a rule appear together, indicating the strength of the association. Lift compares this frequence of co-occurence to individual occurrences.
{{% /tip %}}

**Dimensionality Reduction**

Dimensionality reduction techniques are used to reduce the number of input variables in a dataset. It removes irrelevant or random features while maintaining as much of the important information of the original data as possible. This can help increasing the efficiency of future analyses, reduce computational costs, and help with the visualization and interpretability of the data. In other words, it is a process of transforming high-dimensional data into a lower-dimensional dataset that still captures the essence of the original data. Dimensionality reduction algorithms are usually used as a pre-processing step in modeling, before the actual model training. 

{{% warning %}}
Reducing dimensionality may lead to the loss of important information, which could have a negative impact on how well later algorithms perform. Critically ask yourself why you want to decrease the size and dimensionality of your data.
{{% /warning %}}

<!-- ### Key Concepts -->

## Unsupervised Learning Algorithms
<!-- clustering -->
### Clustering
- K-Means Clustering
  - This algorithm segments data into groups based on similarity and common attributes. The dataset is divided into K clusters by minimizing the distance between each data point and the cluster centroid. An example is segmenting customers into distinct groups based on their purchasing behavior.
  
- Hierarchical Clustering
  - Hierarchical clustering does not require the number of clusters to be specified in advance. It builds a hierarchy either by starting with all data points as one group and splitting them (divisive method), or by starting each data point as its own group and combining them (agglomerative method). 

- Anomaly Detection
  - This method finds data points that differ significantly from the rest of the data. In fields like fraud detection, anomaly detection helps in spotting unusual transactions that could be fraud.

<!-- association -->
### Association
- Apriori Algorithm
  - This association rule algorithm is great for discovering relationships between variables in large databases. It can find frequent itemsets in transactional data, such as identifying products that frequently get bought together. 


- Eclat Algorithm
  - Eclat locates frequently occurring itemsets in transactional databases by performing a depth-first search. It speeds up the process and reduces computational costs by using a vertical data forma that lists each item along with its transaction ID.

### Dimensionality Reduction
<!-- Dimensionality -->
<!-- https://www.geeksforgeeks.org/dimensionality-reduction/ -->
- Principal Component Analysis (PCA)
  - PCA reduces the dimensionality of data by transforming the original variables into a new set of variables, which are linear combinations of the original variables. It simplifies data without losing its core information, and is useful in visualizing high-dimensional data.

- Linear Discriminant Analysis (LDA)
  - LDA separates multiple classes with multiple features. It identifies a linear combination of features that separates two or more classes. It does this by projecting data with two or more dimensions into one dimension, so that it can be more easily classified. It is often used as a pre-processing step of classification algorithms like decision trees. 

## A Clustering Example: K-Means Clustering

In this example of clustering in unsupervised learning we will use the `iris` dataset. This dataset consists of measurements of iris flowers from three different species. Here is how you can apply K-means clustering to this dataset in R.

### Loading and Preparing the Data
First, we load and prepare the data by removing labels since K-means is an unsupervised technique. 

{{% codeblock %}}
```R
library(tidyverse)

# Load the iris dataset
data("iris")
df <- iris # we call the dataframe `df`

# Inspect the data
summary(df)

# Remove the `Species` column to make the data unlabeled
df_unlabeled <- df %>% 
  select(-Species)

# Scale the data
df_scaled <- scale(df_unlabeled)
```
{{% /codeblock %}}

{{% warning %}}
It is important to scale the data, because this method uses the Euclidean distance to form clusters. If different features have different units or scales, one feature might disproportionately influence the distance measure if not scaled. For example, if petal length has a larger range than sepal width, this feature might dominate the distance calculations.
{{% /warning %}}

### Determine the Number of Clusters
Next, we use the Elbow Method to determine the optimal number of clusters:

{{% codeblock %}}
```R
# install.packages("factoextra") # Remove comment if uninstalled
library(factoextra)

fviz_nbclust(df_scaled, kmeans, method = "wss")
```
{{% /codeblock %}}

{{% tip %}}
The Elbow Method is used to choose the optimal number of clusters. It plots the sum of squared distances of samples to their nearest cluster center across different values of K. Look for the point where the line sharply changes — this point, that looks like an "elbow", typically shows the most suitable number of clusters.
{{% /tip %}}

<p align = "center">
<img src = "/images/k-means-elbow-plot.png" width="700">
</p>

In the image, we can see that the elbow is at `k=3`.

### Running K-Means Clustering

We can now procees with the clustering. We choose our number of clusters with `centers = 3`. 
Once we ran the algorithm, we need to check how well the model did by putting back the labels from the removed `Species` column. We can then visualize the clustering results. 

{{% codeblock %}}
```R
# Run K-means clustering
km.out <- kmeans(df_scaled, centers = 3, nstart = 100)
print(km.out)

# Add row names to identify the original labels
rownames(df_scaled) <- paste(df$Species, 1:dim(iris)[1], sep = "_")

# Visualize the clustering results
fviz_cluster(list(data = df_scaled, cluster = km.out$cluster))
```
{{% /codeblock %}}

The plot visually shows us how well the model did. The colours show to clusters that the algorithm made. The labels (in text) show the actual labels. We can see that most flowers are correctly labeled, but some are not.

<p align = "center">
<img src = "/images/k-means-cluster-plot.png" width="700">
</p>

### Analyzing the Results
Finally, we compare the clusters with the original labels to see how well our clustering matched the actual species distribution:

{{% codeblock %}}
```R
# Compare the clusters with the original labels
table(km.out$cluster, df$Species)
```
{{% /codeblock %}}

| Cluster | Setosa | Versicolor | Virginica |
|---------|--------|------------|-----------|
| 1       | 50     | 0          | 0         |
| 2       | 0      | 48         | 14        |
| 3       | 0      | 2          | 36        |

The results show that:
- Cluster 1 exclusively contains all 50 Setosa samples.
- Cluster 2 primarily contains Versicolor, with 48 out of 50, but also includes 14 Virginica.
- Cluster 3 mostly contains Virginica, with 36 out of 50, but includes 2 Versicolor.


## An Association Example

<!-- 
Media platforms use clustering to categorize articles on the same topics 
Defining customer personas
Recommendation engines; discover data trends to develop more effective cross-selling strategies
-->

<!-- https://medium.com/data-science-vibes/association-rule-part-1-f37e3cc545a0 on Association algorithms and Netflix/Supermarket example-->