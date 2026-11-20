---
title: The Machine Learning Process
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

Machine learning can seem intimidating with all the math and theory, but at its core it's an extension of software engineering. Instead of writing explicit instructions, you teach a system to learn patterns from data.

## What is machine learning?

**Machine learning (ML)** is a way of building programs that learn their own rules from examples. It helps to contrast it with traditional programming:

- **Traditional programming**: You give the computer **data** and **rules** (your code), and the program produces **answers**.
- **Machine learning**: You give the computer **data** and the desired **answers**, and the algorithm figures out the **rules** (the model) for you.

Instead of hardcoding a rule like "if an email contains 'win' and 'million', mark it as spam," an ML model looks at thousands of emails and learns the statistical patterns that separate spam from legitimate messages on its own.

## Why this matters

Knowing the whole process keeps you from treating machine learning as "pick an algorithm and call `fit()`." Most of the real work, and most of the mistakes, happen before and after training: collecting the right data, preparing it, and checking honestly whether the model works. Every other guide in this section zooms in on one of these phases.

## The six phases of training a model

Training an ML model is a structured, iterative pipeline. Most projects move through these six phases, often looping back to earlier ones as you learn more about the problem.

### 1. Data collection

A model is only as good as the data it learns from. In this phase you gather raw data relevant to your problem, such as historical house prices, customer transaction logs, or a collection of text documents.

**Key focus:** Make sure the dataset is large, diverse, and representative of the real-world situations the model will face.

### 2. Data preparation and preprocessing

Raw data is messy. It contains missing values, duplicates, formatting inconsistencies, and outliers. During preprocessing you:

- **Handle missing data** by filling it in (imputation) or removing it.
- **Encode categories** by converting text labels into numbers the model can use (for example, one-hot encoding).
- **Scale numbers** by normalizing or standardizing numeric ranges.
- **Select features** by deciding which columns (features) are relevant to the problem:
  - Start with the features that are typically relevant, then run a preliminary analysis of the data.
  - If two features are highly correlated, you might keep only one to avoid redundancy.
  - Some features are theoretically useful but impractical because of poor quality or availability.
- **Split the data** into a **training set** (usually 80%) and a **test set** (usually 20%):
  - **Training** is the process where the model learns from data. The training set is what you feed the model.
  - **Testing** is where you evaluate the model on new, unseen data.

The [feature engineering guide](./feature_engineering.md) covers these techniques in detail with code.

### 3. Model selection

Next you choose an algorithm that fits your problem. That might be a simple [linear regression](../algorithms/linear_regression.md), a [decision tree](../algorithms/decision_trees.md), or a complex neural network:

- **Supervised learning**: The data is labeled (for example, predicting house prices or classifying emails). Examples: linear regression, [random forests](../algorithms/random_forests.md), [support vector machines](../algorithms/support_vector_machines.md).
- **Unsupervised learning**: The data is unlabeled, and the model looks for hidden structure (for example, customer segmentation). Examples: [k-means](../algorithms/k_means.md) clustering, principal component analysis.
- **Deep learning**: Neural networks used for complex tasks like computer vision or natural language processing.

These families are explained in [Types of Machine Learning](./types_of_ml.md).

### 4. Training (fitting) the model

This is where the actual learning happens:

1. You feed the **training set** into your chosen algorithm.
2. The model makes predictions and measures its error with a **loss function** (how far off its predictions are from the real answers).
3. An **optimizer** (like gradient descent) tweaks the model's internal parameters (weights and biases) to reduce that error.
4. This cycle repeats over many passes through the data. Each full pass is called an **epoch**.

In scikit-learn, this whole loop happens inside a single call:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)  # Training happens here
```

The deep learning guides on [loss functions](../deep_learning/loss_functions.md) and [gradient descent](../deep_learning/gradient_descent.md) show what's going on inside `fit()`.

### 5. Evaluation

Once training is complete, you test the model on the **test set**: data it has never seen before. This measures how well the model **generalizes** to new data instead of just memorizing the training examples.

The right metric depends on the task:

- **Classification**: accuracy, precision, recall, or F1-score.
- **Regression**: mean squared error (MSE) or similar error measures.

These are explained in detail in [Evaluating Models](./evaluation.md).

### 6. Deployment, monitoring, and improvement

From here, one of two things happens:

- **The model isn't good enough yet.** Adjust it by tuning its [hyperparameters](./hyperparameter_tuning.md), adding more data, changing the preprocessing, or trying a different algorithm. Then loop back through training and evaluation.
- **The model performs well.** Deploy it and monitor its results in production, so you'll know when the real world drifts away from your training data and the model needs retraining.

## Common mistakes

### Testing on the training data

A model that's evaluated on data it has already seen will look far better than it really is.

```python
# Wrong: scores the model on the data it memorized
model.fit(X, y)
model.score(X, y)

# Correct: hold out a test set the model never sees during training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
model.score(X_test, y_test)
```

### Skipping data preparation

Jumping straight to model selection with raw, messy data usually produces a poor model, and no algorithm can fully make up for it. Look at your data first: check for missing values, outliers, and columns that need encoding.

### Treating deployment as the finish line

The world changes after you deploy. Customer behavior shifts, prices move, and new kinds of fraud appear. Monitor your model's performance in production and plan to retrain it.

## Summary

- Machine learning flips traditional programming: you provide data and answers, and the algorithm learns the rules.
- A typical project moves through collection, preparation, model selection, training, evaluation, and deployment.
- Always evaluate on data the model hasn't seen. Performance on training data alone tells you very little.
- Expect to loop. Most of the work is iterating on data and models until the results are good enough.
