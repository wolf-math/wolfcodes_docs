---
title: Loops
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are loops?

**Loops** let you repeat code. Use loops when you need to process a list, count through numbers, search for a value, or keep doing something while a condition is true.

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (const name of names) {
  console.log(name);
}
```

The loop runs once for each name in the array.

## Why this matters

Programs often need to do the same kind of work many times: display every item in a list, add up numbers, validate form fields, search results, or retry an action. Loops let you write that repeated behavior once instead of copying the same code over and over.

## `for...of`

Use `for...of` to loop over arrays, strings, and other iterable values:

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (const name of names) {
  console.log(name);
}
// Output:
// Alice
// Bob
// Charlie
```

This is the clearest loop for most array iteration.

### Looping over strings

```javascript
const text = "Hi";

for (const character of text) {
  console.log(character);
}
// Output:
// H
// i
```

## Traditional `for` loops

Use a traditional `for` loop when you need an index or a specific number of repetitions:

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
// Output:
// 0
// 1
// 2
// 3
// 4
```

A `for` loop has three parts:

1. **Initialization**: `let i = 0` runs once at the start.
2. **Condition**: `i < 5` is checked before each iteration.
3. **Update**: `i++` runs after each iteration.

Use the index when you need positions:

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (let i = 0; i < names.length; i++) {
  console.log(`${i}: ${names[i]}`);
}
// Output:
// 0: Alice
// 1: Bob
// 2: Charlie
```

## `while` loops

Use `while` when you do not know ahead of time how many times the loop should run:

```javascript
let count = 0;

while (count < 3) {
  console.log(count);
  count++;
}
// Output:
// 0
// 1
// 2
```

**Important:** Make sure the condition eventually becomes falsy. Otherwise, you create an infinite loop.

```javascript
// This would run forever:
// while (true) {
//   console.log("still running");
// }
```

## `do...while`

A `do...while` loop always runs at least once because it checks the condition after the loop body:

```javascript
let count = 0;

do {
  console.log(count);
  count++;
} while (count < 3);
// Output:
// 0
// 1
// 2
```

Use `do...while` only when the body should run before the first condition check.

## `for...in`

`for...in` loops over object property names:

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "New York"
};

for (const key in person) {
  console.log(key, person[key]);
}
// Output:
// name Alice
// age 30
// city New York
```

`for...in` can iterate over inherited properties. For objects, prefer `Object.keys()`, `Object.values()`, or `Object.entries()` as shown in the [objects guide](../data_structures/objects#looping-over-objects).

Do not use `for...in` for arrays. Use `for...of`, a traditional `for` loop, or array methods instead.

## `break` and `continue`

### `break`

Use `break` to exit a loop early:

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (const name of names) {
  if (name === "Bob") {
    break;
  }

  console.log(name);
}
// Output:
// Alice
```

Once JavaScript reaches `break`, the loop stops.

### `continue`

Use `continue` to skip the rest of the current iteration:

```javascript
for (let i = 0; i < 5; i++) {
  if (i === 2) {
    continue;
  }

  console.log(i);
}
// Output:
// 0
// 1
// 3
// 4
```

The loop continues with the next value.

## Loops vs array methods

Loops are great for general repetition. Array methods are often clearer when transforming or filtering arrays:

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(number => number * 2);

console.log(doubled); // [2, 4, 6, 8]
```

Use `map()`, `filter()`, `find()`, and `reduce()` when they clearly describe the operation. Use a loop when the logic has multiple steps or side effects.

## Common patterns

### Accumulating a total

```javascript
const numbers = [1, 2, 3, 4, 5];
let total = 0;

for (const number of numbers) {
  total += number;
}

console.log(total); // 15
```

### Finding an item

```javascript
const names = ["Alice", "Bob", "Charlie"];
let found = null;

for (const name of names) {
  if (name.length > 4) {
    found = name;
    break;
  }
}

console.log(found); // "Alice"
```

You can also use `find()` for this:

```javascript
const found = names.find(name => name.length > 4);

console.log(found); // "Alice"
```

### Looping with an index

Use `.entries()` with `for...of` when you want both index and value:

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (const [index, name] of names.entries()) {
  console.log(`${index}: ${name}`);
}
// Output:
// 0: Alice
// 1: Bob
// 2: Charlie
```

### Nested loops

Use nested loops when you need every combination of two sets of values:

```javascript
const rows = ["A", "B"];
const columns = [1, 2, 3];

for (const row of rows) {
  for (const column of columns) {
    console.log(`${row}${column}`);
  }
}
// Output:
// A1
// A2
// A3
// B1
// B2
// B3
```

Nested loops can get slow with large data sets, so use them carefully.

## Choosing the right loop

- **Use `for...of`** for arrays and other iterable values.
- **Use a traditional `for` loop** when you need an index or exact repetition count.
- **Use `while`** when the number of iterations depends on a changing condition.
- **Use `do...while`** when the loop body must run at least once.
- **Avoid `for...in` for arrays**. For objects, usually prefer `Object.keys()`, `Object.values()`, or `Object.entries()`.
- **Use array methods** when they make the data transformation clearer.

## Best practices

- **Prefer `for...of` for arrays** when you do not need the index.
- **Make loop conditions change** so loops eventually stop.
- **Use clear variable names** like `user`, `item`, `index`, or `total`.
- **Use `break` intentionally** when you have found what you need.
- **Keep nested loops small and readable**.
- **Choose array methods for transformations** such as mapping and filtering.

## Summary

Loops repeat code. Use `for...of` for most array iteration, traditional `for` loops when you need an index, `while` loops when repetition depends on a condition, and array methods when transforming data. Always make sure loop conditions can end, and choose the loop form that makes the repeated work easiest to understand.
