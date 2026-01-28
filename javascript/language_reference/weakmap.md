---
title: WeakMap
sidebar_position: 16
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## Definition

A `WeakMap` is a collection of key-value pairs where keys must be objects. WeakMaps allow garbage collection of keys when they are no longer referenced elsewhere, making them useful for storing private data or metadata about objects.

```javascript
const weakMap = new WeakMap()
weakMap instanceof WeakMap  // true
```

## Creating weakmaps

```javascript
// Empty WeakMap
const weakMap = new WeakMap()

// From array of [key, value] pairs (keys must be objects)
const obj1 = {}
const obj2 = {}
const weakMap2 = new WeakMap([
  [obj1, 'value1'],
  [obj2, 'value2']
])
```

## Weakmap methods

### Setting and Getting

```javascript
const weakMap = new WeakMap()
const obj = {}

// set() - adds or updates a key-value pair
weakMap.set(obj, 'value')

// get() - retrieves value by key
weakMap.get(obj)  // 'value'
weakMap.get({})   // undefined (different object)

// has() - checks if key exists
weakMap.has(obj)  // true
```

### Deleting

```javascript
const weakMap = new WeakMap()
const obj = {}
weakMap.set(obj, 'value')

// delete() - removes a key-value pair
weakMap.delete(obj)  // true
weakMap.has(obj)     // false
```

## Key differences from map

| Feature           | WeakMap                | Map                    |
| ----------------- | ---------------------- | ---------------------- |
| **Key types**     | Objects only           | Any type               |
| **Iteration**     | Not iterable           | Iterable               |
| **Size**          | No `size` property     | Has `size` property    |
| **Garbage collection** | Keys can be GC'd    | Keys prevent GC        |
| **Methods**       | `get`, `set`, `has`, `delete` | Full API |

## Use cases

### Private data storage

```javascript
const privateData = new WeakMap()

class User {
  constructor(name) {
    privateData.set(this, { name })
  }
  
  getName() {
    return privateData.get(this).name
  }
}

const user = new User('Alice')
user.getName()  // 'Alice'
// privateData is not accessible from outside
```

### Metadata storage

```javascript
const metadata = new WeakMap()

function addMetadata(obj, data) {
  metadata.set(obj, data)
}

function getMetadata(obj) {
  return metadata.get(obj)
}

const obj = {}
addMetadata(obj, { created: Date.now() })
getMetadata(obj)  // { created: ... }
```

### Caching with automatic cleanup

```javascript
const cache = new WeakMap()

function getCachedValue(obj) {
  if (!cache.has(obj)) {
    const value = /* expensive computation */
    cache.set(obj, value)
  }
  return cache.get(obj)
}

// When obj is garbage collected, cache entry is automatically removed
```

## Why weakmap?

WeakMaps allow garbage collection of keys when they're no longer referenced:

```javascript
let obj = { id: 1 }
const weakMap = new WeakMap()
weakMap.set(obj, 'data')

obj = null  // Object can now be garbage collected
// WeakMap entry is automatically removed
```

This is different from Map:

```javascript
let obj = { id: 1 }
const map = new Map()
map.set(obj, 'data')

obj = null  // Object cannot be garbage collected
// Map still holds reference to obj
```

## Limitations

1. **Not iterable**: Cannot use `for...of`, `forEach()`, or get `size`.

2. **Objects only**: Keys must be objects, not primitives.

3. **No size property**: Cannot check how many entries exist.

## Best practices

1. **Use for private data**: Store data that should be private to objects.

2. **Use for metadata**: Attach metadata to objects without modifying them.

3. **Let garbage collection work**: Don't hold references to keys elsewhere if you want automatic cleanup.

4. **Don't use for iteration**: If you need to iterate, use Map instead.

5. **Understand garbage collection**: WeakMaps are designed to work with GC—use them when this behavior is desired.

