---
title: Modules
sidebar_position: 12
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Why modules exist

As programs grow, keeping all code in one file becomes unmanageable. **Modules** let you:
- Split code across multiple files
- Organize related functionality together
- Reuse code across different parts of your program
- Avoid naming conflicts (each module has its own scope)
- Control what other code can access (public vs private)

JavaScript modules let you write code in separate files and import what you need where you need it.

## JavaScript modules (`export` and `import`)

Introduced in version **ES6** (2015), modern JavaScript uses `export` and `import` statements . This is the standard way to organize code in JavaScript today.

### Setting up modules

To use ES6 modules, you need to indicate that your JavaScript file is a module:

**In Node.js:** Add `"type": "module"` to your `package.json`:

```json
{
  "type": "module"
}
```

Or use `.mjs` file extension: `myModule.mjs`

**In browsers:** Use `<script type="module">`:

```html
<script type="module" src="main.js"></script>
```

## Commonjs vs es6 modules

:::note
Node.js historically used **CommonJS** (`require`/`module.exports`), but ES6 modules are now the standard. This guide focuses on ES6 modules.
:::

If you see `require()` or `module.exports` in code, that's CommonJS (older style):

```javascript
// CommonJS (old style)
const math = require('./math.js');
module.exports = { add, subtract };

// ES6 modules (modern style - preferred)
import { add, subtract } from './math.js';
export { add, subtract };
```

**Use ES6 modules** in new projects.


## `export` — Making code available

Use `export` to make functions, variables, classes, etc. available to other modules.

### Named exports

**Named exports** let you export multiple things from a module:

```javascript
// math.js
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

export const PI = 3.14159;
```

You can also export at the end of the file:

```javascript
// math.js
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

const PI = 3.14159;

export { add, subtract, PI };
```

### Default export

A **default export** is the main export from a module (only one per module):

```javascript
// user.js
export default function createUser(name, email) {
  return {
    name,
    email,
    createdAt: new Date()
  };
}
```

Or:

```javascript
// user.js
function createUser(name, email) {
  return {
    name,
    email,
    createdAt: new Date()
  };
}

export default createUser;
```

**Note:** You can combine named and default exports in the same module:

```javascript
// utils.js
export default function mainFunction() {
  // ...
}

export function helperFunction() {
  // ...
}

export const CONSTANT = "value";
```

## `import` — Using exported code

Use `import` to bring code from other modules into your current file.

### Importing named exports

Import named exports using curly braces `{}`:

```javascript
// main.js
import { add, subtract, PI } from './math.js';

console.log(add(5, 3));        // 8
console.log(subtract(10, 4));  // 6
console.log(PI);               // 3.14159
```

You can import with different names using `as`:

```javascript
import { add as addNumbers, subtract as subtractNumbers } from './math.js';
```

### Importing default exports

Import default exports without curly braces:

```javascript
// main.js
import createUser from './user.js';

const user = createUser("Alice", "alice@example.com");
```

You can rename default imports:

```javascript
import createUser as makeUser from './user.js';
```

### Importing everything

You can import all named exports as an object:

```javascript
import * as math from './math.js';

console.log(math.add(5, 3));       // 8
console.log(math.subtract(10, 4)); // 6
console.log(math.PI);              // 3.14159
```

**Note:** This doesn't include default exports.

### Combining imports

You can import both default and named exports:

```javascript
// utils.js
export default function main() { }
export function helper() { }

// main.js
import main, { helper } from './utils.js';
//      ^^^^  ^^^^^^^^
//   default   named
```

## File organization basics

### Project structure

Organize modules in a logical file structure:

```
my-project/
  ├── src/
  │   ├── utils/
  │   │   ├── math.js
  │   │   └── strings.js
  │   ├── models/
  │   │   └── user.js
  │   └── main.js
  └── package.json
```

### Module responsibilities

Each module should have a clear, single responsibility. This makes your code easier to find, understand, and maintain.

**Why single responsibility matters:**
- **Easier to find code**: You know `add` is in `math.js`, not a generic `utils.js`
- **Clearer dependencies**: A module about math doesn't need user management code
- **Better organization**: Related functions are grouped together
- **Easier testing**: You can test math functions without loading user management code

**Good organization** - each module has a single responsibility:

```
my-project/
  ├── src/
  │   ├── utils/
  │   │   ├── math.js        // add, multiply, divide
  │   │   └── strings.js     // parseEmail, formatName
  │   ├── models/
  │   │   └── user.js        // createUser, getUserById
  │   └── main.js
```

Clear and organized. Need math functions? Check `utils/math.js`. Need user management? Check `models/user.js`.

**Bad organization** - everything dumped into a single file:

```
my-project/
  ├── src/
  │   ├── utils.js           // add, multiply, parseEmail, createUser, formatName, etc.
  │   └── main.js
```

Everything is in one file. Where's the `add` function? In `utils.js` with 50 other unrelated functions. Good luck finding it quickly!

When everything is in one "utils" file, it becomes a dumping ground where functions are hard to find and unrelated code gets tangled together.

### Naming conventions

- Use descriptive file names: `userService.js`, `mathUtils.js`
- Match export names to their purpose: `createUser`, `calculateTotal`
- Use camelCase for JavaScript files: `userManager.js` (not `user_manager.js`)

## Real-world example

Here's a simple example showing modules in action:

```javascript
// config.js
export const API_URL = "https://api.example.com";
export const TIMEOUT = 5000;

// user.js
import { API_URL, TIMEOUT } from './config.js';

export function fetchUser(id) {
  return fetch(`${API_URL}/users/${id}`, {
    timeout: TIMEOUT
  });
}

// main.js
import { fetchUser } from './user.js';
import { API_URL } from './config.js';

async function displayUser(id) {
  const user = await fetchUser(id);
  console.log(user);
}
```

## Module scope

Each module has its own scope. Variables and functions declared in a module are **private** unless explicitly exported:

```javascript
// utils.js
const privateVar = "I'm private";  // Not exported, can't be accessed outside

export function publicFunction() {
  console.log(privateVar);  // Can access privateVar inside this module
  return "I'm public";
}

// main.js
import { publicFunction } from './utils.js';

console.log(privateVar);  // Error: privateVar is not defined
publicFunction();         // Works
```

This is a form of **encapsulation**—you control what's accessible from outside the module.

## Circular dependencies

**Circular dependencies** occur when module A imports from module B, and module B imports from module A:

```javascript
// a.js
import { funcB } from './b.js';
export function funcA() { }

// b.js
import { funcA } from './a.js';
export function funcB() { }
```

While JavaScript allows circular dependencies, they can cause confusing bugs. **Avoid them when possible** by:
- Restructuring code to remove the circular dependency
- Moving shared code to a third module
- Using dependency injection

