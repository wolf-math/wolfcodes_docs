---
title: Shallow vs deep copies
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

Copying a container does not always copy the objects inside it. In Python, shallow copies duplicate the outer container but keep references to the same nested values.

## What is happening?

This looks like a safe copy:

```python
original = {"items": [1, 2, 3]}
copied = original.copy()

copied["items"].append(4)

print(original)
print(copied)
```

**Output:**

```text
{'items': [1, 2, 3, 4]}
{'items': [1, 2, 3, 4]}
```

**What you might expect:** Changing `copied` leaves `original` alone.

**What actually happens:** Both dictionaries point to the same nested list.

## Why this matters

This bug shows up when code copies:

- nested lists or dictionaries
- default configuration objects
- parsed JSON-like data
- test fixtures that are modified between cases

The outer object is new, but the inner mutable values are shared.

## Use `deepcopy()` when you truly need independence

```python
from copy import deepcopy

original = {"items": [1, 2, 3]}
copied = deepcopy(original)

copied["items"].append(4)

print(original)
print(copied)
```

**Output:**

```text
{'items': [1, 2, 3]}
{'items': [1, 2, 3, 4]}
```

`deepcopy()` recursively copies nested objects, so later mutation does not leak back into the original structure.

## Do not use `deepcopy()` blindly

`deepcopy()` is useful, but it is not always the best answer:

- it can be slower than a targeted copy
- it may copy more than you intended
- it can hide a design that mutates shared state too freely

Sometimes the better fix is to build a fresh structure explicitly.

## Rules of thumb

- A shallow copy only copies the outer container.
- Be careful with nested mutable objects.
- Use `deepcopy()` when you need a truly independent nested copy.
- Prefer explicit fresh structures when the copied shape is small and important.
