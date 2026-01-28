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

## Minimizing DOM updates

DOM manipulation is one of the slowest operations in JavaScript. Minimize updates for better performance.

### Batch DOM updates

```javascript
// Bad: multiple DOM updates
for (let i = 0; i < 100; i++) {
  const div = document.createElement('div');
  div.textContent = `Item ${i}`;
  container.appendChild(div);  // Triggers reflow each time
}

// Good: build fragment, add once
const fragment = document.createDocumentFragment();
for (let i = 0; i < 100; i++) {
  const div = document.createElement('div');
  div.textContent = `Item ${i}`;
  fragment.appendChild(div);
}
container.appendChild(fragment);  // Single reflow
```

### Update classes, not styles

```javascript
// Slower: multiple style updates
element.style.color = 'red';
element.style.fontSize = '18px';
element.style.backgroundColor = 'blue';

// Faster: single class update
element.classList.add('highlighted');
// CSS: .highlighted { color: red; font-size: 18px; background: blue; }
```

### Read, then write

Batch reads and writes separately:

```javascript
// Bad: alternating reads and writes
const width1 = element1.offsetWidth;  // Read
element1.style.width = width1 + 10 + 'px';  // Write
const width2 = element2.offsetWidth;  // Read
element2.style.width = width2 + 10 + 'px';  // Write

// Good: batch reads, then writes
const width1 = element1.offsetWidth;  // Read
const width2 = element2.offsetWidth;  // Read
element1.style.width = width1 + 10 + 'px';  // Write
element2.style.width = width2 + 10 + 'px';  // Write
```

## Avoiding layout thrashing (conceptual)

**Layout thrashing** happens when you repeatedly read layout properties (like `offsetWidth`, `offsetHeight`) after making changes, forcing the browser to recalculate layout.

### The problem

```javascript
// Bad: forces layout recalculation
elements.forEach(element => {
  const width = element.offsetWidth;  // Forces layout calculation
  element.style.width = width * 2 + 'px';  // Triggers layout
  const height = element.offsetHeight;  // Forces layout again!
});
```

### The solution

```javascript
// Good: batch reads, then writes
const dimensions = elements.map(el => ({
  element: el,
  width: el.offsetWidth,
  height: el.offsetHeight
}));

dimensions.forEach(({ element, width, height }) => {
  element.style.width = width * 2 + 'px';
  element.style.height = height * 2 + 'px';
});
```

**Key principle:** Read layout properties once, make all changes, then read again if needed.

## Efficient event handling

### Use event delegation

```javascript
// Bad: listener on every item
items.forEach(item => {
  item.addEventListener('click', handleClick);
});

// Good: single listener
container.addEventListener('click', function(e) {
  if (e.target.classList.contains('item')) {
    handleClick(e);
  }
});
```

### Debounce/throttle expensive operations

```javascript
// Debounce search input
const debouncedSearch = debounce(function(query) {
  // Expensive search operation
  performSearch(query);
}, 300);

searchInput.addEventListener('input', function() {
  debouncedSearch(this.value);
});

// Throttle scroll handler
const throttledScroll = throttle(function() {
  // Expensive scroll operation
  updateScrollPosition();
}, 100);

window.addEventListener('scroll', throttledScroll);
```

### Remove unused listeners

```javascript
// Store listener function
function handleClick() {
  console.log('Clicked');
}

element.addEventListener('click', handleClick);

// Remove when no longer needed
element.removeEventListener('click', handleClick);
```

## Memory leaks in the browser

Memory leaks occur when JavaScript holds references to objects that are no longer needed.

### Common causes

```javascript
// Leak: global variable holding large data
let largeData = new Array(1000000).fill('data');

// Leak: event listeners not removed
function setupListeners() {
  element.addEventListener('click', function() {
    // Handler still references element even if element removed
  });
}

// Leak: closures holding references
function createHandler() {
  const data = largeObject;
  return function() {
    // Closure holds reference to largeObject
    console.log(data);
  };
}
```

### How to avoid

```javascript
// Clean up when done
function cleanup() {
  largeData = null;  // Release reference
  element.removeEventListener('click', handler);
}

// Use weak references when possible (advanced)
// Use WeakMap/WeakSet for temporary references
```

### Check for leaks

Use browser DevTools Memory tab:
1. Take heap snapshot
2. Perform actions
3. Take another snapshot
4. Compare to find growing memory

## Writing readable, maintainable vanilla js

### Organize code into functions

```javascript
// Good: organized functions
function initializeApp() {
  loadUserData();
  setupEventListeners();
  renderInitialUI();
}

function loadUserData() {
  // Load data
}

function setupEventListeners() {
  // Setup events
}

function renderInitialUI() {
  // Render UI
}
```

### Use meaningful names

```javascript
// Bad: unclear names
function doStuff() { }
const x = getData();
const temp = process(x);

// Good: descriptive names
function initializeUserProfile() { }
const userData = fetchUserData();
const processedUser = processUserData(userData);
```

### Keep functions focused

```javascript
// Bad: function does too much
function handleUser() {
  // Validate
  // Save to server
  // Update UI
  // Show notification
  // Log analytics
}

// Good: single responsibility
function validateUser(user) { }
function saveUser(user) { }
function updateUserUI(user) { }
function showNotification(message) { }
function logAnalytics(event) { }
```

### Comment complex logic

```javascript
// Good: explain why, not what
function calculateDiscount(price, user) {
  // Apply loyalty discount for members who've been active > 1 year
  if (user.isMember && user.membershipDuration > 365) {
    return price * 0.15;  // 15% discount
  }
  return 0;
}
```

## Additional best practices

### Cache DOM queries

```javascript
// Bad: querying repeatedly
function update() {
  document.querySelector('#item').textContent = 'a';
  document.querySelector('#item').textContent = 'b';
  document.querySelector('#item').textContent = 'c';
}

// Good: query once
const item = document.querySelector('#item');
function update() {
  item.textContent = 'a';
  item.textContent = 'b';
  item.textContent = 'c';
}
```

### Use `textContent` over `innerHTML`

```javascript
// Safer and faster
element.textContent = userInput;  // Good

element.innerHTML = userInput;  // Avoid unless you need HTML
```

### Minimize global variables

```javascript
// Bad: global pollution
var counter = 0;
var userName = '';
var settings = {};

// Good: namespace or module
const App = {
  counter: 0,
  userName: '',
  settings: {}
};

// Or use modules (best)
// app.js
export const App = {
  counter: 0
};
```

### Handle errors gracefully

```javascript
// Always handle errors
async function loadData() {
  try {
    const data = await fetch('/api/data').then(r => r.json());
    displayData(data);
  } catch (error) {
    console.error('Failed to load data:', error);
    showErrorMessage('Unable to load data. Please try again.');
  }
}
```

## Performance checklist

- ✅ Cache DOM queries
- ✅ Use document fragments for batch updates
- ✅ Use event delegation
- ✅ Debounce/throttle expensive operations
- ✅ Remove unused event listeners
- ✅ Minimize global variables
- ✅ Use `textContent` instead of `innerHTML` when possible
- ✅ Batch DOM reads and writes
- ✅ Clean up references when done
- ✅ Use CSS classes instead of inline styles when possible

## Next steps

Performance matters, but so does code organization. Let's learn about [structuring frontend JavaScript](./structuring_frontend) to keep your code maintainable as projects grow.
