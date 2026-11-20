---
title: Gradient Boosting
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

## What is gradient boosting?

**Gradient boosting** is one of the most powerful and widely used techniques for structured (tabular) data. Like [random forests](./random_forests.md), it's an **ensemble method**: it combines many **weak learners** (usually shallow decision trees) into a single, highly accurate **strong learner**.

The difference is *how* the trees are built:

- **Random forests** build trees **in parallel**, each on its own bootstrap sample, and average them.
- **Gradient boosting** builds trees **one after another**. Each new tree is trained specifically to correct the mistakes (the **residuals**) of all the trees before it.

## Why this matters

Gradient boosting and its descendants (XGBoost, LightGBM, CatBoost) win more tabular-data competitions than any other approach, and power ranking, pricing, and risk models across the industry. Understanding the "fit the residuals" idea makes all of those libraries easier to use and tune.

## How gradient boosting works

1. **Start with a baseline prediction**: Usually the average of the target for regression (or the log-odds for classification).
2. **Compute the residuals**: For every data point, calculate how far off the current prediction is. Technically these are **pseudo-residuals**: the negative gradient of the loss function. With mean squared error, they're simply the actual value minus the predicted value ($y - \hat{y}$).
3. **Fit a weak learner to the residuals**: Train a shallow decision tree to predict those residuals, not the original target.
4. **Update the predictions**: Scale the new tree's predictions by a **learning rate** (also called **shrinkage**) and add them to the running total.
5. **Repeat**: Go back to step 2 for a set number of trees, or until the predictions stop improving.

Each tree nudges the predictions a little closer to the truth. The small learning rate keeps any single tree from overcorrecting.

## Example: building gradient boosting by hand

To make the mechanics clear, let's build a small gradient booster from scratch using NumPy and scikit-learn's decision trees. We'll watch how each new tree gradually fits a curved relationship between square footage and house price.

### Import the packages

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor
```

### Create the data

```python
np.random.seed(42)
n_samples = 150

X = np.sort(np.random.uniform(500, 4500, n_samples))  # Square footage

# A non-linear relationship with some noise
y = 50000 + 150 * X + 50000 * np.sin(X / 500) + np.random.normal(0, 15000, n_samples)

X = X.reshape(-1, 1)
```

### Set the hyperparameters

```python
n_estimators = 5     # Number of trees
learning_rate = 0.3  # How much each tree contributes
```

### Make the initial prediction

The starting prediction is just the mean of `y` for every house.

```python
init_pred = np.mean(y)
predictions = np.full(shape=y.shape, fill_value=init_pred)
```

### Plot the starting point

```python
plt.figure(figsize=(14, 10))

plt.subplot(3, 2, 1)
plt.scatter(X, y, color='black', alpha=0.6, s=20, label='Actual data')
plt.plot(X, predictions, color='red', lw=2, label='Initial prediction (mean)')
plt.title('Step 0: Initial baseline')
plt.legend(loc='upper left', fontsize=8)
```

### Run the boosting loop

```python
trees = []

for i in range(n_estimators):
    # 1. Calculate residuals (the negative gradient for MSE)
    residuals = y - predictions

    # 2. Fit a shallow tree to the residuals
    tree = DecisionTreeRegressor(max_depth=3, random_state=42 + i)
    tree.fit(X, residuals)
    trees.append(tree)

    # 3. Nudge predictions toward the target, scaled by the learning rate
    predictions += learning_rate * tree.predict(X)

    # Plot the ensemble after this tree
    plt.subplot(3, 2, i + 2)
    plt.scatter(X, y, color='black', alpha=0.4, s=15, label='Actual data')
    plt.plot(X, predictions, color='blue', lw=2, label=f"Ensemble after tree {i + 1}")
    plt.title(f"Boosting iteration {i + 1}")
    plt.legend(loc='upper left', fontsize=8)

plt.tight_layout()
plt.show()
```

In the plots, the flat red baseline gradually bends into a curve that follows the data, one small correction at a time.

## Example: using scikit-learn's implementation

In practice, you don't write the loop yourself. scikit-learn provides optimized `GradientBoostingRegressor` and `GradientBoostingClassifier` classes. This example reuses `X` and `y` from above.

### Import the packages

```python
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
```

### Split the data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Train the model

```python
gbr = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42,
)
gbr.fit(X_train, y_train)
```

### Evaluate the model

```python
y_pred = gbr.predict(X_test)

print(f"R^2 score: {r2_score(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):,.2f}")
```

## Key hyperparameters

- **`n_estimators`**: The number of trees. More trees fit the training data more closely.
- **`learning_rate`**: How much each tree contributes. Smaller values need more trees but usually generalize better.
- **`max_depth`**: The depth of each tree. Boosting typically uses shallow trees (depth 3 to 6).

**Rule of thumb:** `learning_rate` and `n_estimators` work together. If you lower the learning rate, raise the number of trees.

## Common mistakes

### A high learning rate with many trees

Each tree corrects the previous ones. With a large learning rate and hundreds of trees, the model quickly starts fitting noise.

```python
# Risky: big steps, many trees, deep trees
GradientBoostingRegressor(learning_rate=1.0, n_estimators=500, max_depth=8)

# Safer: small steps, shallow trees
GradientBoostingRegressor(learning_rate=0.05, n_estimators=500, max_depth=3)
```

### Not checking for overfitting as trees are added

Monitor validation error as you add trees, and stop when it stops improving. scikit-learn's `n_iter_no_change` and XGBoost's early stopping do this for you.

## Summary

- Gradient boosting builds trees one after another, each fixing the errors of the ones before.
- Each tree is fit to the residuals (the negative gradient of the loss), scaled by a learning rate, and added to the ensemble.
- It's often the most accurate algorithm for tabular data, but it's more sensitive to hyperparameters than a random forest.
- [XGBoost](./xgboost.md) is a faster, regularized version used widely in practice.
