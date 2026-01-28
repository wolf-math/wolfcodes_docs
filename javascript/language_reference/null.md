---
title: "null"
sidebar_position: 7
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## Definition

`null` is a primitive value that represents the intentional absence of any object value. It is one of JavaScript's primitive values and is treated as falsy for boolean operations.

```javascript
typeof null         // "object" (this is a bug/legacy behavior)
null === null       // true
null == undefined   // true (loose equality)
null === undefined  // false (strict equality)
```

## Using null

`null` is typically used to indicate that a variable intentionally has no value or that an object reference is intentionally empty.

```javascript
let user = null          // User not set yet
let data = null          // Data not loaded yet
```

## Null vs undefined

| Aspect        | `null`                          | `undefined`                     |
| ------------- | ------------------------------- | ------------------------------- |
| **Type**      | `object` (bug)                  | `undefined`                     |
| **Intent**    | Intentional absence of value    | Variable not assigned           |
| **Default**   | Must be explicitly set          | Default for uninitialized vars  |
| **Usage**     | Explicitly set to "no value"    | Automatically assigned          |

<!-- ```javascript
let x                   // undefined (not assigned)
let y = null            // null (explicitly set)

function example(param) {
  console.log(param)    // undefined if not passed
}

example(x)              // undefined
example(y)              // null
``` -->

## Common Use Cases

### Resetting Values

```javascript
let data = fetchData()
// ... use data ...
data = null             // Clear reference
```

### Optional Parameters

```javascript
function processUser(user) {
  if (user === null) {
    return "No user provided"
  }
  return `Processing ${user.name}`
}
```

### Object Properties

```javascript
const person = {
  name: "Alice",
  age: null            // Age not provided
}
```

## Type Checking

```javascript
// Check for null
value === null         // true if null
value !== null         // true if not null

// Check for null or undefined
value == null          // true if null or undefined
value === null || value === undefined  // explicit check
```

## Nullish Coalescing

The nullish coalescing operator (`??`) provides a default value when a variable is `null` or `undefined`:

```javascript
const name = username ?? "Guest"        // "Guest" if username is null/undefined
const value = input ?? null             // null if input is null/undefined
```

## JSON Serialization

`null` is preserved in JSON:

```javascript
JSON.stringify({ name: null })         // '{"name":null}'
JSON.parse('{"name":null}')            // { name: null }
```

## Best Practices

1. **Use `null` for intentional absence**: When you want to explicitly indicate "no value".

2. **Use `undefined` for uninitialized**: When a variable hasn't been assigned yet.

3. **Be consistent**: Choose one approach and stick with it in your codebase.

4. **Use nullish coalescing**: Prefer `??` over `||` when you only want to check for `null`/`undefined`:

```javascript
// Only checks null/undefined
const value = input ?? "default"

// Checks all falsy values (including 0, "", false)
const value = input || "default"
```

