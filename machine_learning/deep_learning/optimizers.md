---
title: Optimizers
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are optimizers?

An **optimizer** is the algorithm that updates a neural network's weights and biases to minimize the [loss function](./loss_functions.md). It decides how big a step to take and in which direction, every time the network learns from a batch of data.

A network learns by making predictions and comparing them to the true answers. The loss function measures the gap, [backpropagation](./backpropagation.md) calculates the gradients, and the optimizer uses those gradients to adjust the parameters. Without an optimizer, the model would know it was wrong but not how to improve.

## Why this matters

The optimizer decides how quickly and how reliably your network learns. The same model can converge in minutes with a good optimizer, or crawl and stall with a poor one. Fortunately, a few sensible defaults cover most situations.

## How optimizers work

1. **Compute the loss**: The model makes predictions, and the loss function measures the error.
2. **Compute the gradients**: Backpropagation calculates how much each weight contributed to the loss.
3. **Update the parameters**: The optimizer applies its update rule to adjust each weight and bias.

These steps repeat for every batch, across many [epochs](./intro.md#epochs-batches-and-iterations), until the model **converges** (the loss stops improving).

All the optimizers below are variations on [gradient descent](./gradient_descent.md). They differ in how they use the gradients to choose each step.

## Types of optimizers

### Batch gradient descent

- **How it works:** Computes the gradient over the *entire* dataset before making a single update.
- **Strengths:** The gradient points in the exact true direction. It's guaranteed to find the global minimum for convex (bowl-shaped) loss surfaces, and a local minimum otherwise.
- **Limitations:** Extremely slow and memory-hungry for modern datasets, since every single step requires processing all the data.

### Mini-batch gradient descent (SGD)

- **How it works:** Splits the data into small batches (for example, 32, 64, or 128 examples) and updates the weights after each batch. This is what deep learning frameworks call **stochastic gradient descent (SGD)**.
- **Strengths:** Balances efficiency with stability. The slightly noisy gradients can even help the model escape shallow local minima and saddle points.

### Momentum-based optimizers

Plain SGD can zigzag back and forth across steep, narrow valleys in the loss landscape while making slow progress along the valley floor. Momentum fixes this by giving the updates velocity.

- **Classic momentum:** Think of a ball rolling downhill, picking up speed. Each update adds a fraction ($\beta$) of the previous update to the current gradient step. Zigzags cancel out, while consistent downhill directions build up speed.
- **Nesterov accelerated gradient (NAG):** Momentum that "looks ahead." It computes the gradient at the position the momentum is about to carry it to, rather than where it is now. That lets it notice an upcoming overshoot and brake early.

### Adaptive optimizers

Adaptive optimizers give **each parameter its own learning rate**, adjusted automatically based on that parameter's history of gradients. Parameters that get large, frequent updates slow down; rarely updated parameters get bigger steps.

- **AdaGrad (adaptive gradient):**
  - Divides each parameter's step by the accumulated sum of its past squared gradients.
  - **Limitation:** That sum only ever grows, so the effective learning rate keeps shrinking until training stalls.
- **RMSprop (root mean square propagation):**
  - Fixes AdaGrad by using an *exponential moving average* of squared gradients instead of a running sum, so old gradients fade out. The learning rate stays responsive throughout training.
- **Adam (adaptive moment estimation):**
  - Combines momentum (a moving average of gradients) with RMSprop (a moving average of squared gradients), plus bias corrections for the first few steps. It's the classic general-purpose default.
- **AdamW (Adam with decoupled weight decay):**
  - Adam with **weight decay** applied directly to the weights. Plain Adam with an L2 penalty mixes the penalty into the gradient, where the adaptive learning rates weaken it; decoupling it works better. It's the standard choice for training Transformers and large language models.

## Choosing an optimizer

1. **General prototyping:** **Adam** or **AdamW**. If you're not sure where to start, AdamW is the safest bet. It converges quickly and works well across most architectures.
2. **Transformers and large language models:** **AdamW**. Proper weight decay is critical for attention-based models like BERT, GPT, and Vision Transformers.
3. **Classic computer vision (CNNs):** **SGD with momentum**, with a good learning rate schedule (like cosine annealing). Adam converges faster, but well-tuned SGD with momentum often reaches slightly better final accuracy on image classification.
4. **Recurrent networks and reinforcement learning:** **RMSprop** or **Adam**. They handle the rapidly changing gradients of these problems well.

**Rule of thumb:** Start with Adam or AdamW at a learning rate of 0.001. Only switch if you have a specific reason.

## Example: training a network with an optimizer

This example builds a small network in Keras and trains it with AdamW.

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Synthetic data: 1,000 samples with 20 features each, binary labels
X_train = np.random.randn(1000, 20).astype(np.float32)
y_train = np.random.randint(0, 2, size=(1000, 1)).astype(np.float32)

# 2. Build the network
model = models.Sequential([
    layers.Input(shape=(20,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

# 3. Choose the optimizer
optimizer = tf.keras.optimizers.AdamW(learning_rate=0.001, weight_decay=0.01)

# 4. Compile: attach the optimizer, loss function, and metrics
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

# 5. Train
history = model.fit(
    X_train,
    y_train,
    epochs=5,              # Complete passes through the data
    batch_size=32,         # Mini-batch size
    validation_split=0.2,  # Hold out 20% for validation
)
```

:::note
The labels here are random, so the model can't learn anything meaningful. The point of the example is the workflow. Swap in real data to see the optimizer at work.
:::

### Swapping optimizers

Keras keeps the optimizer separate from the model architecture, so trying a different one only means changing one line:

```python
# SGD with momentum
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)

# Nesterov accelerated gradient
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

# RMSprop
optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001, rho=0.9)

# Adam
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
```

For the full list, see the [Keras optimizers documentation](https://keras.io/api/optimizers/).

## Summary

- Optimizers use gradients to update a network's weights and minimize the loss.
- Momentum smooths and accelerates updates; adaptive optimizers give each parameter its own learning rate.
- Adam and AdamW are the standard defaults; SGD with momentum is still popular for CNNs.
- Start with Adam or AdamW at a learning rate of 0.001.
