---
title: Float
sidebar_position: 8
date: 28 October 2025
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
>>> dir(float)
['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
```

## Definition

A float is a positive or negative number, or zero,  with a foating point attached to the end. If the number doesn't have a floating point then it is a [`int`](./int). An operation between a float and an int will result in a float, even if the result is a whole number.

```python
>>> type(42.0)
<class 'float'>

>>> type(42.)
<class 'float'>

>>> type(42)
<class 'int'>
```

## Basic operations on floats


### Arithmetic operations

```python
# addition
>>> 10.3 + 3
13.3

# subraction
>>> 10.3 - 3.3
7.0

# multiplication
>>> 7.5*3.8
28.5

# division
>>> 13.86/4.2
3.3

# floor division
>>> 10 // 3
3

# modulus
>>> 10 % 3
1

# exponent
>>> 10 ** 3
1000
```

### Incrementing and immutability

Integers can be incremented by any artimetic operator. However, since integers are immutable a variable must be used to use these incrementing operations.

```python
>>> a = 5
>>> a += 3    # 8
>>> a *= 3    # 24
>>> a **= 2   # 576
>>> a %=6     # 0

>>> 5 *= 2
  File "<stdin>", line 1
    5 *= 2
    ^
SyntaxError: 'literal' is an illegal expression for augmented assignment
```

### Comparison operations

Comparison operations return a [boolean](./bool) value.

```python
# check equality
>>> 5.5 == 8.6
False

# check not equal to
>>> 5.5 != 8.6
True

# greater than
>>> 5.5 > 8.6
False

# less than
>>> 5.5 < 8.6
True

# greater than or equal to
>>> 5.5 >= 8.6
False

# less than or equal to
>>> 5.5 <= 8.6
True
```

### Boolean values

All integers have truthy boolean values except for 0 which has a falsy value.

```python
>>> bool(1.2)
True

>>> bool(-5.0)
True

>>> bool(-0.1)
True

>>> bool(0.0)
False
```

### Readability

Underscores can be added to integers to improve their readability. This does not affect the value of the integer.

```pyhon
>>> 1_000.3 * 5
5001.5

>>> 1_234_567.89 + 13
1234580.89
```

## Dunder methods

| Dunder Method  | Operation        | Example (normal syntax) | Example (dunder call)     |
| -------------- | ---------------- | ----------------------- | ------------------------- |
| `__add__`      | Addition         | `1.5 + 2.5` → `4.0`     | `(1.5).__add__(2.5)`      |
| `__sub__`      | Subtraction      | `3.0 - 1.0` → `2.0`     | `(3.0).__sub__(1.0)`      |
| `__mul__`      | Multiplication   | `2.0 * 4.0` → `8.0`     | `(2.0).__mul__(4.0)`      |
| `__truediv__`  | Division         | `5.0 / 2.0` → `2.5`     | `(5.0).__truediv__(2.0)`  |
| `__floordiv__` | Floor division   | `5.0 // 2.0` → `2.0`    | `(5.0).__floordiv__(2.0)` |
| `__mod__`      | Modulus          | `5.5 % 2.0` → `1.5`     | `(5.5).__mod__(2.0)`      |
| `__pow__`      | Power            | `2.0 ** 3.0` → `8.0`    | `(2.0).__pow__(3.0)`      |
| `__eq__`       | Equality         | `3.0 == 3.0` → `True`   | `(3.0).__eq__(3.0)`       |
| `__lt__`       | Less than        | `2.0 < 5.0` → `True`    | `(2.0).__lt__(5.0)`       |
| `__abs__`      | Absolute value   | `abs(-3.5)` → `3.5`     | `(-3.5).__abs__()`        |
| `__round__`    | Rounding         | `round(3.5)` → `4`      | `(3.5).__round__()`       |
| `__int__`      | Convert to int   | `int(3.9)` → `3`        | `(3.9).__int__()`         |
| `__float__`    | Convert to float | `float(2)` → `2.0`      | `(2).__float__()`         |


## `float` Methods and attributes

### `as_integer_ratio`

Returns a tuple `(numerator, denominator)` representing the float as an exact fraction.

```python
>>> (5.5).as_integer_ratio()
(11, 2)

>>> (-5.5).as_integer_ratio()
(-11, 2)
```

---

### `conjugate`

Returns the complex conjugate of a number. While floats don't have an complex portion the method exists for all number types. 

```python
>>> (5.5).conjugate()
5.5
```

---

### `fromhex`

Returns a float from a string that represents a float. It is the inverse function of [`hex`](#hex)

```python
>>> float.fromhex('0x1.8000000000000p+1')
3
```

---

### `hex`

Returns the string representation of a float. It is the inverse function of [`fromhex`](#fromhex)

```python
>>> (3.0).hex()
'0x1.8000000000000p+1'
```

---

### `imag`

Returns the complex (imaginary) portion of a float. While floats don't have an complex portion the method exists for all number types.

```python
>>> (5.3).imag
0
```

---

### `is_integer`

Returns `True` if the value is an integer. This means that it's a float, but all characters trailing the floating point are 0. Returns `False` if the value is not an integer. This method performed on the `int` type will return an `AttributeError`.

```python
>>> (5.).is_integer()
True

>>> (5.0).is_integer()
True


>>> (5.5).is_integer()
False

>>> (3.14).is_integer()
False

>>> (5).is_integer()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'is_integer'
```


---

### `real`

Returns the real portion of an integer. While integers don't have an complex portion the method exists for all number types.

```python
>>> (55.8).real
55.8
```
