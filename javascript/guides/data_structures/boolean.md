---
title: Booleans
description: How JavaScript booleans work, including literals, logical and comparison operators, truthiness, and common patterns.
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

In JavaScript, **booleans** are a primitive type that can only be only `true` or `false`. You use booleans to check conditions in your code, like whether a user is logged in or whether a number is bigger than another. They are one of the main building blocks for `if` statements and other decisions.

Key characteristics:

- Only two literal values: `true` and `false` 
- Used with logical operators (`&&`, `||`, `!`) and comparison operators (`===`, `<`, `>`, etc.)
- Non-boolean values can be "truthy" or "falsy" in boolean contexts

Minimal example:

```javascript
const isActive = true;
const isComplete = false;
const hasPermission = true;
```

## Why this matters

Booleans are how you encode yes/no decisions in code. Every conditional, guard clause, feature flag, and validation check ultimately depends on a boolean (or a value coerced to one). Without a clear mental model of booleans—and of truthiness—you can introduce subtle bugs: empty arrays and the string `"false"` are truthy, while `0` and `""` are falsy.

Using booleans well lets you write readable conditionals, safe default values (e.g. with `||` or nullish coalescing), and predictable short-circuit behavior. Sticking to strict equality (`===` and `!==`) and naming flags clearly (e.g. `isActive`, `hasPermission`) keeps logic easy to reason about and debug.

## Basic syntax

Booleans are written as the literals `true` and `false`. Logical and comparison operators produce or consume booleans:

```javascript
const truthy = true;
const falsy = false;

true && true;   // true
true || false;  // true
!true;          // false

const a = 5;
const b = 10;
a < b;   // true
a === b; // false
```

### Simple example

A minimal conditional and a boolean variable:

```javascript
const isLoggedIn = true;

if (isLoggedIn) {
  console.log("Welcome back");
}
```

### Example with return value

Logical operators return a boolean (or the last evaluated value under short-circuit rules). Comparisons always return a boolean:

```javascript
const hasPermission = true;
const isLoggedIn = true;
const canAccess = hasPermission && isLoggedIn; // true

const age = 25;
const isAdult = age >= 18;  // true
```

## Using or invoking the concept

You use booleans in conditionals, loops, and expressions. They appear as the condition in `if`/`else`, `while`, and ternary operators, and as the result of comparisons and logical operations.

Basic usage in conditionals:

```javascript
const isActive = true;

if (isActive) {
  console.log("User is active");
}

const name = "Alice";
if (name) {
  console.log(`Hello, ${name}`);
}
```

Using logical operators to combine conditions:

```javascript
const hasPermission = true;
const isLoggedIn = true;
const canAccess = hasPermission && isLoggedIn; // true

const hasEmail = false;
const hasPhone = true;
const hasContact = hasEmail || hasPhone; // true
const hasContact = hasEmail && hasPhone; // false
```

Using comparison operators (they return booleans):

```javascript
const a = 5;
const b = 10;

a === b;  // false (strict equality)
a !== b;  // true (strict inequality)
a < b;    // true
a <= b;   // true
a >= b;   // false
```

## Parameters, inputs, or variations

### Literals and type

Booleans have only two literal values. In JavaScript they are lowercase:

```javascript
const truthy = true;
const falsy = false;
```

### Logical operators

**AND (`&&`)** — Returns `true` only if both operands are truthy. Short-circuits on the first falsy value.

```javascript
true && true;   // true
true && false;  // false
false && true;  // false
false && false; // false

const canAccess = hasPermission && isLoggedIn;
```

**OR (`||`)** — Returns `true` if at least one operand is truthy. Short-circuits on the first truthy value.

```javascript
true || true;   // true
true || false;  // true
false || true;  // true
false || false; // false

const hasContact = hasEmail || hasPhone;
```

**NOT (`!`)** — Reverses the boolean value.

```javascript
!true;   // false
!false;  // true
const isInactive = !isActive;
```

### Comparison operators

Comparisons produce boolean values. Prefer strict equality to avoid coercion:

```javascript
const a = 5;
const b = "5";

a === b;  // false (strict equality - type and value)
a !== b;  // true (strict inequality)
a == b;   // true (loose equality - coerces types; avoid)
a != b;   // false (loose inequality; avoid)
```

### Converting to boolean

You can convert any value to a boolean explicitly:

```javascript
Boolean(1);        // true
Boolean(0);        // false
Boolean("hello");  // true
Boolean("");       // false
Boolean([]);       // true (empty array is truthy)
Boolean(null);     // false
Boolean(undefined);// false

!!"hello";  // true (double negation pattern)
!!"";       // false
```

## Default behavior (if applicable)

### Truthiness and falsiness

In boolean contexts (e.g. `if (value)`), JavaScript coerces values to booleans. Only a short list of values are **falsy**; everything else is **truthy**.

### Falsy values

These values behave as `false` in conditionals and logical expressions:

```javascript
false;      // boolean
0;          // number
-0;         // number
0n;         // BigInt
"";         // empty string
null;
undefined;
NaN;
```

### Truthy values

Everything not in the falsy list is truthy. Some surprises:

```javascript
true;
1;              // any non-zero number
"hello";        // any non-empty string
"0";            // string "0" is truthy
"false";       // string "false" is truthy
[];             // empty array is truthy
{};             // empty object is truthy
```

### Important: subtle or surprising behavior

- **Empty arrays and objects are truthy.** To check for "has items" use `arr.length > 0` or `arr.length`, not `if (arr)` alone.
- **`Boolean("false")` is `true`** because any non-empty string is truthy. To turn the string `"true"`/`"false"` into a boolean, compare explicitly: `str === "true"`.
- **Loose equality (`==`)** coerces types and can make `0`, `""`, and `false` compare equal in some cases. Prefer `===` and `!==`.

Correct: explicit check for string content:

```javascript
const str = "false";
const flag = str === "true";  // false
```

Avoid: relying on `Boolean(str)` for the string `"false"`:

```javascript
Boolean("false");  // true (string is non-empty)
```

## Rules and constraints

1. Boolean literals are exactly `true` and `false` (lowercase); there are no other primitive boolean values.
2. Logical operators use short-circuit evaluation: `&&` stops at the first falsy operand; `||` stops at the first truthy operand.
3. Comparison operators return a boolean. Use `===` and `!==` for equality to avoid type coercion.
4. In boolean contexts, only the falsy list (above) is treated as `false`; all other values are treated as `true`.

Correct: strict equality and clear intent:

```javascript
if (value === true) { /* ... */ }
if (count > 0) { /* ... */ }
```

Incorrect: loose equality can hide bugs:

```javascript
// if (value == 1) { /* 1 and "1" both match */ }
```

## Documentation or introspection (if applicable)

You can inspect and convert booleans as follows:

- **`typeof value === "boolean"`** — Confirms a value is a boolean.
- **`bool.toString()`** — Returns `"true"` or `"false"`.
- **`String(bool)`** — Same as `toString()` for booleans.

Examples:

```javascript
const value = true;

typeof value === "boolean";  // true
value.toString();            // "true"
String(value);               // "true"
```

Parsing the string `"true"`/`"false"` back to boolean is not built in; compare explicitly:

```javascript
const str = "true";
str === "true";   // true (use this to derive a boolean)
Boolean("true");  // true (but Boolean("false") is also true)
```

## Common patterns

### Conditional Checks

Use booleans or truthy values directly in conditionals:

```javascript
const isActive = true;

if (isActive) {
  console.log("User is active");
}

const name = "Alice";
if (name) {
  console.log(`Hello, ${name}`);
}
```

### Default values with `OR`

Use `||` to supply a default when a value is falsy (or use `??` when you only want to default on `null`/`undefined`):

```javascript
// Falsy-aware defaults (0, "", null, undefined, etc.)
const username = user.name || "Guest";
const port = config.port || 3000;
const theme = settings.theme || "light";

// Nullish-coalescing defaults (only null/undefined trigger the default)
const retryCount = config.retryCount ?? 3; // 0 keeps its value
const apiBaseUrl = settings.apiBaseUrl ?? "https://api.example.com";
```

### Short-circuit evaluation

Logical operators skip evaluating the right-hand side when the outcome is already determined:

```javascript
// && stops at first falsy value
const result = false && expensiveFunction(); // expensiveFunction() never runs

// || stops at first truthy value
const value = "default" || getValue(); // getValue() not called if "default" is truthy
```

### Toggle boolean

Flip a flag with the NOT operator:

```javascript
let isActive = true;
isActive = !isActive; // false
isActive = !isActive; // true
```

### Multiple conditions

Combine conditions with `&&` (all must be true) or `||` (at least one):

```javascript
const age = 25;
const hasLicense = true;
const hasInsurance = true;

if (age >= 18 && hasLicense && hasInsurance) {
  console.log("Can drive");
}

if (age < 18 || !hasLicense || !hasInsurance) {
  console.log("Cannot drive");
}
```

### Checking existence (not `null`/`undefined`)

To test that a value is neither `null` nor `undefined`:

```javascript
const value = getValue();

if (value != null) {
  console.log(value); // excludes both null and undefined
}

// Or with optional chaining
const result = value?.property;
```

### Boolean flags in state

Use boolean variables to track loading, error, and completion state:

```javascript
let isLoading = false;
let hasError = false;
let isComplete = false;

function startProcess() {
  isLoading = true;
  hasError = false;
  isComplete = false;

  // ... do work ...

  isLoading = false;
  isComplete = true;
}
```

### Optional chaining with boolean context

Use optional chaining when reading nested properties in conditions:

```javascript
const user = {
  profile: {
    settings: {
      theme: "dark"
    }
  }
};

if (user?.profile?.settings?.theme) {
  console.log(user.profile.settings.theme);
}
```

## Best practices

- **Use strict equality** (`===` and `!==`) instead of `==` and `!=` to avoid unexpected type coercion.
- **Name booleans for yes/no questions**: e.g. `isActive`, `hasPermission`, `canEdit`, `shouldRetry`.
- **Be explicit when it helps**: use `Boolean(value)` or `value === true` when clarity matters more than brevity.
- **Remember truthiness**: empty arrays and objects are truthy; use `arr.length` or explicit checks when you care about "has items."
- **Prefer `??` for defaulting** when you only want to replace `null` or `undefined`, not other falsy values like `0` or `""`.
- **Avoid double negation** (`!!`) unless it’s a well-understood convention in your codebase; `Boolean(x)` is clearer for conversion.
- **Keep conditions simple**: extract complex logic into a well-named variable or function that returns a boolean.

## Summary

Booleans in JavaScript are the primitive type for logical truth: `true` and `false`. They drive conditionals, combine with logical operators (`&&`, `||`, `!`), and are produced by comparison operators. Non-boolean values are coerced to booleans in conditionals and logical expressions using the truthy/falsy rules, with a small, fixed set of falsy values. Using strict equality, clear naming, and an understanding of truthiness keeps your conditional logic predictable and maintainable.
