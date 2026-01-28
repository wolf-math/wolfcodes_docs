---
title: None
sidebar_position: 13
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## Properties

```python
>>> dir(None)
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

## Definition

`None` is the absence of value. It is used to indicate "nothing" or "no result". Every occurance of `None` refers to the same single object.

## Dunder methods

| Dunder Method | Operation      | Example (normal syntax) | Example (dunder call) |
| ------------- | -------------- | ----------------------- | --------------------- |
| `__bool__`    | Truth value    | `bool(None)` → `False`  | `None.__bool__()`     |
| `__repr__`    | Representation | `repr(None)` → `'None'` | `None.__repr__()`     |
| `__str__`     | String form    | `str(None)` → `'None'`  | `None.__str__()`      |
