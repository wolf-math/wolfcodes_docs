---
title: Intro to Deep Learning
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is deep learning?

**Deep learning** is a subfield of machine learning loosely inspired by the structure of the human brain. It uses **artificial neural networks (ANNs)** made of many layers of connected units called **neurons**. The "deep" refers to stacking many of these layers.

Classical machine learning usually needs a human expert to design the features a model learns from. Deep learning's big advantage is **automatic feature extraction**: it discovers useful patterns directly from raw, unstructured data like images, audio, and text.

## Why this matters

Deep learning powers image recognition, speech assistants, translation, and large language models. Even if you mostly work with tabular data, knowing how neural networks learn helps you judge when they're worth their cost, and the rest of the guides in this section build directly on the concepts introduced here.

## Layers learn levels of abstraction

Each layer in a deep network transforms its input into a slightly more abstract representation, and deeper layers build on the patterns found by earlier ones.

In **image recognition**:

- **Early layers** detect edges, textures, and simple shapes.
- **Middle layers** recognize parts of objects, like a nose, an eye, or a wheel.
- **Deeper layers** identify complete objects, like a cat, a car, or a face.

In **natural language processing (NLP)**:

- **Early layers** pick up on words and short phrases.
- **Middle layers** recognize sentence structure and grammar.
- **Deeper layers** capture context, meaning, and sentiment.

## How deep learning works

A neural network learns by repeating a loop over the training data:

1. **[Forward propagation](./forward_propagation.md)**: Input data (like pixel values) enters the **input layer** and flows through one or more **hidden layers**. In each neuron, inputs are multiplied by adjustable **weights**, a **bias** is added, and the result passes through an **activation function** (like ReLU). The **output layer** produces a prediction.
2. **[Loss calculation](./loss_functions.md)**: A **loss function** compares the prediction with the true answer and produces a single number measuring how wrong it was.
3. **[Backpropagation](./backpropagation.md) and [optimization](./optimizers.md)**: Using the chain rule from calculus, backpropagation calculates how much each weight and bias contributed to the error. An optimizer (like SGD or Adam) then nudges every parameter in the direction that reduces the loss.

Repeat this loop over many passes through the data, and the network's predictions steadily improve.

## Key concepts

### Weights and biases

- **Weights ($W$)**: Numbers that set the strength of each connection between neurons. A larger weight means that input has more influence on the output.
- **Biases ($b$)**: A number added to the weighted sum before the activation function. It shifts the neuron's activation threshold up or down, helping the model fit the data.

Weights and biases are the network's **parameters**: the values it learns during training.

### Activation functions

An **activation function** is applied to each neuron's output to introduce **non-linearity**. Without it, a neural network of any depth would collapse into a single linear model, no more powerful than [linear regression](../algorithms/linear_regression.md).

- **ReLU (rectified linear unit)**: The most popular choice. It outputs the input if it's positive, and 0 otherwise: $f(x) = \max(0, x)$.
- **Sigmoid and tanh**: "Squashing" functions that map inputs into a limited range (0 to 1 for sigmoid). Sigmoid is often used in the output layer for binary classification.

See [activation functions](./activation_functions.md) for the full list.

### Loss (cost) function

A **loss function** measures the gap between the network's predictions and the true labels. Common examples are **mean squared error (MSE)** for regression and **cross-entropy** for classification. Training is the process of minimizing this value.

### Backpropagation

Short for "backward propagation of errors," **backpropagation** is the core algorithm for training neural networks. It applies the chain rule to compute the gradient of the loss with respect to every weight and bias, working backward from the output layer to the input layer.

### Gradient descent

**Gradient descent** is the optimization algorithm that updates the weights and biases using the gradients from backpropagation. It repeatedly takes a step "downhill" on the error surface, in the direction that reduces the loss fastest. Popular variants include **stochastic gradient descent (SGD)** and **Adam**. See [gradient descent](./gradient_descent.md) and [optimizers](./optimizers.md).

### Overfitting and regularization

- **Overfitting**: The model learns the training data *too* well, memorizing noise and outliers instead of general patterns, so it performs poorly on new data.
- **Regularization**: Techniques that prevent overfitting, such as **dropout** (randomly switching off some neurons during training) and **weight decay** (L2 regularization, which penalizes large weights).

See [overfitting and regularization](./regularization.md).

### Epochs, batches, and iterations

- **Epoch**: One complete pass of the entire training dataset through the network.
- **Batch size**: The number of training examples processed together before the weights are updated once.
- **Iteration**: One weight update, i.e. one batch. The number of iterations per epoch is the dataset size divided by the batch size.

For example, with 1,000 training examples and a batch size of 100, one epoch takes 10 iterations.

## Benefits of deep learning

- **Automatic feature engineering**: The model discovers useful representations on its own, instead of relying on hand-crafted features.
- **Scales with data**: Performance keeps improving with more data, and deep learning dominates complex domains like computer vision, NLP, and speech recognition.
- **Handles unstructured data**: It works directly with images, video, audio, and free text.

## Challenges of deep learning

- **Data-hungry**: It usually needs large amounts of high-quality labeled data. On small datasets, simpler methods often win.
- **Computationally expensive**: Training large models requires specialized hardware (GPUs or TPUs) and significant energy.
- **The "black box" problem**: It's hard to explain exactly why a deep network made a particular prediction, which is a serious issue in fields like medicine and finance.

## Deep learning vs. classical machine learning

| Feature | Classical machine learning | Deep learning |
|---------|----------------------------|---------------|
| **Data needed** | Works well on small to medium datasets | Needs large datasets to shine |
| **Feature extraction** | Manual: needs domain expertise | Automatic: learns features from raw data |
| **Hardware** | Runs fine on standard CPUs | Relies on GPUs or TPUs |
| **Training time** | Seconds to hours | Hours to weeks, depending on scale |
| **Typical algorithms** | Linear regression, decision trees, SVMs, random forests | CNNs, RNNs, Transformers |

**Rule of thumb:** For structured, tabular data (spreadsheets, database tables), start with classical models like [gradient boosting](../algorithms/gradient_boosting.md). Reach for deep learning when your data is images, audio, or text, or when you have a very large dataset.

## Summary

- Deep learning uses many-layered neural networks that learn features directly from raw data.
- Training is a loop: forward pass, loss, backpropagation, and a weight update from the optimizer.
- Activation functions add the non-linearity that makes deep networks powerful.
- Deep learning excels on large, unstructured datasets but needs lots of data and compute.
