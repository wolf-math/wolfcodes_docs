---
title: Frozenset
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
## Properties

```python
>>> dir(frozenset)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
```

## Definition

A `frozenset` is the immutable version of a [`set`](./set). Like sets, frozensets are unordered collections of unique, hashable elements. However, unlike sets, frozensets cannot be modified after creation, which makes them hashable and allows them to be used as dictionary keys or elements in other sets.

## Using frozensets

Frozensets are instantiated using the `frozenset()` constructor, which accepts an iterable.

```python
>>> my_frozenset = frozenset([1, 2, 3])
>>> my_frozenset
frozenset({1, 2, 3})
```

### Immutability

Once created, a frozenset cannot be modified. Attempting to add or remove elements will raise an `AttributeError`.

```python
>>> fs = frozenset([1, 2, 3])

>>> fs.add(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'

>>> fs.remove(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'remove'
```

### Unique elements

Like sets, frozensets can only contain unique elements. Duplicate values are automatically removed during creation.

```python
>>> fs = frozenset([1, 2, 2, 3])
>>> fs
frozenset({1, 2, 3})
```

### Operations with frozensets

Frozensets support the same set operations as regular sets, but these operations return new frozensets rather than modifying the original.

```python
>>> s = frozenset([1, 2, 3])
>>> t = frozenset([3, 4, 5])

>>> s | t     # union
frozenset({1, 2, 3, 4, 5})

>>> s & t     # intersection
frozenset({3})

>>> s - t     # difference
frozenset({1, 2})

>>> s ^ t     # symmetric difference
frozenset({1, 2, 4, 5})
```

### Hashability

Because frozensets are immutable, they are hashable and can be used as dictionary keys or elements in other sets.

```python
>>> fs1 = frozenset([1, 2, 3])
>>> fs2 = frozenset([4, 5, 6])

>>> my_dict = {fs1: 'first', fs2: 'second'}
>>> my_dict[fs1]
'first'

>>> my_set = {fs1, fs2}
>>> my_set
{frozenset({1, 2, 3}), frozenset({4, 5, 6})}
```

## Dunder methods

| Dunder Method  | Operation            | Example (normal syntax) | Example (dunder call) |
| -------------- | -------------------- | ----------------------- | --------------------- |
| `__contains__` | Membership           | `2 in a`                | `a.__contains__(2)`   |
| `__len__`      | Length               | `len(a)`                | `a.__len__()`         |
| `__iter__`     | Iterate              | `for x in a`            | `a.__iter__()`        |
| `__and__`      | Intersection         | `a & b`                 | `a.__and__(b)`        |
| `__or__`       | Union                | `a \| b`                | `a.__or__(b)`         |
| `__sub__`      | Difference           | `a - b`                 | `a.__sub__(b)`        |
| `__xor__`      | Symmetric difference | `a ^ b`                 | `a.__xor__(b)`        |
| `__eq__`       | Equality             | `a == b`                | `a.__eq__(b)`         |
| `__hash__`     | Hash                 | `hash(a)`               | `a.__hash__()`        |

---

## Frozenset methods

### `copy`

Returns a copy of the frozenset. Since frozensets are immutable, this returns the same frozenset object.

```python
>>> fs = frozenset([1, 2, 3])

>>> fs_copy = fs.copy()

>>> fs_copy
frozenset({1, 2, 3})

>>> fs is fs_copy
True
```

:::note
Since frozensets are immutable, `copy()` returns the same object. There's no need to create a separate copy as the original cannot be modified.
:::

---

### `difference`

Returns a new frozenset containing elements that are in the first frozenset but not in the other frozenset(s).

```python
>>> s = frozenset([1, 2, 3, 4])
>>> t = frozenset([3, 4, 5])

>>> s.difference(t)
frozenset({1, 2})

>>> s - t  # equivalent operation
frozenset({1, 2})
```

Can accept multiple sets as arguments:

```python
>>> s = frozenset([1, 2, 3, 4, 5])
>>> t = frozenset([2, 3])
>>> u = frozenset([3, 4])

>>> s.difference(t, u)
frozenset({1, 5})
```

---

### `intersection`

Returns a new frozenset containing elements that are common to all frozensets.

```python
>>> s = frozenset([1, 2, 3, 4])
>>> t = frozenset([3, 4, 5])

>>> s.intersection(t)
frozenset({3, 4})

>>> s & t  # equivalent operation
frozenset({3, 4})
```

Can accept multiple sets as arguments:

```python
>>> s = frozenset([1, 2, 3, 4, 5])
>>> t = frozenset([2, 3, 4])
>>> u = frozenset([3, 4, 5])

>>> s.intersection(t, u)
frozenset({3, 4})
```

---

### `isdisjoint`

Returns `True` if the frozenset has no elements in common with the other frozenset. Returns `False` if there is at least one common element.

```python
>>> s = frozenset([1, 2, 3])
>>> t = frozenset([4, 5, 6])

>>> s.isdisjoint(t)
True

>>> u = frozenset([3, 4, 5])

>>> s.isdisjoint(u)
False
```

---

### `issubset`

Returns `True` if all elements of the frozenset are contained in the other frozenset. Returns `False` otherwise.

```python
>>> s = frozenset([1, 2, 3])
>>> t = frozenset([1, 2, 3, 4, 5])

>>> s.issubset(t)
True

>>> s <= t  # equivalent operation
True

>>> u = frozenset([1, 2, 6])

>>> s.issubset(u)
False
```

---

### `issuperset`

Returns `True` if the frozenset contains all elements of the other frozenset. Returns `False` otherwise.

```python
>>> s = frozenset([1, 2, 3, 4, 5])
>>> t = frozenset([1, 2, 3])

>>> s.issuperset(t)
True

>>> s >= t  # equivalent operation
True

>>> u = frozenset([1, 2, 6])

>>> s.issuperset(u)
False
```

---

### `symmetric_difference`

Returns a new frozenset containing elements that are in either frozenset, but not in both.

```python
>>> s = frozenset([1, 2, 3, 4])
>>> t = frozenset([3, 4, 5])

>>> s.symmetric_difference(t)
frozenset({1, 2, 5})

>>> s ^ t  # equivalent operation
frozenset({1, 2, 5})
```

---

### `union`

Returns a new frozenset containing all elements from the frozenset and all elements from the other frozenset(s).

```python
>>> s = frozenset([1, 2, 3])
>>> t = frozenset([3, 4, 5])

>>> s.union(t)
frozenset({1, 2, 3, 4, 5})

>>> s | t  # equivalent operation
frozenset({1, 2, 3, 4, 5})
```

Can accept multiple sets as arguments:

```python
>>> s = frozenset([1, 2])
>>> t = frozenset([2, 3])
>>> u = frozenset([3, 4])

>>> s.union(t, u)
frozenset({1, 2, 3, 4})
```
