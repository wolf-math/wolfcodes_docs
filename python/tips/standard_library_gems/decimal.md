---
title: `decimal`
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`decimal` gives you exact decimal arithmetic, which is often a better fit than `float` when precision and rounding rules matter.

## Why it is useful

Floating-point arithmetic can surprise people:

```python
print(0.1 + 0.2)
```

With `Decimal`, you get exact decimal semantics:

```python
from decimal import Decimal

total = Decimal("0.1") + Decimal("0.2")
print(total)
```

**Output:**

```text
0.3
```

## Good use cases

- money values
- invoices and totals
- explicit rounding rules
- domains where decimal precision matters

## One important detail

Create `Decimal` values from strings when precision matters. Starting from a float can carry float imprecision into the result.

## Rules of thumb

- Use `decimal` when exact decimal behavior matters.
- Create `Decimal` values from strings.
- Prefer `float` only when approximate numeric work is acceptable.
