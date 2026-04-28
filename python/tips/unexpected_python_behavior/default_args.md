---
title: Mutable defaults
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Mutable default arguments

Mutable default arguments keep state between function calls. This surprises many Python developers because the default value is created once when the function is defined, not each time the function runs.

## What is happening?

```python
def add_item(item: str, items: list[str] = []) -> list[str]:
    items.append(item)
    return items


print(add_item("a"))
print(add_item("b"))
```

**Output:**

```text
['a']
['a', 'b']
```

**What you might expect:** Each call gets a fresh list.

**What actually happens:** The same list object is reused.

## Why this happens

Default argument values are evaluated once, when Python defines the function. If that value is mutable, later calls keep mutating the same object.

This affects values like:

- `[]`
- `{}`
- `set()`

## Prefer this instead

Use `None` as the default and create a new object inside the function:

```python
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []
    items.append(item)
    return items
```

Now each call without an explicit `items` argument gets a fresh list.

:::warning
Avoid using mutable objects as default argument values unless you intentionally want shared state.
:::

## Rules of thumb

- Default argument values are created once.
- Do not use `[]`, `{}`, or similar mutable values as defaults in normal code.
- Use `None` and create the object inside the function.
- If shared state is intentional, make that choice explicit and obvious.
