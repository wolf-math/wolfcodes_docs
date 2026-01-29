---
slug: async-await
title: "async/await"
authors: Aaron Wolf
sidebar_position: 1
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---


`async` / `await` is a newer way of writing asynchronous code compared to promises. The main advantages of `async`/`await` are improved readability and the avoidance of _promise chaining_. Promises can become long, hard to read, and may contain deeply nested callbacks that can be difficult to debug.

## Example

Recall our fetch from before.

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error))
  .finally(() => console.log('All done'));
```

Using `async`/`await`, the code can be refactored to look like this:

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  } finally {
    console.log('All done');
  }
}

fetchData();
```

While it may be a few more lines of code, this version is easier to read because it resembles a normal synchronous function. Additionally, if the functions inside the `.then()` statements were more complex, readability and debuggability would be even more impacted. The `async`/`await` example is far clearer.

---

## **Example 2: Sequencing multiple async operations**

Let’s say we have three async functions:

```js
async function getUser(id) {
  const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
  return res.json();
}

async function getPosts(userId) {
  const res = await fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`);
  return res.json();
}

async function getComments(postId) {
  const res = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${postId}`);
  return res.json();
}
```

We want to:

1. Get a user
2. Get that user’s posts
3. Get comments for the first post

```js
async function loadUserActivity(userId) {
  try {
    const user = await getUser(userId);
    const posts = await getPosts(user.id);

    const latest = posts[0];
    const comments = await getComments(latest.id);

    return {
      user,
      latestPost: latest,
      comments
    };
  } catch (err) {
    console.error("Error loading activity:", err);
  }
}
```


```js
const activity = await loadUserActivity(1);
console.log(activity);
```

This shows how async/await handles **dependent** operations cleanly and clearly.

---

### **Example 3: Running async operations in parallel (`promise.all`)**

When two tasks do **not** depend on each other, run them together.

Instead of:

```js
const comments = await getComments(postId);
const likes = await getLikes(postId);
```

…which takes **twice as long**, use:

```js
const [comments, likes] = await Promise.all([
  getComments(postId),
  getLikes(postId)
]);
```

**Full example**

```js
async function getPostActivity(postId) {
  try {
    const [comments, likes] = await Promise.all([
      getComments(postId),
      getLikes(postId)
    ]);

    return { comments, likes };
  } catch (err) {
    console.error("Error loading post activity:", err);
    return null;
  }
}
```

Parallelism is one of the biggest advantages of Promises and async/await lets you use it cleanly without chaining.

---

## **Example 4: `async`/`await` in loops**

`async`/`await` does **not** work the way most people expect with `.forEach()`.

**Avoid:**

```js
ids.forEach(async id => {
  await doSomething(id);
});
```

This does **not** wait. The loop finishes immediately.

**Correct (sequential):**

```js
for (const id of ids) {
  await doSomething(id);
}
```

This ensures each operation finishes before the next begins.

**Correct (parallel):**

```js
await Promise.all(ids.map(id => doSomething(id)));
```

This runs all tasks simultaneously — ideal when operations don’t depend on each other.

---

## **Example 5: Handling delays (the *only* good use of `new Promise`)**

You should almost never write `new Promise()` yourself when using async/await.

The one valid exception is creating intentional delays:

```js
const wait = ms => new Promise(resolve => setTimeout(resolve, ms));

// Usage:
async function demo() {
  console.log("Start");
  await wait(1000);
  console.log("1 second later");
}
```

This is clean, predictable, and common in real-world async workflows (retry logic, animations, rate limiting, etc.).

---

## **Example 6: A complete real-world workflow**

This combines everything:

* Sequential steps
* Parallel steps
* Error handling
* Returning structured data
* Modern async patterns

```js
async function getUserDashboard(userId) {
  try {
    // Step 1: Load user
    const user = await getUser(userId);

    // Step 2: Load user posts
    const posts = await getPosts(user.id);
    const latest = posts[0];

    // Step 3: Load activity in parallel
    const [comments, likes] = await Promise.all([
      getComments(latest.id),
      getLikes(latest.id)
    ]);

    return {
      user,
      latestPost: latest,
      comments,
      likes
    };
  } catch (err) {
    console.error("Error loading dashboard:", err);
    return null;
  }
}
```

**Usage**

```js
const dashboard = await getUserDashboard(1);
console.log(dashboard);
```

This pattern represents a typical async workflow in real applications:
fetch → fetch → parallel fetch → return final result.

---

## **Summary**

From this point forward, you should be comfortable using:

- ✔ Sequential async calls
- ✔ Parallel async calls with `Promise.all`
- ✔ `try/catch` error handling
- ✔ Async loops (`for...of` or Promise.all with map)
- ✔ Avoiding `.then()` and `new Promise()` unless truly necessary

Async/await simplifies complex asynchronous logic and leads to code that is easier to write, debug, and understand.

