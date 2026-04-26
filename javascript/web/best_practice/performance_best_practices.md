---
title: Performance & Best Practices
sidebar_position: 12
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What this page is about

Performance in browser JavaScript is mostly about doing less unnecessary work. The biggest wins usually come from reducing DOM work, handling events carefully, and avoiding code patterns that keep the browser busy longer than needed.

This page focuses on practical habits that make frontend code faster and easier to maintain.

## Why performance matters

When browser JavaScript does too much work, users feel it quickly:

- The page responds slowly to clicks and typing
- Animations feel janky
- Scrolling stutters
- Memory usage grows over time

Good performance work is usually not about micro-optimizing every line. It is more often about choosing better patterns.

## Start with the biggest wins

In most frontend codebases, these changes matter more than small syntax-level optimizations:

- Reduce unnecessary DOM reads and writes
- Reuse DOM queries instead of repeating them
- Use fewer event listeners when delegation works
- Limit how often expensive handlers run
- Clean up timers, listeners, and references when they are no longer needed

## DOM work is expensive

The DOM is slower to work with than plain JavaScript data. That means performance often improves when you do more work in JavaScript first and then make fewer DOM changes.

### Batch DOM updates

```javascript
// Bad: update the DOM many times
for (let i = 0; i < 100; i++) {
  const item = document.createElement("div");
  item.textContent = `Item ${i}`;
  container.appendChild(item);
}
```

```javascript
// Better: build first, append once
const fragment = document.createDocumentFragment();

for (let i = 0; i < 100; i++) {
  const item = document.createElement("div");
  item.textContent = `Item ${i}`;
  fragment.appendChild(item);
}

container.appendChild(fragment);
```

### Prefer class changes over many inline style changes

```javascript
// More work in JavaScript
element.style.color = "red";
element.style.fontSize = "18px";
element.style.backgroundColor = "blue";
```

```javascript
// Usually cleaner and easier to maintain
element.classList.add("highlighted");
```

### Cache DOM queries

```javascript
// Bad: same query repeated
function updateItem() {
  document.querySelector("#item").textContent = "a";
  document.querySelector("#item").classList.add("active");
  document.querySelector("#item").setAttribute("data-ready", "true");
}
```

```javascript
// Better: query once
const item = document.querySelector("#item");

function updateItem() {
  if (!item) {
    return;
  }

  item.textContent = "a";
  item.classList.add("active");
  item.setAttribute("data-ready", "true");
}
```

## Avoid layout thrashing

The browser has to calculate layout when you ask for size or position information. If your code keeps switching back and forth between layout reads and DOM writes, the browser may be forced to recalculate layout repeatedly.

### Read first, then write

```javascript
// Bad: read, write, read, write
const width1 = element1.offsetWidth;
element1.style.width = `${width1 + 10}px`;

const width2 = element2.offsetWidth;
element2.style.width = `${width2 + 10}px`;
```

```javascript
// Better: batch reads, then batch writes
const width1 = element1.offsetWidth;
const width2 = element2.offsetWidth;

element1.style.width = `${width1 + 10}px`;
element2.style.width = `${width2 + 10}px`;
```

### Bigger example

```javascript
// Bad: layout can be recalculated repeatedly
elements.forEach(element => {
  const width = element.offsetWidth;
  element.style.width = `${width * 2}px`;
  const height = element.offsetHeight;
  element.style.height = `${height * 2}px`;
});
```

```javascript
// Better: collect measurements first
const dimensions = elements.map(element => ({
  element,
  width: element.offsetWidth,
  height: element.offsetHeight
}));

dimensions.forEach(({ element, width, height }) => {
  element.style.width = `${width * 2}px`;
  element.style.height = `${height * 2}px`;
});
```

:::tip
Rule of thumb: if you need layout information, do your reads together and your writes together.
:::

## Handle events efficiently

Event listeners are essential, but they can become expensive if you attach too many or let heavy handlers run too often.

### Use event delegation when many similar elements need the same behavior

```javascript
// Bad: one listener per item
items.forEach(item => {
  item.addEventListener("click", handleClick);
});
```

```javascript
// Better: one listener on a parent
container.addEventListener("click", event => {
  if (event.target.classList.contains("item")) {
    handleClick(event);
  }
});
```

### Debounce or throttle expensive handlers

```javascript
const debouncedSearch = debounce(query => {
  performSearch(query);
}, 300);

searchInput.addEventListener("input", () => {
  debouncedSearch(searchInput.value);
});
```

```javascript
const throttledScroll = throttle(() => {
  updateScrollPosition();
}, 100);

window.addEventListener("scroll", throttledScroll);
```

Use:

- **Debounce** when you care about the final action, like a search box
- **Throttle** when you want regular updates, like scroll position

### Remove listeners you no longer need

```javascript
function handleClick() {
  console.log("Clicked");
}

element.addEventListener("click", handleClick);

element.removeEventListener("click", handleClick);
```

## Watch for memory leaks

Memory leaks happen when JavaScript keeps references to things that should be gone.

### Common causes

```javascript
// Large data kept alive unnecessarily
let largeData = new Array(1000000).fill("data");
```

```javascript
// Listener not cleaned up
function setupListeners(element) {
  function handleClick() {
    console.log("Clicked");
  }

  element.addEventListener("click", handleClick);
}
```

```javascript
// Closure keeps a reference alive
function createHandler(largeObject) {
  return function () {
    console.log(largeObject);
  };
}
```

### Practical cleanup

```javascript
let largeData = new Array(1000000).fill("data");

function cleanup(element, handler) {
  largeData = null;
  element.removeEventListener("click", handler);
}
```

### How to investigate leaks

Use browser DevTools memory tools:

1. Take a heap snapshot
2. Perform the action you suspect
3. Take another snapshot
4. Compare whether memory keeps growing

## Choose safer, simpler DOM patterns

These are not huge optimizations on their own, but they are good defaults.

### Prefer `textContent` when you only need text

```javascript
element.textContent = userInput;
```

```javascript
element.innerHTML = userInput;
```

`textContent` is usually the better default because it is simpler and avoids accidentally inserting unsafe HTML.

### Minimize global state

```javascript
// Harder to manage
var counter = 0;
var userName = "";
var settings = {};
```

```javascript
// Clearer organization
const app = {
  counter: 0,
  userName: "",
  settings: {}
};
```

Keeping data organized makes performance bugs easier to reason about because there are fewer moving parts.

## Keep the code maintainable too

Fast code that is hard to understand often becomes slow again later because it is harder to debug and improve.

### Break work into focused functions

```javascript
function initializeApp() {
  loadUserData();
  setupEventListeners();
  renderInitialUI();
}

function loadUserData() {}
function setupEventListeners() {}
function renderInitialUI() {}
```

### Use meaningful names

```javascript
// Hard to understand
function doStuff() {}
const x = getData();
const temp = process(x);
```

```javascript
// Easier to understand
function initializeUserProfile() {}
const userData = fetchUserData();
const processedUser = processUserData(userData);
```

### Keep functions focused

```javascript
// Too much responsibility
function handleUser() {
  // validate
  // save
  // update UI
  // show notification
  // log analytics
}
```

```javascript
function validateUser(user) {}
function saveUser(user) {}
function updateUserUI(user) {}
function showNotification(message) {}
function logAnalytics(event) {}
```

### Comment the why, not the obvious what

```javascript
function calculateDiscount(price, user) {
  // Apply a loyalty discount for long-term members
  if (user.isMember && user.membershipDuration > 365) {
    return price * 0.15;
  }

  return 0;
}
```

## Handle failure paths cleanly

Performance and reliability often go together. If data loading fails and your page gets stuck in a broken state, the user experience is poor even if the code is technically fast.

```javascript
async function loadData() {
  try {
    const response = await fetch("/api/data");
    const data = await response.json();
    displayData(data);
  } catch (error) {
    console.error("Failed to load data:", error);
    showErrorMessage("Unable to load data. Please try again.");
  }
}
```

## Performance checklist

- Cache DOM queries you reuse
- Batch DOM updates when possible
- Group layout reads and writes instead of mixing them
- Use delegation for many similar event targets
- Debounce or throttle expensive handlers
- Remove timers and listeners you no longer need
- Prefer `textContent` unless you truly need HTML
- Keep state and logic organized so problems are easier to fix

## Summary

- The biggest frontend performance wins usually come from reducing DOM work and unnecessary repeated work.
- Start with better patterns before worrying about tiny optimizations.
- Good performance is closely tied to good structure, cleanup, and readability.

## Next steps

Performance matters, but structure matters too. Continue with [Structuring Frontend JavaScript](./structuring_frontend) to make larger codebases easier to manage.
