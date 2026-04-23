---
title: Promises
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is a promise?

**Promises** represent values that will be available in the future (or an error if something goes wrong).

A promise is an object that represents the eventual result of an async operation. It can be in one of three states:

1. **Pending** — operation hasn't completed yet
2. **Fulfilled** — operation succeeded (resolved with a value)
3. **Rejected** — operation failed (rejected with an error)

Once a promise is fulfilled or rejected, it's "settled" and cannot change.

```javascript
const promise = Promise.resolve("Hello");

promise.then(value => {
  console.log(value); // "Hello"
});
```

## Why promises are better than callbacks

Promises solve the problems with callbacks:

- **No callback hell** — chain operations with `.then()` instead of nesting
- **Better error handling** — use `.catch()` for all errors
- **Easier to read** — code flows top to bottom
- **Easier to debug** — clearer error messages

This page focuses on `.then()` / `.catch()` chaining. Many projects use `async` / `await` on top of promises for readability.

## Creating promises

You can create a promise with `new Promise()`:

```javascript
const promise = new Promise((resolve, reject) => {
  // Do some async work
  setTimeout(() => {
    resolve("Success!");  // Promise succeeds
  }, 1000);
});
```

The function you pass to `Promise` receives two functions:
- `resolve(value)` — call this when the operation succeeds
- `reject(error)` — call this when the operation fails

:::warning
You usually do not need `new Promise(...)` in everyday code. Most promise-based APIs already return promises (like `fetch()` in the browser).
:::

## Using promises

Use `.then()` to handle success and `.catch()` to handle errors:

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Data received");
  }, 1000);
});

promise
  .then(data => {
    console.log(data);  // "Data received" (runs when promise resolves)
  })
  .catch(error => {
    console.error(error);  // Runs if promise rejects
  });
```

### How `.then()` works

`.then()` returns a **new promise**, which lets you chain operations:

```javascript
promise
  .then(data => {
    console.log("First:", data);
    return "Processed " + data;  // Return value becomes next promise's value
  })
  .then(processed => {
    console.log("Second:", processed);  // "Processed Data received"
  });
```

If you return a promise from `.then(...)`, the next `.then(...)` waits for it:

```javascript
Promise.resolve(2)
  .then(value => Promise.resolve(value * 3))
  .then(result => {
    console.log(result); // 6
  });
```

## Chaining promises

You can chain multiple async operations without nesting:

```javascript
// Example async APIs:
fetchUser(userId)
  .then(user => {
    return fetchPosts(user.id);  // Return a promise
  })
  .then(posts => {
    return fetchComments(posts[0].id);  // Return another promise
  })
  .then(comments => {
    console.log(comments);
  })
  .catch(error => {
    console.error("Something went wrong:", error);  // One catch for all errors
  });
```

:::note
The functions in the example (`fetchUser`, `fetchPosts`, `fetchComments`) are placeholders to show chaining structure.
:::

### Shorter chaining syntax

You can make it even shorter by returning promises directly:

```javascript
fetchUser(userId)
  .then(user => fetchPosts(user.id))      // Return promise directly
  .then(posts => fetchComments(posts[0].id))
  .then(comments => console.log(comments))
  .catch(error => console.error(error));
```

## Error handling

### Single `.catch()` for all errors

One of the best features of promises: a single `.catch()` handles errors from **anywhere** in the chain:

```javascript
fetchUser(userId)
  .then(user => fetchPosts(user.id))
  .then(posts => fetchComments(posts[0].id))
  .then(comments => console.log(comments))
  .catch(error => {
    // This catches errors from ANY step in the chain!
    console.error("Error:", error);
  });
```

If `fetchUser`, `fetchPosts`, or `fetchComments` fails, the error goes to `.catch()`.

### Throwing errors

You can throw errors in `.then()` handlers, and they'll be caught by `.catch()`:

```javascript
fetchUser(userId)
  .then(user => {
    if (!user) {
      throw new Error("User not found");  // Throws error
    }
    return fetchPosts(user.id);
  })
  .catch(error => {
    console.error(error);  // Catches the thrown error
  });
```

## Common mistakes

### Forgetting to return a promise in a chain

If you start an async step inside `.then(...)` but forget to return it, the outer chain will not wait.

```javascript
fetchUser(userId)
  .then(user => {
    fetchPosts(user.id); // Missing `return`
  })
  .then(() => {
    console.log("This runs too early");
  });
```

Return the promise so the chain waits:

```javascript
fetchUser(userId)
  .then(user => {
    return fetchPosts(user.id);
  })
  .then(posts => {
    console.log(posts);
  });
```

### Starting a promise and never handling rejection

Promises that reject without a `.catch()` can cause confusing warnings and failures.

```javascript
Promise.reject(new Error("Boom"));

// Add a catch to handle it:
Promise.reject(new Error("Boom")).catch(error => {
  console.log(error.message); // "Boom"
});
```

## Promise methods

### `Promise.all()` — wait for all promises

Use `Promise.all()` when you need to wait for multiple promises to complete:

```javascript
const promise1 = fetchUser(1);
const promise2 = fetchUser(2);
const promise3 = fetchUser(3);

Promise.all([promise1, promise2, promise3])
  .then(users => {
    // All promises resolved
    console.log(users);  // [user1, user2, user3]
  })
  .catch(error => {
    // If ANY promise rejects, this runs
    console.error("One failed:", error);
  });
```

**Important:** If any promise rejects, `Promise.all()` rejects immediately.

### `Promise.allSettled()` — wait for all, even if some fail

Use `Promise.allSettled()` when you want to wait for all promises, even if some fail:

```javascript
Promise.allSettled([promise1, promise2, promise3])
  .then(results => {
    // All promises settled (fulfilled or rejected)
    results.forEach((result, index) => {
      if (result.status === 'fulfilled') {
        console.log(`Promise ${index} succeeded:`, result.value);
      } else {
        console.log(`Promise ${index} failed:`, result.reason);
      }
    });
  });
```

### `Promise.race()` — wait for first to complete

Use `Promise.race()` when you want the first promise that completes (fulfilled or rejected):

```javascript
Promise.race([slowPromise, fastPromise])
  .then(result => {
    // Whichever completes first
    console.log(result);
  });
```

## Converting callbacks to promises

Many older APIs use callbacks, but you can wrap them in promises:

```javascript
// Old callback API
function delay(callback, ms) {
  setTimeout(callback, ms);
}

// Wrap it in a promise
function delayPromise(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms);
  });
}

// Now use it
delayPromise(1000)
  .then(() => {
    console.log("Waited 1 second!");
  });
```

## Common promise patterns

### Creating resolved/rejected promises

Sometimes you need to create a promise that's already resolved or rejected:

```javascript
// Already resolved
const resolved = Promise.resolve("value");

// Already rejected
const rejected = Promise.reject(new Error("Something went wrong"));
```

This is useful when you need to return a promise but already have the value.

## Summary

- Promises represent future values and have three states: pending, fulfilled, rejected
- Use `.then()` to handle success and `.catch()` for errors
- Chain promises to avoid callback hell
- One `.catch()` handles errors from anywhere in the chain
- `Promise.all()` waits for all promises; `Promise.race()` waits for the first
- Many codebases use [`async` / `await`](./async_await) on top of promises for readability
