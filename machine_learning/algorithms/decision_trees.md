---
title: Decision Trees
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is a decision tree?

A **decision tree** makes predictions by asking a series of yes/no questions about the features, like a flowchart. Each question splits the data into smaller groups, until you reach an answer. Decision trees can be used for both classification and regression.

```text
                 Credit score > 650?
                /                   \
              no                     yes
              /                        \
     Income > 40k?                  Low risk
       /       \
     no         yes
     /            \
High risk      Low risk
```

## Why this matters

Decision trees are one of the few models you can explain to anyone: you can print the rules and read them aloud. They handle non-linear patterns without [feature scaling](../fundamentals/feature_engineering.md#scaling), and they're the building block of the most successful tabular-data algorithms, random forests and gradient boosting.

## How decision trees work

A decision tree is made of:

- **Root node**: The starting point, representing the entire dataset. It's split on the most informative feature.
- **Decision nodes**: Intermediate nodes that each test one feature (for example, "Is age > 30?") and split the data into branches.
- **Leaves (terminal nodes)**: The endpoints, which hold the final predicted class or value.

### Choosing the best split

To decide which question to ask at each node, algorithms like **CART** (Classification and Regression Trees) try many possible splits and pick the one that best separates the classes. They measure this with an **impurity** metric:

- **Gini impurity**: How often a randomly chosen example in the group would be mislabeled if you labeled it randomly according to the group's class mix. 0 means the group is pure (one class only).
- **Entropy / information gain**: How much a split reduces uncertainty about the class.

The tree keeps splitting until it reaches a stopping rule, such as a maximum depth or a minimum number of samples per leaf.

## Example: predicting loan risk

Imagine a bank that wants to predict whether a loan applicant is **high risk** (likely to default) or **low risk** (likely to repay), based on two scaled features:

1. Credit score
2. Annual income

### Import the packages

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
```

### Generate the data

```python
X, y = make_classification(
    n_samples=400,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    random_state=42,
)
```

### Split the data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Train the model

We set `max_depth=3` to keep the tree small. That prevents [overfitting](../deep_learning/regularization.md) and keeps the tree easy to read.

```python
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X_train, y_train)
```

### Evaluate the model

```python
y_pred = clf.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}\n")
print(classification_report(
    y_test, y_pred, target_names=['Low risk (repaid)', 'High risk (default)']
))
```

### Plot the tree and its decision boundary

```python
plt.figure(figsize=(14, 6))

# Left: the tree itself
plt.subplot(1, 2, 1)
plot_tree(
    clf,
    filled=True,
    feature_names=['Credit score', 'Annual income'],
    class_names=['Low risk', 'High risk'],
    rounded=True,
)
plt.title('Decision Tree Structure')

# Right: the decision boundary
plt.subplot(1, 2, 2)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.coolwarm)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=plt.cm.coolwarm, s=40)
plt.title('Feature Space and Decision Boundary')
plt.xlabel('Credit score (scaled)')
plt.ylabel('Annual income (scaled)')

plt.tight_layout()
plt.show()
```

Notice the decision boundary is made of straight horizontal and vertical segments. Each split tests one feature against one threshold, so trees carve the space into rectangles.

## When to use decision trees

- **Use them** when you need a model you can explain. You can literally read the rules off the tree.
- **Use them** when you don't want to scale your data. Trees compare each feature against a threshold, so feature scale doesn't matter. (In scikit-learn, categorical features still need to be encoded as numbers first.)
- **Be careful**: A single deep tree overfits very easily, and small changes in the data can produce a very different tree. Limit `max_depth`, or use an ensemble like [random forests](./random_forests.md) or [gradient boosting](./gradient_boosting.md).

## Common mistakes

### Growing the tree without limits

By default, scikit-learn grows the tree until every leaf is pure, which memorizes the training data.

```python
# Wrong: perfect training accuracy, poor test accuracy
clf = DecisionTreeClassifier()

# Correct: limit the tree's growth
clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5)
```

### Reading too much into one tree

Small changes in the data can produce a completely different tree. Don't draw firm conclusions from one tree's structure; use an ensemble like a [random forest](./random_forests.md) for more stable results.

## Summary

- A decision tree predicts by asking a sequence of yes/no questions about the features.
- Each split is chosen to make the resulting groups as pure as possible (Gini impurity or entropy).
- Trees are interpretable and need no feature scaling, but overfit easily.
- Control depth to prevent overfitting, or combine many trees into an ensemble.
