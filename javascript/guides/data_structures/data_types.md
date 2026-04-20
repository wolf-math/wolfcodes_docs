---
title: Data Types
sidebar_position: 4
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are data types?

**Data types** describe what kind of value you are working with. A value's type affects what you can do with it: add it, compare it, loop over it, call methods on it, store properties on it, or use it in a condition.

```javascript
const name = "Alice";  // string
const age = 30;        // number
const isAdmin = false; // boolean
const scores = [90, 85, 100]; // array
```

JavaScript has two broad groups of values:

- **Primitive values**: simple values like strings, numbers, booleans, `null`, and `undefined`
- **Reference values**: objects, arrays, and functions

## Why this matters

Types shape how JavaScript behaves. The same operator can do different things depending on the types involved:

```javascript
5 + 3;     // 8
"5" + 3;   // "53"
"5" - 3;   // 2
```

Understanding data types helps you predict what your code will do, avoid confusing type coercion bugs, and choose the right checks before using a value.

## Primitive values

Primitive values are the simplest values in JavaScript. They are **immutable**, which means the value itself cannot be changed. When you "change" a primitive value, you are really creating or assigning a new value.

JavaScript's main primitive types are:

- `string`
- `number`
- `bigint`
- `boolean`
- `null`
- `undefined`
- `symbol`

You will use strings, numbers, booleans, `null`, and `undefined` constantly. `bigint` and `symbol` are more specialized.

### Strings

A **string** is text. Strings can use double quotes, single quotes, or backticks:

```javascript
const firstName = "Alice";
const greeting = 'Hello';
const message = `Hello, ${firstName}!`;

console.log(message); // "Hello, Alice!"
```

Backticks create **template literals**, which are useful when a string includes variables. You'll learn more in the [strings guide](./strings).

### Numbers

JavaScript uses one main `number` type for integers and decimals:

```javascript
const age = 30;
const price = 9.99;
const temperature = -4;
const largeNumber = 1e6; // 1000000
```

**Important:** JavaScript numbers use floating-point math, so some decimal calculations can look surprising:

```javascript
0.1 + 0.2;       // 0.30000000000000004
0.1 + 0.2 === 0.3; // false
```

This is normal in many programming languages. For money, use integer cents or a decimal library instead of relying on exact decimal equality.

### BigInts

A **BigInt** represents an integer larger than regular JavaScript numbers can safely handle. Add `n` to the end of an integer literal:

```javascript
const huge = 9007199254740993n;
```

You usually will not need `BigInt` as a beginner. Use regular numbers unless you specifically need very large integers.

### Booleans

A **boolean** is either `true` or `false`:

```javascript
const isLoggedIn = true;
const hasPermission = false;
```

Booleans are common in conditionals:

```javascript
if (isLoggedIn) {
  console.log("Welcome back");
}
```

### `null`

`null` means "intentionally no value":

```javascript
const selectedUser = null;
```

Use `null` when your code deliberately needs to represent an empty or missing value.

### `undefined`

`undefined` usually means a value has not been set:

```javascript
let name;
console.log(name); // undefined

const user = {};
console.log(user.email); // undefined
```

You usually do not need to assign `undefined` yourself. Let JavaScript use it for values that are not set, and use `null` when you want to intentionally say "no value."

### Symbols

A **symbol** is a unique value often used as an object property key:

```javascript
const id = Symbol("id");
```

Symbols are useful in advanced object patterns, but they are uncommon in beginner code.

## Reference values

Reference values are values that can hold other values. Objects, arrays, and functions are reference values.

### Objects

An **object** stores key-value pairs:

```javascript
const user = {
  name: "Alice",
  age: 30
};

console.log(user.name); // "Alice"
```

Objects are covered in more detail in the [objects guide](./objects).

### Arrays

An **array** stores an ordered list of values:

```javascript
const scores = [90, 85, 100];

console.log(scores[0]); // 90
```

Arrays are covered in more detail in the [arrays guide](./arrays).

### Functions

Functions are also values in JavaScript. You can store a function in a variable, pass it to another function, or return it from a function:

```javascript
const greet = function(name) {
  return `Hello, ${name}!`;
};

console.log(greet("Alice")); // "Hello, Alice!"
```

Functions are covered in more detail in the [functions guide](../functions/function).

## Primitive vs reference values

A useful mental model:

- Primitive values are copied by value.
- Reference values are copied by reference.

### Primitive values are copied

```javascript
let a = 1;
let b = a;

b = 2;

console.log(a); // 1
console.log(b); // 2
```

Changing `b` does not affect `a` because numbers are primitive values.

### Reference values share the same object

```javascript
const first = [1, 2, 3];
const second = first;

second.push(4);

console.log(first);  // [1, 2, 3, 4]
console.log(second); // [1, 2, 3, 4]
```

Both `first` and `second` refer to the same array, so mutating the array through one name affects what you see through the other.

You'll see this again when learning about [reassignment vs mutation](./variables_and_values#reassignment-vs-mutation).

## Dynamic typing

JavaScript is **dynamically typed**. A variable can hold values of different types over time:

```javascript
let value = 5;
value = "hello";
value = true;

console.log(value); // true
```

This flexibility can be convenient, but it can also make bugs easier to create. In most code, keep a variable's meaning consistent. If `value` starts as a number count, do not later reuse it for a string message.

## Checking types with `typeof`

The `typeof` operator tells you the type of many values:

```javascript
typeof "hello";   // "string"
typeof 42;        // "number"
typeof 10n;       // "bigint"
typeof true;      // "boolean"
typeof undefined; // "undefined"
typeof Symbol();  // "symbol"
```

It also has a few important quirks:

```javascript
typeof null;        // "object" (a long-standing JavaScript bug)
typeof [1, 2, 3];   // "object" (arrays are objects)
typeof { name: "Alice" }; // "object"
typeof function() {}; // "function"
```

**Important:** To check for `null`, use strict equality:

```javascript
const value = null;

value === null; // true
```

To check if a value is an array, use `Array.isArray()`:

```javascript
const items = [1, 2, 3];

Array.isArray(items); // true
```

## Truthy and falsy values

In JavaScript, every value behaves like either `true` or `false` in a boolean context, such as an `if` statement. Values that behave like `true` are **truthy**. Values that behave like `false` are **falsy**.

### Falsy values

These values are falsy:

```javascript
false;
0;
-0;
0n;
"";
null;
undefined;
NaN;
```

Everything else is truthy.

### Truthy examples

```javascript
if ("hello") {
  console.log("Non-empty strings are truthy");
}

if (42) {
  console.log("Non-zero numbers are truthy");
}

if ([]) {
  console.log("Empty arrays are truthy");
}

if ({}) {
  console.log("Empty objects are truthy");
}
```

### Common pitfalls

Empty strings are falsy:

```javascript
const name = "";

if (name) {
  console.log("Name exists");
}
```

Zero is falsy, so be explicit when zero is a valid value:

```javascript
const count = 0;

// This will not run because 0 is falsy
if (count) {
  console.log("Has items");
}

// Better: check the exact condition
if (count > 0) {
  console.log("Has items");
}
```

Empty arrays and empty objects are truthy:

```javascript
const items = [];

// This will run because arrays are truthy, even when empty
if (items) {
  console.log("This array exists");
}

// Better: check the length
if (items.length > 0) {
  console.log("This array has items");
}
```

You'll use truthy and falsy values often in conditionals. The [conditionals guide](../control_flow/conditionals) covers this in context.

## Type conversion

JavaScript can convert values from one type to another.

### Explicit conversion

Use explicit conversion when you want the conversion to be obvious:

```javascript
Number("42");       // 42
parseInt("42");     // 42
parseFloat("3.14"); // 3.14

String(42);         // "42"
Boolean("hello");   // true
Boolean("");        // false
```

Prefer `Boolean(value)` over `!!value` in beginner-facing code. Both work, but `Boolean(value)` is easier to read.

### Implicit conversion

JavaScript sometimes converts values automatically. This is called **type coercion**:

```javascript
"5" + 3;  // "53"
"5" - 3;  // 2
"5" * 2;  // 10
true + 1; // 2
```

This behavior is one reason to use strict equality:

```javascript
5 == "5";  // true
5 === "5"; // false
```

Use `===` and `!==` unless you specifically want JavaScript to coerce types. The [variables and values guide](./variables_and_values) explains this in more detail.

## Common patterns

### Checking for missing values

Use strict equality when you care about one specific missing value:

```javascript
const user = null;

if (user === null) {
  console.log("No user selected");
}
```

If you intentionally want to treat both `null` and `undefined` as missing, check for both:

```javascript
if (user === null || user === undefined) {
  console.log("User is missing");
}
```

### Checking for arrays

Use `Array.isArray()` instead of `typeof`:

```javascript
const value = [1, 2, 3];

if (Array.isArray(value)) {
  console.log("This is an array");
}
```

### Checking whether a string has text

Use `.length` when you specifically care whether a string contains characters:

```javascript
const name = "";

if (name.length > 0) {
  console.log("Name has text");
}
```

## Best practices

- **Use strict equality**: Prefer `===` and `!==` so JavaScript does not silently coerce types.
- **Use explicit conversion**: `Number(value)`, `String(value)`, and `Boolean(value)` make your intent clear.
- **Be careful with truthiness**: It is useful, but use explicit checks when `0`, `""`, `null`, and `undefined` mean different things.
- **Check arrays with `Array.isArray()`**: `typeof` reports arrays as `"object"`.
- **Keep variable meanings consistent**: Dynamic typing allows type changes, but reusing one variable for unrelated types makes code harder to read.
- **Remember reference behavior**: Objects and arrays can be mutated through any variable that refers to them.

## Summary

Data types tell you what kind of value you are working with and what JavaScript can do with it. Primitive values like strings, numbers, booleans, `null`, and `undefined` are simple and immutable. Reference values like objects, arrays, and functions can hold other values and can be mutated. Use `typeof` for quick checks, remember its `null` and array quirks, be explicit when converting types, and use strict equality to avoid surprising coercion.
