---
title: Backpropagation
sidebar_position: 7
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is backpropagation?

**Backpropagation** (short for "backward propagation of errors") is the algorithm used to train neural networks. If a network's layers are its anatomy, backpropagation is its nervous system: it lets the network learn from its mistakes by working out how to adjust every weight and bias to reduce the error.

## Why this matters

Backpropagation is what makes training deep networks practical. It computes the gradient for millions of weights in a single backward pass, instead of testing each weight separately. Understanding it also explains common training problems like vanishing and [exploding gradients](./rnn/exploding_gradient.md).

## How backpropagation works

Backpropagation relies on calculus, specifically the **chain rule**, and has three stages:

1. **Calculate the loss**: Compare the network's prediction ($\hat{y}$) with the true label ($y$) using a [loss function](./loss_functions.md). This gives one number representing the total error.
2. **Compute the gradients**: Work backward from the output layer to the input layer. At each neuron, calculate the partial derivative of the loss with respect to its weights and bias. This tells you how much each parameter contributed to the error, and in which direction it should move.
3. **Update the weights**: Move each weight and bias a small step in the *opposite* direction of its gradient, scaled by the **learning rate** ($\alpha$):

   $$
   w_{\text{new}} = w_{\text{old}} - \alpha \frac{\partial L}{\partial w}
   $$

Step 3 is [gradient descent](./gradient_descent.md). Backpropagation's job is step 2: computing all those gradients efficiently.

## The chain rule, intuitively

A weight deep inside the network doesn't affect the loss directly. It affects its neuron's output, which affects the next layer, which eventually affects the prediction, which affects the loss. The chain rule says you can find the total effect by multiplying the effects of each link in that chain:

$$
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w}
$$

Backpropagation computes these factors starting at the output and reuses them as it moves backward, so it never recalculates the same thing twice.

## Example: one backward step

This continues the fraud-detection example from [forward propagation](./forward_propagation.md). There, the network looked at a transaction and produced:

- **Prediction**: $\hat{y} \approx 0.837$ (about an 84% chance of fraud).
- **Actual outcome**: The transaction really was fraud, so $y = 1$.

The hidden neurons output $a_A = 0.705$ and $a_B = 0.86$, and the output neuron had weights $w_{out1} = 1.2$, $w_{out2} = 1.5$ and bias $b_{out} = -0.5$.

### Step 1: calculate the loss

Using a simple squared-error loss, $L = \frac{1}{2}(\hat{y} - y)^2$:

$$
L = \frac{1}{2}(0.837 - 1)^2 = \frac{1}{2}(-0.163)^2 \approx 0.0133
$$

The goal is to change the weights so this number shrinks toward zero.

### Step 2: compute the gradients for the output layer

Work through the chain rule one link at a time:

1. **How the loss changes with the prediction:**

   $$
   \frac{\partial L}{\partial \hat{y}} = \hat{y} - y = 0.837 - 1 = -0.163
   $$

   It's negative, which means increasing $\hat{y}$ would *reduce* the loss.

2. **How the prediction changes with $z_{out}$:** The derivative of the sigmoid is $\hat{y}(1 - \hat{y})$:

   $$
   \frac{\partial \hat{y}}{\partial z_{out}} = 0.837 \times (1 - 0.837) \approx 0.136
   $$

3. **Combine them** into the output neuron's error signal, often written $\delta$:

   $$
   \delta = -0.163 \times 0.136 \approx -0.0222
   $$

4. **How $z_{out}$ changes with each weight:** Since $z_{out} = w_{out1} a_A + w_{out2} a_B + b_{out}$, the derivative with respect to each weight is just its input:

   $$
   \frac{\partial L}{\partial w_{out1}} = \delta \cdot a_A = -0.0222 \times 0.705 \approx -0.0157
   $$

   $$
   \frac{\partial L}{\partial w_{out2}} = \delta \cdot a_B = -0.0222 \times 0.86 \approx -0.0191
   $$

### Step 3: update the weights

With a learning rate of $\alpha = 0.1$:

$$
w_{out1} = 1.2 - 0.1 \times (-0.0157) \approx 1.2016
$$

$$
w_{out2} = 1.5 - 0.1 \times (-0.0191) \approx 1.5019
$$

Both gradients were negative, so both weights *increase*. That pushes the prediction up toward the correct answer of 1. Run the forward pass again with the new weights (and the similarly updated bias) and the loss drops slightly, from 0.01329 to 0.01318.

The change is tiny, and that's intentional. Small, careful steps repeated over many examples are more stable than big jumps.

### Continuing backward

The same process continues into the hidden layer. The output neuron's error signal $\delta$ is passed back through the weights $w_{out1}$ and $w_{out2}$ to tell neurons A and B how much they contributed to the error. Each hidden neuron then computes gradients for its own weights in exactly the same way. That backward flow of error signals is what gives backpropagation its name.

## The training loop: forward + backward

Training repeats two steps over the whole dataset, often millions of times:

1. **Forward pass**: Make a prediction.
2. **Backward pass**: Measure the error and adjust every weight a little.

In the fraud example, this loop gradually turns a network that starts with random guesses into a precise system that catches sophisticated fraud patterns in milliseconds.

:::tip
You'll almost never write backpropagation by hand. Frameworks like TensorFlow and PyTorch compute all the gradients automatically (called **automatic differentiation**) when you call `model.fit()` or `loss.backward()`.
:::

## Summary

- Backpropagation computes how much each weight and bias contributed to the loss.
- It uses the chain rule, working backward from the output layer and reusing results along the way.
- Gradient descent then moves each parameter a small step against its gradient.
- Forward pass, loss, backward pass, update: repeated many times, this is how neural networks learn.
