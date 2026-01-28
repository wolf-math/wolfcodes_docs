---
title: Symbol
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
<!-- ## Properties

```javascript
> Object.getOwnPropertyNames(Symbol.prototype)
['constructor', 'toString', 'valueOf', 'description', Symbol.toPrimitive]
``` -->

## Definition

A `Symbol` is a unique and immutable primitive value that may be used as the key of an object property. Symbols are guaranteed to be unique—even if you create two symbols with the same description, they are different values.

```javascript
> typeof Symbol()
"symbol"
```

## Using symbols

Symbols are created using the `Symbol()` function:

```javascript
// Basic symbol
const sym1 = Symbol()
const sym2 = Symbol()

sym1 === sym2    // false (always unique)

// Symbol with description
const sym3 = Symbol("description")
const sym4 = Symbol("description")

sym3 === sym4    // false (still unique, description is just metadata)
```

### `Symbol.for()` and `Symbol.keyFor()`

#### `Symbol.for()`

Creates a symbol in the global symbol registry. If a symbol with the given key already exists, it returns that symbol.

```javascript
const sym1 = Symbol.for("key")
const sym2 = Symbol.for("key")

sym1 === sym2    // true (same symbol from registry)
```

#### `Symbol.keyFor()`

Retrieves the key for a symbol from the global symbol registry.

```javascript
const sym = Symbol.for("key")
Symbol.keyFor(sym)  // "key"

const localSym = Symbol("key")
Symbol.keyFor(localSym)  // undefined (not in registry)
```

### Using symbols as object keys

Symbols can be used as unique property keys:

```javascript
const sym = Symbol("id")
const obj = {
  name: "Alice",
  [sym]: 12345
}

console.log(obj[sym])   // 12345
console.log(obj.name)   // "Alice"
```

#### Symbol properties are hidden

Symbol properties are not enumerable and won't appear in `for...in` loops or `Object.keys()`:

```javascript
const sym = Symbol("id")
const obj = {
  name: "Alice",
  [sym]: 12345
}

for (let key in obj) {
  console.log(key)      // Only "name"
}

Object.keys(obj)        // ["name"]
Object.getOwnPropertySymbols(obj)  // [Symbol(id)]
```

## Operations on symbols

### Well-known symbols

JavaScript has several built-in symbols that control language behavior:

JavaScript has several built-in symbols that control language behavior:

### `Symbol.iterator`

Makes an object iterable:

```javascript
const obj = {
  *[Symbol.iterator]() {
    yield 1
    yield 2
    yield 3
  }
}

[...obj]  // [1, 2, 3]
```

### `Symbol.toStringTag`

Customizes the default string description of an object:

```javascript
class MyClass {
  get [Symbol.toStringTag]() {
    return "MyClass"
  }
}

String(new MyClass())  // "[object MyClass]"
```

### `Symbol.toPrimitive`

Converts an object to a primitive value:

```javascript
const obj = {
  [Symbol.toPrimitive](hint) {
    if (hint === "number") return 42
    if (hint === "string") return "hello"
    return "default"
  }
}

+obj      // 42
String(obj)  // "hello"
```

### `Symbol.hasInstance`

Customizes the behavior of the `instanceof` operator:

```javascript
class MyArray {
  static [Symbol.hasInstance](instance) {
    return Array.isArray(instance)
  }
}

[] instanceof MyArray  // true
```

### `Symbol.isConcatSpreadable`

Controls whether an object should be flattened when used with `Array.prototype.concat()`:

```javascript
const arr = [1, 2]
arr[Symbol.isConcatSpreadable] = false
[].concat(arr)  // [[1, 2]] instead of [1, 2]
```

### `Symbol.match`, `Symbol.replace`, `Symbol.search`, `Symbol.split`

Customize string matching behavior:

```javascript
class MyMatcher {
  constructor(value) {
    this.value = value
  }
  [Symbol.match](string) {
    return string.indexOf(this.value)
  }
}

"hello".match(new MyMatcher("ll"))  // 2
```

## Common use cases

### Private Properties

Symbols can be used to create "private" properties (though not truly private):

```javascript
const _private = Symbol("private")

class MyClass {
  constructor() {
    this[_private] = "secret"
  }
  
  getPrivate() {
    return this[_private]
  }
}
```

### Avoiding Property Name Collisions

Symbols ensure unique property names:

```javascript
const MY_FEATURE = Symbol("myFeature")

// Multiple libraries can use the same symbol key
library1[MY_FEATURE] = "value1"
library2[MY_FEATURE] = "value2"  // No collision
```

### Metadata

Symbols can store metadata on objects:

```javascript
const metadata = Symbol("metadata")

function addMetadata(obj, data) {
  obj[metadata] = data
}

function getMetadata(obj) {
  return obj[metadata]
}
```

## Symbol methods

### Symbol.prototype.description

Returns the optional description of a symbol:

```javascript
const sym = Symbol("my description")
sym.description  // "my description"

const sym2 = Symbol()
sym2.description  // undefined
```

## Best practices

1. **Use for unique keys**: When you need guaranteed unique property names.

2. **Use well-known symbols**: To customize language behavior (iterators, toString, etc.).

3. **Don't use for true privacy**: Symbols are discoverable via `Object.getOwnPropertySymbols()`.

4. **Use descriptions**: Always provide meaningful descriptions for debugging:

```javascript
// Good
const userId = Symbol("userId")

// Less helpful
const userId = Symbol()
```

