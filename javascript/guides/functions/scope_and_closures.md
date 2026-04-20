---
title: Scope and Closures
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

## What is scope?

**Scope** determines where variables can be accessed. If a variable is outside the current scope, your code cannot use it.

```javascript
function greet() {
  const message = "Hello";
  console.log(message);
}

greet(); // "Hello"

// This would cause an error:
// console.log(message); // ReferenceError
```

The variable `message` exists only inside the `greet` function.

## Why this matters

Scope helps you keep code organized and prevents names from colliding. It also explains why some variables are available in one part of a program but not another.

Closures build on scope. They let functions remember variables from the place where they were created, which is one of JavaScript's most important function patterns.

## Global scope

A variable declared outside functions and blocks is in **global scope**:

```javascript
const appName = "Todo App";

function printAppName() {
  console.log(appName);
}

printAppName(); // "Todo App"
```

Global variables can be read from many places, but too many globals make programs harder to reason about. Prefer keeping variables in the smallest scope that needs them.

## Function scope

Variables declared inside a function are available only inside that function:

```javascript
function createUser() {
  const name = "Alice";
  return { name };
}

console.log(createUser()); // { name: "Alice" }

// This would cause an error:
// console.log(name); // ReferenceError
```

Each function call gets its own local variables:

```javascript
function addOne(number) {
  const result = number + 1;
  return result;
}

console.log(addOne(1)); // 2
console.log(addOne(5)); // 6
```

## Block scope

Variables declared with `let` and `const` are **block-scoped**. A block is code inside `{}`.

```javascript
if (true) {
  const message = "Inside block";
  console.log(message);
}

// This would cause an error:
// console.log(message); // ReferenceError
```

Blocks include:

- `if` statements
- `for` loops
- `while` loops
- `switch` statements
- standalone `{}` blocks

Loop variables declared with `let` are also block-scoped:

```javascript
for (let i = 0; i < 3; i++) {
  console.log(i);
}

// This would cause an error:
// console.log(i); // ReferenceError
```

## `var` has function scope

Remember from the [variables guide](../data_structures/variables_and_values#why-var-exists-and-why-not-to-use-it) that `var` has older scoping behavior. It is function-scoped, not block-scoped:

```javascript
if (true) {
  var functionScoped = "I leak out of the block";
  const blockScoped = "I stay in the block";
}

console.log(functionScoped); // "I leak out of the block"

// This would cause an error:
// console.log(blockScoped); // ReferenceError
```

This is one reason modern JavaScript uses `const` and `let` instead of `var`.

## Variable hoisting

**Hoisting** means JavaScript sets up declarations before code runs. Variables declared with `var`, `let`, and `const` are all hoisted in a technical sense, but they behave differently.

With `var`, the variable exists before the declaration line and starts as `undefined`:

```javascript
console.log(count); // undefined

var count = 1;
```

With `let` and `const`, the variable cannot be used before the declaration line:

```javascript
// This would cause an error:
// console.log(count); // ReferenceError

const count = 1;
```

**Rule of thumb:** Declare variables before using them, and prefer `const` or `let`.

Function hoisting is covered in the [functions guide](./function#hoisting).

## Variable shadowing

**Shadowing** happens when an inner scope has a variable with the same name as an outer scope:

```javascript
const name = "Alice";

function greet() {
  const name = "Bob";
  console.log(name);
}

greet();           // "Bob"
console.log(name); // "Alice"
```

The inner `name` hides the outer `name` while inside the function.

Shadowing is allowed, but it can be confusing. Use more specific names when clarity matters:

```javascript
const userName = "Alice";

function greet() {
  const greetingName = "Bob";
  console.log(greetingName);
}
```

## Lexical scope

JavaScript uses **lexical scope**, which means scope is based on where code is written, not where a function is called.

```javascript
const name = "Alice";

function outer() {
  const name = "Bob";

  function inner() {
    console.log(name);
  }

  return inner;
}

const innerFunction = outer();
innerFunction(); // "Bob"
```

`inner` uses the `name` from `outer` because that is where `inner` was created.

## Scope chain

When JavaScript looks for a variable, it checks scopes from inside to outside:

1. Current scope
2. Outer scope
3. Next outer scope
4. Global scope
5. If not found, `ReferenceError`

```javascript
const globalValue = "global";

function outer() {
  const outerValue = "outer";

  function inner() {
    const innerValue = "inner";

    console.log(innerValue);  // "inner"
    console.log(outerValue);  // "outer"
    console.log(globalValue); // "global"
  }

  inner();
}

outer();
```

This chain is why inner functions can use variables from outer functions.

## What are closures?

A **closure** is a function that remembers variables from its outer scope, even after that outer function has finished running.

```javascript
function createGreeting(name) {
  return function() {
    return `Hello, ${name}!`;
  };
}

const greetAlice = createGreeting("Alice");

console.log(greetAlice()); // "Hello, Alice!"
```

The returned function remembers `name`, even though `createGreeting` has already finished.

## Closures for private state

Closures can keep state private:

```javascript
function createCounter() {
  let count = 0;

  return function() {
    count += 1;
    return count;
  };
}

const counter = createCounter();

console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

Only the returned function can access and update `count`.

## Closures in loops

Closures can be surprising in loops when `var` is used:

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);
  }, 100);
}
// Output:
// 3
// 3
// 3
```

All callbacks share the same function-scoped `i`.

Use `let` to create a new binding for each loop iteration:

```javascript
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);
  }, 100);
}
// Output:
// 0
// 1
// 2
```

This is one of the clearest practical reasons to avoid `var`.

## Common patterns

### Keeping helper variables local

```javascript
function formatName(firstName, lastName) {
  const trimmedFirst = firstName.trim();
  const trimmedLast = lastName.trim();

  return `${trimmedFirst} ${trimmedLast}`;
}
```

The temporary variables stay inside the function where they are needed.

### Creating specialized functions

```javascript
function createMultiplier(multiplier) {
  return function(number) {
    return number * multiplier;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15
```

Each returned function remembers its own `multiplier`.

### Avoiding accidental globals

Always declare variables with `const` or `let`:

```javascript
function saveUser(user) {
  const normalizedName = user.name.trim();
  return normalizedName;
}
```

Avoid assigning to a name that was never declared:

```javascript
function saveUser(user) {
  // Avoid this:
  // normalizedName = user.name.trim();
}
```

## Best practices

- **Use the smallest useful scope**: Declare variables where they are needed.
- **Prefer `const` and `let`**: Avoid `var` in new code.
- **Declare before use**: Do not rely on hoisting.
- **Avoid unnecessary globals**: They are easy to accidentally reuse or overwrite.
- **Avoid confusing shadowing**: Use clearer names when nested scopes overlap.
- **Use closures intentionally**: They are useful for private state and specialized functions.
- **Use `let` in loops** when callbacks need the current loop value.

## Summary

Scope controls where variables are available. JavaScript has global scope, function scope, and block scope. The scope chain lets inner functions access outer variables, and closures let functions remember those variables even after the outer function has finished. Prefer `const` and `let`, keep variables in the smallest useful scope, and avoid relying on hoisting.
