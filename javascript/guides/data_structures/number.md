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

**Numbers** represent numeric values such as counts, prices, indexes, measurements, and coordinates. JavaScript uses one main `number` type for both integers and decimals.

```javascript
const age = 30;
const price = 19.99;
const temperature = -5;

console.log(age + 1); // 31
```

Numbers are primitive values. They are immutable, so operations create new values instead of changing the original number.

## Why this matters

Numbers show up in almost every program: shopping cart totals, animation positions, timers, scores, pagination, form input, and indexes. Understanding JavaScript numbers helps you avoid precision bugs, validate numeric input, and use the `Math` object effectively.

## Creating numbers

Use numeric literals for integers, decimals, negative values, and scientific notation:

```javascript
const integer = 42;
const decimal = 3.14;
const negative = -10;
const large = 1_000_000;
const scientific = 1e6; // 1000000
```

Underscores can make long numbers easier to read. They do not change the value.

## Arithmetic operators

JavaScript supports the standard arithmetic operators:

```javascript
const a = 10;
const b = 3;

console.log(a + b);  // 13
console.log(a - b);  // 7
console.log(a * b);  // 30
console.log(a / b);  // 3.3333333333333335
console.log(a % b);  // 1
console.log(a ** b); // 1000
```

Use parentheses when you need to make order of operations clear:

```javascript
const value = 2 + 3 * 4;
const grouped = (2 + 3) * 4;

console.log(value);   // 14
console.log(grouped); // 20
```

## Updating numeric values

Use compound assignment for counters and totals:

```javascript
let count = 5;

count += 2;
count *= 3;

console.log(count); // 21
```

Use `++` and `--` for simple increments and decrements:

```javascript
let index = 0;

index++;
index++;

console.log(index); // 2
```

## Formatting numbers

Use `toFixed()` when you need a fixed number of decimal places for display:

```javascript
const price = 19.99;
const taxRate = 0.07;
const total = price + price * taxRate;

console.log(total.toFixed(2)); // "21.39"
```

**Important:** `toFixed()` returns a string. Use it for display, not for storing a number you plan to keep calculating with.

Use `toLocaleString()` for user-facing formatting:

```javascript
const amount = 1234567.89;

console.log(amount.toLocaleString()); // "1,234,567.89" in many locales
```

## Parsing numbers from strings

User input and API data often arrive as strings. Convert them before doing numeric work:

```javascript
Number("42");        // 42
Number("3.14");      // 3.14
parseInt("42px");    // 42
parseFloat("3.14em"); // 3.14
```

`Number()` is stricter:

```javascript
Number("42px"); // NaN
parseInt("42px"); // 42
```

Use `Number()` when the whole string should be numeric. Use `parseInt()` or `parseFloat()` when you intentionally want to parse from the beginning of a string.

## `NaN` and `Infinity`

`NaN` means "Not a Number". It appears when a numeric operation cannot produce a meaningful number:

```javascript
0 / 0;          // NaN
"text" / 2;     // NaN
Math.sqrt(-1);  // NaN
```

Use `Number.isNaN()` to check for `NaN`:

```javascript
const value = Number("abc");

console.log(Number.isNaN(value)); // true
```

JavaScript also has `Infinity` and `-Infinity`:

```javascript
console.log(1 / 0);  // Infinity
console.log(-1 / 0); // -Infinity
```

Use `Number.isFinite()` when you need a regular finite number:

```javascript
Number.isFinite(42);       // true
Number.isFinite(Infinity); // false
Number.isFinite(NaN);      // false
```

## Floating-point precision

JavaScript numbers are stored as 64-bit floating-point values. This means decimal math can sometimes look surprising:

```javascript
0.1 + 0.2;       // 0.30000000000000004
0.1 + 0.2 === 0.3; // false
```

This is normal for floating-point arithmetic. For money, store integer cents instead of decimal dollars:

```javascript
const priceInCents = 1999;
const taxInCents = 140;
const totalInCents = priceInCents + taxInCents;

console.log(totalInCents); // 2139
```

## Safe integers

JavaScript can represent only some integers exactly. The safe integer range is:

```javascript
Number.MAX_SAFE_INTEGER; // 9007199254740991
Number.MIN_SAFE_INTEGER; // -9007199254740991
```

Use `Number.isSafeInteger()` when large integer precision matters:

```javascript
Number.isSafeInteger(9007199254740991); // true
Number.isSafeInteger(9007199254740992); // false
```

For integers beyond the safe range, consider `BigInt`.

## The `Math` object

The `Math` object provides common numeric helpers:

```javascript
Math.round(4.6); // 5
Math.floor(4.6); // 4
Math.ceil(4.1);  // 5
Math.abs(-10);   // 10
Math.max(5, 10, 2); // 10
Math.min(5, 10, 2); // 2
```

Use spread syntax with arrays:

```javascript
const numbers = [5, 10, 2, 8];

console.log(Math.max(...numbers)); // 10
console.log(Math.min(...numbers)); // 2
```

## Common patterns

### Validating numeric input

```javascript
function toNumberOrNull(input) {
  const number = Number(input);

  if (!Number.isFinite(number)) {
    return null;
  }

  return number;
}

console.log(toNumberOrNull("42"));  // 42
console.log(toNumberOrNull("abc")); // null
```

### Random integers in a range

`Math.random()` returns a number from `0` up to, but not including, `1`.

```javascript
function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(randomInteger(1, 10)); // random integer from 1 to 10
```

### Rounding for display

```javascript
const average = 87.666666;

console.log(average.toFixed(1)); // "87.7"
```

Remember that `toFixed()` returns a string.

### Comparing decimals with tolerance

When decimal precision matters, compare with a small tolerance:

```javascript
const result = 0.1 + 0.2;
const expected = 0.3;

const isClose = Math.abs(result - expected) < 0.000001;

console.log(isClose); // true
```

## Best practices

- **Validate numeric input**: Use `Number()` and `Number.isFinite()` before trusting external values.
- **Avoid exact decimal equality**: Compare decimals with a tolerance when precision matters.
- **Use integer cents for money**: Avoid storing money as floating-point dollars.
- **Use `toFixed()` for display only**: It returns a string.
- **Use clear names**: Prefer `price`, `count`, `taxRate`, and `index` over vague names.
- **Watch safe integer limits**: Use `Number.isSafeInteger()` for large integer values.
- **Use `Math` helpers**: They make common numeric work clearer.

## Summary

JavaScript uses one main `number` type for integers and decimals. Use arithmetic operators for calculations, `Number()` and parsing functions for conversion, `Number.isFinite()` and `Number.isNaN()` for validation, and `Math` for common numeric helpers. Be careful with floating-point precision, formatted strings, and very large integers.
