---
title: The Exploding Gradient Problem
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

## What is the exploding gradient problem?

The **exploding gradient problem** is the mirror image of the [vanishing gradient problem](./vanishing_gradient.md). Gradients grow exponentially large as they're passed backward through a network, so the weight updates become enormous. It's especially common in [recurrent neural networks](./overview.md) processing long sequences.

Huge updates throw the weights wildly off course, destroy what the network has learned, and often crash training with numerical overflow, showing up as `NaN` (not a number) values.

## Why this matters

Exploding gradients are one of the most common reasons a training run suddenly collapses into `NaN` values. The fix is usually simple, but only if you recognize the symptoms.

## The root cause

In a standard RNN, each hidden state is computed from the current input and the previous hidden state:

$$
h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)
$$

When training with [backpropagation](../backpropagation.md) through time (BPTT), the gradient flowing back from the last step to an earlier hidden state $h_k$ is a product of many factors, one per time step, each containing $W_{hh}$. Roughly, it behaves like raising $W_{hh}$ to a power:

$$
\frac{\partial \mathcal{L}}{\partial h_k} \propto \prod_{j=k+1}^{T} \frac{\partial h_j}{\partial h_{j-1}} \approx \left(W_{hh}\right)^{T-k}
$$

- If the largest eigenvalue of $W_{hh}$ (its strongest stretching factor) is **greater than 1**, repeated multiplication makes the gradient grow exponentially.
- Over a long sequence, this gets extreme fast: $1.2^{50}$ is over 9,000, and $1.5^{50}$ is over **630 million**.

When gradients that large reach the [optimizer](../optimizers.md), they trigger massive, erratic jumps in the weights, wiping out any useful patterns.

## An analogy: an over-amplifying supply chain

Imagine a company with **50 warehouses** arranged in a line. Each warehouse receives a demand forecast from the previous one, applies its own adjustment, and passes it on.

- **The multiplier**: Each warehouse manager is slightly optimistic and multiplies the forecast by 1.1 (a 10% increase).
- **A tiny correction**: At warehouse 1, an analyst adds a 1-unit correction for a rounding error.
- **The explosion**: That correction is multiplied by 1.1 at every one of the 50 steps. By warehouse 50, it has grown to $1.1^{50} \approx 117$ units.

The final warehouse is swamped by distorted noise. The same thing happens in an RNN: small gradient signals multiply uncontrollably across time steps until they overwhelm training.

## Symptoms

Exploding gradients are usually easy to spot:

1. **Sudden loss explosion**: The training loss decreases normally, then suddenly spikes to `inf` or `NaN`.
2. **Wild weights**: Weight values jump between huge positive and negative numbers.
3. **Broken predictions**: Outputs become random or degenerate, like repetitive garbage text or a constant prediction.

## Solutions

- **Gradient clipping**: The most direct fix. If the gradient's overall size (its norm) exceeds a threshold, scale it down before the update:

  $$
  \text{if } \lVert \mathbf{g} \rVert > \text{threshold}: \quad \mathbf{g} \leftarrow \frac{\text{threshold}}{\lVert \mathbf{g} \rVert} \, \mathbf{g}
  $$

  The gradient keeps its direction but can never be larger than the threshold. In Keras, it's a single optimizer argument:

  ```python
  import tensorflow as tf

  optimizer = tf.keras.optimizers.Adam(learning_rate=0.001, clipnorm=1.0)
  ```

- **Truncated BPTT**: Only backpropagate through a limited number of time steps. This keeps the product of factors short, at the cost of limiting long-term memory.
- **[LSTMs](./lstm.md) and [GRUs](./gru.md)**: Their gating mechanisms and additive memory updates keep gradients far more stable than in a plain RNN.
- **Careful weight initialization**: Initializing the recurrent weights as an **orthogonal** matrix keeps their eigenvalues close to 1, so gradients neither explode nor vanish at the start of training.

## Summary

- Exploding gradients happen when backpropagated gradients grow exponentially, usually because recurrent weights amplify the signal at every step.
- They show up as sudden `NaN` or infinite losses and wildly unstable weights.
- Gradient clipping is the standard, simple fix.
- LSTMs, GRUs, truncated BPTT, and orthogonal initialization also help.
