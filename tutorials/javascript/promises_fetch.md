---
slug: promises-fetch
title: "Promises and Fetch"
authors: Aaron Wolf
sidebar_position: 3
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev

---

## Restaurants

A promise in JavaScript is just a **pending task**. It’s like ordering food at a restaurant: when you place your order, the server makes a _promise_ to bring the food you ordered. Once the food is brought to the table the promise has been fulfilled. If the food you ordered can’t be served because the kitchen is out of a key ingredient, then you can _catch_ a meal somewhere else. 

This is all asynchronous. When you sit down at the table, you might be chatting with a friend or scrolling on your phone. You pause what you were doing so that you can give your order to the server, then return to doing what you were doing beforehand.

JavaScript promises work similarly. Since JavaScript is single-threaded, promises allow the JavaScript engine to move on to other tasks while it waits for certain operations to complete.

## JavaScript

A promise is a specific type of object. All promises begin in a pending state. The callback function inside the promise, called an _executor_, defines when to resolve or reject the promise. 

### Creating a promise:

Here, we’re creating a new promise called order. If the promise is fulfilled, it resolves with the message "eat food". If it’s rejected, it returns "find another restaurant" instead.

```javascript
const order = new Promise((resolve, reject) => {
  if ( foodDelivered) {
    resolve('eat food');
  } else {
    reject('find another restaurant');
  }
})
```

Once the promise is created, you can use .then() and .catch() to decide what should happen depending on the outcome.

### Using a promise

```javascript
order
  // wait for the asynchronous value to be fulfilled
  .then(value => console.log(value))
  // handle rejection
  .catch(error => console.log(error))
  .finally(() => console.log('all done'));
```

# Fetch

`fetch` is a built-in function in JavaScript that _returns a promise_. It makes an HTTP request and allows you to handle the response asynchronously with `.then()` and `.catch()`. 

## Using `fetch()`

```javascript
fetch('url')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error))
  .finally(() => console.log('all done'));
```

# The Call Stack and Event Loop

The _call stack_ manages **synchronous** tasks, keeping track of the order in which they execute. This is fairly straightforward: tasks are executed in the order they're written.

However, **asynchronous** tasks are handled by the event loop. The event loop allows asynchronous code to be executed out of order, letting the JavaScript engine continue working on other tasks without waiting.

## Example

How will this execute?

```javascript
console.log("console log first!");
setTimeout( _ => console.log("set timeout second!"), 0);
Promise.resolve().then(() => console.log("promise third"));
console.log("console log last!!!");
```

You might expect that it would execute in order, but it doesn’t. The JavaScript event loop processes these instructions differently.
The result is actually this:

```javascript
> console log first!
> console log last!!!
> promise third
> set timeout second!
```

## Why?

The event loop rearranges the execution priority:

1. Synchronous tasks (like console.log("console log first!") and console.log("console log last!!!")) are executed immediately, in the order they appear.
1. Microtasks (such as Promise callbacks) are given the next priority and are executed before any other asynchronous tasks.
1. Macrotasks (like setTimeout) are handled last, even if the timeout is set to zero.

This allows the JavaScript engine to work asynchronously, performing other tasks without waiting for all operations to complete immediately.

