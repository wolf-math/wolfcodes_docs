---
title: Ellipsis
sidebar_position: 7
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
>>> dir(...)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

## Definition

The ellipsis literal, written as `...`, is a built-in **singleton** object of type `ellipsis`.  
It is commonly used as a placeholder to indicate omitted code, incomplete logic, or “this will be implemented later.”

```python
def future_function():
    ...

class MyClass:
    def method(self):
        ...
```

## Using ellipsis

### Placeholder for incomplete code

`...` is often used instead of `pass` when you want to clearly signal that something is intentionally left unfinished.

```python
def future_function():
    ...

class MyClass:
    def method(self):
        ...
```

### In type hints

Ellipsis can be used in type hints to indicate variadic arguments or incomplete type information:

```python
from typing import Tuple

def process(*args: int) -> Tuple[int, ...]:
    ...

# In function signatures
def func(x: int, ...) -> None:
    ...
```

### In slicing operations (NumPy and other libraries)

Some libraries, particularly NumPy, interpret `...` in slicing operations to mean "all remaining dimensions":

```python
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr[..., 0]  # Selects the first element along the last dimension
```

### Singleton behavior

Every occurrence of `...` refers to the same singleton object:

```python
>>> ... is Ellipsis
True

>>> ... is ...
True

>>> type(...)
<class 'ellipsis'>

>>> id(...) == id(Ellipsis)
True
```

### Boolean value

Ellipsis is truthy:

```python
>>> bool(...)
True

>>> if ...:
...     print("Ellipsis is truthy")
Ellipsis is truthy
```

## Dunder methods

| Dunder Method | Operation | Example (normal syntax) | Example (dunder call) |
| --- | --- | --- | --- |
| `__repr__` | Object representation | `repr(...)` → `'Ellipsis'` | `....__repr__()` |
| `__str__` | String conversion | `str(...)` → `'Ellipsis'` | `....__str__()` |
| `__bool__` | Truth value | `bool(...)` → `True` | `....__bool__()` |
| `__eq__` | Equality comparison | `... == Ellipsis` → `True` | `....__eq__(Ellipsis)` |
| `__ne__` | Inequality comparison | `... != None` → `True` | `....__ne__(None)` |
| `__hash__` | Hash value | `hash(...)` | `....__hash__()` |
| `__lt__` | Less than | `... < Ellipsis` → `False` | `....__lt__(Ellipsis)` |
| `__le__` | Less than or equal | `... <= Ellipsis` → `True` | `....__le__(Ellipsis)` |
| `__gt__` | Greater than | `... > Ellipsis` → `False` | `....__gt__(Ellipsis)` |
| `__ge__` | Greater than or equal | `... >= Ellipsis` → `True` | `....__ge__(Ellipsis)` |
