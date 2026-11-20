---
title: Activation Functions
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

## What are activation functions?

An **activation function** is a mathematical gate attached to each neuron in a neural network. It takes the neuron's weighted sum of inputs and decides what the neuron outputs: whether it "fires," and how strongly.

Another way to think about it: a neuron's weighted sum is just a number. Sometimes you need a clear "yes" or "no," sometimes a probability, sometimes a cleaned-up signal to pass forward. The activation function turns that raw number into something useful.

## Why this matters

Activation functions add **non-linearity**. Without them, stacking layers would be pointless: any number of linear layers combines into a single linear function, no more powerful than [linear regression](../algorithms/linear_regression.md). Non-linear activations are what let deep networks learn curves, edges, faces, and language.

## How activation functions work

Inside each neuron, two steps happen in order:

1. **Linear transformation**: Compute the weighted sum of the inputs plus a bias:

   $$
   z = \sum_{i=1}^{n} (w_i \cdot x_i) + b
   $$

2. **Non-linear activation**: Pass $z$ through the activation function $f$:

   $$
   a = f(z)
   $$

   The output $a$ is what gets sent to the next layer.

## Common activation functions

### Binary step

The simplest activation function, used in early [perceptrons](./perceptron.md). It outputs 1 if the input crosses a threshold (usually 0), and 0 otherwise.

$$
f(z) = \begin{cases} 0 & \text{if } z < 0 \\ 1 & \text{if } z \ge 0 \end{cases}
$$

- **Range**: $\{0, 1\}$
- **Use case**: Early binary classifiers and logic-gate perceptrons.
- **Drawback**: Its derivative is zero everywhere (and undefined at 0). That means gradient descent gets no signal about how to adjust the weights, so it can't be trained with backpropagation. It also can't output probabilities or handle multiple classes.

### Sigmoid

Sigmoid maps any number into a smooth curve between 0 and 1.

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

- **Range**: $(0, 1)$
- **Use case**: The output layer of binary classifiers, where the output represents a probability.
- **Drawback**: Prone to the **vanishing gradient problem**. For very large or very small $z$, the curve is almost flat, so its derivative is nearly zero and learning stalls in deep networks. See [the vanishing gradient problem](./rnn/vanishing_gradient.md).

### Tanh (hyperbolic tangent)

Tanh is a stretched and shifted version of sigmoid that maps inputs to a range between -1 and 1.

$$
\tanh(z) = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}
$$

- **Range**: $(-1, 1)$
- **Use case**: Hidden layers, especially in recurrent networks. Because its output is centered on zero, optimization is often easier than with sigmoid.
- **Drawback**: It still suffers from vanishing gradients for very large positive or negative inputs.

### ReLU (rectified linear unit)

ReLU is the default activation function for hidden layers in modern deep learning. It outputs the input unchanged if it's positive, and 0 otherwise.

$$
f(z) = \max(0, z)
$$

- **Range**: $[0, \infty)$
- **Use case**: Hidden layers in almost every kind of network, including [CNNs](./cnn/overview.md) and standard feedforward networks.
- **Advantages**: Very cheap to compute, and it doesn't suffer from vanishing gradients for positive inputs.
- **Drawback**: The **dying ReLU problem**. If a neuron's weights get pushed so that its input is always negative, it outputs 0 for everything, its gradient is 0, and it never recovers.

### Leaky ReLU

Leaky ReLU fixes the dying ReLU problem by giving negative inputs a small, non-zero slope instead of flattening them to 0.

$$
f(z) = \max(\alpha z, z)
$$

Here $\alpha$ is a small constant, like 0.01.

- **Range**: $(-\infty, \infty)$
- **Use case**: Deep networks where too many standard ReLU neurons are dying.

### Softmax

Unlike the others, softmax works on a whole *vector* of raw scores (called **logits**) at once. It converts them into a probability distribution where every value is between 0 and 1 and they all add up to 1.

$$
\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$

- **Range**: $(0, 1)$, with all outputs summing to 1.
- **Use case**: The output layer of **multi-class** classifiers. Each output is the probability of one class.

## Worked example

Let's compute one neuron's output with two different activation functions.

Given:

- **Inputs**: $x_1 = 2.0$, $x_2 = -1.5$
- **Weights**: $w_1 = 0.5$, $w_2 = 1.2$
- **Bias**: $b = -0.4$

### Step 1: compute the weighted sum

$$
z = (0.5 \cdot 2.0) + (1.2 \cdot -1.5) + (-0.4) = 1.0 - 1.8 - 0.4 = -1.2
$$

### Step 2a: apply the binary step function

Since $z = -1.2$ is less than 0, the step function outputs $f(-1.2) = 0$.

The neuron is "off." The step function throws away the magnitude: it doesn't matter whether $z$ was -1.2 or -1,000.

### Step 2b: apply ReLU

$$
\text{ReLU}(-1.2) = \max(0, -1.2) = 0
$$

Like the step function, ReLU outputs 0 here because the sum is negative. The difference appears with positive inputs: if $z$ had been 1.5, ReLU would output 1.5, while the step function would clamp it to 1. ReLU preserves *how strongly* a neuron fires, and it has a usable gradient. Those are the reasons it replaced the step function in modern networks.

### The same calculation in code

```python
import numpy as np

x = np.array([2.0, -1.5])
w = np.array([0.5, 1.2])
b = -0.4

z = np.dot(w, x) + b
print(f"z = {z:.2f}")                         # z = -1.20
print('step:', 1 if z >= 0 else 0)            # step: 0
print('relu:', max(0.0, z))                   # relu: 0.0
print(f"sigmoid: {1 / (1 + np.exp(-z)):.3f}")  # sigmoid: 0.231
print(f"tanh: {np.tanh(z):.3f}")              # tanh: -0.834
```

## Comparison table

| Function | Formula | Output range | Key advantage | Main drawback |
|----------|---------|--------------|---------------|---------------|
| Binary step | $1$ if $z \ge 0$, else $0$ | $\{0, 1\}$ | Simple threshold logic | Zero gradient; can't be trained with backpropagation |
| Sigmoid | $\frac{1}{1 + e^{-z}}$ | $(0, 1)$ | Outputs a probability | Vanishing gradients; not zero-centered |
| Tanh | $\frac{e^z - e^{-z}}{e^z + e^{-z}}$ | $(-1, 1)$ | Zero-centered; stronger gradients than sigmoid | Vanishing gradients |
| ReLU | $\max(0, z)$ | $[0, \infty)$ | Fast; no vanishing gradient for positive inputs | Dying ReLU |
| Leaky ReLU | $\max(\alpha z, z)$ | $(-\infty, \infty)$ | Prevents dead neurons | Extra hyperparameter ($\alpha$) |
| Softmax | $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | $(0, 1)$, sums to 1 | Multi-class probabilities | Sensitive to extreme logits |

## Choosing an activation function

- **Hidden layers**: Start with **ReLU**. Try **leaky ReLU** if many neurons are dying. Recurrent networks typically use **tanh**.
- **Output layer, binary classification**: **Sigmoid**.
- **Output layer, multi-class classification**: **Softmax**.
- **Output layer, regression**: **No activation** (a plain linear output).

## Common mistakes

### Using sigmoid in every hidden layer

Stacking sigmoid layers makes gradients shrink as they travel backward, so early layers barely learn. Use ReLU in hidden layers and save sigmoid for the output.

### Applying softmax twice

Many loss functions apply softmax for you. If your model already outputs softmax probabilities, pass them to a loss that expects probabilities, not one that expects raw logits.

```python
# Wrong (PyTorch): CrossEntropyLoss applies softmax itself
probs = torch.softmax(logits, dim=1)
loss = nn.CrossEntropyLoss()(probs, targets)

# Correct: pass the raw logits
loss = nn.CrossEntropyLoss()(logits, targets)
```

## Summary

- Activation functions turn a neuron's weighted sum into its output and add the non-linearity that makes deep networks powerful.
- ReLU is the default for hidden layers; sigmoid and softmax are used in output layers for probabilities.
- Sigmoid and tanh can cause vanishing gradients; ReLU can cause dying neurons, which leaky ReLU fixes.
- The step function can't be trained with gradients, which is why modern networks don't use it.
