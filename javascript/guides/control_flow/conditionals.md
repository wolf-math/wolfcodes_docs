---
title: Conditionals
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

## What are conditionals?

**Conditionals** let your program make decisions. They run different code depending on whether a condition is truthy or falsy.

```javascript
const age = 20;

if (age >= 18) {
  console.log("You are an adult");
}
```

The condition is `age >= 18`. Since that expression is `true`, JavaScript runs the code inside the braces.

## Why this matters

Without conditionals, a program would run the same way every time. Conditionals let you respond to user input, validate data, handle errors, show different messages, and choose different behavior based on the current state of your program.

## `if` statements

Use `if` to run code only when a condition is truthy:

```javascript
const isLoggedIn = true;

if (isLoggedIn) {
  console.log("Welcome back");
}
```

If the condition is falsy, JavaScript skips the block:

```javascript
const isLoggedIn = false;

if (isLoggedIn) {
  console.log("Welcome back");
}

console.log("This always runs");
```

## `if` / `else`

Use `else` when you need a fallback:

```javascript
const age = 15;

if (age >= 18) {
  console.log("You are an adult");
} else {
  console.log("You are a minor");
}
```

**Output:**

```text
You are a minor
```

Only one of the two blocks runs.

## `if` / `else if` / `else`

Use `else if` when you need to check multiple conditions in order:

```javascript
const score = 85;

if (score >= 90) {
  console.log("Grade: A");
} else if (score >= 80) {
  console.log("Grade: B");
} else if (score >= 70) {
  console.log("Grade: C");
} else {
  console.log("Grade: F");
}
```

**Output:**

```text
Grade: B
```

**How it works:**

1. JavaScript checks `score >= 90`.
2. If that is false, it checks `score >= 80`.
3. Once it finds a truthy condition, it runs that block and skips the rest.

Only the first matching block runs.

### Order matters

Put more specific checks before broader checks.

```javascript
const score = 95;

if (score >= 70) {
  console.log("Passing");
} else if (score >= 90) {
  console.log("Excellent");
}
```

This prints `"Passing"` because JavaScript stops at the first matching block.

```javascript
const score = 95;

if (score >= 90) {
  console.log("Excellent");
} else if (score >= 70) {
  console.log("Passing");
}
```

Check the narrow condition first when both conditions could be true.

## Truthy and falsy conditions

Conditions do not have to be actual booleans. JavaScript uses truthy and falsy rules, covered in the [data types guide](../data_structures/data_types#truthy-and-falsy-values).

```javascript
const name = "Alice";

if (name) {
  console.log("Name exists");
}
```

Empty strings, `0`, `null`, `undefined`, `false`, and `NaN` are falsy:

```javascript
const count = 0;

if (count) {
  console.log("Has items");
}
```

That block does not run because `0` is falsy.

Be explicit when a specific value matters:

```javascript
const count = 0;

if (count > 0) {
  console.log("Has items");
}
```

## Comparisons in conditions

Comparison operators create boolean values that conditionals can use:

```javascript
const password = "secret";

if (password.length >= 8) {
  console.log("Password is long enough");
} else {
  console.log("Password is too short");
}
```

Use strict equality when comparing exact values:

```javascript
const role = "admin";

if (role === "admin") {
  console.log("Show admin tools");
}
```

Avoid loose equality in beginner code because it can coerce types:

```javascript
console.log(0 == false);  // true
console.log(0 === false); // false
```

## Combining conditions

Use `&&` when all conditions must be truthy:

```javascript
const age = 25;
const hasLicense = true;

if (age >= 18 && hasLicense) {
  console.log("Can drive");
}
```

Use `||` when at least one condition must be truthy:

```javascript
const isWeekend = true;
const isHoliday = false;

if (isWeekend || isHoliday) {
  console.log("No school today");
}
```

Use `!` to invert truthiness:

```javascript
const isLoading = false;

if (!isLoading) {
  console.log("Ready");
}
```

When a combined condition gets hard to read, move part of it into a named variable:

```javascript
const age = 25;
const hasLicense = true;
const hasInsurance = true;

const isAllowedToDrive = age >= 18 && hasLicense && hasInsurance;

if (isAllowedToDrive) {
  console.log("Can drive");
}
```

## `switch`

Use `switch` when you are checking one value against several cases:

```javascript
const day = "Monday";

switch (day) {
  case "Monday":
    console.log("Start of the week");
    break;
  case "Friday":
    console.log("Almost weekend");
    break;
  case "Saturday":
  case "Sunday":
    console.log("Weekend");
    break;
  default:
    console.log("Regular day");
}
```

The `default` case runs when no case matches.

`switch` uses strict comparison, similar to `===`, when matching cases:

```javascript
const value = "1";

switch (value) {
  case 1:
    console.log("number");
    break;
  case "1":
    console.log("string");
    break;
}
```

This prints `"string"` because `"1"` and `1` are different values.

### `break` in `switch`

Use `break` to stop the `switch` after a matching case:

```javascript
const day = "Monday";

switch (day) {
  case "Monday":
    console.log("Monday");
    break;
  case "Tuesday":
    console.log("Tuesday");
    break;
}
```

Without `break`, JavaScript falls through to the next case:

```javascript
const day = "Monday";

switch (day) {
  case "Monday":
    console.log("Monday");
    // Missing break!
  case "Tuesday":
    console.log("Tuesday");
    break;
}
```

**Output:**

```text
Monday
Tuesday
```

Only leave out `break` when fall-through is intentional.

## Conditional expressions

The ternary operator is a compact way to choose between two values:

```javascript
const age = 20;
const status = age >= 18 ? "adult" : "minor";

console.log(status); // "adult"
```

This is equivalent to:

```javascript
const age = 20;
let status;

if (age >= 18) {
  status = "adult";
} else {
  status = "minor";
}
```

Use ternaries for simple value selection. Use `if` / `else` when the logic takes more than one line or needs side effects.

## Common patterns

### Early returns

In functions, use early returns to handle invalid or edge cases first:

```javascript
function getUserEmail(user) {
  if (!user) {
    return null;
  }

  if (!user.email) {
    return null;
  }

  return user.email;
}
```

This keeps the main path less nested.

### Guarding before using a value

```javascript
function printName(user) {
  if (!user) {
    console.log("No user provided");
    return;
  }

  console.log(user.name);
}
```

Check that a value exists before reading properties from it.

### Flattening nested conditionals

Nested conditionals work, but they can get hard to read:

```javascript
const age = 25;
const hasLicense = true;

if (age >= 18) {
  if (hasLicense) {
    console.log("Can drive");
  }
}
```

Combine conditions when the logic is simple:

```javascript
if (age >= 18 && hasLicense) {
  console.log("Can drive");
}
```

## Choosing the right conditional

- **Use `if`** for one decision.
- **Use `if` / `else`** when there are two paths.
- **Use `else if`** when checking multiple conditions in order.
- **Use `switch`** when one value has many possible cases.
- **Use a ternary** for simple value selection.
- **Use early returns** inside functions to handle edge cases first.

## Best practices

- **Keep conditions readable**: Move complex logic into a well-named variable.
- **Check specific cases first**: In an `else if` chain, the first matching block wins.
- **Be explicit when values matter**: Use `count > 0` instead of `if (count)` when zero has meaning.
- **Use strict equality**: Prefer `===` and `!==`.
- **Avoid deep nesting**: Combine simple conditions or return early.
- **Include `break` in `switch`** unless fall-through is intentional.
- **Use ternaries sparingly**: They are best for short value choices, not multi-step logic.

## Summary

Conditionals let JavaScript choose which code to run. Use `if`, `else`, and `else if` for most decisions, `switch` for multiple cases based on one value, and ternaries for small value choices. Remember that JavaScript uses truthy and falsy values in conditions, so be explicit when values like `0`, `""`, `null`, and `undefined` mean different things.
