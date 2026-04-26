---
title: is vs. `==`
sidebar_position: 8
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`is` and `==` answer different questions. `==` compares values, while `is` compares object identity. Using the wrong one can lead to confusing behavior.

## What is happening?

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

**Output:**

```text
True
False
```

`a` and `b` contain the same values, but they are different objects.

## Why this surprises people

Many bugs come from using `is` when the real question is value equality:

```python
name = "wolf"

if name is "wolf":
    print("match")
```

That may appear to work in some cases because of Python implementation details, but it is the wrong comparison.

## When `is` is the right choice

Use `is` when you want to know whether two references point to the same object.

The most common and important case is checking for `None`:

```python
if value is None:
    ...
```

`is` is also correct for sentinel objects whose identity is meaningful.

## Rules of thumb

- Use `==` for value comparisons.
- Use `is` for `None` and sentinel objects.
- Do not use `is` for strings, numbers, or lists when you mean equality.
- Read `is` as "is the same object?" not "has the same value?"
