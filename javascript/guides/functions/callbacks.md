---
title: Callback Functions
sidebar_position: 9.5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are callback functions?

A **callback function** is a function passed into another function as an argument.

The receiving function can call the callback later, once it is ready to use it.

```javascript
function greetUser(name, callback) {
  const message = `Hello, ${name}!`;
  callback(message);
}

function printMessage(message) {
  console.log(message);
}

greetUser("Alice", printMessage);
```

**Output:**

```text
Hello, Alice!
```

`printMessage` is the callback. It is passed into `greetUser`, and `greetUser` decides when to call it.

## Why this matters

Callbacks are possible because functions are values in JavaScript.

You can store a function in a variable, pass it to another function, and call it later.

Callbacks are common in:

- array methods like `map()`, `filter()`, `find()`, and `forEach()`
- event listeners
- timers like `setTimeout()`
- custom helper functions
- older asynchronous APIs

You do not need to use callbacks everywhere, but you do need to recognize them. They are one of the main ways JavaScript lets you customize behavior.

## Passing a named function

A named function is useful when the behavior is reusable or important enough to name.

```javascript
function logUppercase(text) {
  console.log(text.toUpperCase());
}

function processMessage(message, callback) {
  callback(message);
}

processMessage("hello", logUppercase);
```

**Output:**

```text
HELLO
```

Notice that `logUppercase` is passed without parentheses.

```javascript
processMessage("hello", logUppercase);
```

That passes the function itself.

## Passing an anonymous function

You can also pass a function expression directly.

```javascript
function processMessage(message, callback) {
  callback(message);
}

processMessage("hello", function(message) {
  console.log(`Message: ${message}`);
});
```

**Output:**

```text
Message: hello
```

This is useful when the callback is only needed in one place.

## Passing an arrow function

Arrow functions are common for short callbacks.

```javascript
function processMessage(message, callback) {
  callback(message);
}

processMessage("hello", (message) => {
  console.log(`Message: ${message}`);
});
```

**Output:**

```text
Message: hello
```

For very small callbacks, you may see a shorter form:

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map((number) => number * 2);

console.log(doubled); // [2, 4, 6]
```

Use the shorter form when it stays easy to read.

## Callback parameters

The function that calls the callback decides what arguments the callback receives.

```javascript
function repeat(count, callback) {
  for (let index = 0; index < count; index++) {
    callback(index);
  }
}

repeat(3, (index) => {
  console.log(`Run ${index}`);
});
```

**Output:**

```text
Run 0
Run 1
Run 2
```

`repeat` calls the callback and passes the current `index`.

The callback receives that value as its parameter.

## Array method callbacks

Array methods use callbacks to describe what should happen to each item.

### `map()`

Use `map()` when you want to transform each item into a new item.

```javascript
const names = ["alice", "bob", "charlie"];
const upperNames = names.map((name) => name.toUpperCase());

console.log(upperNames); // ["ALICE", "BOB", "CHARLIE"]
```

The callback receives each `name` and returns the transformed value.

### `filter()`

Use `filter()` when you want to keep only some items.

```javascript
const scores = [95, 62, 88, 70];
const passingScores = scores.filter((score) => score >= 70);

console.log(passingScores); // [95, 88, 70]
```

The callback returns `true` to keep an item or `false` to remove it.

### `find()`

Use `find()` when you want the first matching item.

```javascript
const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

const user = users.find((user) => user.id === 2);

console.log(user); // { id: 2, name: "Bob" }
```

The callback returns `true` for the item you want.

### `forEach()`

Use `forEach()` for side effects, such as logging.

```javascript
const names = ["Alice", "Bob", "Charlie"];

names.forEach((name) => {
  console.log(name);
});
```

**Output:**

```text
Alice
Bob
Charlie
```

Use `map()` instead of `forEach()` when you need a new array.

## Timer callbacks

Some browser and Node.js APIs use callbacks because the work happens later.

```javascript
setTimeout(() => {
  console.log("This runs later");
}, 1000);
```

The callback is the function passed to `setTimeout`.

JavaScript waits about one second, then calls the callback.

## Event callbacks

In browser JavaScript, event listeners use callbacks.

```javascript
const button = document.querySelector("button");

button.addEventListener("click", () => {
  console.log("Button clicked");
});
```

The callback runs when the user clicks the button.

In real browser code, check that the element exists before using it:

```javascript
const button = document.querySelector("button");

if (button) {
  button.addEventListener("click", () => {
    console.log("Button clicked");
  });
}
```

## Writing your own callback-based function

Callbacks let you write flexible functions.

```javascript
function applyToEach(items, callback) {
  const results = [];

  for (const item of items) {
    results.push(callback(item));
  }

  return results;
}

const numbers = [1, 2, 3];
const doubled = applyToEach(numbers, (number) => number * 2);

console.log(doubled); // [2, 4, 6]
```

`applyToEach` does not need to know exactly how each item should change.

It lets the callback provide that behavior.

## Common mistake: calling instead of passing

When you pass a callback, pass the function itself.

Do not call it too early.

```javascript
function sayHello() {
  console.log("Hello");
}

setTimeout(sayHello, 1000);
```

This passes the function.

This version calls the function immediately:

```javascript
function sayHello() {
  console.log("Hello");
}

// Avoid this when you mean "run later":
setTimeout(sayHello(), 1000);
```

`sayHello()` runs right away because the parentheses call the function.

## Callbacks and async code

Callbacks are still useful as a general function pattern.

But older JavaScript also used callbacks heavily for asynchronous work.

```javascript
loadUser((user) => {
  loadPosts(user.id, (posts) => {
    console.log(posts);
  });
});
```

This style can become deeply nested when several async steps depend on each other.

For new asynchronous code, prefer [promises](../async/promises) and [async/await](../async/async_await).

The [async callbacks guide](../async/callbacks) covers older callback-based async code so you can recognize it.

## Common patterns

### Naming callback parameters

Use names that describe what the callback does.

```javascript
function saveUser(user, onSuccess) {
  console.log(`Saving ${user.name}`);
  onSuccess();
}

saveUser({ name: "Alice" }, () => {
  console.log("Saved");
});
```

Names like `callback`, `onSuccess`, `onError`, `handleClick`, and `compareNumbers` are more useful than vague names like `fn`.

### Returning from callbacks

Some callbacks should return a value.

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map((number) => {
  return number * 2;
});

console.log(doubled); // [2, 4, 6]
```

Some callbacks are only for side effects.

```javascript
const names = ["Alice", "Bob"];

names.forEach((name) => {
  console.log(name);
});
```

Know which kind of callback the function expects.

### Keeping callbacks readable

Move a callback into a named function when it gets long.

```javascript
function isPassingScore(score) {
  return score >= 70;
}

const scores = [95, 62, 88, 70];
const passingScores = scores.filter(isPassingScore);

console.log(passingScores); // [95, 88, 70]
```

This makes the array operation easier to scan.

## Best practices

- **Pass the function, do not call it early**: Use `setTimeout(sayHello, 1000)`, not `setTimeout(sayHello(), 1000)`.
- **Use arrow functions for short callbacks**: They keep small array callbacks readable.
- **Use named functions for reused or complex callbacks**: A good name explains the behavior.
- **Know what the callback should return**: `map()`, `filter()`, and `find()` use return values differently.
- **Use `forEach()` for side effects only**: Use `map()` when you need a new array.
- **Prefer promises and `async` / `await` for new async code**: Async callbacks are mostly important for reading older code.

## Summary

Callbacks are functions passed into other functions. They let one function customize what another function does.

You will see callbacks in array methods, event listeners, timers, and older async APIs. Pass callbacks without calling them, use clear names, and choose promises or `async` / `await` for new asynchronous code.
