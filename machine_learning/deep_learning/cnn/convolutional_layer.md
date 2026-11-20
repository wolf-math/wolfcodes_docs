---
title: The Convolutional Layer
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

## What is a convolutional layer?

The **convolutional layer** is the core engine of a [CNN](./overview.md). A traditional neural network flattens its input into a long vector, but a convolutional layer works directly on spatial grids, like 2D images with height, width, and color channels.

## Why this matters

The convolutional layer is where a CNN does its learning. Understanding filters, channels, stride, and padding lets you predict the shape of every layer's output, which is exactly what you need to design a network or debug a shape error.

## Key concepts

### Filters (kernels) and weights

A **filter** (or **kernel**) is a small grid of weights, such as $3 \times 3$ or $5 \times 5$. It slides across the input, and at each position it multiplies its weights with the values beneath it and adds them up.

Here's a $3 \times 3$ filter sliding over a $4 \times 4$ grayscale image. At the top-left position, it covers the bracketed patch:

```text
Input (4x4)              Filter (3x3)       Output (2x2)
[1] [0] [2]  1           1  0  -1           -2   .
[0] [1] [3]  0     *     1  0  -1     =      .   .
[2] [1] [0]  1           1  0  -1
 0   2   1   3
```

Multiply each patch value by the filter weight in the same position, then add everything up:

```text
row 1:  (1 × 1) + (0 × 0) + (2 × -1) = -1
row 2:  (0 × 1) + (1 × 0) + (3 × -1) = -3
row 3:  (2 × 1) + (1 × 0) + (0 × -1) =  2
                                total = -2
```

That's the top-left output value. The filter then slides one pixel right and repeats, and so on across the image. The key idea: **each output value is a weighted sum of a small neighborhood of input values**, computed with the same filter everywhere. This particular filter responds to vertical edges, where brightness changes from left to right.

In traditional computer vision, filters like this were designed by hand (the Sobel edge detector is a famous example). In a CNN, **the filter weights are learnable parameters**. Backpropagation adjusts them during training, so the network discovers for itself which patterns matter for the task.

### Channels and depth

- Color images are 3D: height × width × **channels** (red, green, and blue).
- A filter always matches the depth of its input. If the input has 3 channels, a single $3 \times 3$ filter is actually a stack of three $3 \times 3$ grids, one per channel.
- As it slides, the filter multiplies across all channels at once and sums everything into a single number per position. So **one filter produces one 2D feature map**.
- A layer uses many filters (for example, 32 or 64). Their feature maps are stacked together, producing a new multi-channel output for the next layer.

### Stride and padding

- **Stride ($S$)**: How many pixels the filter moves at each step. A stride of 1 moves one pixel at a time; a stride of 2 skips every other position, roughly halving the output size.
- **Padding ($P$)**: A border of zeros added around the input.
  - **Valid padding** ($P = 0$): No padding. The output shrinks, because the filter can't hang over the edges.
  - **Same padding**: Just enough padding that the output has the same width and height as the input (when the stride is 1).

You can calculate the output size with:

$$
O = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1
$$

- $W$ is the input width (or height), $K$ is the filter size, $P$ is the padding, and $S$ is the stride.

For example, a $32 \times 32$ image with a $3 \times 3$ filter, padding 1, and stride 1 gives $\lfloor (32 - 3 + 2) / 1 \rfloor + 1 = 32$. The size is preserved.

### The activation function (ReLU)

Convolution is a linear operation, and linear operations alone can't solve complex problems. So right after the convolution, an activation function is applied to every value, typically ReLU:

$$
\text{ReLU}(x) = \max(0, x)
$$

This replaces negative values with zero and adds the non-linearity the network needs to learn complex patterns. See [activation functions](../activation_functions.md).

## Convolutional layers in code

The examples below create a single 2D convolutional layer and pass a batch of fake images through it, in both PyTorch and TensorFlow/Keras.

:::important
The two frameworks order tensor dimensions differently:

- **PyTorch** expects `NCHW`: (batch, channels, height, width).
- **TensorFlow/Keras** expects `NHWC`: (batch, height, width, channels).
:::

### PyTorch

```python
import torch
import torch.nn as nn

# One RGB image, 32x32 pixels: (batch, channels, height, width)
input_tensor = torch.randn(1, 3, 32, 32)

# 16 filters, each 3x3, with stride 1 and padding 1 ("same" padding)
conv_layer = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)

output_tensor = conv_layer(input_tensor)

print('Input shape: ', input_tensor.shape)   # torch.Size([1, 3, 32, 32])
print('Output shape:', output_tensor.shape)  # torch.Size([1, 16, 32, 32])
```

### TensorFlow/Keras

```python
import tensorflow as tf

# One RGB image, 32x32 pixels: (batch, height, width, channels)
input_tensor = tf.random.normal([1, 32, 32, 3])

# 16 filters, each 3x3, with "same" padding and ReLU built in
conv_layer = tf.keras.layers.Conv2D(
    filters=16,
    kernel_size=(3, 3),
    strides=(1, 1),
    padding='same',
    activation='relu',
)

output_tensor = conv_layer(input_tensor)

print('Input shape: ', input_tensor.shape)   # (1, 32, 32, 3)
print('Output shape:', output_tensor.shape)  # (1, 32, 32, 16)
```

In both cases, the 3 input channels become 16 output channels (one per filter), while "same" padding keeps the $32 \times 32$ size.

## Common mistakes

### Using the wrong dimension order

PyTorch expects channels first (`NCHW`); Keras expects channels last (`NHWC`). Mixing them up either raises a shape error or silently treats image rows as color channels.

```python
# Image from a library like PIL or OpenCV: (height, width, channels)
image.shape  # (32, 32, 3)

# PyTorch needs (channels, height, width): move the channel axis first
tensor = torch.tensor(image).permute(2, 0, 1)  # (3, 32, 32)
```

### Forgetting the batch dimension

Layers expect a batch of images, even if you only have one. Add a leading dimension of size 1: `tensor.unsqueeze(0)` in PyTorch, or `np.expand_dims(image, 0)` for Keras.

## Summary

- A convolutional layer slides small learnable filters across the input to detect local patterns.
- Each filter spans all input channels and produces one feature map; many filters produce many maps.
- Stride and padding control the output size: $O = \lfloor (W - K + 2P)/S \rfloor + 1$.
- A ReLU activation follows the convolution to add non-linearity.
