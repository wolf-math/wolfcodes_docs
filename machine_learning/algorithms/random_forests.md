---
title: Random Forests
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

## What is a random forest?

A **random forest** is an **ensemble** method: it combines many models to make one better prediction. Specifically, it trains a large number of [decision trees](./decision_trees.md) and combines their outputs:

- For **classification**, the forest predicts the class most trees vote for (the mode).
- For **regression**, it predicts the average of all the trees' predictions.

A single decision tree overfits easily. Averaging many slightly different trees cancels out much of that [overfitting](../deep_learning/regularization.md), which makes random forests one of the most reliable algorithms for tabular data.

## Why this matters

Random forests are one of the most reliable "first serious model" choices for tabular data. They're accurate out of the box, hard to overfit badly, need no [feature scaling](../fundamentals/feature_engineering.md#scaling), and tell you which features matter. When you need a strong result quickly, a random forest is often the answer.

## How random forests work

Random forests make their trees different from each other in two ways:

- **Bootstrap aggregating (bagging)**: Each tree is trained on its own **bootstrap sample**: a random sample of the training data, drawn with replacement. See [bootstrapping](../statistics/bootstrapping.md) for how this works.
- **Feature randomness**: At each split, a tree only considers a random subset of the features, rather than all of them. This **decorrelates** the trees: they can't all lean on the same strongest feature, so their mistakes are less likely to line up.

Then they combine the results:

- **Majority voting**: For classification, every tree votes for a class, and the class with the most votes wins.

## Example: predicting customer churn

Imagine you work for a subscription streaming service. You want to predict whether a customer is likely to cancel (**churn = 1**) or stay (**churn = 0**), based on behavioral features like:

- Tenure (months with the company)
- Monthly charges
- Support tickets per month
- Streaming hours per week
- Age

### Import the packages

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
```

### Create the dataset

```python
X, y = make_classification(
    n_samples=2000,
    n_features=5,
    n_informative=4,
    n_redundant=1,
    random_state=42,
)

feature_names = [
    'Tenure (months)',
    'Monthly charges ($)',
    'Support tickets/mo',
    'Streaming hours/wk',
    'Age',
]
```

### Split the data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Train the random forest

```python
rf_classifier = RandomForestClassifier(
    n_estimators=100,  # Number of trees in the forest
    max_depth=6,       # Maximum depth of each tree
    random_state=42,
    n_jobs=-1,         # Use all available CPU cores
)
rf_classifier.fit(X_train, y_train)
```

### Evaluate the predictions

```python
y_pred = rf_classifier.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(classification_report(y_test, y_pred, target_names=['Retained', 'Churned']))
```

### Plot feature importances

Random forests can tell you how much each feature contributed to their decisions. This is one of their most useful practical features.

```python
importances = rf_classifier.feature_importances_
indices = np.argsort(importances)[::-1]  # Sort from most to least important

plt.figure(figsize=(10, 6))
plt.bar(range(X.shape[1]), importances[indices], color='dodgerblue')
plt.xticks(range(X.shape[1]), [feature_names[i] for i in indices], rotation=25, ha='right')
plt.title('Random Forest Feature Importance (Customer Churn)')
plt.ylabel('Relative importance')
plt.xlabel('Feature')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```

## When to use random forests

- **Use them** as a strong default for tabular data. They work well with little tuning and rarely overfit badly.
- **Use them** when you want feature importances to understand what drives predictions.
- **Consider alternatives** when you need the last bit of accuracy ([gradient boosting](./gradient_boosting.md) and [XGBoost](./xgboost.md) usually edge them out), or when model size and prediction speed matter, since hundreds of trees take memory.

## Common mistakes

### Using too few trees

A forest of 5 or 10 trees gives noisy, unstable predictions. Start with at least 100. More trees rarely hurt accuracy; they just take longer.

### Treating feature importance as cause and effect

A high importance means the model *used* that feature, not that the feature *causes* the outcome. Importances can also be inflated for features with many unique values. For a more reliable picture, check scikit-learn's `permutation_importance`.

### Expecting it to extrapolate

A random forest predicts by averaging values it saw during training. For regression, it can never predict a number higher than the largest target in the training data.

## Summary

- A random forest trains many decision trees and combines their votes (or averages).
- Bagging and random feature subsets make the trees different, so their errors cancel out.
- Random forests are accurate, robust, and need little tuning.
- Feature importances help explain what the model learned.
