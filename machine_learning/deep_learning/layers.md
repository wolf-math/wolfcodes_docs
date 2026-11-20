---
title: Neural Network Layers
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are layers?

A single [perceptron](./perceptron.md) is a basic decision-maker, like one person making a simple yes/no choice. Real-world problems are too complex for one neuron. The solution is to organize many neurons into **layers**.

A **layer** is a group of neurons working side by side. Each layer passes its outputs forward to the next, so the network can build up increasingly complex features. There are three main types:

- **Input layer**: Receives the raw features ($x_1, x_2, \dots, x_n$). No math happens here; it just passes the values forward. It has one neuron per input feature.
- **Hidden layers**: The computational engine of the network, sitting between the input and output layers. Each neuron performs a linear transformation followed by a non-linear activation. "Deep" learning gets its name from stacking many hidden layers, which lets the network learn complex, non-linear patterns.
- **Output layer**: Produces the final prediction ($\hat{y}$). Its shape depends on the task:
  - **Binary classification**: one neuron with a sigmoid activation.
  - **Multi-class classification**: one neuron per class with a softmax activation.
  - **Regression**: one neuron with no activation (a plain linear output).

```text
 Input layer      Hidden layer      Output layer

    x1 ──────┬───▶ (neuron) ──┐
             ╳                ├───▶ (neuron) ───▶ ŷ
    x2 ──────┴───▶ (neuron) ──┘
```

## Why this matters

Choosing layers is how you design a neural network. The number of hidden layers controls how complex the patterns can be, and the output layer has to match your task. Get the output layer wrong and the network can't produce a sensible answer, no matter how well everything else is set up.

## What a neuron does

Every neuron in a hidden or output layer performs two steps:

1. **Linear transformation**: Compute the weighted sum of its inputs plus a bias, $z = \sum w_i x_i + b$, exactly like a [perceptron](./perceptron.md).
2. **Non-linear activation**: Pass $z$ through an [activation function](./activation_functions.md) $f$ to get the neuron's output, $a = f(z)$.

## Example: predicting whether a build will pass

Let's walk through a tiny network that predicts whether a software build will **pass (1)** or **fail (0)**, based on two features scaled between 0 and 1:

- $x_1$: Test coverage ratio.
- $x_2$: Amount of code changed.

### The network

- **Input layer**: 2 nodes ($x_1$, $x_2$).
- **Hidden layer**: 2 neurons with ReLU activation.
- **Output layer**: 1 neuron with sigmoid activation (the probability of passing).

### Step 1: forward propagation

Take a commit with $x_1 = 0.8$ (80% coverage) and $x_2 = 0.2$ (a small change).

**Hidden neuron 1**, with weights $w_{11} = 0.5$, $w_{12} = -0.3$ and bias $b_1 = 0.1$:

$$
z_1 = (0.5 \times 0.8) + (-0.3 \times 0.2) + 0.1 = 0.4 - 0.06 + 0.1 = 0.44
$$

Applying ReLU: $a_1 = \max(0, 0.44) = 0.44$.

**Hidden neuron 2**, with weights $w_{21} = -0.2$, $w_{22} = 0.9$ and bias $b_2 = -0.05$:

$$
z_2 = (-0.2 \times 0.8) + (0.9 \times 0.2) - 0.05 = -0.16 + 0.18 - 0.05 = -0.03
$$

Applying ReLU: $a_2 = \max(0, -0.03) = 0$. This neuron is switched off for this input.

**Output neuron**, taking $a_1 = 0.44$ and $a_2 = 0$ with weights $w_{o1} = 1.2$, $w_{o2} = 0.8$ and bias $b_o = -0.1$:

$$
z_{out} = (1.2 \times 0.44) + (0.8 \times 0) - 0.1 = 0.528 - 0.1 = 0.428
$$

Applying sigmoid:

$$
\hat{y} = \frac{1}{1 + e^{-0.428}} \approx 0.605
$$

The network predicts a 60.5% probability that the build passes.

### Step 2: calculate the loss

Suppose the build actually passed ($y = 1$). We measure the error with **binary cross-entropy**:

$$
\text{Loss} = -[y \log(\hat{y}) + (1 - y) \log(1 - \hat{y})] = -\log(0.605) \approx 0.503
$$

See [loss functions](./loss_functions.md) for more on this formula.

### Step 3: backpropagation and optimization

The network computes the gradient of the loss with respect to every weight and bias using the chain rule. An [optimizer](./optimizers.md) then updates each weight a small step in the direction that reduces the loss:

$$
W_{\text{new}} = W_{\text{old}} - \alpha \frac{\partial \text{Loss}}{\partial W}
$$

Here $\alpha$ is the [learning rate](./gradient_descent.md#the-learning-rate). Repeat this across thousands of commits, and the weights gradually settle on values that predict builds well. See [backpropagation](./backpropagation.md) for a worked example.

## Building layers in code

In Keras, each layer is one line. This is the same 2-2-1 network from the example:

```python
import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential([
    layers.Input(shape=(2,)),               # Input layer: 2 features
    layers.Dense(2, activation='relu'),     # Hidden layer: 2 neurons
    layers.Dense(1, activation='sigmoid'),  # Output layer: probability of passing
])

model.summary()
```

`Dense` means **fully connected**: every neuron receives input from every neuron in the previous layer.

## Specialized layer types

As deep learning evolved, specialized layers were invented for specific kinds of data:

| Layer type | Primary use | How it works |
|------------|-------------|--------------|
| **Convolutional** ([CNNs](./cnn/overview.md)) | Images and video | Slides small learnable filters across the input to detect spatial features like edges and textures. |
| **Recurrent** ([RNNs](./rnn/overview.md)) and **attention** (Transformers) | Text, speech, time series | Captures relationships across time steps or between words in a sequence. |
| **Pooling** | Downsampling in CNNs | Shrinks feature maps (for example, max pooling) to cut computation and overfitting. |
| **Normalization** (batch norm, layer norm) | Training stability | Normalizes layer inputs to stabilize and speed up training. |
| **Dropout** | Regularization | Randomly zeroes some neuron outputs during training to prevent overfitting. |

## Common mistakes

### Mismatching the output layer and the task

The output layer must match what you're predicting.

```python
# Wrong: ReLU can't produce a probability (and can output more than 1)
layers.Dense(1, activation='relu')     # for a yes/no question

# Correct
layers.Dense(1, activation='sigmoid')  # Binary classification
layers.Dense(10, activation='softmax') # 10-class classification
layers.Dense(1)                        # Regression: no activation
```

### Starting too big

A network with many huge layers is slow to train and overfits easily. Start small, and add layers or neurons only when the model is clearly underfitting.

## Summary

- Neural networks organize neurons into input, hidden, and output layers.
- Each neuron computes a weighted sum plus bias, then applies an activation function.
- Hidden layers learn intermediate features; stacking more of them makes the network "deep."
- The output layer's size and activation depend on the task: sigmoid for binary, softmax for multi-class, linear for regression.
