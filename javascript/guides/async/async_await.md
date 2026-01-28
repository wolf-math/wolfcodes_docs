---
title: Async/await
sidebar_position: 4
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

**`async/await`** is syntactic sugar over [promises](./promises) that makes async code look like synchronous code. It's the **modern, preferred way** to write async JavaScript.

## Why `async`/`await`?

`async`/`await` makes async code:
- **Easier to read** — looks like regular code
- **Easier to write** — no `.then()` chains
- **Easier to debug** — standard error handling with `try/catch`
- **Easier to understand** — flows top to bottom

## `async` Functions

An `async` function always returns a promise:

```javascript
async function fetchData() {
  return "Data";
}

// Equivalent to:
function fetchData() {
  return Promise.resolve("Data");
}
```

Even if you return a regular value, it gets wrapped in a promise automatically.

### Calling async functions

Since async functions return promises, you can use them with `.then()`:

```javascript
async function getData() {
  return "Hello";
}

getData()
  .then(data => {
    console.log(data);  // "Hello"
  });
```

But you'll usually use `await` instead (see below).

## The `await` keyword

Use `await` to wait for a promise to resolve. It **pauses** the function execution until the promise settles, then returns the value.

```javascript
async function getUser() {
  const user = await fetchUser(userId);  // Wait for promise to resolve
  console.log(user);  // This runs AFTER fetchUser completes
}
```

Without `await`, you'd get a promise object. With `await`, you get the actual value.

### `await` only works in `async` functions

You can only use `await` inside an `async` function:

```javascript
// ✅ Good
async function example() {
  const data = await fetchData();
}

// ❌ Error - can't use await here
function example() {
  const data = await fetchData();  // SyntaxError!
}
```

## Chaining with `async`/`await`

Compare promises vs `async`/`await` for chaining operations:

**With promises:**
```javascript
fetchUser(userId)
  .then(user => fetchPosts(user.id))
  .then(posts => fetchComments(posts[0].id))
  .then(comments => console.log(comments))
  .catch(error => console.error(error));
```

**With `async`/`await`:**
```javascript
async function getComments() {
  const user = await fetchUser(userId);
  const posts = await fetchPosts(user.id);
  const comments = await fetchComments(posts[0].id);
  console.log(comments);
}
```

Much cleaner! It reads like synchronous code.

## Error handling

Use `try/catch` with async/await—the same error handling you already know:

```javascript
async function fetchData() {
  try {
    const data = await fetchFromServer();
    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
}
```

This is much cleaner than promise chains with `.catch()`.

### Handling errors in promise chains

If you mix promises and async/await, you can still use `.catch()`:

```javascript
async function example() {
  try {
    const data = await fetchData()
      .catch(error => {
        console.error("Fetch failed:", error);
        return null;  // Return default value
      });
    
    if (data) {
      console.log(data);
    }
  } catch (error) {
    console.error("Other error:", error);
  }
}
```

But `try/catch` is usually simpler.

## Common patterns

### Sequential operations

Run operations one after another (each waits for the previous):

```javascript
async function sequential() {
  const user = await fetchUser(id);
  const posts = await fetchPosts(user.id);
  const comments = await fetchComments(posts[0].id);
  return comments;
}
```

### Parallel operations

Run multiple operations simultaneously using `Promise.all()`:

```javascript
async function parallel() {
  const [user, posts, settings] = await Promise.all([
    fetchUser(id),
    fetchPosts(id),
    fetchSettings(id)
  ]);
  return { user, posts, settings };
}
```

All three fetches happen at the same time, then you wait for all to complete. Learn more about using [`fetch`](/docs/javascript/web/browser_api/networking) for HTTP requests.

### Looping with async

Process items one at a time:

```javascript
async function processItems(items) {
  for (const item of items) {
    await processItem(item);  // Wait for each item
  }
}
```

Or process all items in parallel:

```javascript
async function processItemsParallel(items) {
  await Promise.all(items.map(item => processItem(item)));
}
```

## Converting callback code to async/await

Many older APIs use callbacks, but you can wrap them in promises, then use async/await:

```javascript
// Old callback API
function delay(callback, ms) {
  setTimeout(callback, ms);
}

// Wrap in promise
function delayPromise(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms);
  });
}

// Now use with async/await
async function doSomething() {
  await delayPromise(1000);  // Wait 1 second
  console.log("Done waiting!");
}
```

## Real-world example

Here's a practical example combining everything:

```javascript
async function getUserProfile(userId) {
  try {
    // Fetch data in parallel
    const [user, posts] = await Promise.all([
      fetch(`/api/users/${userId}`).then(r => r.json()),
      fetch(`/api/users/${userId}/posts`).then(r => r.json())
    ]);

    // Process posts
    const postCount = posts.length;
    const recentPosts = posts.slice(0, 5);

    return {
      user,
      postCount,
      recentPosts
    };
  } catch (error) {
    console.error("Failed to fetch profile:", error);
    throw error;  // Re-throw to let caller handle
  }
}

// Usage
try {
  const profile = await getUserProfile(123);
  console.log(profile);
} catch (error) {
  console.error("Error loading profile:", error);
}
```

## Common mistakes

### Forgetting `await`

```javascript
// ❌ Wrong - returns a promise, not the value
async function example() {
  const data = fetchData();  // Missing await!
  console.log(data);  // Promise object, not the data
}

// ✅ Correct
async function example() {
  const data = await fetchData();
  console.log(data);  // Actual data
}
```

### Forgetting `async`

```javascript
// ❌ Wrong - can't use await without async
function example() {
  const data = await fetchData();  // SyntaxError!
}

// ✅ Correct
async function example() {
  const data = await fetchData();
}
```

### Not handling errors

```javascript
// ❌ Bad - unhandled rejection
async function badExample() {
  await failingPromise();  // Error not caught!
}

// ✅ Good - handle errors
async function goodExample() {
  try {
    await failingPromise();
  } catch (error) {
    console.error("Handled:", error);
  }
}
```

## Summary

- `async` functions always return promises
- `await` pauses execution until a promise resolves
- Use `try/catch` for error handling (same as synchronous code)
- Chain operations naturally—no `.then()` needed
- Use `Promise.all()` for parallel operations
- Async/await is the **preferred way** to write async JavaScript

**You now know modern async JavaScript!** Use async/await for all new code.
