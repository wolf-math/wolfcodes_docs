---
slug: promises-fetch
title: "Promises and Fetch"
author: Aaron Wolf
sidebar_position: 3
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
description: An introduction to JavaScript Promises, the fetch API, and how asynchronous code is scheduled by the event loop.
---

## Restaurants

A Promise in JavaScript represents a **value that will be available in the future**.

A useful way to think about a Promise is ordering food at a restaurant. When you place your order, the server makes a *promise* to bring you the food. 

- As you wait for your food, the promise it **pending**.
- If the food arrives, the promise is **fulfilled**.  
- If the kitchen can’t prepare the meal, the promise is **rejected**.

This entire process is asynchronous.

You don’t sit idle while waiting for the food. You talk with a friend, scroll on your phone, or do something else, and only react when the food arrives. If the meal can’t be served, you *catch* the error and decide what to do next.

JavaScript Promises work similarly. Since JavaScript is single-threaded, Promises allow the engine to continue executing other code while it waits for certain operations to complete.

## JavaScript Promises

A Promise is a specific type of object that represents the eventual result of an asynchronous operation. All Promises begin in a **pending** state.

The function passed to the Promise constructor is called the *executor*. It runs immediately and determines when the Promise should resolve or reject.

### Creating a Promise

Here’s a simplified example to demonstrate how a Promise is constructed:

```javascript
const order = new Promise((resolve, reject) => {
  if (foodDelivered) {
    resolve('eat food');
  } else {
    reject('find another restaurant');
  }
});
```

If the Promise is fulfilled, it resolves with `"eat food"`.
If it is rejected, it returns `"find another restaurant"`.

### Using a Promise

Once a Promise is created, you can attach handlers that run when the Promise settles.

```javascript
order
  .then(value => console.log(value))       // handle fulfillment
  .catch(error => console.log(error))      // handle rejection
  .finally(() => console.log('all done')); // always runs
```

## Fetch

`fetch()` is a built-in JavaScript function that **returns a Promise** representing an HTTP request. It allows you to make network requests and handle responses asynchronously using `.then()` and `.catch()`.

### Using `fetch()`

```javascript
fetch('url')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error))
  .finally(() => console.log('all done'));
```

## The Call Stack and Event Loop

The **call stack** manages synchronous JavaScript execution, keeping track of function calls and the order in which they run.

Asynchronous behavior is coordinated by the **event loop**. Rather than executing code “out of order,” the event loop determines *when* asynchronous callbacks are placed back onto the call stack, allowing the engine to remain responsive.

## Example

How will this code execute?

```javascript
console.log("console log first!");
setTimeout(() => console.log("set timeout second!"), 0);
Promise.resolve().then(() => console.log("promise third"));
console.log("console log last!!!");
```

You might expect it to run top to bottom, but it doesn’t. The actual output is:

```text
console log first!
console log last!!!
promise third
set timeout second!
```

Even though `setTimeout` is set to `0`, it does **not** run immediately.

## Why?

The event loop schedules work using different queues:

1. **Synchronous tasks** run first, directly on the call stack.
2. **Microtasks** (such as Promise callbacks) run next, immediately after the current call stack clears.
3. **Macrotasks** (such as `setTimeout`) run last, even if their delay is set to zero.

This scheduling model allows JavaScript to remain responsive while still handling asynchronous operations predictably.

## Where this fits

Promises are the foundation of modern asynchronous JavaScript. While `async` / `await` provides a cleaner syntax, it is built entirely on top of Promises.

Understanding Promises, the event loop, and task scheduling makes async/await feel predictable instead of magical.
