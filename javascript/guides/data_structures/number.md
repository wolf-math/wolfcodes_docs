---
title: Numbers
description: How JavaScript numbers work, including literals, operations, conversion, precision limits, and common patterns.
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

## What Are numbers?

In JavaScript, **numbers** represent numeric values such as counts, prices, and measurements. JavaScript has a single `number` type that handles both integers and floating‑point (decimal) values, and it is one of the primitive, immutable types.

Key characteristics:

- Numbers are stored as 64‑bit floating‑point values (IEEE‑754)
- Integers and decimals share the same `number` type
- Many operations are handled via the `Math` object

Minimal example:

```javascript
const age = 30;        // integer
const price = 19.99;   // floating‑point
const temperature = -5; // negative integer
```

## Why this matters

Numbers are at the core of almost every JavaScript program. You use them to represent quantities (like items in a cart), prices and taxes, UI measurements (like widths and positions), timestamps, and internal counters or indexes.

Understanding how JavaScript numbers work helps you:

- Avoid subtle bugs from floating‑point precision (for example, `0.1 + 0.2`)
- Correctly parse and validate numeric input from users and APIs
- Safely handle very large or very small values, including infinities and `NaN`
- Use the built‑in `Math` utilities to compute derived values cleanly

Getting comfortable with numbers early makes later topics like dates, animations, and financial calculations much easier to reason about.

## Basic syntax or core form

You create numbers with numeric literals. JavaScript supports integers, decimals, and scientific notation:

```javascript
const integer = 42;
const decimal = 3.14;
const negative = -10;
const large = 1_000_000;  // underscore for readability
const scientific = 1e6;   // 1000000 (1 × 10^6)
```

JavaScript also has standard arithmetic operators:

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

### Simple example

Here is a small example that computes a total with tax:

```javascript
const price = 19.99;
const taxRate = 0.07;               // 7%

const tax = price * taxRate;        // 1.3993
const total = price + tax;          // 21.3893

total.toFixed(2);                   // "21.39" (formatted for display)
```

### Example with return value / behavior

This function uses numbers to calculate a discounted price and returns a rounded value:

```javascript
function calculateDiscountedPrice(price, discountPercent) {
  const discount = price * (discountPercent / 100);
  const result = price - discount;

  // Round to 2 decimal places for display purposes
  return Number(result.toFixed(2));
}

calculateDiscountedPrice(50, 10); // 45
calculateDiscountedPrice(19.99, 15); // 16.99
```

## Using or invoking the concept

You most often use numbers inside expressions, assignments, and function calls.

Basic usage with arithmetic and order of operations:

```javascript
const base = 2;
const exponent = 3;
const result = base ** exponent; // 8

const value = 2 + 3 * 4;     // 14 (multiplication happens before addition)
const value2 = (2 + 3) * 4;  // 20 (parentheses change the order)
```

Using increment and compound assignment for counters:

```javascript
let count = 5;

count++;   // 6 (increment by 1)
count--;   // 5 (decrement by 1)
count += 2; // 7 (add 2)
count *= 2; // 14 (multiply by 2)
```

Numbers are also passed to and returned from functions:

```javascript
function add(a, b) {
  return a + b;
}

add(2, 3);   // 5
add(-1, 10); // 9
```

## Parameters, inputs, or variations

Numbers appear in several literal forms and can be derived from different kinds of input.

### Literal variations

**Integer literals** are whole numbers without a decimal point:

```javascript
const count = 5;
const year = 2024;
const negative = -42;
```

**Floating‑point literals** include a decimal point:

```javascript
const pi = 3.14159;
const price = 19.99;
const small = 0.001;
```

**Scientific notation** is convenient for very large or very small values:

```javascript
const million = 1e6;      // 1000000
const billion = 1e9;      // 1000000000
const tiny = 1e-6;        // 0.000001
const verySmall = 2.5e-3; // 0.0025
```

### Parsing from strings

When numbers come from user input or external systems, they usually arrive as strings. JavaScript provides multiple ways to convert them:

```javascript
const str = "42";

Number(str);        // 42 (preferred for full-string conversion)
parseInt(str);      // 42 (parses integer)
parseInt("42.7");   // 42 (stops at decimal)
parseFloat("42.7"); // 42.7 (parses floating-point)
+"42";              // 42 (unary plus operator)
```

Be aware that `parseInt` and `parseFloat` ignore trailing non‑numeric characters, while `Number` is stricter and returns `NaN` on invalid input.

### Coercing other types

Other primitives can also be coerced into numbers:

```javascript
Number(true);      // 1
Number(false);     // 0
Number(null);      // 0
Number(undefined); // NaN
Number("");        // 0
Number(" 42 ");    // 42 (trims whitespace)
Number("abc");     // NaN
```

Understanding these rules helps you avoid surprises when working with loosely typed data.

## Default behavior

JavaScript defines default behavior for invalid operations and certain edge cases.

### Basic default example: `NaN` and `Infinity`

When an operation has no meaningful numeric result, JavaScript produces `NaN`:

```javascript
0 / 0;           // NaN
"text" / 2;      // NaN
Math.sqrt(-1);   // NaN
```

Dividing by zero or overflowing the numeric range produces infinities:

```javascript
const positiveInfinity = Infinity;
const negativeInfinity = -Infinity;

1 / 0;   // Infinity
-1 / 0;  // -Infinity
```

### Important: Checking for `NaN` and Finite Values

Use `Number.isNaN` to reliably check for `NaN`, and `Number.isFinite` or `isFinite` to detect normal numbers:

```javascript
const value = 0 / 0;        // NaN

isNaN(value);        // true
Number.isNaN(value); // true (preferred)

const num = 42;
const inf = Infinity;

isFinite(num);  // true
isFinite(inf);  // false
isFinite(NaN);  // false
```

These checks are essential when validating user input or results from complex calculations.

## Rules and constraints

JavaScript numbers follow a few important rules:

1. All numeric literals (integers and decimals) are of type `number`.
2. Numbers are represented as 64‑bit floating‑point values (IEEE‑754).
3. Only integers between `Number.MIN_SAFE_INTEGER` and `Number.MAX_SAFE_INTEGER` can be represented exactly.
4. Decimal fractions like `0.1` and `0.2` cannot always be represented exactly, which can cause rounding issues.

Safe integer boundaries:

```javascript
Number.MAX_SAFE_INTEGER;  // 9007199254740991
Number.MIN_SAFE_INTEGER;  // -9007199254740991

Number.isSafeInteger(9007199254740991); // true
Number.isSafeInteger(9007199254740992); // false
```

Common floating‑point surprise:

```javascript
0.1 + 0.2;  // 0.30000000000000004 (not exactly 0.3)
```

To avoid errors in financial code, it is common to work in integers (for example, cents instead of dollars) or use a dedicated decimal library.

## Inspection

JavaScript offers a few simple ways to inspect numeric values and metadata:

- `typeof value` shows that a value is a `number`
- `Number.isInteger(value)` checks whether a number is an integer
- `Number.isFinite(value)` checks for non‑`NaN`, non‑infinite numbers
- `num.toString(radix)` converts a number to a string in a chosen base

Examples:

```javascript
const value = 42;

typeof value;             // "number"
Number.isInteger(value);  // true
Number.isFinite(value);   // true

value.toString(2);        // "101010" (binary)
value.toString(16);       // "2a" (hexadecimal)
```

These helpers are especially useful for debugging and logging.

## Common patterns

### Validating numeric input

When accepting user input, always verify that a value is a useful number:

```javascript
function toNumberOrNull(input) {
  const num = Number(input);

  if (!Number.isFinite(num)) {
    return null;
  }

  return num;
}

toNumberOrNull("42");     // 42
toNumberOrNull("abc");    // null
toNumberOrNull("Infinity"); // null
```

### Generating random integers in a range

`Math.random()` returns a number in `[0, 1)`. You can scale and shift it to get integers in a specific range:

```javascript
// Random integer between 0 and 9
Math.floor(Math.random() * 10);

// Random integer between 1 and 10
Math.floor(Math.random() * 10) + 1;

// Random integer between min and max (inclusive)
function randomInRange(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

randomInRange(5, 10); // Random integer between 5 and 10
```

### Finding minimum and maximum values

Use `Math.min` and `Math.max` with individual values or arrays:

```javascript
Math.min(5, 10, 2);  // 2
Math.max(5, 10, 2);  // 10

const numbers = [5, 10, 2, 8];

Math.min(...numbers); // 2
Math.max(...numbers); // 10
```

### Absolute differences

`Math.abs` is useful for distances and differences where the sign does not matter:

```javascript
const expected = 100;
const actual = 92;

const difference = Math.abs(actual - expected); // 8
```

### Powers, roots, and common math functions

The `Math` object provides many helpers for more advanced calculations:

```javascript
Math.pow(2, 3);  // 8 (2 to the power of 3)
2 ** 3;          // 8 (exponentiation operator - preferred)
Math.sqrt(16);   // 4
Math.cbrt(8);    // 2 (cube root)

Math.PI;         // 3.141592653589793
Math.E;          // 2.718281828459045
Math.sin(0);     // 0
Math.cos(0);     // 1
Math.tan(0);     // 0
Math.log10(100); // 2 (base‑10 logarithm)
```

## Best practices

- **Validate numeric input explicitly**: Use `Number()`, `Number.isFinite`, and `Number.isNaN` instead of assuming input is valid.
- **Avoid relying on floating‑point equality**: Compare with tolerances instead of `a === b` when decimals are involved.
- **Prefer integers for money**: Represent cents as integers or use a decimal library for financial calculations.
- **Use clear names**: Prefer `price`, `count`, `taxRate`, `index` over single letters except in very small scopes.
- **Keep expressions simple**: Break long arithmetic expressions into intermediate variables to improve readability.
- **Use `toFixed`/`toLocaleString` only for display**: Do not store or re‑use formatted strings as numbers.
- **Stay within safe integer range**: When working with large IDs or counters, verify they are safe integers.

## Summary

JavaScript numbers cover both integers and decimals under a single `number` type, backed by 64‑bit floating‑point representation. You create them with literals, combine them with arithmetic operators, and refine their behavior using the `Math` utilities and conversion functions. By understanding precision limits, special values like `NaN` and `Infinity`, and a few common patterns, you can work with numeric data in JavaScript confidently and predictably.

