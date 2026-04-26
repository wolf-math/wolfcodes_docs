---
title: Floating-point comparisons
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

Floating-point values are not stored with perfect decimal precision. That means direct equality checks can fail even when two results look like they should match.

## What is happening?

```python
print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)
```

**Output:**

```text
False
0.30000000000000004
```

**What you might expect:** `0.1 + 0.2` is exactly `0.3`.

**What actually happens:** The internal binary representation is only an approximation.

## Why this matters

This shows up in:

- comparisons in tests
- money-like calculations
- thresholds and tolerances
- scientific or numeric code

The problem is often not the arithmetic itself. The problem is assuming exact equality when the real concept is "close enough."

## Prefer `math.isclose()`

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))
```

**Output:**

```text
True
```

`math.isclose()` lets you compare values using a tolerance, which better matches how floating-point numbers behave.

:::note
For exact decimal behavior, especially with money, `decimal.Decimal` may be a better fit than `float`.
:::

## Rules of thumb

- Do not assume float equality is exact.
- Use `math.isclose()` when approximate comparison is the real goal.
- Choose `Decimal` when exact decimal semantics matter.
- Be especially careful with float equality checks in tests.
