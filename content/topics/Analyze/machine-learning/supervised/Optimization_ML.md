---
title: "Optimization in Machine Learning"  
description: "Essentials of gradient descent as an optimization technique for regression and classification tasks."  
keywords: "optimization, cost function, Machine learning,learning rate, gradient descent"  
date:  
weight: 6 
author: "Kheiry Sohooli"  
authorlink: "https://tilburgsciencehub.com/contributors/kheirysohooli"  
---

## Overview
 
When training a machine learning model, we use an optimization approach to minimize a cost function. Gradient descent serves as a crucial optimization method for optimizing weights in cost functions during regression and classification tasks. This article aims to provide insights into selecting the best optimization algorithm and pairing it with the appropriate loss function when training a machine learning model.

It is highly recommended to review the `Cost and Loss Functions` article before reading this article.

## Optimization 
In the context of machine learning and mathematics, optimization involves finding the best possible solution or configuration for a given problem. This often includes minimizing or maximizing an objective function by adjusting the parameters or variables of a model or system. Feel free to explore more by reading [this paper](https://coral.ise.lehigh.edu/frankecurtis/files/papers/BottCurtNoce18.pdf). In mathematics, various optimization algorithms exist. One of the most common methods, particularly in machine learning, is known as `Gradient Descent`(GD).

## Gradient descent algorithm in simple language

Let's consider Equation 1 as our objective function we want to optimize to match a dataset comprising a single predictor (denoted as $x(i)$) and its corresponding target ($y(i)$). We want to determine the parameters that minimize the difference between the estimated values obtained from this function ($h_\theta(x)$) and the actual target values ($y(i)$). This optimization process involves minimizing the cost function, denoted as $J(\theta_0, \theta_1)$ in Equation 2, through the use of gradient descent.

The GD algorithm begins by initializing $\theta_0$  and $\theta_1$ with random values. Subsequently, it iteratively takes small steps, adjusting these parameters until $J(\theta_0, \theta_1)$ converges to a minimum, which might be a local or global minimum. For a more comprehensive understanding, refer to the visual representation below.

<div style="text-align: center;">
{{<katex>}}
h_\theta(x) = \theta_1x + \theta_0                  
{{</katex>}}
 :Equation1
</div>
-
<div style="text-align: center;">
{{<katex>}}
J(\theta_1, \theta_0) = \left[ \frac{1}{2m} \sum_{i=1}^{m} (y(i) - h_\theta(x(i)))^2 \right]
{{</katex>}}
    :Equation 2
</div>  
-
<div align="center">
  <img src="../images/gradientDecent.png" width="400">
</div>
-

The main part of GD algorithm is iteration of the following steps until convergence is achieved:
<div style="text-align: center;">
{{<katex>}}

\theta_j := \theta_j - \alpha \frac{\sigma J(\theta_0, \theta_1)}{\sigma \theta_j}
\\{for}\ j=0\ \text{and}\ j=1
{{</katex>}}
</div>

In each iteration, the partial derivative of the cost function $J$ with respect to $\theta$ is computed. This derivative is then scaled by the learning rate ($\alpha$) and subtracted from the current $\theta$. This process is repeated until $\theta$ shows negligible changes or until a predefined number of iterations is reached. This iterative approach allows the parameters $\theta$ to gradually adjust, guiding the model toward convergence.


When optimizing your machine learning algorithm, it's crucial to consider the learning rate, denoted here as $\alpha$. This hyperparameter determines the size of the steps taken during optimization. A larger $\alpha$ corresponds to more significant parameter changes in each step, while a smaller $\alpha$ results in more gradual adjustments. It's essential to fine-tune $\alpha$ based on the specific characteristics of your problem. For example, an excessively large $\alpha$ may lead to overshooting, hindering convergence to the minimum. Conversely, an excessively small $\alpha$ may slow down progress. 

<div align="center">
  <img src="../images/Alpha_effect.png" width="400">
</div>

{{% tip %}}
The key hyperparameters in GD are learning rate, maximum number of iteration, and learning rate decay with decay rate. 
{{% /tip %}}
## Gradient Descent Variants
Various variants of Gradient Descent exist, such as `batch gradient descent`, `stochastic gradient descent`. While the fundamental concepts remain consistent across these variants, the approach each algorithm adopts to solve the optimization problem differs.


### Batch Gradient Descent (BGD)
In gradient descent, during each iteration, the parameters of the cost function ($\theta_i$) are updated simultaneously for a single sample point. However, in BGD, a single step involves considering the entire training dataset. The model parameters are updated by calculating the average of gradients from all training samples, using this mean gradient for updating. This involves a single iteration of gradient descent within one epoch.

#### Advantages:
- BGD is particularly suitable for convex problems, such as the Sum of Squared Errors (SEE) cost function.
- It offers high accuracy

#### Disadvantages: 
- As expected, this algorithm tends to be slow on large datasets. 
- It requires more computation and memory, as it considers all training samples at once. 

### Stochastic Gradient Descent(SGD)
Named "stochastic" due to its approach, the algorithm randomly selects one training sample in each iteration to calculate the gradient. This means the algorithm employs either a single sample entry or a small set of training samples to compute the gradient, optimizing the weights. However, since each iteration adjusts the weights using a randomly chosen sample, the cost fluctuates, and it may not consistently decrease.

#### Advantages: 
- The convergence speed of this algorithm surpasses that of BGD, making it particularly suitable for nonconvex problems like the L1 loss function.
- In the case of very large datasets, SGD is preferred over BGD, as BGD processes the entire dataset in every iteration. However, for implementing SGD, it is recommended to use a set of training data rather than a single instance.

#### Disadvantages:
- There is a possibility that the algorithm doesn't always reach the minimum but fluctuates around it. It is important to note that with a sufficient number of iterations, the overall trend of the cost tends to decrease.

### Mini Batch Gradient Descen(MGD)
This algorithm presents a hybrid approach, blending aspects of both BGD and SGD. Unlike SGD, which involves selecting a single sample, and BGD, which considers the entire dataset, this variant of Gradient Descent operates on a fixed-length batch of training samples. By combining elements of the aforementioned algorithms, it leverages the advantages of both. In each iteration, a batch of samples is randomly chosen, and after computing the gradient on these samples, the average gradient is employed to update the weights of the cost function. It's worth noting that fluctuations may occur due to the use of a relatively small group of samples in each iteration.

#### Advantages:
- One key benefit of MBD compared to SGD is the potential performance enhancement achieved through hardware optimization of matrix operations.
- This algorithm is favored for optimization in deep learning due to its ability to balance speed and stability effectively.

#### Disadvantages: 
- Convergence of an error cannot be assured with certainty.
- Manually regulate the learning rate when employing MGD. If the learning rate is set too low, the convergence rate may decrease. Conversely, if the learning rate is too high, it may lead to failure in getting an absolute global or local minimum. Thus, careful control of the learning rate is essential in MGD.

The image below shows the distinctions among three variants of Gradient Descent.
<div align="center">
  <img src="../images/GD_variants.png" width="400">
  <p><a href="https://sweta-nit.medium.com/batch-mini-batch-and-stochastic-gradient-descent-e9bc4cacd461">Source</a></p>
</div>


## Coordinate Descent(CD)

CD optimizes one variable at a time while cycling through the entire set of variables repeatedly. The method optimizes a single coordinate in each iteration by determining the minimum along that specific coordinate while keeping others constant. Following that, the process continues with another coordinate, often employing a selection rule like round robin.

<div align="center">
  <img src="../images/CoordinateDescent.png" width="400">
</div>
-

#### Advantages:
- It is applicable for convex loss functions that lack differentiability, such as those encountered in Lasso regression.
- This technique highlights faster iterations and bypasses the necessity to manually choose a learning rate

#### Disadvantages:
- It may exhibit slower convergence compared to gradient descent.
- A notable limitation is its non-parallelizable nature, restricting its effectiveness in parallel computing settings.

{{% summary %}}
- Quick overview of Optimization
- Simplified explanation of the gradient descent algorithm
- Introduction to various gradient descent variants
- Discussion on the advantages and disadvantages of each variant
- Selection of the appropriate cost function corresponding to each gradient descent variant
- Introduction of coordinate descent as an optimization algorithm
{{% /summary %}}
