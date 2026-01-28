---
title: Bool
sidebar_position: 2
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
>>> dir(bool)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

## Definition

A Boolean value (bool) is a logical value: `True` or `False`.
It answers questions like “Is this statement correct?”
For instance, `1 == 2` is `False`.

`bool` is a subclass of `int`, so in many circumstances booleans are evaulated like numbers.

## Using booleans

If a statement is true then it will evaluate to `True`. Conversely, if a statement is false then it will evaluate to `False`.

```python
>>> 1 == 1
True

>>> 1 == 2
False

>>> "Hello" == "World"
False

>>> "Hello" == "Hello"
True
```

### Types with falsy values

The boolean value of an empty type will always be `False`.

| Type                      | Example          | Notes                      |
| ------------------------- | ---------------- | -------------------------- |
| `bool`                    | `False`          | The literal `False` itself |
| `NoneType`                | `None`           | Represents “no value”      |
| `int`, `float`, `complex` | `0`, `0.0`, `0j` | Any numeric zero           |
| `str`                     | `""`             | Empty string               |
| `list`                    | `[]`             | Empty list                 |
| `tuple`                   | `()`             | Empty tuple                |
| `dict`                    | `{}`             | Empty dictionary           |
| `set`                     | `set()`          | Empty set                  |
| `frozenset`               | `frozenset()`    | Empty frozen set           |
| `range`                   | `range(0)`       | Empty range object         |

Likewise a custom class that ony returns `0` or `False` will be falsy.

### Types with truthy values

The boolean value of a non-empty type will always be `True`.

| Type                      | Example              | Notes |
| ------------------------- | -------------------- | ---- |
| `bool`                    | `True`               | The literal `True` |
| `int`, `float`, `complex` | `1`, `3.14`, `-2+0j` | Any nonzero |
| `str`                     | `"Hello"`            | Any non-empty string |
| `list`                    | `[1, 2, 3]`          | Any non-empty list |
| `tuple`                   | `(1, 2)`             | Any non-empty tuple |
| `dict`                    | `{"a": 1}`           | Any non-empty dictionary |
| `set`                     | `{"x", "y"}`         | Any non-empty set |
| `frozenset`               | `frozenset({1})`     | Any non-empty frozen set |
| `range`                   | `range(1, 5)`        | Any range with at least one value |


### Checking for truthiness

The boolean value of a type can be checked by using the [`bool()`](./built-in#bool) function.

```python
>>> bool("")
False

>>> bool(0)
False

>>> bool("99 problems but a bool aint one")
True
```


## Operations: truth tables

### The `and` operator

| Expression        | Result  | Explanation          |
| ----------------- | ------- | -------------------- |
| `True and True`   | `True`  | Both values are true |
| `True and False`  | `False` | One is false         |
| `False and True`  | `False` | One is false         |
| `False and False` | `False` | Both are false       |

### The `or` operator

| Expression       | Result  | Explanation          |
| ---------------- | ------- | -------------------- |
| `True or True`   | `True`  | At least one is true |
| `True or False`  | `True`  | First value is true  |
| `False or True`  | `True`  | Second value is true |
| `False or False` | `False` | Both are false       |


### The `not` operator

| Expression  | Result  | Explanation       |
| ----------- | ------- | ----------------- |
| `not True`  | `False` | Negates the value |
| `not False` | `True`  | Negates the value |


## Dunder methods
| Dunder Method | Operation | Example (normal syntax)   | Example (dunder call) |
| --- | --- | --- | --- | 
| `__bool__`    | Truth value | `bool(True)` → `True`     | `True.__bool__()`     |
| `__and__`     | Logical AND / Bitwise `&` | `True & False` → `False`  | `True.__and__(False)` |
| `__or__` | Logical OR / Bitwise `\|` | `True \| False` → `True` | `True.__or__(False)` |
| `__xor__`     | Logical XOR / Bitwise `^` | `True ^ False` → `True`   | `True.__xor__(False)` |
| `__invert__`  | Bitwise NOT | `~True` → `-2`     | `True.__invert__()`   |
| `__eq__`      | Equality comparison       | `True == False` → `False` | `True.__eq__(False)`  |
| `__ne__`      | Inequality comparison     | `True != False` → `True`  | `True.__ne__(False)`  |
| `__lt__`      | Less than   | `False < True` → `True`   | `False.__lt__(True)`  |
| `__le__`      | Less than or equal | `True <= True` → `True`   | `True.__le__(True)`   |
| `__gt__`      | Greater than       | `True > False` → `True`   | `True.__gt__(False)`  |
| `__ge__`      | Greater than or equal     | `True >= False` → `True`  | `True.__ge__(False)`  |
| `__add__`     | Addition    | `True + True` → `2`       | `True.__add__(True)`  |
| `__sub__`     | Subtraction | `True - False` → `1`      | `True.__sub__(False)` |
| `__mul__`     | Multiplication     | `True * 5` → `5`   | `True.__mul__(5)`     |
| `__int__`     | Convert to integer | `int(True)` → `1`  | `True.__int__()`      |
| `__float__`   | Convert to float   | `float(False)` → `0.0`    | `False.__float__()`   |
| `__index__`   | Integer index value       | `[10, 20][True]` → `20`   | `True.__index__()`    |
| `__str__`     | String conversion  | `str(True)` → `'True'`    | `True.__str__()`      |
| `__repr__`    | Representation     | `repr(True)` → `'True'`   | `True.__repr__()`     |
| `__hash__`    | Hash value  | `hash(True)` → `1` | `True.__hash__()`     |

---

## Boolean methods

All boolean methods are inherited from [`int`](./int).

### `as_integer_ratio`

Returns a tuple `(numerator, denominator)` representing the boolean as a fraction.

```python
>>> True.as_integer_ratio()
(1, 1)

>>> False.as_integer_ratio()
(0, 1)
```

---

### `bit_count`

Returns the number of `1` bits in the integer representation of the boolean.

```python
>>> True.bit_count()
1

>>> False.bit_count()
0
```

---

### `bit_length`

Returns the number of bits required to represent the boolean as an integer, excluding the sign bit.

```python
>>> True.bit_length()
1

>>> False.bit_length()
0
```

---

### `conjugate`

Returns the complex conjugate of the boolean value. Since booleans are real-valued, this just returns the same integer value (`1` or `0`).

```python
>>> True.conjugate()
1

>>> False.conjugate()
0
```

---

### `denominator`

Returns the denominator of the boolean when viewed as a rational number. It is always `1`.

```python
>>> True.denominator
1

>>> False.denominator
1
```

---

### `from_bytes`

Class method that returns a boolean created from a sequence of bytes. Any non-zero value becomes `True`; zero becomes `False`. It is the inverse of [`to_bytes`](#to_bytes).

```python
>>> int.from_bytes(b"\x01", "big") != 0
True
>>> bool(int.from_bytes(b"\x00", "big"))
False
```

> Note: `from_bytes` is defined on `int`; booleans use the same implementation via inheritance.

---

### `imag`

The imaginary part of the boolean when viewed as a complex number. Always `0`.

```python
>>> True.imag
0
>>> False.imag
0
```

---

### `numerator`

The numerator of the boolean when viewed as a fraction. `True` has numerator `1`; `False` has numerator `0`.

```python
>>> True.numerator
1
>>> False.numerator
0
```

---

### `real`

The real part of the boolean when viewed as a complex number. This is the same as its integer value (`1` or `0`).

```python
>>> True.real
1
>>> False.real
0
```

---

### `to_bytes`

Convert the boolean (as an integer) to a bytes object using a given length and byte order.

```python
>>> True.to_bytes(1, "big")
b'\x01'
>>> False.to_bytes(1, "big")
b'\x00'
```
