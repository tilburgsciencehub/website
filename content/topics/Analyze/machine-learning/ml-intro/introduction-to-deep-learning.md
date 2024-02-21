---
title: "Introduction to Deep Learning"
description: "Broaden your knowledge about machine learning with this introduction to deep learning."
keywords: "machine learning, deep learning, neural networks, model, python"
weight: 3
date: 2024-02-18T22:02:51+05:30
draft: false
aliases:
  - /learn/machine-learning
---
# What is Deep Learning?

Deep Learning is an evolution of Neural Networks, with more layers/modules

• Deep Learning generates non-linear, hierarchical representations, progressively transforming data into more abstract forms with each layer.

• Deep learning models are capable of adapting to diverse input/output formats and sizes, ranging from images to intricate language structures.

### Inspiration from the human brain

• The inspiration comes actually from the human brain structure. Let's take a look at the human brain neuron anatomy.

<p align = "center">
<img src ="../images/neuron-anatomy.png" width="400">
</p>

During his groundbreaking research on neural networks, Geoffrey Hinton posed a crucial question: could we develop computer algorithms that emulate the behavior of neurons in the brain? The aspiration was to replicate the brain's structure in order to harness some of its capabilities. 

In pursuit of this goal, researchers examined the behavior of neurons within the brain. A key insight emerged: a single neuron lacks utility on its own; rather, functional significance arises from networks of neurons working together.

This arises from the nature of neurons, which operate by transmitting signals. Specifically, dendrites of neurons receive signals and transmit them along the axon.

An actual neuron fires an output signal only when the total
strength of the input signals exceed a certain threshold. This
phenomenon is modeled in the perceptron by calculating the
weighted sum of the inputs and applying a step or activation [YET TO BE CHECKED HERE]}function.
Now, how can we convert it to the computers?

Let's consider the architecture below:

<p align = "center">
<img src ="../images/neuron-functionality-in-code.png" width="400">
</p> 
Picture source: McCullum, N. (2021, 28 april). Deep Learning Neural networks explained in Plain English

Weights play a crucial role in deep learning as they are pivotal in training models. The adjustment of weights constitutes the primary method of training deep learning models, a concept that will become evident as we proceed to construct our initial neural networks.

After a neuron gathers inputs from preceding layer neurons, it computes the sum of each signal multiplied by its respective weight. Subsequently, these computed values are transmitted to an activation function, as demonstrated below:

<p align = "center">
<img src ="../images/artificial-neuron.png" width="400">
</p> 
Picture source: McCullum, N. (2021, 28 april). Deep Learning Neural networks explained in Plain English

# Shallow and deep neural networks
• Flexible enough to describe arbitrarily complex input/output mappings
• Can have as many inputs as we want
• Can have as many outputs as we want

Single-layer neural networks, also referred to as shallow neural networks, comprise a solitary hidden layer positioned between the input and output layers. This hidden layer conducts computations, orchestrating the transformation of input data to yield the intended output. Shallow neural networks, though straightforward, possess restricted capacity for learning intricate patterns and representations.

In contrast, deep neural networks boast multiple hidden layers interspersed between the input and output layers. These networks can be profoundly deep, incorporating tens or even hundreds of layers. Each layer undertakes computations, forwarding the modified data to the subsequent layer in succession.

# Components of Deep Learning Network
In the sections above we introduced concept of Deep Learning and we talked a little bit about biology behind it. Lets move now to the core concept in deep learning from the machine learning point of view.

## Input layer
Input layer refers to the first layer of nodes in an artificial neural network. This layer receives input data from the outside world.

## Hidden layer

Hidden layers are what make neural networks "deep" and enable them to learn complex data representations. 

## How information is transferred between the layers?


## Loss function
Training dataset of I pairs of input/output examples:
{x_{1},y_{1}^I_{i}}

Training dataset of I pairs of input/output examples:
• The loss function measures the difference between the model’s predictions and actual outcomes
(how bad model is). Its value depends on:
• The set of parameters controlling the structure of the equation
• The chosen family of mathematical equations;
• The training dataset
• returns a scalar that is smaller when the model maps inputs to outputs better

$L[$\theta, f[x, $\theta], {x_{1},y_{1}^I_{i}}]$

## Training
\hat{$\theta} = argmin[L[{$\theta}]]

\hat{y} = f[x, \hat{$\theta}]
 

## Activation function
The composition of linear functions is still a linear function: without non-linearity, Deep neural networks would still behave like a single-layer network.

Activation functions are essential components of neural networks as they introduce nonlinearity, a crucial element for enabling the development of intricate representations and functions. This nonlinearity expands the network's capacity to capture complex relationships and patterns from the inputs, surpassing the capabilities of a basic linear regression model.

Multiple options are available for the choice of the activation function:
Sigmoid function:
Only used in the output layer of the logistic regression
$$ h_ \a(x) =  \frac{\mathrm{1} }{\mathrm{1} + e^- \theta^Tx }  $$ 

Tanh
$$ a(z) = e^-z - e^--z/e^-z + e^--z $$

ReLU
$$ a(z) = max(0,z)

## Output layer

The output layer is the final layer in the neural network where desired predictions are obtained. There is one output layer in a neural network that produces the desired final prediction.


###  A little bit of math to understand what is happening behind the scences
After introducing all necessary concepts, lets take a look at the math:
input layer:
set of x's
$x_{0}

1st hidden layer:
$h_{0} = a[$\beta_{0}$ + $\omega_{0}$]$

2nd hidden layer:
$h_{1} = a[$\beta_{1}$ + $\omega_{1}$]$

output:
$y =  $\beta_{2}$ + $\omega_{2}h_{2}

$h_{k} = a[$\beta_{k-1}$ + $\omega_{k-1}h_{k-1}$]$
$y =  $\beta_{k}$ + $\omega_{k}h_{k}&

where: 
- a is an activation function
- $\beta is bias vector (biases: Additional parameters added to the weighted sum before applying the activation function)
- $\omega is a weight matrix (grid-like structure containing numerical values. Each value in the matrix represents the strength of a connection between neurons in one layer and neurons in the next layer of a neural network.)

Finally the output of the deep neural network could be annotated as following:
$y = $\beta_{k}$ + $\omega_{k}a[$\beta_{k-1}$ + $\omega_{k-1}a[...$\beta_{2} + $\gamma_{2}a[...$\beta_{1} + $\gamma_{1}]]...]]


So putting it all together on the graph:
### General represantion of a deep network:

## Code example



### References:
Prof. Matteo Bustreo, 2023 “Lesson2-Foundations of Deep Learning" https://tilburguniversity.instructure.com/courses/14887/files/2934299?module_item_id=669643.

McCullum, N. (2021, 28 april). Deep Learning Neural networks explained in Plain English. freeCodeCamp.org. https://www.freecodecamp.org/news/deep-learning-neural-networks-explained-in-plain-english/
