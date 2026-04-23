---
title: Async Callbacks (Historical Context)
sidebar_position: 2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

:::warning Callback-based async code is mostly historical
Callbacks are still a normal JavaScript function pattern. You will use them with array methods, event listeners, timers, and custom helper functions.

This page is specifically about **callback-based asynchronous code**, which is an older way to organize async operations. For new async code, prefer [promises](./promises) and [`async` / `await`](./async_await).

For the general function concept, see the [callback functions guide](../functions/callbacks).
:::

## What are async callbacks?

An **async callback** is a function passed to an async operation so it can be called later, after the operation finishes.

```javascript
// setTimeout takes a callback function
setTimeout(function () {
  console.log("This runs later");
}, 1000);

console.log("This runs now");
```

The function you pass to `setTimeout` is a callback. It gets called after the delay.

**Output:**

```text
This runs now
This runs later
```

**What happens:**

1. `setTimeout(...)` schedules work to happen later.
2. The program keeps going and logs `"This runs now"`.
3. The callback runs after the delay and logs `"This runs later"`.

## Why async callbacks are problematic

Callback-based async code works, but it creates serious problems when you need to chain multiple async operations:

### Callback hell

When you need to do multiple async operations in sequence, async callbacks create deeply nested code:

```javascript
// Callback hell: hard to read and maintain
fetchUser(userId, function(user) {
  fetchPosts(user.id, function(posts) {
    fetchComments(posts[0].id, function(comments) {
      updateUI(comments, function() {
        console.log("Done!");  // 4 levels deep!
      });
    });
  });
});
```

This is called "callback hell" or "the pyramid of doom."

It is:

- **Hard to read**: nested functions are confusing
- **Hard to debug**: errors can happen at any level
- **Hard to maintain**: adding or removing steps is painful

:::note
The functions in the example (`fetchUser`, `fetchPosts`, etc.) are placeholders to show the structure. The point is how nesting grows when each async step depends on the previous one.
:::

### Error handling is messy

With async callbacks, error handling often requires checking errors at every level:

```javascript
fetchUser(userId, function(error, user) {
  if (error) {
    console.error("Error fetching user:", error);
    return;
  }
  fetchPosts(user.id, function(error, posts) {
    if (error) {
      console.error("Error fetching posts:", error);
      return;
    }
    // More nesting...
  });
});
```

This pattern repeats at every level, making code verbose and error-prone.

## A common historical pattern: Node-style callbacks

Older Node.js APIs often used an "error-first" callback style:

```javascript
function readConfig(callback) {
  setTimeout(() => {
    callback(null, { debug: true });
  }, 50);
}

readConfig((error, config) => {
  if (error) {
    console.log("Failed to read config");
    return;
  }

  console.log(config.debug); // true
});
```

The first callback argument is the error (or `null` when successful). The second argument is the successful result.

## Why you should avoid async callbacks in new code

**Modern JavaScript has better solutions:**

1. **Promises**: Cleaner chaining with `.then()` and `.catch()`
2. **async/await**: Makes async code read like synchronous code

Both solve callback hell and make error handling straightforward.

## When you'll see async callbacks

You might encounter callback-based async code in:
- **Older codebases**: written before promises were widely adopted
- **Some Node.js APIs**: older APIs like `fs.readFile()` though modern versions support promises
- **Legacy libraries**: older third-party code

If you see async callbacks, you can usually wrap them in promises:

```javascript
// Old callback API
function oldAPI(callback) {
  setTimeout(() => {
    callback(null, "data");
  }, 1000);
}

// Wrap it in a promise
function newAPI() {
  return new Promise((resolve, reject) => {
    oldAPI((error, data) => {
      if (error) reject(error);
      else resolve(data);
    });
  });
}

// Now use it with async/await
async function useIt() {
  const data = await newAPI();
  console.log(data);
}
```

## Summary

- Callbacks are still a normal function pattern in JavaScript.
- Callback-based async code is the older async style this page is warning about.
- Async callbacks can create "callback hell" with deeply nested functions.
- Error handling in callback-based async code is messy and repetitive.
- Use [promises](./promises) and [`async` / `await`](./async_await) for new async code.
- Learn to recognize async callbacks so you can understand older code.
