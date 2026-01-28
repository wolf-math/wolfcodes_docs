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

**Data types** define what kind of data a value represents and what operations you can perform on it. JavaScript has several built-in data types that fall into two categories:

- **Primitive types** — simple, immutable values
- **Reference types** — objects and arrays (covered in more detail in later guides)

## Primitive types

Primitive types are the basic building blocks of JavaScript. They're **immutable** (cannot be changed), and when you assign them to variables, the value itself is copied.

### String

A **string** is text data, enclosed in quotes:

```javascript
const name = "Alice";
const greeting = 'Hello';
const template = `Template literal`;
```

Strings can use single quotes `'`, double quotes `"`, or backticks `` ` `` (template literals). We'll cover strings in detail in the [strings guide](./strings).

### Number

JavaScript has one type for numbers (unlike some languages that separate integers and floats):

```javascript
const age = 30;           // Integer
const price = 9.99;       // Decimal
const negative = -42;     // Negative number
const scientific = 1e6;   // 1000000 (scientific notation)
```

:::note 
JavaScript numbers can sometimes behave unexpectedly with floating-point arithmetic:

```javascript
0.1 + 0.2 === 0.3  // false! (due to floating-point precision)
```

This is normal in most programming languages that use floating-point numbers. For precise decimal math, consider using a library or converting to integers.
:::

### Boolean

A **boolean** represents a `true` or `false` value:

```javascript
const isActive = true;
const isComplete = false;
```

Booleans are used in conditionals and logical operations.

### `null`

`null` represents the intentional absence of a value:

```javascript
const user = null;  // Explicitly no value
```

Use `null` when you want to explicitly indicate "no value" or "empty." This is different from `''` (empty string) or `0` (zero), which are actual values, whereas `null` means the absence of any value.

### `undefined`

`undefined` means a variable has been declared but not assigned a value:

```javascript
let x;
console.log(x); // undefined

const obj = {};
console.log(obj.missingProperty); // undefined
```

**Note:** You typically won't assign `undefined` yourself. It appears automatically when:
- A variable is declared but not initialized
- An object property doesn't exist
- A function doesn't return anything explicitly

Use `null` when you want to explicitly indicate "no value." Let `undefined` appear naturally when things aren't set.

## Reference types (introduction)

These are more complex types that we'll cover in detail later:

### Arrays

An **array** is an ordered collection of values:

```javascript
const numbers = [1, 2, 3, 4, 5];
const names = ["Alice", "Bob", "Charlie"];
```

See the [arrays guide](./arrays) for details.

### Objects

An **object** is a collection of key-value pairs:

```javascript
const person = {
  name: "Alice",
  age: 30
};
```

See the [objects guide](./objects) for details.

## Dynamic typing

JavaScript is **dynamically typed**, meaning variables can hold values of any type, and the type can change:

```javascript
let x = 5;        // x is a number
x = "hello";      // x is now a string
x = true;         // x is now a boolean
```

This is different from **statically typed** languages (like TypeScript, Java, or C++) where variables must be declared with a specific type that cannot change.

Dynamic typing makes JavaScript flexible but can also lead to bugs if you're not careful. This is why many developers use TypeScript (which adds static typing to JavaScript) for larger projects.

## `typeof` Operator

The `typeof` operator tells you what type a value is:

```javascript
typeof "hello"      // "string"
typeof 42           // "number"
typeof true         // "boolean"
typeof null         // "object" (this is a bug in JavaScript!)
typeof undefined    // "undefined"
typeof [1, 2, 3]    // "object" (arrays are objects in JavaScript)
typeof {a: 1}       // "object"
typeof function(){} // "function"
```

:::note **Gotcha** 
`typeof null` returns `"object"` instead of `"null"`. This is a known bug in JavaScript that can't be fixed without breaking existing code. To check for `null`, use strict equality:

```javascript
const value = null;
value === null  // true (correct way to check for null)
typeof value === "object" && value === null  // true (more verbose but works)
```
:::

## Truthy and falsy values

In JavaScript, values can be **truthy** or **falsy**. This means they evaluate to `true` or `false` in a boolean context (like `if` statements).

### Falsy values

These values are **falsy** (evaluate to `false`):

```javascript
false
0
-0
0n        // BigInt zero
""        // Empty string
null
undefined
NaN       // Not a Number
```

Everything else is **truthy**.

### Truthy examples

```javascript
if ("hello") {        // truthy
  console.log("runs");
}

if (42) {             // truthy
  console.log("runs");
}

if ([]) {             // truthy (empty array is truthy!)
  console.log("runs");
}

if ({}) {             // truthy (empty object is truthy!)
  console.log("runs");
}
```

### Common pitfalls

**Empty strings are falsy:**

```javascript
const name = "";
if (name) {
  // This won't run because empty string is falsy
  console.log("Name exists");
}
```

**Zero is falsy:**

```javascript
const count = 0;
if (count) {
  // This won't run! Zero is falsy
  console.log("Has items");
}

// Better: be explicit
if (count > 0) {
  console.log("Has items");
}
```

**Arrays and objects are always truthy:**

```javascript
const items = [];
if (items) {
  // This WILL run (empty array is truthy!)
  console.log("Has items"); // Wrong! Array is empty
}

// Better: check length
if (items.length > 0) {
  console.log("Has items");
}
```

We'll explore truthy/falsy values more in the [control flow guide](../control_flow/conditionals).

## Type conversion

JavaScript can convert between types automatically (type coercion) or explicitly:

### Explicit conversion

Convert values intentionally:

```javascript
// String to number
Number("42")        // 42
parseInt("42")      // 42
parseFloat("3.14")  // 3.14

// Number to string
String(42)          // "42"
(42).toString()     // "42"

// To boolean
Boolean(1)          // true
Boolean(0)          // false
Boolean("")         // false
Boolean("hello")    // true

// Shorthand for boolean
!!"hello"           // true (double negation trick)
!!0                 // false
```

### Implicit conversion (type coercion)

JavaScript converts types automatically in some contexts:

```javascript
"5" + 3      // "53" (number converted to string, then concatenated)
"5" - 3      // 2 (string converted to number, then subtracted)
"5" * 2      // 10 (string converted to number)
true + 1     // 2 (boolean converted to number)
```

This is why using `===` (strict equality) is important—it avoids these automatic conversions. We covered this in the [variables guide](./variables_and_values).
