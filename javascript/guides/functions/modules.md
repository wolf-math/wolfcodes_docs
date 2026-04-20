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

## What are modules?

**Modules** let you split JavaScript code across multiple files. A module can keep some code private and export the parts other files should use.

```javascript
// math.js
export function add(a, b) {
  return a + b;
}

// main.js
import { add } from "./math.js";

console.log(add(5, 3)); // 8
```

Modules help you organize code as projects grow.

## Why this matters

Small programs can live in one file. Larger programs become easier to understand when related code is grouped into separate files: math helpers, API calls, UI behavior, data models, configuration, and so on.

Modules let you:

- Split code into focused files
- Reuse code across the project
- Control what each file exposes
- Avoid global variable conflicts
- Make dependencies explicit with `import`

## Using JavaScript modules

Modern JavaScript uses `export` and `import`. How you enable modules depends on where the code runs.

### In the browser

In the browser, no `package.json` is required. Load module code with `type="module"`:

```html
<script type="module" src="main.js"></script>
```

That tells the browser to treat `main.js` as a module, so it can use `import` and `export`.

### In Node.js

In Node.js, you have two common options.

Add `"type": "module"` to `package.json` if you want `.js` files to be treated as ES modules:

```json
{
  "type": "module"
}
```

Or use the `.mjs` file extension, which Node treats as an ES module without needing `"type": "module"`:

```text
main.mjs
math.mjs
```

This guide focuses on modern ES modules, not older CommonJS.

## Named exports

Use **named exports** when a module exports multiple things:

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

Import named exports with curly braces:

```javascript
// main.js
import { add, subtract, PI } from "./math.js";

console.log(add(5, 3));       // 8
console.log(subtract(10, 4)); // 6
console.log(PI);              // 3.14159
```

You can also export at the end of a file:

```javascript
// math.js
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

export { add, subtract };
```

## Default exports

Use a **default export** when a module has one main thing to export:

```javascript
// createUser.js
export default function createUser(name, email) {
  return {
    name,
    email
  };
}
```

Import default exports without curly braces:

```javascript
// main.js
import createUser from "./createUser.js";

const user = createUser("Alice", "alice@example.com");

console.log(user.name); // "Alice"
```

Default imports can be renamed by the importing file:

```javascript
import makeUser from "./createUser.js";
```

Use this power carefully. Renaming can be helpful, but inconsistent names make code harder to search.

## Named vs default exports

Use named exports when:

- A file exports several related utilities
- You want imports to use the exact exported names
- You want easier auto-imports and refactors

Use default exports when:

- A file exists mainly for one function, class, or component
- The imported name may reasonably vary by context

```javascript
// Good named exports for utilities
export function formatDate(date) {}
export function parseDate(text) {}

// Good default export for one main thing
export default function createUser(data) {}
```

Many teams prefer named exports most of the time because they make dependencies explicit and consistent.

## Importing with aliases

Use `as` to rename a named import:

```javascript
import { add as addNumbers } from "./math.js";

console.log(addNumbers(2, 3)); // 5
```

Use aliases when names would conflict or when a clearer local name helps.

## Importing everything

Use `* as name` to import all named exports as an object:

```javascript
import * as math from "./math.js";

console.log(math.add(5, 3)); // 8
console.log(math.PI);        // 3.14159
```

This can be useful for grouped utilities, but avoid using it to hide unclear module boundaries.

## Module scope

Each module has its own scope. Variables and functions are private unless exported:

```javascript
// counter.js
let count = 0;

export function increment() {
  count += 1;
  return count;
}
```

Another file can import `increment`, but it cannot access `count` directly:

```javascript
// main.js
import { increment } from "./counter.js";

console.log(increment()); // 1

// This would cause an error:
// console.log(count); // ReferenceError
```

This makes modules a useful way to encapsulate implementation details.

## File organization

Give each module a clear responsibility:

```text
src/
  main.js
  config.js
  api/
    users.js
  utils/
    math.js
    strings.js
```

Good module names describe what lives inside:

- `math.js`
- `formatDate.js`
- `userApi.js`
- `createUser.js`
- `storage.js`

Avoid dumping unrelated helpers into one giant `utils.js`. A file that contains everything becomes hard to search, test, and maintain.

## Real-world example

```javascript
// config.js
export const API_URL = "https://api.example.com";
export const TIMEOUT = 5000;
```

```javascript
// usersApi.js
import { API_URL } from "./config.js";

export async function fetchUser(id) {
  const response = await fetch(`${API_URL}/users/${id}`);
  return response.json();
}
```

```javascript
// main.js
import { fetchUser } from "./usersApi.js";

const user = await fetchUser(1);

console.log(user);
```

Each file has a focused job:

- `config.js` stores shared configuration.
- `usersApi.js` handles user API calls.
- `main.js` uses the exported behavior.

## CommonJS vs ES modules

Older Node.js code often uses CommonJS:

```javascript
const math = require("./math.js");

module.exports = {
  add,
  subtract
};
```

Modern JavaScript uses ES modules:

```javascript
import { add } from "./math.js";

export { add };
```

Use ES modules in new projects unless the project already uses CommonJS.

## Circular dependencies

A **circular dependency** happens when two modules import from each other:

```javascript
// a.js
import { b } from "./b.js";
export function a() {}

// b.js
import { a } from "./a.js";
export function b() {}
```

JavaScript allows circular dependencies, but they can cause confusing bugs because one module may run before the other has finished setting up its exports.

To avoid circular dependencies:

- Move shared code into a third module.
- Simplify module responsibilities.
- Pass dependencies as arguments instead of importing directly.
- Watch for two files that know too much about each other.

## Common patterns

### Utility module

```javascript
// strings.js
export function capitalize(text) {
  return text.charAt(0).toUpperCase() + text.slice(1);
}

export function trimLower(text) {
  return text.trim().toLowerCase();
}
```

### Configuration module

```javascript
// config.js
export const API_URL = "https://api.example.com";
export const DEFAULT_TIMEOUT = 5000;
```

### Barrel file

A barrel file re-exports from several files:

```javascript
// utils/index.js
export { capitalize } from "./strings.js";
export { add } from "./math.js";
```

Barrel files can make imports shorter, but too many barrels can make dependencies harder to trace.

## Best practices

- **Use ES modules for new code**: Prefer `import` and `export`.
- **Keep modules focused**: One module should have one clear responsibility.
- **Prefer named exports for utilities**: They make imports explicit.
- **Use default exports for one-main-thing files** when that matches the project style.
- **Export only what other files need**: Keep implementation details private.
- **Use clear file names**: The filename should hint at the module's purpose.
- **Avoid circular dependencies**: Move shared code to a separate module.
- **Keep import paths readable**: Deep, tangled paths often signal organization problems.

## Summary

Modules split JavaScript code into focused files. Use `export` to make values available and `import` to use them elsewhere. Named exports work well for utilities, default exports work well for one main value, and module scope keeps unexported code private. Good modules make dependencies visible, reduce globals, and keep large programs easier to maintain.
