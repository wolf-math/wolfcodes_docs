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

## Traditional `for` loops

Use a traditional `for` loop when you need an index or a specific number of repetitions:

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

**Output:**

```text
0
1
2
3
4
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
```

**Output:**

```text
0: Alice
1: Bob
2: Charlie
```

## `for...of`

Use `for...of` to loop over arrays, strings, and other iterable values:

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (const name of names) {
  console.log(name);
}
```

**Output:**

```text
Alice
Bob
Charlie
```

This is the clearest loop for most array iteration.

### Looping over strings

```javascript
const text = "Hi";

for (const character of text) {
  console.log(character);
}
```

**Output:**

```text
H
i
```

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
```

**Output:**

```text
name Alice
age 30
city New York
```

`for...in` can iterate over inherited properties. For objects, prefer `Object.keys()`, `Object.values()`, or `Object.entries()` as shown in the [objects guide](../data_structures/objects#looping-over-objects).

Do not use `for...in` for arrays. Use `for...of`, a traditional `for` loop, or array methods instead.

## `while` loops

Use `while` when you do not know ahead of time how many times the loop should run:

```javascript
let count = 0;

while (count < 3) {
  console.log(count);
  count++;
}
```

**Output:**

```text
0
1
2
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
```

**Output:**

```text
0
1
2
```

Use `do...while` only when the body should run before the first condition check.



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
```

**Output:**

```text
Alice
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
```

**Output:**

```text
0
1
3
4
```

The loop continues with the next value.

## Loops vs array methods

Loops and array methods both help you process collections.

Use a loop when you need general step-by-step control.

Use an array method when the operation has a clear data shape, such as transforming, filtering, finding, or combining values.

### Transforming values

Use `map()` when you want one new value for each original value:

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map((number) => number * 2);

console.log(doubled); // [2, 4, 6, 8]
```

The loop version works too, but it takes more code:

```javascript
const numbers = [1, 2, 3, 4];
const doubled = [];

for (const number of numbers) {
  doubled.push(number * 2);
}

console.log(doubled); // [2, 4, 6, 8]
```

When the goal is "make a new array by changing each item," `map()` usually says that more clearly.

### Filtering values

Use `filter()` when you want to keep only some items:

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evenNumbers = numbers.filter((number) => number % 2 === 0);

console.log(evenNumbers); // [2, 4, 6]
```

The loop version is useful when the filtering logic needs several steps:

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evenNumbers = [];

for (const number of numbers) {
  const isEven = number % 2 === 0;

  if (isEven) {
    evenNumbers.push(number);
  }
}

console.log(evenNumbers); // [2, 4, 6]
```

### Finding one value

Use `find()` when you want the first matching item:

```javascript
const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

const user = users.find((user) => user.id === 2);

console.log(user); // { id: 2, name: "Bob" }
```

Use a loop when you need custom side effects before stopping:

```javascript
const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

let foundUser = null;

for (const user of users) {
  console.log(`Checking ${user.name}`);

  if (user.id === 2) {
    foundUser = user;
    break;
  }
}

console.log(foundUser); // { id: 2, name: "Bob" }
```

### Combining values

Use `reduce()` when you want to combine an array into one value:

```javascript
const numbers = [1, 2, 3, 4];
const total = numbers.reduce((sum, number) => sum + number, 0);

console.log(total); // 10
```

Use a loop if `reduce()` makes the code harder to follow:

```javascript
const numbers = [1, 2, 3, 4];
let total = 0;

for (const number of numbers) {
  total += number;
}

console.log(total); // 10
```

**Rule of thumb:** Prefer the version that makes the purpose obvious. If the array method reads like the operation you want, use it. If the callback gets crowded or needs `break`, `continue`, `await`, or several side effects, use a loop.

Array methods are important enough to learn deeply, but they already fit naturally in the [arrays guide](../data_structures/arrays). This page focuses on when to choose them instead of a loop.

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
const found = names.find((name) => name.length > 4);

console.log(found); // "Alice"
```

### Looping with an index

Use `.entries()` with `for...of` when you want both index and value:

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (const [index, name] of names.entries()) {
  console.log(`${index}: ${name}`);
}
```

**Output:**

```text
0: Alice
1: Bob
2: Charlie
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
```

**Output:**

```text
A1
A2
A3
B1
B2
B3
```

Nested loops can get slow with large data sets, so use them carefully.

## Choosing the right loop

- **Use `for...of`** for arrays and other iterable values.
- **Use a traditional `for` loop** when you need an index or exact repetition count.
- **Use `while`** when the number of iterations depends on a changing condition.
- **Use `do...while`** when the loop body must run at least once.
- **Avoid `for...in` for arrays**. For objects, usually prefer `Object.keys()`, `Object.values()`, or `Object.entries()`.
- **Use array methods** when they make the data transformation clearer.
- **Use `forEach()` only for side effects** such as logging or updating the page. Use `map()` when you need a new array.

## Best practices

- **Prefer `for...of` for arrays** when you do not need the index.
- **Make loop conditions change** so loops eventually stop.
- **Use clear variable names** like `user`, `item`, `index`, or `total`.
- **Use `break` intentionally** when you have found what you need.
- **Keep nested loops small and readable**.
- **Choose array methods for transformations** such as mapping and filtering.
- **Choose loops for control flow** when you need `break`, `continue`, `await`, or several side effects.

## Summary

Loops repeat code. Use `for...of` for most array iteration, traditional `for` loops when you need an index, `while` loops when repetition depends on a condition, and array methods when transforming data. Always make sure loop conditions can end, and choose the loop form that makes the repeated work easiest to understand.
