---
title: Naive Bayes
sidebar_position: 4
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is naive Bayes?

**Naive Bayes** is a family of probabilistic classification algorithms based on **Bayes' theorem**. For a new example, it calculates the probability of each class given the example's features, then predicts the class with the highest probability.

## Why this matters

Naive Bayes trains in a single pass over the data and predicts almost instantly, even with thousands of features. That makes it a classic choice for text problems like spam filtering, and a quick baseline for any classification task. It's also a gentle introduction to thinking about predictions as probabilities.

## Why is it called "naive"?

It makes a "naive" assumption: that every feature is **independent** of every other feature, once you know the class. That's rarely true in the real world (height and weight are clearly related, for example).

Even so, naive Bayes works remarkably well in practice, especially for text classification, spam detection, and medical diagnosis. It's also extremely fast to train and predict.

## Bayes' theorem

$$
P(C_k \mid X) = \frac{P(X \mid C_k) \cdot P(C_k)}{P(X)}
$$

- **$P(C_k \mid X)$, the posterior**: The probability that a data point belongs to class $C_k$, given its features $X$. This is what we want.
- **$P(X \mid C_k)$, the likelihood**: The probability of seeing these features if the point belongs to class $C_k$.
- **$P(C_k)$, the prior**: How common class $C_k$ is in the dataset overall.
- **$P(X)$, the evidence**: The overall probability of seeing these features. It's the same for every class, so it acts as a normalizing constant.

The independence assumption is what makes the likelihood easy to compute: instead of modeling all features together, naive Bayes just multiplies the probability of each feature on its own.

## Variants

Different variants model the likelihood differently, depending on the type of features:

- **Gaussian naive Bayes**: For continuous features that roughly follow a normal (bell-curve) distribution.
- **Multinomial naive Bayes**: For counts, such as how many times each word appears in a document.
- **Bernoulli naive Bayes**: For binary (yes/no) features, such as whether each word appears at all.

## Example: classifying wines

This example uses scikit-learn's built-in **wine dataset** to classify wines into one of three grape cultivars, based on two chemical measurements: alcohol content and malic acid.

### Import the packages

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
```

### Load the data

We keep just the first two features so the result can be plotted in 2D.

```python
data = load_wine()
X = data.data[:, :2]  # Alcohol and malic acid
y = data.target       # Three cultivars: classes 0, 1, and 2
```

### Split the data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
```

### Train the model

Both features are continuous, so we use Gaussian naive Bayes.

```python
gnb = GaussianNB()
gnb.fit(X_train, y_train)
```

### Make predictions and evaluate

```python
y_pred = gnb.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}\n")
print('Confusion matrix:')
print(confusion_matrix(y_test, y_pred))
print("\nClassification report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))
```

### Plot the decision boundary

```python
plt.figure(figsize=(9, 6))

x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05), np.arange(y_min, y_max, 0.05))

Z = gnb.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Set2)

scatter = plt.scatter(
    X_test[:, 0], X_test[:, 1], c=y_test, edgecolors='k', cmap=plt.cm.Set2, s=50
)
plt.title('Naive Bayes Decision Boundary (Wine Cultivars)')
plt.xlabel('Alcohol content')
plt.ylabel('Malic acid')
plt.legend(handles=scatter.legend_elements()[0], labels=list(data.target_names), title='Cultivar')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
```

## When to use naive Bayes

- **Use it** for text classification (spam filters, sentiment analysis), where it's fast and surprisingly accurate.
- **Use it** as a quick baseline when you have little training data or need very fast predictions.
- **Be cautious** when features are strongly correlated, or when you need well-calibrated probabilities. The independence assumption tends to make its probabilities overconfident, even when its predicted class is right.

## Common mistakes

### Using the wrong variant

Each variant assumes a different kind of feature. `GaussianNB` on word counts, or `MultinomialNB` on negative numbers (it will raise an error), gives poor results.

```python
# Wrong: word counts aren't bell-curve shaped
GaussianNB().fit(word_counts, labels)

# Correct: counts call for the multinomial variant
MultinomialNB().fit(word_counts, labels)
```

### Trusting the probabilities too much

Naive Bayes often picks the right class but reports it with extreme confidence, like 0.999. Use its predicted classes freely, but be cautious about using its probabilities directly.

## Summary

- Naive Bayes uses Bayes' theorem to pick the most probable class for each example.
- It "naively" assumes features are independent given the class, which makes it simple and fast.
- Choose the variant that matches your features: Gaussian (continuous), multinomial (counts), or Bernoulli (binary).
- It shines on text data and as a fast baseline.
