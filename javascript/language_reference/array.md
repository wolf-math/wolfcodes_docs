---
title: Array
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
<!-- ## Properties

```javascript
> Object.getOwnPropertyNames(Array.prototype)
['length', 'constructor', 'at', 'concat', 'copyWithin', 'entries', 'every', 'fill', 'filter', 'find', 'findIndex', 'findLast', 'findLastIndex', 'flat', 'flatMap', 'forEach', 'includes', 'indexOf', 'join', 'keys', 'lastIndexOf', 'map', 'pop', 'push', 'reduce', 'reduceRight', 'reverse', 'shift', 'slice', 'some', 'sort', 'splice', 'toLocaleString', 'toString', 'unshift', 'values', 'toReversed', 'toSorted', 'toSpliced', 'with']
``` -->

## Definition

An `Array` is a collection of items defined with square brackets `[]`. These items are stored at locations within the array starting at index `0`. Items within an array can be modified, added, or removed, and can contain multiple types, including other arrays. Unlike many other programming languages, a JavaScript array can contain many different types: `['apple', 2, true, 'string cheese']`.

```javascript
> typeof []
"object"

> Array.isArray([])
true
```

## Using arrays

Arrays can be created using array literals or the `Array` constructor:

```javascript
// Literal syntax (preferred)
> const myArray = ['apple', 2, true, 'string cheese']
undefined

// Array constructor
> const myArray2 = new Array('apple', 2, true)
undefined

> const myArray3 = new Array(5)
undefined

> myArray3
[empty × 5]

// Array.of()
> Array.of(1, 2, 3)
[1, 2, 3]

// Array.from()
> Array.from('hello')
['h', 'e', 'l', 'l', 'o']
```

### Accessing elements

Array elements are accessed by their index. Indices start at `0`. A negative index can be used with `at()` method (ES2022).

```javascript
> const myArray = ['apple', 2, true, 'string cheese']
undefined

> myArray[0]
'apple'

> myArray[1]
2

> myArray[3]
'string cheese'

> myArray[10]
undefined

// Using at() method (ES2022)
> myArray.at(-1)
'string cheese'

> myArray.at(-2)
true
```

### Array length

Get the length of an array:

```javascript
> const arr = [1, 2, 3]
undefined

> arr.length
3

// Setting length can truncate or extend array
> arr.length = 5
5

> arr
[1, 2, 3, empty × 2]

> arr.length = 2
2

> arr
[1, 2]
```

### Modifying arrays

#### Adding elements

```javascript
const arr = [1, 2, 3]

// push() - adds to end
arr.push(4)      // [1, 2, 3, 4]

// unshift() - adds to beginning
arr.unshift(0)   // [0, 1, 2, 3, 4]

// Direct assignment
arr[5] = 6       // [0, 1, 2, 3, 4, empty, 6]
```

#### Removing elements

```javascript
const arr = [1, 2, 3, 4, 5]

// pop() - removes from end
arr.pop()        // Returns 5, arr is now [1, 2, 3, 4]

// shift() - removes from beginning
arr.shift()      // Returns 1, arr is now [2, 3, 4]

// splice() - removes/inserts at specific index
arr.splice(1, 1) // Removes 1 element at index 1, arr is now [2, 4]
```

#### Modifying elements

```javascript
const arr = [1, 2, 3]
arr[1] = 20      // [1, 20, 3]
```

## Operations on arrays

### Destructuring

Extract elements from arrays:

```javascript
> const arr = [1, 2, 3]
undefined

// Basic destructuring
> const [a, b, c] = arr
undefined

> a
1

> b
2

> c
3

// Skip elements
> const [first, , third] = arr
undefined

> first
1

> third
3

// Rest operator
> const [first, ...rest] = arr
undefined

> first
1

> rest
[2, 3]

// Default values
> const [a = 0, b = 0] = [1]
undefined

> a
1

> b
0
```

### Spread operator

Copy and merge arrays:

```javascript
> const arr1 = [1, 2, 3]
undefined

> const arr2 = [4, 5, 6]
undefined

// Copy
> const copy = [...arr1]
undefined

> copy
[1, 2, 3]

// Merge
> const merged = [...arr1, ...arr2]
undefined

> merged
[1, 2, 3, 4, 5, 6]

// Add elements
> const extended = [...arr1, 4, 5]
undefined

> extended
[1, 2, 3, 4, 5]
```

## Array methods

### `concat()`

Merges two or more arrays.

```javascript
[1, 2].concat([3, 4])       // [1, 2, 3, 4]
[1, 2].concat([3, 4], [5, 6]) // [1, 2, 3, 4, 5, 6]
```

---

### `every()`

Tests whether all elements pass a test.

```javascript
[1, 2, 3].every(x => x > 0)  // true
```

---

### `filter()`

Creates a new array with elements that pass a test.

```javascript
[1, 2, 3, 4, 5].filter(x => x > 2)  // [3, 4, 5]
```

---

### `find()`

Returns the first element that passes a test.

```javascript
[1, 2, 3, 4, 5].find(x => x > 2)  // 3
```

---

### `findIndex()`

Returns the index of the first element that passes a test.

```javascript
[1, 2, 3, 4, 5].findIndex(x => x > 2)  // 2
```

---

### `forEach()`

Executes a function for each array element.

```javascript
[1, 2, 3].forEach((item, index) => {
  console.log(item, index)
})
// 1 0
// 2 1
// 3 2
```

---

### `includes()`

Determines whether an array includes a certain value.

```javascript
[1, 2, 3].includes(2)       // true
[1, 2, 3].includes(4)       // false
```

---

### `indexOf()`

Returns the first index of an element, or -1 if not found.

```javascript
[1, 2, 3, 2].indexOf(2)     // 1
[1, 2, 3].indexOf(4)        // -1
```

---

### `join()`

Joins all elements into a string.

```javascript
[1, 2, 3].join(', ')      // "1, 2, 3"
[1, 2, 3].join('')        // "123"
```

---

### `lastIndexOf()`

Returns the last index of an element, or -1 if not found.

```javascript
[1, 2, 3, 2].lastIndexOf(2) // 3
```

---

### `map()`

Creates a new array with the results of calling a function on every element.

```javascript
[1, 2, 3].map(x => x * 2)  // [2, 4, 6]
```

---

### `some()`

Tests whether at least one element passes a test.

```javascript
[1, 2, 3].some(x => x > 2)  // true
```

---



### `reduce()`

Reduces an array to a single value.

```javascript
[1, 2, 3, 4].reduce((acc, val) => acc + val, 0)  // 10
```

---

### `reduceRight()`

Same as `reduce()`, but processes from right to left.

```javascript
[1, 2, 3].reduceRight((acc, val) => acc - val, 0)  // -6
```

---

### `reverse()`

Reverses an array in place.

```javascript
const arr = [1, 2, 3]
arr.reverse()              // [3, 2, 1] (mutates original)
```

---

### `slice()`

Returns a shallow copy of a portion of an array.

```javascript
[1, 2, 3, 4, 5].slice(1, 4)  // [2, 3, 4]
[1, 2, 3, 4, 5].slice(2)     // [3, 4, 5]
[1, 2, 3, 4, 5].slice(-2)   // [4, 5]
```

---

### `sort()`

Sorts an array in place.

```javascript
const arr = [3, 1, 2]
arr.sort()                 // [1, 2, 3] (mutates original)

// Custom sort
[3, 1, 2].sort((a, b) => b - a)  // [3, 2, 1] (descending)
```

---

### `splice()`

Changes the contents of an array by removing or replacing elements.

```javascript
const arr = [1, 2, 3, 4, 5]
arr.splice(1, 2, 'a', 'b')  // Removes 2 elements starting at index 1, inserts 'a', 'b'
// arr is now [1, 'a', 'b', 4, 5]
```

---

### `toString()`

Returns a string representation of an array.

```javascript
[1, 2, 3].toString()       // "1,2,3"
```
