---
title: Callbacks (Historical Context)
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

:::warning **Don't use callbacks in new code**
Callbacks are an **old way** of handling async operations. They still exist in older code and some APIs, but you should **never write new code using callbacks**. Use [promises](./promises) and [async/await](./async_await) instead.

This section exists only so you can **recognize callbacks** when you see them in older code.
:::

## What are callbacks?

A **callback** is a function passed to another function to be called later, usually after an async operation completes.

```javascript
// setTimeout takes a callback function
setTimeout(function() {
  console.log("This runs after 1 second");
}, 1000);
```

The function you pass to `setTimeout` is a callback. It gets called after the delay.

## Why callbacks are problematic

Callbacks work, but they create serious problems when you need to chain multiple async operations:

### Callback hell

When you need to do multiple async operations in sequence, callbacks create deeply nested code:

```javascript
// Callback hell - hard to read and maintain!
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

This is called "callback hell" or "the pyramid of doom." It's:
- **Hard to read** — nested functions are confusing
- **Hard to debug** — errors can happen at any level
- **Hard to maintain** — adding or removing steps is painful

### Error handling is messy

With callbacks, error handling often requires checking errors at every level:

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

## Why you shouldn't use callbacks

**Modern JavaScript has better solutions:**

1. **Promises** — Cleaner chaining with `.then()` and `.catch()`
2. **async/await** — Makes async code read like synchronous code

Both solve callback hell and make error handling straightforward.

## When you'll see callbacks

You might encounter callbacks in:
- **Older codebases** — written before promises were widely adopted
- **Some Node.js APIs** — older APIs like `fs.readFile()` (though modern versions support promises)
- **Legacy libraries** — older third-party code

If you see callbacks, you can usually wrap them in promises:

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

- Callbacks are **old** and should **not be used** in new code
- They create "callback hell" with deeply nested functions
- Error handling is messy and repetitive
- Use [promises](./promises) and [async/await](./async_await) instead
- Learn to recognize callbacks so you can understand older code
