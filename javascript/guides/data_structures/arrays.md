---
title: Arrays
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are arrays?

**Arrays** are ordered collections of values. Use an array when you have a list of items and the order matters.

```javascript
const scores = [95, 87, 92];
const names = ["Alice", "Bob", "Charlie"];

console.log(names[0]); // "Alice"
console.log(scores.length); // 3
```

Arrays can contain any JavaScript value, including strings, numbers, booleans, objects, and other arrays. In most real code, keep the items similar so the array is easy to reason about.

## Why this matters

Arrays are one of the most common data structures in JavaScript. You'll use them for lists of users, search results, shopping cart items, form fields, scores, messages, and many other collections.

Arrays also come with useful methods like `map()`, `filter()`, `find()`, and `reduce()`. These methods let you process data clearly without writing every loop by hand.

## Creating arrays

### Array literals

The most common way to create an array is with square brackets:

```javascript
const empty = [];
const numbers = [1, 2, 3];
const names = ["Alice", "Bob"];
const rows = [[1, 2], [3, 4]];
```

Prefer this form in beginner code. It is short and clear.

### The `Array` constructor

JavaScript also has an `Array` constructor:

```javascript
const values = new Array(1, 2, 3); // [1, 2, 3]
```

Avoid `new Array()` unless you have a specific reason. It has surprising behavior when you pass one number:

```javascript
const items = new Array(3);

console.log(items); // [empty x 3]
console.log(items.length); // 3
```

`new Array(3)` creates an array with three empty slots, not `[3]`.

## Accessing elements

Arrays are **zero-indexed**. The first item is at index `0`, the second item is at index `1`, and so on.

```javascript
const names = ["Alice", "Bob", "Charlie"];

console.log(names[0]); // "Alice"
console.log(names[1]); // "Bob"
console.log(names[2]); // "Charlie"
console.log(names[3]); // undefined
```

If you access an index that does not exist, JavaScript returns `undefined`.

### Length

Use `.length` to get the number of items:

```javascript
const names = ["Alice", "Bob", "Charlie"];

console.log(names.length); // 3
```

### Last item

Use `.at(-1)` to get the last item:

```javascript
const names = ["Alice", "Bob", "Charlie"];

console.log(names.at(-1)); // "Charlie"
```

You may also see the older pattern:

```javascript
const last = names[names.length - 1];

console.log(last); // "Charlie"
```

## Mutating vs non-mutating methods

A key array mental model: some methods **mutate** the original array, while others return a new array.

### Mutating methods

Mutating methods change the original array:

```javascript
const numbers = [1, 2, 3];

numbers.push(4);

console.log(numbers); // [1, 2, 3, 4]
```

Common mutating methods include:

- `push()`
- `pop()`
- `shift()`
- `unshift()`
- `splice()`
- `sort()`
- `reverse()`

### Non-mutating methods

Non-mutating methods return a new value and leave the original array unchanged:

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map((number) => number * 2);

console.log(numbers); // [1, 2, 3]
console.log(doubled); // [2, 4, 6]
```

Common non-mutating methods include:

- `map()`
- `filter()`
- `slice()`
- `concat()`
- `find()`
- `includes()`

**Important:** If you want to keep the original array unchanged before using a mutating method, copy it first:

```javascript
const original = [1, 2, 3];
const reversed = [...original].reverse();

console.log(original); // [1, 2, 3]
console.log(reversed); // [3, 2, 1]
```

## Adding and removing items

Use `push()` and `pop()` at the end of an array:

```javascript
const items = ["a", "b"];

items.push("c");
console.log(items); // ["a", "b", "c"]

const last = items.pop();
console.log(last); // "c"
console.log(items); // ["a", "b"]
```

Use `unshift()` and `shift()` at the beginning:

```javascript
const items = ["b", "c"];

items.unshift("a");
console.log(items); // ["a", "b", "c"]

const first = items.shift();
console.log(first); // "a"
console.log(items); // ["b", "c"]
```

These methods mutate the original array.

## Finding items

Use `includes()` when you only need to know whether a value exists:

```javascript
const names = ["Alice", "Bob", "Charlie"];

console.log(names.includes("Bob")); // true
console.log(names.includes("Dana")); // false
```

Use `find()` when you need the first item that matches a condition:

```javascript
const users = [
  { id: 1, name: "Alice" },
  { id: 2, name: "Bob" }
];

const user = users.find((user) => user.id === 2);

console.log(user); // { id: 2, name: "Bob" }
```

Use `findIndex()` when you need the matching item's index:

```javascript
const names = ["Alice", "Bob", "Charlie"];
const index = names.findIndex((name) => name.startsWith("C"));

console.log(index); // 2
```

If no item matches, `find()` returns `undefined` and `findIndex()` returns `-1`:

```javascript
const names = ["Alice", "Bob", "Charlie"];

console.log(names.find((name) => name === "Dana")); // undefined
console.log(names.findIndex((name) => name === "Dana")); // -1
```

## Slicing and splicing

`slice()` copies part of an array without changing the original:

```javascript
const numbers = [1, 2, 3, 4, 5];
const middle = numbers.slice(1, 4);

console.log(middle); // [2, 3, 4]
console.log(numbers); // [1, 2, 3, 4, 5]
```

`splice()` changes the original array by removing or inserting items:

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.splice(2, 1, 99);

console.log(numbers); // [1, 2, 99, 4, 5]
```

**Rule of thumb:** Use `slice()` when you want a copy. Use `splice()` only when you intentionally want to mutate the array.

## Iterating over arrays

### `for...of`

Use `for...of` when you want to do something with each item:

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

Prefer `for...of` when you do not need the index.

### Traditional `for` loop

Use a traditional `for` loop when you need the index:

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

### `forEach()`

`forEach()` runs a function for each item:

```javascript
const names = ["Alice", "Bob", "Charlie"];

names.forEach((name, index) => {
  console.log(`${index}: ${name}`);
});
```

**Output:**

```text
0: Alice
1: Bob
2: Charlie
```

Use `forEach()` for simple side effects, like logging or updating the page. Use `map()` when you want to create a new array.

## Transforming arrays

### `map()`

`map()` creates a new array by transforming each item:

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map((number) => number * 2);

console.log(doubled); // [2, 4, 6, 8]
```

Use `map()` when the output array should have one new item for each original item.

### `filter()`

`filter()` creates a new array with only the items that pass a test:

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evens = numbers.filter((number) => number % 2 === 0);

console.log(evens); // [2, 4, 6]
```

Use `filter()` when you want to keep some items and remove others.

### `reduce()`

`reduce()` combines all items into one value:

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((total, number) => total + number, 0);

console.log(sum); // 10
```

Use `reduce()` for totals, grouped objects, and other "combine everything" operations. If `reduce()` makes the code hard to read, a loop is fine.

**Rule of thumb:** Include the starting value, like `0` in the example above. It keeps the behavior clear and avoids errors with empty arrays.

### Chaining methods

You can chain array methods to process data step by step:

```javascript
const numbers = [1, 2, 3, 4, 5, 6];

const result = numbers
  .filter((number) => number % 2 === 0)
  .map((number) => number * number)
  .reduce((total, number) => total + number, 0);

console.log(result); // 56
```

Keep chains short enough to read. If a chain gets confusing, split it into named intermediate variables.

## Common patterns

### Checking if an array is empty

Empty arrays are truthy, so check `.length`:

```javascript
const items = [];

if (items.length === 0) {
  console.log("Array is empty");
}
```

### Copying arrays

Use the spread operator for a shallow copy:

```javascript
const original = [1, 2, 3];
const copy = [...original];

console.log(copy); // [1, 2, 3]
```

This is a shallow copy. Nested objects and arrays are still shared.

```javascript
const original = [{ name: "Alice" }];
const copy = [...original];

copy[0].name = "Bob";

console.log(original[0].name); // "Bob"
```

The array was copied, but the object inside it was still shared.

Rest and spread syntax are covered in more detail in the [rest and spread guide](./rest_and_spread).

### Combining arrays

Use spread syntax or `concat()`:

```javascript
const first = [1, 2];
const second = [3, 4];

const combined = [...first, ...second];

console.log(combined); // [1, 2, 3, 4]
```

### Sorting numbers

`sort()` mutates the original array and sorts values as strings by default. For numbers, pass a compare function:

```javascript
const numbers = [10, 5, 40, 25];

numbers.sort();

console.log(numbers); // [10, 25, 40, 5]
```

That result happens because the default sort compares values as strings.

```javascript
const numbers = [10, 5, 40, 25];

numbers.sort((a, b) => a - b);

console.log(numbers); // [5, 10, 25, 40]
```

To avoid mutating the original:

```javascript
const numbers = [10, 5, 40, 25];
const sorted = [...numbers].sort((a, b) => a - b);

console.log(numbers); // [10, 5, 40, 25]
console.log(sorted);  // [5, 10, 25, 40]
```

### Checking whether a value is an array

Use `Array.isArray()` when you need to confirm that a value is an array:

```javascript
const items = ["a", "b"];
const user = { name: "Alice" };

console.log(Array.isArray(items)); // true
console.log(Array.isArray(user));  // false
```

Do not use `typeof` for this check. Arrays are objects, so `typeof []` returns `"object"`.

## Arrays vs objects

Use arrays when:

- Order matters
- You have a list of similar items
- You want to iterate over every item
- You want array methods like `map()`, `filter()`, and `reduce()`

Use objects when:

- You need to look up values by name
- The data has meaningful properties
- You are representing one structured thing, like a user or configuration

```javascript
const names = ["Alice", "Bob", "Charlie"];

const user = {
  name: "Alice",
  age: 30
};
```

## Best practices

- **Prefer array literals**: Use `[]` instead of `new Array()`.
- **Use `const` for arrays by default**: The array can still be mutated, but the variable cannot be reassigned.
- **Check `.length` for emptiness**: Empty arrays are truthy.
- **Know which methods mutate**: Be careful with `sort()`, `reverse()`, `splice()`, and push/pop methods.
- **Use `map()` for transformation**: Do not use it just for side effects.
- **Keep chains readable**: Split long chains into named steps.
- **Use `Array.isArray()` for array checks**: `typeof` cannot tell arrays and plain objects apart.
- **Use objects for named data**: If each value needs a label, an object may be clearer than an array.

## Summary

Arrays are ordered collections for lists of values. Use indexes to access items, `.length` to check size, and methods like `map()`, `filter()`, `find()`, and `reduce()` to process data. Remember the mutation rule: some methods change the original array, while others return a new value. When in doubt, choose the method that makes the data flow easiest to read.
