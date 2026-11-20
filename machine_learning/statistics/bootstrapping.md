---
title: Bootstrapping
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

## What is bootstrapping?

**Bootstrapping** is a resampling technique for estimating how much a statistic (like a mean) or a model's performance would vary if you could collect your data again. It's **non-parametric**, meaning it doesn't assume your data follows any particular distribution.

Gathering brand-new datasets from the real world is often expensive or impossible. Bootstrapping instead creates many simulated datasets, called **bootstrap samples**, by **sampling with replacement** from the data you already have.

## Why this matters

Many statistics, like the median or a model's F1-score, have no simple formula for their uncertainty. Bootstrapping gives you one anyway, using nothing but your data and a loop. It's also the core idea behind bagging and random forests, so understanding it makes those algorithms much less mysterious.

## Key characteristics

- **Sampling with replacement**: Each time a value is drawn from the original dataset of size $N$, it goes back into the pool. So a single data point can appear several times in one bootstrap sample, while other points don't appear at all.
- **Out-of-bag (OOB) observations**: On average, a bootstrap sample contains about 63.2% of the original unique data points. The remaining ~36.8% are called **out-of-bag** samples, and they're often used for validation.
- **Foundation of ensemble methods**: Bootstrapping is the "B" in **bagging** (bootstrap aggregating). It's the backbone of [random forests](../algorithms/random_forests.md), where many trees are each trained on a different bootstrap sample to reduce variance and overfitting.

Here's what sampling with replacement looks like on a tiny dataset:

```python
import numpy as np

np.random.seed(0)
data = np.array([10, 20, 30, 40, 50])
print(np.random.choice(data, size=len(data), replace=True))
```

**Output:**

```text
[50 10 40 40 40]
```

The value `40` appears three times, while `20` and `30` aren't drawn at all. Those two are this sample's out-of-bag points.

## Example: a confidence interval from scratch

This example uses bootstrapping to build a 95% confidence interval for the mean of a small dataset, using only NumPy.

```python
import numpy as np

data = np.array([45, 50, 52, 58, 60, 63, 70, 75, 80, 95])

np.random.seed(42)
n_iterations = 1000
bootstrap_means = []

for _ in range(n_iterations):
    # Draw a sample the same size as the data, with replacement
    sample = np.random.choice(data, size=len(data), replace=True)
    bootstrap_means.append(np.mean(sample))

# The middle 95% of bootstrap means forms the confidence interval
lower_bound = np.percentile(bootstrap_means, 2.5)
upper_bound = np.percentile(bootstrap_means, 97.5)

print(f"Original mean: {np.mean(data):.2f}")
print(f"Bootstrap 95% confidence interval: [{lower_bound:.2f}, {upper_bound:.2f}]")
```

**How it works:**

1. Draw 1,000 bootstrap samples from the original data.
2. Calculate the mean of each sample. This gives you a distribution of 1,000 plausible means.
3. Take the 2.5th and 97.5th percentiles of that distribution. The middle 95% is your confidence interval.

## Example: bootstrapping with scikit-learn

scikit-learn's `resample` function generates a bootstrap sample for features (`X`) and labels (`y`) together, keeping each row's feature and label aligned.

```python
import numpy as np
from sklearn.utils import resample

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([0, 0, 1, 1, 1])

X_boot, y_boot = resample(X, y, replace=True, n_samples=len(X), random_state=42)

print("Original X:\n", X)
print("\nBootstrap sample X (notice the repeated rows):\n", X_boot)
print("\nMatching bootstrap y:\n", y_boot)
```

## Common mistakes

### Sampling without replacement

A bootstrap sample must be drawn **with** replacement. Without it, every sample is just a shuffled copy of the original data and has the same mean every time.

```python
# Wrong: every "bootstrap" sample has exactly the same mean
np.random.choice(data, size=len(data), replace=False)

# Correct
np.random.choice(data, size=len(data), replace=True)
```

### Too few iterations

With only a handful of bootstrap samples, the confidence interval itself is noisy. Use at least 1,000 iterations, and more for tight intervals.

### Expecting bootstrapping to fix a bad sample

Bootstrapping can only resample the data you have. If your original sample is tiny or biased, the bootstrap inherits those problems.

## Summary

- Bootstrapping simulates new datasets by sampling your existing data with replacement.
- It estimates the uncertainty of a statistic without assuming a distribution.
- Each bootstrap sample leaves out about 36.8% of the data (the out-of-bag points), which can be used for validation.
- It's the foundation of bagging and random forests.
