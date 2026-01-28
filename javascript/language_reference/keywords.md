---
title: Keywords
sidebar_position: 19
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
<!-- ## Properties

```javascript
// JavaScript keywords (ES2023)
const keywords = [
  'break', 'case', 'catch', 'class', 'const', 'continue', 'debugger',
  'default', 'delete', 'do', 'else', 'export', 'extends', 'finally',
  'for', 'function', 'if', 'import', 'in', 'instanceof', 'new', 'return',
  'super', 'switch', 'this', 'throw', 'try', 'typeof', 'var', 'void',
  'while', 'with', 'yield', 'await', 'let', 'static', 'enum', 'implements',
  'interface', 'package', 'private', 'protected', 'public'
]
``` -->

## Definition

A keyword is a special word that is part of JavaScript's syntax. They are not functions, methods, or objects. They define how the language is structured and executed.

| Category                      | Examples                                                                     | Description                                 |
| ----------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------- |
| **Control flow**              | `if`, `else`, `for`, `while`, `do`, `break`, `continue`, `return`, `switch`, `case`, `default` | Manage loops and decision-making            |
| **Structure and definitions** | `function`, `class`, `const`, `let`, `var`, `import`, `export`               | Define functions, classes, and variables    |
| **Logical and comparison**   | `typeof`, `instanceof`, `in`, `void`, `delete`                               | Type checking and property operations       |
| **Exception handling**      | `try`, `catch`, `finally`, `throw`                                           | Handle errors                               |
| **Object-oriented**           | `new`, `this`, `super`, `extends`, `static`                                  | Object creation and inheritance             |
| **Asynchronous**              | `async`, `await`, `yield`                                                    | Asynchronous programming                    |
| **Special purpose**           | `null`, `undefined`, `true`, `false`, `debugger`, `with`                    | Language-level constants or syntax keywords |

## Keyword definitions

### `if`

Starts a conditional block that executes code only when a condition is `true`. The bread and butter of decision-making.

```javascript
if (x > 0) {
  console.log("positive")
}
```

---

### `else`

Executes code when the preceding `if` condition is `false`. The "otherwise" clause.

```javascript
if (x > 0) {
  console.log("positive")
} else {
  console.log("not positive")
}
```

---

### `for`

Creates a loop that executes a block of code a specified number of times.

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i)
}
```

---

### `while`

Creates a loop that executes a block of code as long as a condition is `true`.

```javascript
let i = 0
while (i < 5) {
  console.log(i)
  i++
}
```

---

### `do`

Creates a loop that executes at least once, then continues while a condition is `true`.

```javascript
let i = 0
do {
  console.log(i)
  i++
} while (i < 5)
```

---

### `break`

Exits a loop or `switch` statement immediately.

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) break
  console.log(i)
}
```

---

### `continue`

Skips the rest of the current loop iteration and continues with the next iteration.

```javascript
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) continue
  console.log(i)  // Only odd numbers
}
```

---

### `return`

Exits a function and optionally returns a value.

```javascript
function add(a, b) {
  return a + b
}
```

---

### `switch`

Evaluates an expression and executes code based on matching cases.

```javascript
switch (value) {
  case 1:
    console.log("one")
    break
  case 2:
    console.log("two")
    break
  default:
    console.log("other")
}
```

---

### `case`

Defines a match condition in a `switch` statement.

---

### `default`

Defines the default case in a `switch` statement when no other cases match.

---

### `function`

Declares a function.

```javascript
function greet(name) {
  return `Hello, ${name}!`
}
```

---

### `class`

Declares a class for object-oriented programming.

```javascript
class Person {
  constructor(name) {
    this.name = name
  }
}
```

---

### `const`

Declares a constant variable that cannot be reassigned.

```javascript
const PI = 3.14159
```

---

### `let`

Declares a block-scoped variable that can be reassigned.

```javascript
let x = 5
x = 10  // OK
```

---

### `var`

Declares a function-scoped variable (legacy, prefer `let` or `const`).

```javascript
var x = 5
```

---

### `import`

Imports bindings from another module.

```javascript
import { add } from './math.js'
import React from 'react'
```

---

### `export`

Exports bindings from a module.

```javascript
export function add(a, b) {
  return a + b
}

export const PI = 3.14159
```

---

### `try`

Starts a block of code to test for errors.

```javascript
try {
  riskyOperation()
} catch (error) {
  console.error(error)
}
```

---

### `catch`

Handles errors thrown in a `try` block.

```javascript
try {
  throw new Error("Something went wrong")
} catch (error) {
  console.error(error.message)
}
```

---

### `finally`

Executes code after `try` and `catch`, regardless of the result.

```javascript
try {
  // code
} catch (error) {
  // handle error
} finally {
  // always executes
}
```

---

### `throw`

Throws a user-defined exception.

```javascript
throw new Error("Something went wrong")
```

---

### `typeof`

Returns a string indicating the type of a value.

```javascript
typeof 42           // "number"
typeof "hello"      // "string"
typeof true         // "boolean"
typeof undefined    // "undefined"
typeof null         // "object" (quirk)
```

---

### `instanceof`

Tests whether an object is an instance of a constructor.

```javascript
[] instanceof Array        // true
[] instanceof Object       // true
new Date() instanceof Date // true
```

---

### `in`

Tests whether a property exists in an object.

```javascript
'name' in { name: 'Alice' }  // true
'age' in { name: 'Alice' }   // false
```

---

### `new`

Creates an instance of a constructor function or class.

```javascript
new Date()
new Array(5)
new Person('Alice')
```

---

### `this`

Refers to the current object context.

```javascript
const person = {
  name: 'Alice',
  greet() {
    return `Hello, I'm ${this.name}`
  }
}
```

---

### `super`

Calls the parent class constructor or method.

```javascript
class Animal {
  speak() {
    return "Some sound"
  }
}

class Dog extends Animal {
  speak() {
    return super.speak() + " - Woof!"
  }
}
```

---

### `extends`

Creates a class that inherits from another class.

```javascript
class Dog extends Animal {
  // ...
}
```

---

### `static`

Defines a static method or property on a class.

```javascript
class Math {
  static add(a, b) {
    return a + b
  }
}
```

---

### `async`

Declares an asynchronous function.

```javascript
async function fetchData() {
  const response = await fetch('/api/data')
  return response.json()
}
```

---

### `await`

Pauses execution until a Promise is resolved.

```javascript
async function example() {
  const data = await fetch('/api/data')
  return data.json()
}
```

---

### `yield`

Pauses and resumes a generator function.

```javascript
function* numbers() {
  yield 1
  yield 2
  yield 3
}
```

---

### `void`

Evaluates an expression and returns `undefined`.

```javascript
void 0  // undefined
```

---

### `delete`

Removes a property from an object.

```javascript
const obj = { a: 1, b: 2 }
delete obj.a
// obj is now { b: 2 }
```

---

### `debugger`

Invokes any available debugging functionality.

```javascript
function problematicFunction() {
  debugger  // Execution pauses here if debugger is active
  // ...
}
```

---

### `with` (deprecated)

Extends the scope chain for a statement. **Deprecated**: Do not use. It's not allowed in strict mode and makes code harder to understand.

---

### `enum`, `implements`, `interface`, `package`, `private`, `protected`, `public`

These are reserved words in JavaScript but not currently used. They are reserved for potential future use or for compatibility with other languages (like TypeScript).

