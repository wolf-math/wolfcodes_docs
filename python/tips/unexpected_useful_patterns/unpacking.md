---
title: Tuple unpacking
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Tuple unpacking makes several common Python patterns cleaner. It is useful for assigning several values at once, handling multi-value returns, and writing clearer loops.

## What is tuple unpacking?

Instead of assigning values one at a time, Python can unpack them directly:

```python
point = (10, 20)
x, y = point
```

This keeps the structure of the data visible in the assignment itself.

## Why it is useful

Unpacking improves readability in patterns like these:

Returning several values:

```python
def min_max(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)


low, high = min_max([3, 7, 1, 9])
```

Looping over pairs:

```python
pairs = [("a", 1), ("b", 2)]

for key, value in pairs:
    print(key, value)
```

Swapping variables:

```python
left, right = right, left
```

These forms are concise, but they are also expressive.

## Use unpacking to make shape visible

Unpacking works best when the data naturally has a fixed structure that readers should notice.

If the number of values is unclear or highly variable, a more explicit structure may be easier to understand.

## Rules of thumb

- Use unpacking when the data naturally comes in fixed parts.
- Prefer it for multi-value returns and loop pairs.
- Let the assignment reflect the structure of the value.
- Avoid forcing unpacking when the shape is unclear.
