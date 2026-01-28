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

**Events** are actions that happen in the browser—a user clicking a button, typing in an input, scrolling the page, or the page finishing loading. JavaScript lets you **listen** for these events and **respond** to them.

Events are what make web pages interactive. Without events, pages would be static HTML and CSS.

## `addEventListener`

The modern way to handle events is with `addEventListener`:

```javascript
const button = document.querySelector('button');

button.addEventListener('click', function() {
  console.log('Button clicked!');
});
```

### Syntax

```javascript
element.addEventListener(eventType, handler, options);
```

- **`eventType`** — the type of event to listen for (`'click'`, `'submit'`, etc.)
- **`handler`** — the function to call when the event occurs
- **`options`** — optional configuration (less commonly used)

### Multiple listeners

You can add multiple listeners to the same element:

```javascript
const button = document.querySelector('button');

button.addEventListener('click', function() {
  console.log('First handler');
});

button.addEventListener('click', function() {
  console.log('Second handler');
});

// Both run when button is clicked
```

### Removing listeners

To remove an event listener, you need a **named function**:

```javascript
function handleClick() {
  console.log('Clicked');
}

button.addEventListener('click', handleClick);
button.removeEventListener('click', handleClick);  // Remove it
```

**Note:** You can't remove an anonymous function, so store it in a variable or use a named function.

## The event object

When an event occurs, the browser passes an **event object** to your handler function:

```javascript
button.addEventListener('click', function(event) {
  console.log(event);  // Event object with lots of properties
});
```

### Common event properties

```javascript
element.addEventListener('click', function(e) {
  e.type;        // Event type: "click"
  e.target;      // Element that triggered the event
  e.currentTarget; // Element the listener is attached to
  e.preventDefault(); // Prevent default behavior
  e.stopPropagation(); // Stop event bubbling
  
  // Mouse events
  e.clientX;     // X coordinate of click
  e.clientY;     // Y coordinate of click
  
  // Keyboard events
  e.key;         // Key that was pressed
  e.code;        // Physical key code
  e.ctrlKey;     // Was Ctrl held?
  e.shiftKey;    // Was Shift held?
});
```

### `target` vs `currentTarget`

```javascript
<div id="parent">
  <button id="child">Click me</button>
</div>
```

```javascript
const parent = document.querySelector('#parent');
parent.addEventListener('click', function(e) {
  console.log(e.target);        // Button (element that was clicked)
  console.log(e.currentTarget); // Div (element with the listener)
});
```

**Use `target`** when you want the element that triggered the event.  
**Use `currentTarget`** when you want the element with the listener.

## Common events

### Click events

```javascript
button.addEventListener('click', function(e) {
  console.log('Button clicked!');
});
```

### Input events

For `<input>` and `<textarea>` elements:

```javascript
const input = document.querySelector('input');

// Fires on every keystroke
input.addEventListener('input', function(e) {
  console.log('Input value:', e.target.value);
});

// Fires when input loses focus (user clicks away)
input.addEventListener('change', function(e) {
  console.log('Final value:', e.target.value);
});
```

### Submit events

For forms:

```javascript
const form = document.querySelector('form');

form.addEventListener('submit', function(e) {
  e.preventDefault();  // Prevent form from submitting normally
  console.log('Form submitted!');
});
```

### Keyboard events

```javascript
document.addEventListener('keydown', function(e) {
  console.log('Key pressed:', e.key);
  console.log('Key code:', e.code);
  
  if (e.key === 'Enter') {
    console.log('Enter key pressed!');
  }
  
  if (e.ctrlKey && e.key === 's') {
    e.preventDefault();  // Prevent save dialog
    console.log('Ctrl+S pressed');
  }
});

// keyup fires when key is released
document.addEventListener('keyup', function(e) {
  console.log('Key released:', e.key);
});
```

### Other common events

```javascript
// Page load
window.addEventListener('load', function() {
  console.log('Page fully loaded');
});

// DOM ready (fires earlier than load)
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM ready');
});

// Scroll
window.addEventListener('scroll', function() {
  console.log('Page scrolled');
});

// Resize
window.addEventListener('resize', function() {
  console.log('Window resized');
});

// Focus/blur
input.addEventListener('focus', function() {
  console.log('Input focused');
});

input.addEventListener('blur', function() {
  console.log('Input lost focus');
});
```

## Event bubbling and capturing

Events don't just happen on one element—they **bubble up** through parent elements.

### Bubbling example

```html
<div id="parent">
  <button id="child">Click me</button>
</div>
```

```javascript
const parent = document.querySelector('#parent');
const button = document.querySelector('#child');

button.addEventListener('click', function() {
  console.log('Button clicked');
});

parent.addEventListener('click', function() {
  console.log('Parent clicked');
});

// When you click the button:
// Output: "Button clicked"
// Output: "Parent clicked" (event bubbled up!)
```

The click event **bubbles up** from the button to its parent.

### Capturing (less common)

Events can also be captured on the way down (capturing phase):

```javascript
parent.addEventListener('click', function() {
  console.log('Capturing phase');
}, true);  // true enables capturing phase
```

**Most of the time, you'll use bubbling** (the default). Capturing is less commonly needed.

### Stopping propagation

To prevent an event from bubbling up:

```javascript
button.addEventListener('click', function(e) {
  e.stopPropagation();  // Stop event from bubbling
  console.log('Button clicked');
});

parent.addEventListener('click', function() {
  console.log('This won't run if stopPropagation was called');
});
```

**Use carefully:** Stopping propagation can break other code that expects events to bubble.

## Event delegation

**Event delegation** means attaching an event listener to a parent element and handling events for child elements. This is powerful for dynamic content.

### The problem without delegation

```javascript
// Bad: adding listener to each button
document.querySelectorAll('button').forEach(button => {
  button.addEventListener('click', handleClick);
});

// If you add a new button dynamically, it won't have the listener!
const newButton = document.createElement('button');
document.body.appendChild(newButton);  // No click handler!
```

### The solution: delegation

```javascript
// Good: listen on parent, check target
const container = document.querySelector('#container');

container.addEventListener('click', function(e) {
  // Check if clicked element is a button
  if (e.target.tagName === 'BUTTON') {
    console.log('Button clicked:', e.target.textContent);
  }
});

// Now dynamically added buttons work automatically!
const newButton = document.createElement('button');
newButton.textContent = 'New Button';
container.appendChild(newButton);  // Works! Event bubbles up to container
```

### Benefits of event delegation

1. **Works with dynamic content** — new elements automatically get event handling
2. **Better performance** — one listener instead of many
3. **Less memory** — fewer event listeners
4. **Easier management** — one place to handle events

### Example: Dynamic list

```javascript
const list = document.querySelector('#list');

// Single listener for entire list
list.addEventListener('click', function(e) {
  if (e.target.classList.contains('delete-btn')) {
    e.target.closest('li').remove();  // Remove the list item
  }
  
  if (e.target.classList.contains('edit-btn')) {
    // Handle edit
  }
});

// All delete buttons work, even if added later
function addItem(text) {
  const li = document.createElement('li');
  li.innerHTML = `
    ${text}
    <button class="delete-btn">Delete</button>
    <button class="edit-btn">Edit</button>
  `;
  list.appendChild(li);  // Automatically works!
}
```

## Preventing default behavior

Some elements have default behaviors:

- `<a>` tags navigate to URLs
- Forms submit to the server
- Submit buttons submit forms
- Right-click shows context menu

To prevent these:

```javascript
const link = document.querySelector('a');
link.addEventListener('click', function(e) {
  e.preventDefault();  // Prevent navigation
  console.log('Link clicked but navigation prevented');
});

const form = document.querySelector('form');
form.addEventListener('submit', function(e) {
  e.preventDefault();  // Prevent form submission
  // Handle form manually
});
```

## Best practices

### 1. Use named functions when removing

```javascript
// Good: can remove later
function handleClick() { }
button.addEventListener('click', handleClick);
button.removeEventListener('click', handleClick);

// Bad: can't remove anonymous function
button.addEventListener('click', function() { });
```

### 2. Use event delegation for dynamic content

```javascript
// Good: delegation
container.addEventListener('click', function(e) {
  if (e.target.matches('.button')) {
    // Handle click
  }
});
```

### 3. Check if element exists

```javascript
const button = document.querySelector('button');
if (button) {
  button.addEventListener('click', handleClick);
}
```

### 4. Consider performance

```javascript
// Bad: listener on every item
items.forEach(item => {
  item.addEventListener('click', handler);
});

// Good: single listener with delegation
container.addEventListener('click', function(e) {
  if (e.target.classList.contains('item')) {
    handler(e);
  }
});
```
