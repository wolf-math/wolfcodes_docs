---
title: Rest and Spread
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

## What are rest and spread?

**Rest** and **spread** both use the `...` syntax, but they do opposite jobs.

Rest gathers multiple values into one array or object.

Spread expands one array or object into multiple values or properties.

```javascript
const numbers = [1, 2, 3];

console.log(Math.max(...numbers)); // 3
```

Here, spread expands the `numbers` array into separate arguments.

## Why this matters

The `...` syntax appears in several common JavaScript patterns:

- passing arrays into functions
- writing functions that accept flexible arguments
- copying arrays
- combining arrays
- copying objects
- merging objects
- collecting the remaining values during destructuring

The syntax is small, but the meaning depends on where it appears.

## The mental model

Use this rule of thumb:

- **Rest gathers** values together.
- **Spread expands** values outward.

```javascript
function addAll(...numbers) {
  return numbers.reduce((total, number) => total + number, 0);
}

console.log(addAll(1, 2, 3)); // 6
```

`...numbers` gathers arguments into an array.

```javascript
const numbers = [1, 2, 3];

console.log(addAll(...numbers)); // 6
```

`...numbers` spreads the array back out into separate arguments.

The same syntax is doing different work because it appears in a different place.

## Rest parameters

Use a rest parameter when a function should accept any number of arguments.

```javascript
function addAll(...numbers) {
  let total = 0;

  for (const number of numbers) {
    total += number;
  }

  return total;
}

console.log(addAll(1, 2, 3));    // 6
console.log(addAll(5, 10, 15));  // 30
```

The rest parameter gathers all remaining arguments into the `numbers` array.

Rest parameters must come last:

```javascript
function buildName(firstName, ...middleNames) {
  return `${firstName} ${middleNames.join(" ")}`;
}

console.log(buildName("Alice", "Marie", "Lee")); // "Alice Marie Lee"
```

This works because `...middleNames` gathers everything after `firstName`.

## Spreading into function calls

Use spread when you have an array but a function expects separate arguments.

```javascript
const numbers = [5, 10, 2, 8];

console.log(Math.max(...numbers)); // 10
console.log(Math.min(...numbers)); // 2
```

Without spread, `Math.max(numbers)` would pass the whole array as one argument.

Spread is also useful when calling your own functions:

```javascript
function greet(firstName, lastName) {
  return `Hello, ${firstName} ${lastName}!`;
}

const nameParts = ["Alice", "Smith"];

console.log(greet(...nameParts)); // "Hello, Alice Smith!"
```

## Spreading arrays

Use spread to copy an array.

```javascript
const original = [1, 2, 3];
const copy = [...original];

console.log(copy); // [1, 2, 3]
```

Use spread to combine arrays.

```javascript
const first = [1, 2];
const second = [3, 4];

const combined = [...first, ...second];

console.log(combined); // [1, 2, 3, 4]
```

Use spread to add values while copying.

```javascript
const items = ["a", "b"];
const updated = ["start", ...items, "end"];

console.log(updated); // ["start", "a", "b", "end"]
```

## Array spread is shallow

Array spread creates a shallow copy.

The array itself is new, but nested objects and arrays are still shared.

```javascript
const original = [{ name: "Alice" }];
const copy = [...original];

copy[0].name = "Bob";

console.log(original[0].name); // "Bob"
```

The array was copied, but the object inside it was not.

## Spreading objects

Use object spread to copy an object.

```javascript
const user = {
  name: "Alice",
  role: "admin"
};

const copy = { ...user };

console.log(copy); // { name: "Alice", role: "admin" }
```

Use object spread to merge objects.

```javascript
const defaults = {
  theme: "light",
  language: "en"
};

const userPrefs = {
  theme: "dark"
};

const settings = {
  ...defaults,
  ...userPrefs
};

console.log(settings); // { theme: "dark", language: "en" }
```

When two objects have the same property, the later spread wins.

In this example, `userPrefs.theme` replaces `defaults.theme`.

## Updating objects with spread

Object spread is useful when you want a new object with one changed property.

```javascript
const user = {
  name: "Alice",
  role: "member"
};

const adminUser = {
  ...user,
  role: "admin"
};

console.log(adminUser); // { name: "Alice", role: "admin" }
console.log(user);      // { name: "Alice", role: "member" }
```

The original object is unchanged.

## Object spread is shallow

Object spread also creates a shallow copy.

```javascript
const user = {
  name: "Alice",
  address: {
    city: "Cleveland"
  }
};

const copy = { ...user };

copy.address.city = "Boston";

console.log(user.address.city); // "Boston"
```

The top-level object was copied, but the nested `address` object was still shared.

## Rest in array destructuring

Use rest in array destructuring to collect the remaining items.

```javascript
const scores = [95, 88, 72, 64];

const [highest, secondHighest, ...otherScores] = scores;

console.log(highest);       // 95
console.log(secondHighest); // 88
console.log(otherScores);   // [72, 64]
```

Here, `...otherScores` gathers the remaining array items.

## Rest in object destructuring

Use rest in object destructuring to collect the remaining properties.

```javascript
const user = {
  id: 1,
  name: "Alice",
  role: "admin",
  active: true
};

const { id, ...details } = user;

console.log(id);      // 1
console.log(details); // { name: "Alice", role: "admin", active: true }
```

Here, `...details` gathers the properties that were not already pulled out.

## Common mistake: rest vs spread

The same `...` syntax can mean rest or spread.

Ask what direction the values are moving.

```javascript
function printNames(...names) {
  console.log(names);
}

const users = ["Alice", "Bob"];

printNames(...users);
```

**What happens:**

1. `...users` spreads the array into separate arguments.
2. `...names` gathers those arguments back into an array.
3. The function prints `["Alice", "Bob"]`.

## Common patterns

### Copying before sorting

Use spread before a mutating method when the original array should stay unchanged.

```javascript
const numbers = [10, 5, 40, 25];
const sorted = [...numbers].sort((a, b) => a - b);

console.log(numbers); // [10, 5, 40, 25]
console.log(sorted);  // [5, 10, 25, 40]
```

### Adding an item without changing the original array

```javascript
const items = ["a", "b"];
const updatedItems = [...items, "c"];

console.log(items);        // ["a", "b"]
console.log(updatedItems); // ["a", "b", "c"]
```

### Updating one object property

```javascript
const settings = {
  theme: "light",
  language: "en"
};

const updatedSettings = {
  ...settings,
  theme: "dark"
};

console.log(updatedSettings); // { theme: "dark", language: "en" }
```

## Best practices

- **Remember the direction**: rest gathers, spread expands.
- **Use rest parameters for flexible argument lists**.
- **Use spread for shallow copies of arrays and objects**.
- **Remember that spread is shallow**: nested objects and arrays are still shared.
- **Put object spreads in the right order**: later properties override earlier ones.
- **Prefer spread for simple copying and merging** when it keeps the code readable.

## Summary

Rest and spread both use `...`, but they do opposite jobs. Rest gathers values into an array or object. Spread expands arrays and objects into arguments, items, or properties.

Use rest parameters for flexible function arguments, array spread for copying and combining arrays, object spread for copying and merging objects, and destructuring rest when you need the remaining values.
