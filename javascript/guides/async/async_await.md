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

## What is `async` / `await`?

**`async` / `await`** is syntax for working with [promises](./promises) that lets async code read more like top-to-bottom code.

```javascript
function wait(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms);
  });
}

async function example() {
  console.log("Start");
  await wait(10);
  console.log("End");
}

example();
```

## Why `async` / `await`?

`async` / `await` is popular because it:

- Reads like normal control flow (`try/catch`, `if`, `for`)
- Avoids deeply nested callbacks
- Avoids long `.then(...)` chains in many cases

## `async` functions

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
    console.log(data); // "Hello"
  });
```

But you'll usually use `await` instead (see below).

## The `await` keyword

Use `await` to wait for a promise to settle. It pauses the current `async` function until the promise resolves (or rejects), then gives you the resolved value (or throws the rejection error).

```javascript
async function getUser() {
  // Example async API:
  const user = await fetchUser(userId);
  console.log(user);
}
```

Without `await`, you'd get a promise object. With `await`, you get the actual value.

### `await` only works in `async` functions

You can only use `await` inside an `async` function:

```javascript
// Good
async function example() {
  const data = await fetchData();
}

// Error - can't use await here
function example() {
  const data = await fetchData();  // SyntaxError!
}
```

:::note
Some environments also support top-level `await` in modules. As a beginner default, use `await` inside an `async` function.
:::

## Chaining with `async`/`await`

Compare promises vs `async`/`await` for chaining operations:

**With promises:**
```javascript
// Example async APIs:
fetchUser(userId)
  .then(user => fetchPosts(user.id))
  .then(posts => fetchComments(posts[0].id))
  .then(comments => console.log(comments))
  .catch(error => console.error(error));
```

**With `async`/`await`:**
```javascript
async function getComments() {
  // Example async APIs:
  const user = await fetchUser(userId);
  const posts = await fetchPosts(user.id);
  const comments = await fetchComments(posts[0].id);
  console.log(comments);
}
```

:::note
The functions in these examples (`fetchUser`, `fetchPosts`, `fetchComments`) are placeholders to show how chaining works.
:::

## Error handling

Use `try/catch` with `async` / `await`:

```javascript
async function fetchData() {
  try {
    // Example async API:
    const data = await fetchFromServer();
    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
}
```

This works because `await` turns a rejected promise into a thrown error.

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
  // Example async APIs:
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
    // Example async APIs:
    fetchUser(id),
    fetchPosts(id),
    fetchSettings(id)
  ]);
  return { user, posts, settings };
}
```

All three operations start immediately, then you wait for all of them to complete.

**Rule of thumb:** use `await` for sequential steps, and `Promise.all(...)` for independent work you can do in parallel.

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

Be careful with parallel loops if the list can be very large. Starting thousands of async operations at once can overload the system.

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
      fetch(`/api/users/${userId}/posts`).then(r => r.json()),
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
async function run() {
  try {
    const profile = await getUserProfile(123);
    console.log(profile);
  } catch (error) {
    console.error("Error loading profile:", error);
  }
}

run();
```

## Common mistakes

### Forgetting `await`

```javascript
// Wrong - returns a promise, not the value
async function example() {
  const data = fetchData();  // Missing await!
  console.log(data);  // Promise object, not the data
}

// Correct
async function example() {
  const data = await fetchData();
  console.log(data);  // Actual data
}
```

### Forgetting `async`

```javascript
// Wrong - can't use await without async
function example() {
  const data = await fetchData();  // SyntaxError!
}

// Correct
async function example() {
  const data = await fetchData();
}
```

### Awaiting independent work sequentially

If two async operations do not depend on each other, awaiting them one-by-one is slower than waiting in parallel:

```javascript
// Slower: runs one after the other
const user = await fetchUser(id);
const settings = await fetchSettings(id);
```

```javascript
// Faster: start both, then await both
const [user, settings] = await Promise.all([fetchUser(id), fetchSettings(id)]);
```

### Not handling errors

```javascript
// Bad - unhandled rejection
async function badExample() {
  await failingPromise();  // Error not caught!
}

// Good - handle errors
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
- `async` / `await` is the most common way to write promise-based code
