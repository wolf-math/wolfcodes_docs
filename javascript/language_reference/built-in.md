---
title: Built-in Functions and Global Objects
sidebar_position: 1
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

Built-in functions are JavaScript functions that exist in the global namespace. They are available everywhere in your code without needing to import. Some of these functions are not tied to a specific type, such as the `parseInt()` function that can convert strings to numbers.

```javascript
// Get all global properties
Object.getOwnPropertyNames(globalThis)
```

You will notice several groups in JavaScript's global namespace. This page focuses on the actual built-in functions of JavaScript that are not constructors or objects.

### `decodeURI`

Decodes a Uniform Resource Identifier (URI) previously created by `encodeURI()`.

```javascript
const encoded = encodeURI('https://example.com/hello world')
// 'https://example.com/hello%20world'

decodeURI(encoded)
// 'https://example.com/hello world'
```

---

### `decodeURIComponent`

Decodes a Uniform Resource Identifier (URI) component previously created by `encodeURIComponent()`.

```javascript
const encoded = encodeURIComponent('hello world')
// 'hello%20world'

decodeURIComponent(encoded)
// 'hello world'
```

---

### `encodeURI`

Encodes a URI by replacing each instance of certain characters with escape sequences.

```javascript
encodeURI('https://example.com/hello world')
// 'https://example.com/hello%20world'
```

---

### `encodeURIComponent`

Encodes a URI component by replacing each instance of certain characters with escape sequences.

```javascript
encodeURIComponent('hello world')
// 'hello%20world'
```

---

### `escape` (deprecated)

Creates a new string in which certain characters have been escaped. **Deprecated**: Use `encodeURI()` or `encodeURIComponent()` instead.

---

### `eval`

Evaluates JavaScript code represented as a string. 

```javascript
eval('2 + 2')  // 4
eval('let x = 5; x * 2')  // 10
```

:::warning
Using `eval()` is dangerous and should be avoided. It can execute arbitrary code and is a security risk. It also makes code harder to understand and optimize.
:::

---

### `isFinite`

Determines whether the passed value is a finite number. Returns `false` if the value is `NaN`, `Infinity`, or `-Infinity`.

```javascript
isFinite(42)           // true
isFinite(Infinity)     // false
isFinite(-Infinity)    // false
isFinite(NaN)          // false
isFinite('42')         // true (coerces to number)
isFinite('hello')      // false
```

---

### `isNaN`

Determines whether a value is `NaN` (Not-a-Number). Note that `NaN` is the only value that is not equal to itself.

```javascript
isNaN(NaN)             // true
isNaN(42)              // false
isNaN('42')            // false (coerces to number)
isNaN('hello')         // true (coerces to NaN)
isNaN(undefined)       // true
```

For a more robust check, use `Number.isNaN()` which doesn't coerce values.

---

### `parseFloat`

Parses a string argument and returns a floating point number.

```javascript
parseFloat('3.14')     // 3.14
parseFloat('42')       // 42
parseFloat('42px')     // 42 (stops at first non-numeric character)
parseFloat('hello')    // NaN
parseFloat('')         // NaN
```

---

### `parseInt`

Parses a string argument and returns an integer of the specified radix (base).

```javascript
parseInt('42')         // 42
parseInt('42.7')       // 42 (stops at decimal point)
parseInt('42px')       // 42
parseInt('1010', 2)    // 10 (binary)
parseInt('FF', 16)     // 255 (hexadecimal)
parseInt('hello')      // NaN
```

---



### `unescape` (deprecated)

Computes a new string in which hexadecimal escape sequences are replaced with the characters they represent. **Deprecated**: Use `decodeURI()` or `decodeURIComponent()` instead.

---

## Global objects

Global objects are built-in objects that are available in the global scope of JavaScript. Unlike global functions (which are callable directly), global objects are constructors or utility objects that provide methods, properties, and functionality for working with specific data types or performing common operations.

These objects are automatically available in any JavaScript environment (browser, Node.js, etc.) without needing to be imported or declared. They serve as the foundation for JavaScript's built-in functionality, providing constructors for creating instances of built-in types (like `Array`, `Date`, `Object`) as well as utility objects for common operations (like `Math`, `JSON`, `console`).

Key characteristics of global objects:
- **Constructors**: Many global objects (like `Array`, `Date`, `Object`) can be used with the `new` keyword to create instances
- **Static methods**: Global objects often provide static methods that can be called directly on the object (like `Array.isArray()`, `Object.keys()`)
- **Utility objects**: Some global objects (like `Math`, `JSON`) are utility objects that provide methods and constants but are not meant to be instantiated
- **Always available**: These objects are part of the global scope and don't require any imports or declarations

The following global objects provide important functionality:

### `Array`

The `Array` constructor and its methods for working with arrays.

```javascript
Array.isArray([1, 2, 3])                 // true
Array.from('hello')                      // ['h', 'e', 'l', 'l', 'o']
Array.of(1, 2, 3)                        // [1, 2, 3]
```

---

### `Boolean`

The `Boolean` constructor for working with boolean values.

```javascript
Boolean(1)                               // true
Boolean(0)                               // false
Boolean('')                              // false
```

---

### `console`

The `console` object provides methods for logging and debugging.

```javascript
console.log('Hello')                     // Logs to console
console.error('Error')                   // Logs error
console.warn('Warning')                  // Logs warning
console.info('Info')                     // Logs info
```

---

### `Date`

The `Date` constructor for working with dates and times.

```javascript
new Date()                               // Current date/time
new Date('2023-01-01')                   // Specific date
Date.now()                               // Current timestamp
```

---

### `Error`, `TypeError`, `ReferenceError`, etc.

Error constructors for creating error objects.

```javascript
new Error('Something went wrong')
new TypeError('Invalid type')
new ReferenceError('Variable not defined')
```


---

### `JSON`

The `JSON` object provides methods for parsing and stringifying JSON data.

```javascript
JSON.parse('{"name": "Alice"}')           // { name: 'Alice' }
JSON.stringify({ name: 'Alice' })        // '{"name":"Alice"}'
```

---


### `Map`, `Set`, `WeakMap`, `WeakSet`

Constructors for collection types.

```javascript
new Map()                                // Empty Map
new Set()                                // Empty Set
new WeakMap()                            // Empty WeakMap
new WeakSet()                            // Empty WeakSet
```

---

### `Math`

The `Math` object provides mathematical constants and functions.

```javascript
Math.PI                                  // 3.141592653589793
Math.sqrt(16)                            // 4
Math.max(1, 2, 3)                        // 3
Math.min(1, 2, 3)                        // 1
Math.random()                            // Random number between 0 and 1
```

---

### `Number`

The `Number` constructor and its methods for working with numbers.

```javascript
Number.isNaN(NaN)                        // true
Number.isFinite(42)                      // true
Number.parseInt('42')                    // 42
Number.parseFloat('3.14')                // 3.14
```

---

### `Object`

The `Object` constructor and its methods for working with objects.

```javascript
Object.keys({ a: 1, b: 2 })              // ['a', 'b']
Object.values({ a: 1, b: 2 })            // [1, 2]
Object.entries({ a: 1, b: 2 })          // [['a', 1], ['b', 2]]
Object.assign({}, { a: 1 })             // { a: 1 }
```

---


### `Promise`

The `Promise` constructor for working with asynchronous operations.

```javascript
new Promise((resolve, reject) => {
  resolve('Success')
})
```

---

### `RegExp`

The `RegExp` constructor for working with regular expressions.

```javascript
new RegExp('hello')                      // /hello/
RegExp('hello', 'gi')                    // /hello/gi
```

---

### `String`

The `String` constructor and its methods for working with strings.

```javascript
String.fromCharCode(65)                  // 'A'
String.raw`Hello\nWorld`                 // 'Hello\\nWorld'
```



