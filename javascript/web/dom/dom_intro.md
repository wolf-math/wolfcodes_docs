---
title: The DOM (Document Object Model)
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is the DOM?

The **DOM (Document Object Model)** is a representation of your HTML page that JavaScript can read and modify. Think of it as a tree structure where each HTML element is a node that JavaScript can access and manipulate.

When the browser loads an HTML page, it:
1. Parses the HTML
2. Creates the DOM tree
3. Makes it available to JavaScript via the `document` object

## DOM tree mental model

The DOM represents your HTML as a **tree** of nodes:

```html
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello</h1>
    <p>World</p>
  </body>
</html>
```

This HTML becomes a DOM tree:

```
document
  └── html
      ├── head
      │   └── title
      │       └── "My Page"
      └── body
          ├── h1
          │   └── "Hello"
          └── p
              └── "World"
```

Each box in this tree is a **node**, and JavaScript can:
- Navigate the tree (parent, child, sibling relationships)
- Read node properties
- Modify nodes
- Add new nodes
- Remove nodes

## Nodes vs elements

Understanding the difference between **nodes** and **elements** helps you work with the DOM effectively.

### Nodes

A **node** is any object in the DOM tree. There are different types of nodes:

- **Element nodes** — HTML elements (`<div>`, `<p>`, `<button>`, etc.)
- **Text nodes** — text content inside elements
- **Comment nodes** — HTML comments
- **Document nodes** — the document itself
- **Attribute nodes** — attributes on elements (less commonly used in modern code)

### Elements

An **element** is a specific type of node—an HTML element. Elements are what you usually work with:

```javascript
// This is an element node
const button = document.querySelector('button');

// Elements have properties like tagName
console.log(button.tagName);  // "BUTTON"
```

**In practice:** When you work with the DOM, you're usually working with **element nodes** (just called "elements"), but occasionally you'll encounter text nodes and other node types.

## Live vs static collections

When you select multiple elements, you get a **collection**. There are two types:

### Live collections

**Live collections** update automatically when the DOM changes:

```javascript
// getElementsByClassName returns a live collection
const divs = document.getElementsByClassName('item');
console.log(divs.length);  // 3

// Add a new div with class 'item'
const newDiv = document.createElement('div');
newDiv.className = 'item';
document.body.appendChild(newDiv);

console.log(divs.length);  // 4 (automatically updated!)
```

Live collections reflect the current state of the DOM.

### Static collections

**Static collections** don't update when the DOM changes:

```javascript
// querySelectorAll returns a static collection
const divs = document.querySelectorAll('.item');
console.log(divs.length);  // 3

// Add a new div with class 'item'
const newDiv = document.createElement('div');
newDiv.className = 'item';
document.body.appendChild(newDiv);

console.log(divs.length);  // Still 3 (snapshot at time of query)
```

Static collections are snapshots taken at the time of the query.

### Which to use?

- **Live collections** (`getElementsByClassName`, `getElementsByTagName`) — useful when the DOM changes frequently
- **Static collections** (`querySelectorAll`) — preferred for most cases, easier to reason about

**Recommendation:** Use `querySelectorAll` (static) for most cases. It's more predictable and easier to work with.

## Accessing the DOM

The `document` object is your entry point:

```javascript
// document represents the entire HTML page
document.body;      // The <body> element
document.head;      // The <head> element
document.title;     // The page title
document.URL;       // The page URL
```

### Parent-child relationships

You can navigate the DOM tree:

```javascript
const element = document.querySelector('p');

element.parentElement;        // Parent element
element.children;             // Child elements
element.firstElementChild;    // First child element
element.lastElementChild;     // Last child element
element.nextElementSibling;   // Next sibling
element.previousElementSibling; // Previous sibling
```

### Example: Navigating the tree

```html
<div id="parent">
  <p>First paragraph</p>
  <p>Second paragraph</p>
</div>
```

```javascript
const firstP = document.querySelector('#parent p');

console.log(firstP.parentElement.id);        // "parent"
console.log(firstP.nextElementSibling.textContent); // "Second paragraph"
```

## The DOM is dynamic

One of the most important things to understand: **the DOM is live**. Changes you make with JavaScript are immediately reflected in what users see:

```javascript
const heading = document.querySelector('h1');
heading.textContent = 'New heading';  // Page updates immediately!
```

This is what makes JavaScript powerful for building interactive web pages.

## DOM methods overview

The DOM provides many methods (we'll cover them in detail in upcoming guides):

- **Selecting elements** — `getElementById`, `querySelector`, etc.
- **Creating elements** — `createElement`
- **Modifying elements** — `textContent`, `innerHTML`, `setAttribute`
- **Adding/removing** — `appendChild`, `removeChild`, `insertBefore`
- **Classes** — `classList.add`, `classList.remove`, `classList.toggle`

## Common DOM properties

Elements have many properties:

```javascript
const element = document.querySelector('div');

element.id;              // Element's ID
element.className;       // Element's class attribute
element.tagName;         // Tag name (e.g., "DIV")
element.textContent;     // Text content
element.innerHTML;       // HTML content
element.style;           // Inline styles
element.dataset;         // Data attributes
```

We'll explore these in detail in the [manipulating the DOM guide](./manipulating_dom).

## Performance considerations

The DOM is powerful but can be slow if overused:

### Minimize DOM queries

```javascript
// Bad: querying DOM multiple times
for (let i = 0; i < 1000; i++) {
  const element = document.querySelector('.item');  // Queries DOM 1000 times!
  element.textContent = i;
}

// Good: query once, reuse
const element = document.querySelector('.item');
for (let i = 0; i < 1000; i++) {
  element.textContent = i;
}
```

### Batch DOM updates

```javascript
// Bad: updating DOM in loop
const list = document.querySelector('#list');
for (let i = 0; i < 100; i++) {
  const item = document.createElement('li');
  item.textContent = `Item ${i}`;
  list.appendChild(item);  // Triggers reflow each time
}

// Better: build fragment, add once
const list = document.querySelector('#list');
const fragment = document.createDocumentFragment();
for (let i = 0; i < 100; i++) {
  const item = document.createElement('li');
  item.textContent = `Item ${i}`;
  fragment.appendChild(item);
}
list.appendChild(fragment);  // Single DOM update
```

We'll cover more performance tips in the [performance guide](../best_practice/performance_best_practices).
