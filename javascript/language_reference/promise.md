---
title: Promise
sidebar_position: 18
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

A `Promise` is an object representing the eventual completion or failure of an asynchronous operation. Promises provide a cleaner way to handle asynchronous code compared to callbacks.

```javascript
const promise = new Promise((resolve, reject) => {})
promise instanceof Promise  // true
```

## Creating promises

```javascript
// Basic promise
const promise = new Promise((resolve, reject) => {
  // Asynchronous operation
  if (success) {
    resolve(value)
  } else {
    reject(error)
  }
})
```

## Promise states

A Promise has three states:

1. **Pending**: Initial state, neither fulfilled nor rejected
2. **Fulfilled**: Operation completed successfully
3. **Rejected**: Operation failed

## Using promises

### `then()` and `catch()`

```javascript
const promise = fetch('/api/data')

promise
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error))
```

### Chaining

```javascript
fetch('/api/data')
  .then(response => response.json())
  .then(data => processData(data))
  .then(result => saveResult(result))
  .catch(error => handleError(error))
```

## Promise methods

### `Promise.resolve()`

Creates a resolved promise:

```javascript
Promise.resolve(42)
  .then(value => console.log(value))  // 42
```

### `Promise.reject()`

Creates a rejected promise:

```javascript
Promise.reject(new Error('Failed'))
  .catch(error => console.error(error))  // Error: Failed
```

### `Promise.all()`

Waits for all promises to resolve:

```javascript
const p1 = Promise.resolve(1)
const p2 = Promise.resolve(2)
const p3 = Promise.resolve(3)

Promise.all([p1, p2, p3])
  .then(values => console.log(values))  // [1, 2, 3]
```

If any promise rejects, `Promise.all()` rejects:

```javascript
const p1 = Promise.resolve(1)
const p2 = Promise.reject(new Error('Failed'))
const p3 = Promise.resolve(3)

Promise.all([p1, p2, p3])
  .catch(error => console.error(error))  // Error: Failed
```

### `Promise.allSettled()`

Waits for all promises to settle (resolve or reject):

```javascript
const p1 = Promise.resolve(1)
const p2 = Promise.reject(new Error('Failed'))
const p3 = Promise.resolve(3)

Promise.allSettled([p1, p2, p3])
  .then(results => {
    // [
    //   { status: 'fulfilled', value: 1 },
    //   { status: 'rejected', reason: Error },
    //   { status: 'fulfilled', value: 3 }
    // ]
  })
```

### `Promise.race()`

Returns the first settled promise:

```javascript
const p1 = new Promise(resolve => setTimeout(() => resolve(1), 100))
const p2 = new Promise(resolve => setTimeout(() => resolve(2), 50))

Promise.race([p1, p2])
  .then(value => console.log(value))  // 2 (faster)
```

### `Promise.any()`

Returns the first fulfilled promise:

```javascript
const p1 = Promise.reject(new Error('Failed'))
const p2 = Promise.resolve(2)
const p3 = Promise.resolve(3)

Promise.any([p1, p2, p3])
  .then(value => console.log(value))  // 2
```

## `async`/`await`

Syntactic sugar for working with promises:

```javascript
async function fetchData() {
  try {
    const response = await fetch('/api/data')
    const data = await response.json()
    return data
  } catch (error) {
    console.error(error)
  }
}
```

## Common patterns

### Timeout

```javascript
function timeout(ms) {
  return new Promise((_, reject) => {
    setTimeout(() => reject(new Error('Timeout')), ms)
  })
}

Promise.race([fetch('/api/data'), timeout(5000)])
  .then(data => console.log(data))
  .catch(error => console.error(error))
```

### Retry

```javascript
function retry(fn, retries = 3) {
  return fn().catch(error => {
    if (retries > 0) {
      return retry(fn, retries - 1)
    }
    throw error
  })
}
```

### Sequential Execution

```javascript
async function sequential() {
  const result1 = await operation1()
  const result2 = await operation2(result1)
  const result3 = await operation3(result2)
  return result3
}
```

## Best practices

1. **Always handle errors**: Use `.catch()` or `try/catch` with async/await.

2. **Avoid promise hell**: Use async/await for cleaner code.

3. **Use Promise.all() for parallel operations**: When operations don't depend on each other.

4. **Don't forget to return**: In promise chains, return values to pass them along.

5. **Handle both success and failure**: Always provide error handling.

