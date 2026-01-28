---
title: Complex
sidebar_position: 5
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
>>> dir(complex)
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']
```

## Definition

A `complex` number represents a value with a real part and an imaginary part, written as `a + bj` where `a` is the real component and `b` is the imaginary component. Complex numbers are immutable.

```python
>>> z = 2 + 3j
>>> type(z)
<class 'complex'>

>>> complex(5)        # real only
(5+0j)

>>> complex(1, -2)    # real, imag
(1-2j)

>>> complex("3+4j")   # from string
(3+4j)
```

## Using complex numbers

### Basic arithmetic

```python
>>> (2 + 3j) + (1 + 4j)
(3+7j)

>>> (5 + 2j) - (3 + 1j)
(2+1j)

>>> (2 + 3j) * (1 + 2j)
(-4+7j)

>>> (1 + 2j) / (1 + 1j)
(1.5+0.5j)
```

### Magnitude, conjugate, and parts

```python
>>> z = 3 + 4j

>>> abs(z)            # magnitude
5.0

>>> z.conjugate()     # flip the sign of the imaginary part
(3-4j)

>>> z.real, z.imag    # attributes
(3.0, 4.0)
```

### Boolean value

Complex numbers are truthy unless both parts are zero.

```python
>>> bool(0 + 0j)
False

>>> bool(0 + 2j)
True
```

### Immutability

Complex numbers cannot be modified in place; operations always create new complex values.

## Dunder methods

| Dunder Method | Operation            | Example (normal syntax)              | Example (dunder call)          |
| --- | --- | --- | --- |
| `__add__`       | Addition             | `(2+3j) + (1+4j)` → `(3+7j)`         | `(2+3j).__add__(1+4j)`         |
| `__sub__`       | Subtraction          | `(5+2j) - (3+1j)` → `(2+1j)`         | `(5+2j).__sub__(3+1j)`         |
| `__mul__`       | Multiplication       | `(2+3j)*(1+2j)` → `(-4+7j)`          | `(2+3j).__mul__(1+2j)`         |
| `__truediv__`   | Division             | `(1+2j)/(1+1j)` → `(1.5+0.5j)`       | `(1+2j).__truediv__(1+1j)`     |
| `__abs__`       | Magnitude            | `abs(3+4j)` → `5.0`                  | `(3+4j).__abs__()`             |
| `__neg__`       | Negation             | `-(3+4j)` → `(-3-4j)`                | `(3+4j).__neg__()`             |
| `__eq__`        | Equality             | `(1+2j) == (1+2j)` → `True`          | `(1+2j).__eq__(1+2j)`          |
| `__bool__`      | Truth value          | `bool(0+0j)` → `False`               | `(0+0j).__bool__()`            |
| `__complex__`   | Convert to complex   | `complex(3)` → `(3+0j)`              | `(3).__complex__()`            |
| `__float__`     | Convert to float     | `float(3+0j)` → `3.0`                | `(3+0j).__float__()`           |
| `__repr__`      | Representation       | `repr(1+2j)` → `'(1+2j)'`            | `(1+2j).__repr__()`            |
| `__str__`       | String conversion    | `str(1+2j)` → `'(1+2j)'`             | `(1+2j).__str__()`             |

---

## `complex` Methods and attributes

### `conjugate`

Returns the complex conjugate (negates the imaginary part).

```python
>>> (3 + 4j).conjugate()
(3-4j)
```

---

### `real`

Returns the real component as a float.

```python
>>> (5 + 2j).real
5.0
```

---

### `imag`

Returns the imaginary component as a float.

```python
>>> (5 + 2j).imag
2.0
```
