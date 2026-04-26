---
title: Sentinel objects
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

A sentinel object is a unique marker value used to mean "not provided" or "not found." It is useful when `None` is already a valid, meaningful value and you need a different way to represent absence.

## Why this matters

Using `None` as a default is common:

```python
def update_user(name: str | None = None) -> None:
    ...
```

But this creates a problem when `None` itself is a legitimate value you may want to pass explicitly.

Now the function cannot easily tell the difference between:

- no argument provided
- argument provided with value `None`

## Prefer a sentinel object

```python
MISSING = object()


def update_user(name: str | None | object = MISSING) -> None:
    if name is MISSING:
        print("No name argument provided")
    elif name is None:
        print("Explicitly clear the name")
    else:
        print(f"Set name to {name}")
```

Because `MISSING` is a unique object, it cannot be confused with ordinary input values.

## Why it is useful

Sentinel objects are especially helpful in:

- function arguments
- dictionary lookups
- parsing code
- APIs where `None` has business meaning

They make absence explicit instead of overloading `None` with too many jobs.

## Rules of thumb

- Use a sentinel when `None` is a valid real value.
- Compare sentinels with `is`, not `==`.
- Give sentinel names that explain the meaning, such as `MISSING` or `UNSET`.
- Reach for this pattern when "not provided" must be distinct from "provided as `None`."
