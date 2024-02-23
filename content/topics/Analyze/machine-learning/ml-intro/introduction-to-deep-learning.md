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

Deep learning is a type of machine learning that's inspired by the structure and function of the human brain, particularly in how it processes information and learns from it. It's called "deep" learning because it involves neural networks with many layers—these are the "deep" part. Each layer of these networks learns to transform the data in a way that makes it more useful for achieving the network's overall goal.

## Inspiration from the human brain

As has been described in the section above, the inspiration actually comes from the human brain structure. Let's take a look at the human brain neuron anatomy.

<p align = "center">
<img src ="../images/neuron-anatomy.png" width="400">
</p>
Picture source: McCullum, N. (2021, 28 april). Deep Learning Neural networks explained in Plain English

During his groundbreaking research on neural networks, Geoffrey Hinton posed a crucial question: could we develop computer algorithms that emulate the behavior of neurons in the brain? The aspiration was to replicate the brain's structure in order to harness some of its capabilities. 

In pursuit of this goal, researchers examined the behavior of neurons within the brain. A key insight emerged: a single neuron lacks utility on its own; rather, functional significance arises from networks of neurons working together.

This arises from the nature of neurons, which operate by transmitting signals. Specifically, dendrites of neurons receive signals and transmit them along the axon.

### How neurons forward the information?
An actual neuron fires an output signal only when the total strength of the input signals exceed a certain threshold. This
phenomenon is modeled in the perceptron by calculating the weighted sum of the inputs and applying a step or activation [YET TO BE CHECKED HERE]} function.

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

When it comes to neural networks we could distinguish shallow and deep neural networks. What is the difference?

Single-layer neural networks, also referred to as shallow neural networks, comprise a solitary hidden layer positioned between the input and output layers. This hidden layer conducts computations, orchestrating the transformation of input data to yield the intended output. Shallow neural networks, though straightforward, possess restricted capacity for learning intricate patterns and representations.

In contrast, deep neural networks boast multiple hidden layers interspersed between the input and output layers. These networks can be profoundly deep, incorporating tens or even hundreds of layers. Each layer undertakes computations, forwarding the modified data to the subsequent layer in succession.

# Components of deep learning network
In the sections above we introduced concept of deep learning and we talked a little bit about biology behind it. Let's move now to the core concept in deep learning from the machine learning point of view.

### Input layer
Input layer refers to the first layer of nodes in an artificial neural network. This layer receives input data from the outside world.

###  Hidden layer

Hidden layers are what make neural networks "deep" and enable them to learn complex data representations. 

### Output layer

The output layer is the final layer in the neural network where desired predictions are obtained. There is one output layer in a neural network that produces the desired final prediction.

## How information is transferred between the layers?

In neural networks, information is transferred between layers through weighted connections. Each neuron in a layer receives input from neurons in the previous layer, multiplies these inputs by corresponding weights, sums them up, and applies an activation function to produce an output. This output becomes the input for neurons in the next layer, and the process repeats for each layer until reaching the output layer. 

## Loss function
The loss function in deep learning measures how well the model's predictions match the actual targets in the training data. It quantifies the difference between predicted and true values, providing feedback for adjusting the model's parameters during training. The goal is to minimize the loss function, indicating better alignment between predictions and actual outcomes, ultimately improving the model's performance. 

Mathematically speaking it is the chosen family of mathematical equations which returns a scalar that is smaller when the model maps inputs to outputs better.

$L[\theta, f[x, \theta], \{ [x_{i}, y_{i}] \}^{I}_{i=1}]$

where: 
- $ f[x, \theta] $ is a deep learning model
- $ \{ [x_{i}, y_{i}] \}^{I}_{i=1} \$ is a training data

## Training
Training dataset of I pairs of input/output examples:
YET TO BE CORRECTED
$ \{ [x_{i}, y_{i} ]\}^{I}_{i=1} \$

Training consists in finding the model's parameters to minimize the loss function, i.e:

$\hat{\theta} = argmin[L[\theta, f[x, \theta], \{ [x_{i}, y_{i}] \}^{I}_{i=1}]]$

Let us denote a single prediction $\hat{y}$ in the following way:

$\hat{y} = f[x, \hat{\theta}]$

## Activation function
The composition of linear functions is still a linear function: without non-linearity, Deep neural networks would still behave like a single-layer network.

Activation functions are essential components of neural networks as they introduce nonlinearity, a crucial element for enabling the development of intricate representations and functions. This nonlinearity expands the network's capacity to capture complex relationships and patterns from the inputs, surpassing the capabilities of a basic linear regression model.

Multiple options are available for the choice of the activation function:

- Sigmoid function (Only used in the output layer of the logistic regression):
$ a(z) =  \frac{\mathrm{1} }{\mathrm{1} + e^-{z} }  $ 

- Tanh function:
$ a(z) = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}} $

- ReLU function:
$ a(z) = \max\(0,z)$

## Putting the layers mathematically together
After introducing all necessary concepts, lets take a look at the math:

input layer:
$ x_{0} = {x_{0}, x_{1},... x_{i}} $

$1st$ hidden layer:
$ h_{0} = a[\beta_{0} + \omega_{0}] $ 

$2nd$ hidden layer:
$ h_{1} = a[\beta_{1} + \omega_{1}]$

output:
$ y =  \beta_{2} + \omega_{2}h_{2} $

$kth$ hidden layer:
$ h_{k} = a[\beta_{k-1} + \omega_{k-1}h_{k-1}] $

output:
$y =  \beta_{k} + \omega_{k}h_{k} $

{{<katex>}}  {{</katex>}} 

where: 

- $a$ is an activation function
- $\beta$ is bias vector (biases: Additional parameters added to the weighted sum before applying the activation function)
- $\omega$ is a weight matrix (grid-like structure containing numerical values. Each value in the matrix represents the strength of a connection between neurons in one layer and neurons in the next layer of a neural network.)

Finally the general equation of the deep neural network could be annotated as following:

$y = \beta_{k} + \omega_{k}a[\beta_{k-1} + \omega_{k-1}a[...\beta_{2} + \gamma_{2}a[...\beta_{1} + \gamma_{1}]]...]]$

### General graphical represantion of a deep neural network:
So putting it all together on the graph:
<p align = "center">
<img src ="../images/deep-neural-network-graphics.png" width="400">
</p> 

## Coding deep neural network

The go-to tools for building deep neural networks are TensorFlow, Keras, and PyTorch. Since TensorFlow 2.0, Keras has merged with TensorFlow, which means we can now use Keras to build complex networks directly within TensorFlow. It's a powerful combination that simplifies the process of creating sophisticated models.


```
# Importing necessary libraries
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess the data
X_train = X_train.reshape((X_train.shape[0], -1)).astype('float32') / 255
X_test = X_test.reshape((X_test.shape[0], -1)).astype('float32') / 255
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Creating a Sequential model
model = Sequential()

# Adding layers to the model
model.add(Dense(units=64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# Compiling the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Training the model
model.fit(X_train, y_train, epochs=10, batch_size=128, verbose=1, validation_split=0.2)

# Evaluating the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)

```

### References:
Prof. Matteo Bustreo, 2023 “Lesson2-Foundations of Deep Learning" https://tilburguniversity.instructure.com/courses/14887/files/2934299?module_item_id=669643.

McCullum, N. (2021, 28 april). Deep Learning Neural networks explained in Plain English. freeCodeCamp.org. https://www.freecodecamp.org/news/deep-learning-neural-networks-explained-in-plain-english/
