---
title: Set
sidebar_position: 16
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
>>> dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
```

## Definition

A set is an unordered collection of unique, hashable elements. Sets are used when you need to eliminate duplicates, test membership efficiently, or perform mathematical set operations such as union, intersection, and difference.

## Using sets

Sets are instantiated using curly braces `{}`. However, unlike [dictionaries](./dict), they do not use key value pairs, and thus do not have a colon `:`. 

```python
>>> my_set = {1, 2, 3}
```

### Adding and removing from a set

```python
>>> s = {1, 2}
>>> s.add(3)
>>> s
{1, 2, 3}

>>> s.remove(2)
>>> s
{1, 3}
```

### Unique elements

A set can only contain unique elements. This means that no value will ever be doubled. 

```python
>>> s = {1, 2, 2, 3}
>>> s
{1, 2, 3}

>>> s.add(3)
>>> s
{1, 2, 3}
```

### Operations with sets

```python
>>> s = {1, 2, 3}
>>> t = {3, 4, 5}

>>> s | t     # union
{1, 2, 3, 4, 5}

>>> s & t     # intersection
{3}

>>> s - t     # difference
{1, 2}

>>> s ^ t     # symmetric difference
{1, 2, 4, 5}
```

## Dunder methods

| Dunder Method  | Operation            | Example (normal syntax)       | Example (dunder call)      |
| --- | --- | --- | --- | 
| `__contains__` | Membership           | `2 in {1,2,3}`                | `{1,2,3}.__contains__(2)` |
| `__len__`      | Length               | `len({1,2,3})`                | `{1,2,3}.__len__()`        |
| `__iter__`     | Iteration            | `for x in {1,2,3}`            | `{1,2,3}.__iter__()`       |
| `__and__`      | Intersection         | `{1,2,3} & {2,3,4}` → `{2,3}` | `{1,2,3}.__and__({2,3,4})` |
| `__or__`       | Union                | `{1,2} \| {2,3}`→`{1,2,3}`    | `{1,2}.__or__({2,3})` |
| `__sub__`      | Difference           | `{1,2,3} - {2}` → `{1,3}`     | `{1,2,3}.__sub__({2})`     |
| `__xor__`      | Symmetric difference | `{1,2,3} ^ {2,4}` → `{1,3,4}` | `{1,2,3}.__xor__({2,4})`   |
| `__eq__`       | Equality             | `{1,2} == {2,1}`              | `{1,2}.__eq__({2,1})`      |

---

## Set methods

### `add`

Adds an element to the set. No change is made if the element already exists in the set.

```python
>>> s = {1, 2, 2, 3}

>>> s.add(3)

>>> s
{1, 2, 3}
```

---

### `clear`

Removes all elements from the set.

```python
>>> my_set = {1,2,3,4}

>>> print(my_set)
{1, 2, 3, 4}

>>> my_set.clear()

>>> print(my_set)
set()
```

---

### `copy`

Returns a copy (or clone) of a set.

```python
>>> my_set = {1, 2, 3, 4}

>>> my_other = my_set.copy()

>>> my_other
{1, 2, 3, 4}

>>> my_other.add(5)

>>> my_other
{1, 2, 3, 4, 5}

>>> my_set
{1, 2, 3, 4}
```

:::note
Making a copy of a set like this:

```python
my_other = my_set
```

will only create another variable that refers to the same set. In such a scenario altering `my_set` would also alter `my_other`.
:::

---

### `difference`

Returns a new set containing elements that are in the first set but not in the other set(s).

```python
>>> s = {1, 2, 3, 4}
>>> t = {3, 4, 5}

>>> s.difference(t)
{1, 2}

>>> s - t  # equivalent operation
{1, 2}
```

Can accept multiple sets as arguments:

```python
>>> s = {1, 2, 3, 4, 5}
>>> t = {2, 3}
>>> u = {3, 4}

>>> s.difference(t, u)
{1, 5}
```

---

### `difference_update`

Modifies the set in-place by removing all elements that are also in the other set(s). Returns `None`.

```python
>>> s = {1, 2, 3, 4}
>>> t = {3, 4, 5}

>>> s.difference_update(t)

>>> s
{1, 2}
```

Can accept multiple sets as arguments:

```python
>>> s = {1, 2, 3, 4, 5}
>>> t = {2, 3}
>>> u = {3, 4}

>>> s.difference_update(t, u)

>>> s
{1, 5}
```

---

### `discard`

Removes an element from the set if it is present. Unlike `remove`, `discard` does not raise a `KeyError` if the element is not found.

```python
>>> s = {1, 2, 3, 4}

>>> s.discard(3)

>>> s
{1, 2, 4}

>>> s.discard(5)  # No error raised

>>> s
{1, 2, 4}
```

---

### `intersection`

Returns a new set containing elements that are common to all sets.

```python
>>> s = {1, 2, 3, 4}
>>> t = {3, 4, 5}

>>> s.intersection(t)
{3, 4}

>>> s & t  # equivalent operation
{3, 4}
```

Can accept multiple sets as arguments:

```python
>>> s = {1, 2, 3, 4, 5}
>>> t = {2, 3, 4}
>>> u = {3, 4, 5}

>>> s.intersection(t, u)
{3, 4}
```

---

### `intersection_update`

Modifies the set in-place to keep only elements that are also in the other set(s). Returns `None`.

```python
>>> s = {1, 2, 3, 4}
>>> t = {3, 4, 5}

>>> s.intersection_update(t)

>>> s
{3, 4}
```

Can accept multiple sets as arguments:

```python
>>> s = {1, 2, 3, 4, 5}
>>> t = {2, 3, 4}
>>> u = {3, 4, 5}

>>> s.intersection_update(t, u)

>>> s
{3, 4}
```

---

### `isdisjoint`

Returns `True` if the set has no elements in common with the other set. Returns `False` if there is at least one common element.

```python
>>> s = {1, 2, 3}
>>> t = {4, 5, 6}

>>> s.isdisjoint(t)
True

>>> u = {3, 4, 5}

>>> s.isdisjoint(u)
False
```

---

### `issubset`

Returns `True` if all elements of the set are contained in the other set. Returns `False` otherwise.

```python
>>> s = {1, 2, 3}
>>> t = {1, 2, 3, 4, 5}

>>> s.issubset(t)
True

>>> s <= t  # equivalent operation
True

>>> u = {1, 2, 6}

>>> s.issubset(u)
False
```

---

### `issuperset`

Returns `True` if the set contains all elements of the other set. Returns `False` otherwise.

```python
>>> s = {1, 2, 3, 4, 5}
>>> t = {1, 2, 3}

>>> s.issuperset(t)
True

>>> s >= t  # equivalent operation
True

>>> u = {1, 2, 6}

>>> s.issuperset(u)
False
```

---

### `pop`

Removes and returns an arbitrary element from the set. Raises a `KeyError` if the set is empty.

```python
>>> s = {1, 2, 3, 4}

>>> s.pop()
1

>>> s
{2, 3, 4}

>>> s.pop()
2

>>> s
{3, 4}
```

:::note
Since sets are unordered, `pop` removes an arbitrary element. The element returned may vary between calls.
:::

---

### `remove`

Removes an element from the set. Raises a `KeyError` if the element is not found.

```python
>>> s = {1, 2, 3, 4}

>>> s.remove(2)

>>> s
{1, 3, 4}

>>> s.remove(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 5
```

:::note
Use `discard` if you want to remove an element without raising an error if it doesn't exist.
:::

---

### `symmetric_difference`

Returns a new set containing elements that are in either set, but not in both.

```python
>>> s = {1, 2, 3, 4}
>>> t = {3, 4, 5}

>>> s.symmetric_difference(t)
{1, 2, 5}

>>> s ^ t  # equivalent operation
{1, 2, 5}
```

---

### `symmetric_difference_update`

Modifies the set in-place to keep only elements that are in either set, but not in both. Returns `None`.

```python
>>> s = {1, 2, 3, 4}
>>> t = {3, 4, 5}

>>> s.symmetric_difference_update(t)

>>> s
{1, 2, 5}
```

---

### `union`

Returns a new set containing all elements from the set and all elements from the other set(s).

```python
>>> s = {1, 2, 3}
>>> t = {3, 4, 5}

>>> s.union(t)
{1, 2, 3, 4, 5}

>>> s | t  # equivalent operation
{1, 2, 3, 4, 5}
```

Can accept multiple sets as arguments:

```python
>>> s = {1, 2}
>>> t = {2, 3}
>>> u = {3, 4}

>>> s.union(t, u)
{1, 2, 3, 4}
```

---

### `update`

Modifies the set in-place by adding all elements from the other set(s) or iterable(s). Returns `None`.

```python
>>> s = {1, 2, 3}
>>> t = {3, 4, 5}

>>> s.update(t)

>>> s
{1, 2, 3, 4, 5}
```

Can accept multiple iterables as arguments:

```python
>>> s = {1, 2}

>>> s.update([2, 3], {4, 5})

>>> s
{1, 2, 3, 4, 5}
```

Can also use the `|=` operator:

```python
>>> s = {1, 2, 3}
>>> t = {3, 4, 5}

>>> s |= t

>>> s
{1, 2, 3, 4, 5}
```