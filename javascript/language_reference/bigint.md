---
title: BigInt
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
<!-- ## Properties

```javascript
> Object.getOwnPropertyNames(BigInt.prototype)
['constructor', 'toLocaleString', 'toString', 'valueOf', 'asIntN', 'asUintN']
``` -->

## Definition

`BigInt` is a built-in object that provides a way to represent whole numbers larger than `Number.MAX_SAFE_INTEGER` (2^53 - 1). BigInt values are created by appending `n` to the end of an integer literal or by calling the `BigInt()` constructor.

```javascript
typeof 42n       // "bigint"
typeof BigInt(42) // "bigint"
```

## Using bigint

BigInt values can be created in several ways:

```javascript
// Literal syntax (append 'n')
> 42n
42n

> 9007199254740991n
9007199254740991n

// BigInt constructor
> BigInt(42)
42n

> BigInt("9007199254740991")
9007199254740991n

// From Number.MAX_SAFE_INTEGER
> BigInt(Number.MAX_SAFE_INTEGER)
9007199254740991n
```

## Operations on bigint

### Arithmetic operations

```javascript
const a = 10n
const b = 20n

a + b            // 30n
a - b            // -10n
a * b            // 200n
a / b            // 0n (division truncates, returns BigInt)
a % b            // 10n
a ** b           // 100000000000000000000n
```

### Comparison operations

```javascript
10n < 20n        // true
10n === 10n      // true
10n == 10        // true (loose equality)
10n === 10       // false (strict equality, different types)
```

### Bitwise operations

```javascript
5n & 3n          // 1n (bitwise AND)
5n | 3n          // 7n (bitwise OR)
5n ^ 3n          // 6n (bitwise XOR)
~5n              // -6n (bitwise NOT)
5n << 2n         // 20n (left shift)
5n >> 1n         // 2n (right shift)
```

### Type coercion

BigInt cannot be mixed with Numbers in operations:

```javascript
10n + 20         // TypeError: Cannot mix BigInt and other types
10n * 2          // TypeError: Cannot mix BigInt and other types

// Must convert explicitly
10n + BigInt(20) // 30n
Number(10n) + 20 // 30
```

### Comparisons Work

Comparisons between BigInt and Number work:

```javascript
10n > 5          // true
10n == 10        // true
10n === 10       // false (different types)
```

## Bigint methods

### `BigInt.asIntN()`

Clamps a BigInt value to a signed integer with the given number of bits:

```javascript
BigInt.asIntN(8, 255n)   // -1n (signed 8-bit)
BigInt.asIntN(16, 65535n) // -1n (signed 16-bit)
```

### `BigInt.asUintN()`

Clamps a BigInt value to an unsigned integer with the given number of bits:

```javascript
BigInt.asUintN(8, 255n)   // 255n (unsigned 8-bit)
BigInt.asUintN(16, 65535n) // 65535n (unsigned 16-bit)
```

## Converting bigint

### To Number

```javascript
Number(42n)      // 42
parseInt(42n)    // 42
+42n             // TypeError (unary plus doesn't work)
```

### To String

```javascript
String(42n)      // "42"
42n.toString()   // "42"
42n.toString(2)  // "101010" (binary)
```

### From String

```javascript
BigInt("42")     // 42n
BigInt("0xFF", 16) // 255n (with radix, but BigInt doesn't support radix in constructor)
```

## JSON serialization

BigInt values cannot be serialized to JSON by default:

```javascript
JSON.stringify({ value: 42n })  // TypeError: Do not know how to serialize a BigInt
```

You need to provide a custom replacer:

```javascript
function replacer(key, value) {
  if (typeof value === 'bigint') {
    return value.toString()
  }
  return value
}

JSON.stringify({ value: 42n }, replacer)  // '{"value":"42"}'
```

## Common use cases

### Large Integer Calculations

```javascript
// Calculate factorial of large numbers
function factorial(n) {
  let result = 1n
  for (let i = 2n; i <= n; i++) {
    result *= i
  }
  return result
}

factorial(100n)  // 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000n
```

### Cryptography

```javascript
// Large prime numbers
const largePrime = 982451653n
```

### Timestamps

```javascript
// Nanosecond precision timestamps
const timestamp = BigInt(Date.now()) * 1000000n
```

## Limitations

1. **No decimals**: BigInt can only represent whole numbers.

2. **No Math methods**: Most `Math` methods don't work with BigInt:

```javascript
Math.sqrt(16n)    // TypeError
```

3. **No JSON serialization**: Must use custom replacer.

4. **No unary plus**: `+42n` throws a TypeError.

## Best practices

1. **Use for large integers**: Only use BigInt when you need integers beyond `Number.MAX_SAFE_INTEGER`.

2. **Be explicit with conversions**: Always convert explicitly when mixing with Numbers.

3. **Use literal syntax**: Prefer `42n` over `BigInt(42)` for readability.

4. **Handle JSON carefully**: Provide custom serialization for BigInt values in JSON.

