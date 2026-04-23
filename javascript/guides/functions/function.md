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

**Functions** are reusable blocks of code that perform a specific task. They let you give a name to behavior, avoid repetition, and break a program into smaller pieces.

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}

console.log(greet("Alice")); // "Hello, Alice!"
console.log(greet("Bob"));   // "Hello, Bob!"
```

Instead of writing the greeting code twice, you define it once and call the function with different values.

## Why this matters

Functions are how JavaScript programs stay organized. You'll use them to calculate values, handle events, validate data, process arrays, fetch data, and separate one piece of logic from another.

Good functions make code easier to read because the function name explains what the code does:

```javascript
const total = calculateTotal(cartItems);
```

That is usually clearer than repeating the calculation everywhere.

## Function declarations

A **function declaration** uses the `function` keyword and gives the function a name:

```javascript
function add(a, b) {
  return a + b;
}

const result = add(5, 3);

console.log(result); // 8
```

Function declarations are useful for named, reusable behavior.

## Function expressions

A **function expression** creates a function value and stores it in a variable:

```javascript
const add = function(a, b) {
  return a + b;
};

const result = add(5, 3);

console.log(result); // 8
```

The function is assigned to `add`, so you call it with `add(5, 3)`.

## Arrow functions

**Arrow functions** are a shorter syntax for function expressions:

```javascript
const add = (a, b) => {
  return a + b;
};

console.log(add(5, 3)); // 8
```

When the body is one expression, you can use an implicit return:

```javascript
const add = (a, b) => a + b;
const square = (number) => number * number;
const greet = () => "Hello";

console.log(square(4)); // 16
```

Arrow functions are common for callbacks and array methods:

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map((number) => number * 2);

console.log(doubled); // [2, 4, 6, 8]
```

Arrow functions are covered in more detail in the [callback functions guide](./callbacks), where they are used with array methods, timers, and events.

**Important:** Arrow functions handle `this` differently from regular functions. That matters most in object-oriented code and is covered in the [OOP guide](../oop/introduction).

## Hoisting

**Hoisting** is JavaScript's behavior of setting up some declarations before code runs. Function declarations and function expressions behave differently, so this is an important mental model.

### Function declarations are hoisted

You can call a function declaration before it appears in the file:

```javascript
sayHello();

function sayHello() {
  console.log("Hello");
}
```

**Output:**

```text
Hello
```

JavaScript knows about the function declaration before executing the code.

### Function expressions are not usable before initialization

Function expressions stored in `const` or `let` are not usable before the assignment runs:

```javascript
// This would cause an error:
// sayHello(); // ReferenceError: Cannot access 'sayHello' before initialization

const sayHello = function() {
  console.log("Hello");
};
```

The variable exists in the scope, but it cannot be used before JavaScript reaches the `const` assignment.

### Arrow functions follow function expression rules

Arrow functions are also function expressions:

```javascript
// This would cause an error:
// sayHello(); // ReferenceError: Cannot access 'sayHello' before initialization

const sayHello = () => {
  console.log("Hello");
};
```

### Rule of thumb

Define functions before you call them unless you are intentionally using a function declaration.

```javascript
function calculateTotal(items) {
  return items.reduce((total, item) => total + item.price, 0);
}

const total = calculateTotal([{ price: 10 }, { price: 15 }]);

console.log(total); // 25
```

This keeps the code easy to read even when hoisting would allow a different order.

## Parameters and arguments

**Parameters** are the names in the function definition. **Arguments** are the values you pass when calling the function.

```javascript
function greet(name, greeting) {
  return `${greeting}, ${name}!`;
}

const message = greet("Alice", "Hello");

console.log(message); // "Hello, Alice!"
```

Here, `name` and `greeting` are parameters. `"Alice"` and `"Hello"` are arguments.

### Missing arguments

If you call a function with fewer arguments than parameters, the missing parameters are `undefined`:

```javascript
function greet(name, greeting) {
  return `${greeting}, ${name}!`;
}

console.log(greet("Alice")); // "undefined, Alice!"
```

### Default parameters

Use default parameters when an argument should be optional:

```javascript
function greet(name, greeting = "Hello") {
  return `${greeting}, ${name}!`;
}

console.log(greet("Alice"));       // "Hello, Alice!"
console.log(greet("Alice", "Hi")); // "Hi, Alice!"
```

Default parameters are used only when the argument is `undefined`:

```javascript
function greet(name, greeting = "Hello") {
  return `${greeting}, ${name}!`;
}

console.log(greet("Alice", undefined)); // "Hello, Alice!"
console.log(greet("Alice", null));      // "null, Alice!"
```

### Rest parameters

Use a rest parameter when a function should accept any number of arguments.

```javascript
function addAll(...numbers) {
  let total = 0;

  for (const number of numbers) {
    total += number;
  }

  return total;
}

console.log(addAll(1, 2, 3));    // 6
console.log(addAll(5, 10, 15));  // 30
```

The `...numbers` parameter gathers the remaining arguments into an array.

Use rest parameters when the function naturally works with a list of values.

Rest parameters and spread syntax are covered together in the [rest and spread guide](../data_structures/rest_and_spread).

## Return values

Use `return` to send a value back to the caller:

```javascript
function add(a, b) {
  return a + b;
}

const result = add(5, 3);

console.log(result); // 8
```

When a `return` statement runs, the function stops immediately:

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

console.log(getGrade(85)); // "B"
```

If a function does not return a value, it returns `undefined`:

```javascript
function logMessage(message) {
  console.log(message);
}

const result = logMessage("Hello");

console.log(result); // undefined
```

## Scope basics

Variables declared inside a function are local to that function:

```javascript
function createMessage() {
  const message = "Hello";
  return message;
}

console.log(createMessage()); // "Hello"

// This would cause an error:
// console.log(message); // ReferenceError
```

Functions can access variables from outer scopes:

```javascript
const prefix = "Hello";

function greet(name) {
  return `${prefix}, ${name}!`;
}

console.log(greet("Alice")); // "Hello, Alice!"
```

Scope and closures are covered in more detail in the [scope and closures guide](./scope_and_closures).

## Functions as values

Functions are values in JavaScript. You can store them in variables, pass them to other functions, and return them from functions.

```javascript
function callTwice(callback) {
  callback();
  callback();
}

callTwice(() => {
  console.log("Hello");
});
```

**Output:**

```text
Hello
Hello
```

This is why functions work so well with array methods and event listeners. The function passed to `callTwice` is a callback, which is covered in more detail in the [callback functions guide](./callbacks).

## Common patterns

### Helper functions

Use helper functions to name reusable logic:

```javascript
function isAdult(age) {
  return age >= 18;
}

if (isAdult(20)) {
  console.log("Can continue");
}
```

### Early returns

Use early returns to handle edge cases first:

```javascript
function getEmail(user) {
  if (!user) {
    return null;
  }

  if (!user.email) {
    return null;
  }

  return user.email;
}
```

### Array callbacks

Functions are often passed to array methods:

```javascript
const numbers = [1, 2, 3, 4, 5];

const evens = numbers.filter((number) => number % 2 === 0);
const squares = numbers.map((number) => number * number);

console.log(evens);   // [2, 4]
console.log(squares); // [1, 4, 9, 16, 25]
```

For a deeper explanation of passing functions into other functions, see the [callback functions guide](./callbacks).

### Immediately invoked function expressions

An immediately invoked function expression, or IIFE, runs right after it is created:

```javascript
(function() {
  console.log("This runs immediately");
})();
```

IIFEs are less common in modern JavaScript because modules solve many of the same scope problems, but you may see them in older code.

## When to create a function

Create a function when:

- You are repeating the same logic.
- A block of code has one clear purpose.
- A name would make the behavior easier to understand.
- You want to test a piece of logic by itself.
- A section of code is getting long or hard to scan.

Good function names usually start with a verb:

```javascript
function calculateTotal(items) {}
function getUserById(id) {}
function isValidEmail(email) {}
```

Avoid vague names:

```javascript
function stuff() {}
function doThings() {}
function handleIt() {}
```

## Best practices

- **Use descriptive names**: The name should explain what the function does.
- **Keep functions focused**: One function should do one clear job.
- **Return values consistently**: Avoid sometimes returning a value and sometimes not unless that behavior is intentional.
- **Use default parameters for common defaults**.
- **Use rest parameters** when a function should accept a flexible number of arguments.
- **Prefer early returns over deep nesting**.
- **Define functions before calling them** unless you intentionally rely on function declaration hoisting.
- **Use arrow functions for short callbacks** and regular functions when `this` behavior matters.

## Summary

Functions package reusable behavior. Function declarations, function expressions, and arrow functions all create callable values, but they differ in syntax and hoisting behavior. Use parameters for inputs, rest parameters for flexible argument lists, `return` for outputs, and clear names to make code easier to read. Functions are also values, which is why callbacks work. Hoisting lets function declarations be called before their definition, but defining functions before use is usually the clearest habit.
