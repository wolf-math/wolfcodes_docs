---
title: any() and all()
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`any()` and `all()` are small built-ins that make boolean intent much clearer. They are especially useful when you want to say "at least one item matches" or "every item matches" without managing flags by hand.

## What are `any()` and `all()`?

`any()` returns `True` if at least one item in an iterable is truthy. `all()` returns `True` only if every item is truthy.

Without them, code often grows extra state:

```python
found_error = False

for line in lines:
    if "ERROR" in line:
        found_error = True
        break
```

## Why they are useful

The built-in version says the same thing more directly:

```python
found_error = any("ERROR" in line for line in lines)
```

That is easier to scan because the real question is visible immediately.

`all()` works the same way for "every item" checks:

```python
all_valid = all(score >= 0 for score in scores)
```

These patterns remove bookkeeping and make the condition easier to name.

## Use them to express intent

They work especially well for:

- validation checks
- membership-style conditions
- filtering prerequisites
- early exit questions

Because they accept any iterable, they also pair nicely with generator expressions.

## Prefer them when the question is boolean

If you only need a yes-or-no answer, `any()` and `all()` are often better than a manual loop.

If you also need the matching item or more complex control flow, a regular loop may still be clearer.

## Rules of thumb

- Use `any()` for "does at least one item match?"
- Use `all()` for "do all items match?"
- Pair them with generator expressions for readable checks.
- Prefer a loop when you need more than a boolean answer.
