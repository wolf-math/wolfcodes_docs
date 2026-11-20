---
title: Long Short-Term Memory (LSTM)
sidebar_label: LSTMs
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

## What is an LSTM?

A **long short-term memory (LSTM)** network is a specialized type of [recurrent neural network](./overview.md) built to handle long sequences. It was designed to overcome the vanishing and [exploding gradient](./exploding_gradient.md) problems that keep standard RNNs from remembering things over long distances.

## Why this matters

LSTMs were the standard model for text, speech, and time series for years, and they're still widely used for forecasting and smaller sequence tasks. Understanding their gates explains how a network can learn what to remember and what to forget.

## The problem with standard RNNs

A standard RNN passes a hidden state $h_t$ from one step to the next. During [backpropagation](../backpropagation.md) through time, the gradient is multiplied over and over across the steps. In long sequences it either shrinks to zero (the network forgets early context) or blows up. Either way, standard RNNs struggle to learn **long-term dependencies**, like connecting the subject at the start of a paragraph to a verb at the end.

See [the vanishing gradient problem](./vanishing_gradient.md) for the details.

## How LSTMs work

An LSTM adds a second memory track called the **cell state** ($C_t$). Think of it as a conveyor belt running straight through the whole sequence. Information can ride along it largely unchanged, which lets the LSTM remember things for a long time.

To control what goes onto and comes off the conveyor belt, an LSTM uses three **gates**. Each gate is a small neural layer with a sigmoid activation, which outputs values between 0 ("block everything") and 1 ("let everything through"). The gate's output is multiplied element by element with the information it controls.

All three gates look at the same two things: the previous hidden state $h_{t-1}$ and the current input $x_t$, written together as $[h_{t-1}, x_t]$.

### The forget gate ($f_t$)

- **Purpose**: Decides what to *throw away* from the previous cell state $C_{t-1}$.
- **How it works**: Outputs a number between 0 and 1 for each value in the cell state. A 0 means "forget this completely"; a 1 means "keep this entirely."

$$
f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)
$$

### The input gate ($i_t$) and candidate values ($\tilde{C}_t$)

- **Purpose**: Decides what *new* information to store in the cell state.
- **How it works**: Two parts work together:
  - The **input gate** (a sigmoid layer) decides which values to update:

    $$
    i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)
    $$

  - A **tanh layer** creates a vector of new candidate values that could be added:

    $$
    \tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)
    $$

### Updating the cell state

The old cell state is updated in one step: forget what's irrelevant, then add the new information.

$$
C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t
$$

Here $\odot$ means element-wise multiplication. Notice the update is mainly **addition**, not repeated multiplication by a weight matrix. That's why gradients can flow back through the cell state across many time steps without vanishing.

### The output gate ($o_t$)

- **Purpose**: Decides what the new hidden state $h_t$ (and therefore the output) should be, based on a filtered version of the cell state.
- **How it works**: A sigmoid layer picks which parts of the cell state to output. The cell state is passed through $\tanh$ (squashing it between -1 and 1) and multiplied by that gate:

$$
o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)
$$

$$
h_t = o_t \odot \tanh(C_t)
$$

## Example: sequence classification in Keras

This example builds an LSTM to classify sequences, like predicting whether a time series is trending up or down. The input has the 3D shape LSTMs expect: `(samples, timesteps, features)`.

### Import the packages

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense, Input
from tensorflow.keras.models import Sequential
```

### Generate synthetic data

1,000 samples, each with 10 time steps and 5 features per step:

```python
num_samples = 1000
timesteps = 10
features = 5

X = np.random.random((num_samples, timesteps, features))
y = np.random.randint(0, 2, size=(num_samples, 1))  # Binary target (up/down)
```

### Build the model

```python
model = Sequential([
    Input(shape=(timesteps, features)),
    # 64 LSTM units; returns only the final output, not one per time step
    LSTM(64, activation='tanh'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid'),  # Binary classification output
])
```

### Compile the model

```python
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
```

### Train the model

```python
model.fit(X, y, epochs=5, batch_size=32, validation_split=0.2)
```

### Make a prediction

```python
sample_input = np.random.random((1, timesteps, features))
prediction = model.predict(sample_input)
print(f"Prediction probability: {prediction[0][0]:.4f}")
```

:::note
The data is random, so accuracy will hover around 50%. The example shows the shapes and workflow; swap in a real sequence dataset to see the LSTM learn.
:::

### Key Keras LSTM parameters

- **`units`**: The size of the hidden state and cell state (the number of memory cells in the layer).
- **`return_sequences`**: Set to `True` when stacking another recurrent layer on top, so this layer outputs its hidden state at every time step (`[batch, timesteps, units]`) instead of just the last one (`[batch, units]`).
- **`return_state`**: Set to `True` to also return the final hidden state ($h_t$) and cell state ($C_t$).

## Common mistakes

### Stacking LSTMs without `return_sequences`

When one recurrent layer feeds another, the first must output its hidden state at every time step.

```python
# Wrong: the second LSTM receives 2D input and raises an error
LSTM(64), LSTM(32)

# Correct
LSTM(64, return_sequences=True), LSTM(32)
```

### Shuffling time-series data before splitting

Randomly splitting a time series lets the model train on the future and test on the past. Split by time: train on earlier data, test on later data.

## Summary

- LSTMs add a cell state, a "conveyor belt" of memory that runs through the whole sequence.
- Three gates control it: forget (what to drop), input (what to add), and output (what to reveal).
- Because the cell state is updated mainly by addition, gradients survive across long sequences.
- In Keras, an `LSTM` layer is a drop-in replacement for `SimpleRNN`.
