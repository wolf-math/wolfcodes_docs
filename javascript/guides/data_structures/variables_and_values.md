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

**Variables** are names that refer to values. They let you store information, give it a meaningful label, and use it later in your program.

```javascript
const name = "Alice";
const age = 30;

console.log(name); // "Alice"
console.log(age);  // 30
```

Here, `name` refers to the string `"Alice"`, and `age` refers to the number `30`. The variable names make the code easier to understand than using raw values everywhere.

## Why this matters

Variables are one of the basic building blocks of JavaScript programs. You'll use them to store user input, keep track of counts, save results from calculations, and pass information between different parts of your code.

Good variable names also make code easier to read. A name like `userAge` tells you what a value means. The number `30` by itself does not.

## Declaring variables with `const` and `let`

In modern JavaScript, declare variables with `const` or `let`.

### `const`

Use `const` when the variable should not be reassigned to a different value:

```javascript
const userName = "Alice";
const maxAttempts = 3;
```

Trying to reassign a `const` variable causes an error:

```javascript
const name = "Alice";

// This would cause an error:
// name = "Bob"; // TypeError: Assignment to constant variable
```

**Important:** `const` prevents reassignment. It does not always make the value itself unchangeable. Arrays and objects can still be mutated, which we'll cover below.

### `let`

Use `let` when the variable needs to be reassigned later:

```javascript
let attempts = 0;

attempts = attempts + 1;
attempts = attempts + 1;

console.log(attempts); // 2
```

`let` is also common in traditional `for` loops because the loop counter changes each time through the loop:

```javascript
for (let i = 0; i < 3; i++) {
  console.log(i);
}
// Output:
// 0
// 1
// 2
```

### When to use `const` vs `let`

**Rule of thumb:** Use `const` by default. Use `let` only when you know the variable needs to be reassigned.

```javascript
// Good: this value does not need reassignment
const userName = "Alice";

// Good: this value changes over time
let score = 0;
score += 10;
```

This habit makes code more predictable. When you see `const`, you know that name will keep pointing at the same value.

## Why `var` exists (and why not to use it)

JavaScript also has `var`, which is the older way to declare variables:

```javascript
var oldWay = "This still works";
```

You will see `var` in older code, but avoid it in new code.

`var` is harder to reason about because:

- It has function [scope](../functions/scope_and_closures), not block scope.
- It allows redeclaring the same variable name.
- It is [hoisted](../functions/scope_and_closures.md) in ways that can surprise beginners.

Use `const` and `let` instead. They are clearer and match modern JavaScript style.

## Names refer to values

A useful mental model is: **a variable name points to a value**.

```javascript
let count = 1;
count = 2;

console.log(count); // 2
```

The name `count` first points to `1`. After reassignment, `count` points to `2`.

This matters because changing the variable and changing the value are not always the same thing.

## Reassignment vs mutation

JavaScript makes an important distinction between **reassignment** and **mutation**.

### Reassignment

**Reassignment** means making a variable point to a different value:

```javascript
let color = "red";
color = "blue";

console.log(color); // "blue"
```

This works with `let`, but not with `const`:

```javascript
const color = "red";

// This would cause an error:
// color = "blue"; // TypeError: Assignment to constant variable
```

### Mutation

**Mutation** means changing the contents of an object or array:

```javascript
const numbers = [1, 2, 3];
numbers.push(4);

console.log(numbers); // [1, 2, 3, 4]
```

This works even though `numbers` was declared with `const`. The variable still points to the same array. The array's contents changed.

Objects behave the same way:

```javascript
const user = { name: "Alice" };
user.age = 30;

console.log(user); // { name: "Alice", age: 30 }
```

You'll see this distinction again in the [arrays](./arrays) and [objects](./objects) guides.

## Basic operators

Variables become useful when you combine, compare, and update values.

### Arithmetic operators

Use arithmetic operators for number calculations:

```javascript
const sum = 5 + 3;          // 8
const difference = 10 - 4;  // 6
const product = 6 * 7;      // 42
const quotient = 15 / 3;    // 5
const remainder = 17 % 5;   // 2
```

### Compound assignment

Compound assignment operators update a variable based on its current value:

```javascript
let count = 5;

count += 3; // Same as count = count + 3
count -= 2; // Same as count = count - 2

console.log(count); // 6
```

Use these when they make the update easier to read.

## Comparison operators

Comparison operators return boolean values: `true` or `false`.

```javascript
5 > 3;   // true
5 < 3;   // false
5 >= 5;  // true
5 <= 4;  // false
5 === 5; // true
5 !== 4; // true
```

Comparisons are often used in conditionals:

```javascript
const age = 20;

if (age >= 18) {
  console.log("You are an adult");
}
```

## Strict equality: `===` vs `==`

JavaScript has two equality operators, but beginners should almost always use `===`.

### `===` checks value and type

`===` is called **strict equality**. It checks that both values are equal and have the same type:

```javascript
5 === 5;     // true
5 === "5";   // false
true === true; // true
```

### `==` performs type coercion

`==` is called **loose equality**. It may convert values before comparing them:

```javascript
5 == "5";         // true
0 == false;       // true
"" == false;      // true
null == undefined; // true
```

These conversions can make code harder to understand and debug.

```javascript
// Avoid: unclear because JavaScript may coerce the value
if (userId == 5) {
  console.log("Found user");
}

// Prefer: clear and predictable
if (userId === 5) {
  console.log("Found user");
}
```

**Rule of thumb:** Use `===` and `!==` unless you have a specific reason to allow type coercion.

## Variable naming rules

JavaScript variable names must follow a few syntax rules:

1. They must start with a letter, `$`, or `_`.
2. They can contain letters, numbers, `$`, and `_`.
3. They cannot be reserved words like `if`, `for`, or `function`.
4. They are case-sensitive, so `name` and `Name` are different.

```javascript
const userName = "Alice";  // Good
const $button = "save";    // Valid, often used by libraries
const _internal = "value"; // Valid, often means "internal use"

// These would cause errors:
// const 2bad = "invalid";
// const user-name = "invalid";
// const if = "invalid";
```

### Naming conventions

JavaScript usually uses **camelCase** for variables and functions:

```javascript
const userName = "Alice";
const maxAttempts = 3;
const isLoggedIn = true;
```

For constants that represent fixed configuration values, some codebases use **UPPER_SNAKE_CASE**:

```javascript
const MAX_ATTEMPTS = 3;
const API_BASE_URL = "https://api.example.com";
```

The most important thing is that names should describe what the value means.

## Common patterns

### Counting

Use `let` when a value changes over time:

```javascript
let count = 0;

count += 1;
count += 1;

console.log(count); // 2
```

### Storing a calculation result

Use `const` when you calculate a value once and reuse it:

```javascript
const price = 20;
const taxRate = 0.08;
const total = price + price * taxRate;

console.log(total); // 21.6
```

### Naming boolean values

Boolean variables often read well with names like `is...`, `has...`, or `can...`:

```javascript
const isLoggedIn = true;
const hasPermission = false;
const canEdit = isLoggedIn && hasPermission;

console.log(canEdit); // false
```

## Best practices

- **Use `const` by default**: It prevents accidental reassignment.
- **Use `let` for changing values**: Counters, loop indexes, and values that update over time usually need `let`.
- **Avoid `var` in new code**: Use `const` and `let` instead.
- **Use strict equality**: Prefer `===` and `!==` so JavaScript does not silently coerce types.
- **Choose descriptive names**: Prefer `userName`, `totalPrice`, and `isValid` over vague names like `x`, `data`, or `thing`.
- **Keep names consistent**: Do not reuse the same variable name for unrelated meanings in the same section of code.

## Summary

Variables are names that refer to values. Use `const` by default, switch to `let` when a variable needs reassignment, and avoid `var` in new code. Remember the difference between reassignment and mutation: `const` keeps the variable pointing at the same value, but objects and arrays can still change internally. Use clear names and strict equality to keep your JavaScript predictable.
