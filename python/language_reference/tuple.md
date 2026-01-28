---
title: Tuple
sidebar_position: 19
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
>>> dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
```

## Definition

A `tuple` is an **immutable** ordered collection of items, defined with parentheses `()` or commas. Tuples can contain mixed types and nesting. Once created, a tuple cannot be modified; all operations that would change contents must produce a new tuple.

```python
>>> t = (1, "a", True)
>>> t
(1, 'a', True)

>>> nested = (1, (2, 3), ["mutable list"])
```

## Using tuples

### Instantiation

```python
# literal with parentheses
>>> t = (1, 2, 3)

# parentheses optional for simple tuples
>>> t = 1, 2, 3

# single-element tuple needs a trailing comma
>>> single = (42,)
>>> type(single)
<class 'tuple'>

# constructor from iterable
>>> tuple([1, 2, 3])
(1, 2, 3)
```

### Accessing elements

Tuples are indexed from `0`. Negative indices access from the end.

```python
>>> t = ('apple', 2, True, 'string cheese')
>>> t[0]
'apple'
>>> t[1]
2
>>> t[-1]
'string cheese'
>>> t[-2]
True
```

### Slicing

Tuples support slicing like lists.

```python
>>> t = ('apple', 2, True, 'string cheese')
>>> t[0:3]
('apple', 2, True)
>>> t[1:]
(2, True, 'string cheese')
>>> t[:2]
('apple', 2)
>>> t[::2]
('apple', True)
```

### Membership testing

Check existence with `in`.

```python
>>> 2 in (1, 2, 3)
True
>>> "x" in (1, 2, 3)
False
```

### Immutability

Tuples cannot be changed after creation.

```python
>>> t = (1, 2, 3)
>>> t[0] = 99
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

To “modify,” create a new tuple:

```python
>>> t = (1, 2, 3)
>>> t = (99,) + t[1:]
>>> t
(99, 2, 3)
```

### Packing and unpacking

```python
>>> point = (3, 4)
>>> x, y = point
>>> x
3
>>> y
4

# extended unpacking
>>> a, *rest = (1, 2, 3, 4)
>>> a, rest
(1, [2, 3, 4])
```

### Tuple vs list

- Tuple: immutable, typically used for fixed-size, heterogeneous data.
- List: mutable, used for sequences that change.

## Dunder methods

| Dunder Method  | Operation     | Example (normal syntax)     | Example (dunder call)     |
| -------------- | ------------- | --------------------------- | ------------------------- |
| `__getitem__`  | Indexing      | `(1,2,3)[0]` → `1`          | `(1,2,3).__getitem__(0)`  |
| `__len__`      | Length        | `len((1,2,3))`              | `(1,2,3).__len__()`       |
| `__contains__` | Membership    | `2 in (1,2,3)`              | `(1,2,3).__contains__(2)` |
| `__add__`      | Concatenation | `(1,2)+(3,4)` → `(1,2,3,4)` | `(1,2).__add__((3,4))`    |
| `__mul__`      | Repeat        | `(1,2)*2` → `(1,2,1,2)`     | `(1,2).__mul__(2)`        |
| `__eq__`       | Equality      | `(1,2)==(1,2)`              | `(1,2).__eq__((1,2))`     |
| `__iter__`     | Iteration     | `for x in (1,2,3)`          | `(1,2,3).__iter__()`      |

---

## `tuple` Methods

### `count`

Returns the number of occurrences of a value in the tuple.

```python
>>> t = (1, 2, 2, 3)
>>> t.count(2)
2
>>> t.count(5)
0
```

---

### `index`

Returns the index of the first occurrence of a value. Raises `ValueError` if not found.

```python
>>> t = ('a', 'b', 'c', 'b')
>>> t.index('b')
1

>>> t.index('x')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple
```
