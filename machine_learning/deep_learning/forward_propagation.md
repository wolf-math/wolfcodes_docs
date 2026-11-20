---
title: Forward Propagation
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is forward propagation?

**Forward propagation** (the **forward pass**) is how a neural network turns an input into a prediction. Data flows forward from the input layer, through each hidden layer, to the output layer.

Think of it as a factory assembly line: raw materials (the data) enter at one end, pass through stations where specific transformations happen, and a finished product (the prediction) comes out the other end.

## Why this matters

Forward propagation is how a trained network makes every prediction, and it's the first half of every training step. Being able to trace it by hand turns a neural network from a black box into a sequence of simple, checkable calculations.

## How it works

At every neuron, forward propagation performs two operations:

1. **Linear transformation**: Compute the weighted sum of the inputs plus a bias, $z = \sum w_i x_i + b$. This is exactly what a [perceptron](./perceptron.md) does.
2. **Non-linear activation**: Pass $z$ through an [activation function](./activation_functions.md) to get the neuron's output, which becomes an input for the next layer.

Layer by layer, the outputs of one layer become the inputs of the next, until the output layer produces the final prediction.

## Example: detecting credit card fraud

Let's walk through a forward pass for a network that predicts whether a credit card transaction is fraudulent.

### The input layer

The network looks at two features of an incoming transaction, both scaled between 0 and 1:

- $x_1 = 0.85$: The transaction amount relative to the user's normal spending. This is an unusually large purchase.
- $x_2 = 0.90$: The geographic distance from the user's last known location. This is very far away.

### The hidden layer: extracting features

Neurons in the hidden layer combine the inputs to detect higher-level patterns. Let's look at two of them, both using ReLU.

**Neuron A** learns to detect an **unusual spending spike**. It weights the amount heavily: $w_1 = 0.9$, $w_2 = 0.1$, with bias $-0.15$.

$$
z_A = (0.85 \times 0.9) + (0.90 \times 0.1) - 0.15 = 0.765 + 0.09 - 0.15 = 0.705
$$

ReLU leaves positive values unchanged, so $a_A = 0.705$.

**Neuron B** learns to detect an **impossible-travel anomaly**, such as a cloned card used abroad. It weights distance more: $w_1 = 0.4$, $w_2 = 0.8$, with bias $-0.2$.

$$
z_B = (0.85 \times 0.4) + (0.90 \times 0.8) - 0.2 = 0.34 + 0.72 - 0.2 = 0.86
$$

After ReLU, $a_B = 0.86$.

### The output layer: the final prediction

The output neuron takes $a_A = 0.705$ and $a_B = 0.86$, with weights $w_{out1} = 1.2$ and $w_{out2} = 1.5$ and bias $b_{out} = -0.5$:

$$
z_{out} = (1.2 \times 0.705) + (1.5 \times 0.86) - 0.5 = 0.846 + 1.29 - 0.5 = 1.636
$$

A sigmoid activation squashes this into a probability:

$$
\hat{y} = \sigma(1.636) = \frac{1}{1 + e^{-1.636}} \approx 0.84
$$

The network outputs 0.84: an 84% probability that the transaction is fraudulent, which could trigger an automatic block or security alert.

### The same forward pass in code

With NumPy, a whole layer is a single matrix multiplication:

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

x = np.array([0.85, 0.90])

# Hidden layer: one row of weights per neuron (A and B)
W_hidden = np.array([[0.9, 0.1],
                     [0.4, 0.8]])
b_hidden = np.array([-0.15, -0.2])

# Output layer
W_out = np.array([1.2, 1.5])
b_out = -0.5

hidden = relu(W_hidden @ x + b_hidden)
y_hat = sigmoid(W_out @ hidden + b_out)

print(hidden)           # [0.705 0.86 ]
print(f"{y_hat:.2f}")   # 0.84
```

## What happens next?

Forward propagation only produces a prediction. To *learn*, the network compares that prediction ($\hat{y}$) to the actual outcome ($y$, whether the transaction really was fraud) using a [loss function](./loss_functions.md). That error is then sent backward through the network during [backpropagation](./backpropagation.md) to update the weights and biases, making the model sharper for future transactions.

## Summary

- Forward propagation passes input data through the network, layer by layer, to produce a prediction.
- Each neuron computes a weighted sum plus bias, then applies an activation function.
- Hidden neurons learn to detect useful intermediate patterns, like spending spikes or impossible travel.
- The forward pass is the first half of training; backpropagation is the second.
