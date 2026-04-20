---
title: Errors and Control Flow
sidebar_position: 11
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are errors?

**Errors** are objects that represent something going wrong. In JavaScript, errors also affect control flow: when an error is thrown, normal execution stops and JavaScript looks for error-handling code.

```javascript
throw new Error("Something went wrong");
```

You usually throw errors when your code cannot continue safely, and you catch errors when you can respond to the problem.

## Why this matters

Real programs deal with missing data, invalid input, network failures, broken JSON, and unexpected states. Error handling lets you fail clearly, recover when possible, and avoid silent bugs.

Good error handling answers three questions:

- What went wrong?
- Where can this be handled?
- Should the program recover, return a fallback, or stop?

## Common error types

JavaScript has several built-in error types.

### `ReferenceError`

A `ReferenceError` happens when you use a variable that does not exist:

```javascript
// This would cause a ReferenceError:
// console.log(missingValue);
```

### `TypeError`

A `TypeError` happens when a value is not the type or shape your code expected:

```javascript
const user = null;

// This would cause a TypeError:
// console.log(user.name);
```

### `SyntaxError`

A `SyntaxError` happens when JavaScript code is not valid syntax. These are usually caught before the code runs:

```javascript
// This would cause a SyntaxError:
// if (true {
//   console.log("missing parenthesis");
// }
```

### `RangeError`

A `RangeError` happens when a value is outside an allowed range:

```javascript
// This would cause a RangeError:
// const items = new Array(-1);
```

## Throwing errors

Use `throw` when a function cannot continue safely:

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }

  return a / b;
}
```

Throwing an error stops the function immediately:

```javascript
function getUserName(user) {
  if (!user) {
    throw new Error("User is required");
  }

  return user.name;
}
```

The `return` line only runs if `user` exists.

## `try` / `catch`

Use `try/catch` when code might throw and you can handle the failure:

```javascript
try {
  const data = JSON.parse("{ bad json }");
  console.log(data);
} catch (error) {
  console.log("Could not parse JSON:", error.message);
}

console.log("Program continues");
```

**What happens:**

1. JavaScript tries to run the code in `try`.
2. `JSON.parse()` throws an error.
3. JavaScript jumps to `catch`.
4. Code after the `try/catch` continues.

## The error object

The `catch` block receives the thrown error:

```javascript
try {
  JSON.parse("{ bad json }");
} catch (error) {
  console.log(error.name);    // "SyntaxError"
  console.log(error.message); // Error message
}
```

Common properties include:

- `name`: the error type name
- `message`: the human-readable message
- `stack`: where the error happened

`stack` is useful for debugging, but it is usually too detailed for beginner-facing output.

## Catching specific errors

Use `instanceof` when you need different handling for different error types:

```javascript
try {
  JSON.parse("{ bad json }");
} catch (error) {
  if (error instanceof SyntaxError) {
    console.log("Invalid JSON");
  } else {
    throw error;
  }
}
```

If you cannot handle an error, rethrow it. Do not silently swallow it.

## `finally`

A `finally` block always runs, whether an error happened or not:

```javascript
let isLoading = true;

try {
  runOperation();
} catch (error) {
  console.log("Operation failed:", error.message);
} finally {
  isLoading = false;
}
```

Use `finally` for cleanup: resetting loading state, releasing resources, closing connections, or clearing temporary state.

## Error propagation

If an error is not caught, it moves up the call stack:

```javascript
function level1() {
  level2();
}

function level2() {
  level3();
}

function level3() {
  throw new Error("Failed in level3");
}

try {
  level1();
} catch (error) {
  console.log(error.message); // "Failed in level3"
}
```

The error starts in `level3`, moves through `level2` and `level1`, and is caught by the `catch` block.

If no code catches the error, the program usually stops or logs the error to the console.

## Errors vs normal control flow

Errors are useful for exceptional cases. Do not use them for ordinary decisions that are easy to check first.

Avoid this:

```javascript
function getItem(array, index) {
  try {
    return array[index].name;
  } catch (error) {
    return null;
  }
}
```

Prefer checking first:

```javascript
function getItem(array, index) {
  const item = array[index];

  if (!item) {
    return null;
  }

  return item.name;
}
```

Use `if` statements for expected branches. Use errors when something violates the assumptions your code needs to continue.

## Custom errors

You can create custom error classes when a specific kind of failure matters:

```javascript
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

function validateEmail(email) {
  if (!email.includes("@")) {
    throw new ValidationError("Email must include @");
  }
}
```

Custom errors are most useful in larger applications where callers need to respond differently to different failures.

## Async errors

Async code needs its own error handling. With `async` / `await`, use `try/catch`:

```javascript
async function loadUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    return await response.json();
  } catch (error) {
    console.error("Failed to load user:", error);
    throw error;
  }
}
```

With promises, use `.catch()`:

```javascript
fetch("/api/users/1")
  .then(response => response.json())
  .then(user => console.log(user))
  .catch(error => {
    console.error("Failed to load user:", error);
  });
```

Async patterns are covered in more detail in the [async guide](../async/asyncronous).

## Common patterns

### Parsing JSON safely

```javascript
function parseJSONOrNull(text) {
  try {
    return JSON.parse(text);
  } catch (error) {
    return null;
  }
}

console.log(parseJSONOrNull('{"name":"Alice"}')); // { name: "Alice" }
console.log(parseJSONOrNull("{ bad json }"));     // null
```

This is a good use of `try/catch` because invalid JSON is an expected possibility.

### Validating inputs early

```javascript
function createUser(name, email) {
  if (!name) {
    throw new Error("Name is required");
  }

  if (!email.includes("@")) {
    throw new Error("Email must include @");
  }

  return { name, email };
}
```

Clear validation errors make bugs easier to find.

### Handling and rethrowing

```javascript
try {
  saveSettings(settings);
} catch (error) {
  console.error("Could not save settings:", error.message);
  throw error;
}
```

Log or add context when useful, then rethrow if this part of the program cannot recover.

## Best practices

- **Throw errors when code cannot continue safely**.
- **Catch errors where you can respond**: recover, show a message, retry, or return a fallback.
- **Do not swallow errors silently**: it hides bugs.
- **Use descriptive messages**: include what was expected and what went wrong.
- **Validate inputs early**: fail before doing deeper work.
- **Use normal conditionals for expected branches**: do not use `try/catch` as a replacement for `if`.
- **Rethrow errors you cannot handle**.
- **Use `finally` for cleanup** when cleanup must happen either way.

## Summary

Errors represent failures and change control flow. Use `throw` when a function cannot continue, `try/catch` when you can handle a failure, and `finally` when cleanup must always run. Catch errors at the level that can respond meaningfully, avoid swallowing them silently, and use ordinary conditionals for normal expected decisions.
