---
title: Web APIs Overview
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What this section is about

When JavaScript runs in the browser, it can use more than just the language itself. It can also use **Web APIs**, which are browser-provided tools for things like timing, network requests, storage, events, animation, and much more.

The name **Web APIs** is a bit misleading. These APIs do not have to be "about the web" in the everyday sense, and many of them also do not feel specifically "browser-like" when you first meet them. The standard term is still **Web APIs** because they are part of the broader **web platform**, not part of the JavaScript language itself.

This section focuses on a few foundational Web APIs that show up in real frontend code very quickly:

- **How JavaScript processes code** so async behavior has a clear mental model
- **Timers and scheduling** for delayed work, repeated work, and animation
- **`fetch()`** for loading and sending data
- **Storage APIs** for saving small amounts of data in the browser

## How this fits with the rest of the guide

Earlier pages in this guide teach:

- How JavaScript runs in the browser
- How to work with the DOM
- How to respond to events
- How to keep application state in JavaScript

This section builds on that foundation. These APIs are how your app starts doing more real-world work:

- Fetch data from a server
- Save user preferences
- Delay or repeat actions
- Animate UI updates

## Recommended reading order

1. [How JavaScript Processes Code](./how_js_processes_code)
2. [Timers, Scheduling, and Animation](./async_browser_apis)
3. [Fetch API](./networking)
4. [Web Storage](./browser_storage)

## A useful mental model

Think of Web APIs like this:

- **JavaScript** is the language
- **Web APIs** are the browser features JavaScript can call
- **The DOM** is one important Web API, but not the only one

That distinction matters because it helps you understand which features belong to the language and which are provided by the web platform.
