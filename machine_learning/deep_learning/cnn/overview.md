---
title: Convolutional Neural Networks
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

## What are convolutional neural networks?

**Convolutional neural networks (CNNs)** are neural networks designed for data with a grid-like structure, such as images (2D grids of pixels) or time series (1D grids of measurements).

A standard fully connected network treats every pixel as an independent input, ignoring which pixels are next to each other. CNNs take advantage of that **spatial structure**. They automatically learn a hierarchy of visual patterns, from low-level edges and corners in early layers to object parts and complete shapes in deeper layers.

## Why this matters

CNNs made modern computer vision possible: photo tagging, medical image analysis, self-driving perception, and document scanning all rely on them. Their key ideas, local patterns and shared weights, also show up in audio and time-series models.

## How CNNs work

A typical CNN stacks a few kinds of layers, each with a specific job.

### Convolutional layers: extracting features

- **Filters (kernels)**: Small grids of learnable weights (for example, $3 \times 3$ or $5 \times 5$) slide across the input image.
- **Feature maps**: At each position, the filter multiplies its weights with the image patch beneath it and adds up the results into a single number. Sliding the filter across the whole image produces a **feature map** that shows where the filter's pattern appears. Different filters learn to detect different patterns, like vertical edges, curves, or color changes.
- **Stride and padding**: The **stride** is how many pixels the filter moves at each step. **Padding** adds a border (usually of zeros) around the input to control the size of the output.
- **Activation (ReLU)**: Applied right after the convolution to add non-linearity, turning negative values into zero: $f(x) = \max(0, x)$.

See [the convolutional layer](./convolutional_layer.md) for details.

### Pooling layers: downsampling

- **Max or average pooling**: A small window (typically $2 \times 2$) slides across each feature map and keeps either the largest value (max pooling) or the average (average pooling).
- **Purpose**: Shrinks the feature maps' width and height, which reduces computation and memory, helps control overfitting, and makes the network less sensitive to small shifts in an object's position.

See [the pooling layer](./pooling_layer.md) for details.

### Flattening

The final feature maps (3D: height × width × channels) are unrolled into a single 1D vector. This connects the convolutional "feature extractor" to the dense "classifier" at the end.

### Fully connected (dense) layers and output

- Standard [dense layers](../layers.md), where every neuron connects to every value from the previous layer, combine the extracted features to make the final decision.
- The **output layer** usually uses [softmax](../activation_functions.md#softmax) to produce a probability for each class.

```text
Image → [Conv → ReLU → Pool] → [Conv → ReLU → Pool] → Flatten → Dense → Softmax → Class
          feature extraction                                       classification
```

## CNNs vs. standard neural networks

| Feature | Standard (fully connected) network | Convolutional neural network |
|---------|------------------------------------|------------------------------|
| **Input handling** | Needs flattened 1D input; ignores the image's 2D structure | Preserves and uses the spatial structure and neighboring pixels |
| **Parameter count** | Huge: every pixel connects to every neuron, leading to memory bloat and overfitting | Small: the same filter weights are reused across the whole image (**parameter sharing**) |
| **Position sensitivity** | Very sensitive: if the object moves, accuracy drops | Robust to small shifts and distortions, thanks to shared filters and pooling |
| **Feature learning** | Struggles to learn visual hierarchies | Learns them automatically: edges → textures → parts → objects |

## Example: classifying images with CIFAR-10

This example uses TensorFlow and Keras to build and train a CNN on **CIFAR-10**, a dataset of 60,000 small ($32 \times 32$) color images in 10 classes, such as airplanes, cats, and trucks.

```python
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# 1. Load the data and scale pixel values from 0-255 down to 0-1
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# 2. Build the CNN
model = models.Sequential([
    layers.Input(shape=(32, 32, 3)),  # 32x32 pixels, 3 color channels (RGB)

    # First convolutional block
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Second convolutional block
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Third convolutional layer
    layers.Conv2D(64, (3, 3), activation='relu'),

    # Classification head
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax'),  # One output per class
])

# 3. Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # Labels are class numbers, not one-hot
    metrics=['accuracy'],
)

model.summary()

# 4. Train
history = model.fit(
    train_images, train_labels,
    epochs=10,
    validation_data=(test_images, test_labels),
)

# 5. Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"Test accuracy: {test_acc:.4f}")
```

:::tip
Training this on a CPU takes several minutes. A simple CNN like this typically reaches around 70% test accuracy on CIFAR-10. Deeper networks and [data augmentation](../regularization.md) push that much higher.
:::

## Common mistakes

### Forgetting to normalize pixel values

Raw pixels range from 0 to 255. Divide by 255 (or standardize) so training is stable.

```python
# Wrong: raw 0-255 values
model.fit(train_images, train_labels)

# Correct
model.fit(train_images / 255.0, train_labels)
```

### Building too big a network for the data

A deep CNN trained on a few hundred images will memorize them. For small datasets, start from a **pretrained** model (like ResNet or MobileNet) and fine-tune it, a technique called **transfer learning**.

## Summary

- CNNs are built for grid-shaped data like images, and preserve the spatial relationships between pixels.
- Convolutional layers detect features with small sliding filters; pooling layers shrink the feature maps.
- Filters are shared across the whole image, which keeps parameter counts low.
- A typical CNN is a stack of conv/pool blocks, followed by flattening and dense layers for classification.
