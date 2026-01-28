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

**Arrays** are ordered collections of values. In JavaScript, arrays can contain values of any type, and you can mix different types in the same array (though this is usually not recommended).

```javascript
const numbers = [1, 2, 3, 4, 5];
const names = ["Alice", "Bob", "Charlie"];
const mixed = [1, "hello", true, null]; // Mixed types (not recommended)
```

Arrays are one of JavaScript's most important data structures. They're used constantly in real programs.

## Creating arrays

### Array literals

The most common way to create an array is using square brackets `[]`:

```javascript
const empty = [];                    // Empty array
const numbers = [1, 2, 3];           // Array of numbers
const names = ["Alice", "Bob"];      // Array of strings
const nested = [[1, 2], [3, 4]];     // Array of arrays
```

### Array constructor

You can also use the `Array` constructor (less common):

```javascript
const arr1 = new Array();           // Empty array []
const arr2 = new Array(1, 2, 3);    // [1, 2, 3]
const arr3 = new Array(5);          // [empty × 5] (creates array with length 5, but empty slots)
```

**Prefer array literals** `[]` over the constructor. They're shorter and clearer.

## Accessing elements

Arrays are **zero-indexed**, meaning the first element is at index `0`:

```javascript
const names = ["Alice", "Bob", "Charlie"];

// Bracket notation
names[0];  // "Alice" (first element)
names[1];  // "Bob" (second element)
names[2];  // "Charlie" (third element)
names[3];  // undefined (doesn't exist)

// Using .at() method
names.at(0);  // "Alice" (first element)
names.at(1);  // "Bob" (second element)
names.at(-1); // "Charlie" (last element, negative index counts from end)
names.at(-2); // "Bob" (second from end)
names.at(3);  // undefined (doesn't exist)
```

### Getting the length

```javascript
const names = ["Alice", "Bob", "Charlie"];
names.length;  // 3
```

### Accessing the last element

```javascript
const names = ["Alice", "Bob", "Charlie"];
names.at(-1); // "Charlie"
```

## Mutating vs non-mutating methods

This is a crucial distinction when working with arrays:

### Mutating methods (change the original array)

Some array methods **modify the original array**:

```javascript
const arr = [1, 2, 3];
arr.push(4);     // Mutates: arr is now [1, 2, 3, 4]
arr.pop();       // Mutates: arr is now [1, 2, 3]
arr.reverse();   // Mutates: arr is now [3, 2, 1]
arr.sort();      // Mutates: arr is sorted
```

### Non-mutating methods (return a new array)

Other methods **return a new array** without changing the original:

```javascript
const arr = [1, 2, 3];
const doubled = arr.map(x => x * 2);  // Returns [2, 4, 6], arr is still [1, 2, 3]
const filtered = arr.filter(x => x > 1); // Returns [2, 3], arr is still [1, 2, 3]
const sliced = arr.slice(1, 3);       // Returns [2, 3], arr is still [1, 2, 3]
```

**Important:** When you want to keep the original array unchanged, use non-mutating methods or create a copy first:

```javascript
const original = [1, 2, 3];
const reversed = [...original].reverse(); // Creates copy, then reverses
// original is still [1, 2, 3]
```

## Common array methods

### Adding and removing elements

```javascript
const arr = [1, 2, 3];

// Add to end
arr.push(4);        // [1, 2, 3, 4] (mutates)

// Remove from end
arr.pop();          // Returns 4, arr is now [1, 2, 3] (mutates)

// Add to beginning
arr.unshift(0);     // [0, 1, 2, 3] (mutates)

// Remove from beginning
arr.shift();        // Returns 0, arr is now [1, 2, 3] (mutates)
```

### Finding elements

```javascript
const names = ["Alice", "Bob", "Charlie"];

names.indexOf("Bob");        // 1 (returns index, or -1 if not found)
names.includes("Bob");       // true
names.find(name => name.length > 3); // "Alice" (first element matching condition)
names.findIndex(name => name.length > 3); // 0 (index of first matching element)
```

### Slicing and splicing

```javascript
const arr = [1, 2, 3, 4, 5];

// slice() - non-mutating, extracts portion
arr.slice(1, 4);    // [2, 3, 4] (from index 1 to 3, original unchanged)
arr.slice(2);       // [3, 4, 5] (from index 2 to end)
arr.slice(-2);      // [4, 5] (last 2 elements)

// splice() - mutating, adds/removes elements
const arr2 = [1, 2, 3, 4, 5];
arr2.splice(2, 1, 99); // Remove 1 element at index 2, insert 99
// arr2 is now [1, 2, 99, 4, 5]
```

### Transforming arrays

```javascript
const numbers = [1, 2, 3, 4];

// map() - transform each element (non-mutating)
const doubled = numbers.map(x => x * 2);  // [2, 4, 6, 8]

// filter() - keep only matching elements (non-mutating)
const evens = numbers.filter(x => x % 2 === 0);  // [2, 4]

// reduce() - combine elements into a single value (non-mutating)
const sum = numbers.reduce((acc, x) => acc + x, 0);  // 10
```

We'll explore `map`, `filter`, and `reduce` in more detail below.

## Iteration patterns

### `for` loop

The classic way to iterate over arrays:

```javascript
const names = ["Alice", "Bob", "Charlie"];

for (let i = 0; i < names.length; i++) {
  console.log(names[i]);
}
// Output:
// Alice
// Bob
// Charlie
```

### `for...of` loop

A cleaner way to iterate (preferred for arrays):

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

**Prefer `for...of`** when you don't need the index. It's more readable and less error-prone.

### `forEach()` method

Arrays also have a `forEach()` method:

```javascript
const names = ["Alice", "Bob", "Charlie"];

names.forEach((name, index) => {
  console.log(`${index}: ${name}`);
});
// Output:
// 0: Alice
// 1: Bob
// 2: Charlie
```

## Array methods deep dive

### `map()` — transform each element

`map()` creates a new array by applying a function to each element:

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(x => x * 2);
// [2, 4, 6, 8]

const names = ["alice", "bob", "charlie"];
const capitalized = names.map(name => name.charAt(0).toUpperCase() + name.slice(1));
// ["Alice", "Bob", "Charlie"]
```

**Use `map()` when:** You want to transform each element into something else.

### `filter()` — keep matching elements

`filter()` creates a new array with only elements that pass a test:

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evens = numbers.filter(x => x % 2 === 0);
// [2, 4, 6]

const names = ["Alice", "Bob", "Charlie"];
const longNames = names.filter(name => name.length > 3);
// ["Alice", "Charlie"]
```

**Use `filter()` when:** You want to keep only some elements based on a condition.

### `reduce()` — combine elements

`reduce()` combines all elements into a single value:

```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
// 10

// Without initial value (uses first element as initial)
const sum2 = numbers.reduce((acc, current) => acc + current);
// 10

// More complex example: counting occurrences
const words = ["apple", "banana", "apple", "cherry", "banana", "apple"];
const counts = words.reduce((acc, word) => {
  acc[word] = (acc[word] || 0) + 1;
  return acc;
}, {});
// { apple: 3, banana: 2, cherry: 1 }
```

**Use `reduce()` when:** You need to combine all elements into a single value (sum, product, object, etc.).

### Chaining methods

You can chain array methods together:

```javascript
const numbers = [1, 2, 3, 4, 5, 6];

const result = numbers
  .filter(x => x % 2 === 0)  // [2, 4, 6]
  .map(x => x * x)            // [4, 16, 36]
  .reduce((acc, x) => acc + x, 0); // 56

console.log(result); // 56
```

This is a powerful pattern for processing data step by step.

## Common array operations

### Checking if array is empty

```javascript
const arr = [];

if (arr.length === 0) {
  console.log("Array is empty");
}

// Note: Empty array is truthy, so this doesn't work:
if (arr) {
  console.log("This runs even for empty arrays!");
}
```

### Copying arrays

```javascript
const original = [1, 2, 3];

// Shallow copy using spread operator
const copy1 = [...original];

// Shallow copy using slice()
const copy2 = original.slice();

// Note: These are shallow copies. Nested arrays/objects are still shared.
```

### Combining arrays

```javascript
const arr1 = [1, 2];
const arr2 = [3, 4];

const combined = [...arr1, ...arr2];  // [1, 2, 3, 4] (spread operator)
const combined2 = arr1.concat(arr2);   // [1, 2, 3, 4] (concat method)
```

### Sorting arrays

```javascript
const numbers = [3, 1, 4, 1, 5];
numbers.sort();  // [1, 1, 3, 4, 5] (mutates original)

// For numbers, you need a compare function
const nums = [10, 5, 40, 25];
nums.sort((a, b) => a - b);  // [5, 10, 25, 40] (ascending)
nums.sort((a, b) => b - a);  // [40, 25, 10, 5] (descending)
```

## Arrays vs objects (when to use each)

- **Use arrays** when:
  - Order matters
  - You need to iterate over all elements
  - You have a list of similar items

- **Use objects** (covered in the [next guide](./objects)) when:
  - You need to look up values by name/key
  - The data has a structure (properties with meaning)
  - Order doesn't matter (usually)
