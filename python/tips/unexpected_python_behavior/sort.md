---
title: sort() vs sorted()
sidebar_position: 11
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `sort()` vs `sorted()`

`list.sort()` and `sorted()` look similar, but they behave differently in an important way. One mutates the original list and returns `None`. The other returns a new sorted result.

## What is happening?

```python
numbers = [3, 1, 2]
result = numbers.sort()

print(numbers)
print(result)
```

**Output:**

```text
[1, 2, 3]
None
```

**What you might expect:** `result` holds the sorted list.

**What actually happens:** `sort()` changes `numbers` in place and returns `None`.

## Why this matters

This design helps make mutation explicit. It prevents code from accidentally treating an in-place operation like a pure one.

The bug usually appears when code writes:

```python
numbers = [3, 1, 2]
sorted_numbers = numbers.sort()
```

Now `sorted_numbers` is `None`.

## Choose based on whether mutation is intended

Use `sort()` when you intentionally want to mutate the existing list:

```python
numbers.sort()
```

Use `sorted()` when you want a new sorted value:

```python
numbers = [3, 1, 2]
sorted_numbers = sorted(numbers)
```

## Rules of thumb

- `sort()` mutates a list and returns `None`.
- `sorted()` returns a new sorted result.
- Use `sort()` for intentional in-place mutation.
- Use `sorted()` when you want to preserve the original data.
