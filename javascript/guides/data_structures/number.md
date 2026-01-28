---
title: Numbers
sidebar_position: 4.1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are numbers?

**Numbers** are used to represent numeric values in JavaScript. JavaScript has one number type that handles both integers and floating-point numbers. Numbers are one of the primitive data types and are immutable.

```javascript
const age = 30;
const price = 19.99;
const temperature = -5;
```

## Number literals

You can create numbers using numeric literals:

```javascript
const integer = 42;
const decimal = 3.14;
const negative = -10;
const large = 1000000;
const scientific = 1e6;  // 1000000 (1 × 10^6)
```

### Integer literals

Integers are whole numbers without decimal points:

```javascript
const count = 5;
const year = 2024;
const negative = -42;
```

### Floating-point literals

Floating-point numbers include a decimal point:

```javascript
const pi = 3.14159;
const price = 19.99;
const small = 0.001;
```

### Scientific notation

For very large or very small numbers, you can use scientific notation:

```javascript
const million = 1e6;      // 1000000
const billion = 1e9;      // 1000000000
const tiny = 1e-6;        // 0.000001
const verySmall = 2.5e-3; // 0.0025
```

## Number operations

### Arithmetic operators

JavaScript supports standard arithmetic operations:

```javascript
const a = 10;
const b = 3;

a + b;  // 13 (addition)
a - b;  // 7 (subtraction)
a * b;  // 30 (multiplication)
a / b;  // 3.3333333333333335 (division)
a % b;  // 1 (modulo - remainder)
a ** b; // 1000 (exponentiation)
```

### Order of operations

JavaScript follows standard mathematical order of operations (PEMDAS):

```javascript
const result = 2 + 3 * 4;     // 14 (not 20)
const result2 = (2 + 3) * 4;  // 20 (parentheses change order)
```

### Increment and decrement

```javascript
let count = 5;

count++;  // 6 (increment by 1)
count--;  // 5 (decrement by 1)
count += 2; // 7 (add 2)
count -= 1; // 6 (subtract 1)
count *= 2; // 12 (multiply by 2)
count /= 3; // 4 (divide by 3)
```

## Number methods

### Converting to strings

```javascript
const num = 42;

num.toString();      // "42"
num.toString(2);     // "101010" (binary)
num.toString(16);    // "2a" (hexadecimal)
String(num);         // "42" (alternative)
```

### Rounding numbers

```javascript
const num = 3.7;

Math.round(num);     // 4 (rounds to nearest integer)
Math.floor(num);     // 3 (rounds down)
Math.ceil(num);      // 4 (rounds up)
Math.trunc(num);     // 3 (removes decimal part)
```

### Formatting numbers

```javascript
const num = 1234.567;

num.toFixed(2);      // "1234.57" (2 decimal places)
num.toPrecision(5);  // "1234.6" (5 significant digits)
num.toLocaleString(); // "1,234.567" (locale-specific formatting)
```

## Special number values

### Infinity

```javascript
const positiveInfinity = Infinity;
const negativeInfinity = -Infinity;
const result = 1 / 0;  // Infinity
```

### `NaN` (Not a Number)

`NaN` represents a value that is "not a number" (often from invalid operations):

```javascript
const result = 0 / 0;        // NaN
const result2 = "text" / 2;  // NaN
const result3 = Math.sqrt(-1); // NaN

// Checking for NaN
isNaN(result);        // true
Number.isNaN(result); // true (more reliable)
```

### Checking for finite numbers

```javascript
const num = 42;
const inf = Infinity;
const nan = NaN;

isFinite(num);  // true
isFinite(inf);  // false
isFinite(nan);  // false
```

## Number conversion

### Converting strings to numbers

```javascript
const str = "42";

Number(str);        // 42
parseInt(str);      // 42 (parses integer)
parseInt("42.7");   // 42 (stops at decimal)
parseFloat("42.7"); // 42.7 (parses floating-point)
+"42";              // 42 (unary plus operator)
```

### Converting other types to numbers

```javascript
Number(true);   // 1
Number(false);  // 0
Number(null);   // 0
Number(undefined); // NaN
Number("");     // 0
Number(" 42 "); // 42 (trims whitespace)
Number("abc");  // NaN
```

## Common number patterns

### Checking if a value is a number

```javascript
const value = 42;

typeof value === "number";  // true
Number.isInteger(value);    // true (checks if integer)
Number.isFinite(value);     // true (checks if finite number)
```

### Generating random numbers

```javascript
Math.random();                    // Random number between 0 and 1
Math.random() * 10;               // Random number between 0 and 10
Math.floor(Math.random() * 10);   // Random integer between 0 and 9
Math.floor(Math.random() * 10) + 1; // Random integer between 1 and 10

// Random number in a range
function randomInRange(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
randomInRange(5, 10); // Random integer between 5 and 10
```

### Finding min and max

```javascript
Math.min(5, 10, 2);  // 2
Math.max(5, 10, 2);  // 10

const numbers = [5, 10, 2, 8];
Math.min(...numbers); // 2
Math.max(...numbers); // 10
```

### Absolute value

```javascript
Math.abs(-5);  // 5
Math.abs(5);   // 5
```

### Power and square root

```javascript
Math.pow(2, 3);    // 8 (2 to the power of 3)
2 ** 3;            // 8 (exponentiation operator - preferred)
Math.sqrt(16);     // 4
Math.cbrt(8);      // 2 (cube root)
```

## Number precision and limitations

### Floating-point precision

JavaScript uses 64-bit floating-point numbers, which can lead to precision issues:

```javascript
0.1 + 0.2;  // 0.30000000000000004 (not exactly 0.3)
```

For financial calculations, consider using libraries that handle decimal arithmetic, or work with integers (cents instead of dollars).

### Safe integers

JavaScript has a maximum safe integer:

```javascript
Number.MAX_SAFE_INTEGER;  // 9007199254740991
Number.MIN_SAFE_INTEGER;  // -9007199254740991

Number.isSafeInteger(9007199254740991);  // true
Number.isSafeInteger(9007199254740992); // false
```

## Common math methods

```javascript
Math.PI;           // 3.141592653589793
Math.E;            // 2.718281828459045
Math.sin(0);       // 0 (sine)
Math.cos(0);       // 1 (cosine)
Math.tan(0);       // 0 (tangent)
Math.log(10);      // 2.302585092994046 (natural logarithm)
Math.log10(100);   // 2 (base-10 logarithm)
```
