---
title: Booleans
sidebar_position: 4.2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are booleans?

**Booleans** are values that can only be `true` or `false`. Use booleans for yes/no decisions in your code.

```javascript
const isLoggedIn = true;
const hasPermission = false;

if (isLoggedIn) {
  console.log("Welcome back");
}
```

Booleans are the foundation of conditionals, validation checks, feature flags, loops, and many other decisions.

## Why this matters

Programs constantly make decisions: is the user logged in, did the request fail, is the form valid, should this button be disabled? Booleans let you represent those decisions clearly.

JavaScript also lets non-boolean values act like booleans in conditions. That behavior is useful, but it can surprise you if you do not understand truthy and falsy values.

## Boolean literals

JavaScript has two boolean literals:

```javascript
const yes = true;
const no = false;
```

They are lowercase. `True` and `False` are not JavaScript booleans.

## Comparisons produce booleans

Comparison operators return `true` or `false`:

```javascript
const age = 20;

console.log(age >= 18); // true
console.log(age < 18);  // false
console.log(age === 20); // true
console.log(age !== 20); // false
```

You can store comparison results in clearly named variables:

```javascript
const age = 20;
const isAdult = age >= 18;

console.log(isAdult); // true
```

## Logical operators

Logical operators combine or invert boolean-like values.

### `&&` means "and"

`&&` is truthy only when both sides are truthy:

```javascript
const isLoggedIn = true;
const hasPermission = true;

const canEdit = isLoggedIn && hasPermission;

console.log(canEdit); // true
```

### `||` means "or"

`||` is truthy when at least one side is truthy:

```javascript
const hasEmail = false;
const hasPhone = true;

const canContact = hasEmail || hasPhone;

console.log(canContact); // true
```

### `!` means "not"

`!` flips truthiness:

```javascript
const isLoading = false;

console.log(!isLoading); // true
```

Use it to toggle a boolean:

```javascript
let isOpen = false;

isOpen = !isOpen;

console.log(isOpen); // true
```

## Truthy and falsy values

In JavaScript, values do not need to be actual booleans to work in a condition. Values that act like `true` are **truthy**. Values that act like `false` are **falsy**.

### Falsy values

These values are falsy:

```javascript
false;
0;
-0;
0n;
"";
null;
undefined;
NaN;
```

Everything else is truthy.

### Truthy surprises

Some values may look empty or false-like, but they are truthy:

```javascript
Boolean("false"); // true
Boolean("0");     // true
Boolean([]);      // true
Boolean({});      // true
```

This happens because non-empty strings, arrays, and objects are truthy.

## Boolean conversion

Use `Boolean(value)` to convert a value to `true` or `false`:

```javascript
Boolean(1);       // true
Boolean(0);       // false
Boolean("hello"); // true
Boolean("");      // false
Boolean(null);    // false
```

You may also see double negation:

```javascript
!!"hello"; // true
!!0;       // false
```

For beginner-facing code, `Boolean(value)` is clearer.

## Short-circuit behavior

`&&` and `||` use **short-circuit evaluation**. They stop as soon as the result is known.

With `&&`, JavaScript stops at the first falsy value:

```javascript
const result = false && getValue();

console.log(result); // false
```

`getValue()` never runs because the left side is already falsy.

With `||`, JavaScript stops at the first truthy value:

```javascript
const username = "" || "Guest";

console.log(username); // "Guest"
```

This is useful, but it can also hide bugs when `0` or `""` are valid values.

## Default values: `||` vs `??`

Use `||` when any falsy value should trigger the default:

```javascript
const displayName = "" || "Guest";

console.log(displayName); // "Guest"
```

Use `??` when only `null` or `undefined` should trigger the default:

```javascript
const retryCount = 0;
const retries = retryCount ?? 3;

console.log(retries); // 0
```

**Rule of thumb:** Use `??` when `0`, `false`, or `""` should remain valid values.

## Common pitfalls

### The string `"false"` is truthy

```javascript
const input = "false";

if (input) {
  console.log("This runs");
}
```

If you need to parse a string into a boolean, compare explicitly:

```javascript
const input = "false";
const value = input === "true";

console.log(value); // false
```

### Empty arrays are truthy

```javascript
const items = [];

if (items) {
  console.log("This runs even though the array is empty");
}
```

Check `.length` when you care whether an array has items:

```javascript
if (items.length > 0) {
  console.log("Array has items");
}
```

### Loose equality can hide type bugs

```javascript
0 == false;  // true
"" == false; // true
```

Use strict equality instead:

```javascript
0 === false;  // false
"" === false; // false
```

## Common patterns

### Guard clauses

Use booleans to stop early when a condition is not met:

```javascript
function saveUser(user) {
  if (!user) {
    return;
  }

  console.log("Saving user");
}
```

### Combining conditions

```javascript
const age = 25;
const hasLicense = true;
const hasInsurance = true;

const canDrive = age >= 18 && hasLicense && hasInsurance;

console.log(canDrive); // true
```

### Boolean state flags

```javascript
let isLoading = false;
let hasError = false;
let isComplete = false;

function startLoading() {
  isLoading = true;
  hasError = false;
  isComplete = false;
}
```

### Checking for a real boolean

Use `typeof` when you need to confirm a value is actually a boolean:

```javascript
const value = true;

if (typeof value === "boolean") {
  console.log("This is a boolean");
}
```

## Best practices

- **Name booleans like yes/no questions**: Use names like `isActive`, `hasPermission`, `canEdit`, and `shouldRetry`.
- **Use strict equality**: Prefer `===` and `!==` over `==` and `!=`.
- **Be explicit when values matter**: Use `count > 0`, `items.length > 0`, or `value === null` when truthiness is too broad.
- **Prefer `Boolean(value)` for conversion**: It is clearer than `!!value` for beginners.
- **Use `??` for nullish defaults**: It preserves valid falsy values like `0` and `""`.
- **Keep conditions readable**: Move complex logic into a well-named variable or function.

## Summary

Booleans represent `true` and `false` decisions. Comparisons produce booleans, logical operators combine them, and conditionals use them to choose what code runs. JavaScript also has truthy and falsy values, so be explicit when `0`, `""`, `null`, `undefined`, empty arrays, or strings like `"false"` matter. Clear boolean names and strict equality make conditional logic much easier to trust.
