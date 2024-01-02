---
title: "Gradient Descent Variants"  
description: "Essentials of gradient descent as an optimization technique for regression and classification tasks."  
keywords: "optimization, cost function, loss function, squared error, learning rate, gradient descent, Mean Absolute Error, Smooth Mean Absolute Error, Huber loss, cross-entropy "  
date: 2023-12-30  
weight:   
author: "Kheiry Sohooli"  
authorlink: "www.linkedin.com/in/kheiry-sohooli"  
---
## Overview
 
[Gradient descent](https://tilburgsciencehub.com/building-blocks/analyze-data/machine-learning/Basics_of_optimization_in_Machine_Learning/) serves as a crucial optimization method for optimizing weights in cost functions during regression and classification tasks. Although it demonstrates remarkable speed in handling high-dimensional datasets, it is prone to overfitting. This building block delves into various variants of gradient descent, exploring their details. At the same time, it examine distinct loss functions to the different variants of gradient descent, helping a comprehensive understanding of the optimization process.

This building block provides some hints to select the optimization algorithm and loss function during training a machine learning algorithm on a dataset 


## Gradient Descent and Its Variations
In machine learning and deep learning problems, the [loss function](https://tilburgsciencehub.com/building-blocks/analyze-data/machine-learning/Basics_of_optimization_in_Machine_Learning/) is defined as the error between predictions and the actual values of the target variable. Gradient Descent (GD) is employed to solve the cost function and optimize the weights to minimize the error. 
Various variants of Gradient Descent exist, such as **batch gradient descent**, **stochastic gradient descent**. While the fundamental concepts remain consistent across these variants, the approach each algorithm adopts to solve the optimization problem differs.
The key hyperparameters in GD include the **learning rate**, **maximum number of iteration**, **learning rate decay with decay rate**. 

### Batch Gradient Descent
In gradient descent iterations in each step the parameters of cost function($\theta_i$) for single sample point are simultanously updated. But in Batch Gradient Descent (BGD), a single step involves considering the entire training dataset. The model parameters are updated by calculating the average of gradients from all training samples and using this mean gradient. This constitutes a single iteration of gradient descent within one epoch.
As it is may expected, this algorithm is slow on large datasets. BGD is suitable for convex problems like SEE cost function.  

### Stochastic Gradient Descent(SGD)
Named "stochastic" due to its approach, the algorithm randomly selects one training sample in each iteration to calculate the gradient. This means the algorithm employs either a single sample entry or a small set of training samples to compute the gradient, optimizing the weights. Consequently, the convergence speed of this algorithm surpasses that of Batch Gradient Descent (BGD), making it particularly suitable for nonconvex problems like the L1 loss function. However, since each iteration adjusts the weights using a randomly chosen sample, the cost fluctuates, and it may not consistently decrease. There is a possibility that the algorithm doesn't always reach the minimum but fluctuates around it. It is important to note that with a sufficient number of iterations, the overall trend of the cost tends to decrease.


Balancing speed and accuracy in optimization, Batch Gradient Descent (BGD) may be slower than Stochastic Gradient Descent (SGD), but it offers higher accuracy. Furthermore, BGD requires more computation and memory compared to SGD, as it considers all training samples at once. In the case of very large datasets, SGD is preferred over BGD, as BGD processes the entire dataset in every iteration. However, for implementing Stochastic GD, it is recommended to use a set of training data rather than a single instance.


### Mini Batch Gradient Descent
This algorithm presents a hybrid approach, blending aspects of both Batch Gradient Descent (BGD) and Stochastic Gradient Descent (SGD). Unlike SGD, which involves selecting a single sample, and GD, which considers the entire dataset, this variant of Gradient Descent operates on a fixed-length batch of training samples. By combining elements of the aforementioned algorithms, it leverages the advantages of both. In each iteration, a batch of samples is randomly chosen, and after computing the gradient on these samples, the average gradient is employed to update the weights of the cost function. It's worth noting that fluctuations may occur due to the use of a relatively small group of samples in each iteration.

{{% tip %}}
In the context of mini-batch gradient descent, we update our parameters frequently, and we also have the option to leverage a vectorized implementation for more efficient computations.
{{% /tip %}}


### Coordinate Descent

Coordinate descent provides an alternative approach to optimization, especially applicable for convex loss functions that lack differentiability, such as those encountered in Lasso regression. The method optimizes a single coordinate in each iteration by determining the minimum along that specific coordinate while keeping others constant. Following that, the process continues with another coordinate, often employing a selection rule like round robin. This technique highlights faster iterations and bypasses the necessity to manually choose a learning rate. However, it may exhibit slower convergence compared to gradient descent, and a notable limitation is its non-parallelizable nature, restricting its effectiveness in parallel computing settings.


## [Cost Function](https://tilburgsciencehub.com/building-blocks/analyze-data/machine-learning/Basics_of_optimization_in_Machine_Learning/)

The cost function is employed to assess the proximity of an estimated target value to the actual value during the training of a dataset in classification or regression algorithms. Following sections will introduce you to various loss functions applied in both regression and classification tasks, along with the appropriate Gradient Descent variants for each.

### Cost Functions in Regression Models 
Regression models employ various loss functions, with the quadratic loss function being the first among them. Several other loss functions in regression models are variations of this initial one. The second one is the mean absolute error, and there is also the smooth mean absolute error.


#### Mean Squared Error (MSE)
MSE, or Mean Squared Error, quantifies the squared difference between actual and predicted values. Also referred to as L2 loss, MSE is notably sensitive to outliers. In the presence of outliers within the dataset, the error tends to increase exponentially.

<div style="text-align: center;">
{{<katex>}}
J(\theta_1, \theta_0) = \left[ \frac{1}{2m} \sum_{i=1}^{m} (y(i) - h_\theta(x(i)))^2 \right]
{{</katex>}}
</div>  

for solving MSE , GD is used but it should be used cautiously, as it tends to easily overfit the data. Overfitting occurs when the model coefficients become excessively large, resulting in a steep incline or decline. This sensitivity to changes in input (x) can lead to a significant variation in output (y). Notably, Gradient Descent involves no hyperparameters that directly control model complexity, making it a versatile optimization technique.
Additionally, SGD can be used to solve MSE equation. however, for smoother variation of Minibatch SGD is preffered. 

To address overfitting in Mean Squared Error (MSE), one can introduce a penalty term into the loss function. There are two options available for mitigating overfitting in MSE: applying L2 regularization or L1 regularization.

When the L2 regularization term is added to the Mean Squared Error (MSE), the resulting model is referred to as Ridge regression. In Ridge regression, the model faces a penalty if the coefficients become large, and the regularization term acts to diminish the impact of coefficients, mitigating the risk of overfitting. The degree of regularization is governed by the $\lambda$ term, with an increase in $\lambda$ intensifying regularization; typically, the default value is set to 1. Ridge regression maintains convexity, enabling optimization through various methods such as closed-form solutions (Cholesky), gradient descent (including variants like Stochastic Average Gradient), and conjugate gradient.

<div style="text-align: center;">
{{<katex>}}
Min \sum_{i=1}^{n} \left(y_i - \sum_{j=1}^{p} x_{ij}\theta_j\right)^2 + \lambda \sum_{j=1}^{p} \theta_j^2
{{</katex>}}
</div>  

{{% tip %}}

As the regularization strength increases, the coefficients' ($\theta$) decrease, yet they never reach zero.

{{% /tip %}}

By adding L1 regularization penalty term  to the MSE, the equation is called lasso, short for Least Absolute Shrinkage and Selection Operator. Similar to the previous regurarization method, parameter $\lambda$ control the strength of regularization. But in this method many weights being precisely set to zero. Unlike Ridge regression, Lasso lacks a closed-form solution, and its optimization involves a convex, yet not strictly convex, and non-differentiable objective function. Coordinate descent is commonly used for optimizing weights. Notably, L1 regularization favors sparse models by encouraging coefficients to be exactly zero, facilitating automatic feature selection where some features are entirely ignored.

<div style="text-align: center;">
{{<katex>}}  
Min \sum_{i=1}^{n} \left(y_i - \sum_{j=1}^{p} x_{ij}\theta_j\right)^2 + \lambda \sum_{j=1}^{p} |\theta_j|
{{</katex>}}
</div>  


#### Mean Absolute Error(MAE)
This loss function also known as L1 loss. It gives the average of absolute errors of all data samples. In contrast to MSE that get the average of squared error, it takes the average of the absolute error. This characteristic makes it robust to the outliers. Therefore it is more suitable if your datasets contains outliers or noises. 

<div style="text-align: center;">
{{<katex>}}
MAE = \frac{1}{n}\sum_{i=1}^{n} |y_i - \hat{y}_i|
{{</katex>}}
</div>  

{{% tip %}}

Although MAE is less sentative to outliers compared to the MSE, some times MSE is preffered since MAE is not diffrentiable. 

{{% /tip %}}

#### Smooth Mean Absolute Error or Huber Loss
This cost function is the mixture of both previous cost functions. Hence, it is differentiable when the error is small by using the MSE part, and it uses MAE when the error is large. Therefore is less sensitive to the outliers and noise and differentiable close to the minima. There is a hyperparameter to tune it when use MSE or MAE.  

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


\begin{array}{ll}
\frac{1}{2} (y_i - \hat{y}_i)^2 & \text{for } |y_i - \hat{y}_i| \leq \delta \\\
\delta \cdot |y_i - \hat{y}_i| - \frac{1}{2} \delta^2 & \text{otherwise}
\end{array}


### [Cost Functions in Classsification Models](https://tilburgsciencehub.com/building-blocks/analyze-data/machine-learning/)
 Cost functions employed in classification differ from those in regression models, primarily due to the nature of the target variable. In regression models, the target variable is continuous, whereas in classification problems, it is discrete. The prevalent cost function in classification is the cross-entropy loss, which comes in two variations: Binary Cross-Entropy for binary classification and Categorical Cross-Entropy for multiclass classification. Another commonly used cost function in classification is Hinge loss.

#### Cost Function for Binary Classification Tasks
In machine learning problems where the target variable has two classes, Binary Cross-Entropy is used. This loss function is alternatively referred to as log loss, logistic loss, and maximum likelihood. Additionally, L1/L2 regularization terms can be incorporated into this loss function. 

<div style="text-align: center;">
{{<katex>}}
J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(h_\theta(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_\theta(x^{(i)})) \right]
{{</katex>}}
</div>


Diverse optimization techniques, are available for the minimization of cross-entropy loss. The foundational approach of gradient descent, constrained to L2 regularization. The differentiability of log loss, permitting its application in stochastic gradient descent and related variants like Stochastic Average Gradient (SAG, SAGA). Coordinate descent, supports both L1 and L2 regularization, facilitates faster iterations but may show slower convergence and encounter challenges associated with saddle points. Newton-Rhapson or Newton Conjugate Gradient, exclusively designed for L2 regularization, employs the Hessian matrix but may be slow with big datasets. While effective in convex solution spaces, it may encounter difficulties in non-convex scenarios. Quasi-Newton methods like Limited-memory Broyden–Fletcher–Goldfarb–Shanno (lbfgs), suitable for L2 regularization, provide approximate yet computationally efficient solutions and serve as the default option in scikit-learn for Logistic Regression. 

{{% tip %}}

Data scaling helps convergence and minimizes difference between solvers, contributing to more stable optimization processes.

{{% /tip %}}


#### Cost Function for Multiclassification models

In a classification problem with multiple classes as the target variable, it is necessary to use categorical cross-entropy as the loss function.

<div style="text-align: center;">
{{<katex>}}
\text{Categorical Cross-Entropy} = -\frac{1}{n}\sum_{i=1}^{n}\sum_{j=1}^{m}y_{ij} \cdot \log(\hat{y}_{ij})
{{</katex>}}
</div>  

Another alternative is hinge loss, also referred to as Multi-class SVM Loss. This particular cost function is designed to maximize the marginal distance and is commonly employed for optimizing Support Vector Machine (SVM) models.

<div style="text-align: center;">
{{<katex>}}
\text{Hinge Loss} = \max(0, 1 - y_i \cdot \hat{y}_i)
{{</katex>}}
</div>  

The Hing loss equals zero when $x_i$ is positioned correctly with respect to the margin(it means when the prediction is correct). However, for data located on the incorrect side of the margin, the function's value is directly proportional to the distance from the margin.

By adding a regularization term to the equation, the parameter $\lambda > 0$ plays a crucial role in achieving a balance between enlarging the margin size and ensuring that $\max(0, 1 - y_i \cdot \hat{y}_i)$ is satisfied, guaranteeing that $x_i$ lies on the correct side of the margin.

<div style="text-align: center;">
{{<katex>}}
\text{SVM Cost Function} = \frac{1}{n} \sum_{i=1}^{n} \left[ \max(0, 1 - y_i \cdot \hat{y}_i) + \lambda \lVert \mathbf{w} \rVert^2 \right]
{{</katex>}}
</div> 


## Summary

* Gradient Desent Variants: in this Building Block, we first explore the variations of gradient descent (GD). 
    * Batch Gradient Descent
    * Stochastic Gradient Descent(SGD)
    * Mini Batch Gradient Descent
    * Coordinate Descent
* Cost Functions: Following the discussion on Gradient Descent (GD), different cost functions for regression and classification models are explained, along with the suitable Gradient Descent methods for optimizing them.
    * Cost Functions in Regression Models
        * Mean Squared Error (MSE)
        * Mean Absolute Error(MAE)
        * Smooth Mean Absolute Error or Huber Loss
    * Cost Functions in Classsification Models
        * Binary Cross-Entropy
        * Categorical Cross-Entropy
        * Hinge Loss



#### Additional Resources for In-Depth Study:
1- https://www.geeksforgeeks.org/gradient-descent-algorithm-and-its-variants/

2- https://ml-course.github.io/master/notebooks/02%20-%20Linear%20Models.html