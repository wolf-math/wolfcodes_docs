---
title: Generator
sidebar_position: 22
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

A generator is a special type of function that can be paused and resumed. Generators are created using the `function*` syntax and use the `yield` keyword to produce values.

```javascript
function* generator() {
  yield 1
  yield 2
  yield 3
}
```

## Creating generators

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

## Generator methods

### `next()`

Advances the generator and returns the next value:

```javascript
function* counter() {
  let count = 0
  while (true) {
    yield count++
  }
}

const gen = counter()
gen.next()  // { value: 0, done: false }
gen.next()  // { value: 1, done: false }
gen.next()  // { value: 2, done: false }
```

### `return()`

Terminates the generator:

```javascript
function* numbers() {
  yield 1
  yield 2
  yield 3
}

const gen = numbers()
gen.return(10)  // { value: 10, done: true }
gen.next()     // { value: undefined, done: true }
```

### `throw()`

Throws an error into the generator:

```javascript
function* numbers() {
  try {
    yield 1
  } catch (error) {
    console.error(error)
  }
}

const gen = numbers()
gen.next()        // { value: 1, done: false }
gen.throw(new Error('Failed'))  // Error handled in generator
```

## Iterating generators

### `for...of` Loop

```javascript
function* numbers() {
  yield 1
  yield 2
  yield 3
}

for (const num of numbers()) {
  console.log(num)
}
// 1
// 2
// 3
```

### Spread Operator

```javascript
function* numbers() {
  yield 1
  yield 2
  yield 3
}

[...numbers()]  // [1, 2, 3]
```

## Generator functions

### Yielding Values

```javascript
function* generator() {
  yield 1
  yield 2
  return 3  // Final value
}
```

### Yielding from Another Generator

```javascript
function* generator1() {
  yield 1
  yield 2
}

function* generator2() {
  yield* generator1()  // Delegates to generator1
  yield 3
}

[...generator2()]  // [1, 2, 3]
```

### Passing Values to Generators

```javascript
function* generator() {
  const x = yield 1
  const y = yield x + 2
  return y
}

const gen = generator()
gen.next()      // { value: 1, done: false }
gen.next(10)    // { value: 12, done: false } (x = 10)
gen.next(20)    // { value: 20, done: true } (y = 20)
```

## Use cases

### Infinite Sequences

```javascript
function* fibonacci() {
  let [prev, curr] = [0, 1]
  while (true) {
    yield curr
    [prev, curr] = [curr, prev + curr]
  }
}

const fib = fibonacci()
fib.next().value  // 1
fib.next().value  // 1
fib.next().value  // 2
fib.next().value  // 3
```

### Lazy Evaluation

```javascript
function* range(start, end) {
  for (let i = start; i < end; i++) {
    yield i
  }
}

const numbers = range(0, 1000000)  // Doesn't create array
numbers.next()  // { value: 0, done: false }
```

### State Machines

```javascript
function* stateMachine() {
  yield 'start'
  yield 'processing'
  yield 'complete'
}

const machine = stateMachine()
machine.next().value  // 'start'
machine.next().value  // 'processing'
machine.next().value  // 'complete'
```

## Async generators

Generators can be used with async/await:

```javascript
async function* asyncGenerator() {
  yield await fetch('/api/data1')
  yield await fetch('/api/data2')
  yield await fetch('/api/data3')
}

for await (const data of asyncGenerator()) {
  console.log(data)
}
```

## Best practices

1. **Use for lazy sequences**: When you need to generate values on demand.

2. **Use for state machines**: When you need to manage state across multiple calls.

3. **Use async generators**: For streaming data or handling async sequences.

4. **Understand iteration**: Generators are iterable and work with `for...of`.

5. **Be aware of memory**: Generators can be more memory-efficient than arrays for large sequences.

