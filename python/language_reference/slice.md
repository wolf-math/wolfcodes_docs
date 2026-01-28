---
title: Slice
sidebar_position: 17
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
>>> dir(slice)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'indices', 'start', 'step', 'stop']
```

## Definition

A `slice` object stores the `start`, `stop`, and `step` parameters for slicing sequences. Slice objects are created implicitly with `seq[start:stop:step]` or explicitly with `slice(start, stop, step)`.

```python
>>> s = slice(1, 5, 2)
>>> s.start, s.stop, s.step
(1, 5, 2)
>>> [0,1,2,3,4,5][s]
[1, 3]
```

## Creating slices

```python
slice(stop)            # start=None, step=None
slice(start, stop)     # step=None
slice(start, stop, step)
```

## Using `indices()`

`indices(length)` normalizes the slice for a sequence of given length, returning `(start, stop, step)` with bounds applied—useful when implementing `__getitem__`.

```python
>>> s = slice(-3, None, 2)
>>> s.indices(6)
(3, 6, 2)
```

## Dunder methods

| Dunder Method  | Operation              | Example (normal syntax)                   | Example (dunder call)           |
| -------------- | ---------------------- | ----------------------------------------- | ------------------------------- |
| `__reduce__`   | Pickle support         | `import pickle; pickle.dumps(slice(1,5))` | `slice(1,5).__reduce__()`       |
| `__repr__`     | Representation         | `repr(slice(1,5,2))` → `'slice(1, 5, 2)'` | `slice(1,5,2).__repr__()`       |
| `__eq__`       | Equality               | `slice(1,5)==slice(1,5)` → `True`         | `slice(1,5).__eq__(slice(1,5))` |
| *(attributes)* | Access start/stop/step | `s.start`, `s.stop`, `s.step`             | —                               |
