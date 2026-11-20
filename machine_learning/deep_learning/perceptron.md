---
title: The Perceptron
sidebar_position: 2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is a perceptron?

A **perceptron** is the simplest possible neural network: a single artificial neuron. It's the foundational building block of deep learning.

A perceptron is a **binary linear classifier**. It takes several inputs, weighs how important each one is, and outputs a single yes/no decision: 0 or 1.

## Why this matters

Every neural network, from a tiny classifier to a large language model, is built from units that work like a perceptron: weigh the inputs, add a bias, apply an activation. Understanding one neuron makes the rest of deep learning much easier to follow.

## The parts of a perceptron

A perceptron has four components:

1. **Inputs ($x_1, x_2, \dots, x_n$)**: The features, or numeric data, fed into the model.
2. **Weights ($w_1, w_2, \dots, w_n$)**: One per input. They set how much each input influences the decision. Larger weights mean more influence.
3. **Bias ($b$)**: An adjustable offset that shifts the decision boundary. It controls how easily the perceptron "fires," and lets it output 1 even when every input is 0.
4. **Activation function**: A threshold function that turns the weighted sum into a 0 or 1. The classic choice is the **step function** (also called the Heaviside step function).

## The math

The perceptron computes a weighted sum of its inputs and adds the bias:

$$
z = \sum_{i=1}^{n} w_i x_i + b = \mathbf{w} \cdot \mathbf{x} + b
$$

Then the step function decides the output:

$$
y = \begin{cases} 1 & \text{if } z \ge 0 \\ 0 & \text{if } z < 0 \end{cases}
$$

## Example: an AND gate

Let's see a perceptron model a logical **AND gate**, which outputs 1 only when *both* inputs are 1.

### The truth table

| $x_1$ | $x_2$ | Output |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Choosing weights and bias

Set the weights to $w_1 = 1$ and $w_2 = 1$, and the bias to $b = -1.5$. The weighted sum becomes:

$$
z = (1 \cdot x_1) + (1 \cdot x_2) - 1.5
$$

### Checking every case

1. **$x_1 = 0, x_2 = 0$** (both false):
   $z = (1 \cdot 0) + (1 \cdot 0) - 1.5 = -1.5$.
   Since $-1.5 < 0$, the output is **0**.

2. **$x_1 = 0, x_2 = 1$** (only $x_2$ true):
   $z = (1 \cdot 0) + (1 \cdot 1) - 1.5 = -0.5$.
   Since $-0.5 < 0$, the output is **0**.

3. **$x_1 = 1, x_2 = 0$** (only $x_1$ true):
   $z = (1 \cdot 1) + (1 \cdot 0) - 1.5 = -0.5$.
   Since $-0.5 < 0$, the output is **0**.

4. **$x_1 = 1, x_2 = 1$** (both true):
   $z = (1 \cdot 1) + (1 \cdot 1) - 1.5 = 0.5$.
   Since $0.5 \ge 0$, the output is **1**.

The perceptron reproduces the AND gate perfectly. Geometrically, it draws a straight line that separates the point $(1, 1)$ from the other three.

:::note
Because a perceptron can only draw a single straight line, it can't learn problems that aren't linearly separable. The classic example is XOR (output 1 when exactly one input is 1). Solving problems like that requires multiple [layers](./layers.md) of neurons.
:::

## Learning the weights

Above, we chose the weights by hand. A real perceptron *learns* them from examples using the **perceptron learning rule**: whenever it gets an example wrong, nudge each weight in the direction that would have made the answer more correct.

$$
w_i \leftarrow w_i + \alpha \cdot (y - \hat{y}) \cdot x_i
\qquad
b \leftarrow b + \alpha \cdot (y - \hat{y})
$$

- $\alpha$ is the **learning rate**, which controls the size of each nudge.
- $y - \hat{y}$ is the error: the true label minus the prediction. It's 0 when the prediction is correct, so correct answers cause no change.

## Implementing a perceptron in Python

Here's a perceptron with prediction and the learning rule, using NumPy:

```python
import numpy as np


class Perceptron:
    def __init__(self, input_dim, lr=0.1):
        self.weights = np.zeros(input_dim)
        self.bias = 0.0
        self.lr = lr

    def activation(self, z):
        return 1 if z >= 0 else 0

    def predict(self, x):
        z = np.dot(x, self.weights) + self.bias
        return self.activation(z)

    def train(self, X, y, epochs=10):
        for _ in range(epochs):
            for xi, target in zip(X, y):
                error = target - self.predict(xi)
                # Perceptron learning rule: only update when wrong
                if error != 0:
                    self.weights += self.lr * error * xi
                    self.bias += self.lr * error


# Train it on the AND gate
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

perceptron = Perceptron(input_dim=2)
perceptron.train(X_and, y_and, epochs=10)

print('Learned weights:', perceptron.weights)
print('Learned bias:', perceptron.bias)
print('Predictions:', [perceptron.predict(x) for x in X_and])
```

The final line should print `Predictions: [0, 0, 0, 1]`, matching the AND truth table. The learned weights won't match our hand-picked ones exactly; any line that separates the points works.

## Summary

- A perceptron is a single artificial neuron: weighted sum, plus bias, through a step function.
- It's a binary linear classifier, so it can only separate classes with a straight line.
- It learns by nudging its weights whenever it makes a mistake.
- Stacking perceptrons into layers is what gives neural networks their power.
