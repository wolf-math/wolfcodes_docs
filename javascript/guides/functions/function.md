---
title: Functions
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are functions?

**Functions** are reusable blocks of code that perform a specific task. They let you:
- Organize code into logical units
- Avoid repetition (DRY: Don't Repeat Yourself)
- Make code easier to read and maintain

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}

console.log(greet("Alice"));  // "Hello, Alice!"
console.log(greet("Bob"));    // "Hello, Bob!"
```

Instead of writing the greeting code twice, we wrote it once in a function and called it multiple times.

## Function declarations

A **function declaration** uses the `function` keyword:

```javascript
function add(a, b) {
  return a + b;
}

const result = add(5, 3);  // 8
```

Function declarations are **hoisted**, meaning they can be called before they're defined in your code:

```javascript
sayHello();  // Works! (function is hoisted)

function sayHello() {
  console.log("Hello!");
}
```

## Function expressions

A **function expression** assigns a function to a variable:

```javascript
const add = function(a, b) {
  return a + b;
};

const result = add(5, 3);  // 8
```

Function expressions are **not hoisted**, so you must define them before calling:

```javascript
sayHello();  // Error! Cannot access before initialization

const sayHello = function() {
  console.log("Hello!");
};
```

## Arrow functions

**Arrow functions** (introduced in ES6) are a shorter syntax for function expressions:

```javascript
// Function expression
const add = function(a, b) {
  return a + b;
};

// Arrow function (equivalent)
const add = (a, b) => {
  return a + b;
};

// Arrow function with implicit return (when body is single expression)
const add = (a, b) => a + b;

// Single parameter (no parentheses needed)
const square = x => x * x;

// No parameters (parentheses required)
const greet = () => "Hello!";
```

### When to use arrow functions

Arrow functions are preferred in modern JavaScript for:
- Short, simple functions
- Callbacks (functions passed to other functions)
- Array methods (`map`, `filter`, `reduce`)

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(x => x * 2);  // [2, 4, 6, 8]
```

However, arrow functions behave differently with `this` (covered in the [OOP guide](../oop/introduction)), so use regular functions when you need `this` binding.

## Parameters and return values

### Parameters

Functions can accept **parameters** (also called arguments):

```javascript
function greet(name, greeting) {
  return `${greeting}, ${name}!`;
}

greet("Alice", "Hello");  // "Hello, Alice!"
```

If you call a function with fewer arguments than parameters, missing parameters are `undefined`:

```javascript
function greet(name, greeting) {
  return `${greeting}, ${name}!`;
}

greet("Alice");  // "undefined, Alice!"
```

### Default parameters

You can provide **default values** for parameters:

```javascript
function greet(name, greeting = "Hello") {
  return `${greeting}, ${name}!`;
}

greet("Alice");           // "Hello, Alice!" (uses default)
greet("Alice", "Hi");     // "Hi, Alice!" (overrides default)
```

Default parameters are only used when the argument is `undefined`:

```javascript
function greet(name, greeting = "Hello") {
  return `${greeting}, ${name}!`;
}

greet("Alice", undefined);  // "Hello, Alice!" (uses default)
greet("Alice", null);       // "null, Alice!" (null is not undefined)
```

### Return values

Functions can **return** values using the `return` statement:

```javascript
function add(a, b) {
  return a + b;
}

const result = add(5, 3);  // result is 8
```

If a function doesn't have a `return` statement (or returns without a value), it returns `undefined`:

```javascript
function doSomething() {
  console.log("Doing something");
  // No return statement
}

const result = doSomething();  // result is undefined
```

### Multiple return statements

Functions can have multiple return statements:

```javascript
function getGrade(score) {
  if (score >= 90) {
    return "A";
  }
  if (score >= 80) {
    return "B";
  }
  return "F";
}
```

When a `return` statement executes, the function exits immediately.

## Scope basics

**Scope** determines where variables are accessible. JavaScript has different scopes:

### Global scope

Variables declared outside functions are in **global scope**:

```javascript
const globalVar = "I'm global";

function myFunction() {
  console.log(globalVar);  // Can access global variable
}
```

### Local scope (function scope)

Variables declared inside a function are in **local scope**:

```javascript
function myFunction() {
  const localVar = "I'm local";
  console.log(localVar);  // Works
}

console.log(localVar);  // Error: localVar is not defined
```

### Block scope

Variables declared with `let` and `const` are **block-scoped** (confined to the block `{}`):

```javascript
if (true) {
  const blockVar = "I'm in a block";
  console.log(blockVar);  // Works
}

console.log(blockVar);  // Error: blockVar is not defined
```

We'll explore scope in more detail in the [scope and closures guide](./scope_and_closures).

## Common function patterns

### Functions that don't return values

Sometimes functions perform actions without returning values:

```javascript
function logMessage(message) {
  console.log(`[${new Date().toISOString()}] ${message}`);
}

logMessage("Something happened");
// Output: [2024-01-15T10:30:00.000Z] Something happened
```

### Functions as values

Functions are **first-class citizens** in JavaScript—they can be:
- Assigned to variables
- Passed as arguments
- Returned from other functions

```javascript
// Assign to variable
const myFunc = function() {
  console.log("Hello");
};

// Pass as argument
function callTwice(func) {
  func();
  func();
}

callTwice(() => console.log("Hello"));
// Output: Hello (twice)
```

### Anonymous functions

Functions without names are **anonymous functions**:

```javascript
// Anonymous function assigned to variable
const greet = function(name) {
  return `Hello, ${name}!`;
};

// Anonymous arrow function
const greet = (name) => `Hello, ${name}!`;

// Anonymous function passed as argument
setTimeout(function() {
  console.log("Delayed");
}, 1000);
```

### Immediately Invoked Function Expressions (IIFE)

An IIFE runs immediately after it's defined:

```javascript
(function() {
  console.log("This runs immediately");
})();

// Arrow function version
(() => {
  console.log("This also runs immediately");
})();
```

IIFEs are less common in modern JavaScript (modules replaced most use cases), but you might encounter them in older code.

## Functions and arrays

Functions work great with array methods:

```javascript
const numbers = [1, 2, 3, 4, 5];

// Using named function
function double(x) {
  return x * 2;
}
const doubled = numbers.map(double);

// Using arrow function (more common)
const doubled2 = numbers.map(x => x * 2);

// Filtering with function
const evens = numbers.filter(x => x % 2 === 0);

// Reducing with function
const sum = numbers.reduce((acc, x) => acc + x, 0);
```

## When to create functions

Create functions when:
- You're repeating the same code
- A block of code has a clear, single purpose
- You want to test a piece of code in isolation
- The code is getting long or hard to read

**Good function names** are descriptive and start with a verb:

```javascript
// Good
function calculateTotal(items) { }
function getUserById(id) { }
function isValidEmail(email) { }

// Bad
function stuff() { }
function doThings() { }
function xyz() { }
```
