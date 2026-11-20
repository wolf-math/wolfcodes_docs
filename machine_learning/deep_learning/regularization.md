---
title: Overfitting and Regularization
sidebar_position: 10
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is overfitting?

**Overfitting** happens when a model learns its training data *too* well. Instead of the true underlying pattern, it memorizes random noise, outliers, and quirks that won't appear in new data.

- **The symptom**: The model scores near 100% on the training set but performs poorly on validation and test data.
- **The root cause**: The model has too much capacity (too many parameters or layers) relative to the amount and variety of training data. It can memorize the data rather than generalize from it.

### Signs of overfitting

- Training accuracy is much higher than test accuracy.
- Training loss keeps falling while validation loss levels off or starts to rise.
- The model performs poorly on new, real-world data.

See [Evaluating Models](../fundamentals/evaluation.md) for how learning curves reveal overfitting.

## Why this matters

Neural networks are powerful enough to memorize almost any training set, so overfitting is the most common reason a model that looks great in training disappoints in production. Regularization is how you keep that power pointed at real patterns.

## What is regularization?

**Regularization** is any change to a model or its training that's designed to reduce overfitting, so the model performs better on unseen data, even if it does slightly worse on the training data.

These techniques are used across classical machine learning and deep learning.

## Penalty-based regularization (weight decay)

These techniques add a penalty to the [loss function](./loss_functions.md) based on the size of the model's weights. That discourages the model from leaning too heavily on any single feature, which keeps its decision boundaries smoother.

### L2 regularization (ridge)

Adds a penalty proportional to the **squared** size of the weights:

$$
L_{\text{total}} = L_{\text{data}}(y, \hat{y}) + \lambda \sum_{i=1}^{n} w_i^2
$$

- $L_{\text{data}}$ is the normal loss (like MSE or cross-entropy).
- $\lambda$ (lambda) controls how strong the penalty is.
- **Effect:** Shrinks all weights smoothly toward zero, with large weights penalized most. Importance gets spread across many features.

### L1 regularization (lasso)

Adds a penalty proportional to the **absolute** size of the weights:

$$
L_{\text{total}} = L_{\text{data}}(y, \hat{y}) + \lambda \sum_{i=1}^{n} \lvert w_i \rvert
$$

- **Effect:** Can push weights all the way to exactly zero, which effectively removes irrelevant features. It acts as automatic feature selection.

## Deep learning techniques

Neural networks have millions of parameters, so neurons can easily team up to memorize training examples. These techniques break that up.

### Dropout

During each training step, every neuron is randomly "dropped out" (its output temporarily set to zero) with probability $p$, typically between 0.2 and 0.5.

- **Effect:** Neurons can't rely on specific neighbors being present, so the network is forced to learn redundant, robust features.
- **At prediction time**, dropout is switched off and every neuron is active. To keep the overall signal strength consistent, the outputs are rescaled. Modern frameworks like Keras do this during training (scaling surviving outputs up by $\frac{1}{1-p}$), so you don't need to change anything at prediction time.

### Batch normalization

**Batch normalization** normalizes each layer's inputs across a mini-batch. It's mainly used to stabilize and speed up training, but the small amount of noise it introduces also has a mild regularizing effect.

## Training process controls

How and when you stop training plays a big role in overfitting.

- **Early stopping:** Monitor the validation loss after every [epoch](./intro.md#epochs-batches-and-iterations). If it stops improving for a set number of epochs (the **patience**), stop training and restore the weights from the best epoch.
- **Data augmentation:** Expand the training set with label-preserving changes: rotating, cropping, or color-shifting images; replacing words with synonyms in text. The model learns to ignore small, irrelevant variations.
- **K-fold cross-validation:** Doesn't prevent overfitting by itself, but gives a reliable estimate of performance on unseen data. That lets you tune regularization settings (like $\lambda$ or the dropout rate) with confidence.

## Choosing a technique

| Technique | Best for | How it helps |
|-----------|----------|--------------|
| L2 regularization | Linear models, neural networks | Prevents large weights; smooths boundaries |
| L1 regularization | Feature selection, sparse models | Drives unnecessary weights to zero |
| Dropout | Deep neural networks | Stops neurons from co-adapting |
| Early stopping | Any iteratively trained model (boosting, deep learning) | Stops before the model starts memorizing noise |
| Data augmentation | Images, text, audio | Exposes the model to more varied inputs |

## Example: combining techniques in Keras

This example combines L2 regularization, dropout, and early stopping in one network.

```python
import tensorflow as tf
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import callbacks, layers, regularizers

# 1. Create and scale a binary classification dataset
X, y = make_classification(n_samples=2000, n_features=20, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# 2. Build the model with L2 regularization and dropout
model = tf.keras.Sequential([
    layers.Input(shape=(20,)),
    layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.Dropout(0.3),  # Drop 30% of outputs during training
    layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3. Stop when validation loss hasn't improved for 5 epochs
early_stopping = callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True,
)

# 4. Train
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=32,
    callbacks=[early_stopping],
)
```

### What each technique does here

1. **L2 regularization** (`kernel_regularizer=regularizers.l2(0.001)`)
   - Adds a penalty proportional to the squared weights to the loss. The factor `0.001` sets how strongly large weights are penalized.
   - Passed directly to each `Dense` layer.
2. **Dropout** (`layers.Dropout(0.3)`)
   - Randomly switches off 30% of the previous layer's outputs at each training step, forcing the network to learn robust, distributed features.
   - Added as its own layer. It turns itself off automatically during evaluation and prediction.
3. **Early stopping** (`callbacks.EarlyStopping`)
   - Watches the validation loss after every epoch, and halts training if it hasn't improved for 5 epochs (`patience=5`).
   - `restore_best_weights=True` makes sure you keep the weights from the best epoch, not the last one.

## Common mistakes

### Leaving dropout on during prediction

Keras turns dropout off automatically in `predict()` and `evaluate()`. In PyTorch, you must switch modes yourself.

```python
# PyTorch
model.train()  # Dropout active: use while training
model.eval()   # Dropout off: use before evaluating or predicting
```

### Regularizing a model that's underfitting

If training and validation scores are both poor, the model is too simple, and adding regularization makes it worse. Regularize only when there's a clear gap between training and validation performance.

### Choosing the penalty strength by test score

Pick $\lambda$ and the dropout rate using a validation set or cross-validation, never the test set.

## Summary

- Overfitting means memorizing the training data instead of learning general patterns.
- L1 and L2 regularization penalize large weights; L1 can also zero out useless features.
- Dropout, early stopping, and data augmentation are the main tools for deep networks.
- Combine techniques, and use validation data to tune how strong they should be.
