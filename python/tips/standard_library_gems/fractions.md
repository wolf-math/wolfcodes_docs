---
title: `fractions`
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

`fractions.Fraction` gives you exact rational arithmetic. It is a useful alternative when you want values like one-third to stay exact instead of becoming floating-point approximations.

## What is `Fraction`?

```python
from fractions import Fraction

value = Fraction(1, 3) + Fraction(1, 6)
print(value)
```

**Output:**

```text
1/2
```

## Why it is useful

This is helpful when:

- ratios matter
- exact rational results are important
- rounding would hide useful structure

It can also make examples and educational code more honest about exact values.

## When not to use it

For everyday approximate numeric work, `float` is usually simpler. For decimal business rules, `decimal.Decimal` is often the better fit.

## Rules of thumb

- Use `Fraction` for exact rational arithmetic.
- Prefer it when ratios should stay exact.
- Choose `Decimal` for decimal money-like rules instead.
