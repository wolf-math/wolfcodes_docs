---
title: Method
sidebar_position: 23
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## Definition

A **method** is a function bound to an object. Accessing `obj.method` produces a bound method that remembers `obj` as its first argument. Methods can be inspected for their underlying function and the bound instance.

```python
class Greeter:
    def hi(self, name):
        return f"hi {name}"

g = Greeter()
bound = g.hi      # method bound to g
bound("Ada")      # 'hi Ada'
```

## Introspection

- `__self__` — the bound instance (or `None` for unbound functions retrieved from a class)
- `__func__` — the original function object

```python
>>> bound.__self__ is g
True
>>> bound.__func__ is Greeter.hi
True
```

## Dunder methods

| Dunder Method | Operation           | Example (normal syntax) | Example (dunder call)   |
| ------------- | ------------------- | ----------------------- | ----------------------- |
| `__call__`    | Call the method     | `"hi".upper()` → `'HI'` | `"hi".upper.__call__()` |
| `__func__`    | Underlying function | `obj.method.__func__`   | *(attribute access)*    |
| `__self__`    | Bound instance      | `obj.method.__self__`   | *(attribute access)*    |
