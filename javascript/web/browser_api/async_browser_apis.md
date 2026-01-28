---
title: Asynchronous Browser APIs
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

## Why async matters in the browser

The browser needs to handle many things simultaneously: user input, animations, network requests, and more. **Asynchronous APIs** let JavaScript start operations and continue with other code while waiting for them to complete.

This prevents the browser from freezing while waiting for operations to finish.

## `setTimeout`

`setTimeout` executes code after a specified delay (in milliseconds).

### Basic usage

```javascript
setTimeout(function() {
  console.log('This runs after 1 second');
}, 1000);  // 1000 milliseconds = 1 second

// Continue with other code immediately
console.log('This runs immediately');
// Output: "This runs immediately"
// (after 1 second) "This runs after 1 second"
```

### Clearing timeouts

`setTimeout` returns an ID you can use to cancel it:

```javascript
const timeoutId = setTimeout(function() {
  console.log('This will not run');
}, 5000);

// Cancel it
clearTimeout(timeoutId);
```

### Common use cases

```javascript
// Show message temporarily
function showMessage(message) {
  const div = document.createElement('div');
  div.textContent = message;
  document.body.appendChild(div);
  
  setTimeout(() => {
    div.remove();
  }, 3000);  // Remove after 3 seconds
}

// Delay an action
button.addEventListener('click', function() {
  setTimeout(() => {
    window.location.href = '/next-page';
  }, 500);  // Navigate after 500ms
});
```

## `setInterval`

`setInterval` executes code repeatedly at specified intervals.

### Basic usage

```javascript
setInterval(function() {
  console.log('This runs every second');
}, 1000);
```

### Clearing intervals

```javascript
const intervalId = setInterval(function() {
  console.log('Ticking...');
}, 1000);

// Stop after 10 seconds
setTimeout(() => {
  clearInterval(intervalId);
}, 10000);
```

### Example: Countdown timer

```javascript
let count = 10;

const intervalId = setInterval(function() {
  document.querySelector('#timer').textContent = count;
  count--;
  
  if (count < 0) {
    clearInterval(intervalId);
    document.querySelector('#timer').textContent = 'Time\'s up!';
  }
}, 1000);  // Update every second
```

## `requestAnimationFrame`

`requestAnimationFrame` is optimized for animations. It runs before the next browser repaint (usually 60 times per second).

### Basic usage

```javascript
function animate() {
  // Update animation
  element.style.left = position + 'px';
  position += 1;
  
  // Continue animation
  requestAnimationFrame(animate);
}

// Start animation
requestAnimationFrame(animate);
```

### Why use `requestAnimationFrame`?

- **Smooth animations** — synced with browser's refresh rate
- **Performance** — browser optimizes it
- **Battery efficient** — pauses when tab is hidden
- **Better than `setInterval`** for animations

### Example: Smooth movement

```javascript
let position = 0;

function move() {
  position += 2;
  element.style.transform = `translateX(${position}px)`;
  
  if (position < 500) {
    requestAnimationFrame(move);
  }
}

requestAnimationFrame(move);
```

### Stopping animations

```javascript
let animationId;

function startAnimation() {
  function animate() {
    // Update animation
    updatePosition();
    
    animationId = requestAnimationFrame(animate);
  }
  
  animationId = requestAnimationFrame(animate);
}

function stopAnimation() {
  cancelAnimationFrame(animationId);
}
```

## Debouncing and throttling (conceptual)

These patterns limit how often functions execute, which is important for performance.

### Debouncing

**Debouncing** delays function execution until the user stops performing the action.

**Use case:** Search input that queries API as user types.

```javascript
function debounce(func, delay) {
  let timeoutId;
  return function(...args) {
    clearTimeout(timeoutId);  // Cancel previous timeout
    timeoutId = setTimeout(() => {
      func.apply(this, args);
    }, delay);
  };
}

// Usage
const searchInput = document.querySelector('#search');
const debouncedSearch = debounce(function(query) {
  console.log('Searching for:', query);
  // Make API call
}, 300);  // Wait 300ms after user stops typing

searchInput.addEventListener('input', function() {
  debouncedSearch(this.value);
});
```

**How it works:** Each time the user types, the previous timeout is cancelled and a new one starts. The function only runs after the user stops typing for 300ms.

### Throttling

**Throttling** limits function execution to at most once per time period.

**Use case:** Scroll events that trigger expensive operations.

```javascript
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => {
        inThrottle = false;
      }, limit);
    }
  };
}

// Usage
const throttledScroll = throttle(function() {
  console.log('Scrolled');
  // Expensive operation
}, 100);  // Run at most once per 100ms

window.addEventListener('scroll', throttledScroll);
```

**How it works:** The function runs immediately, then ignores all calls for the next 100ms. After 100ms, it can run again.

### When to use each

- **Debounce** — wait for user to finish (search, resize, typing)
- **Throttle** — limit frequency (scroll, mousemove, resize)

## Common patterns

### Delayed execution

```javascript
// Show tooltip after delay
let tooltipTimeout;

element.addEventListener('mouseenter', function() {
  tooltipTimeout = setTimeout(() => {
    showTooltip();
  }, 500);  // Show after 500ms
});

element.addEventListener('mouseleave', function() {
  clearTimeout(tooltipTimeout);
  hideTooltip();
});
```

### Polling

```javascript
// Check for updates every 5 seconds
function pollForUpdates() {
  fetch('/api/updates')
    .then(response => response.json())
    .then(data => {
      updateUI(data);
    });
}
```

Learn more about the [`fetch` API](/docs/javascript/web/browser_api/networking) for making HTTP requests.

const pollInterval = setInterval(pollForUpdates, 5000);

// Stop polling when needed
clearInterval(pollInterval);
```

### Animation loop

```javascript
let animationRunning = false;

function animate() {
  if (!animationRunning) return;
  
  // Update animation
  updateAnimation();
  
  requestAnimationFrame(animate);
}

function startAnimation() {
  animationRunning = true;
  animate();
}

function stopAnimation() {
  animationRunning = false;
}
```

## Performance considerations

### Avoid too many timers

```javascript
// Bad: creates many timers
elements.forEach(element => {
  setInterval(() => {
    updateElement(element);
  }, 1000);
});

// Good: single timer updates all
setInterval(() => {
  elements.forEach(updateElement);
}, 1000);
```

### Clean up timers

```javascript
// Remember to clean up
const timeouts = [];

function scheduleAction(callback, delay) {
  const id = setTimeout(callback, delay);
  timeouts.push(id);
  return id;
}

function cleanup() {
  timeouts.forEach(clearTimeout);
  timeouts.length = 0;
}
```

### Use `requestAnimationFrame` for animations

```javascript
// Bad: use setInterval for animations
setInterval(() => {
  animate();
}, 16);  // ~60fps but not synced

// Good: use requestAnimationFrame
function animate() {
  // Animation code
  requestAnimationFrame(animate);
}
```
