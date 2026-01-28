---
title: Function
sidebar_position: 11
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
> Object.getOwnPropertyNames(Function.prototype)
['constructor', 'apply', 'bind', 'call', 'toString', 'name', 'length', Symbol.hasInstance]
``` -->

## Definition

A `Function` is a callable object that executes a block of code. Functions are first-class objects in JavaScript, meaning they can be assigned to variables, passed as arguments, and returned from other functions.

```javascript
> typeof function() {}
"function"
```

## Using functions

### Function Declaration

```javascript
function greet(name) {
  return `Hello, ${name}!`
}
```

### Function Expression

```javascript
const greet = function(name) {
  return `Hello, ${name}!`
}
```

### Arrow Function (ES6+)

```javascript
const greet = (name) => {
  return `Hello, ${name}!`
}

// Shorthand for single expression
const greet = (name) => `Hello, ${name}!`

// Single parameter (no parentheses needed)
const square = x => x * x
```

### Function Constructor

```javascript
const greet = new Function('name', 'return `Hello, ${name}!`')
```

### Function parameters

### Default Parameters

```javascript
function greet(name = "Guest") {
  return `Hello, ${name}!`
}

greet()           // "Hello, Guest!"
greet("Alice")    // "Hello, Alice!"
```

### Rest Parameters

```javascript
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0)
}

sum(1, 2, 3, 4)   // 10
```

### Destructuring Parameters

```javascript
function greet({ name, age }) {
  return `Hello, ${name}, age ${age}!`
}

greet({ name: "Alice", age: 30 })  // "Hello, Alice, age 30!"
```

## Operations on functions

## Function methods

### `call()`

Calls a function with a specified `this` value and arguments provided individually.

```javascript
function greet() {
  return `Hello, ${this.name}!`
}

const person = { name: "Alice" }
greet.call(person)  // "Hello, Alice!"
```

### `apply()`

Calls a function with a specified `this` value and arguments provided as an array.

```javascript
function sum(a, b, c) {
  return a + b + c
}

sum.apply(null, [1, 2, 3])  // 6
```

### `bind()`

Creates a new function with a specified `this` value and initial arguments.

```javascript
function greet() {
  return `Hello, ${this.name}!`
}

const person = { name: "Alice" }
const boundGreet = greet.bind(person)
boundGreet()  // "Hello, Alice!"
```

## Arrow functions vs regular functions

### `this` Binding

Arrow functions don't have their own `this`—they inherit it from the enclosing scope:

```javascript
const obj = {
  name: "Alice",
  regular: function() {
    return this.name  // "Alice" (this refers to obj)
  },
  arrow: () => {
    return this.name  // undefined (this refers to global/window)
  }
}
```

### Arguments Object

Arrow functions don't have their own `arguments` object:

```javascript
function regular() {
  console.log(arguments)  // Arguments object
}

const arrow = () => {
  console.log(arguments)  // ReferenceError
}
```

### Constructor

Arrow functions cannot be used as constructors:

```javascript
const Regular = function() {}
new Regular()  // OK

const Arrow = () => {}
new Arrow()     // TypeError: Arrow is not a constructor
```

## Higher-order functions

Functions that take other functions as arguments or return functions:

```javascript
// Function as argument
function map(arr, fn) {
  return arr.map(fn)
}

// Function as return value
function multiplier(factor) {
  return function(x) {
    return x * factor
  }
}

const double = multiplier(2)
double(5)  // 10
```

## Closures

Functions that have access to variables in their outer scope:

```javascript
function outer() {
  const message = "Hello"
  
  function inner() {
    console.log(message)  // Accesses outer variable
  }
  
  return inner
}

const innerFn = outer()
innerFn()  // "Hello"
```

## Immediately invoked function expression (iife)

Functions that are executed immediately:

```javascript
(function() {
  console.log("IIFE")
})()

// With arrow function
(() => {
  console.log("IIFE")
})()
```

## Generator functions

Functions that can be paused and resumed:

```javascript
function* numbers() {
  yield 1
  yield 2
  yield 3
}

const gen = numbers()
gen.next()  // { value: 1, done: false }
gen.next()  // { value: 2, done: false }
gen.next()  // { value: 3, done: false }
gen.next()  // { value: undefined, done: true }
```

## Async functions

Functions that return Promises:

```javascript
async function fetchData() {
  const response = await fetch('/api/data')
  return response.json()
}
```

### Function properties

### `name`

The name of the function:

```javascript
function greet() {}
greet.name  // "greet"

const anonymous = function() {}
anonymous.name  // "anonymous"
```

### `length`

The number of parameters:

```javascript
function example(a, b, c) {}
example.length  // 3
```

## Best practices

1. **Use arrow functions for callbacks**: Cleaner syntax for `map()`, `filter()`, etc.

2. **Use function declarations for hoisting**: Function declarations are hoisted, expressions are not.

3. **Be consistent with `this`**: Understand when to use arrow functions vs regular functions based on `this` binding needs.

4. **Use default parameters**: Instead of checking for `undefined` inside the function.

5. **Use rest parameters**: For functions that accept variable numbers of arguments.

