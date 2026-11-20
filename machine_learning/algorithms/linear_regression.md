---
title: Linear Regression
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is linear regression?

**Linear regression** models the relationship between a numeric target variable ($y$) and one or more input features ($X$) by fitting a straight line through the data. It's the simplest [supervised learning](../fundamentals/types_of_ml.md#supervised-learning) algorithm for predicting continuous numbers, and the foundation many other models build on.

## Why this matters

Linear regression is the baseline every regression model is compared against. It trains instantly, its weights tell you exactly how each feature affects the prediction, and many advanced models, including neural networks, are built from the same weighted-sum idea. If a complex model can't beat linear regression, it isn't worth its complexity.

## The model

With a single feature, the model is the equation of a line:

$$
y = mx + b
$$

- $y$: The predicted target value (for example, house price).
- $x$: The input feature (for example, square footage).
- $m$: The **slope**, often written $w$ for **weight**. It's how much $y$ changes when $x$ increases by one unit.
- $b$: The **bias** or **intercept**. It's the predicted value of $y$ when $x = 0$.

With more features, each one gets its own weight, and the line becomes a flat **hyperplane**: $y = w_1x_1 + w_2x_2 + \dots + w_nx_n + b$.

## How the best line is chosen

To find the best-fitting line, the algorithm minimizes the **mean squared error (MSE)**, which acts as its **cost function**:

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

- $y_i$ is the actual value.
- $\hat{y}_i$ is the predicted value.
- $n$ is the number of samples.

scikit-learn solves this directly with **ordinary least squares (OLS)**: a formula that calculates the exact best $w$ and $b$ in one step, without any iterative training loop.

## Example: predicting house prices

This example uses NumPy to create data, scikit-learn to train the model, and Matplotlib to visualize the result.

### Import the packages

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
```

:::note
If these packages aren't installed in your environment, install them with `pip`. Note that scikit-learn is installed as `pip install scikit-learn` but imported as `sklearn`.
:::

### Create the data

```python
X = np.array([[12], [15], [18], [20], [22], [25], [28], [30], [35], [40]])
y = np.array([155, 185, 215, 245, 275, 310, 345, 370, 430, 495])
```

- `X`: House size in hundreds of square feet (15 means 1,500 sq. ft.).
- `y`: House price in thousands of dollars (185 means \$185,000).

`X` is a 2D array (one row per house, one column per feature) because scikit-learn always expects features in that shape, even when there's only one.

### Train the model

```python
model = LinearRegression()
model.fit(X, y)
```

### Inspect the learned parameters

```python
weight = model.coef_[0]
bias = model.intercept_

print(f"Learned weight (price increase per 100 sq. ft.): ${weight * 1000:,.2f}")
print(f"Learned bias (baseline price): ${bias * 1000:,.2f}")
```

The weight tells you how much each extra 100 square feet adds to the price. That's one of linear regression's biggest strengths: the model is easy to interpret.

### Make predictions

Now let's predict prices for a 1,600 sq. ft. house and a 3,200 sq. ft. house:

```python
houses_to_predict = np.array([[16], [32]])
predicted_prices = model.predict(houses_to_predict)

for size, price in zip(houses_to_predict, predicted_prices):
    print(f"Predicted price for a {size[0] * 100} sq. ft. house: ${price * 1000:,.2f}")
```

### Evaluate the model

```python
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"R-squared: {r2:.4f} (explains {r2 * 100:.1f}% of price variance)")
print(f"Root mean squared error: ${rmse * 1000:,.2f}")
```

Two metrics are especially useful for linear regression:

- **$R^2$ (coefficient of determination)**: Usually between 0 and 1. An $R^2$ of 0.95 means 95% of the variation in house prices is explained by square footage.
- **Root mean squared error (RMSE)**: The typical size of a prediction error, in the target's original units (here, dollars).

:::warning
This example evaluates on the same data it trained on, to keep things short. In a real project, split your data into training and test sets and evaluate on the test set. See [Evaluating Models](../fundamentals/evaluation.md).
:::

### Plot the model

```python
X_range = np.array([[10], [42]])
y_line = model.predict(X_range)

plt.figure(figsize=(9, 6))
plt.scatter(X * 100, y * 1000, color='royalblue', s=70, edgecolors='k', label='Actual sales')
plt.plot(X_range * 100, y_line * 1000, color='crimson', linewidth=2.5, label='Linear regression fit')
plt.scatter(
    houses_to_predict * 100, predicted_prices * 1000,
    color='darkorange', s=100, zorder=5, label='New predictions',
)

plt.title('House Price vs. Square Footage')
plt.xlabel('Square footage (sq. ft.)')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
```

## When to use linear regression

- **Use it** as your first baseline for any numeric prediction problem, and whenever you need a model you can explain.
- **It works best** when the relationship between features and target is roughly a straight line.
- **Avoid it** when the relationship is strongly curved or full of interactions, unless you engineer features (like squared terms) to capture them. Tree-based models like [gradient boosting](./gradient_boosting.md) handle those cases more naturally.

## Common mistakes

### Passing a 1D array as features

scikit-learn expects `X` to be 2D (rows × features), even with a single feature.

```python
# Wrong: 1D array raises a ValueError
X = np.array([12, 15, 18])

# Correct: one column per feature
X = np.array([[12], [15], [18]])
# Or reshape an existing 1D array
X = np.array([12, 15, 18]).reshape(-1, 1)
```

### Using it on clearly curved relationships

A straight line can't fit a curve, no matter how much data you add. Plot your data first. If the relationship bends, add features (like $x^2$) or use a non-linear model.

### Predicting far outside the training range

The model learned from houses between 1,200 and 4,000 sq. ft. Its prediction for a 20,000 sq. ft. mansion is a guess extended along a straight line, not something the data supports.

## Summary

- Linear regression fits a line (or hyperplane) to predict a continuous number.
- It learns one weight per feature plus a bias, chosen to minimize mean squared error.
- Evaluate it with $R^2$ (variance explained) and RMSE (typical error size).
- It's fast, interpretable, and the right first baseline for regression problems.
