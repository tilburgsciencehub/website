---
title: "Basics of optimization in Machine Learning"  
description: "Essentials of gradient descent as an optimization technique for regression and classification tasks."  
keywords: "optimization, cost function, loss function, Machine learning, squared error, regression, classification, learning rate, gradient descent"  
date: 2023-11-13  
weight: 1  
author: "Kheiry Sohooli"  
authorlink: "www.linkedin.com/in/kheiry-sohooli"  
---
## Overview

When training a machine learning model, our goal is to predict values as accurately as possible. We use an optimization approach to reduce a loss function, aiming for the most precise predictions. Models learn and improve by minimizing the error measured in a loss function, which gauges the gap between actual and predicted values. In this building block, you'll learn how to optimize parameters in objective function for both classification and regression models using Gradient descent.


## Optimization 
Optimization refers to the process of making something as effective or functional as possible. In the context of machine learning and mathematics, optimization involves finding the best possible solution or configuration for a given problem. This often includes minimizing or maximizing an objective function by adjusting the parameters or variables of a model or system. (https://coral.ise.lehigh.edu/frankecurtis/files/papers/BottCurtNoce18.pdf)

There are multiple algorithms for optimization. In this building block one of the most common used ones is discussed: gradient descent. However, before delving into specifics of these algorithm, it's crucial to familiarize ourselves with key terms and their respective definitions

### Cost function and loss function 
These two terms are occasionally used interchangeably, yet they bear distinctions. The loss function addresses the variance between the actual and predicted values for an individual entry in the dataset, whereas the cost function is the average of the loss function across the entire dataset. The cost function aids in optimizing the best function for the training data.

### Cost function in regression problems 

Consider fitting a linear function (Equation 1) with two parameters $\theta_0$ and $\theta_1$ to a dataset. The goal is to choose $\theta_0$ and $\theta_1$ such that the differences between $h(x)$ (the predicted value) and $y$ (the actual value) is minimized. This involves solving a minimization problem. One approach is to minimize the squared difference between $y$ and $h(x)$ and calculate their average (Equation2). The objective is to select $\theta_0$ and $\theta_1$ in a manner that minimizes Equation 2. The visual representation of this objective function is depicted in the figure below.

<div style="text-align: center;">
{{<katex>}}
h_\theta(x) = \theta1x + \theta0                  
{{</katex>}}
 :Equation1
</div>

<p align = "center">
<img src = "../img/hypothesis_function.png" width="400">
</p>

this is going to be objective function for linear regression. And we need to minimize $J(\theta_1,\theta_0)$ over $\theta_0$ and $\theta_1$: 


<div style="text-align: center;">
{{<katex>}}
J(\theta_1, \theta_0) = \left[ \frac{1}{2m} \sum_{i=1}^{m} (y(i) - h_\theta(x(i)))^2 \right]
{{</katex>}}
    :Equation 2
</div>  


 Equation 2 represents the cost function for regression problems. This particular cost function, known as the squared error cost function, is widely used for optimizing the majority of regression problems. It serves as a measure to quantify the difference between predicted values and actual values, providing a foundation for minimizing the error during the optimization process. 
For a more intuitive understanding, let's consider the following example.

{{% example %}}

for simplicity, let's assume $\theta_0=0$, implying that the equation line passes through the origin $(0,0)$. Our goal is to fit the equation $h(x)=\theta_1*x$ to the sample data showed by red crosses in the following plots. We examine different values for $\theta_1$ such as $1, 0.5, -0.5$  to observe their efffect on the cost function $J(\theta_1)$. while $h_\theta(x)$ is a function of $x$, the cost function is dependent on $\theta_1$. The plots below illustrate how changes in $\theta_1$ values affect the cost function. Note that we need to find th optimal $\theta_1$ that minimize cost function.
<p align = "center">
<img src = "../img/costfunctionplot_1.png" width="400">
</p>
<p align = "center">
<img src = "../img/costfunctionplot_2.png" width="400">
</p>



{{% /example %}}

In real-world scenarios, it's common to have more than one predictor, such as $\theta_1$. Consequently, the cost function becomes dependent on multiple variables. In the case of a two-dimensional problem, the cost function takes on a form similar to the following: 
<p align = "center">
<img src = "../img/2_dim_costfunction.png" width="400">
</p>


The contour plot below illustrates the two-dimensional cost function, representing the mapping of the previous plot onto a 2D surface. Each contour on this plot corresponds to the same cost value for different $\theta$ values. In machine learning, the goal is to navigate towards the smallest contour on this plot, indicating the minimum cost value. Essentially, when $\theta_1$ and $\theta_0$ are set in a way that the line aligns with the data trend, the cost value converges towards the center (minimum value). Conversely, when the objective function is not aligned with the data trend, the cost value is situated farther from the center on the contour levels. This alignment process is crucial in achieving optimal parameter values for effective model fitting.

<div style="text-align: center; position: relative;">
<img src = "../img/countourmap_2d.jpeg" width="400">
Contour map on cost function for two dimentional problem.   
<sup> Andrew Ng</sup>
</p>
</div>


### Cost function in classification 

Given that the objective function for a classification problem differs from that of a regression problem, the associated cost function also varies. Consider optimizing a logistic regression problem involving two classes, denoted as 0 and 1. In this context, the objective function is represented by the sigmoid function, which is outlined as follows: 


<div style="text-align: center;">
{{<katex>}}
h_\theta(x) = \frac{1}{1 + e^{-\theta \cdot x}}
for j=0 , j=1
{{</katex>}}
Equation 3
</div>

and corresponding cost function is: 

 <div style="text-align: center;">
{{<katex>}}
\text{Cost}(h_{\theta}(x), y) = \begin{cases}
    -\log(h_{\theta}(x)), & \text{if } y = 1 \\
    -\log(1 - h_{\theta}(x)), & \text{if } y = 0
\end{cases}
{{</katex>}}
        Equation 4
</div>

The next figure visualizes the cost function across various combinations of the objective function results (predicted values) and actual labels when $y$ is either $0$ or $1$. This visualization provides insights into how the cost varies with different scenarios. For instance, when predicted value is $0$ while the actual value is $1$, the cost function goes towards infinity. 

<p align = "center">
<img src = "../img/classification cost function.png" width="400">
</p>

we can combine both form of cost function from Equation 4 in to a single consolidated cost function: 

<div style="text-align: center;">
{{<katex>}}
J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y^{(i)} \log(h_\theta(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_\theta(x^{(i)})) \right]

{{</katex>}}
        Equation 5
</div>

{{% tip %}}
When  $y$ equals $1$, the second term $\(1 - y) \log(1 - h_\theta(x))\$ becomes $0$, having no impact on the outcome. Similarly, if $y$ is $0$, the first term $\-y \log(h_\theta(x))\$ becomes $0$, has no influence on the result.
{{% /tip %}}




## Gradient decent     

Now that we've delved into the concept of the cost function, let's explore the algorithms employed to optimize it. One widely utilized optimization algorithm is gradient descent, applicable not only to the cost function in linear regression but also to a diverse array of cost functions.

Suppose our goal is to minimize $J(\theta_0, \theta_1)$  using gradient descent. The algorithm begins by initializing $\theta_0$  and $\theta_1$ with random values. Subsequently, it iteratively takes small steps, adjusting these parameters until it converges to a minimum, which might be a local minimum. For a more comprehensive understanding, refer to the visual representation below.

<p align = "center">
<img src = "../img/gradientDecent.png" width="400">
</p>
Moving from a random point to the minimum using Gradient Decent
<sup>Andrew Ng</sup>

{{% tip %}}
- Reaching a minimum point depends on the initial random start. As shown in the picture, two different starting points lead to different local minima. This emphasizes how the choice of the starting point influences the optimization outcome.
{{% /tip %}}

### Gradient descent algorithm

Gradient Descent Algorithm plays a pivotal role in optimizing model parameters. It is a powerful iterative approach that refines these parameters to minimize the difference between predicted and actual values, ultimately enhancing the model's predictive accuracy. The algorithm, defined by repeated iterations, involves updating parameters based on gradients calculated from the cost function. This iterative refinement continues until convergence is achieved, ensuring the model approaches an optimal solution. 

The main part of GD algorithm is iteration of the following steps until convergence is achieved:
<div style="text-align: center;">
{{<katex>}}

\theta_j := \theta_j - \alpha \frac{\sigma J(\theta_0, \theta_1)}{\sigma \theta_j}

for j=0 and j=1.
{{</katex>}}
</div>

In each iteration, the partial derivative of the cost function $J$ with respect to $\theta$ is computed. This derivative is then scaled by the learning rate and subtracted from the current $\theta$. This process is repeated until $\theta$ shows negligible changes or until a predefined number of iterations is reached. This iterative approach allows the parameters $\theta$ to gradually adjust, guiding the model toward convergence.
 
{{% tip %}}

When optimizing your machine learning algorithm, it's crucial to consider the learning rate, denoted as $\alpha$. This hyperparameter determines the size of the steps taken during optimization. A larger $\alpha$ corresponds to more significant parameter changes in each step, while a smaller $\alpha$results in more gradual adjustments. It's essential to fine-tune $\alpha$ based on the specific characteristics of your problem. For example, an excessively large $\alpha$ may lead to overshooting, hindering convergence to the minimum. Conversely, an excessively small $\alpha$ may slow down progress. Striking the right balance is key to achieving effective optimization.

{{% /tip %}}

To gain a comprehensive understanding of concepts like gradient descent and other machine learning principles, consider watching Andrew Ng's instructional videos. 

Andrew Ng. Machine Learning. [Online] https://www.coursera.org/learn/machine-learning-course

{{% summary %}}
- **Understanding Optimization:**
  - get familiar with the definition of loss function and cost function.
  - Explore cost function for linear regression.
  - explore cost function for logistic regression.
- **Gradient Descent:**
    - explore concept of gradient descent 
    - explain Gradient descent algorithm 

{{% /summary %}}











