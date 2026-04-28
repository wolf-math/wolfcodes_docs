---
title: zip() for parallel iteration
sidebar_position: 10
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`zip()` lets you iterate over several iterables in parallel. It is a clean way to express "take one item from each sequence together" without indexing by hand.

## What is `zip()`?

```python
names = ["Ada", "Grace", "Linus"]
scores = [95, 99, 88]

for name, score in zip(names, scores):
    print(name, score)
```

**Output:**

```text
Ada 95
Grace 99
Linus 88
```

This is usually clearer than looping over indexes and then looking up values in each list.

## Why it is useful

`zip()` helps when:

- two sequences belong together
- parallel iteration is the real task
- manual indexing would add noise

It also combines well with unpacking, which keeps the loop body simple.

## One important detail

`zip()` stops when the shortest iterable runs out.

That is often exactly what you want, but it can hide mismatched lengths if the data should always line up.

:::note
If equal lengths are required, it is worth validating that assumption instead of relying on `zip()` silently truncating.
:::

## Rules of thumb

- Use `zip()` when iterating over related sequences together.
- Prefer it over manual index-based loops for parallel data.
- Remember that it stops at the shortest iterable.
- Validate lengths when truncation would be a bug.
