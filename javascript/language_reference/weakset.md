---
title: WeakSet
sidebar_position: 17
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

A `WeakSet` is a collection of unique objects. Like WeakMap, WeakSet allows garbage collection of its elements when they are no longer referenced elsewhere. WeakSets are useful for tracking object membership without preventing garbage collection.

```javascript
const weakSet = new WeakSet()
weakSet instanceof WeakSet  // true
```

## Creating weaksets

```javascript
// Empty WeakSet
const weakSet = new WeakSet()

// From array of objects
const obj1 = {}
const obj2 = {}
const weakSet2 = new WeakSet([obj1, obj2])
```

## Weakset methods

### Adding and checking

```javascript
const weakSet = new WeakSet()
const obj = {}

// add() - adds an object
weakSet.add(obj)

// has() - checks if object exists
weakSet.has(obj)  // true
weakSet.has({})    // false (different object)

// delete() - removes an object
weakSet.delete(obj)  // true
weakSet.has(obj)    // false
```

## Key differences from set

| Feature           | WeakSet               | Set                    |
| ----------------- | --------------------- | ---------------------- |
| **Value types**   | Objects only          | Any type               |
| **Iteration**     | Not iterable          | Iterable               |
| **Size**          | No `size` property    | Has `size` property    |
| **Garbage collection** | Values can be GC'd | Values prevent GC      |
| **Methods**       | `add`, `has`, `delete` | Full API              |

## Use cases

### Tracking object membership

```javascript
const processed = new WeakSet()

function processObject(obj) {
  if (processed.has(obj)) {
    return 'Already processed'
  }
  
  // Process object
  processed.add(obj)
  return 'Processed'
}
```

### Preventing circular references

```javascript
const visited = new WeakSet()

function traverse(obj) {
  if (visited.has(obj)) {
    return  // Already visited, prevent infinite loop
  }
  
  visited.add(obj)
  // Continue traversal
}
```

### Tagging objects

```javascript
const tagged = new WeakSet()

function tag(obj) {
  tagged.add(obj)
}

function isTagged(obj) {
  return tagged.has(obj)
}

const obj = {}
tag(obj)
isTagged(obj)  // true
```

## Why weakset?

WeakSets allow garbage collection of their elements:

```javascript
let obj = { id: 1 }
const weakSet = new WeakSet()
weakSet.add(obj)

obj = null  // Object can now be garbage collected
// WeakSet entry is automatically removed
```

This is different from Set:

```javascript
let obj = { id: 1 }
const set = new Set()
set.add(obj)

obj = null  // Object cannot be garbage collected
// Set still holds reference to obj
```

## Limitations

1. **Not iterable**: Cannot use `for...of`, `forEach()`, or get `size`.

2. **Objects only**: Values must be objects, not primitives.

3. **No size property**: Cannot check how many objects are in the WeakSet.

4. **Limited API**: Only `add()`, `has()`, and `delete()` methods.

## Best practices

1. **Use for object tracking**: Track which objects have been processed or visited.

2. **Use for tagging**: Mark objects with metadata without modifying them.

3. **Let garbage collection work**: Don't hold references to objects elsewhere if you want automatic cleanup.

4. **Don't use for iteration**: If you need to iterate, use Set instead.

5. **Understand garbage collection**: WeakSets are designed to work with GC—use them when this behavior is desired.

