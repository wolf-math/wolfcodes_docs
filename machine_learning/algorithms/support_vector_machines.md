---
title: Support Vector Machines
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are support vector machines?

A **support vector machine (SVM)** is a supervised learning algorithm used mainly for classification (though it can also do regression). It finds the decision boundary that separates the classes with the **widest possible margin**.

In scikit-learn, the classifier version is called `SVC` (support vector classifier), and the regression version is `SVR`.

## Why this matters

SVMs were the state of the art for classification before deep learning, and they're still excellent on small to medium datasets and high-dimensional data like text. The ideas they introduced, maximum margins and kernels, show up throughout machine learning.

## Key concepts

- **Hyperplane**: The decision boundary. In 2D it's a line, in 3D it's a flat plane, and in higher dimensions it's called a hyperplane.
- **Margin**: The gap between the hyperplane and the nearest points of each class. SVM picks the hyperplane with the largest margin, because a wide gap tends to generalize better to new data.
- **Support vectors**: The data points closest to the boundary. They alone determine where the hyperplane sits. Remove any other point and the boundary doesn't move; remove a support vector and it shifts.
- **The kernel trick**: Real-world data is rarely separable by a straight line. Kernels let SVMs find curved boundaries by implicitly working in a higher-dimensional space (explained next).

## The kernel trick

Imagine a 1D dataset where red dots are sandwiched between blue dots: `[Blue, Red, Red, Blue]`. No single point on the line can separate red from blue.

Now "lift" the data into 2D by adding a second coordinate, $x^2$. The outer blue dots rise high, while the red dots in the middle stay low. Suddenly a flat line can separate them.

```text
1D (x only): no single cut works      2D (x and x²): a flat line works

                                       x²
                                        |  B                 B
  B     R     R     B                   | ---------------------- <- boundary
 -2    -1     1     2   x               |        R     R
                                        +------------------------ x
                                          -2   -1     1     2
```

**The problem:** Actually computing new high-dimensional coordinates for thousands or millions of points is extremely expensive.

**The kernel solution:** A **kernel** is a shortcut function that computes how similar two points *would be* in the higher-dimensional space, without ever calculating their coordinates there. The SVM gets the benefit of the extra dimensions at a fraction of the cost.

## Choosing a kernel

### Linear kernel (`kernel="linear"`)

- **How it works:** No transformation. It finds a straight line, plane, or hyperplane in the original feature space.
- **Best for:** Very large datasets and **text classification** (spam detection, sentiment analysis), where there are already tens of thousands of features and the classes are often linearly separable.
- **Trade-off:** Very fast, but fails on complex, non-linear patterns.

### RBF (Gaussian) kernel (`kernel="rbf"`)

- **How it works:** Measures similarity by distance, creating smooth, bell-shaped "islands" of influence around data points. It can model almost any boundary shape.
- **Best for:** General-purpose non-linear data, especially when you don't know the underlying shape. It's scikit-learn's default.
- **Key hyperparameter `gamma`:** Controls the radius of each island.
  - High `gamma`: tight, isolated pockets around individual points (overfitting risk).
  - Low `gamma`: smooth, broad boundaries (underfitting risk).

### Polynomial kernel (`kernel="poly"`)

- **How it works:** Models relationships using polynomial combinations of features, up to a chosen `degree`.
- **Best for:** Problems where interactions between features matter, such as some image-processing tasks.
- **Key hyperparameter `degree`:** The exponent (for example, `degree=3` allows cubic boundaries). Higher degrees create wavy boundaries that overfit easily.

### Sigmoid kernel (`kernel="sigmoid"`)

- **How it works:** Uses the hyperbolic tangent function, loosely mimicking a two-layer neural network.
- **Best for:** Mostly historical interest. It rarely beats RBF in practice.

**Rule of thumb:** Start with RBF. Switch to linear if you have a huge number of features or samples and need speed.

## Example: classifying iris flowers

Let's classify two species of iris flowers, *Versicolor* and *Virginica*, using two measurements (sepal length and sepal width). Two features make it easy to visualize the boundary and the support vectors.

### Import the packages

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
```

### Load and prepare the data

```python
iris = load_iris()
X = iris.data
y = iris.target

# Keep two classes (Versicolor = 1, Virginica = 2) and two features (sepal length and width)
mask = y != 0
X = X[mask, :2]
y = np.where(y[mask] == 1, 0, 1)  # Relabel as 0 and 1
```

### Split the data

`stratify=y` keeps the same proportion of each class in the training and test sets.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
```

### Scale the features

:::important
Feature scaling is mandatory for SVMs. They work with distances between points, so a feature ranging from 0 to 1,000 would completely dominate one ranging from 0 to 1. Always use `StandardScaler` or `MinMaxScaler`.
:::

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Train the model

```python
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model.fit(X_train_scaled, y_train)
```

`C` controls how strictly the model avoids misclassifying training points. Lower values allow a wider, softer margin; higher values try to classify every point correctly and risk overfitting.

### Evaluate the model

```python
y_pred = svm_model.predict(X_test_scaled)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}\n")
print(classification_report(y_test, y_pred, target_names=['Versicolor', 'Virginica']))
```

These two species overlap heavily in sepal measurements, so don't expect perfect accuracy here. The point is to see how the boundary and support vectors behave.

### Plot the boundary and support vectors

```python
plt.figure(figsize=(10, 6))

x_min, x_max = X_train_scaled[:, 0].min() - 1, X_train_scaled[:, 0].max() + 1
y_min, y_max = X_train_scaled[:, 1].min() - 1, X_train_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)

# Training points
plt.scatter(
    X_train_scaled[:, 0], X_train_scaled[:, 1],
    c=y_train, edgecolors='k', cmap=plt.cm.coolwarm, s=60,
)

# Circle the support vectors
support_vectors = svm_model.support_vectors_
plt.scatter(
    support_vectors[:, 0], support_vectors[:, 1],
    s=150, facecolors='none', edgecolors='black', linewidth=1.5, label='Support vectors',
)

plt.xlabel('Sepal length (scaled)')
plt.ylabel('Sepal width (scaled)')
plt.title('SVM Decision Boundary and Support Vectors')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
```

The circled points are the support vectors: the only training points that shape the boundary.

## When to use SVMs

- **Use them** on small to medium datasets with clear margins between classes, and on high-dimensional data like text.
- **Use them** when you want a strong non-linear classifier without building a neural network.
- **Avoid them** on very large datasets (training time grows quickly with the number of samples), or when you need probability estimates by default.

## Common mistakes

### Forgetting to scale features

SVMs measure distances, so unscaled features distort the margin. This is the single most common reason an SVM performs badly.

```python
# Correct: scaling and the model bundled together
from sklearn.pipeline import make_pipeline

model = make_pipeline(StandardScaler(), SVC(kernel='rbf'))
model.fit(X_train, y_train)
```

A pipeline also makes sure the test data is scaled with the training data's statistics.

### Leaving `C` and `gamma` at their defaults

The defaults are a starting point. Small changes to `C` and `gamma` can swing accuracy dramatically, so tune them together with a grid search.

### Using it on very large datasets

Training time grows at least with the square of the number of samples. For hundreds of thousands of rows, try `LinearSVC` or a different algorithm.

## Summary

- SVMs find the boundary that separates classes with the widest margin.
- Only the support vectors, the points nearest the boundary, determine where it sits.
- Kernels let SVMs draw curved boundaries cheaply. Start with RBF, and use linear for huge or text-heavy datasets.
- Always scale your features, and tune `C` and `gamma` to balance underfitting and overfitting.
