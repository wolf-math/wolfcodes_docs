---
title: Events
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are events?

**Events** are actions that happen in the browser, such as clicking a button, typing in an input, submitting a form, or the page finishing loading. JavaScript lets you listen for those events and respond when they happen.

Events are what make web pages interactive. Without events, pages would mostly be static HTML and CSS.

### Smallest working example

```html
<button id="helloButton">Click me</button>
```

```javascript
const button = document.getElementById("helloButton");

if (button) {
  button.addEventListener("click", () => {
    console.log("Button clicked!");
  });
}
```

## Why this matters

Events are how browser JavaScript reacts to what is happening on the page:

- User actions like clicks, typing, and form submissions
- Browser changes like page load, resize, and scroll
- UI behavior like opening menus, validating forms, and updating state

## `addEventListener()`

The standard way to handle events in modern JavaScript is `addEventListener()`:

```javascript
const button = document.getElementById("button");

if (button) {
  button.addEventListener("click", () => {
    console.log("Button clicked!");
  });
}
```

### Syntax

```javascript
element.addEventListener(eventType, handler, options);
```

- **`eventType`**: the event to listen for, like `"click"` or `"submit"`
- **`handler`**: the function that runs when the event happens
- **`options`**: optional configuration, used less often in beginner code

### Multiple listeners

You can attach more than one listener to the same element:

```javascript
const button = document.getElementById("button");

if (button) {
  button.addEventListener("click", () => {
    console.log("First handler");
  });

  button.addEventListener("click", () => {
    console.log("Second handler");
  });
}
```

### Removing listeners

To remove a listener, you need to keep a reference to the same function:

```javascript
function handleClick() {
  console.log("Clicked");
}

const button = document.getElementById("button");

if (button) {
  button.addEventListener("click", handleClick);
  button.removeEventListener("click", handleClick);
}
```

:::note
You cannot remove an anonymous function later unless you stored it somewhere first.
:::

## The event object

When an event happens, the browser passes an **event object** into your handler:

```javascript
const button = document.getElementById("button");

if (button) {
  button.addEventListener("click", event => {
    console.log(event);
  });
}
```

### Common event properties

```javascript
element.addEventListener("click", e => {
  e.type; // Event type: "click"
  e.target; // Element that triggered the event
  e.currentTarget; // Element the listener is attached to
  e.preventDefault(); // Prevent default behavior
  e.stopPropagation(); // Stop event bubbling

  // Mouse events
  e.clientX; // X coordinate of click
  e.clientY; // Y coordinate of click

  // Keyboard events
  e.key; // Key that was pressed
  e.code; // Physical key code
  e.ctrlKey; // Was Ctrl held?
  e.shiftKey; // Was Shift held?
});
```

### `target` vs `currentTarget`

```html
<div id="parent">
  <button id="child">Click me</button>
</div>
```

```javascript
const parent = document.getElementById("#parent");

if (parent) {
  parent.addEventListener("click", e => {
    console.log(e.target); // The element that was clicked
    console.log(e.currentTarget); // The element with the listener
  });
}
```

**Use `target`** when you want the element that triggered the event.  
**Use `currentTarget`** when you want the element that owns the listener.

:::tip
Rule of thumb: `target` is "what was clicked"; `currentTarget` is "where the listener is attached".
:::

## Common events

### Click events

```javascript
const button = document.getElementById("button");

if (button) {
  button.addEventListener("click", () => {
    console.log("Button clicked!");
  });
}
```

### Input events

For `<input>` and `<textarea>` elements:

```javascript
const input = document.getElementById("input");

if (input) {
  input.addEventListener("input", e => {
    console.log("Input value:", e.target.value);
  });

  input.addEventListener("change", e => {
    console.log("Final value:", e.target.value);
  });
}
```

**What happens:**
1. `input` fires on every keystroke.
2. `change` fires when the value is committed, usually when the field loses focus.

### Submit events

```javascript
const form = document.getElementById("form");

if (form) {
  form.addEventListener("submit", e => {
    e.preventDefault();
    console.log("Form submitted!");
  });
}
```

### Keyboard events

```javascript
document.addEventListener("keydown", e => {
  console.log("Key pressed:", e.key);
  console.log("Key code:", e.code);

  if (e.key === "Enter") {
    console.log("Enter key pressed!");
  }

  if (e.ctrlKey && e.key === "s") {
    e.preventDefault();
    console.log("Ctrl+S pressed");
  }
});

document.addEventListener("keyup", e => {
  console.log("Key released:", e.key);
});
```

### Other common events

```javascript
window.addEventListener("load", () => {
  console.log("Page fully loaded");
});

document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM ready");
});

window.addEventListener("scroll", () => {
  console.log("Page scrolled");
});

window.addEventListener("resize", () => {
  console.log("Window resized");
});

const input = document.getElementById("input");

if (input) {
  input.addEventListener("focus", () => {
    console.log("Input focused");
  });

  input.addEventListener("blur", () => {
    console.log("Input lost focus");
  });
}
```

## Event bubbling and capturing

Events do not stay only on one element. In most cases, they **bubble up** through parent elements.

### Bubbling example

```html
<div id="parent">
  <button id="child">Click me</button>
</div>
```

```javascript
const parent = document.getElementById("parent");
const button = document.getElementById("child");

if (button) {
  button.addEventListener("click", () => {
    console.log("Button clicked");
  });
}

if (parent) {
  parent.addEventListener("click", () => {
    console.log("Parent clicked");
  });
}
```

**What happens:**
1. You click the button.
2. The button's listener runs first.
3. The event bubbles up, so the parent's listener runs next.

### Capturing

Events can also be handled on the way down. This is called the **capturing phase**:

```javascript
const parent = document.getElementById("parent");

if (parent) {
  parent.addEventListener("click", () => {
    console.log("Capturing phase");
  }, true);
}
```

Most of the time, you will use the default bubbling behavior.

### Stopping propagation

If you need to stop an event from bubbling:

```javascript
const parent = document.getElementById("parent");
const button = document.getElementById("child");

if (button) {
  button.addEventListener("click", e => {
    e.stopPropagation();
    console.log("Button clicked");
  });
}

if (parent) {
  parent.addEventListener("click", () => {
    console.log("This will not run if propagation was stopped");
  });
}
```

:::warning
Use `stopPropagation()` carefully. It can break other code that expects events to bubble normally.
:::

## Event delegation

**Event delegation** means adding one listener to a parent element and handling events for matching child elements. This is especially useful for dynamic content.

### Without delegation

```javascript
document.querySelectorAll("button").forEach(button => {
  button.addEventListener("click", handleClick);
});

const newButton = document.createElement("button");
document.body.appendChild(newButton);
```

If you add a new button later, it will not automatically get a click listener.

### With delegation

```javascript
const container = document.querySelector("#container");

if (container) {
  container.addEventListener("click", e => {
    const clickedButton = e.target.closest("button");

    if (clickedButton && container.contains(clickedButton)) {
      console.log("Button clicked:", clickedButton.textContent);
    }
  });
}

const newButton = document.createElement("button");
newButton.textContent = "New Button";

if (container) {
  container.appendChild(newButton);
}
```

### Why delegation is useful

- **Works with dynamic content**: new elements automatically participate
- **Uses fewer listeners**: often one listener instead of many
- **Simplifies updates**: event handling stays in one place

### Example: dynamic list

```javascript
const list = document.querySelector("#list");

if (list) {
  list.addEventListener("click", e => {
    const deleteButton = e.target.closest(".delete-btn");
    if (deleteButton) {
      const listItem = deleteButton.closest("li");
      if (listItem) {
        listItem.remove();
      }
      return;
    }

    const editButton = e.target.closest(".edit-btn");
    if (editButton) {
      console.log("Edit clicked");
    }
  });
}

function addItem(text) {
  const li = document.createElement("li");
  li.innerHTML = `
    ${text}
    <button class="delete-btn">Delete</button>
    <button class="edit-btn">Edit</button>
  `;

  if (list) {
    list.appendChild(li);
  }
}
```

## Preventing default behavior

Some elements have built-in browser behavior:

- `<a>` tags navigate to another URL
- Forms submit to the server
- Submit buttons submit forms

You can prevent that behavior with `preventDefault()`:

```javascript
const link = document.getElementById("a");

if (link) {
  link.addEventListener("click", e => {
    e.preventDefault();
    console.log("Link clicked but navigation prevented");
  });
}

const form = document.getElementById("form");

if (form) {
  form.addEventListener("submit", e => {
    e.preventDefault();
    console.log("Handle form submission manually");
  });
}
```

## Best practices

### Use named functions when you need removal

```javascript
function handleClick() {}

const button = document.getElementById("button");

if (button) {
  button.addEventListener("click", handleClick);
  button.removeEventListener("click", handleClick);
}
```

### Check elements before attaching listeners

```javascript
function handleClick() {}

const button = document.getElementById("button");

if (button) {
  button.addEventListener("click", handleClick);
}
```

### Prefer delegation for many similar elements

```javascript
function handler(event) {
  console.log(event.target);
}

const container = document.querySelector("#container");

if (container) {
  container.addEventListener("click", e => {
    if (e.target.classList.contains("item")) {
      handler(e);
    }
  });
}
```

## Summary

- Events let your JavaScript respond to browser activity like clicks, typing, and form submission.
- `addEventListener()` is the standard way to handle events in modern code.
- Event delegation is often the best choice when many child elements need the same behavior.
- Check that elements exist before attaching listeners, and use `preventDefault()` or `stopPropagation()` carefully.

## Next up

- [Forms and input](./forms_input)
