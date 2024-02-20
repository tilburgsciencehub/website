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
Single-layer neural networks, also referred to as shallow neural networks, comprise a solitary hidden layer positioned between the input and output layers. This hidden layer conducts computations, orchestrating the transformation of input data to yield the intended output. Shallow neural networks, though straightforward, possess restricted capacity for learning intricate patterns and representations.

In contrast, deep neural networks boast multiple hidden layers interspersed between the input and output layers. These networks can be profoundly deep, incorporating tens or even hundreds of layers. Each layer undertakes computations, forwarding the modified data to the subsequent layer in succession.

# Components of Deep Learning Network
In the sections above we introduced concept of Deep Learning and we talked a little bit about biology behind it. Lets move not to the core concept in deep learning from the machine learning point of view.

## Loss function
Training dataset of I pairs of input/output examples:
• The loss function measures the difference between the model’s predictions and actual outcomes
(how bad model is). Its value depends on:
• The set of parameters controlling the structure of the equation
• The chosen family of mathematical equations;
• The training dataset
• returns a scalar that is smaller when the model maps inputs to outputs better

## Activation function
Activation functions are essential components of neural networks as they introduce nonlinearity, a crucial element for enabling the development of intricate representations and functions. This nonlinearity expands the network's capacity to capture complex relationships and patterns from the inputs, surpassing the capabilities of a basic linear regression model.

## Input layer
Input layer refers to the first layer of nodes in an artificial neural network. This layer receives input data from the outside world.

## Hidden layer

Hidden layers are what make neural networks "deep" and enable them to learn complex data representations. 

## Output layer

The output layer is the final layer in the neural network where desired predictions are obtained. There is one output layer in a neural network that produces the desired final prediction.

## Code example

### References:
Prof. Matteo Bustreo, 2023 “Lesson2-Foundations of Deep Learning" https://tilburguniversity.instructure.com/courses/14887/files/2934299?module_item_id=669643.
Matteo's lecture 

McCullum, N. (2021, 28 april). Deep Learning Neural networks explained in Plain English. freeCodeCamp.org. https://www.freecodecamp.org/news/deep-learning-neural-networks-explained-in-plain-english/
