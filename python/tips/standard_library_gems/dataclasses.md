---
title: `dataclasses`
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`dataclasses` are a great standard-library tool for plain data objects. They reduce boilerplate and make object fields easy to scan.

## What are `dataclasses`?

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    active: bool = True
```

This creates a readable data-first class without hand-writing `__init__()` and other common methods.

## Why it is useful

`dataclasses` work especially well for:

- configuration objects
- parsed records
- structured function results
- values passed between modules

The field definitions stay front and center.

## When not to use it

If a class is mostly about behavior, lifecycle management, or heavy custom initialization, a regular class may be clearer.

## Rules of thumb

- Use `@dataclass` for simple structured data.
- Keep dataclasses focused on state.
- Prefer regular classes when behavior is the main story.
