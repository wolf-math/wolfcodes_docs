---
title: Object
sidebar_position: 14
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
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

## Definition

`object` is the base class of all new-style classes in Python. Every class ultimately inherits from `object`, which provides default implementations for core behaviors like representation, equality, hashing, and attribute access.

```python
>>> class X: pass
>>> isinstance(X(), object)
True
```

## Subclassing object

Explicitly inheriting from `object` is optional in Python 3, but the behaviors come from it regardless.

```python
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

## Attribute access hooks

- `__getattribute__` — intercepts all attribute access.
- `__setattr__` / `__delattr__` — customize assignment/deletion.

Use with care to avoid infinite recursion; delegate to `super().__getattribute__` as needed.

## Descriptor protocol

Objects implementing `__get__`, `__set__`, or `__delete__` act as descriptors (used by properties, methods, etc.).

## Dunder methods

| Dunder Method      | Operation                | Example (normal syntax) | Example (dunder call)          |
| ------------------ | ------------------------ | ----------------------- | ------------------------------ |
| `__init__`         | Initialize               | `object()`              | `object().__init__()`          |
| `__str__`          | String representation    | `str(object())`         | `object().__str__()`           |
| `__repr__`         | Developer representation | `repr(object())`        | `object().__repr__()`          |
| `__eq__`           | Equality                 | `object() == object()`  | `object().__eq__(object())`    |
| `__hash__`         | Hash value               | `hash(object())`        | `object().__hash__()`          |
| `__getattribute__` | Attribute lookup         | `obj.attr`              | `obj.__getattribute__('attr')` |
| `__setattr__`      | Attribute set            | `obj.attr = 1`          | `obj.__setattr__('attr',1)`    |
| `__delattr__`      | Attribute delete         | `del obj.attr`          | `obj.__delattr__('attr')`      |

| Dunder Method | Operation        | Example (normal syntax) | Example (dunder call)          |
| ------------- | ---------------- | ----------------------- | ------------------------------ |
| `__get__`     | Access attribute | `obj.x`                 | `prop.__get__(obj, type(obj))` |
| `__set__`     | Assign value     | `obj.x = 5`             | `prop.__set__(obj, 5)`         |
| `__delete__`  | Delete value     | `del obj.x`             | `prop.__delete__(obj)`         |
