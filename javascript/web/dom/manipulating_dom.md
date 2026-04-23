---
title: Manipulating the DOM
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What does it mean to manipulate the DOM?

**Manipulating the DOM** means changing what’s on the page by updating elements: their text, attributes, classes, styles, or position in the document.

### Smallest working example

```html
<button id="toggle">Toggle</button>
<p id="message">Hello</p>
```

```javascript
const button = document.querySelector("#toggle");
const message = document.querySelector("#message");

if (button && message) {
  button.addEventListener("click", () => {
    message.classList.toggle("hidden");
  });
}
```

## Why this matters

Most browser interactivity is DOM manipulation:

- Update the UI when something changes (data loaded, user clicks a button)
- Show/hide content and validation messages
- Build and update lists, cards, or tables dynamically

## Reading and updating text

Once you've [selected an element](./selecting_elements), you can read and modify its text content.

### `textContent`

`textContent` gets or sets the **plain text** content of an element:

```javascript
const paragraph = document.querySelector("p");

if (paragraph) {
  // Read text
  console.log(paragraph.textContent); // "Hello World"

  // Update text
  paragraph.textContent = "New text";

  // textContent ignores HTML tags
  paragraph.textContent = "<strong>Bold</strong>"; // Displays as text, not HTML
  // Result: "<strong>Bold</strong>" (shown as text, not rendered as HTML)
}
```

**Use `textContent` when:** You want plain text only (safer, prevents XSS attacks).

### `innerHTML`

`innerHTML` gets or sets the **HTML content** of an element:

```javascript
const div = document.querySelector("div");

if (div) {
  // Read HTML
  console.log(div.innerHTML); // "<p>Hello</p>"

  // Update HTML
  div.innerHTML = "<p>New paragraph</p>";

  // innerHTML renders HTML
  div.innerHTML = "<strong>Bold</strong>"; // Renders as bold text
}
```

**Use `innerHTML` when:** You need to insert HTML (but be careful with user input—see safety notes below).

### Safety with `innerHTML`

:::warning
Never put raw user input into `innerHTML`. It can lead to **XSS (Cross-Site Scripting)**.
:::

```javascript
const element = document.querySelector("#output");
const userInput = `<img src="x" onerror="alert('XSS')" />`;

if (element) {
  // DANGEROUS: user input directly in innerHTML
  // element.innerHTML = userInput;

  // Safer default: show it as text
  element.textContent = userInput;
}
```

**Best practice:** Use `textContent` unless you specifically need HTML. If you must use `innerHTML` with user input, sanitize it first.

:::note
Setting `innerHTML` replaces an element’s existing children, which can also remove event listeners attached to those child elements.
:::

## Attributes

HTML elements have attributes (`id`, `class`, `src`, `href`, etc.). You can read and modify them:

### Reading attributes

```javascript
const link = document.querySelector("a");

if (link) {
  link.id; // Get ID
  link.className; // Get class attribute
  link.href; // Get href (full URL)
  link.getAttribute("href"); // Get href (as written in HTML)

  // For custom attributes (data-*)
  link.dataset.userId; // Get data-user-id="123"
  link.getAttribute("data-user-id"); // Alternative
}
```

### Setting attributes

```javascript
const img = document.querySelector("img");

if (img) {
  // Direct property (for standard attributes)
  img.src = "new-image.jpg";
  img.alt = "New alt text";
  img.id = "myImage";

  // Using setAttribute (works for any attribute)
  img.setAttribute("src", "new-image.jpg");
  img.setAttribute("data-id", "123");
  img.setAttribute("aria-label", "Description");
}
```

### Removing attributes

```javascript
const element = document.querySelector("div");

if (element) {
  element.removeAttribute("id");
  element.removeAttribute("data-custom");
}
```

### Data attributes

HTML5 data attributes (`data-*`) are commonly used to store custom data:

```html
<div data-user-id="123" data-status="active">User</div>
```

```javascript
const div = document.querySelector("div");

if (div) {
  // Access via dataset (converts kebab-case to camelCase)
  div.dataset.userId; // "123"
  div.dataset.status; // "active"

  // Or use getAttribute
  div.getAttribute("data-user-id"); // "123"
}
```

## Classes

Managing CSS classes is a common task. The `classList` property makes this easy:

### `classList.add()`

Add one or more classes:

```javascript
const element = document.querySelector("div");

if (element) {
  element.classList.add("active");
  element.classList.add("highlighted", "visible"); // Multiple classes
}
```

### `classList.remove()`

Remove one or more classes:

```javascript
const element = document.querySelector("div");

if (element) {
  element.classList.remove("active");
  element.classList.remove("highlighted", "visible");
}
```

### `classList.toggle()`

Add the class if it's not present, remove it if it is:

```javascript
const element = document.querySelector("div");

if (element) {
  element.classList.toggle("active"); // Toggle on/off
  element.classList.toggle("active", true); // Force add
  element.classList.toggle("active", false); // Force remove
}
```

### `classList.contains()`

Check if an element has a class:

```javascript
const element = document.querySelector("div");

if (element) {
  console.log(element.classList.contains("active"));
}
```

### `classList.replace()`

Replace one class with another:

```javascript
const element = document.querySelector("div");

if (element) {
  element.classList.replace("old-class", "new-class");
}
```

### Example: Toggle button state

```javascript
const button = document.querySelector("button");

if (button) {
  button.addEventListener("click", () => {
    button.classList.toggle("active");

    if (button.classList.contains("active")) {
      button.textContent = "Active";
      return;
    }

    button.textContent = "Inactive";
  });
}
```

:::tip
Prefer classes for most styling. Use inline styles mainly for dynamic values (like setting a calculated position).
:::

## Inline styles

You can modify inline styles directly via the `style` property:

```javascript
const element = document.querySelector("div");

if (element) {
  // Set individual styles
  element.style.color = "red";
  element.style.backgroundColor = "blue";
  element.style.fontSize = "18px";
  element.style.display = "none";

  // Note: CSS properties use camelCase in JavaScript
  // CSS: background-color → JavaScript: backgroundColor
  // CSS: font-size → JavaScript: fontSize
}
```

### Setting multiple styles

```javascript
const element = document.querySelector("div");

if (element) {
  // Method 1: Set individually
  element.style.color = "red";
  element.style.fontSize = "18px";

  // Method 2: Use cssText (replaces all styles)
  element.style.cssText = "color: red; font-size: 18px;";

  // Method 3: Object.assign
  Object.assign(element.style, {
    color: "red",
    fontSize: "18px"
  });
}
```

## Creating elements

Create new elements dynamically:

```javascript
// Create element
const newDiv = document.createElement("div");
const newParagraph = document.createElement("p");
const newButton = document.createElement("button");

// Set properties before adding to DOM
newDiv.textContent = "Hello";
newDiv.className = "container";
newParagraph.textContent = "Paragraph text";
```

### Creating with `innerHTML`

You can also create elements using `innerHTML`:

```javascript
const container = document.querySelector("#container");

if (container) {
  container.innerHTML = `<div class="item">New item</div>`;
}
```

:::note
`innerHTML` replaces all existing content. For appending, prefer `insertAdjacentHTML()`.
:::

```javascript
const container = document.querySelector("#container");

if (container) {
  container.insertAdjacentHTML("beforeend", "<div>New item</div>");
}
```

## Appending and removing elements

### Appending elements

Add elements to the DOM:

```javascript
const parent = document.querySelector("#container");
const newDiv = document.createElement("div");
newDiv.textContent = "New element";

if (parent) {
  // Add to end
  parent.appendChild(newDiv);

  // Alternative:
  // parent.insertAdjacentElement("beforeend", newDiv);
}
```

### `insertAdjacentHTML` positions

```javascript
const element = document.querySelector("#container");

if (element) {
  // beforebegin - before the element
  element.insertAdjacentHTML("beforebegin", "<div>Before</div>");

  // afterbegin - inside, at the start
  element.insertAdjacentHTML("afterbegin", "<div>First child</div>");

  // beforeend - inside, at the end (like appendChild)
  element.insertAdjacentHTML("beforeend", "<div>Last child</div>");

  // afterend - after the element
  element.insertAdjacentHTML("afterend", "<div>After</div>");
}
```

### Removing elements

```javascript
const element = document.querySelector("#toRemove");

if (element) {
  // Modern alternative (simpler)
  element.remove();
}
```

### Example: Dynamic list

```javascript
function addListItem(text) {
  const list = document.querySelector("#myList");
  if (!list) {
    return;
  }

  const newItem = document.createElement("li");
  newItem.textContent = text;

  const deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete";
  deleteButton.addEventListener("click", () => {
    newItem.remove();
  });

  newItem.appendChild(deleteButton);
  list.appendChild(newItem);
}

addListItem("Item 1");
addListItem("Item 2");
```

## Document fragments

When adding many elements, use **document fragments** for better performance:

```javascript
// Without fragment (many DOM updates)
const list = document.querySelector("#list");
if (list) {
  for (let i = 0; i < 100; i++) {
    const item = document.createElement("li");
    item.textContent = `Item ${i}`;
    list.appendChild(item);
  }
}
```

```javascript
// With fragment (single append)
const list = document.querySelector("#list");
if (list) {
  const fragment = document.createDocumentFragment();
  for (let i = 0; i < 100; i++) {
    const item = document.createElement("li");
    item.textContent = `Item ${i}`;
    fragment.appendChild(item);
  }
  list.appendChild(fragment);
}
```

Fragments let you build elements in memory before adding them to the DOM.

## Common patterns

### Show/hide elements

```javascript
const element = document.querySelector("#modal");

if (element) {
  // Hide
  element.classList.add("hidden");

  // Show
  element.classList.remove("hidden");
}
```

### Updating multiple elements

```javascript
document.querySelectorAll(".item").forEach(item => {
  item.textContent = "Updated";
  item.classList.add("highlighted");
});
```

### Cloning elements

```javascript
const original = document.querySelector(".template");

if (original) {
  const clone = original.cloneNode(true); // true = deep clone
  clone.id = "new-id"; // Change ID to avoid duplicates
  document.body.appendChild(clone);
}
```

## Summary

- Use `textContent` as the safest default for updating text.
- Use `innerHTML` only when you need HTML, and never with raw user input.
- `classList` is the cleanest way to toggle styles and UI state.
- Use fragments when adding lots of elements.

## Next up

- [DOM introduction](./dom_intro)
- [Selecting elements](./selecting_elements)
- [DOM events](../events/dom_events)
