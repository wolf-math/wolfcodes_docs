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

**Booleans** are a data type that represents one of two values: `true` or `false`. Booleans are used to express logical conditions and control program flow. They are one of the primitive data types in JavaScript.

```javascript
const isActive = true;
const isComplete = false;
const hasPermission = true;
```

## Boolean literals

Booleans have only two possible values:

```javascript
const truthy = true;
const falsy = false;
```

Unlike some languages, JavaScript booleans are lowercase (`true` and `false`), not capitalized.

## Boolean operations

### Logical operators

JavaScript provides logical operators to combine and manipulate boolean values:

#### AND (`&&`)

Returns `true` only if both operands are `true`:

```javascript
true && true;   // true
true && false;  // false
false && true;  // false
false && false; // false

const hasPermission = true;
const isLoggedIn = true;
const canAccess = hasPermission && isLoggedIn; // true
```

#### OR (`||`)

Returns `true` if at least one operand is `true`:

```javascript
true || true;   // true
true || false;  // true
false || true;  // true
false || false; // false

const hasEmail = false;
const hasPhone = true;
const hasContact = hasEmail || hasPhone; // true
```

#### NOT (`!`)

Reverses the boolean value:

```javascript
!true;   // false
!false;  // true

const isActive = true;
const isInactive = !isActive; // false
```

### Comparison operators

Comparison operators return boolean values:

```javascript
const a = 5;
const b = 10;

a === b;  // false (strict equality)
a !== b;  // true (strict inequality)
a < b;    // true (less than)
a > b;    // false (greater than)
a <= b;   // true (less than or equal)
a >= b;   // false (greater than or equal)
```

### Equality operators

```javascript
const a = 5;
const b = "5";

a === b;  // false (strict equality - checks type and value)
a == b;   // true (loose equality - coerces types, avoid using)
a !== b;  // true (strict inequality)
a != b;   // false (loose inequality, avoid using)
```

**Best practice:** Always use `===` and `!==` for comparisons to avoid unexpected type coercion.

## Truthiness and falsiness

In JavaScript, values can be "truthy" or "falsy" when used in boolean contexts. This means non-boolean values are automatically converted to booleans when needed.

### Falsy values

These values are considered `false` in boolean contexts:

```javascript
false;      // false (boolean)
0;          // false (number)
-0;         // false (number)
0n;         // false (BigInt)
"";         // false (empty string)
null;       // false
undefined;  // false
NaN;        // false
```

### Truthy values

Everything else is truthy:

```javascript
true;           // true
1;              // true (any non-zero number)
-1;             // true
"hello";        // true (any non-empty string)
"0";            // true (string "0" is truthy!)
"false";        // true (string "false" is truthy!)
[];             // true (empty array is truthy!)
{};             // true (empty object is truthy!)
[];             // true (arrays are truthy)
{};             // true (objects are truthy)
```

### Converting to boolean

You can explicitly convert values to booleans:

```javascript
Boolean(1);        // true
Boolean(0);        // false
Boolean("hello");  // true
Boolean("");       // false
Boolean([]);       // true
Boolean({});       // true
Boolean(null);     // false
Boolean(undefined); // false

// Double negation (common pattern)
!!1;        // true
!!0;        // false
!!"hello";  // true
!!"";       // false
```

## Common boolean patterns

### Conditional checks

```javascript
const isActive = true;

if (isActive) {
  console.log("User is active");
}

// Using truthiness
const name = "Alice";
if (name) {
  console.log(`Hello, ${name}`);
}
```

### Default values with OR

The `||` operator is often used to provide default values:

```javascript
const username = user.name || "Guest";
const port = config.port || 3000;
const theme = settings.theme || "light";
```

### Short-circuit evaluation

Logical operators use short-circuit evaluation:

```javascript
// && stops at first falsy value
const result = false && expensiveFunction(); // expensiveFunction() never runs

// || stops at first truthy value
const value = "default" || getValue(); // getValue() never runs if "default" is truthy
```

### Optional chaining with boolean checks

```javascript
const user = {
  profile: {
    settings: {
      theme: "dark"
    }
  }
};

// Check if nested property exists
if (user?.profile?.settings?.theme) {
  console.log(user.profile.settings.theme);
}
```

## Boolean methods

### Converting to string

```javascript
const bool = true;
bool.toString();  // "true"
String(bool);     // "true"
```

### Converting from string

```javascript
Boolean("true");   // true
Boolean("false");  // true (any non-empty string is truthy!)
Boolean("");       // false

// To parse string "true"/"false" to boolean
const str = "true";
str === "true";    // true (manual check)
```

## Common boolean patterns

### Toggle boolean

```javascript
let isActive = true;
isActive = !isActive; // false
isActive = !isActive; // true
```

### Multiple conditions

```javascript
const age = 25;
const hasLicense = true;
const hasInsurance = true;

// All conditions must be true
if (age >= 18 && hasLicense && hasInsurance) {
  console.log("Can drive");
}

// At least one condition must be true
if (age < 18 || !hasLicense || !hasInsurance) {
  console.log("Cannot drive");
}
```

### Checking existence

```javascript
const value = null;

// Check if value exists (not null/undefined)
if (value != null) {  // Checks both null and undefined
  console.log(value);
}

// More explicit
if (value !== null && value !== undefined) {
  console.log(value);
}

// Using optional chaining (modern approach)
const result = value?.property;
```

### Boolean in arrays

```javascript
const items = [1, 2, 3, 4, 5];

// Check if array has items
if (items.length > 0) {
  console.log("Array has items");
}

// Using truthiness (empty array is truthy, so check length)
if (items.length) {
  console.log("Array has items");
}
```

### Boolean flags

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

## Type checking

```javascript
const value = true;

typeof value === "boolean";  // true
typeof value === "boolean";  // true
```

## Best practices

1. **Use strict equality** (`===` and `!==`) instead of loose equality (`==` and `!=`)
2. **Be explicit** with boolean conversions when clarity is important
3. **Understand truthiness** - remember that empty arrays and objects are truthy
4. **Use meaningful names** for boolean variables (e.g., `isActive`, `hasPermission`, `canEdit`)
5. **Avoid double negation** unless necessary - `!!value` can be confusing
