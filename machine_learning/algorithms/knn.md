---
title: K-Nearest Neighbors
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

## What is k-nearest neighbors?

**K-nearest neighbors (KNN)** predicts the label of a new data point by looking at the $K$ training points closest to it. It can be used for both classification and regression. KNN is:

- **Non-parametric**: It makes no assumptions about the shape of the data (unlike linear regression, which assumes a straight-line relationship).
- **A lazy learner**: It doesn't learn anything during training. It simply memorizes the dataset and does all the work when you ask for a prediction. See [Lazy vs Eager Learning](../fundamentals/lazy_vs_eager_learning.md).

## Why this matters

KNN is the most intuitive algorithm in machine learning: "you're probably like your neighbors." It needs no training, works for both classification and regression, and makes a handy baseline. It's also a great way to understand why feature scaling and the curse of dimensionality matter for every distance-based method.

## How KNN works

1. **Choose $K$**: Decide how many neighbors to consider (for example, $K = 5$).
2. **Calculate distances**: Measure the distance from the new point to every point in the training set.
3. **Find the neighbors**: Pick the $K$ closest training points.
4. **Vote or average**:
   - For **classification**, predict the most common class among the $K$ neighbors (majority vote).
   - For **regression**, predict the average of the neighbors' values.

**Choosing $K$:** A small $K$ (like 1) follows the training data very closely and overfits to noise. A large $K$ smooths things out but can blur real boundaries. Odd values avoid ties in two-class problems.

## Example: predicting premium subscriptions

Imagine an online store that wants to predict whether a customer will subscribe to a premium membership, based on two features:

1. Age (years)
2. Monthly spending (dollars)

### Import the packages

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
```

### Create the dataset

`make_classification` generates synthetic data, which we then rescale to realistic ranges: ages around 20 to 65 and monthly spending around \$50 to \$550.

```python
X, y = make_classification(
    n_samples=300,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    weights=[0.6, 0.4],
    random_state=42,
)

X[:, 0] = X[:, 0] * 12 + 40   # Age
X[:, 1] = X[:, 1] * 120 + 250  # Monthly spending ($)
```

### Split the data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Scale the features

:::important
Feature scaling is critical for KNN. Distances are dominated by whichever feature has the largest numbers. Without scaling, two customers who differ by \$300 in monthly spending look 10 times farther apart than two customers who differ by 30 years in age.
:::

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Train the classifier

```python
k = 5
knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
knn.fit(X_train_scaled, y_train)  # Just stores the data
```

### Evaluate the model

```python
y_pred = knn.predict(X_test_scaled)

print(f"Accuracy with K={k}: {accuracy_score(y_test, y_pred):.2%}\n")
print(classification_report(y_test, y_pred, target_names=['Free tier', 'Premium']))
```

### Plot the decision boundary

```python
plt.figure(figsize=(10, 6))

x_min, x_max = X_train_scaled[:, 0].min() - 1, X_train_scaled[:, 0].max() + 1
y_min, y_max = X_train_scaled[:, 1].min() - 1, X_train_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

Z = knn.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)

scatter = plt.scatter(
    X_train_scaled[:, 0], X_train_scaled[:, 1],
    c=y_train, cmap=plt.cm.coolwarm, edgecolor='k', s=50,
)
plt.title(f"KNN Decision Boundary (K = {k})")
plt.xlabel('Age (scaled)')
plt.ylabel('Monthly spending (scaled)')
plt.legend(*scatter.legend_elements(), title='Segment', loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

Unlike [logistic regression](./logistic_regression.md), the boundary can curve and bend to follow local clusters of points.

## When to use KNN

- **Use it** for small to medium datasets where you want a simple, flexible baseline with no training time.
- **Use it** when similar examples really should have similar labels (recommendations, simple pattern matching).
- **Avoid it** for large datasets (predictions get slow) or data with many features (distances become meaningless in high dimensions).

## Common mistakes

### Forgetting to scale features

Without scaling, KNN's notion of "nearest" is dominated by whichever feature has the biggest numbers.

```python
# Wrong: distances are dominated by spending (hundreds) over age (tens)
knn.fit(X_train, y_train)

# Correct: put features on the same scale first
scaler = StandardScaler()
knn.fit(scaler.fit_transform(X_train), y_train)
```

### Fitting the scaler on the test set

Use `fit_transform()` on the training data and only `transform()` on the test data. Refitting on the test set changes the scale and leaks information.

### Picking K without testing it

`K=5` is a default, not a rule. Try several values with cross-validation and pick the one that scores best.

## Summary

- KNN predicts by looking at the $K$ closest training points: majority vote for classification, average for regression.
- It's a lazy learner: training is instant, predictions are slow.
- Always scale your features, because KNN depends entirely on distances.
- Tune $K$ to balance overfitting (small $K$) against oversmoothing (large $K$).
