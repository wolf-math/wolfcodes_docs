---
title: Generator expressions
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

Generator expressions let you process values lazily instead of building a full list first. They are especially useful when you only need to iterate once or pass values directly into another function.

## Why this matters

This pattern builds an unnecessary list:

```python
total = sum([value * 2 for value in numbers])
```

It works, but the intermediate list is only used once.

## Prefer a generator expression

```python
total = sum(value * 2 for value in numbers)
```

This version streams values into `sum()` without creating a separate list in memory first.

That is often:

- more memory efficient
- just as readable
- a better fit for one-pass operations

## Where generator expressions shine

They work especially well with functions like:

- `sum()`
- `any()`
- `all()`
- `max()`
- `min()`

For example:

```python
has_error = any("ERROR" in line for line in lines)
```

The values are produced only as needed.

## When a list is still the right choice

Use a list comprehension instead when:

- you need to reuse the result multiple times
- you need list methods later
- the full collection is the real output

Laziness is helpful, but only when it matches the task.

## Rules of thumb

- Prefer generator expressions for one-pass consumption.
- Skip the extra list when the values are only being fed into another function.
- Use a list comprehension when you actually need a list.
- Favor the form that best matches how the result will be used.
