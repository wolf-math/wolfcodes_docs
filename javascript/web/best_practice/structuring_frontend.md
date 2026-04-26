---
title: Structuring Frontend JavaScript
sidebar_position: 13
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

As frontend code grows, structure becomes just as important as correctness. A project with clear files, clear responsibilities, and predictable flow is easier to debug, extend, and keep fast over time.

This page focuses on practical structure patterns for vanilla JavaScript in the browser.

## Why structure matters

Good structure helps you answer questions quickly:

- Where does this data live?
- Which file updates the DOM?
- Where are event listeners set up?
- What is responsible for talking to the server?

If those answers are unclear, even small projects become harder to change safely.

## Start with simple file organization

You do not need a huge architecture for a small app, but you do need clear boundaries.

### A simple project structure

```text
my-app/
  ├── index.html
  ├── css/
  │   └── styles.css
  ├── js/
  │   ├── app.js
  │   ├── utils.js
  │   └── components/
  │       ├── todo.js
  │       └── user.js
  └── assets/
      └── images/
```

This is enough for many small projects.

### Separate by responsibility

As the app grows, clearer splits usually help:

```text
js/
  ├── app.js          # Main application logic
  ├── state.js        # State management
  ├── dom.js          # DOM manipulation
  ├── api.js          # API calls
  └── utils.js        # Utility functions
  ```

This kind of split makes it easier to see what each file is for:

- `app.js`: startup and wiring
- `state.js`: application data
- `dom.js`: rendering and DOM updates
- `api.js`: server communication
- `utils.js`: shared helpers

## Use ES modules in the browser

ES modules let you split code into focused files and import only what you need.

### Basic setup

```html
<script type="module" src="js/app.js"></script>
```

### Small example

```javascript
// utils.js
export function formatCurrency(amount) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD"
  }).format(amount);
}
```

```javascript
// app.js
import { formatCurrency } from "./utils.js";

const price = formatCurrency(100);
console.log(price);
```

## Choose a structure that matches the app

There is no single perfect folder layout. The right structure depends on the project size and how the features relate to each other.

### Structure by technical role

This works well when the app is still small:

```text
js/
  ├── app.js
  ├── state.js
  ├── dom.js
  ├── api.js
  └── utils.js
```

### Structure by feature

This often scales better once the app has several distinct features:



```text
js/
  ├── app.js
  ├── todo/
  |     ├── todo.js
  |     ├── todo-state.js
  |     └── todo-ui.js
  ├── user/
  |     ├── user.js
  |     └── user-api.js
  └── utils/
        └── helpers.js
```

Feature-based structure is often easier when each feature has its own UI, state, and API logic.

:::tip
Rule of thumb: if you keep jumping between many unrelated folders to understand one feature, feature-based structure may be a better fit.
:::

## Separate responsibilities clearly

One of the biggest improvements you can make is to keep data, DOM work, and wiring separate.

### State vs DOM updates

```javascript
// state.js
export const todos = {
  items: [],
  add(text) {
    this.items.push({
      id: Date.now(),
      text,
      completed: false
    });
  },
  toggle(id) {
    const todo = this.items.find(item => item.id === id);
    if (todo) {
      todo.completed = !todo.completed;
    }
  }
};
```

```javascript
// ui.js
import { todos } from "./state.js";

export function renderTodos() {
  const list = document.querySelector("#todo-list");
  if (!list) {
    return;
  }

  list.innerHTML = "";

  todos.items.forEach(todo => {
    const listItem = document.createElement("li");
    listItem.textContent = todo.text;

    if (todo.completed) {
      listItem.classList.add("completed");
    }

    list.appendChild(listItem);
  });
}
```

```javascript
// app.js
import { todos } from "./state.js";
import { renderTodos } from "./ui.js";

const addButton = document.querySelector("#add-btn");

if (addButton) {
  addButton.addEventListener("click", () => {
    todos.add("New todo");
    renderTodos();
  });
}
```

### Events vs business logic

Event handlers should usually gather input and call other functions, not hold all of the application logic themselves.

```javascript
// events.js
import { todos } from "./state.js";
import { renderTodos } from "./ui.js";

export function setupEventListeners() {
  const addButton = document.querySelector("#add-btn");
  const input = document.querySelector("#todo-input");
  const list = document.querySelector("#todo-list");

  if (addButton && input) {
    addButton.addEventListener("click", () => {
      todos.add(input.value);
      input.value = "";
      renderTodos();
    });
  }

  if (list) {
    list.addEventListener("click", event => {
      if (event.target.classList.contains("delete")) {
        const id = Number(event.target.dataset.id);
        todos.remove(id);
        renderTodos();
      }
    });
  }
}
```

## Keep initialization predictable

Every app needs a clear place where setup happens.

### Simple initialization flow

```javascript
function initializeApp() {
  loadInitialState();
  setupEventListeners();
  render();
}

document.addEventListener("DOMContentLoaded", () => {
  initializeApp();
});
```

This works well because the app has one clear entry point.

### Class-based app wrapper

```javascript
class App {
  constructor() {
    this.state = {};
    this.components = {};
  }

  init() {
    this.loadState();
    this.initComponents();
    this.setupEvents();
    this.render();
  }

  loadState() {}
  initComponents() {}
  setupEvents() {}
  render() {}
}

document.addEventListener("DOMContentLoaded", () => {
  const app = new App();
  app.init();
});
```

This is helpful when your app has multiple moving parts that need one owner.

## Use progressive enhancement when possible

A good frontend structure does not assume JavaScript is the only thing making the page usable.

### Start with working HTML

```html
<form action="/api/submit" method="POST">
  <input type="text" name="username" required />
  <button type="submit">Submit</button>
</form>
```

### Add JavaScript enhancements

```javascript
const form = document.querySelector("form");

if (form) {
  form.addEventListener("submit", event => {
    event.preventDefault();
    submitFormWithFeedback(form);
  });
}
```

This approach often improves resilience, accessibility, and long-term maintainability.

## Common patterns

### Component-style classes

```javascript
export class TodoList {
  constructor(container, todos) {
    this.container = container;
    this.todos = todos;
  }

  render() {
    if (!this.container) {
      return;
    }

    this.container.innerHTML = "";

    this.todos.forEach(todo => {
      const item = this.createTodoItem(todo);
      this.container.appendChild(item);
    });
  }

  createTodoItem(todo) {
    const listItem = document.createElement("li");
    listItem.textContent = todo.text;

    if (todo.completed) {
      listItem.classList.add("completed");
    }

    return listItem;
  }
}
```

Use this pattern when one piece of UI has its own rendering behavior and internal logic.

### Service-style classes

```javascript
export class ApiService {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }

  async get(endpoint) {
    const response = await fetch(`${this.baseUrl}${endpoint}`);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    return response.json();
  }

  async post(endpoint, data) {
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    return response.json();
  }
}
```

Use this pattern when you want network logic in one clear place instead of spreading `fetch()` calls across the app.

## Practical best practices

### Give each file one main responsibility

```javascript
// Good
// utils/formatting.js
export function formatCurrency() {}
export function formatDate() {}
```

```javascript
// Harder to maintain
// utils.js
export function formatCurrency() {}
export function formatDate() {}
export function apiCall() {}
export function domManipulation() {}
```

### Use descriptive file names

```text
todo-manager.js
user-service.js
form-validator.js
```

Avoid vague names like `stuff.js` or giant catch-all files like `utils.js` when the project grows.

### Export only what should be public

```javascript
export function publicFunction() {}
export const publicConstant = 123;

function privateFunction() {}
```

### Keep dependencies obvious

```javascript
import { formatCurrency } from "./utils/formatting.js";
import { ApiService } from "./services/api.js";
```

This is easier to follow than broad imports that hide where things come from.

## Summary

- Good structure makes frontend code easier to understand, change, and debug.
- Separate state, DOM updates, events, and API work so each part has a clearer role.
- Use modules and file organization that match the size and shape of the app.
- Favor predictable initialization and simple boundaries over clever architecture.

## Next steps

Once your code is structured well, the next skill is finding problems quickly. Continue with [Debugging Frontend JavaScript](./debugging_frontend).
