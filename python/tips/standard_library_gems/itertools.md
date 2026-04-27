---
title: Itertools
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

# `itertools` for lazy iteration patterns

`itertools` gives you building blocks for lazy iteration. It is especially useful when you want to transform, combine, or slice streams of values without building extra lists.

## Why it is useful

A few high-value tools cover many cases:

- `chain()` to combine iterables
- `islice()` to take a slice from any iterable
- `product()` for combinations
- `groupby()` for grouped iteration

Example:

```python
from itertools import chain

values = chain([1, 2], [3, 4])
print(list(values))
```

**Output:**

```text
[1, 2, 3, 4]
```

## Where it shines

`itertools` works well for:

- data pipelines
- lazy processing
- combinatorics
- iterator-heavy code

## When not to use it

Some iterator chains become harder to read than a normal loop. Prefer the clearest version, especially when the logic is not naturally stream-shaped.

## Rules of thumb

- Reach for `itertools` when you are shaping iterables lazily.
- Use it to avoid unnecessary intermediate lists.
- Stop when the pipeline becomes harder to read than a loop.
