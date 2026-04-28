---
title: Timers, Scheduling, and Animation
sidebar_position: 11
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are timers, scheduling, and animation APIs?

**Timers, scheduling, and animation APIs** let JavaScript delay work, repeat work, or run code just before the browser paints the next frame. These are foundational Web APIs for building responsive interfaces.

### Smallest working example

```javascript
console.log("Start");

setTimeout(() => {
  console.log("This runs later");
}, 1000);

console.log("End");
```

**What happens:**
1. `"Start"` logs first.
2. `"End"` logs right away.
3. After about 1 second, `"This runs later"` logs.

## Why this matters

The browser often has to wait for something:

- A delay before showing or hiding UI
- Repeated updates like timers or polling
- The next paint during an animation
- A burst of user input that should not trigger heavy work every time

If this work blocked the page, the UI would feel frozen.

## `setTimeout()`

`setTimeout()` runs code once after a delay.

### Basic usage

```javascript
setTimeout(() => {
  console.log("This runs after 1 second");
}, 1000);

console.log("This runs immediately");
```

### Clearing timeouts

`setTimeout()` returns an ID that you can cancel:

```javascript
const timeoutId = setTimeout(() => {
  console.log("This will not run");
}, 5000);

clearTimeout(timeoutId);
```

### Common uses

```javascript
function showMessage(message) {
  const container = document.querySelector("#messages");
  if (!container) {
    return;
  }

  const messageElement = document.createElement("div");
  messageElement.textContent = message;
  container.appendChild(messageElement);

  setTimeout(() => {
    messageElement.remove();
  }, 3000);
}
```

```javascript
const button = document.querySelector("#next-button");

if (button) {
  button.addEventListener("click", () => {
    setTimeout(() => {
      window.location.href = "/next-page";
    }, 500);
  });
}
```

## `setInterval()`

`setInterval()` runs code repeatedly after a fixed amount of time.

### Basic usage

```javascript
const intervalId = setInterval(() => {
  console.log("This runs every second");
}, 1000);
```

### Clearing intervals

```javascript
const intervalId = setInterval(() => {
  console.log("Ticking...");
}, 1000);

setTimeout(() => {
  clearInterval(intervalId);
}, 10000);
```

### Example: countdown timer

```javascript
let count = 10;
const timerElement = document.querySelector("#timer");

const intervalId = setInterval(() => {
  if (!timerElement) {
    clearInterval(intervalId);
    return;
  }

  timerElement.textContent = `${count}`;
  count -= 1;

  if (count < 0) {
    clearInterval(intervalId);
    timerElement.textContent = "Time's up!";
  }
}, 1000);
```

:::tip
Use `setTimeout()` for one future action and `setInterval()` for repeated actions.
:::

## `requestAnimationFrame()`

`requestAnimationFrame()` asks the browser to run your code before the next repaint. It is the best default for visual animations.

### Basic usage

```javascript
const box = document.querySelector("#box");
let position = 0;

function animate() {
  if (!box) {
    return;
  }

  box.style.transform = `translateX(${position}px)`;
  position += 1;

  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

### Why use `requestAnimationFrame()`?

- **Matches the browser's paint cycle**: smoother motion
- **Improves efficiency**: the browser can optimize when it runs
- **Pauses in hidden tabs**: better battery usage than many timer loops

### Example: stop an animation

```javascript
const box = document.querySelector("#box");
let position = 0;
let animationId = 0;

function animate() {
  if (!box) {
    return;
  }

  position += 2;
  box.style.transform = `translateX(${position}px)`;

  if (position < 500) {
    animationId = requestAnimationFrame(animate);
  }
}

function startAnimation() {
  animationId = requestAnimationFrame(animate);
}

function stopAnimation() {
  cancelAnimationFrame(animationId);
}
```

## Related patterns: debouncing and throttling

These are patterns for limiting how often a function runs.

### Debouncing

**Debouncing** waits until the user stops triggering the action for a certain amount of time.

Use it for:
- Search inputs
- Auto-save after typing
- Resize handling when you only care about the final size

```javascript
function debounce(func, delay) {
  let timeoutId;

  return function (...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      func.apply(this, args);
    }, delay);
  };
}

const searchInput = document.querySelector("#search");
const debouncedSearch = debounce(query => {
  console.log("Searching for:", query);
}, 300);

if (searchInput) {
  searchInput.addEventListener("input", () => {
    debouncedSearch(searchInput.value);
  });
}
```

### Throttling

**Throttling** limits a function so it runs at most once during a time window.

Use it for:
- Scroll handlers
- Mouse movement tracking
- Resize handlers that update layout while resizing

```javascript
function throttle(func, limit) {
  let inThrottle = false;

  return function (...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;

      setTimeout(() => {
        inThrottle = false;
      }, limit);
    }
  };
}

const throttledScroll = throttle(() => {
  console.log("Scrolled");
}, 100);

window.addEventListener("scroll", throttledScroll);
```

### Choosing between them

- **Use debounce** when only the final action matters
- **Use throttle** when regular updates matter but full frequency is too expensive

## Common patterns

### Delayed tooltip

```javascript
const element = document.querySelector("#help-icon");
let tooltipTimeoutId = 0;

function showTooltip() {}
function hideTooltip() {}

if (element) {
  element.addEventListener("mouseenter", () => {
    tooltipTimeoutId = setTimeout(() => {
      showTooltip();
    }, 500);
  });

  element.addEventListener("mouseleave", () => {
    clearTimeout(tooltipTimeoutId);
    hideTooltip();
  });
}
```

### Animation loop

```javascript
let animationRunning = false;

function updateAnimation() {}

function animate() {
  if (!animationRunning) {
    return;
  }

  updateAnimation();
  requestAnimationFrame(animate);
}

function startAnimation() {
  if (animationRunning) {
    return;
  }

  animationRunning = true;
  requestAnimationFrame(animate);
}

function stopAnimation() {
  animationRunning = false;
}
```

## Common pitfalls

### Forgetting to clean up timers

```javascript
function updateClock() {}

// Bad: starts a timer and never stops it
const intervalId = setInterval(() => {
  updateClock();
}, 1000);
```

```javascript
function updateClock() {}

// Good: keep the ID so you can stop it later
const intervalId = setInterval(() => {
  updateClock();
}, 1000);

function cleanup() {
  clearInterval(intervalId);
}
```

### Using `setInterval()` for animations

```javascript
function animate() {}

// Less ideal for visual animation
setInterval(() => {
  animate();
}, 16);
```

```javascript
function updateAnimation() {}

// Better for visual animation
function animate() {
  updateAnimation();
  requestAnimationFrame(animate);
}
```

### Starting too many timers

```javascript
const elements = document.querySelectorAll(".item");

function updateElement(element) {
  console.log(element);
}

// Bad: one interval per element
elements.forEach(element => {
  setInterval(() => {
    updateElement(element);
  }, 1000);
});
```

```javascript
const elements = document.querySelectorAll(".item");

function updateElement(element) {
  console.log(element);
}

// Better: one interval updates everything
setInterval(() => {
  elements.forEach(updateElement);
}, 1000);
```

## Summary

- Use `setTimeout()` for one delayed action.
- Use `setInterval()` for repeated work, but remember to stop it when you no longer need it.
- Use `requestAnimationFrame()` for visual animation instead of timer-based loops.
- Use debounce and throttle when repeated events would otherwise run too often.

## Next up

- [How JavaScript Processes Code](./how_js_processes_code)
- [Fetch API](./networking)
- [Web Storage](./browser_storage)
- [Events](../events/dom_events)
