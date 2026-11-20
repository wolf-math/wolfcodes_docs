---
title: XGBoost
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

## What is XGBoost?

**XGBoost** (Extreme Gradient Boosting) is an enhanced, high-performance version of [gradient boosting](./gradient_boosting.md). The core idea is the same, building trees one after another to correct earlier mistakes, but XGBoost adds several optimizations that make it faster and less prone to overfitting. It's a go-to choice for tabular data in industry and competitions.

Install it with `pip install xgboost`.

:::note
On macOS, XGBoost also needs the OpenMP runtime. If importing it fails with a `libomp.dylib` error, install it with `brew install libomp`.
:::

## Why this matters

XGBoost is what many teams reach for when a [random forest](./random_forests.md) isn't quite accurate enough. It's fast, handles missing values on its own, and has built-in protection against overfitting. Knowing how it differs from plain gradient boosting helps you understand its long list of hyperparameters.

## What XGBoost adds to gradient boosting

- **Regularization**: XGBoost includes $L_1$ (lasso) and $L_2$ (ridge) penalties that discourage overly complex trees, which helps prevent overfitting. See [regularization](../deep_learning/regularization.md).
- **Parallelization**: Trees are still built one after another, but XGBoost uses all your CPU cores to search for the best splits *within* each tree, which drastically speeds up training.
- **Built-in handling of missing values**: When a value is missing, XGBoost learns which branch it should go down during training, so you don't always need to impute first.
- **Smarter tree pruning**: Standard greedy algorithms stop splitting as soon as a split doesn't help. XGBoost grows trees to `max_depth` first, then prunes backward. That lets it keep a split that looks useless on its own but enables a valuable split below it.

## Example: predicting California house prices

Let's build a regression model on scikit-learn's **California housing dataset**. XGBoost provides a scikit-learn-compatible interface, so it plugs right into the usual workflow.

### Import the packages

```python
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
```

### Load the dataset

```python
housing = fetch_california_housing()
X, y = housing.data, housing.target  # Target: median house value in $100,000s
```

### Split the data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Train the model

```python
model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    objective='reg:squarederror',
    random_state=42,
)
model.fit(X_train, y_train)
```

### Evaluate the model

```python
y_pred = model.predict(X_test)

print(f"Mean squared error: {mean_squared_error(y_test, y_pred):.4f}")
print(f"R^2 score: {r2_score(y_test, y_pred):.4f}")
```

### Visualize the results

```python
plt.figure(figsize=(14, 6))

# Left: actual vs. predicted values
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.3, color='#2b5c8f', edgecolor='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect prediction')
plt.xlabel('Actual house value ($100k)')
plt.ylabel('Predicted house value ($100k)')
plt.title('Actual vs. Predicted Prices')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# Right: which features mattered most
plt.subplot(1, 2, 2)
xgb.plot_importance(
    model, ax=plt.gca(), max_num_features=6, importance_type='gain', show_values=False
)
plt.title('Top Feature Importance (Gain)')

plt.tight_layout()
plt.show()
```

The closer the points sit to the red dashed line, the more accurate the predictions.

## Key hyperparameters

XGBoost has many hyperparameters. These are the ones to tune first:

- **`n_estimators`**: The number of trees.
- **`learning_rate`**: How much each tree contributes.
- **`max_depth`**: The maximum depth of each tree.
- **`min_child_weight`**: The minimum amount of data needed in a leaf. Higher values make the model more conservative.
- **`subsample`**: The fraction of rows used to build each tree.

See [hyperparameter tuning](../fundamentals/hyperparameter_tuning.md) for what each one does and how to search for good values.

## Common mistakes

### Tuning everything at once

XGBoost has dozens of hyperparameters. Start with `learning_rate`, `n_estimators`, and `max_depth`, then move on to `min_child_weight` and `subsample` only if you need more.

### Skipping early stopping

Without early stopping, you have to guess `n_estimators`. Give the model a validation set and let it stop when the validation score stops improving.

```python
model = xgb.XGBRegressor(n_estimators=1000, learning_rate=0.05, early_stopping_rounds=20)
model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
print(model.best_iteration)
```

## Summary

- XGBoost is gradient boosting with added regularization, parallel split-finding, missing-value handling, and smarter pruning.
- It's fast, accurate, and a standard choice for tabular data.
- It works like any scikit-learn model: create it, `fit()`, then `predict()`.
- Tune `learning_rate`, `n_estimators`, and `max_depth` first.
