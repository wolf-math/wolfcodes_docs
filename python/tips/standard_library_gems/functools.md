---
title: Functools
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `functools` for caching, partial application, and more

`functools` contains several small tools with big practical payoff. The most useful ones in everyday code are `lru_cache`, `partial`, and `cached_property`.

## Why it is useful

These tools help you avoid boilerplate:

- `lru_cache` memoizes repeated function calls
- `partial` pre-fills some function arguments
- `cached_property` computes a value once per instance

## A few high-value patterns

Caching repeated pure work:

```python
from functools import lru_cache


@lru_cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Pre-filling arguments:

```python
from functools import partial

int_base_2 = partial(int, base=2)
print(int_base_2("101"))
```

## When to be careful

Caching only helps when repeated calls use the same inputs and the function behaves like a pure function. `partial` is handy, but not if it makes call sites more mysterious.

## Rules of thumb

- Use `lru_cache` for repeated pure computations.
- Use `partial` when a configured function is clearer than a wrapper.
- Use `cached_property` for expensive per-instance values.
