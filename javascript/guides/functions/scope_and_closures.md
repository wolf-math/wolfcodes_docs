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

**Scope** determines where variables are accessible in your code. Understanding scope is essential for writing correct JavaScript programs and avoiding bugs.

JavaScript has three main types of scope:
- **Global scope** — accessible everywhere
- **Function scope** — accessible only within a function
- **Block scope** — accessible only within a block `{}`

## Global vs local scope

### Global scope

Variables declared outside any function or block are in **global scope**:

```javascript
const globalVar = "I'm global";

function myFunction() {
  console.log(globalVar);  // Can access global variable
}

if (true) {
  console.log(globalVar);  // Can also access here
}

console.log(globalVar);  // Works everywhere
```

**Warning:** Too many global variables can cause problems:
- Name collisions (two variables with the same name)
- Harder to track where variables are modified
- Can accidentally overwrite important values

### Local scope (function scope)

Variables declared inside a function are in **function scope** (also called local scope):

```javascript
function myFunction() {
  const localVar = "I'm local";
  console.log(localVar);  // Works: inside the function
}

console.log(localVar);  // Error: localVar is not defined
```

Function-scoped variables are only accessible within the function where they're declared.

## Block scope (`let` and `const`)

Variables declared with `let` and `const` are **block-scoped**, meaning they're only accessible within the block `{}` where they're declared:

```javascript
if (true) {
  const blockVar = "I'm in a block";
  let anotherVar = "Me too";
  console.log(blockVar);  // Works
}

console.log(blockVar);  // Error: blockVar is not defined
console.log(anotherVar);  // Error: anotherVar is not defined
```

### Blocks include:

- `if` statements
- `for` loops
- `while` loops
- `switch` statements
- Any code inside curly braces `{}`

```javascript
for (let i = 0; i < 3; i++) {
  const loopVar = i;
  console.log(loopVar);  // Works
}

console.log(loopVar);  // Error: loopVar is not defined
console.log(i);        // Error: i is not defined
```

### `var` has function scope (not block scope)

Remember from the [variables guide](../data_structures/variables_and_values#why-var-exists-and-why-not-to-use-it) that `var` has different scoping rules:

```javascript
if (true) {
  var functionScoped = "I'm function-scoped";
  let blockScoped = "I'm block-scoped";
}

console.log(functionScoped);  // Works! (var leaks out)
console.log(blockScoped);     // Error! (let stays in block)
```

This is one reason to avoid `var`, it can cause confusing bugs.

## Variable shadowing

When a variable in an inner scope has the same name as a variable in an outer scope, it **shadows** (hides) the outer variable:

```javascript
const name = "Alice";  // Outer scope

function greet() {
  const name = "Bob";  // Inner scope (shadows outer name)
  console.log(name);   // "Bob" (uses inner variable)
}

console.log(name);  // "Alice" (outer variable unchanged)
greet();            // "Bob"
```

Shadowing can be confusing, so use different variable names when possible:

```javascript
// Better: use different names
const userName = "Alice";

function greet() {
  const greetingName = "Bob";
  console.log(greetingName);
}
```

## Closures (conceptual introduction)

A **closure** is a function that has access to variables from its outer (enclosing) scope, even after the outer function has finished executing.

### Simple closure example

```javascript
function outer() {
  const outerVar = "I'm from outer";

  function inner() {
    console.log(outerVar);  // inner can access outerVar
  }

  return inner;
}

const innerFunc = outer();  // outer() has finished executing
innerFunc();                // But inner() can still access outerVar!
// Output: "I'm from outer"
```

The `inner` function "closes over" the `outerVar` variable, creating a closure.

### Why closures matter

Closures enable powerful patterns:

```javascript
function createCounter() {
  let count = 0;  // Private variable

  return function() {
    count++;      // Can access count even though createCounter finished
    return count;
  };
}

const counter = createCounter();
console.log(counter());  // 1
console.log(counter());  // 2
console.log(counter());  // 3
```

The `count` variable is "private", so it can only be accessed through the returned function. This is a common pattern for creating private state.

### Closures in loops

Closures can cause unexpected behavior in loops:

```javascript
// Problem: all functions reference the same i
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);  // Prints 3, 3, 3 (not 0, 1, 2!)
  }, 100);
}

// Solution 1: use let (block scope)
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);  // Prints 0, 1, 2 (each i is in its own scope)
  }, 100);
}

// Solution 2: create a new scope with IIFE
for (var i = 0; i < 3; i++) {
  (function(j) {
    setTimeout(function() {
      console.log(j);  // Prints 0, 1, 2
    }, 100);
  })(i);
}
```

This is why using `let` in loops is important, because it creates a new binding for each iteration.

## Common beginner pitfalls

### 1. Forgetting variable scope

```javascript
function example() {
  if (true) {
    const x = 5;
  }
  console.log(x);  // Error: x is not defined (it's block-scoped)
}
```

**Fix:** Declare variables in the appropriate scope.

### 2. Accidentally creating globals

```javascript
function example() {
  x = 5;  // Missing const/let/var creates a global variable!
}

example();
console.log(x);  // 5 (x is global, oops!)
```

**Fix:** Always use `const`, `let`, or `var` when declaring variables.

### 3. Loop variable issues (with var)

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);  // Prints 3, 3, 3
  }, 100);
}
```

**Fix:** Use `let` in loops instead of `var`.

### 4. Reusing variable names

```javascript
const name = "Alice";

function process() {
  const name = "Bob";  // Shadows outer name (confusing)
  // ...
}
```

**Fix:** Use descriptive, unique names to avoid shadowing.

## Lexical scope

JavaScript uses **lexical scope** (also called static scope), meaning scope is determined by where code is written, not where it's called:

```javascript
const name = "Alice";

function outer() {
  const name = "Bob";

  function inner() {
    console.log(name);  // "Bob" (uses name from outer(), not global)
  }

  return inner;
}

const innerFunc = outer();
innerFunc();  // "Bob" (not "Alice")
```

The `inner` function uses the `name` from `outer()` because that's where it's defined (lexically), not because of where it's called.

## Scope chain

When JavaScript looks for a variable, it searches up the **scope chain**:

1. Check current scope
2. Check outer scope
3. Check next outer scope
4. Continue until global scope
5. If not found, throw `ReferenceError`

```javascript
const global = "global";

function outer() {
  const outerVar = "outer";

  function inner() {
    const innerVar = "inner";
    console.log(innerVar);  // Found in inner scope
    console.log(outerVar);  // Found in outer scope
    console.log(global);    // Found in global scope
    console.log(doesntExist); // Error: not found anywhere
  }

  inner();
}

outer();
```
