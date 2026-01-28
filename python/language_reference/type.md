---
title: Type
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
## Properties

```python
>>> dir(type)
['__abstractmethods__', '__annotations__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__or__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__weakrefoffset__', 'mro']
```

## Definition

`type` is the metaclass for all new-style classes. `type(obj)` returns the object’s class. Calling `type(name, bases, attrs)` dynamically creates a new class. All built-in and user-defined classes are instances of `type`.

```python
>>> type(5)
<class 'int'>
>>> isinstance(int, type)
True
```

## Getting the type of an object

```python
>>> type("hi")
<class 'str'>
>>> type([1, 2, 3]) is list
True
```

## Creating classes dynamically

```python
>>> Point = type("Point", (object,), {"x": 0, "y": 0})
>>> p = Point()
>>> p.x, p.y
(0, 0)
```

## Metaclass hooks

- `__prepare__(name, bases)` — returns the initial class namespace (often a dict).
- `__call__` — called when instantiating the class (constructs instances).
- `__instancecheck__` / `__subclasscheck__` — customize `isinstance` / `issubclass`.

## Dunder methods

| Dunder Method       | Operation              | Example (normal syntax)    | Example (dunder call)         |
| ------------------- | ---------------------- | -------------------------- | ----------------------------- |
| `__call__`          | Create instance        | `int('5')` → `5`           | `int.__call__('5')`           |
| `__instancecheck__` | Used by `isinstance()` | `isinstance(3, int)`       | `int.__instancecheck__(3)`    |
| `__subclasscheck__` | Used by `issubclass()` | `issubclass(bool, int)`    | `int.__subclasscheck__(bool)` |
| `__prepare__`       | Class namespace setup  | `type.__prepare__('X',())` | *(rarely used manually)*      |
