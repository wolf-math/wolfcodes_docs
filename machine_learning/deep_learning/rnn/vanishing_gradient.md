---
title: The Vanishing Gradient Problem
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

## What is the vanishing gradient problem?

The **vanishing gradient problem** happens when the gradients used to train a network shrink exponentially toward zero as they're passed backward. In [recurrent neural networks](./overview.md), this happens during [backpropagation](../backpropagation.md) through time (BPTT). When the gradient vanishes, the weights stop learning from early time steps, and the model can't learn **long-term dependencies** in a sequence.

The same problem affects very deep feedforward networks, where the gradient fades as it passes back through many layers.

## Why this matters

The vanishing gradient problem explains why plain RNNs forget the beginning of long sequences, and why deep networks were hard to train for years. Knowing the cause helps you recognize it in your own models and choose the right fix.

## The root cause

Recall how a standard RNN updates its hidden state at each time step:

$$
h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)
$$

- $W_{hh}$ is the recurrent weight matrix.
- $W_{xh}$ is the input weight matrix.
- $\tanh$ is the [activation function](../activation_functions.md).

During BPTT, we need the gradient of the loss at the final step $T$ with respect to an earlier hidden state $h_k$. The chain rule turns that into a long product, with one factor for every step in between:

$$
\frac{\partial L_T}{\partial h_k} = \frac{\partial L_T}{\partial h_T} \prod_{j=k+1}^{T} \frac{\partial h_j}{\partial h_{j-1}}
$$

Each factor involves the recurrent weight matrix and the derivative of $\tanh$:

$$
\frac{\partial h_j}{\partial h_{j-1}} = \text{diag}(1 - h_j^2) \, W_{hh}
$$

:::note
You don't need to follow every detail of the math. The key takeaway is that the gradient is a **product of many terms**, one per time step.
:::

## Why the gradient shrinks

Multiply many numbers smaller than 1 together and the result shrinks fast. Two things make the factors small:

- **The activation derivative**: The derivative of $\tanh$ is at most 1 (at $x = 0$), and smaller everywhere else. For sigmoid, it's at most 0.25. Repeatedly multiplying by numbers below 1 drives the product toward zero.
- **The weight matrix**: If the largest eigenvalue (roughly, the strongest "stretching factor") of $W_{hh}$ is less than 1, multiplying by it again and again also shrinks the product exponentially as the gap $T - k$ grows.

A quick feel for the numbers: $0.9^{50} \approx 0.005$, and $0.5^{50}$ is less than one quadrillionth.

If those factors are *greater* than 1 instead, you get the opposite problem: [exploding gradients](./exploding_gradient.md).

## The impact on learning

Because the gradient shrinks exponentially as it travels back in time:

- **Short-term memory only**: The network easily learns relationships between nearby elements, like predicting the next word in a short phrase.
- **Forgetting the past**: Information from many steps earlier has almost no effect on the weight updates. In *"The cat that chased the brown and white dogs across the muddy yard **was**..."*, a vanishing gradient makes it hard for the RNN to connect the singular subject "cat" to the verb "was" across all those intervening words.

## Example: routing support emails

Imagine a support team that uses an RNN to read incoming emails and route each one to either **urgent refunds** or **general inquiries**.

Consider this 50-word email:

> "I am writing to formally request a full refund because the software subscription I purchased last Tuesday completely crashes every time I try to export a report. *[40 words of error codes, system specs, troubleshooting steps, and frustration with the interface.]* Therefore, please process my money back."

### What the network needs to learn

To route this correctly, the RNN must connect the intent stated in the very first sentence, **"request a full refund"**, to the classification decision it makes at the very end.

### How the vanishing gradient breaks training

When the model gets this email wrong during training, it computes an error gradient and sends it backward through all 50 words.

- **Multiplicative decay**: At every word, the gradient is multiplied by the recurrent weights and the $\tanh$ derivative.
- **A shrinking signal**: If those factors are mostly below 1, the gradient decays exponentially. By the time it reaches "request a full refund" near the start, it's practically zero.

### The real-world failure

- The weights never update based on the early context.
- The model develops "short-term memory loss," tuning itself almost entirely on the last few words ("please process my money back," or generic closing phrases).
- In production, it misroutes high-priority refund requests because it effectively forgot what the email was about by the time it finished reading.

## Solutions

Several breakthroughs were designed to fix or sidestep vanishing gradients:

- **[LSTMs](./lstm.md) and [GRUs](./gru.md)**: Gated architectures with a separate memory path. LSTMs keep a **cell state** that is updated mostly by *addition* rather than repeated multiplication, so gradients can flow back across many steps without vanishing.
- **ReLU activations**: In deep feedforward networks, ReLU's derivative is exactly 1 for positive inputs, which helps gradients survive. (It's less common inside RNNs, where it can make gradients explode.)
- **Residual (skip) connections**: Shortcuts that let the gradient bypass layers or time steps, giving it a direct path backward.
- **Transformers**: Abandon recurrence entirely. Using **self-attention**, a Transformer connects any two words in a sequence directly, so there's no long chain of multiplications for the gradient to fade through.

:::note
Gradient clipping is sometimes mentioned alongside these, but it only fixes *exploding* gradients. It does nothing for vanishing ones.
:::

## Summary

- Vanishing gradients happen when backpropagated gradients shrink exponentially across many steps or layers.
- The cause is repeated multiplication by activation derivatives and weights smaller than 1.
- The result is short-term memory: RNNs can't learn connections between distant parts of a sequence.
- LSTMs, GRUs, skip connections, and Transformers were all designed to solve it.
