---
title: Async/await
sidebar_position: 21
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

`async` and `await` are keywords that provide syntactic sugar for working with Promises. They make asynchronous code look and behave more like synchronous code.

```javascript
async function example() {
  const result = await somePromise()
  return result
}
```

## Async functions

An `async` function always returns a Promise:

```javascript
async function example() {
  return 42
}

example()  // Returns Promise<42>
```

Even if you return a non-Promise value, it's wrapped in a Promise:

```javascript
async function example() {
  return 'hello'
}

example().then(value => console.log(value))  // "hello"
```

## Await

The `await` keyword pauses execution until a Promise settles:

```javascript
async function fetchData() {
  const response = await fetch('/api/data')
  const data = await response.json()
  return data
}
```

## Error handling

### `try`/`catch`

```javascript
async function fetchData() {
  try {
    const response = await fetch('/api/data')
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error:', error)
    throw error
  }
}
```

### Catching Rejected Promises

```javascript
async function example() {
  try {
    await Promise.reject(new Error('Failed'))
  } catch (error) {
    console.error(error)  // Error: Failed
  }
}
```

## Parallel execution

### `Promise.all()` with await

```javascript
async function fetchAll() {
  const [data1, data2, data3] = await Promise.all([
    fetch('/api/data1'),
    fetch('/api/data2'),
    fetch('/api/data3')
  ])
  return [data1, data2, data3]
}
```

### Sequential vs Parallel

```javascript
// Sequential (slower)
async function sequential() {
  const a = await fetch('/api/a')
  const b = await fetch('/api/b')
  const c = await fetch('/api/c')
}

// Parallel (faster)
async function parallel() {
  const [a, b, c] = await Promise.all([
    fetch('/api/a'),
    fetch('/api/b'),
    fetch('/api/c')
  ])
}
```

## Common patterns

### Async Arrow Functions

```javascript
const fetchData = async () => {
  const response = await fetch('/api/data')
  return response.json()
}
```

### Async IIFE

```javascript
(async () => {
  const data = await fetchData()
  console.log(data)
})()
```

### Async Methods

```javascript
class DataFetcher {
  async fetch() {
    const response = await fetch('/api/data')
    return response.json()
  }
}
```

## Best practices

1. **Always use try/catch**: Handle errors in async functions.

2. **Use Promise.all() for parallel operations**: Don't await sequentially when operations are independent.

3. **Don't forget await**: Missing `await` returns a Promise instead of the value.

4. **Use async/await over .then()**: Cleaner and easier to read.

5. **Handle both success and failure**: Always provide error handling.

