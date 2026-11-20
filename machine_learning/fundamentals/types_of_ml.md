---
title: Types of Machine Learning
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

## What are the types of machine learning?

Machine learning is broadly divided into three types, based on what kind of feedback the system learns from:

- **Supervised learning**: Learns from labeled examples where the right answer is known.
- **Unsupervised learning**: Finds structure in data that has no labels.
- **Reinforcement learning**: Learns by trial and error, taking actions and receiving rewards.

## Why this matters

Choosing the right algorithm is a turning point in any ML project. Think of algorithms as different lenses: some draw straight lines through continuous data, some find complex decision boundaries, some group items by hidden similarities, and some learn the best behavior by interacting with an environment.

Your choice depends on three things:

1. **Your data**: Is it labeled or unlabeled?
2. **Your goal**: Are you predicting a value, grouping items, or choosing actions?
3. **How the system learns**: From a fixed dataset, or by actively interacting with an environment?

## Supervised learning

In **supervised learning**, the algorithm learns from a **labeled** dataset. For every input, you already know the correct output, and the model learns to map one to the other.

Supervised problems come in two flavors: regression and classification.

### Regression: predicting numbers

**Regression** algorithms predict a continuous numeric value.

#### Linear regression

- **How it works:** Fits a straight line (or a flat hyperplane in higher dimensions) that minimizes the distance between predicted values and the actual data points.
- **Real-world example:** Predicting house prices. Given features like square footage, number of bedrooms, and age of the home, the model calculates a dollar value.

The model is defined by the equation of a line:

$$
y = mx + b
$$

- $y$ is the dependent variable (what you're predicting), on the y-axis.
- $m$ is the slope of the line.
- $b$ is the y-intercept.
- $x$ is the independent variable (the input feature), on the x-axis.

See the [linear regression guide](../algorithms/linear_regression.md) for a full example.

### Classification: predicting categories

**Classification** algorithms assign inputs to discrete classes, such as "Spam" vs. "Not Spam," or output the probability of each class.

#### Logistic regression

- **How it works:** Despite the name, this is a classification algorithm. It uses the sigmoid function to squash a linear combination of features into a probability between 0 and 1.
- **Real-world example:** Email spam detection, classifying each email as "Spam (1)" or "Not Spam (0)".

$$
P(Y=1 \mid X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_n X_n)}}
$$

- $P(Y=1 \mid X)$ is the probability that the outcome is 1 (the positive class).
- $e$ is Euler's number (about 2.71828).
- $\beta_0$ is the intercept (bias) term.
- $\beta_1, \beta_2, \dots, \beta_n$ are the coefficients for each feature $X_1, X_2, \dots, X_n$.

See the [logistic regression guide](../algorithms/logistic_regression.md).

#### Decision trees and random forests

- **How it works:** A decision tree splits data into branches using feature thresholds (for example, "Is credit score > 700?"). A random forest builds hundreds of independent decision trees and combines their votes for a more robust prediction.
- **Real-world example:** Loan approval, using credit metrics, employment history, and debt ratios to approve or deny applications.

See [decision trees](../algorithms/decision_trees.md) and [random forests](../algorithms/random_forests.md).

#### Support vector machines (SVM)

- **How it works:** Finds the decision boundary (hyperplane) that separates classes with the widest possible margin, using the "kernel trick" to handle non-linear boundaries.
- **Real-world example:** Handwritten digit recognition, such as reading postal codes on mail.

See [support vector machines](../algorithms/support_vector_machines.md).

#### K-nearest neighbors (KNN)

- **How it works:** A "[lazy learner](./lazy_vs_eager_learning.md)." It doesn't build an explicit model. Instead, it looks at the $K$ closest training points to a new input and assigns the majority class.
- **Real-world example:** Product recommendations ("customers similar to you also bought...").

See [k-nearest neighbors](../algorithms/knn.md).

#### Naive Bayes

- **How it works:** Uses Bayes' theorem to calculate the probability of each class given the features, assuming the features are independent of one another once you know the class.
- **Real-world example:** Sentiment analysis, classifying a review as positive, neutral, or negative.

$$
P(C_k \mid X) = \frac{P(X \mid C_k) \cdot P(C_k)}{P(X)}
$$

- $P(C_k \mid X)$ is the **posterior**: the probability that a data point belongs to class $C_k$ given its features $X$.
- $P(X \mid C_k)$ is the **likelihood**: the probability of seeing these features if the point belongs to class $C_k$.
- $P(C_k)$ is the **prior**: how common class $C_k$ is in the dataset overall.
- $P(X)$ is the **evidence** (marginal likelihood): the overall probability of the features. It acts as a normalizing constant.

See [naive Bayes](../algorithms/naive_bayes.md).

## Unsupervised learning

In **unsupervised learning**, the training data has no labels. The algorithm's job is to discover patterns and structure on its own.

### Clustering: finding groups

**Clustering** algorithms group similar data points together without being told what the groups should be.

#### K-means clustering

- **How it works:** Places $K$ center points (centroids) in the data, assigns each point to its nearest centroid, then repeatedly moves each centroid to the middle of its assigned points until they stop moving.
- **Real-world example:** Customer segmentation, grouping shoppers into personas like "bargain hunters" and "premium subscribers" for marketing.

See [k-means clustering](../algorithms/k_means.md).

#### Hierarchical clustering

- **How it works:** Builds a tree of clusters (a **dendrogram**) by repeatedly merging small clusters together (agglomerative) or splitting large ones apart (divisive).
- **Real-world example:** Grouping genes by expression patterns, or building biological taxonomies.

### Dimensionality reduction: compressing data

**Dimensionality reduction** compresses data with many features into fewer features while keeping its most important structure.

#### Principal component analysis (PCA)

- **How it works:** Finds the directions (principal components) along which the data varies the most, then projects the data onto those directions.
- **Real-world example:** Image compression and feature extraction, shrinking image data while keeping the key features a facial-recognition model needs.

## Reinforcement learning

Unlike supervised and unsupervised learning, **reinforcement learning (RL)** doesn't rely on a fixed dataset. Instead, an **agent** learns to make a sequence of decisions by interacting with an **environment**. It takes actions, receives rewards or penalties, and tries to maximize its total long-term reward.

```text
+-------------+    Action    +-------------+
|             | -----------> |             |
|    Agent    |              | Environment |
|             | <----------- |             |
+-------------+ State/Reward +-------------+
```

### Q-learning (value-based)

- **How it works:** The agent keeps a table (or, in deep Q-learning, a neural network) that maps each state and action to its expected future reward, called a **Q-value**. It updates these values as it explores.
- **Real-world example:** Game-playing AI that learns games like Pac-Man or Breakout purely from the screen and the score.

### Policy gradient methods (policy-based)

- **How it works:** Directly optimizes the agent's strategy (its **policy**) instead of building a value table. This works well for continuous control tasks.
- **Real-world example:** Robotic motor control, training a robot to walk or grasp objects by rewarding stability and penalizing falls.

### Deep Q-networks and actor-critic methods

- **How it works:** Combine deep neural networks with RL so the agent can handle complex inputs like camera feeds or high-dimensional sensor data.
- **Real-world example:** Self-driving trajectory planning, or controlling data-center cooling to minimize power usage.

## Choosing the right type

When deciding which kind of algorithm to use:

1. **Identify the feedback you have:**
   - Do you have labels (known answers)? Use **supervised learning**.
   - Do you have raw, unlabeled data that needs structure? Use **unsupervised learning**.
   - Do you have an environment where actions produce outcomes? Use **reinforcement learning**.
2. **Start simple:** Establish a baseline, such as linear or logistic regression for tabular data, or basic Q-learning for a simple environment.
3. **Scale up only when needed:** Move to non-linear ensembles (random forests, [gradient boosting](../algorithms/gradient_boosting.md)) or [deep learning](../deep_learning/intro.md) when the simple baseline isn't good enough.

**Rule of thumb:** A simple model you understand beats a complex model you can't explain, unless the complex model is clearly better on your test data.

## Summary

- **Supervised learning** uses labeled data to predict numbers (regression) or categories (classification).
- **Unsupervised learning** finds groups (clustering) or compresses features (dimensionality reduction) in unlabeled data.
- **Reinforcement learning** learns actions through rewards in an environment.
- Pick the type based on your data and goal, start with a simple baseline, and add complexity only when it earns its keep.
