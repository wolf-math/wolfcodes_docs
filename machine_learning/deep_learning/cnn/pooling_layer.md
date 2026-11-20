---
title: The Pooling Layer
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is a pooling layer?

A **pooling layer** usually follows one or more [convolutional layers](./convolutional_layer.md) and **downsamples** their feature maps. Convolutional layers extract features; pooling layers compress them, keeping the important information in a smaller grid.

Unlike convolutional layers, pooling layers have **no learnable weights**. They apply a fixed rule, like "keep the maximum."

## Why this matters

Pooling is a cheap, simple way to shrink feature maps between convolutional layers. It keeps networks fast and helps them recognize objects even when they move slightly within an image.

## Why pooling matters

### Reducing spatial size

Feature maps can stay large as they pass through several convolutional layers, which makes later layers expensive. Pooling shrinks their width and height (for example, from $32 \times 32$ down to $16 \times 16$), cutting the computation and memory needed downstream.

### Tolerance to small shifts

Real objects appear in slightly different positions from one image to the next. Pooling builds in some **translation invariance**: if an edge shifts by a pixel or two but stays inside the same $2 \times 2$ window, the maximum in that window often stays the same. The network recognizes the feature regardless of tiny movements.

### Reducing overfitting

By keeping only the dominant features and discarding fine detail, pooling acts as a structural regularizer that helps the model avoid memorizing noise.

## Types of pooling

### Max pooling

The most common type. It splits the feature map into windows (typically $2 \times 2$ with a stride of 2) and keeps only the largest value in each one. This emphasizes strong, prominent features, like sharp edges, while discarding weaker background activity.

```text
Feature map (4x4)            Max pooling (2x2, stride 2)

 1   3 | 2   1
 4   2 | 0   1               4   2
-------+-------      →
 5   1 | 1   2               6   3
 6   0 | 3   0
```

Each $2 \times 2$ block is replaced by its maximum, so the $4 \times 4$ map becomes $2 \times 2$.

### Average pooling

Takes the average of each window instead of the maximum. This smooths the feature map, keeping more of the overall context rather than just the strongest signals. Applied to the same feature map above, the top-left block becomes $(1 + 3 + 4 + 2) / 4 = 2.5$.

### Global pooling

**Global max pooling** and **global average pooling** take the maximum or average across an *entire* feature map, collapsing a $H \times W \times C$ tensor into just $C$ values (one per channel). It's often used right before the final classification layer, in place of flattening.

## Pooling layers in code

The examples below apply $2 \times 2$ max pooling to a batch of feature maps in PyTorch and TensorFlow/Keras. Remember that PyTorch uses `NCHW` order and Keras uses `NHWC`.

### PyTorch

```python
import torch
import torch.nn as nn

# 16 feature maps, each 32x32: (batch, channels, height, width)
input_tensor = torch.randn(1, 16, 32, 32)

# 2x2 window, stride 2: halves the width and height
max_pool = nn.MaxPool2d(kernel_size=2, stride=2)

output_tensor = max_pool(input_tensor)

print('Input shape: ', input_tensor.shape)   # torch.Size([1, 16, 32, 32])
print('Output shape:', output_tensor.shape)  # torch.Size([1, 16, 16, 16])
```

### TensorFlow/Keras

```python
import tensorflow as tf

# 16 feature maps, each 32x32: (batch, height, width, channels)
input_tensor = tf.random.normal([1, 32, 32, 16])

# 2x2 window, stride 2: halves the width and height
max_pool = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))

output_tensor = max_pool(input_tensor)

print('Input shape: ', input_tensor.shape)   # (1, 32, 32, 16)
print('Output shape:', output_tensor.shape)  # (1, 16, 16, 16)
```

Notice that pooling changes the width and height but leaves the number of channels unchanged.

## Summary

- Pooling layers downsample feature maps to reduce computation and memory.
- Max pooling keeps the strongest value in each window; average pooling keeps the mean.
- Pooling adds tolerance to small shifts and helps reduce overfitting.
- It has no learnable weights and doesn't change the number of channels.
