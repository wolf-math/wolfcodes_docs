---
title: Recurrent Neural Networks
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

## What are recurrent neural networks?

**Recurrent neural networks (RNNs)** are neural networks designed for **sequential data**: data where order matters, such as text, speech, time-series measurements, and DNA sequences.

Feedforward networks (like standard dense networks and [CNNs](../cnn/overview.md)) treat every input independently. RNNs have a form of **memory**. They process a sequence one element at a time while keeping an internal **hidden state** that summarizes everything they've seen so far.

## Why this matters

Text, speech, sensor readings, and stock prices all arrive as sequences, where order carries meaning. RNNs were the first neural networks built to handle that, and the ideas they introduced, hidden state and backpropagation through time, are the foundation for LSTMs, GRUs, and the sequence models that followed.

## How RNNs work

The defining feature of an RNN is its **hidden state** ($h_t$), the network's internal memory.

At each time step $t$, the RNN takes two inputs:

1. The current element of the sequence, $x_t$.
2. The hidden state from the previous step, $h_{t-1}$.

It combines them and passes the result through an [activation function](../activation_functions.md) (typically $\tanh$) to produce the new hidden state:

$$
h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)
$$

- $W_{xh}$ is the weight matrix applied to the current input.
- $W_{hh}$ is the weight matrix applied to the previous hidden state.
- $b_h$ is the bias.

The new hidden state $h_t$ is used to produce the output for this step ($y_t$), and it's passed forward as memory to the next step ($t + 1$).

## Key concepts

### Parameter sharing

In a standard dense network, every input position has its own weights. Feed it a 50-word sentence and it learns one set of weights for word 1, a different set for word 2, and so on.

An RNN does the opposite. It uses the **same** weight matrices ($W_{xh}$ and $W_{hh}$) at every time step. Whether it's reading the 2nd word or the 200th, it applies exactly the same rule to update its memory.

#### Why parameter sharing matters

**It recognizes patterns anywhere in a sequence.** Compare *"The fierce dog barked"* with *"Yesterday, out in the quiet park, a fierce dog barked."* The relationship between "fierce" and "dog" is identical, even though the words appear in different positions. Because an RNN uses the same weights at every step, a pattern it learns at step 3 automatically applies at step 50.

**It handles sequences of any length.** A support chat might be 5 messages or 500; a stock history might cover 30 days or 5 years. If a network needed separate weights for each position, you'd have to fix the sequence length in advance. With shared weights, the same network can run for 5 steps or 5,000.

**It keeps the parameter count small.** Learning separate weights for every step of a 100-step sequence would explode the number of parameters and invite **overfitting**. Shared weights keep the model compact: it only learns one rule for moving from one step to the next.

**It's computationally efficient.** Fewer parameters mean less memory and faster training, so long sequences can be processed on standard hardware.

### Unrolling through time

In code, an RNN is a single compact recurrent cell (for example, one `SimpleRNN` layer) that loops over the sequence. To understand how data flows, it helps to picture the network **unrolled**: the loop drawn out as a chain, with one copy of the cell per time step.

```text
        y1          y2          y3                yT
        ▲           ▲           ▲                 ▲
h0 ─▶ [cell] ─h1─▶ [cell] ─h2─▶ [cell] ─h3─▶ ... [cell] ─▶ hT
        ▲           ▲           ▲                 ▲
        x1          x2          x3                xT
```

1. **Step 1**: The cell takes $x_1$ and an initial hidden state $h_0$ (usually all zeros) and produces $y_1$ and $h_1$.
2. **Step 2**: The cell takes $x_2$ and $h_1$, and produces $y_2$ and $h_2$.
3. **Step $T$**: This continues to the last step, where $h_T$ holds a compressed memory of the entire sequence.

Unrolled, an RNN looks like a very deep feedforward network where each "layer" is a moment in time, and every layer shares the same weights.

### Backpropagation through time (BPTT)

Feedforward networks are trained with [backpropagation](../backpropagation.md): errors are calculated at the output and passed backward through the layers. Because an RNN's "depth" is time, it's trained with an extension called **backpropagation through time (BPTT)**:

1. **Forward pass**: The network processes the sequence from $t = 1$ to $t = T$, passing hidden states forward and producing predictions (at each step, or just at the end).
2. **Calculate the loss**: Compare the predictions with the true labels using a [loss function](../loss_functions.md).
3. **Backward pass through time**: The error at step $T$ determines how much the final hidden state $h_T$ was responsible. That error is then passed back to step $T - 1$, then $T - 2$, and so on down the unrolled chain. Because the weights are shared, the gradients from every step are added together to update them.

### The vanishing gradient problem

Standard RNNs struggle to remember things over long distances. During BPTT, the gradient is multiplied again and again as it travels backward through time, and it can shrink exponentially. Errors at the end of a sequence then barely affect what the network learns from the beginning.

This limitation led to gated architectures like [LSTMs](./lstm.md) and [GRUs](./gru.md), which are designed to preserve long-range memory. See [the vanishing gradient problem](./vanishing_gradient.md).

## Example: classifying sequences in Keras

This example builds a `SimpleRNN` model to classify sequences of word IDs, as you might for sentiment analysis.

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Embedding, Input, SimpleRNN
from tensorflow.keras.models import Sequential

# 1. Synthetic data: 1,000 sequences, each 20 tokens long
num_samples = 1000
vocab_size = 10000      # Number of distinct words
sequence_length = 20

X_train = np.random.randint(0, vocab_size, size=(num_samples, sequence_length))
y_train = np.random.randint(0, 2, size=(num_samples, 1))  # Binary labels

print(f"X_train shape: {X_train.shape}")  # (1000, 20)
print(f"y_train shape: {y_train.shape}")  # (1000, 1)

# 2. Build the model
model = Sequential([
    Input(shape=(sequence_length,)),
    # Turn each word ID into a learned 32-dimensional vector
    Embedding(input_dim=vocab_size, output_dim=32),
    # Read the sequence step by step with 64 hidden units
    SimpleRNN(units=64, activation='tanh'),
    # Binary classification output
    Dense(units=1, activation='sigmoid'),
])

# 3. Compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

# 4. Train
model.fit(X_train, y_train, epochs=3, batch_size=32)

# 5. Predict on a new sequence
sample_input = np.random.randint(0, vocab_size, size=(1, sequence_length))
prediction = model.predict(sample_input)
print(f"Prediction probability: {prediction[0][0]:.4f}")
```

:::note
The data here is random, so the model has nothing real to learn. Replace it with real tokenized text (such as the IMDB reviews dataset in `tf.keras.datasets.imdb`) to see it learn.
:::

## Common mistakes

### Feeding 2D data to a recurrent layer

Recurrent layers expect 3D input: `(samples, timesteps, features)`. A single series of numbers needs a features dimension added.

```python
# Wrong: (1000, 20), no feature dimension
X = np.random.random((1000, 20))

# Correct: one feature per time step
X = X.reshape(1000, 20, 1)
```

(The example above avoids this because the `Embedding` layer adds the feature dimension.)

### Using a plain RNN for long sequences

`SimpleRNN` struggles to remember anything more than a few dozen steps back. For longer sequences, use an [LSTM](./lstm.md) or [GRU](./gru.md).

## Summary

- RNNs process sequences one step at a time, carrying a hidden state that acts as memory.
- They reuse the same weights at every step, so they handle sequences of any length with few parameters.
- They're trained with backpropagation through time on the unrolled network.
- Plain RNNs struggle with long-range dependencies, which LSTMs and GRUs were designed to fix.
