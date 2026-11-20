---
title: Evaluating Models
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

## What is model evaluation?

**Model evaluation** is how you measure whether a trained model is actually any good. During training, a model adjusts its parameters on data it has already seen. The real test is **generalization**: how well does it perform on data it has never seen?

To answer that objectively, you test the model on a held-out **test set** and use:

- **Evaluation metrics** that put a number on performance
- **Validation strategies** that make those numbers reliable
- **Diagnostic tools** that tell you whether the model is learning real patterns or just memorizing noise

## Why this matters

A model that looks great on the data it trained on can still be useless in the real world. Evaluation is how you find out before your users do. Choosing the right metric also changes which model you pick: the "most accurate" fraud detector can be the one that catches no fraud at all.

## Classification metrics

Classification metrics are built from four basic outcomes. Imagine a model that predicts whether a patient has a disease ("positive") or not ("negative"):

- **True positives (TP)**: The model predicted positive, and it really was positive. It correctly found the condition.
- **True negatives (TN)**: The model predicted negative, and it really was negative. It correctly ruled the condition out.
- **False positives (FP)**: The model predicted positive, but it was actually negative. A false alarm.
- **False negatives (FN)**: The model predicted negative, but it was actually positive. A missed case.

These four counts are usually laid out in a **confusion matrix**:

|  | Predicted positive | Predicted negative |
|---|---|---|
| **Actually positive** | TP | FN |
| **Actually negative** | FP | TN |

Every classification metric below is a different way of combining these counts.

### Accuracy

**Accuracy** is the fraction of all predictions that were correct:

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

:::warning
Accuracy can be badly misleading on **imbalanced datasets**. If 99% of transactions are legitimate and 1% are fraud, a lazy model that predicts "legitimate" for everything scores 99% accuracy while catching zero fraud.
:::

### Precision: quality of positive predictions

**Precision** asks: of everything the model flagged as positive, how much really was positive?

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

**Use precision when false positives are costly**, for example:

- **Spam filtering**: You don't want legitimate emails sent to the junk folder.
- **Freezing accounts for fraud**: Wrongly freezing a customer's card is disruptive and expensive.

### Recall: how many positives you found

**Recall** (also called **sensitivity**) asks: of all the actual positives, how many did the model find?

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

**Use recall when false negatives are dangerous**, for example:

- **Medical screening**: Missing a sick patient has severe consequences.
- **Predictive maintenance**: Missing a jet engine part that's about to fail is far worse than an extra inspection.

### F1-score: balancing the two

Precision and recall usually pull against each other: catching more positives tends to bring in more false alarms. The **F1-score** combines them into one number using their harmonic mean:

$$
F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}
$$

F1 is only high when *both* precision and recall are high, which makes it a good single metric for imbalanced problems.

### Classification metrics in scikit-learn

You rarely calculate these by hand. scikit-learn computes them all:

```python
from sklearn.metrics import classification_report, confusion_matrix

y_true = [1, 0, 1, 1, 0, 1, 0, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred))
```

**Output:**

```text
[[3 1]
 [1 3]]
              precision    recall  f1-score   support

           0       0.75      0.75      0.75         4
           1       0.75      0.75      0.75         4

    accuracy                           0.75         8
   macro avg       0.75      0.75      0.75         8
weighted avg       0.75      0.75      0.75         8
```

:::note
scikit-learn's confusion matrix puts class `0` first, so its layout is `[[TN, FP], [FN, TP]]`.
:::

## Regression metrics

For regression (predicting numbers like house prices), you measure the size of the errors, or **residuals**, between actual values ($y_i$) and predictions ($\hat{y}_i$). Training aims to make these errors as small as possible.

Regression metrics double as **loss functions**. The [loss functions guide](../deep_learning/loss_functions.md) covers them, and others, in more depth.

### Mean squared error (MSE)

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

- $y_i$ is the actual value.
- $\hat{y}_i$ is the predicted value.
- $n$ is the number of samples.

**How it works:** Squaring the differences penalizes large mistakes much more than small ones.

**Related metric:** **Root mean squared error (RMSE)** is $\sqrt{\text{MSE}}$. It converts the error back into the original units of your target, so an RMSE of 12,000 on house prices means predictions are typically off by about \$12,000.

## Probability metrics: cross-entropy

**Cross-entropy** comes from information theory. It measures the difference between two probability distributions: the true labels (which are certain, 0 or 1) and the probabilities your model predicted. It's used to evaluate (and train) classification models that output probabilities, rather than just hard labels.

### Binary cross-entropy (log loss)

Binary cross-entropy is used when each example belongs to one of two classes (spam vs. not spam, fraud vs. legitimate). The model outputs a single probability between 0 and 1, usually from a sigmoid activation.

$$
\text{BCE} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
$$

- $y_i$ is the true label for sample $i$ (either 0 or 1).
- $\hat{y}_i$ is the predicted probability that sample $i$ is class 1.
- $N$ is the total number of samples.

### Categorical cross-entropy

Categorical cross-entropy is used when each example belongs to exactly one of three or more classes (for example, handwritten digits 0 to 9). The model outputs a probability for every class using a [softmax](../deep_learning/activation_functions.md#softmax) activation.

True labels are usually **one-hot encoded**: class 2 out of 4 becomes `[0, 1, 0, 0]`. The formula sums across all $N$ samples and all $C$ classes:

$$
\text{CCE} = -\frac{1}{N} \sum_{i=1}^{N} \sum_{c=1}^{C} y_{i,c} \log(\hat{y}_{i,c})
$$

- $y_{i,c}$ is 1 if class $c$ is the correct class for sample $i$, otherwise 0.
- $\hat{y}_{i,c}$ is the model's predicted probability that sample $i$ belongs to class $c$.
- $C$ is the total number of classes.

## Robust validation strategies

A single train/test split can be fragile. Your score might depend heavily on which data points happened to land in the test set. **Cross-validation** gives you a more reliable estimate.

### K-fold cross-validation

**How it works:** The dataset is split into $K$ equal parts, called **folds** (commonly $K = 5$ or $10$). The model is trained $K$ times. Each time, one fold is held out for validation and the other $K - 1$ folds are used for training. The final score is the average across all $K$ runs.

**Why use it:** Every data point gets used for both training and validation, which makes the score much less dependent on one lucky (or unlucky) split.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
model = LogisticRegression(max_iter=5000)

scores = cross_val_score(model, X, y, cv=5)
print(scores)
print(f"Mean accuracy: {scores.mean():.3f}")
```

### Stratified k-fold cross-validation

**How it works:** A variation of k-fold for classification. It makes sure each fold has roughly the same proportion of each class as the full dataset.

**Why use it:** It's essential for **imbalanced datasets**, where a regular split might accidentally put zero examples of a rare class into a fold.

:::tip
When you pass `cv=5` to scikit-learn with a classifier, it uses stratified k-fold automatically.
:::

## Diagnosing problems with learning curves

How do you know whether your model is **underfitting** (too simple) or **overfitting** (too complex)? A **learning curve** plots the model's error on both the training set and a validation set as training goes on (either as the training set grows, or across training [epochs](../deep_learning/intro.md#epochs-batches-and-iterations)).

- **Underfitting (high bias):** Training error and validation error are *both* high and level off at a poor value. The model is too simple to capture the underlying pattern.
- **Overfitting (high variance):** Training error is very low, but validation error stays high, leaving a wide gap between the two curves. The model has memorized the training data, including its noise, instead of learning general rules.
- **A good fit:** Both errors are low and close together.

| Pattern | Training error | Validation error | Gap between them |
|---------|----------------|------------------|------------------|
| **Underfitting** | High | High | Small |
| **Overfitting** | Low | High | Large |
| **Good fit** | Low | Low | Small |

In code, scikit-learn's `learning_curve` function calculates both errors for you at several training-set sizes, ready to plot.

The [overfitting and regularization guide](../deep_learning/regularization.md) covers techniques for fixing overfitting.

## Common mistakes

### Trusting accuracy on imbalanced data

```python
# 990 legitimate transactions, 10 fraudulent ones
y_true = [0] * 990 + [1] * 10
y_pred = [0] * 1000  # A "model" that never predicts fraud

accuracy_score(y_true, y_pred)  # 0.99, looks great
recall_score(y_true, y_pred)    # 0.0, catches no fraud at all
```

Always check precision and recall (or the confusion matrix) when one class is rare.

### Tuning on the test set

If you try many models and keep the one with the best test score, the test set is no longer "unseen," and your final score is too optimistic. Use cross-validation on the training data to compare models, and look at the test set once, at the end.

### Leaking information during preprocessing

Scaling or imputing the whole dataset before splitting lets statistics from the test set sneak into training. Split first, then fit preprocessing on the training set only.

## Summary

- Always evaluate on data the model hasn't seen during training.
- For classification, choose between accuracy, precision, recall, and F1 based on which mistakes are most costly. Be wary of accuracy on imbalanced data.
- For regression, MSE punishes large errors heavily, and RMSE reports error in the target's own units.
- Use (stratified) k-fold cross-validation for reliable scores, and learning curves to spot underfitting and overfitting.
