---
title: Loss Functions
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are loss functions?

A **loss function** measures how wrong a model's predictions ($\hat{y}$) are compared to the true values ($y$), and boils it down to a single number. It's the compass of machine learning: during training, optimization algorithms like [gradient descent](./gradient_descent.md) follow the gradient of the loss to update the model's weights and shrink that number.

**The goal of training is to minimize the loss.**

:::note
Loss functions aren't just for deep learning. The same formulas are used to train and evaluate classical machine learning models. See [Evaluating Models](../fundamentals/evaluation.md).
:::

The examples below calculate each loss by hand to show how it works. In practice, frameworks compute the loss for you during training.

## Why this matters

The loss function defines what "good" means for your model. Training does exactly one thing: make this number smaller. Pick a loss that doesn't match your task, and the model will optimize perfectly for the wrong goal.

## Regression loss functions

Regression models predict continuous numbers. The main choice is how much to punish large errors (outliers) versus small ones.

All the regression examples use this data:

```python
import numpy as np

y_true = np.array([3.0, -0.5, 2.0, 7.0])
y_pred = np.array([2.5, 0.0, 2.0, 8.0])
```

### Mean squared error (MSE) / L2 loss

**Intuition:** Average the squared differences between predictions and actual values. Because errors are squared, large errors are punished far more than small ones, which makes MSE sensitive to outliers.

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

- $n$: The number of samples in the dataset or batch.
- $i$: The index of the current sample, from 1 to $n$.
- $y_i$: The true value for sample $i$.
- $\hat{y}_i$: The predicted value for sample $i$.

**Use it for:** Standard regression, where large errors are especially bad (for example, house price prediction).

```python
mse = np.mean((y_true - y_pred) ** 2)
print(f"MSE: {mse}")  # MSE: 0.375
```

### Mean absolute error (MAE) / L1 loss

**Intuition:** Average the absolute differences between predictions and actual values. Errors count in proportion to their size, so MAE is robust to outliers. The downside is that its gradient is constant, which can make training slow or unstable close to the minimum.

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} \lvert y_i - \hat{y}_i \rvert
$$

- $\lvert \cdot \rvert$: The absolute value, which makes every error positive whether the prediction was too high or too low.

**Use it for:** Noisy data with outliers you don't want to dominate training.

```python
mae = np.mean(np.abs(y_true - y_pred))
print(f"MAE: {mae}")  # MAE: 0.5
```

### Huber loss

**Intuition:** The best of both. Huber loss behaves like MSE when the error is small (smooth, stable convergence) and like MAE when the error is large (limiting the influence of outliers).

$$
L_\delta(y, \hat{y}) =
\begin{cases}
\frac{1}{2}(y - \hat{y})^2 & \text{if } \lvert y - \hat{y} \rvert \le \delta \\
\delta \left( \lvert y - \hat{y} \rvert - \frac{1}{2}\delta \right) & \text{otherwise}
\end{cases}
$$

- $\delta$ (delta): A threshold hyperparameter. Errors smaller than $\delta$ are treated like MSE; larger ones like MAE.

**Use it for:** Regression where outliers exist but you still want smooth training.

```python
import torch
import torch.nn as nn

loss_fn = nn.HuberLoss(delta=1.0)
loss = loss_fn(torch.tensor([2.5, 0.0, 2.0, 8.0]), torch.tensor([3.0, -0.5, 2.0, 7.0]))
print(f"Huber loss: {loss.item()}")  # Huber loss: 0.1875
```

## Classification loss functions

Classification models predict classes, usually as probabilities.

### Binary cross-entropy (BCE) / log loss

**Intuition:** Measures how well predicted probabilities (between 0 and 1) match binary labels. The penalty grows sharply as the predicted probability moves away from the true label. Being confidently wrong is punished hardest.

$$
\text{BCE} = -\frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
$$

- $y_i$: The true label for sample $i$, either 0 or 1.
- $\hat{y}_i$: The predicted probability that sample $i$ is class 1.
- $\log$: The natural logarithm.

Only one term is active for each sample: when $y_i = 1$ the loss is $-\log(\hat{y}_i)$, and when $y_i = 0$ it's $-\log(1 - \hat{y}_i)$.

**Use it for:** Binary classification (spam detection, medical diagnosis), with a sigmoid output layer.

```python
import torch
import torch.nn.functional as F

y_pred = torch.tensor([0.9, 0.1, 0.8])  # Predicted probabilities
y_true = torch.tensor([1.0, 0.0, 1.0])  # True labels

bce_loss = F.binary_cross_entropy(y_pred, y_true)
print(f"BCE loss: {bce_loss.item():.4f}")  # BCE loss: 0.1446
```

### Categorical cross-entropy (CCE)

**Intuition:** The multi-class version of binary cross-entropy. It compares the predicted probability distribution across $C$ classes with the true class, which is usually represented as a one-hot vector.

$$
\text{CCE} = -\frac{1}{n} \sum_{i=1}^{n} \sum_{c=1}^{C} y_{ic} \log(\hat{y}_{ic})
$$

- $C$: The number of classes.
- $c$: The index of the current class.
- $y_{ic}$: 1 if class $c$ is the correct class for sample $i$, otherwise 0.
- $\hat{y}_{ic}$: The predicted probability that sample $i$ belongs to class $c$ (usually from a softmax output).

Because $y_{ic}$ is 0 for every wrong class, the loss for each sample is just $-\log$ of the probability the model gave the *correct* class.

**Use it for:** Multi-class classification where each example belongs to exactly one class (for example, image classification).

```python
import torch
import torch.nn.functional as F

# Raw scores (logits) before softmax, and the correct class index for each sample
logits = torch.tensor([[2.0, 1.0, 0.1], [0.1, 2.5, 0.4]])
targets = torch.tensor([0, 1])

cce_loss = F.cross_entropy(logits, targets)  # Applies softmax internally
print(f"Categorical cross-entropy: {cce_loss.item():.4f}")  # 0.3051
```

### Hinge loss

**Intuition:** Designed for [support vector machines](../algorithms/support_vector_machines.md). It penalizes predictions that are wrong, *and* predictions that are right but not confident enough (inside the margin).

$$
L(y, \hat{y}) = \max(0, 1 - y \cdot \hat{y})
$$

- $y$: The true label, written as -1 or +1 (not 0 and 1).
- $\hat{y}$: The raw score from the classifier (its signed distance from the boundary), not a probability.
- $1$: The margin. If $y \cdot \hat{y} \ge 1$, the prediction is correct and confidently outside the margin, so the loss is 0.

**Use it for:** Maximum-margin classifiers like linear SVMs.

```python
import torch

y_pred = torch.tensor([0.8, -0.5, 1.2])  # Raw scores
y_true = torch.tensor([1.0, -1.0, 1.0])  # Labels in {-1, 1}

hinge_loss = torch.mean(torch.clamp(1 - y_true * y_pred, min=0))
print(f"Hinge loss: {hinge_loss.item():.4f}")  # Hinge loss: 0.2333
```

## Quick reference

| Task | Loss function | Key characteristic | Common framework name |
|------|---------------|--------------------|-----------------------|
| Regression | MSE (L2) | Heavily penalizes large errors; sensitive to outliers | `MSELoss` / `mean_squared_error` |
| Regression | MAE (L1) | Robust to outliers; constant gradient | `L1Loss` / `mean_absolute_error` |
| Regression | Huber | MSE for small errors, MAE for large ones | `HuberLoss` / `Huber` |
| Binary classification | Binary cross-entropy | Logarithmic penalty on probabilities | `BCELoss`, `BCEWithLogitsLoss` / `binary_crossentropy` |
| Multi-class classification | Categorical cross-entropy | Expects logits or probabilities across classes | `CrossEntropyLoss` / `categorical_crossentropy` |
| Classification (SVM) | Hinge | Enforces a confident margin | `Hinge` (Keras) |

## Common mistakes

### Pairing the loss with the wrong output

Each loss expects a particular kind of output. In PyTorch, `BCELoss` expects probabilities (after a sigmoid), while `BCEWithLogitsLoss` expects raw scores and applies the sigmoid itself.

```python
# Wrong: raw scores passed to a loss that expects probabilities
loss = nn.BCELoss()(raw_scores, targets)

# Correct (and more numerically stable)
loss = nn.BCEWithLogitsLoss()(raw_scores, targets)
```

### Using MSE for classification

MSE on predicted probabilities trains slowly and punishes confident mistakes too weakly. Use cross-entropy for classification.

### Mixing up label formats

Keras's `categorical_crossentropy` expects one-hot labels like `[0, 1, 0]`; `sparse_categorical_crossentropy` expects class numbers like `1`. Using the wrong one raises a shape error.

## Summary

- A loss function turns prediction errors into one number that training tries to minimize.
- For regression: MSE punishes big errors, MAE resists outliers, and Huber blends the two.
- For classification: binary cross-entropy for two classes, categorical cross-entropy for many, and hinge loss for SVMs.
- Match the loss to your output layer: sigmoid with binary cross-entropy, softmax with categorical cross-entropy.
