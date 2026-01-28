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

## Why async exists

JavaScript is **single-threaded**, meaning it can only do one thing at a time. However, many operations take time:
- Fetching data from a server
- Reading files
- Waiting for user input
- Animations

If JavaScript waited for these operations to finish, your program would freeze. **Asynchronous programming** lets JavaScript start these operations and continue with other code while waiting for them to complete.

## The problem with synchronous code

Imagine fetching data from a server:

```javascript
// Synchronous (blocking) - DON'T DO THIS
const data = fetchFromServer();  // Program freezes until this completes
console.log(data);               // This won't run until fetch completes
doOtherThings();                 // This also waits
```

If this took 2 seconds, your entire program would freeze for 2 seconds—terrible user experience!

## How JavaScript handles async

JavaScript has evolved through three approaches to handle asynchronous operations:

1. **Callbacks** (old, don't use) — Functions passed to other functions to be called later
2. **Promises** (better) — Objects that represent future values
3. **async/await** (modern, preferred) — Syntax that makes async code read like synchronous code

This section will teach you promises and async/await—the modern way to write async JavaScript. We'll briefly cover callbacks only so you can recognize them in older code, but **you should use async/await in all new code**.

## What this section covers

This section teaches you modern async JavaScript:

1. **[Callbacks](./callbacks)** — Old approach (learn to recognize, don't use)
2. **[Promises](./promises)** — Better way to handle async operations
3. **[async/await](./async_await)** — Modern, preferred syntax

**Start with promises**, then learn async/await. You'll use async/await for 99% of your async code.

## What this section doesn't cover

- 🚫 **Event loop deep dive** — understanding JavaScript's event loop in detail
- 🚫 **Browser APIs** — [`fetch`](/docs/javascript/web/browser_api/networking), [`setTimeout`](/docs/javascript/web/browser_api/async_browser_apis), DOM events (those belong in Web Development guides)
- 🚫 **Advanced promise patterns** — complex promise compositions
- 🚫 **Generators and async iterators** — advanced async patterns

Focus on mastering promises and async/await first. These cover 90% of async use cases.
