---
title: JavaScript in the Browser
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

## How JavaScript runs in the browser

JavaScript can run in many environments—browsers, Node.js servers, mobile apps, and more. This guide focuses on **JavaScript in the browser**, where it runs alongside HTML and CSS to create interactive web pages.

When you write JavaScript for the browser, you're not just writing JavaScript—you're using JavaScript to interact with **browser APIs** and the **DOM (Document Object Model)** that browsers provide.

## The relationship between HTML, CSS, and JavaScript

Modern web pages are built with three technologies working together:

### HTML — Structure

**HTML** (HyperText Markup Language) defines the **structure** and **content** of your page:

```html
<button id="myButton">Click me</button>
<p id="message">Hello</p>
```

HTML describes *what* is on the page, but not how it looks or behaves.

### CSS — Presentation

**CSS** (Cascading Style Sheets) defines the **appearance** and **styling**:

```css
button {
  background-color: blue;
  color: white;
  padding: 10px;
}

#message {
  font-size: 18px;
}
```

CSS describes *how* things look, but not how they behave.

### JavaScript — Behavior

**JavaScript** adds **interactivity** and **dynamic behavior**:

```javascript
const button = document.getElementById('myButton');
const message = document.getElementById('message');

button.addEventListener('click', function() {
  message.textContent = 'Button clicked!';
});
```

JavaScript describes *what happens* when users interact with the page.

### Working together

These three technologies work together:

1. **HTML** provides the structure (elements, buttons, forms)
2. **CSS** styles those elements (colors, layouts, animations)
3. **JavaScript** makes them interactive (clicks, form submissions, dynamic updates)

Each has a specific role, and understanding how they interact is key to web development.

## What the browser provides beyond JavaScript

The browser environment gives JavaScript access to powerful APIs that don't exist in pure JavaScript:

### The DOM (Document Object Model)

The **DOM** is a representation of your HTML page that JavaScript can read and modify:

```javascript
// Access HTML elements
const element = document.getElementById('myButton');

// Change content
element.textContent = 'New text';

// Add event listeners
element.addEventListener('click', handleClick);
```

### Browser APIs

Browsers provide many APIs:

- **Fetch API** — make HTTP requests
- **Storage APIs** — `localStorage` and `sessionStorage`
- **Geolocation API** — get user's location
- **Canvas API** — draw graphics
- **WebSockets** — real-time communication
- And many more...

These are **browser features**, not JavaScript language features. They're only available when JavaScript runs in a browser.

## JavaScript vs the web platform

It's important to understand the distinction:

- **JavaScript** — the programming language (variables, functions, arrays, objects)
- **Web Platform** — browser APIs, DOM, events, storage, networking

You learned **JavaScript the language** in the [JavaScript User Guide](../../guides). This guide teaches you how to use JavaScript with the **Web Platform**—the browser's APIs and capabilities.

### Example of the distinction

```javascript
// Pure JavaScript (works everywhere)
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2);

// Web Platform (only works in browsers)
const button = document.getElementById('myButton'); // DOM API
button.addEventListener('click', handler); // Events API
fetch('/api/data'); // Fetch API
```

Both are written in JavaScript, but the second example uses browser-specific APIs.

## When JavaScript runs

Understanding when JavaScript executes helps you write better code:

### Page loading order

1. **HTML parsing** — browser reads HTML and builds the DOM tree
2. **CSS parsing** — browser reads CSS and applies styles
3. **JavaScript execution** — JavaScript runs and can interact with the DOM

### Script placement matters

```html
<!-- Script at the end (recommended) -->
<body>
  <button id="myButton">Click me</button>
  <script src="app.js"></script>
</body>
```

Placing scripts at the end of `<body>` ensures the DOM is ready before JavaScript runs.

### The `DOMContentLoaded` event

For scripts in `<head>`, wait for the DOM to be ready:

```javascript
document.addEventListener('DOMContentLoaded', function() {
  // DOM is ready, safe to access elements
  const button = document.getElementById('myButton');
});
```

This ensures all HTML elements exist before your JavaScript tries to access them.

### Script execution timing

- **Synchronous scripts** — block HTML parsing until they finish
- **Async scripts** — download in parallel but execute immediately when ready
- **Deferred scripts** — download in parallel but execute after HTML parsing

```html
<script src="app.js"></script>           <!-- Blocking -->
<script src="app.js" async></script>     <!-- Async -->
<script src="app.js" defer></script>     <!-- Deferred -->
```

## Why this matters

Understanding the relationship between HTML, CSS, and JavaScript, and knowing when JavaScript runs, helps you:

- Write code that works reliably
- Debug issues with timing and loading
- Structure your code effectively
- Understand how web pages actually work

## What this guide covers

This guide teaches you:

- How to interact with the DOM
- How to handle user events
- How to make web pages dynamic and interactive
- How to work with browser APIs
- How to structure frontend JavaScript applications

## What this guide does not cover

This guide intentionally does **NOT** cover:

- **JavaScript the language** — see the [JavaScript User Guide](../../guides)
- **React, Vue, Angular** — these are frameworks built on JavaScript
- **Build tools** — webpack, Vite, etc.
- **CSS frameworks** — Bootstrap, Tailwind, etc.
- **Backend development** — server-side JavaScript

We focus on **vanilla JavaScript** and **browser APIs** to give you a solid foundation before learning frameworks.
