---
title: Int
sidebar_position: 10
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
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

## Definition

An `int` (integer) is a positive or negative whole number or 0. If a number has a trailing decimal `.` it is a [`float`](./float), even if there are no digits trailing the decimal point. Python's integers can be as large as your computer's memory allows.

```python
>>> type(42)
<class 'int'>

>>> type(42.)
<class 'float'>

>>> type(42.0)
<class 'float'>
```


## Basic operations on integers


### Arithmetic operations

```python
# addition
>>> 10 + 3
13

# subraction
>>> 10 - 3
7

# multiplication
>>> 10 * 3
30

# division (always returns a float)
>>> 10 / 3
3.3333333333333335

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
>>> 5 == 8
False

# check not equal to
>>> 5 != 8
True

# greater than
>>> 5 > 8
False

# less than
>>> 5 < 8
True

# greater than or equal to
>>> 5 >= 8
False

# less than or equal to
>>> 5 <= 8
True
```

### Boolean values

All integers have truthy boolean values except for 0 which has a falsy value.

```python
>>> bool(1)
True

>>> bool(-50)
True

>>> bool(0)
False
```

### Readability

Underscores can be added to integers to improve their readability. This does not affect the value of the integer.

```pyhon
>>> 1_000 * 5
5000

>>> 1_234_567 + 13
1234580
```


## Dunder methods

| Dunder Method  | Operation         | Example (normal syntax)   | Example (dunder call) |
| -------------- | ----------------- | ------------------------- | --------------------- |
| `__add__`      | Addition          | `3 + 4` → `7`             | `(3).__add__(4)`      |
| `__sub__`      | Subtraction       | `7 - 2` → `5`             | `(7).__sub__(2)`      |
| `__mul__`      | Multiplication    | `3 * 2` → `6`             | `(3).__mul__(2)`      |
| `__truediv__`  | Division          | `7 / 2` → `3.5`           | `(7).__truediv__(2)`  |
| `__floordiv__` | Floor division    | `7 // 2` → `3`            | `(7).__floordiv__(2)` |
| `__mod__`      | Modulo            | `7 % 2` → `1`             | `(7).__mod__(2)`      |
| `__pow__`      | Exponentiation    | `2 ** 3` → `8`            | `(2).__pow__(3)`      |
| `__neg__`      | Negation          | `-5` → `-5`               | `(5).__neg__()`       |
| `__pos__`      | Unary plus        | `+5` → `5`                | `(5).__pos__()`       |
| `__abs__`      | Absolute value    | `abs(-3)` → `3`           | `(-3).__abs__()`      |
| `__eq__`       | Equality          | `3 == 3` → `True`         | `(3).__eq__(3)`       |
| `__lt__`       | Less than         | `2 < 5` → `True`          | `(2).__lt__(5)`       |
| `__int__`      | Convert to int    | `int(3.0)` → `3`          | `(3.0).__int__()`     |
| `__float__`    | Convert to float  | `float(3)` → `3.0`        | `(3).__float__()`     |
| `__hash__`     | Hash value        | `hash(3)`                 | `(3).__hash__()`      |
| `__index__`    | Used for indexing | `[10,20,30][True]` → `20` | `(1).__index__()`     |

---

## `int` Methods and attributes

### `as_integer_ratio`

Returns a number as a fraction represented by a tuple. The first number is the numerator of the fraction and the second number is the denominator.

```python
>>> (10).as_integer_ratio()
(10, 1)

>>> (10.5).as_integer_ratio()
(21, 2)

# converting a decimal to fraction and back again
>>> x = (44.8).as_integer_ratio()
>>> x[0] / x[1]
44.8
```
---

### `bit_count`

Returns the number of 1 bits consumed by an integer when observed in binary. Below the examples are using [`bin`](./built-in#bin) to display the number in binary form.

```python
>>> bin(0)
'0b0'

>>> (0).bit_count()
0

>>> bin(2)
'0b10'

>>> (2).bit_count()
1

>>> bin(3)
'0b11'

>>> (3).bit_count()
2

>>> bin(15)
'0b1111'

>>> (15).bit_count()
4
```

---

### `bit_length`

Returns the total number of bits (1's and 0's) required to represent the intger in binary. 

```python
>>> bin(0)
'0b0'

>>> (0).bit_length()
0

>>> bin(1)
'0b1'

>>> (1).bit_length()
1

>>> bin(15)
'0b1111'

>>> (15).bit_length()
4

>>> bin(16)
'0b10000'

>>> (16).bit_length()
5
```

---

### `conjugate`

Returns the complex conjugate of a number. While integers don't have an complex portion the method exists for all number types. 

```python
>>> (5).conjugate()
5
>>> (-9).conjugate()
-9
```

---

### `denominator`

Returns the denominator of the integer. While integers always have a denominator of 1 the attribute exists for multiple number types.

```python
>>> (5).denominator
1

>>> (10).denominator
1

>>> (-33).denominator
1
```

---

### `from_bytes`

Returns an interger from a sequence of bytes. It is the inverse of [`to_bytes`](#to_bytes).

syntax:
```python
int.from_bytes(bytes, byteorder, signed=False)
```

---

### `imag`

Returns the complex (imaginary) portion of an integer. While integers don't have an complex portion the method exists for all number types.

```python
>>> (5).imag
0
```

---

### `numerator`

Returns the numerator of the integer. While integers always have a numerator of the number itself the attribute exists for multiple number types.

```python
>>> (5).numerator
5

>>> (-19).numerator
-19
```

---

### `real`

Returns the real portion of an integer. While integers don't have an complex portion the method exists for all number types.

```python
>>> (55).real
55
```

---

### `to_bytes`