---
title: Gated Recurrent Units (GRU)
sidebar_label: GRUs
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

## What is a GRU?

A **gated recurrent unit (GRU)** is a type of [recurrent neural network](./overview.md). Like an [LSTM](./lstm.md), it was designed to solve the [vanishing gradient problem](./vanishing_gradient.md), so it can capture long-term dependencies in text, time series, and audio.

GRUs streamline the LSTM design:

- They **merge** the cell state and hidden state into a single hidden state.
- They use **two gates** instead of three.

The result has fewer parameters and usually trains faster, while performing about as well as an LSTM on many tasks.

## Why this matters

GRUs give you most of the long-memory benefits of an LSTM with fewer parameters, so they train faster and need less data. For many sequence problems, they're the first gated model worth trying.

## How GRUs work

A GRU controls its memory with two gates: the **update gate** and the **reset gate**. Both look at the previous hidden state $h_{t-1}$ and the current input $x_t$, and both use a sigmoid ($\sigma$) to output values between 0 and 1.

### The update gate ($z_t$)

The update gate decides **how much of the hidden state to replace** with new information at this step. It plays the role of the LSTM's forget and input gates combined.

$$
z_t = \sigma(W_z \cdot [h_{t-1}, x_t] + b_z)
$$

- $x_t$: The input at the current time step.
- $h_{t-1}$: The hidden state from the previous step.
- $\sigma$: The sigmoid function, which squashes values between 0 and 1.

### The reset gate ($r_t$)

The reset gate decides **how much of the past to use** when computing new candidate information.

$$
r_t = \sigma(W_r \cdot [h_{t-1}, x_t] + b_r)
$$

If $r_t$ is close to 0, the GRU ignores the previous hidden state and focuses only on the current input, effectively "resetting" its memory for this calculation.

### The candidate hidden state ($\tilde{h}_t$)

Using the reset gate, the GRU computes a candidate hidden state that combines the current input with whatever past information the reset gate lets through:

$$
\tilde{h}_t = \tanh(W \cdot [r_t \odot h_{t-1}, x_t] + b)
$$

- $\odot$ means element-wise multiplication.
- $\tanh$ squashes the result between -1 and 1.

### The final hidden state ($h_t$)

Finally, the update gate blends the old hidden state with the candidate:

$$
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t
$$

- If $z_t \approx 0$: the GRU **keeps its old memory** ($h_t \approx h_{t-1}$) and ignores the candidate. This is how it carries information unchanged across many steps.
- If $z_t \approx 1$: the GRU **overwrites its memory** with the new candidate ($h_t \approx \tilde{h}_t$).

:::note
This is the form from the original GRU paper. Keras and PyTorch use the swapped version, $h_t = z_t \odot h_{t-1} + (1 - z_t) \odot \tilde{h}_t$, where $z_t \approx 1$ keeps the old memory. The idea is the same either way: the update gate interpolates between keeping the old state and taking the new one.
:::

## GRU vs. LSTM

| Feature | LSTM | GRU |
|---------|------|-----|
| **Gates** | 3 (input, forget, output) | 2 (update, reset) |
| **Memory** | Separate cell state ($C_t$) and hidden state ($h_t$) | A single hidden state ($h_t$) |
| **Parameters** | More (higher capacity) | Fewer (faster training) |
| **Performance** | Often better on very long, complex sequences | Often just as good on smaller datasets, and trains faster |

**Rule of thumb:** Try a GRU first when you want speed or have limited data. Switch to an LSTM if you need more capacity for long, complex sequences.

## Example: sequence classification in Keras

This example builds a GRU model to classify sequences of shape `(samples, timesteps, features)`.

### Import the packages

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import GRU, Dense, Dropout, Input
from tensorflow.keras.models import Sequential
```

### Generate synthetic data

1,000 training samples and 200 validation samples, each with 20 time steps and 10 features per step:

```python
np.random.seed(42)
X_train = np.random.randn(1000, 20, 10).astype(np.float32)
y_train = np.random.randint(0, 2, size=(1000, 1)).astype(np.float32)

X_val = np.random.randn(200, 20, 10).astype(np.float32)
y_val = np.random.randint(0, 2, size=(200, 1)).astype(np.float32)
```

### Build the model

```python
model = Sequential([
    Input(shape=(20, 10)),
    GRU(
        units=64,
        return_sequences=False,         # Only output the final hidden state
        activation='tanh',              # For the candidate state
        recurrent_activation='sigmoid', # For the update and reset gates
    ),
    Dropout(0.3),                       # Regularization
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid'),     # Binary classification output
])
```

### Compile the model

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
```

### Train the model

```python
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=10,
    batch_size=32,
)
```

### Evaluate on the validation set

```python
loss, accuracy = model.evaluate(X_val, y_val)
print(f"Validation loss: {loss:.4f}")
print(f"Validation accuracy: {accuracy:.2%}")
```

### Key Keras GRU parameters

- **`return_sequences`**: Set to `True` when stacking another recurrent layer on top, or for sequence-to-sequence tasks, so the layer outputs a hidden state for every time step. Leave it `False` when you only need the final hidden state, as in sequence classification.
- **`recurrent_activation`**: The activation for the gates ($z_t$ and $r_t$). Defaults to `"sigmoid"`.
- **`activation`**: The activation for the candidate state. Defaults to `"tanh"`.

## Summary

- A GRU is a streamlined LSTM with two gates and a single hidden state.
- The update gate decides how much memory to replace; the reset gate decides how much past to use for new information.
- GRUs have fewer parameters and train faster, often matching LSTM performance.
- In Keras, a `GRU` layer is a drop-in replacement for `LSTM` or `SimpleRNN`.
