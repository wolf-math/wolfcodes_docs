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

**Conditionals** let you make decisions in your code. They allow you to execute different code based on whether conditions are true or false. Without conditionals, programs would execute line by line without any decision-making.

## `if` / `else`

The `if` statement lets you execute code conditionally; only when a condition is true.

### Basic `if` statement

```javascript
const age = 20;

if (age >= 18) {
  console.log("You are an adult");
}
```

If the condition `age >= 18` is true, the code inside the braces runs. If false, it's skipped.

### `if` / `else`

Add an `else` clause to handle the false case:

```javascript
const age = 15;

if (age >= 18) {
  console.log("You are an adult");
} else {
  console.log("You are a minor");
}
// Output: "You are a minor"
```

### `if` / `else if` / `else`

Chain multiple conditions with `else if`:

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
// Output: "Grade: B"
```

JavaScript evaluates conditions from top to bottom and executes only the first matching block.

### Truthy and falsy in conditionals

Remember from the [data types guide](../data_structures/data_types#truthy-and-falsy-values) that JavaScript uses truthy/falsy values:

```javascript
const name = "Alice";

if (name) {  // "Alice" is truthy
  console.log("Name exists");
}

const count = 0;
if (count) {  // 0 is falsy, so this won't run
  console.log("Has items");
}

// Be explicit when checking for specific values
if (count > 0) {  // Better: explicit check
  console.log("Has items");
}
```

### Multiple conditions

Combine conditions with logical operators:

```javascript
const age = 25;
const hasLicense = true;

if (age >= 18 && hasLicense) {  // Both must be true
  console.log("Can drive");
}

if (age < 13 || age > 65) {  // Either can be true
  console.log("Eligible for discount");
}

if (!hasLicense) {  // NOT operator
  console.log("Cannot drive");
}
```

## `switch`

Use `switch` when you have multiple conditions based on the same value:

```javascript
const day = "Monday";

switch (day) {
  case "Monday":
    console.log("Start of the week");
    break;
  case "Friday":
    console.log("Almost weekend!");
    break;
  case "Saturday":
  case "Sunday":
    console.log("Weekend!");
    break;
  default:
    console.log("Regular day");
}
```

**Important:** Always include `break` statements (except when you want fall-through behavior). Without `break`, execution "falls through" to the next case:

```javascript
const day = "Monday";

switch (day) {
  case "Monday":
    console.log("Monday");  // This runs
    // Missing break!
  case "Tuesday":
    console.log("Tuesday");  // This also runs! (fall-through)
    break;
}
```

The `default` case handles values that don't match any `case`.

### `break` in `switch`

As mentioned above, `break` is used in `switch` statements to prevent fall-through:

```javascript
switch (value) {
  case 1:
    console.log("One");
    break;  // Exit switch
  case 2:
    console.log("Two");
    break;
}
```

## Common patterns

### Conditional assignment

```javascript
const age = 20;
const status = age >= 18 ? "adult" : "minor";
// Equivalent to:
// let status;
// if (age >= 18) {
//   status = "adult";
// } else {
//   status = "minor";
// }
```

### Early returns

In functions, use early returns to handle edge cases:

```javascript
function processUser(user) {
  if (!user) {
    return null;
  }
  
  if (!user.email) {
    return null;
  }
  
  // Process user...
  return processedUser;
}
```

### Nested conditionals

You can nest conditionals inside other conditionals:

```javascript
const age = 25;
const hasLicense = true;

if (age >= 18) {
  if (hasLicense) {
    console.log("Can drive");
  } else {
    console.log("Need a license");
  }
} else {
  console.log("Too young to drive");
}
```

## Choosing the right conditional

- **Use `if/else`** for simple conditionals based on different variables
- **Use `switch`** for conditionals based on a single value with multiple cases
- **Use ternary operator** (`? :`) for simple one-line conditionals
- **Use early returns** in functions to handle edge cases first
