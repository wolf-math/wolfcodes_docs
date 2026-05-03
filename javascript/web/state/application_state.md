---
title: Application State in the Browser
sidebar_position: 8
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is application state?

**Application state** is the data that represents your app's current condition. It is what your app "remembers" while the user interacts with it.

Examples of state:
- Shopping cart items
- The current page in a paginated list
- Whether a modal is open
- Form values before submission
- Whether a user is logged in

### Smallest working example

```html
<p id="count">0</p>
<button id="increment">Increment</button>
```

```javascript
let count = 0;

const countElement = document.querySelector("#count");
const incrementButton = document.querySelector("#increment");

function render() {
  if (countElement) {
    countElement.textContent = `${count}`;
  }
}

if (incrementButton) {
  incrementButton.addEventListener("click", () => {
    count += 1;
    render();
  });
}

render();
```

## Why this matters

State gives your UI something reliable to display and update:

- It keeps track of what the user has done
- It lets the DOM reflect the current app condition
- It helps avoid bugs caused by scattered or duplicated data

This idea connects directly to [manipulating the DOM](../dom/manipulating_dom), [handling events](../events/dom_events), and [structuring frontend code](../best_practice/structuring_frontend).

## State vs the DOM

This is the key distinction:

- **State**: data in JavaScript variables, arrays, and objects
- **DOM**: the HTML elements the user sees

**The DOM should reflect state, not be the source of truth.**

### The wrong way

```javascript
function getCartItems() {
  const items = [];

  document.querySelectorAll(".cart-item").forEach(item => {
    items.push(item.textContent ?? "");
  });

  return items;
}
```

The problem is that the app has to read the UI to figure out its own data. That is fragile and easy to break.

### The right way

```javascript
const cartState = [];

function addToCart(item) {
  cartState.push(item);
  renderCart();
}

function renderCart() {
  const cartList = document.querySelector("#cart");
  if (!cartList) {
    return;
  }

  cartList.innerHTML = "";

  cartState.forEach(item => {
    const listItem = document.createElement("li");
    listItem.textContent = item;
    cartList.appendChild(listItem);
  });
}
```

## Keeping state in JavaScript

Store state in JavaScript variables:

```javascript
let count = 0;
let isModalOpen = false;
let currentUser = null;

const appState = {
  user: {
    name: "Alice",
    isLoggedIn: true
  },
  cart: {
    items: [],
    total: 0
  },
  settings: {
    theme: "light",
    language: "en"
  }
};
```

### State object pattern

Related state often fits best in one object:

```javascript
const state = {
  todos: [],
  filter: "all",
  inputValue: ""
};

function addTodo(text) {
  state.todos.push({
    id: Date.now(),
    text,
    completed: false
  });
}

function toggleTodo(id) {
  const todo = state.todos.find(item => item.id === id);
  if (todo) {
    todo.completed = !todo.completed;
  }
}
```

:::tip
Rule of thumb: keep one clear source of truth for each piece of data. If you have to wonder which value is the "real" one, your state is probably split in the wrong place.
:::

## Syncing state to the DOM

When state changes, update the DOM to match it. That usually means combining state updates with [rendering code](../dom/manipulating_dom) and event handlers from [the events section](../events/dom_events).

```javascript
let count = 0;

const countElement = document.querySelector("#counter");
const incrementButton = document.querySelector("#increment-btn");

function increment() {
  count += 1;
  render();
}

function render() {
  if (countElement) {
    countElement.textContent = `${count}`;
  }

  if (incrementButton) {
    incrementButton.disabled = count >= 10;
  }
}
```

### Single source of truth

Always update state first, then render:

```javascript
const items = [];

function addItem(name) {
  items.push(name);
  renderItems();
}

function renderItems() {
  const list = document.querySelector("#items");
  if (!list) {
    return;
  }

  list.innerHTML = "";

  items.forEach(item => {
    const listItem = document.createElement("li");
    listItem.textContent = item;
    list.appendChild(listItem);
  });
}
```

## Common state bugs

### State and DOM get out of sync

```javascript
// Bad: DOM changed, state did not
function addItem() {
  const list = document.querySelector("#list");
  if (!list) {
    return;
  }

  const listItem = document.createElement("li");
  listItem.textContent = "New item";
  list.appendChild(listItem);
}

// Good: state changes first, then UI updates
const items = [];

function addItem() {
  items.push("New item");
  renderItems();
}
```

### Reading from the DOM instead of state

```javascript
// Bad
function getItemCount() {
  return document.querySelectorAll(".item").length;
}

// Good
function getItemCount() {
  return items.length;
}
```

### Multiple sources of truth

```javascript
// Bad
let count1 = 0;
let count2 = 0;

// Good
const state = {
  counter: 0
};
```

### Forgetting to re-render

```javascript
// Bad
function updateCount() {
  count = 10;
}

// Good
function updateCount() {
  count = 10;
  render();
}
```

## Common patterns

### Simple state plus render

For smaller apps, a state variable plus one render function works well:

```javascript
const state = {
  todos: [],
  filter: "all"
};

function render() {
  const list = document.querySelector("#todo-list");
  if (!list) {
    return;
  }

  const visibleTodos =
    state.filter === "all"
      ? state.todos
      : state.todos.filter(todo =>
          state.filter === "active" ? !todo.completed : todo.completed
        );

  list.innerHTML = "";

  visibleTodos.forEach(todo => {
    const listItem = document.createElement("li");
    listItem.textContent = todo.text;

    if (todo.completed) {
      listItem.classList.add("completed");
    }

    list.appendChild(listItem);
  });
}

function addTodo(text) {
  state.todos.push({ id: Date.now(), text, completed: false });
  render();
}

function toggleTodo(id) {
  const todo = state.todos.find(item => item.id === id);
  if (todo) {
    todo.completed = !todo.completed;
    render();
  }
}
```

### Event-driven updates

Another common pattern is to keep state and render logic together:

```javascript
const app = {
  state: {
    count: 0
  },

  increment() {
    this.state.count += 1;
    this.render();
  },

  decrement() {
    this.state.count -= 1;
    this.render();
  },

  render() {
    const countElement = document.querySelector("#count");
    if (countElement) {
      countElement.textContent = `${this.state.count}`;
    }
  }
};

const incrementButton = document.querySelector("#increment");

if (incrementButton) {
  incrementButton.addEventListener("click", () => {
    app.increment();
  });
}
```

## Example: todo app state

Here is a slightly larger example that keeps todo data in state and renders the UI from that state.

```javascript
const todoState = {
  items: [],
  nextId: 1
};

function addTodo(text) {
  todoState.items.push({
    id: todoState.nextId,
    text,
    completed: false
  });

  todoState.nextId += 1;
  renderTodos();
}

function toggleTodo(id) {
  const todo = todoState.items.find(item => item.id === id);
  if (todo) {
    todo.completed = !todo.completed;
    renderTodos();
  }
}

function deleteTodo(id) {
  todoState.items = todoState.items.filter(item => item.id !== id);
  renderTodos();
}

function renderTodos() {
  const list = document.querySelector("#todo-list");
  const countElement = document.querySelector("#count");

  if (!list || !countElement) {
    return;
  }

  list.innerHTML = "";

  todoState.items.forEach(todo => {
    const listItem = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = todo.completed;
    checkbox.addEventListener("change", () => {
      toggleTodo(todo.id);
    });

    const label = document.createElement("span");
    label.textContent = todo.text;
    if (todo.completed) {
      label.classList.add("completed");
    }

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", () => {
      deleteTodo(todo.id);
    });

    listItem.appendChild(checkbox);
    listItem.appendChild(label);
    listItem.appendChild(deleteButton);
    list.appendChild(listItem);
  });

  const remainingCount = todoState.items.filter(item => !item.completed).length;
  countElement.textContent =
    `${remainingCount} item${remainingCount !== 1 ? "s" : ""} remaining`;
}
```

:::note
This example uses a full re-render after each change because it is simple and easy to reason about. For small apps, that tradeoff is often worth it.
:::

## Choosing where state should live

- **Use plain JavaScript variables or objects** when the app is small and the state is local
- **Use `localStorage`** when you need state to survive page refreshes
- **Use a framework or state library** when the UI becomes large and many parts of the app share the same data

Learn more about persistence in the [Web Storage guide](../web_api/browser_storage).

If state starts to feel scattered across too many files, [Structuring Frontend JavaScript](../best_practice/structuring_frontend) is the next helpful page.

## Summary

- Application state is the data that describes what your app currently knows.
- Keep state in JavaScript, not in the DOM.
- Update state first, then render the DOM from that state.
- One source of truth is safer and easier to debug than duplicated or scattered values.

## Next up

- [Web Storage](../web_api/browser_storage)
- [Events](../events/dom_events)
- [Manipulating the DOM](../dom/manipulating_dom)
