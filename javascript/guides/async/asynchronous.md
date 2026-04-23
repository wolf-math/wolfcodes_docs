---
title: Asynchronous JavaScript
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is asynchronous JavaScript?

**Asynchronous (async) JavaScript** is JavaScript that starts a task now and finishes it later. While that task is waiting, the program can keep doing other work.

This is important because many operations take time:

- Fetching data from a server
- Reading files
- Waiting for user input
- Timers and animations

If JavaScript had to wait for these operations to finish before doing anything else, programs would feel frozen and unresponsive.

## Why async exists

JavaScript is **single-threaded**, meaning it runs your JavaScript code one step at a time. But the environment (the browser or Node.js) can do work in the background, like waiting for a timer or a network response.

Async programming is how you start those background tasks and handle the result when it is ready.

## A tiny async example

This example shows the basic async idea: code continues running while a timer waits.

```javascript
console.log("Start");

setTimeout(() => {
  console.log("Later");
}, 0);

console.log("End");
```

**Output:**

```text
Start
End
Later
```

Even with a `0` millisecond delay, the timer callback runs after the current synchronous code finishes.

## The three common async styles

JavaScript codebases commonly use three styles for async work:

1. **Callbacks**: you pass a function to run later.
2. **Promises**: an object that represents a value you will have in the future.
3. **`async` / `await`**: syntax that makes promise-based code read more like top-to-bottom code.

In modern JavaScript, you will usually write promises and `async` / `await`.

## What this section covers

This section teaches modern async JavaScript:

1. **[Callbacks](./callbacks)**: Learn to recognize callback style and understand why promise-based code is easier to manage.
2. **[Promises](./promises)**: The core tool for representing future values.
3. **[`async` / `await`](./async_await)**: The most common way to write promise-based code.

**Recommended order:** start with promises, then learn `async` / `await`.

## What this section does not cover

- A deep dive into the event loop
- Browser and Node async APIs in detail (`fetch`, `setTimeout`, DOM events)
- Advanced promise compositions and edge cases
- Generators and async iterators

Focus on mastering promises and `async` / `await` first. They cover most real-world async code.
