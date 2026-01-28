---
title: Set
sidebar_position: 15
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
> Object.getOwnPropertyNames(Set.prototype)
['constructor', 'size', 'add', 'clear', 'delete', 'entries', 'forEach', 'has', 'keys', 'values', Symbol.toStringTag, Symbol.iterator]
``` -->

## Definition

A `Set` is a collection of unique values. Each value can occur only once in a Set. Sets maintain insertion order and provide efficient membership testing.

```javascript
> const set = new Set()
undefined

> set instanceof Set
true
```

## Using sets

```javascript
// Empty set
const set = new Set()

// From array
const set2 = new Set([1, 2, 3, 3, 2, 1])
// Set { 1, 2, 3 } (duplicates removed)

// From string
const set3 = new Set('hello')
// Set { 'h', 'e', 'l', 'o' } (duplicates removed)
```

## Operations on sets

## Set methods

### Adding and Checking

```javascript
const set = new Set()

// add() - adds a value
set.add(1)
set.add(2)
set.add(1)  // Ignored (duplicate)

// has() - checks if value exists
set.has(1)  // true
set.has(3)  // false
```

### Size

```javascript
const set = new Set([1, 2, 3])
set.size  // 3
```

### Deleting

```javascript
const set = new Set([1, 2, 3])

// delete() - removes a value
set.delete(2)  // true (value existed)
set.delete(4)  // false (value didn't exist)

// clear() - removes all values
set.clear()
set.size  // 0
```

### Iteration

### `for...of` Loop

```javascript
const set = new Set([1, 2, 3])

for (const value of set) {
  console.log(value)
}
// 1
// 2
// 3
```

### `forEach()`

```javascript
const set = new Set([1, 2, 3])

set.forEach(value => {
  console.log(value)
})
```

### `values()`, `keys()`, `entries()`

```javascript
const set = new Set([1, 2, 3])

Array.from(set.values())  // [1, 2, 3]
Array.from(set.keys())    // [1, 2, 3] (same as values)
Array.from(set.entries()) // [[1, 1], [2, 2], [3, 3]]
```

### Set operations

### Union

```javascript
const set1 = new Set([1, 2, 3])
const set2 = new Set([3, 4, 5])

const union = new Set([...set1, ...set2])
// Set { 1, 2, 3, 4, 5 }
```

### Intersection

```javascript
const set1 = new Set([1, 2, 3])
const set2 = new Set([2, 3, 4])

const intersection = new Set(
  [...set1].filter(x => set2.has(x))
)
// Set { 2, 3 }
```

### Difference

```javascript
const set1 = new Set([1, 2, 3])
const set2 = new Set([2, 3, 4])

const difference = new Set(
  [...set1].filter(x => !set2.has(x))
)
// Set { 1 }
```

## Use cases

### Removing Duplicates

```javascript
const array = [1, 2, 2, 3, 3, 3]
const unique = [...new Set(array)]
// [1, 2, 3]
```

### Membership Testing

```javascript
const allowedUsers = new Set(['alice', 'bob', 'charlie'])

function isAllowed(username) {
  return allowedUsers.has(username)
}
```

### Tracking Visited Items

```javascript
const visited = new Set()

function visit(item) {
  if (visited.has(item)) {
    return 'Already visited'
  }
  visited.add(item)
  return 'First visit'
}
```

## Set vs array

| Feature        | Set                    | Array                 |
| -------------- | ---------------------- | --------------------- |
| **Uniqueness** | Enforced automatically | Manual checking       |
| **Lookup**     | O(1) average           | O(n)                  |
| **Order**      | Insertion order        | Index-based           |
| **Duplicates** | Not allowed            | Allowed               |

## Best practices

1. **Use Set for uniqueness**: When you need to ensure values are unique.

2. **Use Set for membership testing**: Faster than `array.includes()` for large collections.

3. **Convert to array when needed**: Use spread operator `[...set]` to convert back to array.

4. **Use Set for deduplication**: Simple way to remove duplicates from arrays.

5. **Consider WeakSet**: For object-only collections that allow garbage collection.

