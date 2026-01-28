---
title: Running JavaScript
sidebar_position: 2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## How to run JavaScript code

Unlike Python, which requires installation, JavaScript comes built into every web browser. However, to run JavaScript outside the browser, you'll need Node.js installed.

:::note
There are other JavaScript runtimes besides Node.js, like Bun and Deno. For this guide, though, we'll stick with Node.js because it’s the most widely used and best supported place to start.
:::

This guide shows you three main ways to run JavaScript:

1. **Browser console** — quick experimentation
2. **JavaScript files** — writing and saving programs
3. **Node.js** — running JavaScript from the terminal

## JavaScript in the browser console

Every modern web browser has a built-in JavaScript console where you can type and run JavaScript code immediately.

### Opening the console

- **Chrome/Edge**: Press `F12` or `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Option+I` (Mac), then click the "Console" tab
- **Firefox**: Press `F12` or `Ctrl+Shift+K` (Windows/Linux) or `Cmd+Option+K` (Mac)
- **Safari**: Enable Developer menu first (Preferences → Advanced → "Show Develop menu"), then `Cmd+Option+C`

### Running code in the console

Once the console is open, you can type JavaScript code and press Enter to run it:

```javascript
console.log("Hello, World!");
// Output: Hello, World!

const name = "Alice";
console.log(name);
// Output: Alice
```

The console is perfect for:
- Quick experiments
- Testing small snippets of code
- Debugging (seeing what your code actually does)

**Note:** This guide focuses on core JavaScript, not browser-specific features. The console is useful for learning, but we won't cover DOM manipulation or other browser APIs here.

## JavaScript in a `.js` file

For real programs, you'll write JavaScript code in files with the `.js` extension.

### Creating your first JavaScript file

1. Create a new file called `hello.js`
2. Add this code:

```javascript
console.log("Hello, World!");
console.log("This is my first JavaScript program!");
```

3. Save the file

### Running the file in Node.js

Open your terminal and navigate to the directory containing `hello.js`, then run:

```bash
node hello.js
```

You should see:

```
Hello, World!
This is my first JavaScript program!
```

### Running in a browser (HTML file)

You can also run JavaScript files in a browser by embedding them in an HTML file:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My First JavaScript</title>
</head>
<body>
  <script src="hello.js"></script>
</body>
</html>
```

Open the HTML file in a browser, and the JavaScript will run. However, for learning core JavaScript (without browser features), **Node.js is recommended**.

## Using `node` to run JavaScript

**Node.js** is a JavaScript runtime that lets you run JavaScript outside of a browser. It's essential for learning JavaScript as a programming language.

### Installing Node.js

1. Visit [nodejs.org](https://nodejs.org/)
2. Download the LTS (Long Term Support) version
3. Follow the installation instructions for your operating system

### Verifying installation

After installing, open your terminal and type:

```bash
node --version
```

You should see something like `v20.10.0` (the exact version doesn't matter, as long as it's recent).

### Running JavaScript files with Node

Once Node.js is installed, you can run any `.js` file:

```bash
node filename.js
```

Example:

```javascript
// greet.js
const name = "Alice";
console.log(`Hello, ${name}!`);
```

```bash
node greet.js
# Output: Hello, Alice!
```

### Running JavaScript interactively

Node.js also provides an interactive REPL (Read-Eval-Print Loop) similar to Python's interactive mode:

```bash
node
```

This opens an interactive session where you can type JavaScript code:

```javascript
> const x = 5;
undefined
> x * 2
10
> console.log("Hello!")
Hello!
undefined
> .exit
```

Press `Ctrl+C` twice or type `.exit` to quit.

## `console.log()` As your primary debugging tool

The `console.log()` function is your most important tool for seeing what your code is doing. It prints values to the console (browser console or terminal).

### Basic usage

```javascript
console.log("Hello, World!");
console.log(42);
console.log(true);
```

Output:
```
Hello, World!
42
true
```

### Logging variables

```javascript
const name = "Alice";
const age = 30;
console.log(name);      // Alice
console.log(age);       // 30
console.log(name, age); // Alice 30
```

### Debugging with `console.log()`

When learning or debugging, `console.log()` helps you see what's happening:

```javascript
const x = 5;
const y = 10;
console.log("x is:", x);  // x is: 5
console.log("y is:", y);  // y is: 10

const sum = x + y;
console.log("sum is:", sum); // sum is: 15
```

You'll use `console.log()` constantly as you learn JavaScript. It's the JavaScript equivalent of Python's `print()`.

## Running code examples in this guide

Throughout this guide, code examples can be run in two ways:

1. **Copy into a `.js` file** and run with `node filename.js`
2. **Paste into your browser's console** (though some examples won't work without Node.js features)

For the best learning experience, **create `.js` files** and run them with Node.js. This matches how you'll write JavaScript in real projects.
