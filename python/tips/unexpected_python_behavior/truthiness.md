---
title: Truthiness can hide meaning
sidebar_position: 12
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Python lets many values act like `True` or `False` in conditionals. That is convenient, but it can hide important distinctions when different falsy values mean different things.

## What is happening?

All of these values are falsy:

- `0`
- `""`
- `[]`
- `{}`
- `None`

That makes code like this easy to write:

```python
value = 0

if not value:
    print("No value")
```

But `0` may be a valid result rather than an absence of data.

## Why this matters

The same conditional can blur together cases that should be handled differently:

- `0` might mean a real numeric count
- `""` might mean an intentionally empty string
- `[]` might mean "present but empty"
- `None` might mean "missing"

Those differences are often part of the program's logic.

## Prefer explicit checks when meaning matters

If the real question is whether a value is missing, say that directly:

```python
if value is None:
    print("Missing value")
```

If the real question is whether a list is empty, checking truthiness may be fine:

```python
if not items:
    print("No items")
```

The key is to match the condition to the meaning, not just to the boolean result.

## Rules of thumb

- Truthiness is convenient, but it can hide distinctions.
- Use `is None` when you mean "missing."
- Use truthiness checks when emptiness is the real concept.
- Be explicit when `0`, `""`, or `None` should mean different things.
