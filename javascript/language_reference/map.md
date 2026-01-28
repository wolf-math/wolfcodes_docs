---
title: Map
sidebar_position: 14
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
> Object.getOwnPropertyNames(Map.prototype)
['constructor', 'size', 'clear', 'delete', 'entries', 'forEach', 'get', 'has', 'keys', 'set', 'values', Symbol.toStringTag, Symbol.iterator]
``` -->

## Definition

A `Map` is a collection of key-value pairs where keys can be any type (unlike objects where keys must be strings or symbols). Maps maintain insertion order and provide efficient lookups.

```javascript
> const map = new Map()
undefined

> map instanceof Map
true
```

## Using maps

```javascript
// Empty map
const map = new Map()

// From array of [key, value] pairs
const map2 = new Map([
  ['name', 'Alice'],
  ['age', 30]
])

// From another map
const map3 = new Map(map2)
```

## Map methods

### Setting and Getting

```javascript
const map = new Map()

// set() - adds or updates a key-value pair
map.set('name', 'Alice')
map.set('age', 30)

// get() - retrieves value by key
map.get('name')  // 'Alice'
map.get('age')   // 30
map.get('city')  // undefined (key doesn't exist)

// has() - checks if key exists
map.has('name')  // true
map.has('city')  // false
```

### Size

```javascript
const map = new Map([['a', 1], ['b', 2]])
map.size  // 2
```

### Deleting

```javascript
const map = new Map([['a', 1], ['b', 2]])

// delete() - removes a key-value pair
map.delete('a')  // true (key existed)
map.delete('c')  // false (key didn't exist)

// clear() - removes all entries
map.clear()
map.size  // 0
```

## Operations on maps

### Iteration

### `for...of` Loop

```javascript
const map = new Map([['name', 'Alice'], ['age', 30]])

// Iterate over entries (default)
for (const [key, value] of map) {
  console.log(key, value)
}

// Iterate over keys
for (const key of map.keys()) {
  console.log(key)
}

// Iterate over values
for (const value of map.values()) {
  console.log(value)
}
```

### `forEach()`

```javascript
const map = new Map([['name', 'Alice'], ['age', 30]])

map.forEach((value, key) => {
  console.log(key, value)
})
```

### `entries()`, `keys()`, `values()`

```javascript
const map = new Map([['name', 'Alice'], ['age', 30]])

Array.from(map.entries())  // [['name', 'Alice'], ['age', 30]]
Array.from(map.keys())      // ['name', 'age']
Array.from(map.values())    // ['Alice', 30]
```

## Map vs object

| Feature           | Map                    | Object                 |
| ----------------- | ---------------------- | ---------------------- |
| **Key types**     | Any type               | String or Symbol       |
| **Size**          | `map.size`             | Manual calculation     |
| **Iteration**     | Directly iterable      | Requires `Object.keys()` |
| **Prototype**     | No default keys        | Has default keys        |
| **Performance**    | Better for frequent additions/deletions | Better for small, static data |

## Use cases

### Using Non-String Keys

```javascript
const map = new Map()

const objKey = { id: 1 }
const funcKey = () => {}

map.set(objKey, 'value1')
map.set(funcKey, 'value2')

map.get(objKey)  // 'value1'
```

### Counting Occurrences

```javascript
const words = ['hello', 'world', 'hello']
const count = new Map()

words.forEach(word => {
  count.set(word, (count.get(word) || 0) + 1)
})
// Map { 'hello' => 2, 'world' => 1 }
```

### Caching

```javascript
const cache = new Map()

function expensiveOperation(input) {
  if (cache.has(input)) {
    return cache.get(input)
  }
  
  const result = /* expensive computation */
  cache.set(input, result)
  return result
}
```

## Best practices

1. **Use Map for dynamic key-value pairs**: When you frequently add/remove entries.

2. **Use Object for static data**: When you have a fixed set of known properties.

3. **Use Map for non-string keys**: When you need objects or functions as keys.

4. **Use Map.size**: More convenient than `Object.keys(obj).length`.

5. **Consider performance**: Maps are optimized for frequent additions/deletions.

