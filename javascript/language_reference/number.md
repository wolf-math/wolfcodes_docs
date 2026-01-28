---
title: Number
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
<!-- ## Properties

```javascript
> Object.getOwnPropertyNames(Number.prototype)
['constructor', 'toExponential', 'toFixed', 'toPrecision', 'toString', 'valueOf', 'toLocaleString']
``` -->

## Definition

A `Number` is a numeric data type in JavaScript. JavaScript uses the IEEE 754 double-precision floating-point format for all numbers, meaning **numbers can be integers or floating-point values**.

```javascript
> typeof 42
"number"

> typeof 3.14
"number"

> typeof -10
"number"
```

## Using numbers

Numbers can be created using literals or the `Number` constructor (not recommended).

```javascript
// Literal syntax
> 42
42

> 3.14
3.14

> -10
-10

> 0.5
0.5

// Scientific notation
> 1e5
100000

> 1e-5
0.00001

// Number constructor
> new Number(42)
[Number: 42]

> Number(42)
42
```

### Special number values

#### `Infinity` and `-Infinity`

Represent positive and negative infinity.

```javascript
> Infinity
Infinity

> -Infinity
-Infinity

> 1 / 0
Infinity

> -1 / 0
-Infinity
```

#### `NaN` (Not-a-Number)

Represents a value that is not a valid number.

```javascript
> NaN
NaN

> 0 / 0
NaN

> Number('hello')
NaN
```

:::note
`NaN` is the only value that is not equal to itself.
::: 

```javascript
> NaN === NaN
false

> isNaN(NaN)
true

> Number.isNaN(NaN)
true
```

## Operations on numbers

JavaScript provides various operations that can be performed on numbers through operators and built-in methods.

| Operation | Syntax | Example | Result |
| --- | --- | --- | --- |
| Addition | `+` | `3 + 4` | `7` |
| Subtraction | `-` | `7 - 2` | `5` |
| Multiplication | `*` | `3 * 2` | `6` |
| Division | `/` | `7 / 2` | `3.5` |
| Modulo | `%` | `7 % 2` | `1` |
| Exponentiation | `**` | `2 ** 3` | `8` |
| Negation | `-` | `-5` | `-5` |
| Unary plus | `+` | `+5` | `5` |
| Absolute value | `Math.abs()` | `Math.abs(-3)` | `3` |
| Equality (strict) | `===` | `3 === 3` | `true` |
| Equality (loose) | `==` | `3 == 3` | `true` |
| Less than | `<` | `2 < 5` | `true` |
| Greater than | `>` | `5 > 2` | `true` |
| Convert to string | `toString()` | `(3).toString()` | `"3"` |
| Convert to number | `Number()` | `Number("3")` | `3` |

### Arithmetic operations

```javascript
// Addition
> 10 + 3
13

// Subtraction
> 10 - 3
7

// Multiplication
> 10 * 3
30

// Division
> 10 / 3
3.3333333333333335

// Modulus
> 10 % 3
1

// Exponentiation
> 10 ** 3
1000

> Math.pow(10, 3)
1000
```

### Incrementing and decrementing

Numbers can be incremented or decremented using the `++` and `--` operators. However, since numbers are immutable primitives, a variable must be used for these operations.

```javascript
> let a = 5
undefined

// execute then increment
> a++
5

> a
6

// increment then execute
> ++a
7

> a
7

// execute then decrement
> a--
7

> a
6

// decrement then execute
> --a
5

> a
5

// Augmented assignment
> a += 3
8

> a *= 3
24

> a **= 2
576

> a %= 6
0
```

### Comparison operations

Comparison operations return a boolean value.

```javascript
// Check equality
> 5 == 8
false

// Check value and type (triple equals)
> 5 === 5
true

// Check only value (double equals)
> "5" == 5
true

> 5 === 8
false

// Check not equal to
> 5 != 8
true

> 5 !== 8
true

// Greater than
> 5 > 8
false

// Less than
> 5 < 8
true

// Greater than or equal to
> 5 >= 8
false

// Less than or equal to
> 5 <= 8
true
```

### Boolean values

All numbers have truthy boolean values except for `0`, `-0`, and `NaN` which have falsy values.

```javascript
> Boolean(1)
true

> Boolean(-50)
true

> Boolean(0)
false

> Boolean(-0)
false

> Boolean(NaN)
false
```

### Readability

Underscores can be added to numbers to improve their readability. This does not affect the value of the number.

```javascript
> 1_000 * 5
5000

> 1_234_567 + 13
1234580
```

## Number methods

### `toExponential`

Returns a string representing the number in exponential notation.

```javascript
> (1234).toExponential()
"1.234e+3"

> (1234).toExponential(2)
"1.23e+3"
```

---

### `toFixed`

Formats a number using fixed-point notation.

```javascript
> (3.14159).toFixed(2)
"3.14"

> (42).toFixed(2)
"42.00"
```

---

### `toPrecision`

Formats a number to a specified precision.

```javascript
> (3.14159).toPrecision(3)
"3.14"

> (42).toPrecision(3)
"42.0"
```

---

### `toString`

Converts a number to a string.

```javascript
> (42).toString()
"42"

> (42).toString(2)
"101010"

> (42).toString(16)
"2a"
```

---

### `toLocaleString`

Returns a string with a language-sensitive representation of the number.

```javascript
> (1234567.89).toLocaleString()
"1,234,567.89"

> (1234567.89).toLocaleString('de-DE')
"1.234.567,89"
```

---

### `valueOf`

Returns the primitive value of a number object.

```javascript
> const num = new Number(42)
undefined

> num.valueOf()
42
```

---

## Number static methods

### `Number.isNaN`

Determines whether the passed value is `NaN` without coercion.

```javascript
> Number.isNaN(NaN)
true

> Number.isNaN('hello')
false

> isNaN('hello')
true
```

---

### `Number.isFinite`

Determines whether the passed value is a finite number.

```javascript
> Number.isFinite(42)
true

> Number.isFinite(Infinity)
false

> Number.isFinite(NaN)
false
```

---

### `Number.isInteger`

Determines whether the passed value is an integer.

```javascript
> Number.isInteger(42)
true

> Number.isInteger(42.5)
false

> Number.isInteger(42.0)
true
```

---

### `Number.isSafeInteger`

Determines whether the passed value is a safe integer (between `Number.MIN_SAFE_INTEGER` and `Number.MAX_SAFE_INTEGER`).

```javascript
> Number.isSafeInteger(42)
true

> Number.isSafeInteger(Number.MAX_SAFE_INTEGER + 1)
false
```

---

### `Number.parseInt`

Parses a string and returns an integer.

```javascript
> Number.parseInt('42')
42

> Number.parseInt('42.7')
42

> Number.parseInt('1010', 2)
10
```

---

### `Number.parseFloat`

Parses a string and returns a floating-point number.

```javascript
> Number.parseFloat('3.14')
3.14

> Number.parseFloat('42')
42
```

---

## Number properties

### `Number.MAX_VALUE`

The largest positive representable number.

```javascript
> Number.MAX_VALUE
1.7976931348623157e+308
```

---

### `Number.MIN_VALUE`

The smallest positive representable number (closest to zero).

```javascript
> Number.MIN_VALUE
5e-324
```

---

### `Number.MAX_SAFE_INTEGER`

The maximum safe integer in JavaScript (2^53 - 1).

```javascript
> Number.MAX_SAFE_INTEGER
9007199254740991
```

---

### `Number.MIN_SAFE_INTEGER`

The minimum safe integer in JavaScript (-(2^53 - 1)).

```javascript
> Number.MIN_SAFE_INTEGER
-9007199254740991
```

---

### `Number.EPSILON`

The smallest interval between two representable numbers.

```javascript
> Number.EPSILON
2.220446049250313e-16
```

---

### `Number.POSITIVE_INFINITY`

Same as `Infinity`.

```javascript
> Number.POSITIVE_INFINITY
Infinity
```

---

### `Number.NEGATIVE_INFINITY`

Same as `-Infinity`.

```javascript
> Number.NEGATIVE_INFINITY
-Infinity
```

---

### `Number.NaN`

Same as `NaN`.

```javascript
> Number.NaN
NaN
```

