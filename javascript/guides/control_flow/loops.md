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

**Loops** let you repeat code multiple times. They're essential for processing collections of data, repeating actions, and automating repetitive tasks.

## `for` Loop

The `for` loop is the most common loop in JavaScript:

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
// Output: 0, 1, 2, 3, 4
```

The `for` loop has three parts:
1. **Initialization** (`let i = 0`) — runs once at the start
2. **Condition** (`i < 5`) — checked before each iteration
3. **Update** (`i++`) — runs after each iteration

This is equivalent to:
- Start with `i = 0`
- While `i < 5`, run the code and then increment `i`

## `while` Loop

A `while` loop repeats as long as a condition is true:

```javascript
let count = 0;

while (count < 5) {
  console.log(count);
  count++;
}
// Output: 0, 1, 2, 3, 4
```

**Warning:** Make sure the condition eventually becomes false, or you'll create an infinite loop!

### `do...while` loop

A `do...while` loop is similar to `while`, but it always executes at least once:

```javascript
let count = 0;

do {
  console.log(count);
  count++;
} while (count < 5);
// Output: 0, 1, 2, 3, 4
```

The difference is that `do...while` checks the condition after executing the code, while `while` checks before.

## `for...of` Loop

The `for...of` loop iterates over iterable values (arrays, strings, etc.):

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (const name of names) {
  console.log(name);
}
// Output: Alice, Bob, Charlie
```

**Prefer `for...of`** over traditional `for` loops when iterating over arrays—it's cleaner and less error-prone.

### Iterating over strings

```javascript
const text = "Hello";

for (const char of text) {
  console.log(char);
}
// Output: H, e, l, l, o
```

## `for...in` Loop

The `for...in` loop iterates over object properties (use `Object.keys()` instead for arrays):

```javascript
const person = {
  name: "Alice",
  age: 30,
  city: "NYC"
};

for (const key in person) {
  console.log(key, person[key]);
}
// Output:
// name Alice
// age 30
// city NYC
```

:::note
`for...in` can iterate over inherited properties. For objects, prefer `Object.keys()`, `Object.values()`, or `Object.entries()` as shown in the [objects guide](../data_structures/objects#looping-over-objects).
:::

## `break` And `continue`

### `break` — exit loop early

`break` exits the loop immediately:

```javascript
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;  // Exit loop when i is 5
  }
  console.log(i);
}
// Output: 0, 1, 2, 3, 4
```

### `continue` — skip to next iteration

`continue` skips the rest of the current iteration and moves to the next:

```javascript
for (let i = 0; i < 5; i++) {
  if (i === 2) {
    continue;  // Skip when i is 2
  }
  console.log(i);
}
// Output: 0, 1, 3, 4
```

## Common patterns

### Looping through arrays

```javascript
const numbers = [1, 2, 3, 4, 5];

// Using for...of (preferred)
for (const num of numbers) {
  console.log(num);
}

// Using traditional for loop
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}

// Using array methods (often preferred for transformations)
numbers.forEach(num => console.log(num));
```

### Finding elements with loops

```javascript
const names = ["Alice", "Bob", "Charlie"];
let found = null;

for (const name of names) {
  if (name.length > 4) {
    found = name;
    break;  // Found it, exit early
  }
}

console.log(found);  // "Alice"
```

### Nested loops

You can nest loops inside other loops:

```javascript
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    console.log(i, j);
  }
}
// Output:
// 0 0, 0 1, 0 2
// 1 0, 1 1, 1 2
// 2 0, 2 1, 2 2
```

Be careful with nested loops—they can be slow for large datasets.

### Conditional loops

Combine loops with conditionals:

```javascript
const numbers = [1, 2, 3, 4, 5];

for (const num of numbers) {
  if (num % 2 === 0) {
    console.log(`${num} is even`);
  } else {
    console.log(`${num} is odd`);
  }
}
```

### Accumulating values

```javascript
const numbers = [1, 2, 3, 4, 5];
let sum = 0;

for (const num of numbers) {
  sum += num;
}

console.log(sum);  // 15
```

### Looping with index

If you need the index when using `for...of`, use `entries()`:

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (const [index, name] of names.entries()) {
  console.log(index, name);
}
// Output:
// 0 Alice
// 1 Bob
// 2 Charlie
```

## Choosing the right loop

- **Use `for`** when you know how many times to loop or need the index
- **Use `while`** when you don't know how many times to loop
- **Use `for...of`** for iterating over arrays or other iterables (preferred)
- **Use `for...in`** for iterating over object properties (but prefer `Object.keys()`)
- **Use array methods** (`forEach`, `map`, `filter`) when transforming arrays
- **Use `break`** to exit a loop early when you find what you're looking for
- **Use `continue`** to skip the current iteration and move to the next
