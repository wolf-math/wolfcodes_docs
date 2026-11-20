---
title: Gradient Descent
sidebar_position: 8
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is gradient descent?

**Gradient descent** is an iterative optimization algorithm for finding the minimum of a function. In machine learning, it's the engine behind training: it starts a model with random parameters (weights and biases), measures how wrong its predictions are with a [loss function](./loss_functions.md), and repeatedly adjusts the parameters to make the loss smaller.

A useful picture: imagine standing on a foggy hillside, trying to reach the valley floor. You can't see the bottom, but you can feel which way the ground slopes under your feet. So you take a step downhill, check the slope again, and repeat. The **gradient** is the slope, and the valley floor is the lowest possible loss.

## Why this matters

Almost every model you train, from [logistic regression](../algorithms/logistic_regression.md) to large neural networks, is optimized with some form of gradient descent. Understanding the learning rate and the batch size, its two most important settings, helps you fix training that's too slow or doesn't converge at all.

## How it works

1. **Start** with random weights and biases.
2. **Calculate the loss**: how wrong the predictions are with the current parameters.
3. **Calculate the gradient**: the derivative of the loss with respect to each parameter. It points in the direction where the loss *increases* fastest. [Backpropagation](./backpropagation.md) is how neural networks compute it.
4. **Update every parameter** by stepping in the opposite direction of its gradient:

   $$
   w_{\text{new}} = w_{\text{old}} - \alpha \frac{\partial \text{Loss}}{\partial w}
   $$

5. **Repeat** steps 2 to 4 until the loss stops improving.

## The learning rate

The **learning rate** ($\alpha$) is a [hyperparameter](../fundamentals/hyperparameter_tuning.md) that sets how big each step is:

- **Too high**: You overshoot the bottom, bouncing back and forth across the valley or even climbing out of it (the loss **diverges**).
- **Too low**: Your steps are tiny, so training takes forever or gets stuck before reaching the bottom.

Common starting values are between 0.1 and 0.0001.

## Example: gradient descent from scratch

Let's use gradient descent to fit a line, $\hat{y} = wx + b$, to some data. The loss is mean squared error.

```python
import numpy as np

# Data that follows y = 2x + 1
X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([3.0, 5.0, 7.0, 9.0, 11.0])

w, b = 0.0, 0.0      # Start with arbitrary parameters
learning_rate = 0.05

for epoch in range(1000):
    y_pred = w * X + b
    error = y_pred - y

    # Gradients of MSE with respect to w and b
    dw = 2 * np.mean(error * X)
    db = 2 * np.mean(error)

    # Step downhill
    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 200 == 0:
        print(f"Epoch {epoch}: loss = {np.mean(error ** 2):.4f}")

print(f"Learned w = {w:.3f}, b = {b:.3f}")  # Close to w = 2, b = 1
```

The loss drops steadily, and the learned parameters approach the true values $w = 2$ and $b = 1$. Try changing `learning_rate` to `0.1` to see what happens when the steps are too large.

## The three flavors of gradient descent

The variants differ in how much data they use to calculate each gradient:

| Variant | Data per step | Pros | Cons |
|---------|---------------|------|------|
| **Batch gradient descent** | The entire dataset | Exact, smooth path toward the minimum | Very slow, or impossible to fit in memory, for large datasets |
| **Stochastic gradient descent (SGD)** | One random example | Fast updates; the noise can help escape shallow local minima | Very noisy; the loss bounces around instead of descending smoothly |
| **Mini-batch gradient descent** | A small batch (for example, 32, 64, or 128 examples) | The industry standard: efficient and reasonably stable | Batch size is one more thing to tune |

:::note
In deep learning frameworks, "SGD" almost always means mini-batch gradient descent. When you call `model.fit(..., batch_size=32)` in Keras, you're using mini-batches of 32.
:::

## Common mistakes

### A learning rate that's too high

If the loss jumps around wildly, increases, or turns into `nan`, the steps are too big. Divide the learning rate by 10 and try again.

### Not scaling the input features

When one feature ranges from 0 to 1 and another from 0 to 100,000, the loss surface becomes a long, narrow valley that gradient descent zigzags across. Standardize your features first.

### Stopping too early

A loss that's still clearly decreasing means the model hasn't finished learning. Plot the loss over [epochs](./intro.md#epochs-batches-and-iterations) before deciding training is done.

## Summary

- Gradient descent minimizes the loss by repeatedly stepping in the opposite direction of the gradient.
- The learning rate controls the step size: too high diverges, too low crawls.
- Mini-batch gradient descent is the standard balance of speed and stability.
- [Optimizers](./optimizers.md) like Adam build on gradient descent with smarter step sizes.
