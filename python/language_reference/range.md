---
title: Range
sidebar_position: 15
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
>>> dir(range)
['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']
```

## Definition

`range` represents an immutable sequence of evenly spaced integers. It is memory efficient and generates values lazily. Commonly used for loops, indexing, and producing integer sequences without materializing a list.

```python
>>> r = range(2, 10, 2)  # start, stop, step
>>> list(r)
[2, 4, 6, 8]
```

## Using range

### Instantiation

```python
>>> range(5)          # 0,1,2,3,4
>>> range(2, 5)       # 2,3,4
>>> range(10, 2, -3)  # 10,7,4
```

### Indexing and slicing

```python
>>> r = range(0, 10, 2)
>>> r[2]
4
>>> r[-1]
8
>>> r[1:3]
range(2, 6, 2)
>>> list(r[1:3])
[2, 4]
```

### Membership

Membership is computed arithmetically, not by iterating.

```python
>>> 6 in range(0, 10, 2)
True
>>> 7 in range(0, 10, 2)
False
```

### Length

```python
>>> len(range(1_000_000_000))
1000000000
```

### Start, stop, step attributes

```python
>>> r = range(3, 9, 2)
>>> r.start, r.stop, r.step
(3, 9, 2)
```

### count and index

```python
>>> r = range(0, 10, 2)
>>> r.count(4)
1
>>> r.count(5)
0
>>> r.index(4)
2
```

## Dunder methods

| Dunder Method  | Operation    | Example (normal syntax)  | Example (dunder call)         |
| -------------- | ------------ | ------------------------ | ----------------------------- |
| `__len__`      | Length       | `len(range(5))` → `5`    | `range(5).__len__()`          |
| `__getitem__`  | Index access | `range(5)[2]` → `2`      | `range(5).__getitem__(2)`     |
| `__contains__` | Membership   | `3 in range(5)` → `True` | `range(5).__contains__(3)`    |
| `__iter__`     | Iteration    | `for n in range(3)`      | `range(3).__iter__()`         |
| `__eq__`       | Equality     | `range(3) == range(0,3)` | `range(3).__eq__(range(0,3))` |

