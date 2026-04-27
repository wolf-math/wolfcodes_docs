---
title: Typing
sidebar_position: 21
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `typing` for clearer APIs

`typing` makes Python APIs easier to understand and navigate. Even a few good type hints can make a codebase more readable and easier to maintain.

## Why it is useful

Simple hints clarify contracts:

```python
def get_total(prices: list[float]) -> float:
    return sum(prices)
```

`Protocol` is especially useful when you care about behavior instead of inheritance:

```python
from typing import Protocol


class SupportsWrite(Protocol):
    def write(self, text: str) -> None: ...
```

That lets code express "anything with this method works here."

## Good use cases

- public functions
- shared utility code
- interfaces between modules
- behavior-based contracts with `Protocol`

## Rules of thumb

- Use type hints to make interfaces obvious.
- Reach for `Protocol` when behavior matters more than class ancestry.
- Prefer clear contracts over exhaustive clever typing.
