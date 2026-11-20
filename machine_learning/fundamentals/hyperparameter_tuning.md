---
title: Hyperparameter Tuning
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

## What are hyperparameters?

**Hyperparameters** are configuration settings you choose *before* training begins. They control how the model trains and how complex it can become, and they can't be learned from the data directly. Examples include the learning rate in gradient descent, the maximum depth of a decision tree, and the number of hidden layers in a neural network.

They're different from **model parameters** (like weights and biases), which the algorithm learns automatically during training.

```python
from sklearn.tree import DecisionTreeClassifier

# max_depth is a hyperparameter: you choose it
model = DecisionTreeClassifier(max_depth=3)

# The split thresholds are parameters: the model learns them
model.fit(X_train, y_train)  # Assumes training data from an earlier split
```

**Hyperparameter tuning** is the search for the combination of hyperparameters that gives the best performance on validation data.

## Why this matters

The same algorithm can perform very differently depending on its settings. A decision tree with no depth limit memorizes its training data; the same tree limited to depth 3 might generalize well. Tuning is often the cheapest way to get a better model without collecting more data or switching algorithms.

## Examples of hyperparameters

Every algorithm has its own hyperparameters. Here are two common examples.

### Support vector machines

- **`C` (regularization strength)**: A lower `C` allows a wider margin with some misclassified points, which usually generalizes better. A higher `C` tries to classify every training point correctly, which risks overfitting.
- **`gamma`**: Controls how far the influence of a single training example reaches. A high `gamma` creates tight, complex boundaries around individual points (overfitting risk).
- **`kernel`**: Think of the kernel as the glasses you wear to look at your data. A `"linear"` kernel is like clear glasses: you see straight-line relationships. A `"poly"` kernel is like a tinted lens that highlights curved, polynomial patterns. See [support vector machines](../algorithms/support_vector_machines.md) for details.

### XGBoost

- **`learning_rate`**: The size of the step taken at each boosting round. Larger values learn faster but can overshoot and overfit; smaller values learn more slowly but more carefully.
- **`n_estimators`**: The number of trees to build. More trees can improve accuracy but increase overfitting risk and training time.
- **`max_depth`**: The maximum depth of each tree. Deeper trees capture more complex relationships but overfit more easily.
- **`min_child_weight`**: The minimum amount of data (technically, the sum of instance weights) required in a child node. Larger values make the model more conservative.
- **`subsample`**: The fraction of rows used to build each tree. Values below 1.0 add randomness that can reduce overfitting and speed up training.

Notice the theme: almost every hyperparameter trades off between **underfitting** (too simple) and **overfitting** (too complex). Tuning is finding the sweet spot. See the [XGBoost guide](../algorithms/xgboost.md) for a full example.

## Tuning techniques

All three techniques below use the same setup: a random forest on scikit-learn's breast cancer dataset.

```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

rf = RandomForestClassifier(random_state=42)

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
}
```

### Grid search

**Grid search** (`GridSearchCV`) tries *every* combination of the values you list. It's thorough, but the cost grows fast: the grid above has 3 × 4 × 3 × 3 = 108 combinations, and with 5-fold cross-validation that's 540 model fits.

```python
from sklearn.model_selection import GridSearchCV

grid_search = GridSearchCV(
    estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1
)
grid_search.fit(X_train, y_train)

print('Best parameters:', grid_search.best_params_)
print(f"Best cross-validation accuracy: {grid_search.best_score_:.4f}")
```

### Random search

**Random search** (`RandomizedSearchCV`) samples a fixed number of random combinations instead of trying them all. It logs each result and returns the best one. In practice, it often finds a combination nearly as good as grid search in a fraction of the time.

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_grid,
    n_iter=10,  # Number of random combinations to try
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=-1,
)
random_search.fit(X_train, y_train)

print('Best parameters:', random_search.best_params_)
print(f"Best cross-validation accuracy: {random_search.best_score_:.4f}")
```

### Bayesian optimization with Optuna

**Bayesian optimization** is smarter than random guessing: it uses the results of previous trials to decide which combination to try next, focusing on the most promising regions. **Optuna** is a popular Python framework for it. Install it with `pip install optuna`.

```python
import optuna
from sklearn.model_selection import cross_val_score


def objective(trial):
    # Optuna suggests a value for each hyperparameter
    model = RandomForestClassifier(
        n_estimators=trial.suggest_int('n_estimators', 50, 300),
        max_depth=trial.suggest_int('max_depth', 2, 32, log=True),
        min_samples_split=trial.suggest_int('min_samples_split', 2, 10),
        min_samples_leaf=trial.suggest_int('min_samples_leaf', 1, 5),
        random_state=42,
    )

    # Score this combination with cross-validation
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    return scores.mean()


study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)

print('Best parameters:', study.best_params)
print(f"Best cross-validation accuracy: {study.best_value:.4f}")
```

### Choosing a technique

| Technique | Best for | Drawback |
|-----------|----------|----------|
| Grid search | Small search spaces you want to cover completely | Cost explodes as you add hyperparameters |
| Random search | Quickly scanning large search spaces | Can miss the exact best combination |
| Bayesian (Optuna) | Expensive models where each trial counts | Extra dependency and setup |

## Best practices

- **Always use cross-validation**: Score each combination with k-fold cross-validation (`cv=5`) so you don't overfit to a single validation split.
- **Prevent data leakage**: Put preprocessing steps (scaling, imputation) inside a scikit-learn `Pipeline` that you pass to the search, instead of applying them to the whole dataset beforehand.
- **Start broad, then refine**: Use random search to scan a wide range, then run a focused grid search or Bayesian optimization around the best region.
- **Keep the test set for the end**: Tune on training data with cross-validation, and evaluate on the test set only once you've picked your final model.

## Summary

- Hyperparameters are settings you choose before training; parameters are what the model learns.
- Most hyperparameters trade off between underfitting and overfitting.
- Grid search is exhaustive, random search is efficient, and Bayesian optimization is adaptive.
- Tune with cross-validation and pipelines, and save the test set for the final check.
