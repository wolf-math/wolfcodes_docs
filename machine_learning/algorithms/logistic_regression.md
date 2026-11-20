---
title: Logistic Regression
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

## What is logistic regression?

**Logistic regression** is one of the most widely used supervised learning algorithms for **binary classification**: predicting which of two categories something belongs to (yes/no, spam/not spam, pass/fail, upgrade/churn).

Despite "regression" in its name, it's a classification algorithm. It predicts the *probability* that an example belongs to the positive class, then turns that probability into a category.

## Why this matters

Logistic regression is the go-to first model for yes/no questions: will this customer churn, is this email spam, will this loan default? It's fast, gives you probabilities instead of just labels, and shows which features push predictions up or down. It's also exactly what a single neuron with a sigmoid activation computes, so it's a stepping stone to neural networks.

## How logistic regression works

### Step 1: a linear combination

Like [linear regression](./linear_regression.md), it starts by computing a weighted sum of the input features:

$$
z = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n
$$

- $\beta_0$ is the intercept (bias) term.
- $\beta_1, \dots, \beta_n$ are the coefficients (weights) for each feature $x_1, \dots, x_n$.

### Step 2: the sigmoid function

The value $z$ can be any number from $-\infty$ to $+\infty$, which isn't a valid probability. So logistic regression passes $z$ through the **sigmoid** (logistic) function, which squashes it into the range 0 to 1:

$$
\hat{y} = P(y = 1 \mid x) = \frac{1}{1 + e^{-z}}
$$

- $e$ is Euler's number (about 2.71828).
- $\hat{y}$ is the predicted probability that the input belongs to the positive class.

Large positive $z$ values give probabilities near 1, large negative values give probabilities near 0, and $z = 0$ gives exactly 0.5.

### Step 3: the decision boundary

Finally, a **threshold** (usually 0.5) turns the probability into a class:

- If $\hat{y} \ge 0.5$, predict class 1.
- Otherwise, predict class 0.

## Example: predicting SaaS customer conversion

Imagine you're a data scientist at a software-as-a-service (SaaS) company. You want to predict whether a trial user will **upgrade to a paid subscription (1)** or **churn (0)**, meaning they stop using the product. You have two behavioral features:

- **Feature 1**: Total hours spent in the app during the trial.
- **Feature 2**: Number of support tickets submitted during the trial.

### Import the packages

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
```

### Generate a realistic dataset

```python
np.random.seed(42)
n_samples = 300

app_hours = np.random.uniform(2, 28, n_samples)
support_tickets = np.random.uniform(0, 6, n_samples)

# More app hours -> more likely to upgrade; more tickets -> more friction
z = 0.35 * app_hours - 0.6 * support_tickets - 4.5
probabilities = 1 / (1 + np.exp(-z))
purchased = np.random.binomial(1, probabilities)

X = np.column_stack((app_hours, support_tickets))
y = purchased
```

The labels are generated with the same sigmoid formula the model uses, plus randomness, so there's a real pattern for the model to find.

### Split into training and test sets

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Train the model

```python
model = LogisticRegression()
model.fit(X_train, y_train)
```

### Make predictions

```python
y_pred = model.predict(X_test)

# You can also get the probabilities behind each prediction
y_proba = model.predict_proba(X_test)[:, 1]
```

### Evaluate the model

```python
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification report:")
print(classification_report(y_test, y_pred))
```

See [Evaluating Models](../fundamentals/evaluation.md) for what precision, recall, and the confusion matrix mean.

### Visualize the decision boundary

```python
plt.figure(figsize=(10, 6))

# Predict the class for every point on a grid to color the background
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))

Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)

scatter = plt.scatter(
    X_test[:, 0], X_test[:, 1], c=y_test, edgecolors='k', cmap=plt.cm.coolwarm, s=60
)
plt.title('Logistic Regression Decision Boundary (SaaS Conversion)')
plt.xlabel('App usage (hours)')
plt.ylabel('Support tickets submitted')
plt.legend(*scatter.legend_elements(), title='Purchased')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

The boundary between the two colored regions is a straight line. That's a defining trait of logistic regression: it always draws a **linear** decision boundary.

## When to use logistic regression

- **Use it** as your first baseline for any binary classification problem.
- **Use it** when you need probabilities, not just labels, or when you need to explain which features push predictions up or down.
- **Look elsewhere** when the boundary between classes is strongly non-linear. Try [support vector machines](./support_vector_machines.md) with an RBF kernel, or tree-based models like [random forests](./random_forests.md).

## Common mistakes

### Using it for continuous targets

Despite the name, logistic regression is for classification. For a numeric target like price, use [linear regression](./linear_regression.md).

### Always using a 0.5 threshold

The 0.5 cutoff is just a default. When missing a positive case is expensive (like fraud or disease), use the probabilities and lower the threshold.

```python
# Default: predict 1 when probability >= 0.5
y_pred = model.predict(X_test)

# Custom: flag more cases by lowering the threshold
y_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_proba >= 0.3).astype(int)
```

### Ignoring convergence warnings

If scikit-learn warns that the solver failed to converge, scale your features with `StandardScaler` or raise `max_iter`.

## Summary

- Logistic regression is a classification algorithm that predicts the probability of the positive class.
- It computes a linear combination of features, then squashes it through the sigmoid function.
- A threshold (usually 0.5) converts the probability into a class label.
- It's fast, interpretable, and always produces a linear decision boundary.
