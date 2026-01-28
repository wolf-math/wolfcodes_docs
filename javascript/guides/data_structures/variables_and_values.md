---
title: Variables and Values
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are variables?

**Variables** are containers that store values so you can use them later in your program. Think of a variable as a labeled box that holds a piece of data.

```javascript
const name = "Alice";
const age = 30;
```

Here, `name` and `age` are variables. `name` stores the string `"Alice"`, and `age` stores the number `30`.

## Declaring variables: `let` and `const`

In modern JavaScript, you declare variables using `let` or `const`:

### `const` — constants

Use `const` when you want to declare a variable that **cannot be reassigned**:

```javascript
const name = "Alice";
name = "Bob"; // Error! Cannot reassign a const variable
```

The value itself might still be changeable (if it's an object or array), but you can't assign a new value to the variable itself. We'll cover this distinction in the [objects](./objects) and [arrays](./arrays) guides.

### `let` — reassignable variables

Use `let` when you need to reassign the variable later:

```javascript
let counter = 0;
counter = 1;  // OK!
counter = 2;  // OK!
```

### When to use `const` vs `let`

**General rule:** Use `const` by default. Only use `let` when you know you'll need to reassign the variable.

```javascript
// Good: Use const when the variable won't be reassigned
const userName = "Alice";
const maxAttempts = 3;

// Good: Use let when you need reassignment
let attempts = 0;
attempts = attempts + 1;

// Also good: Use let in loops
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

This practice helps prevent bugs and makes your code more predictable.

## Why `var` exists (and why not to use it)

JavaScript also has `var`, which is the old way of declaring variables (from before 2015):

```javascript
var oldWay = "Don't use this";
```

**Why avoid `var`:**

- `var` has function scope, not block scope (leads to confusing bugs)
- `var` allows redeclaration (can cause subtle errors)
- `var` is "hoisted" in unexpected ways

**Use `let` and `const` instead.** They were introduced in ES6 (2015) to fix these problems. This guide uses `let` and `const` exclusively.

## Reassignment vs mutation

This is a crucial distinction:

### Reassignment

**Reassignment** means giving a variable a completely new value:

```javascript
let x = 5;
x = 10;  // Reassignment: x now holds a different value
```

With `const`, you cannot reassign:

```javascript
const x = 5;
x = 10;  // Error: Assignment to constant variable
```

### Mutation

**Mutation** means changing the contents of an object or array (even if the variable itself isn't reassigned):

```javascript
const arr = [1, 2, 3];
arr.push(4);  // Mutation: changing the array's contents
// arr is still the same variable, but its contents changed

const obj = { name: "Alice" };
obj.age = 30;  // Mutation: adding a property
```

This is allowed with `const` because you're not reassigning the variable, instead you're modifying what it points to. We'll explore this more in the [objects](./objects) and [arrays](./arrays) guides.

## Basic operators

JavaScript supports the standard arithmetic operators:

### Arithmetic operators

```javascript
const sum = 5 + 3;      // 8 (addition)
const diff = 10 - 4;    // 6 (subtraction)
const product = 6 * 7;  // 42 (multiplication)
const quotient = 15 / 3; // 5 (division)
const remainder = 17 % 5; // 2 (modulo - remainder after division)
```

### Compound assignment operators

You can combine operators with assignment:

```javascript
let x = 5;
x += 3;  // Same as x = x + 3, now x is 8
x -= 2;  // Same as x = x - 2, now x is 6
x *= 2;  // Same as x = x * 2, now x is 12
x /= 3;  // Same as x = x / 3, now x is 4
```

## Comparison operators

Comparison operators return `true` or `false`:

```javascript
5 > 3   // true (greater than)
5 < 3   // false (less than)
5 >= 5  // true (greater than or equal)
5 <= 4  // false (less than or equal)
5 === 5 // true (strict equality - preferred!)
5 !== 4 // true (strict inequality - preferred!)
```

## `===` Vs `==` (use `===`)

JavaScript has two equality operators:

### `===` (strict equality) — USE THIS

`===` checks if values are **exactly equal**, including their type:

```javascript
5 === 5    // true
5 === "5"  // false (number vs string)
true === true // true
```

### `==` (loose equality) — AVOID THIS

`==` performs **type coercion** (converts types) before comparing, which leads to confusing behavior:

```javascript
5 == "5"   // true (!!)
0 == false // true (!!)
"" == false // true (!!)
null == undefined // true (!!)
```

These examples are confusing and can cause bugs. **Always use `===` and `!==`** unless you have a very specific reason not to.

### Why strict equality matters

Using `===` makes your code more predictable and easier to debug:

```javascript
// Confusing with ==
if (x == 5) {
  // Does x equal 5? Or is x the string "5"? Unclear!
}

// Clear with ===
if (x === 5) {
  // Definitely the number 5, no ambiguity
}
```

**Rule of thumb:** If you find yourself using `==`, stop and ask yourself if you really need type coercion. The answer is almost always "no."

## Variable naming rules

JavaScript has rules for variable names:

1. **Must start with** a letter, `$`, or `_`
2. **Can contain** letters, numbers, `$`, and `_`
3. **Cannot be** reserved words like `if`, `for`, `function`, etc.
4. **Case-sensitive** — `name` and `Name` are different

```javascript
const userName = "Alice";     // Good
const user_name = "Alice";    // OK (but use camelCase in JavaScript)
const $special = "value";     // OK (rare, used in some libraries)
const _private = "value";     // OK (convention for "internal use")
const 2bad = "invalid";       // Error: can't start with number
const user-name = "invalid";  // Error: can't use hyphens
```

### Naming conventions

JavaScript uses **camelCase** for variables:

```javascript
const userName = "Alice";        // Good: camelCase
const user_name = "Alice";       // OK but not idiomatic
const user-name = "Alice";       // Error: syntax error
```

For constants that never change, some developers use **UPPER_SNAKE_CASE**:

```javascript
const MAX_ATTEMPTS = 3;
const API_BASE_URL = "https://api.example.com";
```
