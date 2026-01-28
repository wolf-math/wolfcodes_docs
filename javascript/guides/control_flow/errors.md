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

**Errors** occur when something goes wrong in your program. JavaScript has several types of errors, and understanding how to handle them is crucial for writing robust code.

In JavaScript, errors are not just problems, they're also a **control flow mechanism**. When an error occurs, it interrupts normal execution and jumps to error-handling code.

## Runtime errors

Errors that occur while your program is running are **runtime errors**:

```javascript
const x = undefined;
console.log(x.name);  // TypeError: Cannot read property 'name' of undefined

const arr = [1, 2, 3];
console.log(arr[10]);  // undefined (not an error, but probably not what you want)
```

### Common error types

- **`ReferenceError`** — variable doesn't exist
- **`TypeError`** — wrong type or trying to use something that doesn't exist
- **`SyntaxError`** — invalid JavaScript syntax (usually caught before runtime)
- **`RangeError`** — value is out of range

```javascript
// ReferenceError
console.log(nonExistentVar);  // ReferenceError: nonExistentVar is not defined

// TypeError
const x = null;
x.someMethod();  // TypeError: Cannot read property 'someMethod' of null

// RangeError
const arr = new Array(-1);  // RangeError: Invalid array length
```

## `try` / `catch`

The `try/catch` statement lets you handle errors gracefully:

```javascript
try {
  // Code that might throw an error
  const result = riskyOperation();
  console.log(result);
} catch (error) {
  // Code to run if an error occurs
  console.log("Something went wrong:", error.message);
}
```

### Basic structure

```javascript
try {
  // Try to execute this code
  const data = JSON.parse(invalidJson);
} catch (error) {
  // Handle any errors that occur
  console.error("Error parsing JSON:", error.message);
}

// Code continues here even if an error occurred
console.log("Program continues...");
```

### Accessing error information

The `catch` block receives an error object with useful information:

```javascript
try {
  const x = undefined;
  console.log(x.name);
} catch (error) {
  console.log(error.name);     // "TypeError"
  console.log(error.message);  // "Cannot read property 'name' of undefined"
  console.log(error.stack);    // Stack trace (where the error occurred)
}
```

### Catching specific errors

You can check error types in the `catch` block:

```javascript
try {
  riskyOperation();
} catch (error) {
  if (error instanceof TypeError) {
    console.log("Type error occurred");
  } else if (error instanceof ReferenceError) {
    console.log("Reference error occurred");
  } else {
    console.log("Some other error:", error.message);
  }
}
```

## Throwing errors

You can create and throw your own errors using the `throw` statement:

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error("Division by zero is not allowed");
  }
  return a / b;
}

try {
  const result = divide(10, 0);
} catch (error) {
  console.log(error.message);  // "Division by zero is not allowed"
}
```

### Throwing different error types

You can throw specific error types:

```javascript
function getValue(obj, key) {
  if (!obj) {
    throw new TypeError("Object cannot be null or undefined");
  }
  if (!(key in obj)) {
    throw new ReferenceError(`Property '${key}' does not exist`);
  }
  return obj[key];
}
```

### Creating custom errors

You can create custom error classes:

```javascript
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

function validateEmail(email) {
  if (!email.includes("@")) {
    throw new ValidationError("Invalid email format");
  }
}
```

## Why errors are control flow

This is an important mental model: **errors are a form of control flow**, not just problems to avoid.

### Error-based control flow

Errors let you exit functions early and jump to error-handling code:

```javascript
function processUser(user) {
  if (!user) {
    throw new Error("User is required");
  }
  if (!user.email) {
    throw new Error("User email is required");
  }
  // Continue processing only if we get here
  return `Processing ${user.email}`;
}

try {
  const result = processUser(null);
  console.log(result);
} catch (error) {
  console.log("Validation failed:", error.message);
  // Handle the error gracefully
}
```

This is similar to early returns in functions, but for exceptional cases.

### Error propagation

If an error isn't caught, it propagates up the call stack:

```javascript
function level1() {
  level2();
}

function level2() {
  level3();
}

function level3() {
  throw new Error("Error in level3");
}

try {
  level1();  // Error propagates through level1 -> level2 -> level3
} catch (error) {
  console.log("Caught error:", error.message);  // Caught here
}
```

If no `try/catch` exists, the error eventually crashes your program (or logs to console in browsers).

## The `finally` block

The `finally` block always runs, whether an error occurred or not:

```javascript
try {
  riskyOperation();
} catch (error) {
  console.log("Error occurred");
} finally {
  console.log("This always runs");
  // Useful for cleanup (closing files, clearing resources, etc.)
}
```

Common uses for `finally`:
- Cleaning up resources
- Closing connections
- Resetting state

```javascript
let fileOpen = true;

try {
  readFile();
} catch (error) {
  console.log("Error reading file");
} finally {
  fileOpen = false;  // Always close the file
  console.log("File closed");
}
```

## Best practices

### 1. Don't catch errors you can't handle

```javascript
// Bad: catching but not handling
try {
  importantOperation();
} catch (error) {
  // Swallows the error silently (bad!)
}

// Better: handle or rethrow
try {
  importantOperation();
} catch (error) {
  console.error("Operation failed:", error);
  throw error;  // Re-throw if you can't handle it
}
```

### 2. Be specific with error messages

```javascript
// Bad: generic error
throw new Error("Error");

// Good: descriptive error
throw new Error("Cannot divide by zero. Value received: " + value);
```

### 3. Validate inputs early

```javascript
function processData(data) {
  // Validate early, throw errors clearly
  if (!data) {
    throw new Error("Data is required");
  }
  if (typeof data !== "object") {
    throw new TypeError("Data must be an object");
  }
  // Continue processing...
}
```

### 4. Use try/catch for expected errors

```javascript
// Good: handling expected errors
function parseJSON(jsonString) {
  try {
    return JSON.parse(jsonString);
  } catch (error) {
    return null;  // Return null if parsing fails
  }
}
```

### 5. Don't use try/catch for control flow

```javascript
// Bad: using try/catch as control flow
try {
  return array[index];
} catch (error) {
  return null;
}

// Good: check first
if (index < array.length) {
  return array[index];
}
return null;
```

## Errors in async code

Errors in asynchronous code require special handling (covered in the [async guide](../async/asyncronous)):

```javascript
async function fetchData() {
  try {
    const response = await fetch(url);
    return await response.json();
  } catch (error) {
    console.error("Failed to fetch:", error);
    throw error;
  }
}
```
