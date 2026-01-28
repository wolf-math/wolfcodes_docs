---
title: Introduction to JavaScript
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

## What is JavaScript?

**JavaScript** is a programming language that was originally designed to make web pages interactive. However, JavaScript is much more than "the browser language", it's a full-featured programming language that runs in many environments.

Today, JavaScript powers:
- **Web browsers** — making websites interactive and dynamic
- **Node.js** — running JavaScript on servers and in command-line tools
- **Mobile apps** — through frameworks like React Native
- **Desktop applications** — through Electron and similar technologies

Despite its name, JavaScript is not related to Java. The name was a marketing decision made in the 1990s. JavaScript is its own language with its own syntax, rules, and ecosystem.

## Where JavaScript runs

### In the browser

When JavaScript runs in a web browser, it has access to browser-specific features like the Document Object Model (DOM), which lets you manipulate web pages. However, this guide focuses on **core JavaScript** not browser APIs. The [browser API](/docs/javascript/web/) will be covered in the next section.

### In Node.js

**Node.js** is a JavaScript runtime built on Chrome's V8 JavaScript engine. It lets you run JavaScript on your computer outside of a browser, similar to how you run Python or other languages. You can use Node.js to:
- Build web servers
- Write command-line tools
- Create scripts to automate tasks

### Other environments

JavaScript also runs in database systems (like MongoDB), IoT devices, and many other places. The core language features are the same across all these environments.

## JavaScript vs Python: key differences

If you're coming from Python, here are some important mental model differences:

### Statements vs expressions

Both JavaScript and Python have statements and expressions, but JavaScript often uses expressions where Python uses statements:

```javascript
// JavaScript - conditional expression
const result = x > 5 ? "big" : "small";

// Python - conditional statement
result = "big" if x > 5 else "small"
```

JavaScript makes heavy use of expressions for control flow, which can make code more compact (but sometimes less readable).

### Indentation vs braces

Python uses indentation to define code blocks:

```python
if x > 5:
    print("big")
else:
    print("small")
```

JavaScript uses curly braces `{}`:

```javascript
if (x > 5) {
  console.log("big");
} else {
  console.log("small");
}
```

### Dynamic typing (with differences)

Both languages are dynamically typed, but they behave differently:

- **Python** treats `None` as distinct from other falsy values
- **JavaScript** has both `null` and `undefined`, and they behave slightly differently
- **JavaScript** has some type coercion quirks that Python doesn't have (e.g., `"5" + 3` vs `"5" - 3`)

### Semicolons (optional but recommended)

JavaScript allows you to omit semicolons in many cases (automatic semicolon insertion), but adding them explicitly prevents subtle bugs and is generally recommended for beginners.

## What this guide covers

This guide will teach you:

- Core JavaScript language features (variables, types, functions, objects)
- Control flow (conditionals, loops)
- Functions and scope
- Objects and arrays
- Object-oriented programming in JavaScript
- Asynchronous programming (promises, async/await)
- Modules and code organization

## What these guides intentionally **do not** cover

These guides focus on **JavaScript the language**, not JavaScript in specific environments:

- **Browser APIs** (DOM manipulation, `fetch`, events) — these belong in a Web Development guide
- **Node.js-specific features** — file system APIs, `require` (though we cover ES6 `import`/`export`)
- **Frameworks** — React, Vue, Angular, etc. are built on JavaScript but are separate topics
- **Build tools** — webpack, Babel, etc. are ecosystem tools, not language features

The goal is to give you a solid foundation in **JavaScript itself**, so you can then learn browser APIs, Node.js, or frameworks with confidence.

## How to use this guide

Work through these guides in order. Each builds on previous concepts:

1. **Start with the basics** — variables, types, and running JavaScript
2. **Learn data structures** — strings, arrays, objects
3. **Master control flow** — conditionals and loops
4. **Understand functions** — how to write and organize code
5. **Explore advanced topics** — OOP, async, modules

You don't need to master everything at once. Focus on understanding each concept before moving forward, and feel free to revisit earlier sections as you learn more.
