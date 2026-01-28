---
title: Object
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
<!-- ## Properties -->

<!-- ```javascript
> Object.getOwnPropertyNames(Object.prototype)
['constructor', '__defineGetter__', '__defineSetter__', 'hasOwnProperty', '__lookupGetter__', '__lookupSetter__', 'isPrototypeOf', 'propertyIsEnumerable', 'toString', 'valueOf', '__proto__', 'toLocaleString']
``` -->

## Definition

An `Object` is a collection of properties, where each property is a key-value pair. Objects are the fundamental data structure in JavaScript and are used to store and organize data.

```javascript
> typeof {}
"object"

> typeof []
"object"

> typeof null
"object"
```

:::note

 The `typeof` operator returns `"object"` for arrays and `null`, but this can be misleading:

- **Arrays**: Arrays are actually a special type of object in JavaScript. They're objects with numeric indices and a `length` property. To check if a value is an array, use `Array.isArray()` instead:
  ```javascript
  > Array.isArray([])
  true
  
  > Array.isArray({})
  false
  ```

- **`null`**: The fact that `typeof null` returns `"object"` is a well-known historical bug in JavaScript that has been preserved for backwards compatibility. `null` is actually a primitive value representing the intentional absence of any object value, not an object itself. To check for `null`, use strict equality:
  ```javascript
  > value === null
  true
  ```
:::

## Using objects

Objects can be created using object literals or the `Object` constructor:

```javascript
// Object literal (preferred)
> const person = { name: "Alice", age: 30 }
undefined

// Object constructor
> const person2 = new Object()
undefined

> person2.name = "Alice"
"Alice"

> person2.age = 30
30

// Object.create()
> const person3 = Object.create(null)
undefined

> person3.name = "Bob"
"Bob"
```

:::note

In these console/REPL examples, `undefined` appears after variable declarations because:

- **Variable declarations** (using `const`, `let`, or `var`) don't return a value—they return `undefined`. The variable is created, but the statement itself evaluates to `undefined`.
- **Assignment expressions** (like `person2.name = "Alice"`) return the assigned value, which is why you see `"Alice"` and `30` as outputs.
- This is normal behavior in JavaScript REPLs and browser consoles, which display the result of evaluating each expression.

:::

### Accessing properties

```javascript
> const person = { name: "Alice", age: 30 }
undefined

// Dot notation
> person.name
"Alice"

// Bracket notation
> person["name"]
"Alice"

> person["age"]
30

// Dynamic property (variable) access
> const key = "name"
undefined

> person[key]
"Alice"
```

### Setting properties

```javascript
> const person = {}
undefined

// Dot notation
> person.name = "Alice"
"Alice"

> person.age = 30
30

// Bracket notation
> person["city"] = "Boston"
"Boston"

> person["favorite color"] = "blue"
"blue"
```

### Deleting properties

```javascript
> const person = { name: "Alice", age: 30 }
undefined

> delete person.age
true

> person
{ name: "Alice" }
```

### Computed property names

Use expressions as property names:

```javascript
> const key = "name"
undefined

> const obj = { [key]: "Alice", [`${key}Length`]: 5 }
undefined

> obj
{ name: "Alice", nameLength: 5 }
```

### Property shorthand

When property name matches variable name:

```javascript
> const name = "Alice"
undefined

> const age = 30
undefined

> const person = { name, age }
undefined

> person
{ name: "Alice", age: 30 }
```

### Methods in object literals

Define methods in object literals:

```javascript
> const person = {
...   name: "Alice",
...   greet() {
...     return `Hello, I'm ${this.name}`
...   }
... }
undefined

> person.greet()
"Hello, I'm Alice"
```

### Getters and setters

```javascript
> const person = {
...   _age: 30,
...   get age() {
...     return this._age
...   },
...   set age(value) {
...     if (value > 0) {
...       this._age = value
...     }
...   }
... }
undefined

> person.age = 25
25

> person.age
25
```

## Operations on objects

### Destructuring

Extract properties from objects:

```javascript
> const person = { name: "Alice", age: 30 }
undefined

// Basic destructuring
> const { name, age } = person
undefined

> name
"Alice"

> age
30

// With renaming
> const { name: personName } = person
undefined

> personName
"Alice"

// With default values
> const { name, city = "Unknown" } = person
undefined

> city
"Unknown"
```

### Spread operator

Copy and merge objects:

```javascript
> const obj1 = { a: 1, b: 2 }
undefined

> const obj2 = { c: 3, d: 4 }
undefined

// Copy
> const copy = { ...obj1 }
undefined

> copy
{ a: 1, b: 2 }

// Merge
> const merged = { ...obj1, ...obj2 }
undefined

> merged
{ a: 1, b: 2, c: 3, d: 4 }

// Override
> const updated = { ...obj1, b: 3 }
undefined

> updated
{ a: 1, b: 3 }
```

### Iteration

#### `for`...`in` loop

Iterates over all enumerable properties (including inherited ones).

```javascript
> const person = { name: "Alice", age: 30 }
undefined

> for (let key in person) {
...   console.log(key, person[key])
... }
name Alice
age 30
```

#### `Object.keys()` with `forEach`

```javascript
> const person = { name: "Alice", age: 30 }
undefined

> Object.keys(person).forEach(key => {
...   console.log(key, person[key])
... })
name Alice
age 30
```

#### `Object.entries()` with `for`...`of`

```javascript
> const person = { name: "Alice", age: 30 }
undefined

> for (let [key, value] of Object.entries(person)) {
...   console.log(key, value)
... }
name Alice
age 30
```

## Object methods

JavaScript provides two types of object methods:

- **Static methods** (`Object.methodName()`): Called directly on the `Object` constructor. These are utility functions that operate on objects but don't require an instance. Examples: `Object.keys()`, `Object.assign()`, `Object.freeze()`.
- **Instance methods** (`Object.prototype.methodName()`): Available on all object instances. These are called on specific object instances. Examples: `obj.toString()`, `obj.hasOwnProperty()`, `obj.valueOf()`.

The key difference: static methods are called on the `Object` constructor itself, while instance methods are called on individual object instances.

```javascript
// Static method - called on Object constructor
> const obj = { name: "Alice", age: 30 }
undefined

> Object.keys(obj)
["name", "age"]

// Instance method - called on the object instance
> obj.toString()
"[object Object]"

> obj.hasOwnProperty("name")
true
```

---

### `Object.keys()`

Returns an array of a given object's own enumerable property names.

```javascript
> const person = { name: "Alice", age: 30 }
undefined

> Object.keys(person)
["name", "age"]
```

### `Object.values()`

Returns an array of a given object's own enumerable property values.

```javascript
> const person = { name: "Alice", age: 30 }
undefined

> Object.values(person)
["Alice", 30]
```

### `Object.entries()`

Returns an array of a given object's own enumerable string-keyed property [key, value] pairs.

```javascript
> const person = { name: "Alice", age: 30 }
undefined

> Object.entries(person)
[["name", "Alice"], ["age", 30]]
```

### `Object.assign()`

Copies all enumerable own properties from one or more source objects to a target object.

```javascript
> const target = { a: 1 }
undefined

> const source = { b: 2, c: 3 }
undefined

> Object.assign(target, source)
{ a: 1, b: 2, c: 3 }

> target
{ a: 1, b: 2, c: 3 }
```

### `Object.create()`

Creates a new object with the specified prototype object and properties.

```javascript
> const proto = { greet() { return "Hello" } }
undefined

> const obj = Object.create(proto)
undefined

> obj.greet()
"Hello"
```

### `Object.freeze()`

Freezes an object, preventing new properties from being added and existing properties from being modified or deleted.

```javascript
> const obj = { name: "Alice" }
undefined

> Object.freeze(obj)
{ name: "Alice" }

> obj.name = "Bob"
"Bob"

> obj.name
"Alice"

> obj.age = 30
30

> obj.age
undefined
```

### `Object.seal()`

Seals an object, preventing new properties from being added and marking all existing properties as non-configurable. Unlike `Object.freeze()`, sealed objects allow existing properties to be modified, but they cannot be deleted.

```javascript
> const obj = { name: "Alice" }
undefined

> Object.seal(obj)
{ name: "Alice" }

> obj.name = "Bob"
"Bob"

> obj.name
"Bob"

> obj.age = 30
30

> obj.age
undefined

> delete obj.name
false
```

### `Object.is()`

Determines whether two values are the same value. This method compares by reference, not by value, meaning it checks if two values refer to the exact same object or primitive value **in memory**. For objects, this means two objects with identical properties will return `false` unless they are the same object reference.

**Comparison with `==` and `===`**:
- `Object.is()` is similar to `===` (strict equality) for most cases, but differs in two important ways:
  - `Object.is(NaN, NaN)` returns `true`, while `NaN === NaN` returns `false`
  - `Object.is(-0, +0)` returns `false`, while `-0 === +0` returns `true`
- For objects, both `Object.is()` and `===` compare by reference, so they behave the same way
- `==` (loose equality) performs type coercion, which `Object.is()` does not

```javascript
> Object.is(5, 5)
true

> Object.is(NaN, NaN)
true

> Object.is(-0, +0)
false

// With objects, Object.is() compares by reference (like ===)
> const obj1 = { name: "Alice" }
undefined

> const obj2 = { name: "Alice" }
undefined

> Object.is(obj1, obj2)
false

> Object.is(obj1, obj1)
true

// Contrast with == (loose equality)
> obj1 == obj2
false

> obj1 == obj1
true
```

### `Object.hasOwnProperty()`

Returns a boolean indicating whether the object has the specified property as its own property.

```javascript
> const obj = { name: "Alice" }
undefined

> obj.hasOwnProperty("name")
true

> obj.hasOwnProperty("toString")
false
```

### `Object.prototype.toString()`

Returns a string representing the object.

```javascript
> const obj = { name: "Alice" }
undefined

> obj.toString()
"[object Object]"
```

:::note
**Why `"[object Object]"` instead of `"{ name: \"Alice\" }"`?** The default `toString()` method is generic and works for all objects. It doesn't inspect the object's properties—it only returns a string indicating the object's type. To get a detailed representation of an object's properties, use `JSON.stringify()` instead:

```javascript
> JSON.stringify({ name: "Alice" })
'{"name":"Alice"}'
```

You can also override `toString()` in your own objects to provide custom string representations.
:::