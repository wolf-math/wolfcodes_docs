---
title: Lazy vs Eager Learning
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

## What are lazy and eager learning?

In machine learning, the difference between **lazy learning** and **eager learning** comes down to *when* the model does the heavy lifting:

- **Eager learners** do the work up front, during training, by building a general model.
- **Lazy learners** do the work later, at prediction time, by comparing each new input to stored examples.

This guide covers how each approach works, their trade-offs, and when to use each.

## Why this matters

This distinction tells you where an algorithm spends its time and memory. That matters as soon as a model leaves your laptop: a model that's fast to train but slow to predict may be fine for a nightly report and useless for a website that needs answers in milliseconds.

## Quick comparison

| Feature | Eager learning | Lazy learning |
|---------|----------------|---------------|
| **Training phase** | Builds an explicit, general model from the training data | Just stores the training examples (little or no training) |
| **Prediction phase** | Fast: plugs new data into the pre-built model | Slow: compares new data against stored examples on the fly |
| **Memory** | Usually compact (stores model parameters, not raw data) | High (must keep the entire training set) |
| **Adaptability** | Hard to update; usually requires retraining | New data can be added instantly |
| **Examples** | Decision trees, SVMs, neural networks, naive Bayes | K-nearest neighbors, case-based reasoning |

## Eager learning

An **eager learner** builds a general model (a target function) during training, before it ever sees new data. Once training is done, the original training data usually isn't needed to make predictions.

### How eager learning works

The algorithm analyzes the whole training set to find patterns, set decision boundaries, or learn weights. When a new example arrives, it simply plugs the features into the already-built model.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)    # Slow part: learns weights from all the data
model.predict(X_new)           # Fast part: a quick calculation with learned weights
```

### Advantages

- **Fast predictions**: The mapping from inputs to outputs is already computed.
- **Compact storage**: Only the model parameters (weights, tree structure) need to be stored, which is often much smaller than the raw data.

### Disadvantages

- **Long training time**: Training can be computationally expensive, especially on large datasets.
- **Inflexible updates**: When new data arrives, the model often has to be retrained from scratch.

### Examples of eager learners

- Logistic regression
- Support vector machines (SVMs)
- Neural networks
- Random forests

## Lazy learning

A **lazy learner** puts off generalizing until it's asked to make a prediction. Instead of building a model in advance, it simply memorizes the training data.

### How lazy learning works

When a new data point arrives, the algorithm searches the stored training examples, finds the most similar ones, and uses them to make a local prediction for that specific point.

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)    # Fast part: just stores the data
model.predict(X_new)           # Slow part: measures distance to every stored point
```

### Advantages

- **Instant training**: There's essentially no training phase.
- **Natural adaptability**: New examples can be added immediately, without retraining a global model. You just add them to the stored data.
- **Complex decision boundaries**: Because predictions are based on local neighborhoods, lazy learners can model highly irregular, non-linear boundaries that global models might miss.

### Disadvantages

- **Slow predictions**: Every prediction requires comparing the new point against the entire training set.
- **High memory use**: All training data must stay in memory at prediction time.
- **The curse of dimensionality**: Performance drops quickly as the number of features grows, because distances become less meaningful in high-dimensional spaces.

### Examples of lazy learners

- K-nearest neighbors (KNN)
- Case-based reasoning
- Locally weighted regression

## Choosing between them

- **Use eager learning** when prediction speed matters most and your dataset is stable enough that a heavy upfront training phase is worth it.
- **Use lazy learning** when your data changes often, you need to add new data without retraining, or you're working with smaller datasets where local neighborhoods describe the problem better than one global model.

**Rule of thumb:** Most production systems use eager learners because fast predictions matter. Reach for a lazy learner like KNN when the dataset is small and you want a simple, flexible baseline.

## Summary

- Eager learners train hard and predict fast; lazy learners train instantly and predict slowly.
- Eager learners store a compact model; lazy learners store the whole dataset.
- Lazy learners adapt to new data instantly but struggle with many features.
