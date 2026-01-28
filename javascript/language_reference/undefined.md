---
title: Undefined
sidebar_position: 8
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

`undefined` is a primitive value that indicates a variable has been declared but not assigned a value, or a property doesn't exist on an object. It is one of JavaScript's primitive values and is treated as falsy for boolean operations.

```javascript
typeof undefined  // "undefined"
undefined === undefined  // true
undefined == null        // true (loose equality)
undefined === null       // false (strict equality)
```

## When undefined appears

### Uninitialized Variables

```javascript
let x
console.log(x)           // undefined
```

### Missing Function Parameters

```javascript
function example(param) {
  console.log(param)     // undefined if not passed
}

example()                // undefined
```

### Missing Object Properties

```javascript
const obj = { a: 1 }
console.log(obj.b)       // undefined
```

### Function Return Value

```javascript
function noReturn() {
  // No return statement
}

console.log(noReturn())  // undefined
```

### Array Holes

```javascript
const arr = [1, , 3]     // Sparse array
console.log(arr[1])      // undefined
```

## Undefined vs null

| Aspect        | `undefined`                    | `null`                          |
| ------------- | ------------------------------ | ------------------------------- |
| **Type**      | `undefined`                    | `object` (bug)                  |
| **Intent**    | Variable not assigned          | Intentional absence of value    |
| **Default**   | Automatically assigned         | Must be explicitly set          |
| **Usage**     | Uninitialized variables        | Explicitly set to "no value"    |

<!-- ```javascript
let x                    // undefined (not assigned)
let y = null            // null (explicitly set)

function example(param) {
  console.log(param)    // undefined if not passed
}

example()               // undefined
example(null)           // null
``` -->

## Checking for undefined

```javascript
// Strict equality (recommended)
value === undefined     // true if undefined
value !== undefined     // true if not undefined

// Loose equality (not recommended)
value == undefined      // true if undefined or null

// typeof check (works even if undefined is shadowed)
typeof value === 'undefined'  // true if undefined
```

## The undefined Global

`undefined` is a property of the global object, but it's not a reserved word, so it can be shadowed:

```javascript
// In older code, undefined could be reassigned (not in strict mode)
// Modern JavaScript: undefined is read-only

(function() {
  let undefined = "not undefined"
  console.log(undefined)  // "not undefined" (local variable)
})()

// Safe check using typeof
function isUndefined(value) {
  return typeof value === 'undefined'
}
```

## Common Patterns

<!-- ### Default Parameters

```javascript
function greet(name = "Guest") {
  return `Hello, ${name}!`
}

greet()                 // "Hello, Guest!"
greet("Alice")          // "Hello, Alice!"
``` -->

### Optional Chaining

Optional chaining (`?.`) allows you to safely access nested object properties without throwing an error if any part of the chain is `null` or `undefined`. Instead of throwing an error, it returns `undefined`.

```javascript
> const user = { name: "Alice" }
undefined

> user.address?.city
undefined

// Without optional chaining, this would throw an error
> user.address.city
TypeError: Cannot read property 'city' of undefined

// Works with multiple levels
> const data = { user: { profile: { email: "alice@example.com" } } }
undefined

> data.user?.profile?.email
"alice@example.com"

> data.user?.profile?.phone
undefined

// Also works with method calls
> const obj = { method() { return "hello" } }
undefined

> obj.method?.()
"hello"

> obj.nonexistent?.()
undefined

// Works with array access
> const arr = [[1, 2, 3]]
undefined

> arr[0]?.[2]
3

> arr[1]?.[0]
undefined
```

Optional chaining is especially useful when working with data from APIs or user input where properties might not exist.

### Nullish Coalescing

The nullish coalescing operator (`??`) provides a default value when a variable is `null` or `undefined`. Unlike the logical OR operator (`||`), it only checks for `null` and `undefined`, not other falsy values like `0`, `""`, or `false`.

```javascript
> const username = undefined
undefined

> const name = username ?? "Guest"
undefined

> name
"Guest"

// Only checks for null/undefined, not other falsy values
> const count = 0
undefined

> count ?? 10
0

> count || 10
10

> const message = ""
undefined

> message ?? "No message"
""

> message || "No message"
"No message"

// Common pattern: combining with optional chaining
> const user = { name: "Alice" }
undefined

> const displayName = user.name ?? user.email ?? "Anonymous"
undefined

> displayName
"Alice"

> const user2 = {}
undefined

> const displayName2 = user2.name ?? user2.email ?? "Anonymous"
undefined

> displayName2
"Anonymous"
```

The nullish coalescing operator is perfect when you want to provide defaults but preserve other falsy values like `0` or empty strings.

## JSON Serialization

`undefined` is not preserved in JSON. Properties with `undefined` values are omitted:

```javascript
JSON.stringify({ name: undefined })  // '{}'
JSON.stringify({ name: null })      // '{"name":null}'
```

## Best Practices

1. **Don't assign `undefined`**: Let it be the default for uninitialized variables.

2. **Use `null` for intentional absence**: If you need to explicitly indicate "no value", use `null`.

3. **Use strict equality**: Always use `===` to check for `undefined`.

4. **Use default parameters**: Instead of checking for `undefined` inside functions:

```javascript
// Good
function greet(name = "Guest") {
  return `Hello, ${name}!`
}

// Less ideal
function greet(name) {
  name = name || "Guest"
  return `Hello, ${name}!`
}
```

5. **Use optional chaining**: For safe property access:

```javascript
// Safe access
const city = user?.address?.city  // undefined if any part is missing
```

